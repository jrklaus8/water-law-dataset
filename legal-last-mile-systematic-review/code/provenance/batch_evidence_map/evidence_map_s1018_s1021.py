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
        "study_id": "S1018",
        "study_design_class": "documentary/policy review (new-institutional-economics framework, case-law analysis)",
        "evidence_level": "high",
        "mechanism_family": "eligibility",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Water Act 1968 Section 6 borehole-permission regime; no constitutional right to water",
        "institutional_context": "Water Utilities Corporation, government agencies administering the Water Act",
    },
    {
        "study_id": "S1019",
        "study_design_class": "mixed-methods (798-project primary dataset, qualitative enquiry)",
        "evidence_level": "high",
        "mechanism_family": "political_coordination",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Mahatma Gandhi National Rural Employment Guarantee Act (MGNREGA)",
        "institutional_context": "elected village panchayats",
    },
    {
        "study_id": "S1020",
        "study_design_class": "quasi-experimental (propensity score matching, treatment/control watersheds)",
        "evidence_level": "high",
        "mechanism_family": "political_coordination",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "TRUE",
        "qualitative_synthesis_eligible": "FALSE",
        "legal_context": "government watershed-development institutional intervention (rural-development policy instrument)",
        "institutional_context": "Rajiv Gandhi Mission for Watershed Development",
    },
    {
        "study_id": "S1021",
        "study_design_class": "historical-institutional analysis (secondary/documentary sources, Census data)",
        "evidence_level": "high",
        "mechanism_family": "eligibility",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "1888 Bombay Municipal Corporation Act; notified/non-notified slum eligibility classification",
        "institutional_context": "Municipal Corporation of Greater Mumbai (MCGM), hydraulic department",
    },
]

for r in new_rows:
    assert r["study_id"] not in existing, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
