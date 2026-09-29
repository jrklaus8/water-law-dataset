#!/usr/bin/env python3
"""Score a filled second-extractor sheet: agreement of the AI extraction with an independent human, by field and overall.

Usage: python3 code/analysis/score_second_extractor_sheet.py path/to/filled_sheet.csv
Counts rows whose `agrees (Y/N/cannot_tell)` is Y or N (cannot_tell and blank are excluded and reported). Reports disagreement rate with a Wilson 95% interval.
With ~60 studies the interval for any one field is wide (about +/-10 points); read the overall figure, not single fields.
"""
import csv, math, sys
from collections import Counter, defaultdict


def wilson(k, n, z=1.96):
    if n == 0:
        return (float('nan'),) * 2
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (c - h) / d, (c + h) / d


def main(path):
    rows = list(csv.DictReader(open(path, encoding='utf-8', newline='')))
    col = 'agrees (Y/N/cannot_tell)'
    tot, bad, skipped = Counter(), Counter(), Counter()
    per_study = defaultdict(int)
    for r in rows:
        v = r[col].strip().upper()
        if v not in ('Y', 'N'):
            skipped[r['field']] += 1
            continue
        tot[r['field']] += 1
        if v == 'N':
            bad[r['field']] += 1
            per_study[r['study_id']] += 1
    print(f"{'field':22} {'n':>4} {'disagree':>8} {'rate':>6}   95% CI")
    for f in list(tot):
        lo, hi = wilson(bad[f], tot[f])
        print(f"{f:22} {tot[f]:4d} {bad[f]:8d} {100 * bad[f] / tot[f]:5.1f}%   {100 * lo:.0f}-{100 * hi:.0f}%")
    n, k = sum(tot.values()), sum(bad.values())
    if n:
        lo, hi = wilson(k, n)
        print(f"{'ALL FIELDS':22} {n:4d} {k:8d} {100 * k / n:5.1f}%   {100 * lo:.0f}-{100 * hi:.0f}%  (fields are not independent within a study)")
    print(f"studies with at least one disagreement: {len(per_study)} of {len({r['study_id'] for r in rows})}; rows skipped (blank or cannot_tell): {sum(skipped.values())}")


if __name__ == '__main__':
    main(sys.argv[1])
