#!/usr/bin/env python3
import csv, tempfile, os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/descriptive/evidence_map.csv"


def atomic_write(path, fieldnames, rows):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path))
    with os.fdopen(fd, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp, path)


with open(PATH, newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

existing_ids = {r["study_id"] for r in rows}

new_rows = [
    {
        "study_id": "S1127",
        "study_design_class": "quantitative household-survey study",
        "evidence_level": "moderate",
        "mechanism_family": "fees, service_area, burden, affordability (demand-driven/water-markets institutional model)",
        "outcome_family": "water_access, service_coverage, service_quantity, affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "demand-driven/water-markets full-cost pricing prescription",
        "institutional_context": "3 Kenyan towns",
    },
    {
        "study_id": "S1128",
        "study_design_class": "ethnographic institutional/legal case study",
        "evidence_level": "moderate",
        "mechanism_family": "fees, discretion, administrative_review, judicial_review, participation (water-tariff regulatory formula)",
        "outcome_family": "water_access, affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "ARESEP water-tariff regulatory formula; constitutional right to water",
        "institutional_context": "Costa Rica",
    },
    {
        "study_id": "S1129",
        "study_design_class": "institutional/planning-history case study",
        "evidence_level": "moderate",
        "mechanism_family": "planning, service_area, institutional_fragmentation, political_coordination (colonial-era centralized infrastructure design)",
        "outcome_family": "sanitation_access, service_coverage",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "colonial-era 'piped paradigm' infrastructure planning legacy",
        "institutional_context": "Dar es Salaam, Tanzania",
    },
]

for nr in new_rows:
    assert nr["study_id"] not in existing_ids, nr["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
