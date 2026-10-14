#!/usr/bin/env python3
import csv
import os
import tempfile

REPO = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
DB = os.path.join(REPO, "02_screening/full_text/full_text_screening_database.csv")

REVIEWER = "Claude-AI-fulltext-2026-09-21"

INCLUDES = {
    "R8C898DA2D09A": "Qualitative ethnographic case study of household water insecurity and "
        "'patchwork adaptability' in three low-income unplanned-settlement neighbourhood enclaves "
        "in south-eastern Bangalore, India, documenting the municipality's resource-governance "
        "failure and settlements' exclusion from the municipal piped-water grid (informal, "
        "'largely unregulated by a state entity'), with real primary fieldwork (30-household "
        "questionnaires plus door-knocking and semi-structured interviews/focus groups across "
        "three neighbourhoods, January-August 2018) tied to real household-level water-access "
        "coping-strategy and connection-cost outcomes. Extracted for record_id R8C898DA2D09A.",
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

print(f"Batch 128 recorded: {len(INCLUDES)} includes, 0 excludes.")
