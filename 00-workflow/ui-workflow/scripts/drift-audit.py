#!/usr/bin/env python3
"""UI static drift & layered style-grammar audit.

Zero third-party dependencies. Backward-compatible with basic px scale checks,
and supports full manifest-driven governance:
  - spacing / radius px (+ optional utility class) scale & distinct radius budget
  - raw color escape outside token/primitive files
  - border / box-shadow / font-size entropy budgets + zero-offset glow detection
  - page-layer Visual Quintuple ban outside --primitive-paths (with /* ui-exception: */ escape)
  - selection rule-block fingerprinting (<= max_selection_grammars) + selection font-weight reflow
  - transition: all detection

Usage:
  python3 -I drift-audit.py <path...> [--manifest UI-DESIGN-SPEC.md] [--primitive-paths dir1,dir2]
                            [--spacing 0,4,8,12,16,24,32,48] [--radius 0,6,8,12,999]
                            [--max-distinct-radius 4] [--scan-utilities] [--check-entropy]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

SPACING_PROPS = r"(?:gap|row-gap|column-gap|padding(?:-[a-z]+)?|margin(?:-[a-z]+)?|rowGap|columnGap|padding[A-Z][a-z]+|margin[A-Z][a-z]+)"
RADIUS_PROPS = r"(?:border-radius|border-[a-z]+-[a-z]+-radius|borderRadius)"
DECL = re.compile(r"(?P<prop>" + SPACING_PROPS + "|" + RADIUS_PROPS + r")\s*:\s*(?P<val>[^;}\n]+)")
PX = re.compile(r"(?<![\w.-])(-?\d+(?:\.\d+)?)px")
RADIUS_RE = re.compile(RADIUS_PROPS)

BORDER_DECL = re.compile(r"\bborder(?:-(?:top|right|bottom|left))?\s*:\s*([^;}\n]+)")
SHADOW_DECL = re.compile(r"\bbox-shadow\s*:\s*([^;}\n]+)")
FONTSIZE_DECL = re.compile(r"\b(?:font-size|fontSize)\s*:\s*([^;}\n]+)")
TRANSITION_ALL = re.compile(r"\btransition\s*:\s*[^;}\n]*\ball\b", re.I)
RAW_COLOR = re.compile(r"(?:#[0-9a-fA-F]{3,8}\b|\b(?:rgba?|hsla?|oklch)\s*\([^)]+\))")
ZERO_GLOW = re.compile(r"(?:^|,)\s*0(?:px)?\s+0(?:px)?\s+([1-9]\d*(?:\.\d+)?)px")
EXCEPTION_MARK = re.compile(r"ui-exception\s*:", re.I)

# Utility-class mappers (optional --scan-utilities)
UTIL_SPACING = re.compile(
    r"\b(?:p|px|py|pt|pr|pb|pl|m|mx|my|mt|mr|mb|ml|gap|gap-x|gap-y)-(\d+(?:\.\d+)?|\[\d+(?:\.\d+)?px\])\b"
)
UTIL_RADIUS_NAMED = {
    "none": 0.0,
    "xs": 2.0,
    "sm": 4.0,
    "DEFAULT": 4.0,
    "md": 6.0,
    "lg": 8.0,
    "xl": 12.0,
    "2xl": 16.0,
    "3xl": 24.0,
    "full": 999.0,
}
UTIL_RADIUS = re.compile(r"\brounded(?:-(?:none|xs|sm|md|lg|xl|2xl|3xl|full|\[\d+(?:\.\d+)?px\]))?\b")
UTIL_QUINTUPLE_BG = re.compile(r"\bbg-(?:\[|[a-z]+-\d{2,3}\b)")
UTIL_QUINTUPLE_BORDER = re.compile(r"\bborder(?:-(?:0|2|4|8|\[|[a-z]+-\d{2,3}))?\b")
UTIL_QUINTUPLE_SHADOW = re.compile(r"\bshadow(?:-(?:sm|md|lg|xl|2xl|\[))?\b")

CSS_RULE_BLOCK = re.compile(r"([^{}@][^{}]*)\{([^{}]+)\}", re.S)
SELECTION_SELECTOR = re.compile(
    r"(?:\.active\b|\.selected\b|:checked\b|aria-selected|aria-current|data-selected|data-active|data-state\s*=\s*['\"]?(?:active|on|checked))",
    re.I,
)


def parse_scale(s: str) -> set[float]:
    return {float(x) for x in s.split(",") if x.strip()}


def load_manifest(spec_path: str) -> dict:
    text = Path(spec_path).read_text(encoding="utf-8", errors="ignore")
    m = re.search(
        r"<!--\s*MANIFEST_START\s*-->\s*```json\s*(.*?)\s*```\s*<!--\s*MANIFEST_END\s*-->",
        text,
        flags=re.S | re.I,
    )
    if not m:
        raise SystemExit(f"ERROR: manifest block not found in {spec_path}")
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError as e:
        raise SystemExit(f"ERROR: invalid manifest JSON in {spec_path}: {e}")


def iter_files(paths: list[str], exts: set[str]):
    for p in paths:
        if os.path.isfile(p):
            yield p
            continue
        for root, dirs, names in os.walk(p):
            dirs[:] = [d for d in dirs if d not in ("node_modules", "dist", "out", "build", ".git", "__pycache__")]
            for n in sorted(names):
                if os.path.splitext(n)[1] in exts:
                    yield os.path.join(root, n)


def is_in_primitives(filepath: str, prim_prefixes: list[str]) -> bool:
    if not prim_prefixes:
        return False
    norm = os.path.normpath(filepath).replace("\\", "/")
    for pref in prim_prefixes:
        p = os.path.normpath(pref).replace("\\", "/").rstrip("/")
        if norm == p or norm.startswith(p + "/") or ("/" + p + "/") in ("/" + norm + "/") or norm.endswith("/" + p):
            return True
    return False


def is_token_file(filepath: str) -> bool:
    base = os.path.basename(filepath).lower()
    return any(k in base for k in ("token", "theme", "palette", "variables"))


def normalize_decl_val(val: str) -> str:
    return re.sub(r"\s+", " ", val.strip().strip("'\"")).lower()


def main() -> int:
    ap = argparse.ArgumentParser(description="UI static drift & style-grammar audit")
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--manifest", help="Path to UI-DESIGN-SPEC.md containing JSON manifest")
    ap.add_argument("--primitive-paths", default="", help="Comma-separated allowed primitive dirs/files")
    ap.add_argument("--spacing", default=None)
    ap.add_argument("--radius", default=None)
    ap.add_argument("--ext", default=".css,.scss,.less,.tsx,.jsx,.vue")
    ap.add_argument("--max-distinct-radius", type=int, default=None)
    ap.add_argument("--scan-utilities", action="store_true", help="Scan utility classes for spacing/radius/quintuple")
    ap.add_argument("--check-entropy", action="store_true", help="Enable border/shadow/font/color/selection entropy checks")
    ap.add_argument("--show", type=int, default=3)
    a = ap.parse_args()

    manifest = load_manifest(a.manifest) if a.manifest else {}
    m_visual = manifest.get("visual") or {}
    m_grammar = manifest.get("grammar") or {}
    m_budgets = manifest.get("budgets") or {}

    spacing_allowed = (
        parse_scale(a.spacing)
        if a.spacing is not None
        else ({float(x) for x in m_visual["spacing"]} if "spacing" in m_visual else parse_scale("0,4,8,12,16,24,32,48"))
    )
    radius_allowed = (
        parse_scale(a.radius)
        if a.radius is not None
        else ({float(x) for x in m_visual["radius"]} if "radius" in m_visual else parse_scale("0,6,8,12,999"))
    )
    max_distinct_radius = (
        a.max_distinct_radius
        if a.max_distinct_radius is not None
        else int(m_budgets.get("max_distinct_non_pill_radius", 4))
    )

    prim_paths: list[str] = []
    if a.primitive_paths:
        prim_paths = [p.strip() for p in a.primitive_paths.split(",") if p.strip()]
    elif m_grammar.get("primitive_paths"):
        prim_paths = list(m_grammar["primitive_paths"])

    entropy_on = bool(a.check_entropy or a.manifest)
    max_border_styles = int(m_budgets.get("max_border_styles", 2))
    max_shadow_levels = int(m_budgets.get("max_shadow_levels", 2))
    max_font_sizes = int(m_budgets.get("max_font_sizes", 6))
    max_selection_grammars = int(m_budgets.get("max_selection_grammars", 2))
    max_ad_hoc_exceptions = int(m_budgets.get("max_ad_hoc_exceptions", 0))

    allowed = {"spacing": spacing_allowed, "radius": radius_allowed}
    exts = set(a.ext.split(","))
    total = {"spacing": 0, "radius": 0}
    distinct = {"spacing": set(), "radius": set()}
    off = {"spacing": defaultdict(list), "radius": defaultdict(list)}

    borders: dict[str, list[str]] = defaultdict(list)
    shadows: dict[str, list[str]] = defaultdict(list)
    font_sizes: dict[str, list[str]] = defaultdict(list)
    raw_colors: list[str] = []
    zero_glows: list[str] = []
    transition_alls: list[str] = []
    ad_hoc_violations: list[str] = []
    ad_hoc_exceptions: list[str] = []
    selection_fingerprints: dict[tuple[str, ...], list[str]] = defaultdict(list)
    selection_reflows: list[str] = []

    for f in iter_files(a.paths, exts):
        in_prim = is_in_primitives(f, prim_paths)
        tok_file = is_token_file(f)
        content = Path(f).read_text(encoding="utf-8", errors="ignore")
        lines = content.splitlines()

        for ln, line in enumerate(lines, 1):
            prev_line = lines[ln - 2] if ln >= 2 else ""
            has_exc = bool(EXCEPTION_MARK.search(line) or EXCEPTION_MARK.search(prev_line))

            # 1. CSS spacing / radius px literals
            for m in DECL.finditer(line):
                kind = "radius" if RADIUS_RE.fullmatch(m.group("prop")) else "spacing"
                for v in PX.findall(m.group("val")):
                    total[kind] += 1
                    n = abs(float(v))
                    distinct[kind].add(n)
                    if n not in allowed[kind]:
                        off[kind][n].append(f"{f}:{ln}")

            # 2. Optional utility-class scanning
            if a.scan_utilities:
                for m in UTIL_SPACING.finditer(line):
                    raw = m.group(1)
                    n = float(raw[1:-3]) if raw.startswith("[") else float(raw) * 4.0
                    total["spacing"] += 1
                    distinct["spacing"].add(n)
                    if n not in allowed["spacing"]:
                        off["spacing"][n].append(f"{f}:{ln}")
                for m in UTIL_RADIUS.finditer(line):
                    tok = m.group(0)
                    suffix = tok[len("rounded") :].lstrip("-") or "DEFAULT"
                    if suffix.startswith("["):
                        n = float(suffix[1:-3])
                    else:
                        n = UTIL_RADIUS_NAMED.get(suffix, None)
                    if n is not None:
                        total["radius"] += 1
                        distinct["radius"].add(n)
                        if n not in allowed["radius"]:
                            off["radius"][n].append(f"{f}:{ln}")

            # 3. transition: all
            if entropy_on and TRANSITION_ALL.search(line):
                transition_alls.append(f"{f}:{ln}")

            # 4. Entropy checks (border / shadow / font-size / raw colors)
            if entropy_on:
                for m in BORDER_DECL.finditer(line):
                    val = normalize_decl_val(m.group(1))
                    if val not in ("0", "none", "0px", "inherit", "transparent"):
                        borders[val].append(f"{f}:{ln}")
                for m in SHADOW_DECL.finditer(line):
                    val = normalize_decl_val(m.group(1))
                    if val not in ("none", "0", "inherit"):
                        shadows[val].append(f"{f}:{ln}")
                        if ZERO_GLOW.search(val) and "inset" not in val:
                            zero_glows.append(f"{f}:{ln}")
                for m in FONTSIZE_DECL.finditer(line):
                    val = normalize_decl_val(m.group(1))
                    if val and not val.startswith("var("):
                        font_sizes[val].append(f"{f}:{ln}")
                if not tok_file and not in_prim and not has_exc:
                    if RAW_COLOR.search(line) and "--" not in line.split(":")[0]:
                        raw_colors.append(f"{f}:{ln}")

            # 5. Page-layer Visual Quintuple Ban (only when --primitive-paths provided)
            if prim_paths and not in_prim and not tok_file:
                css_quintuple = bool(
                    BORDER_DECL.search(line)
                    or RADIUS_RE.search(line)
                    or SHADOW_DECL.search(line)
                )
                util_hits = 0
                if a.scan_utilities:
                    util_hits = sum(
                        1
                        for rx in (UTIL_QUINTUPLE_BG, UTIL_QUINTUPLE_BORDER, UTIL_RADIUS, UTIL_QUINTUPLE_SHADOW)
                        if rx.search(line)
                    )
                if css_quintuple or util_hits >= 2:
                    if has_exc:
                        ad_hoc_exceptions.append(f"{f}:{ln}")
                    else:
                        ad_hoc_violations.append(f"{f}:{ln}")

        # 6. Selection rule-block fingerprinting (CSS-like files)
        if entropy_on and os.path.splitext(f)[1] in (".css", ".scss", ".less"):
            for m in CSS_RULE_BLOCK.finditer(content):
                sel, body = m.group(1).strip(), m.group(2)
                if not SELECTION_SELECTOR.search(sel):
                    continue
                props = set()
                has_reflow = False
                for decl_line in body.split(";"):
                    if ":" not in decl_line:
                        continue
                    prop = decl_line.split(":", 1)[0].strip().lower()
                    if prop in (
                        "background",
                        "background-color",
                        "color",
                        "border",
                        "border-color",
                        "border-bottom",
                        "border-left",
                        "box-shadow",
                        "outline",
                    ):
                        props.add("background" if prop == "background-color" else prop)
                    if prop in ("font-weight", "border-width", "border-left-width", "border-bottom-width"):
                        has_reflow = True
                if props:
                    ln_num = content[: m.start()].count("\n") + 1
                    selection_fingerprints[tuple(sorted(props))].append(f"{f}:{ln_num} ({sel.splitlines()[-1].strip()[:40]})")
                if has_reflow:
                    ln_num = content[: m.start()].count("\n") + 1
                    selection_reflows.append(f"{f}:{ln_num} ({sel.splitlines()[-1].strip()[:40]})")

    bad = 0
    for kind in ("spacing", "radius"):
        count = sum(len(v) for v in off[kind].values())
        bad += count
        pct = (count / total[kind] * 100) if total[kind] else 0
        print(
            f"[{kind}] scale={sorted(allowed[kind])}  literals={total[kind]}  distinct={len(distinct[kind])}  off-scale={count} ({pct:.0f}%)"
        )
        for val, locs in sorted(off[kind].items(), key=lambda kv: -len(kv[1])):
            more = f" …+{len(locs) - a.show}" if len(locs) > a.show else ""
            print(f"  {val:g}px ×{len(locs)}  " + ", ".join(locs[: a.show]) + more)

    non_pill_radii = sorted(r for r in distinct["radius"] if 0 < r < 900)
    if len(non_pill_radii) > max_distinct_radius:
        bad += 1
        print(f"[radius-budget] FAIL: {len(non_pill_radii)} distinct non-zero/non-pill radii {non_pill_radii} > max {max_distinct_radius}")

    if entropy_on:
        print(
            f"[entropy] borders={len(borders)}/{max_border_styles}  shadows={len(shadows)}/{max_shadow_levels}  "
            f"font-sizes={len(font_sizes)}/{max_font_sizes}  selection-recipes={len(selection_fingerprints)}/{max_selection_grammars}  "
            f"raw-colors={len(raw_colors)}  transition-all={len(transition_alls)}"
        )
        if len(borders) > max_border_styles:
            bad += 1
            print(f"[border-budget] FAIL: {len(borders)} distinct border styles > max {max_border_styles}: {list(borders)[:5]}")
        if len(shadows) > max_shadow_levels:
            bad += 1
            print(f"[shadow-budget] FAIL: {len(shadows)} distinct box-shadow levels > max {max_shadow_levels}")
        if zero_glows:
            bad += 1
            print(f"[zero-offset-glow] FAIL: {len(zero_glows)} hit(s)  " + ", ".join(zero_glows[: a.show]))
        if len(font_sizes) > max_font_sizes:
            bad += 1
            print(f"[font-size-budget] FAIL: {len(font_sizes)} distinct font-sizes > max {max_font_sizes}: {sorted(font_sizes)[:8]}")
        if raw_colors:
            bad += 1
            print(f"[raw-color] FAIL: {len(raw_colors)} raw color escape(s) outside token/primitive files  " + ", ".join(raw_colors[: a.show]))
        if transition_alls:
            bad += 1
            print(f"[transition-all] FAIL: {len(transition_alls)} hit(s)  " + ", ".join(transition_alls[: a.show]))
        if len(selection_fingerprints) > max_selection_grammars:
            bad += 1
            print(f"[selection-grammar] FAIL: {len(selection_fingerprints)} distinct selection recipes > max {max_selection_grammars}")
            for fp, locs in selection_fingerprints.items():
                print(f"  recipe={list(fp)}  " + ", ".join(locs[: a.show]))
        if selection_reflows:
            bad += 1
            print(f"[selection-reflow] FAIL: font-weight/border-width changed in selection rule  " + ", ".join(selection_reflows[: a.show]))

    if prim_paths:
        if ad_hoc_violations:
            bad += len(ad_hoc_violations)
            print(f"[ad-hoc-style] FAIL: {len(ad_hoc_violations)} visual-quintuple write(s) outside primitive_paths  " + ", ".join(ad_hoc_violations[: a.show]))
        if len(ad_hoc_exceptions) > max_ad_hoc_exceptions:
            bad += 1
            print(f"[ad-hoc-exceptions] FAIL: {len(ad_hoc_exceptions)} ui-exception(s) > max {max_ad_hoc_exceptions}")
        elif not ad_hoc_violations:
            print(f"[layer-boundary] PASS: 0 ad-hoc visual-quintuple writes outside primitive_paths (exceptions={len(ad_hoc_exceptions)}/{max_ad_hoc_exceptions})")

    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
