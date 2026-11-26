#!/usr/bin/env python3
"""Per-group outcome summary with Wilson 95% intervals. Usage: python make_summary.py nl_outcomes_coded.csv nl_outcome_summary.csv"""
import collections
import csv
import math
import sys

csv.field_size_limit(10 ** 9)
rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8")))


def wilson(k, n):
    if n == 0:
        return "", ""
    z = 1.96
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return round(100 * (c - h), 1), round(100 * (c + h), 1)


def line(sub, name):
    c = collections.Counter(r["outcome"] for r in sub)
    dec = c["WIN"] + c["LOSS"] + c["PARTIAL"]
    lo, hi = wilson(c["WIN"], dec)
    return [name, len(sub), c["WIN"], c["PARTIAL"], c["LOSS"], c["INADMISSIBLE"], c["REMAND"] + c["INTERIM"] + c["NO_MERITS_RULING"],
            c["UNCLASSIFIED"], c["NO_TEXT"], dec, round(100 * c["WIN"] / dec, 1) if dec else "", lo, hi]


spec = [r for r in rows if r["sample"] == "specific_categories"]
by = collections.defaultdict(list)
for r in spec:
    by[r["governance_cat"]].append(r)
out = [line(v, k) for k, v in sorted(by.items(), key=lambda x: -len(x[1]))]
out.append(line(spec, "ALL specific categories"))
kw = [r for r in rows if r["sample"] == "other_water_keyword_match"]
out.append(line(kw, "other_water rows with a water term in the summary"))
out.append(line(spec + kw, "specific categories + keyword matches"))
out.append(line([r for r in rows if r["in_random_sample"] == "1"], "other_water random sample (seed 42)"))
with open(sys.argv[2], "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["group", "n", "WIN", "PARTIAL", "LOSS", "INADMISSIBLE", "REMAND_INTERIM_PROCEDURAL", "UNCLASSIFIED", "NO_TEXT",
                "decided_n(W+P+L)", "win_pct_of_decided", "wilson95_lo", "wilson95_hi"])
    w.writerows(out)
