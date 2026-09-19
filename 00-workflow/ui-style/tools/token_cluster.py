#!/usr/bin/env python3
"""Tiny numeric clustering helper for raw UI measurements.

Example:
  token_cluster.py --tolerance 1 7 8 9 15 16 16

This only groups numbers. Semantic role decisions still belong to the model.
"""
from __future__ import annotations

import argparse
import statistics


def cluster(values, tolerance):
    groups = []
    for value in sorted(values):
        if not groups or value - groups[-1][-1] > tolerance:
            groups.append([value])
        else:
            groups[-1].append(value)
    return groups


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("values", nargs="+", type=float)
    ap.add_argument("--tolerance", type=float, default=1.0)
    args = ap.parse_args()
    for i, group in enumerate(cluster(args.values, args.tolerance), 1):
        print(f"cluster {i}: raw={group} median={statistics.median(group):g} n={len(group)}")


if __name__ == "__main__":
    main()
