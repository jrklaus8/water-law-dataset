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
        "study_id": "S1082",
        "study_design_class": "cross-sectional household survey with shared dialogue workshop",
        "evidence_level": "moderate",
        "mechanism_family": "eligibility, fees (Water User Committee financial-contribution requirements)",
        "outcome_family": "water_access, service_reliability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "community-based management (CBM) model for rural water supply",
        "institutional_context": "Water User Committees, Lwengo district, southern Uganda",
    },
    {
        "study_id": "S1083",
        "study_design_class": "practitioner impact-assessment study",
        "evidence_level": "moderate",
        "mechanism_family": "fees, bureaucratic_assistance (NGO-ULB-community cost-sharing partnership)",
        "outcome_family": "sanitation_access, affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "One Home-One Toilet (OHOT) household sanitation delivery model",
        "institutional_context": "Shelter Associates (NGO) and Urban Local Bodies, four Maharashtra cities, India",
    },
    {
        "study_id": "S1084",
        "study_design_class": "quantitative panel survey regression study",
        "evidence_level": "moderate",
        "mechanism_family": "broad socioeconomic/geographic determinants (age, education, wealth, distance, region)",
        "outcome_family": "water_access, sanitation_access, service_coverage",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Nepal Living Standard Survey panel, 1995-2011",
        "institutional_context": "national water/sanitation/waste-disposal infrastructure, Nepal",
    },
    {
        "study_id": "S1085",
        "study_design_class": "quantitative household survey regression study (Tobit)",
        "evidence_level": "high",
        "mechanism_family": "fees, participation (WUC-set tariff/contribution levels)",
        "outcome_family": "household contribution amount (financing-sustainability, not direct water access)",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "community-based management (CBM) model for rural water supply",
        "institutional_context": "Water User Committees, Achefer area, Amhara region, Ethiopia",
    },
    {
        "study_id": "S1086",
        "study_design_class": "mixed quantitative/ethnographic case study",
        "evidence_level": "high",
        "mechanism_family": "eligibility, tenure, fees (tenure-proof requirement waived for payment proof)",
        "outcome_family": "household water access, formal connection, coverage, affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Greater Bangalore water project 'beneficiary capital contribution' cost-recovery policy",
        "institutional_context": "Bangalore Water Supply and Sewerage Board, peripheral 'revenue layout' settlements, India",
    },
    {
        "study_id": "S1087",
        "study_design_class": "fieldwork-based institutional/regulatory case study",
        "evidence_level": "high",
        "mechanism_family": "eligibility, fees, enforcement (CPC licensing and tariff regulation)",
        "outcome_family": "water_access, service_coverage, affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "National Water Resources Board Certificate of Public Convenience licensing framework",
        "institutional_context": "small-scale water providers and NGOs, post-privatization Metro Manila, Philippines",
    },
]

for nr in new_rows:
    assert nr["study_id"] not in existing_ids, nr["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
