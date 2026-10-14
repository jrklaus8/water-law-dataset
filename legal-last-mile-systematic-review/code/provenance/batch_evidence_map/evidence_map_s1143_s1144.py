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
        "study_id": "S1143",
        "study_design_class": "quantitative regression-based institutional/administrative-mechanism study",
        "evidence_level": "high",
        "mechanism_family": "discretion_accommodation, enforcement, planning, service_area, procedural_steps, discretion, complaint, political_coordination (administrative service-delivery rules mechanism)",
        "outcome_family": "sanitation_access, service_coverage, service_reliability, service_quantity",
        "quantitative_synthesis_eligible": "TRUE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "municipal administrative service-delivery rules (route/resource allocation)",
        "institutional_context": "City of Detroit Sanitation Division and Environmental Enforcement Division, Michigan, USA",
    },
    {
        "study_id": "S1144",
        "study_design_class": "quantitative regression-based institutional/administrative-assistance-mechanism study",
        "evidence_level": "high",
        "mechanism_family": "eligibility, burden, discretion_accommodation, planning, service_area, fees, procedural_steps, participation, institutional_fragmentation, bureaucratic_assistance, formal_connection, application_success, refusal (social-proximity/trust-based NGO/CBO access mechanism)",
        "outcome_family": "sanitation_access, service_coverage, service_reliability, service_quality, affordability",
        "quantitative_synthesis_eligible": "TRUE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "NGO/CBO-supplied sanitation service provision in unrecognized informal settlements",
        "institutional_context": "Kampala slums, Uganda",
    },
]

for nr in new_rows:
    assert nr["study_id"] not in existing_ids, nr["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
