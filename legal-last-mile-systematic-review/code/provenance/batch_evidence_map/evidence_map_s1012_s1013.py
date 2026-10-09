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
        "study_id": "S1012",
        "study_design_class": "case study (household survey, community-institutional documentation)",
        "evidence_level": "moderate",
        "mechanism_family": "discretion",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "SEDALIB institutional water-rationing policy",
        "institutional_context": "SEDALIB municipal water enterprise, Comite de Agua neighborhood water committee",
    },
    {
        "study_id": "S1013",
        "study_design_class": "action-research case study (interviews, stakeholder-dialogue forum, documentary analysis)",
        "evidence_level": "high",
        "mechanism_family": "eligibility",
        "outcome_family": "sanitation_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "municipal connection-eligibility rules (legal property ownership/tax-currency, later relaxed)",
        "institutional_context": "municipal government, traditional Mayan alcaldia/cofradia (historical), neighborhood alley committees",
    },
]

for r in new_rows:
    assert r["study_id"] not in existing, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
