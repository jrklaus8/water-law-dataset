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

existing = {r["study_id"] for r in rows}

new_rows = [
    {
        "study_id": "S1031",
        "study_design_class": "comparative case study (policy/documentary analysis)",
        "evidence_level": "moderate",
        "mechanism_family": "planning",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "'world city'/'global city' urban development plans and strategic planning documents",
        "institutional_context": "municipal governments (Johannesburg, Hyderabad)",
    },
    {
        "study_id": "S1032",
        "study_design_class": "quantitative regression analysis (logistic regression, household survey)",
        "evidence_level": "high",
        "mechanism_family": "administrative_review",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "TRUE",
        "qualitative_synthesis_eligible": "FALSE",
        "legal_context": "Ahmedabad Slum Networking Project (SNP) co-production partnership",
        "institutional_context": "Ahmedabad Municipal Corporation, NGOs",
    },
    {
        "study_id": "S1033",
        "study_design_class": "case study (documentary/interview analysis)",
        "evidence_level": "moderate",
        "mechanism_family": "enforcement",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Tri-Water Sector Partnership (TWSP)",
        "institutional_context": "Ghana Water Company Ltd (GWCL), community water boards, chieftaincy institution",
    },
]

for r in new_rows:
    assert r["study_id"] not in existing, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
