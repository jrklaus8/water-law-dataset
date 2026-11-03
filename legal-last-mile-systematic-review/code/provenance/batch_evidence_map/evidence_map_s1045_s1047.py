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
        "study_id": "S1045",
        "study_design_class": "systematic literature review (185 articles)",
        "evidence_level": "moderate",
        "mechanism_family": "eligibility",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "international/domestic indigenous water-rights recognition; joint management agreements; pluralistic legal systems",
        "institutional_context": "multi-country (concentrated US, Canada, New Zealand, Australia); government/development agencies",
    },
    {
        "study_id": "S1046",
        "study_design_class": "qualitative process-based analysis (interviews, participant observation)",
        "evidence_level": "high",
        "mechanism_family": "administrative_practice",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "utility operational/maintenance discretion within centralized network",
        "institutional_context": "Lilongwe Water Board, Malawi",
    },
    {
        "study_id": "S1047",
        "study_design_class": "qualitative case study (archival + 40 key-informant interviews)",
        "evidence_level": "high",
        "mechanism_family": "enforcement",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "judicial adjudication; Ministerio Publico rights-based advocacy",
        "institutional_context": "Brazilian courts; Sao Paulo metropolitan water/sanitation governance",
    },
]

for r in new_rows:
    assert r["study_id"] not in existing, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
