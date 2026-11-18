#!/usr/bin/env python3
import csv
import tempfile
import os

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
        "study_id": "S986",
        "study_design_class": "economic/institutional framework analysis with numerical modeling",
        "evidence_level": "moderate",
        "mechanism_family": "discretion",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "municipal tariff-setting and retail-water sales-permit licensing, Jakarta City Council",
        "institutional_context": "municipal water utility staff, public tap operators, distributing vendors, neighborhood government officials",
    },
    {
        "study_id": "S987",
        "study_design_class": "qualitative/mixed-methods case study",
        "evidence_level": "moderate",
        "mechanism_family": "participation",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Mozambique National Rural Water Supply and Sanitation Program",
        "institutional_context": "community water committees, village governance structures",
    },
    {
        "study_id": "S988",
        "study_design_class": "comparative qualitative case study",
        "evidence_level": "high",
        "mechanism_family": "institutional_fragmentation",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "India Sector Reforms Pilot Project 1999, Demand Responsive Approach reform",
        "institutional_context": "Gram Panchayat local government, Village Water and Sanitation Committee",
    },
]

for r in new_rows:
    assert r["study_id"] not in existing_ids, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
