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
        "study_id": "S1121",
        "study_design_class": "quantitative panel-regression study",
        "evidence_level": "high",
        "mechanism_family": "eligibility, administrative_review, delay, discretion, procedural_steps (water-adequacy screening administrative review vs. impact fees)",
        "outcome_family": "water_access, service_coverage, refusal, delay_outcome",
        "quantitative_synthesis_eligible": "TRUE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "California SB 901 (1995), SB 610/SB 221 (2001)",
        "institutional_context": "289 California jurisdictions",
    },
    {
        "study_id": "S1122",
        "study_design_class": "quantitative event-history regression study (Cox model)",
        "evidence_level": "high",
        "mechanism_family": "eligibility, zoning, tenure, property, service_area (zoned vs. non-zoned settlement status)",
        "outcome_family": "water_access, service_coverage, refusal",
        "quantitative_synthesis_eligible": "TRUE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "urban zoning/land-allocation system",
        "institutional_context": "Ouagadougou, Burkina Faso",
    },
    {
        "study_id": "S1123",
        "study_design_class": "case study (documentary analysis)",
        "evidence_level": "moderate",
        "mechanism_family": "service_area, institutional_fragmentation, political_coordination, participation (municipal annexation/underbounding)",
        "outcome_family": "water_access, sanitation_access, service_coverage, refusal",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "municipal annexation law",
        "institutional_context": "colonias, California, United States",
    },
    {
        "study_id": "S1124",
        "study_design_class": "mixed-methods empirical case study (household surveys, interviews)",
        "evidence_level": "moderate",
        "mechanism_family": "fees, procedural_steps, institutional_fragmentation, burden (connection-fee and service fragmentation)",
        "outcome_family": "water_access, service_coverage, service_reliability, service_quantity, affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "2002 Tanzania National Water Policy",
        "institutional_context": "Dar es Salaam, Tanzania",
    },
    {
        "study_id": "S1125",
        "study_design_class": "institutional/governance case study",
        "evidence_level": "moderate",
        "mechanism_family": "discretion, participation, institutional_fragmentation, bureaucratic_assistance, political_coordination (centralized-state vs. community-centered water governance)",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "DFRRI centralized rural-development program",
        "institutional_context": "Plateau State, Nigeria",
    },
    {
        "study_id": "S1126",
        "study_design_class": "multi-city comparative field-research case study",
        "evidence_level": "moderate",
        "mechanism_family": "institutional_fragmentation, political_coordination, discretion_accommodation, service_area (local water-governance capacity)",
        "outcome_family": "water_access, service_reliability, service_continuity",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "absence of coordinated municipal water-planning agencies",
        "institutional_context": "5 Himalayan cities, Nepal and India",
    },
]

for nr in new_rows:
    assert nr["study_id"] not in existing_ids, nr["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
