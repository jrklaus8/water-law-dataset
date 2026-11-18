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
        "study_id": "S1053",
        "study_design_class": "qualitative case study (interviews, participatory research)",
        "evidence_level": "high",
        "mechanism_family": "fees",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Orissa Pani Panchayat Act 2002 / Rules 2003, statutory WUA fee-based access",
        "institutional_context": "Pani Panchayat (WUAs), Orissa, India",
    },
    {
        "study_id": "S1054",
        "study_design_class": "qualitative case study (Social Impact Assessment fieldwork)",
        "evidence_level": "high",
        "mechanism_family": "legal_status",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Treaty of Guadalupe Hidalgo (1848) traditional water rights vs. state water-rights adjudication",
        "institutional_context": "acequia system, Espanola Valley, New Mexico, USA",
    },
    {
        "study_id": "S1055",
        "study_design_class": "theoretical-empirical case study",
        "evidence_level": "moderate",
        "mechanism_family": "legal_status",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "citizenship/legal-subject status ('citizen' vs. 'squatter')",
        "institutional_context": "Mumbai Municipal Corporation; pavement-dwelling communities, India",
    },
    {
        "study_id": "S1056",
        "study_design_class": "quantitative cross-sectional survey analysis (correlational)",
        "evidence_level": "moderate",
        "mechanism_family": "social_capital_caste",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "caste-based social structure; informal collective action",
        "institutional_context": "community-level water-supply organization, India",
    },
    {
        "study_id": "S1057",
        "study_design_class": "quantitative econometric study (OLS, probit, IV/2SLS)",
        "evidence_level": "high",
        "mechanism_family": "participation",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "TRUE",
        "qualitative_synthesis_eligible": "FALSE",
        "legal_context": "community-based/demand-responsive water-service design participation",
        "institutional_context": "government rural water programs, Sri Lanka, Karnataka and Maharashtra (India)",
    },
    {
        "study_id": "S1058",
        "study_design_class": "qualitative case study",
        "evidence_level": "high",
        "mechanism_family": "enforcement",
        "outcome_family": "affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "differentiated non-payment/revenue-recovery enforcement by income level",
        "institutional_context": "private water concessionaires, Metro Manila, Philippines",
    },
]

for r in new_rows:
    assert r["study_id"] not in existing, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
