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
        "study_id": "S1074",
        "study_design_class": "ethnographic case study",
        "evidence_level": "high",
        "mechanism_family": "deliberate administrative inaction / discriminatory infrastructure neglect",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "municipal infrastructure maintenance obligations and bore-well permitting",
        "institutional_context": "Municipal Corporation of Greater Mumbai (BMC), Premnagar settlement",
    },
    {
        "study_id": "S1075",
        "study_design_class": "quantitative empirical study using national regulator survey data",
        "evidence_level": "moderate",
        "mechanism_family": "institutional ownership/management model (PPP vs. corporate public ownership)",
        "outcome_family": "affordability, service_quality",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Portuguese Water Sector Regulator (ERSAR) economic regulation",
        "institutional_context": "national water utilities, Portugal (PPP and corporate public sector)",
    },
    {
        "study_id": "S1076",
        "study_design_class": "mixed qualitative-quantitative institutional case study",
        "evidence_level": "high",
        "mechanism_family": "institutional fragmentation and regulatory delay",
        "outcome_family": "service_coverage, affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "multi-level water governance (LWUA, NWRB, DOH, local government)",
        "institutional_context": "Zamboanga City Water District, Philippines",
    },
    {
        "study_id": "S1077",
        "study_design_class": "critical policy-analysis essay",
        "evidence_level": "moderate",
        "mechanism_family": "gender-mainstreaming implementation and water-sector privatization",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "water-sector reform and privatization, gender policy",
        "institutional_context": "SEWA 'Women, Water and Work' campaign, India",
    },
    {
        "study_id": "S1078",
        "study_design_class": "qualitative institutional/legal case study",
        "evidence_level": "high",
        "mechanism_family": "eligibility, fees",
        "outcome_family": "household water access, coverage and affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "National Community Water and Sanitation Program (NCWSP), community-based management policy replacing customary water rights",
        "institutional_context": "Community Water and Sanitation Agency (CWSA), Nankani settlement, Upper East Region, Ghana",
    },
    {
        "study_id": "S1079",
        "study_design_class": "quantitative cross-national panel regression study",
        "evidence_level": "moderate",
        "mechanism_family": "broad socioeconomic/structural determinants (investment, agricultural share, vulnerable female employment, education, urbanization)",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "UN-recognized human right to water (Resolution 64/292, 2010); MDG/SDG policy framework",
        "institutional_context": "111 countries, national water-sector institutions",
    },
    {
        "study_id": "S1080",
        "study_design_class": "empirical case study of street-level regulatory bureaucrats",
        "evidence_level": "moderate",
        "mechanism_family": "privatization/contracting-out and regulatory enforcement capacity",
        "outcome_family": "sanitation_access, service_quality",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "privatization and contracting-out of environmental sanitation services",
        "institutional_context": "Environmental Health Department street-level officials, Kumasi and Accra, Ghana",
    },
    {
        "study_id": "S1081",
        "study_design_class": "qualitative assessment (key-informant interviews, focus-group discussions)",
        "evidence_level": "moderate",
        "mechanism_family": "eligibility, fees, connection requirements",
        "outcome_family": "sanitation_access, service_coverage, affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Dhaka Sanitation Improvement Project (DSIP) sewerage-network connection policy",
        "institutional_context": "Dhaka Water Supply and Sewerage Authority (DWASA), 16 low-income communities, Bangladesh",
    },
]

for nr in new_rows:
    assert nr["study_id"] not in existing_ids, nr["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
