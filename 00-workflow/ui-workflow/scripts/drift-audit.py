#!/usr/bin/env python3
"""UI drift audit: report spacing / radius px literals outside the approved scale.

Usage:
  python3 -I drift-audit.py <path...> [--spacing 0,4,8,12,16,24,32,48] [--radius 0,6,8,12,999] [--ext .css,.scss,.tsx,.jsx,.vue]

Scans CSS-like declarations (and inline style objects) for gap/padding/margin
and border-radius values in px (positional top/left/inset are not audited). var(--token) references are counted as on-scale.
Exit code 1 when any off-scale literal is found.
"""
import argparse, os, re, sys
from collections import defaultdict

SPACING_PROPS = r"(?:gap|row-gap|column-gap|padding(?:-[a-z]+)?|margin(?:-[a-z]+)?|rowGap|columnGap|padding[A-Z][a-z]+|margin[A-Z][a-z]+)"
RADIUS_PROPS = r"(?:border-radius|border-[a-z]+-[a-z]+-radius|borderRadius)"
DECL = re.compile(r"(?P<prop>" + SPACING_PROPS + "|" + RADIUS_PROPS + r")\s*:\s*(?P<val>[^;}\n]+)")
PX = re.compile(r"(?<![\w.-])(-?\d+(?:\.\d+)?)px")
RADIUS = re.compile(RADIUS_PROPS)


def scale(s):
    return {float(x) for x in s.split(",") if x.strip()}


def files(paths, exts):
    for p in paths:
        if os.path.isfile(p):
            yield p
            continue
        for root, dirs, names in os.walk(p):
            dirs[:] = [d for d in dirs if d not in ("node_modules", "dist", "out", "build", ".git")]
            for n in names:
                if os.path.splitext(n)[1] in exts:
                    yield os.path.join(root, n)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--spacing", default="0,4,8,12,16,24,32,48")
    ap.add_argument("--radius", default="0,6,8,12,999")
    ap.add_argument("--ext", default=".css,.scss,.less,.tsx,.jsx,.vue")
    ap.add_argument("--show", type=int, default=3, help="locations listed per off-scale value")
    a = ap.parse_args()
    allowed = {"spacing": scale(a.spacing), "radius": scale(a.radius)}
    exts = set(a.ext.split(","))
    total = {"spacing": 0, "radius": 0}
    off = {"spacing": defaultdict(list), "radius": defaultdict(list)}
    for f in files(a.paths, exts):
        with open(f, encoding="utf-8", errors="ignore") as fh:
            for ln, line in enumerate(fh, 1):
                for m in DECL.finditer(line):
                    kind = "radius" if RADIUS.fullmatch(m.group("prop")) else "spacing"
                    for v in PX.findall(m.group("val")):
                        total[kind] += 1
                        n = abs(float(v))
                        if n not in allowed[kind]:
                            off[kind][n].append(f"{f}:{ln}")
    bad = 0
    for kind in ("spacing", "radius"):
        count = sum(len(v) for v in off[kind].values())
        bad += count
        pct = (count / total[kind] * 100) if total[kind] else 0
        print(f"[{kind}] scale={sorted(allowed[kind])}  px literals={total[kind]}  off-scale={count} ({pct:.0f}%)")
        for val, locs in sorted(off[kind].items(), key=lambda kv: -len(kv[1])):
            more = f" …+{len(locs) - a.show}" if len(locs) > a.show else ""
            print(f"  {val:g}px ×{len(locs)}  " + ", ".join(locs[: a.show]) + more)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
