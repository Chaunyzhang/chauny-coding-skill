#!/usr/bin/env python3
"""Export token facts from a DESIGN-LANGUAGE-SPEC JSON manifest.

Produces a compact DTCG-style JSON file. Only facts with kind='token',
token_type and value are exported; components/layout remain in the Spec.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def extract_manifest(text: str):
    m = re.search(
        r"<!--\s*MANIFEST_START\s*-->\s*```json\s*(.*?)\s*```\s*<!--\s*MANIFEST_END\s*-->",
        text,
        flags=re.S | re.I,
    )
    if not m:
        raise ValueError("machine-readable manifest block not found")
    return json.loads(m.group(1))


def main(src: str, dst: str) -> None:
    text = Path(src).read_text(encoding="utf-8")
    manifest = extract_manifest(text)
    out = {}
    for token_id, fact in (manifest.get("facts") or {}).items():
        if not isinstance(fact, dict):
            continue
        if fact.get("kind") != "token":
            continue
        if "value" not in fact or not fact.get("token_type"):
            continue
        entry = {
            "$type": fact["token_type"],
            "$value": fact["value"],
        }
        desc = fact.get("description")
        if desc:
            entry["$description"] = desc
        out[token_id] = entry
    Path(dst).write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Exported {len(out)} token(s) to {dst}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: spec_export.py DESIGN-LANGUAGE-SPEC.md design-tokens.json", file=sys.stderr)
        raise SystemExit(2)
    try:
        main(sys.argv[1], sys.argv[2])
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        raise SystemExit(1)
