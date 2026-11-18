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
        "study_id": "S1113",
        "study_design_class": "institutional/regulatory case study",
        "evidence_level": "moderate",
        "mechanism_family": "eligibility, service_area, tenure, fees (regulatory framework, informal-settlement exclusion from statistics)",
        "outcome_family": "water_access, sanitation_access, service_coverage, affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Lei 14.026/2020 (Brazil's new sanitation legal framework)",
        "institutional_context": "national, Brazil",
    },
    {
        "study_id": "S1114",
        "study_design_class": "qualitative case study",
        "evidence_level": "high",
        "mechanism_family": "enforcement, sanction, discretion, participation (village by-law enforcement)",
        "outcome_family": "sanitation_access, service_coverage",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "village WASH by-laws, Njombe District Council",
        "institutional_context": "Njombe District Council, Tanzania",
    },
    {
        "study_id": "S1115",
        "study_design_class": "qualitative institutional case study (stakeholder interviews)",
        "evidence_level": "moderate",
        "mechanism_family": "discretion_accommodation, procedural_steps, bureaucratic_assistance, political_coordination (decentralization/privatization policy)",
        "outcome_family": "water_access, sanitation_access, service_coverage, service_continuity",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Uganda decentralization and privatization policy",
        "institutional_context": "8 districts, Uganda",
    },
    {
        "study_id": "S1116",
        "study_design_class": "comparative case study",
        "evidence_level": "high",
        "mechanism_family": "enforcement, tenure, property, planning, zoning (informal-settlement repression/acceptance)",
        "outcome_family": "water_access, sanitation_access, affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "informal-settlement land-use enforcement policy",
        "institutional_context": "4 East African cities",
    },
    {
        "study_id": "S1117",
        "study_design_class": "multi-country comparative documentation",
        "evidence_level": "high",
        "mechanism_family": "eligibility, disconnection, reconnection, hardship_exception, judicial_review, fees (COVID-19 emergency water-access policy)",
        "outcome_family": "water_access, affordability, service_continuity, service_coverage",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "COVID-19 emergency decrees/regulations, 14 countries",
        "institutional_context": "14 Global South countries (EfD network)",
    },
    {
        "study_id": "S1118",
        "study_design_class": "qualitative institutional/legal case study",
        "evidence_level": "high",
        "mechanism_family": "eligibility, tenure, property, planning, zoning, discretion (town planning scheme, legal status of constructions)",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "town planning scheme (TPS), Ahmedabad Municipal Corporation",
        "institutional_context": "Ahmedabad, India",
    },
    {
        "study_id": "S1119",
        "study_design_class": "mixed-methods case study (interviews, workshops, literature review)",
        "evidence_level": "moderate",
        "mechanism_family": "tenure, property, planning, discretion_accommodation, institutional_fragmentation, participation (landownership, governance capacity)",
        "outcome_family": "water_access, sanitation_access, affordability, service_continuity, refusal",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "decentralization policies, informal-settlement governance",
        "institutional_context": "Arusha (Tanzania), Dodowa (Ghana), Kampala (Uganda)",
    },
    {
        "study_id": "S1120",
        "study_design_class": "institutional/political-economy case study",
        "evidence_level": "high",
        "mechanism_family": "eligibility, service_area, fees, discretion_accommodation, planning (service-area/eligibility classification by ability-to-pay)",
        "outcome_family": "water_access, service_coverage, affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "GWSC/GWCL urban water privatization restructuring",
        "institutional_context": "national, Ghana",
    },
]

for nr in new_rows:
    assert nr["study_id"] not in existing_ids, nr["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
