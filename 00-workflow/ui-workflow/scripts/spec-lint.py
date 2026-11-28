#!/usr/bin/env python3
"""Lightweight deterministic linter for UI-DESIGN-SPEC.md.

Zero third-party dependencies. Validates:
  - Required core sections (Style Kernel, Style Grammar, Canonical Components, Creative Field)
  - Embedded JSON manifest between <!-- MANIFEST_START --> and <!-- MANIFEST_END -->
  - Closed-set style unity locks (boundary_philosophy, L0-L3 containment_topology, selection_grammar)
  - Visual & entropy budgets (non-pill radii <= 4, selection recipes <= 2)
  - Component reuse_policy (exact / adapt / exemplar)
  - Constraint overload (>40% hard facts, local+hard in extension mode, Generated promoted to style)
  - Unknown font contradiction

Usage:
  python3 -I spec-lint.py <UI-DESIGN-SPEC.md>
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REQUIRED_HEADINGS = [
    "Style Kernel",
    "Style Grammar",
    "Canonical Components",
    "Creative Field",
]
VALID_BOUNDARIES = {"hairline-embedded", "tonal-layered", "bordered-card"}
REQUIRED_SLOTS = ("L0_shell", "L1_section", "L2_item", "L3_overlay")
VALID_REUSE = {"exact", "adapt", "exemplar"}


def extract_manifest(text: str):
    m = re.search(
        r"<!--\s*MANIFEST_START\s*-->\s*```json\s*(.*?)\s*```\s*<!--\s*MANIFEST_END\s*-->",
        text,
        flags=re.S | re.I,
    )
    if not m:
        return None, "missing machine-readable JSON manifest block (<!-- MANIFEST_START --> ... <!-- MANIFEST_END -->)"
    try:
        return json.loads(m.group(1)), None
    except json.JSONDecodeError as e:
        return None, f"manifest JSON invalid: {e}"


def section_body(text: str, heading: str) -> str:
    pattern = rf"(?ms)^##\s+\d*\.?\s*{re.escape(heading)}[^\n]*$\n(.*?)(?=^##\s+|\Z)"
    m = re.search(pattern, text)
    return m.group(1) if m else ""


def bullet_count(body: str) -> int:
    return len(re.findall(r"(?m)^\s*[-*]\s+\S", body))


def main(path: str) -> int:
    p = Path(path)
    if not p.is_file():
        print(f"ERROR: file not found: {p}", file=sys.stderr)
        return 2
    text = p.read_text(encoding="utf-8")
    errors: list[str] = []
    warnings: list[str] = []

    for h in REQUIRED_HEADINGS:
        if not re.search(rf"(?mi)^##\s+\d*\.?\s*{re.escape(h)}\b", text):
            errors.append(f"missing required section: {h}")

    kernel_body = section_body(text, "Style Kernel")
    kc = bullet_count(kernel_body)
    if kc and kc < 3:
        warnings.append(f"Style Kernel has only {kc} bullet(s); verify visual identity is sufficiently anchored")
    if kc > 12:
        warnings.append(f"Style Kernel has {kc} bullets (>12); likely over-constrained")

    manifest, manifest_err = extract_manifest(text)
    if manifest_err:
        errors.append(manifest_err)
    else:
        for key in ("meta", "kernel", "grammar", "visual", "budgets", "components", "creative_field"):
            if key not in manifest:
                errors.append(f"manifest missing required key: {key}")

        mode = (manifest.get("meta") or {}).get("mode", "extension")
        grammar = manifest.get("grammar") or {}
        bp = grammar.get("boundary_philosophy")
        if bp not in VALID_BOUNDARIES:
            errors.append(f"grammar.boundary_philosophy must be one of {sorted(VALID_BOUNDARIES)}, got: {bp!r}")

        topo = grammar.get("containment_topology") or {}
        missing_slots = [s for s in REQUIRED_SLOTS if not topo.get(s)]
        if missing_slots:
            errors.append(f"grammar.containment_topology missing slot(s): {', '.join(missing_slots)}")

        sel = grammar.get("selection_grammar") or {}
        sel_recipes = sel.get("recipes") or {}
        sel_bindings = sel.get("bindings") or {}
        budgets = manifest.get("budgets") or {}
        max_sel = int(budgets.get("max_selection_grammars", 2))
        if max_sel > 2:
            warnings.append(f"budgets.max_selection_grammars={max_sel} > 2; risk of selection dialect drift")
        if not sel_recipes:
            errors.append("grammar.selection_grammar.recipes is empty")
        elif len(sel_recipes) > max_sel:
            errors.append(f"selection_grammar has {len(sel_recipes)} recipes > max {max_sel}")
        if not sel_bindings:
            errors.append("grammar.selection_grammar.bindings is empty (must bind semantic roles 1:1)")
        else:
            for role, target in sel_bindings.items():
                if target not in sel_recipes:
                    errors.append(f"selection binding '{role}' -> '{target}' not defined in selection_grammar.recipes")

        if not grammar.get("primitive_paths"):
            warnings.append("grammar.primitive_paths is empty; page-layer visual-quintuple audit cannot enforce boundaries")

        visual = manifest.get("visual") or {}
        radii = [float(r) for r in (visual.get("radius") or [])]
        non_pill = [r for r in radii if 0 < r < 900]
        max_r = int(budgets.get("max_distinct_non_pill_radius", 4))
        if len(non_pill) > max_r:
            errors.append(f"visual.radius has {len(non_pill)} non-zero/non-pill values {non_pill} > max {max_r}")

        comps = manifest.get("components") or {}
        if not comps:
            warnings.append("manifest.components is empty; declare Canonical Shell & Components")
        for cid, comp in comps.items():
            if not isinstance(comp, dict):
                continue
            rp = comp.get("reuse_policy")
            if rp not in VALID_REUSE:
                errors.append(f"component '{cid}' must specify reuse_policy in {sorted(VALID_REUSE)}, got: {rp!r}")

        facts = manifest.get("facts") or {}
        if isinstance(facts, dict) and facts:
            constraints = []
            for fid, fobj in facts.items():
                if not isinstance(fobj, dict):
                    continue
                strength = fobj.get("constraint_strength")
                scope = fobj.get("transfer_scope")
                if strength:
                    constraints.append((fid, strength, scope))
                if fobj.get("provenance") == "Generated" and fobj.get("stability_scope") == "style":
                    warnings.append(f"Generated fact '{fid}' promoted to global style scope; verify justification")
                if mode == "extension" and strength == "hard" and scope == "local":
                    warnings.append(f"local fact '{fid}' marked hard in extension mode")
            hard = [c for c in constraints if c[1] == "hard"]
            if len(constraints) >= 5 and len(hard) / len(constraints) > 0.4:
                warnings.append(f"hard facts ratio {len(hard)}/{len(constraints)} (>40%); verify spec is not over-constrained")

    if re.search(r"(?i)font-family\s*[:=]\s*['\"]?(?:Inter|SF Pro|Roboto)", text) and re.search(
        r"(?i)font[^\n]*Unknown", text
    ):
        warnings.append("spec marks font as Unknown while also specifying a common concrete font-family")

    print(f"Spec lint: {p}")
    for e in errors:
        print(f"ERROR: {e}")
    for w in warnings:
        print(f"WARN:  {w}")
    if not errors and not warnings:
        print("OK: spec structure, closed grammar locks, and manifest valid")
    elif not errors:
        print(f"OK with {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: spec-lint.py <UI-DESIGN-SPEC.md>", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))
