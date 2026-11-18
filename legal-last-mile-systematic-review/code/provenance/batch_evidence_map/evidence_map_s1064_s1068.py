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
        "study_id": "S1064",
        "study_design_class": "ethnographic case study",
        "evidence_level": "high",
        "mechanism_family": "fees",
        "outcome_family": "affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "cost-recovery/tariff enforcement; constitutional non-denial-of-service right",
        "institutional_context": "Junta de Agua y Drenaje (JAD), Matamoros, Tamaulipas, Mexico",
    },
    {
        "study_id": "S1065",
        "study_design_class": "quantitative cross-sectional survey analysis (Human Opportunity Index)",
        "evidence_level": "moderate",
        "mechanism_family": "regional_disparity",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "regional infrastructure disparity; circumstance-based inequality of opportunity",
        "institutional_context": "national water/sanitation infrastructure, Tunisia",
    },
    {
        "study_id": "S1066",
        "study_design_class": "qualitative case study",
        "evidence_level": "high",
        "mechanism_family": "enforcement",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "prepaid water metering; disconnection enforcement",
        "institutional_context": "Johannesburg Water (Operation Gcin'amanzi), Soweto, South Africa",
    },
    {
        "study_id": "S1067",
        "study_design_class": "detailed qualitative case study (project evaluation)",
        "evidence_level": "high",
        "mechanism_family": "fees",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "water-user-committee fee collection; customary land tenure; gender exclusion from committees",
        "institutional_context": "government rural water supply agency (RWSS), South Pacific island country",
    },
    {
        "study_id": "S1068",
        "study_design_class": "comparative mixed-methods case study",
        "evidence_level": "high",
        "mechanism_family": "institutional_arrangement",
        "outcome_family": "affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "binational water-policy and institutional parameters",
        "institutional_context": "local water utilities, Columbus (New Mexico, USA) and Palomas (Chihuahua, Mexico)",
    },
]

for r in new_rows:
    assert r["study_id"] not in existing, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
