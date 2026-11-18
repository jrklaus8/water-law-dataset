#!/usr/bin/env python3
import csv
import os
import tempfile

REPO = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
DB = os.path.join(REPO, "02_screening/full_text/full_text_screening_database.csv")
EXLOG = os.path.join(REPO, "02_screening/exclusion_log/exclusion_log.csv")

REVIEWER = "Claude-AI-fulltext-2026-09-21"
DATE = "2026-09-22"

INCLUDES = {
    "R512A2C899B40": "Qualitative institutional case study of informal-settlement water governance "
        "in three Dar es Salaam settlements, with primary data from 35 interviews with non-state "
        "water service providers plus key-informant interviews (municipal water engineer, ward "
        "leaders, ward health officer), documenting the formal/informal rules governing water "
        "pricing, distribution, and access and the state water utility's (DAWASA) limited capacity "
        "to serve informal settlements, tied to real settlement-level household/income data. "
        "Extracted for record_id R512A2C899B40.",
    "R84E44162269B": "Qualitative comparative case study of co-production between the City of Cape "
        "Town and two informal settlements (Malawi Camp, Klipheuwel), documenting real municipal "
        "Water & Sanitation Department regulations (denial of communal-toilet/tap relocation to "
        "individual yards) and the negotiated institutional workaround (community-managed 'Water "
        "Saving Ambassadors'), tied to real settlement-level water/sanitation infrastructure "
        "outcomes (toilet cementing/repair, standpipe management). Extracted for record_id "
        "R84E44162269B.",
}

EXCLUDES = {
    "R77892B64F9F0": ("E01", "Macro/city-level composite-index panel-regression study of urban water "
        "supply system resilience (UWSSR) across the Yangtze River Delta urban agglomeration, using "
        "12 indicators including GDP per capita, public financial resources, and a public-regulation "
        "index; no household-level access data or specific legal/administrative access mechanism "
        "examined, same macro/city-level governance-index rationale as the Nkiaka/Schiel/Laitinen/"
        "Padowski exclusions."),
}

TITLES = {
    "R77892B64F9F0": ("Spatiotemporal differentiation and influencing factors of urban water supply system resilience in the Yangtze River Delta urban agglomeration", "Sun, Gu, Chen, Xia and Chen", "2022"),
}

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

by_id = {r["record_id"]: r for r in rows}

for rid in list(INCLUDES) + list(EXCLUDES):
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

print(f"Batch 126 recorded: {len(INCLUDES)} includes, {len(EXCLUDES)} excludes.")
print(f"exclusion_log.csv new total: {len(ex_rows)}")
