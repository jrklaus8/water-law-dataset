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
        "study_id": "S1148",
        "study_design_class": "qualitative comparative institutional-capacity case study",
        "evidence_level": "moderate",
        "mechanism_family": "burden, discretion_accommodation, planning, service_area, fees, discretion, institutional_fragmentation, political_coordination, formal_connection (water-utility institutional-capacity comparison)",
        "outcome_family": "water_access, service_coverage, service_reliability, affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "municipal water-utility institutional-capacity/governance comparison",
        "institutional_context": "Saltillo and Hermosillo municipal water utilities, Mexico",
    },
    {
        "study_id": "S1149",
        "study_design_class": "qualitative institutional/regulatory-reform case study",
        "evidence_level": "moderate",
        "mechanism_family": "discretion_accommodation, enforcement, planning, service_area, discretion, participation, institutional_fragmentation, political_coordination (EU Water Framework Directive regulatory transition)",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "EU Water Framework Directive-driven national water-governance paradigm shift",
        "institutional_context": "national water-governance authorities, Spain and Portugal",
    },
    {
        "study_id": "S1150",
        "study_design_class": "qualitative institutional/legal-mechanism case study",
        "evidence_level": "moderate",
        "mechanism_family": "eligibility, burden, discretion_accommodation, tenure, property, planning, zoning, service_area, fees, discretion, institutional_fragmentation, political_coordination, formal_connection (multi-agency legal fragmentation and informal-settlement status)",
        "outcome_family": "water_access, sanitation_access, service_coverage, service_reliability, service_quantity",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "multi-agency water/sanitation governance fragmentation; KWSB Act 1996; formal/informal settlement status",
        "institutional_context": "Karachi Water & Sewerage Board, Karachi, Pakistan",
    },
]

for nr in new_rows:
    assert nr["study_id"] not in existing_ids, nr["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
