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
        "study_id": "S1101",
        "study_design_class": "comparative case study",
        "evidence_level": "high",
        "mechanism_family": "eligibility, fees, enforcement (tariff/indigent-subsidy, credit-control disconnection)",
        "outcome_family": "water_access, affordability, service_continuity",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Greater Hermanus Water Conservation Programme tiered tariff structure",
        "institutional_context": "Hermanus Municipality, Zwelihle township, South Africa",
    },
    {
        "study_id": "S1102",
        "study_design_class": "quantitative quasi-experimental study (propensity score matching)",
        "evidence_level": "high",
        "mechanism_family": "participation, fees (capital-cost contribution, meeting attendance)",
        "outcome_family": "water_access, service_reliability, service_quality",
        "quantitative_synthesis_eligible": "TRUE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "community-based rural drinking-water project management",
        "institutional_context": "water user groups/committees, 45 villages, India",
    },
    {
        "study_id": "S1103",
        "study_design_class": "comparative natural-experiment case study",
        "evidence_level": "high",
        "mechanism_family": "fees, eligibility, enforcement (corporate governance/management model, connection-fee installments)",
        "outcome_family": "water_access, service_coverage, formal_connection",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "1997 MWSS concession contracts, identical terms across two concessionaires",
        "institutional_context": "Manila Water Company and Maynilad Water Services, Metro Manila, Philippines",
    },
    {
        "study_id": "S1104",
        "study_design_class": "multi-country comparative case-study analysis",
        "evidence_level": "high",
        "mechanism_family": "eligibility, fees, tenure (land-title waiver, installment connection fees, shared connections)",
        "outcome_family": "water_access, sanitation_access, formal_connection, affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "public-private-community partnership institutional arrangements",
        "institutional_context": "public utilities, private operators, NGOs, 10 Asian countries",
    },
    {
        "study_id": "S1105",
        "study_design_class": "ethnographic case study",
        "evidence_level": "moderate",
        "mechanism_family": "service_area, discretion, political_coordination (infrastructure sequencing, customary governance dispute)",
        "outcome_family": "water_access, delay_outcome",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Adduction d'eau potable Grombaou water-conveyance project",
        "institutional_context": "Municipality Council of Kone and customary Council of Elders, Kanak tribes, New Caledonia",
    },
]

for nr in new_rows:
    assert nr["study_id"] not in existing_ids, nr["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
