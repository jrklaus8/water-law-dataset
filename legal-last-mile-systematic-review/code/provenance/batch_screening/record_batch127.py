#!/usr/bin/env python3
import csv
import os
import tempfile

REPO = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
DB = os.path.join(REPO, "02_screening/full_text/full_text_screening_database.csv")

REVIEWER = "Claude-AI-fulltext-2026-09-21"

INCLUDES = {
    "RFAAFF404B38C": "Qualitative institutional case study of decentralized rural water management "
        "capacity gaps in Ghana across three rural communities (Esereso, Wabrease, Wioso) and "
        "multi-level water management agencies (Community Water and Sanitation Agency, district "
        "assemblies), documenting the real regulatory/institutional framework (National Community "
        "Water and Sanitation Programme, CWSA standards/guidelines, district assemblies as legal "
        "owners of communal infrastructure, Water and Sanitation Committee formation rules) via "
        "household/informant interviews and focus group discussions. Extracted for record_id "
        "RFAAFF404B38C.",
}

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

by_id = {r["record_id"]: r for r in rows}

for rid in INCLUDES:
    assert rid in by_id, f"record_id {rid} not found"
    r = by_id[rid]
    assert not r["full_text_decision"] and not r["final_decision"], f"{rid} already decided"

for rid, note in INCLUDES.items():
    r = by_id[rid]
    r["full_text_decision"] = "include"
    r["final_decision"] = "include"
    r["full_text_status"] = "retrieved"
    r["reviewer_1"] = REVIEWER
    r["notes"] = note

fd, tmppath = tempfile.mkstemp(dir=REPO)
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmppath, DB)

print(f"Batch 127 recorded: {len(INCLUDES)} includes, 0 excludes.")
