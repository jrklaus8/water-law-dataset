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
        "study_id": "S1000",
        "study_design_class": "mixed-methods case study (survey, archives, GIS, interviews)",
        "evidence_level": "high",
        "mechanism_family": "discretion",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "utility governance norms, land-use policy, connection-fee/tariff policy",
        "institutional_context": "PAM Jaya water utility (public and private management)",
    },
    {
        "study_id": "S1001",
        "study_design_class": "historical case study with archival and interview data",
        "evidence_level": "high",
        "mechanism_family": "legal_status",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "colonial-era institutional citizenship classification, postcolonial modernization projects",
        "institutional_context": "colonial and postcolonial Jakarta water utility, private management from 1998",
    },
    {
        "study_id": "S1002",
        "study_design_class": "quantitative spatial/regression analysis",
        "evidence_level": "high",
        "mechanism_family": "enforcement",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "U.S. Safe Drinking Water Act (1974, amended)",
        "institutional_context": "Pennsylvania community water systems, EPA",
    },
    {
        "study_id": "S1003",
        "study_design_class": "cross-country comparative analysis using secondary datasets",
        "evidence_level": "moderate",
        "mechanism_family": "legal_status",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "formal legal promulgation of a right to water (Hohfeldian framework)",
        "institutional_context": "national water-sector institutions, governance-quality indicators",
    },
]

for r in new_rows:
    assert r["study_id"] not in existing_ids, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
