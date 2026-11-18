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
        "study_id": "S1140",
        "study_design_class": "quantitative regression-based institutional/administrative-mechanism study",
        "evidence_level": "high",
        "mechanism_family": "eligibility, discretion_accommodation, documentation, planning, service_area, procedural_steps, administrative_review, participation, political_coordination, bureaucratic_assistance, formal_connection, application_success, refusal (self-organized network-capital funding-allocation mechanism)",
        "outcome_family": "water_access, sanitation_access, service_coverage",
        "quantitative_synthesis_eligible": "TRUE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Rural Water Supply and Sanitation Program (RWSSP) competitive application funding",
        "institutional_context": "village communities, Nepal",
    },
]

for nr in new_rows:
    assert nr["study_id"] not in existing_ids, nr["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
