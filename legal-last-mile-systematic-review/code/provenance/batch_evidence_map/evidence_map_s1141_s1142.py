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
        "study_id": "S1141",
        "study_design_class": "qualitative ethnographic institutional/legal-mechanism case study",
        "evidence_level": "moderate",
        "mechanism_family": "eligibility, burden, discretion_accommodation, enforcement, documentation, tenure, property, planning, zoning, service_area, procedural_steps, delay, discretion, administrative_review, complaint, sanction, participation, institutional_fragmentation, political_coordination, formal_connection, application_success, refusal, delay_outcome (informal-settlement legal-status service-eligibility mechanism)",
        "outcome_family": "water_access, service_coverage",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "informal-settlement legal recognition/formalisation as precondition for municipal service extension",
        "institutional_context": "Tlokwe municipality, Marikana informal settlement, Potchefstroom, South Africa",
    },
    {
        "study_id": "S1142",
        "study_design_class": "qualitative/descriptive policy case study",
        "evidence_level": "moderate",
        "mechanism_family": "eligibility, burden, discretion_accommodation, enforcement, planning, service_area, fees, procedural_steps, delay, discretion, hardship_exception, administrative_review, complaint, disconnection, reconnection, sanction, participation, institutional_fragmentation, political_coordination, formal_connection, delay_outcome (cost-recovery/disconnection mechanism)",
        "outcome_family": "water_access, service_coverage, service_reliability, affordability, service_continuity",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "post-apartheid municipal water cost-recovery and disconnection-for-non-payment policy",
        "institutional_context": "Cape Town local government, townships, South Africa",
    },
]

for nr in new_rows:
    assert nr["study_id"] not in existing_ids, nr["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
