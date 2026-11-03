#!/usr/bin/env python3
import csv
import os
import tempfile

REPO = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
DB = os.path.join(REPO, "02_screening/full_text/full_text_screening_database.csv")
EXLOG = os.path.join(REPO, "02_screening/exclusion_log/exclusion_log.csv")

REVIEWER = "Claude-AI-fulltext-2026-09-21"
DATE = "2026-09-22"

EXCLUDES = {
    "RD44ED5F07FED": ("E06", "Technical service-quality/design-standard benchmarking study using "
        "psychometric scaling (successive interval scaling, zone of tolerance, user satisfaction "
        "level) to determine appropriate quantitative construction attributes (area, door, number) "
        "of subsidized rural household toilets in India from user-perception surveys; no legal/"
        "institutional access-barrier mechanism examined, following the established single-dwelling "
        "engineering/construction-standard E06 precedent (Morena et al. 2019 Pekanbaru)."),
}

TITLES = {
    "RD44ED5F07FED": ("Determination of Appropriate Service Delivery Level for Quantitative Attributes of Household Toilets in Rural Settlements of India from Users' Perspective", "Rashid and Pandit", "2018"),
}

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

by_id = {r["record_id"]: r for r in rows}

for rid in EXCLUDES:
    assert rid in by_id, f"record_id {rid} not found"
    r = by_id[rid]
    assert not r["full_text_decision"] and not r["final_decision"], f"{rid} already decided"

for rid, (code, detail) in EXCLUDES.items():
    r = by_id[rid]
    r["full_text_decision"] = "exclude"
    r["final_decision"] = "exclude"
    r["full_text_status"] = "retrieved"
    r["reviewer_1"] = REVIEWER
    r["exclusion_reason"] = code
    r["exclusion_reason_detail"] = detail

fd, tmppath = tempfile.mkstemp(dir=REPO)
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmppath, DB)

with open(EXLOG, newline="", encoding="utf-8") as f:
    ex_reader = csv.DictReader(f)
    ex_fieldnames = ex_reader.fieldnames
    ex_rows = list(ex_reader)

for rid, (code, detail) in EXCLUDES.items():
    title, authors, year = TITLES[rid]
    ex_rows.append({
        "record_id": rid,
        "title": title,
        "authors": authors,
        "year": year,
        "stage": "full_text",
        "exclusion_code": code,
        "exclusion_reason_detail": detail,
        "reviewer": REVIEWER,
        "date": DATE,
    })

fd, tmppath = tempfile.mkstemp(dir=REPO)
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=ex_fieldnames)
    writer.writeheader()
    writer.writerows(ex_rows)
os.replace(tmppath, EXLOG)

print(f"Batch 131 recorded: 0 includes, {len(EXCLUDES)} excludes.")
print(f"exclusion_log.csv new total: {len(ex_rows)}")
