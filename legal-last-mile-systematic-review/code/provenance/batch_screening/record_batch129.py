#!/usr/bin/env python3
import csv
import os
import tempfile

REPO = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
DB = os.path.join(REPO, "02_screening/full_text/full_text_screening_database.csv")

REVIEWER = "Claude-AI-fulltext-2026-09-21"

INCLUDES = {
    "R0C5195EA94D6": "Mixed-methods institutional case study of dissonance between customary and "
        "statutory water institutions in the Okavango Delta, Botswana, documenting Botswana's real "
        "legal/regulatory water-sector framework (WUC Act 1970, 2008 water-sector reform "
        "delineating DWA/WUC/district-council responsibilities, shift from free access to "
        "cost-recovery tariffs) via a large-N primary sample (455 household heads, 44 community "
        "elders, 17 government officials across 3 rural villages) combining key-informant "
        "interviews, FGDs, household interview schedules, and inferential statistics (Kruskal-"
        "Wallis, Mann-Whitney U). Extracted for record_id R0C5195EA94D6.",
    "RBFA4A3198454": "Mixed-methods institutional case study of community-based water supply "
        "management (CBWSM) sustainability across six rural villages in Northwest Cameroon, "
        "documenting Cameroon's decentralization policy (ministerial decree Articles 3(11)/3(16)) "
        "and traditional-authority/village-Chief institutional structures against real primary "
        "household-level data (156-household systematic-sample questionnaires across 6 villages "
        "plus key-informant interviews) on water-project success/failure outcomes. Extracted for "
        "record_id RBFA4A3198454.",
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

print(f"Batch 129 recorded: {len(INCLUDES)} includes, 0 excludes.")
