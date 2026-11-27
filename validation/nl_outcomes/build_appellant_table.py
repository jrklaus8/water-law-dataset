#!/usr/bin/env python3
"""Join appellant coding and water-density features to the outcome table; write summaries and a blind check sheet.
Usage: python validation/nl_outcomes/build_appellant_table.py FEATURES_JSONL[,MORE] NEG_IDS_TXT CTL_IDS_TXT
Run from the repository root. Reads validation/nl_outcomes/nl_outcomes_coded.csv; writes nl_appellant_coded.csv,
nl_appellant_outcome_summary.csv, nl_relevance_check.csv and manual_check_appellant_BLIND.csv.
"""
import collections
import csv
import json
import math
import random
import statistics as st
import sys
from pathlib import Path

sys.path.insert(0, "utils")
import nl_appellant_coding as ac  # noqa: E402

csv.field_size_limit(10 ** 9)
D = Path("validation/nl_outcomes")
feat = {}
for f in sys.argv[1].split(","):
    for line in open(f, encoding="utf-8"):
        r = json.loads(line)
        feat[r["ecli"]] = r
neg = set(Path(sys.argv[2]).read_text().split())
ctl = set(Path(sys.argv[3]).read_text().split())
coded = list(csv.DictReader(open(D / "nl_outcomes_coded.csv", encoding="utf-8")))
core = [r for r in coded if r["sample"] in ("specific_categories", "other_water_keyword_match")]

rows = []
for r in core:
    f = feat[r["ecli"]]
    a = ac.code_opening(f["opening"])
    rows.append({"ecli": r["ecli"], "tribunal": r["tribunal"], "year": r["year"], "governance_cat": r["governance_cat"], "sample": r["sample"],
                 "outcome": r["outcome"], "appellant_type": a["appellant_type"], "appellant_rule": a["appellant_rule"],
                 "appellant_segment": a["appellant_segment"], "water_hits": f["water_hits"], "words": f["words"], "water_per_1k": f["water_per_1k"]})
with open(D / "nl_appellant_coded.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)


def wilson(k, n):
    z = 1.96
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return round(100 * (c - h), 1), round(100 * (c + h), 1)


def family(t):
    return "MIXED" if t.startswith("MIXED") else t


t = collections.defaultdict(collections.Counter)
for r in rows:
    t[family(r["appellant_type"])][r["outcome"]] += 1
out = [["appellant_type", "n", "decided(W+P+L)", "WIN", "PARTIAL", "LOSS", "upheld_pct_of_decided", "wilson95_lo", "wilson95_hi"]]
for k, v in sorted(t.items(), key=lambda x: -sum(x[1].values())):
    d = v["WIN"] + v["PARTIAL"] + v["LOSS"]
    lo, hi = wilson(v["WIN"], d) if d else ("", "")
    out.append([k, sum(v.values()), d, v["WIN"], v["PARTIAL"], v["LOSS"], round(100 * v["WIN"] / d, 1) if d else "", lo, hi])
csv.writer(open(D / "nl_appellant_outcome_summary.csv", "w", newline="")).writerows(out)


def rel(name, ids):
    d = [feat[i] for i in ids if i in feat]
    wt = [x for x in d if x["words"] > 0]
    return [name, len(d), len(d) - len(wt), round(st.median([x["water_per_1k"] for x in wt]), 2),
            round(100 * sum(1 for x in wt if x["water_per_1k"] >= 3) / len(wt), 1), round(100 * sum(1 for x in wt if x["water_hits"] >= 10) / len(wt), 1)]


R = [["group", "n", "no_body_text", "median_water_terms_per_1k_words", "pct_with_>=3_per_1k", "pct_with_>=10_hits"],
     rel("specific categories", [r["ecli"] for r in core if r["sample"] == "specific_categories"]),
     rel("other_water, keyword in summary", [r["ecli"] for r in core if r["sample"] == "other_water_keyword_match"]),
     rel("other_water, no keyword in summary (random 300)", neg),
     rel("not_water_related (random 100, control)", ctl)]
csv.writer(open(D / "nl_relevance_check.csv", "w", newline="")).writerows(R)

random.seed(2027)
pick = random.sample(rows, 120)
with open(D / "manual_check_appellant_BLIND.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["ecli", "caption_text", "human_appellant_type", "human_note"])
    for r in pick:
        w.writerow([r["ecli"], feat[r["ecli"]]["opening"][:700], "", ""])
print(collections.Counter(family(r["appellant_type"]) for r in rows).most_common())
for o in out[:10]:
    print(o)
for x in R:
    print(x)
