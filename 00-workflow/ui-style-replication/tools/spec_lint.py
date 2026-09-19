#!/usr/bin/env python3
"""Lightweight linter for DESIGN-LANGUAGE-SPEC.md.

No third-party dependencies. It checks structure, manifest validity, Kernel size,
and obvious constraint-overload patterns. It is intentionally conservative:
visual judgment remains the model's job.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REQUIRED_HEADINGS = [
    "Style Kernel",
    "Style Grammar",
    "Creative Field",
    "Canonical Components",
]


def extract_manifest(text: str):
    m = re.search(
        r"<!--\s*MANIFEST_START\s*-->\s*```json\s*(.*?)\s*```\s*<!--\s*MANIFEST_END\s*-->",
        text,
        flags=re.S | re.I,
    )
    if not m:
        return None, "machine-readable manifest block not found"
    try:
        return json.loads(m.group(1)), None
    except json.JSONDecodeError as e:
        return None, f"manifest JSON invalid: {e}"


def section(text: str, heading: str) -> str:
    pattern = rf"(?ms)^##\s+\d*\.?\s*{re.escape(heading)}\s*$\n(.*?)(?=^##\s+|\Z)"
    m = re.search(pattern, text)
    return m.group(1) if m else ""


def bullet_count(body: str) -> int:
    return len(re.findall(r"(?m)^\s*[-*]\s+\S", body))


def main(path: str) -> int:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    errors = []
    warnings = []

    for h in REQUIRED_HEADINGS:
        if not re.search(rf"(?mi)^##\s+\d*\.?\s*{re.escape(h)}\s*$", text):
            errors.append(f"missing required section: {h}")

    kernel = section(text, "Style Kernel")
    kc = bullet_count(kernel)
    if kc and kc < 3:
        warnings.append(f"Style Kernel has only {kc} bullet(s); verify identity is sufficiently specified")
    if kc > 12:
        warnings.append(f"Style Kernel has {kc} bullets; likely over-constrained (target usually 5–12)")

    manifest, manifest_error = extract_manifest(text)
    if manifest_error:
        errors.append(manifest_error)
    else:
        for key in ["meta", "kernel", "grammar", "creative_field", "facts", "components"]:
            if key not in manifest:
                errors.append(f"manifest missing key: {key}")

        constraints = []
        for fact_id, fact in (manifest.get("facts") or {}).items():
            if isinstance(fact, dict):
                strength = fact.get("constraint_strength")
                scope = fact.get("transfer_scope")
                if strength:
                    constraints.append((fact_id, strength, scope))
                if fact.get("provenance") == "Generated" and fact.get("stability_scope") == "style":
                    warnings.append(f"Generated fact promoted to style scope: {fact_id}; verify evidence justifies promotion")

        hard = [x for x in constraints if x[1] == "hard"]
        if len(constraints) >= 5 and len(hard) / len(constraints) > 0.4:
            warnings.append(
                f"hard constraints are {len(hard)}/{len(constraints)} facts (>40%); verify the spec is not over-constrained"
            )
        for fact_id, strength, scope in constraints:
            if strength == "hard" and scope == "local":
                warnings.append(f"local fact marked hard: {fact_id}; valid for reconstruction, suspicious for extension")

        comps = manifest.get("components") or {}
        for cid, comp in comps.items():
            if isinstance(comp, dict) and not comp.get("reuse_policy"):
                warnings.append(f"component lacks reuse_policy exact/adapt/exemplar: {cid}")

    if re.search(r"(?i)font-family\s*[:=]\s*(Inter|SF Pro|Roboto)", text) and re.search(r"(?i)font.*Unknown", text):
        warnings.append("document contains both Unknown font evidence and a concrete common font; verify it is not an unsupported guess")

    print(f"Spec lint: {p}")
    for e in errors:
        print(f"ERROR: {e}")
    for w in warnings:
        print(f"WARN:  {w}")
    if not errors and not warnings:
        print("OK: no structural or constraint-overload issues found")
    elif not errors:
        print(f"OK with {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: spec_lint.py DESIGN-LANGUAGE-SPEC.md", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))
