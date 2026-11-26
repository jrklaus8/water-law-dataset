#!/usr/bin/env python3
"""Join the raw outcome checkpoint (JSONL from utils/nl_outcome_coding.py fetch) to the dataset's metadata and
re-apply the current rules to the stored dispositive text. Standard library only.

Usage: python validation/nl_outcomes/build_outcome_table.py CODED_CSV CHECKPOINT_JSONL[,MORE_JSONL] SPECIFIC_IDS_TXT OUT_CSV [RANDOM_IDS_TXT [KEYWORD_IDS_TXT]]
  CODED_CSV     water_law_global_coded.csv (Harvard Dataverse, doi:10.7910/DVN/C9PEFS)
  SPECIFIC_IDS  one ECLI per line: every NL case whose governance_cat is not other_water or not_water_related
"""
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "utils"))
import nl_outcome_coding as n  # noqa: E402

csv.field_size_limit(10 ** 9)
coded, ckpt, spec_ids, out = sys.argv[1:5]
random_ids = set(Path(sys.argv[5]).read_text().split()) if len(sys.argv) > 5 else set()
keyword_ids = set(Path(sys.argv[6]).read_text().split()) if len(sys.argv) > 6 else set()
meta = {r["case_id"]: r for r in csv.DictReader(open(coded, encoding="utf-8-sig")) if r["country"] == "Netherlands"}
spec = set(Path(spec_ids).read_text().split())
latest = {}
for path in ckpt.split(","):  # several checkpoints may be given, comma separated; later lines win (re-fetches)
    for line in open(path, encoding="utf-8"):
        r = json.loads(line)
        latest[r["ecli"]] = r
rows = []
for r in latest.values():
    if r["outcome"] != "FETCH_FAILED":
        r["outcome"], r["rule"], r["multi_step"] = n.classify(r["dispositive"])
    m = meta[r["ecli"]]
    r.update(tribunal=m["tribunal"], year=m["year"][:4], governance_cat=m["governance_cat"],
             sample=("specific_categories" if r["ecli"] in spec else "other_water_keyword_match" if r["ecli"] in keyword_ids else "random_other_water_n1500_seed42"))
    if r["ecli"] in random_ids:
        r["in_random_sample"] = 1
    rows.append(r)
cols = ["ecli", "tribunal", "year", "governance_cat", "sample", "in_random_sample", "outcome", "rule", "multi_step", "dispositive"]
with open(out, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    for r in sorted(rows, key=lambda x: x["ecli"]):
        w.writerow({c: r.get(c, 0) for c in cols})
print(len(rows), "rows written to", out)
