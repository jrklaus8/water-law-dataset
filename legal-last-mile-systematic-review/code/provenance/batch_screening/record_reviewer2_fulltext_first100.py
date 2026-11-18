#!/usr/bin/env python3
"""
Records the human PI's (Claudio Klaus) independent full-text reviewer_2 pass
over the first 100 chronologically-included studies (S001-S100 in
extraction_database.csv), per the researcher's explicit instruction:
"I've just reviewed the first 100 articles that were included and I want to
register my decision which is that I agree with the classification."

Maps study_id -> record_id via DOI (normalized) then title fallback,
verified by hand for the residual unmatched/ambiguous cases (see
CHANGELOG.md entry for the full method and the one caught data anomaly:
S063's extraction DOI matches record R7EECD84CD3AA textually, but that
record_id is itself a documented post-hoc duplicate (E08) of the true
include RF043AAD78E8E -- corrected before writing).

Sets reviewer_2 = "Human-reviewer2-fulltext-2026-09-27" and conflict = FALSE
for these 100 records (agreement, not a firm contradiction) per
FULL_TEXT_README.md's stated schema. Does not touch final_decision (already
"include") or any other field.
"""
import csv
import json
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
MAPPING_PATH = "/tmp/claude-0/-home-user-water-law-dataset/13a4d716-bf67-5f8e-b123-127698a45259/scratchpad/reviewer2_first100_match.json"

REVIEWER_2 = "Human-reviewer2-fulltext-2026-09-27"


def atomic_write(path, fieldnames, rows):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path))
    with os.fdopen(fd, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp, path)


with open(MAPPING_PATH) as f:
    study_to_record = json.load(f)

assert len(study_to_record) == 100
record_ids = set(study_to_record.values())
assert len(record_ids) == 100

with open(PATH, newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

updated = 0
for row in rows:
    if row["record_id"] in record_ids:
        assert row["final_decision"] == "include", row["record_id"]
        assert not row["reviewer_2"].strip(), f"{row['record_id']} already has reviewer_2={row['reviewer_2']!r}"
        row["reviewer_2"] = REVIEWER_2
        row["conflict"] = "FALSE"
        updated += 1

assert updated == 100, f"expected to update 100 rows, updated {updated}"

atomic_write(PATH, fieldnames, rows)
print(f"full_text_screening_database.csv updated: reviewer_2 set on {updated} records (S001-S100, all agreement, zero conflicts).")
