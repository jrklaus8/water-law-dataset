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
        "study_id": "S1039",
        "study_design_class": "historical case study (municipal archival records)",
        "evidence_level": "moderate",
        "mechanism_family": "fees",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "municipal water-concession regime; private monopoly consolidation (SGAB)",
        "institutional_context": "Sociedad General de Aguas de Barcelona; Barcelona City Council",
    },
    {
        "study_id": "S1040",
        "study_design_class": "qualitative case study (interviews, focus groups)",
        "evidence_level": "moderate",
        "mechanism_family": "eligibility",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "DSK Model community-based water governance partnership",
        "institutional_context": "Dhaka Water Supply and Sewerage Authority (DWASA); DSK (NGO); community-based organizations",
    },
    {
        "study_id": "S1041",
        "study_design_class": "quantitative cross-sectional logistic regression",
        "evidence_level": "moderate",
        "mechanism_family": "fees",
        "outcome_family": "affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "water utility ownership structure (public vs. privatized)",
        "institutional_context": "U.S. community water systems; EPA SDWIS-Fed classification",
    },
]

for r in new_rows:
    assert r["study_id"] not in existing, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
