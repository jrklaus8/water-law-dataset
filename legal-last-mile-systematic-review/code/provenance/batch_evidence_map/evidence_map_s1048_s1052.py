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
        "study_id": "S1048",
        "study_design_class": "descriptive/institutional policy analysis (national administrative data)",
        "evidence_level": "moderate",
        "mechanism_family": "regulatory_model",
        "outcome_family": "service_coverage",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "PLANASA concession model; 2007 National Sanitation Law (Law 11,445)",
        "institutional_context": "state-owned WSS utilities vs. municipal utilities, Brazil",
    },
    {
        "study_id": "S1049",
        "study_design_class": "qualitative case study (interviews, observation)",
        "evidence_level": "moderate",
        "mechanism_family": "fees",
        "outcome_family": "affordability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "unregulated emptying-fee pricing; institutional fragmentation",
        "institutional_context": "Kampala City Council Authority (KCCA), Uganda",
    },
    {
        "study_id": "S1050",
        "study_design_class": "comparative multi-case-study analysis (11 metropolitan areas)",
        "evidence_level": "high",
        "mechanism_family": "regulatory_model",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "economic regulation of water services in developing economies",
        "institutional_context": "11 metropolitan areas, Africa and Asia",
    },
    {
        "study_id": "S1051",
        "study_design_class": "mixed-methods case study (household surveys, interviews)",
        "evidence_level": "moderate",
        "mechanism_family": "eligibility",
        "outcome_family": "sanitation_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "facility-governance-structure-dependent eligibility and fees",
        "institutional_context": "informal settlements, Kampala (Uganda) and Dar es Salaam (Tanzania)",
    },
    {
        "study_id": "S1052",
        "study_design_class": "program case study / process evaluation",
        "evidence_level": "moderate",
        "mechanism_family": "participation",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "participatory Ward Water Committee site-selection process",
        "institutional_context": "Kerala Water Authority; Socio-Economic Units, India",
    },
]

for r in new_rows:
    assert r["study_id"] not in existing, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
