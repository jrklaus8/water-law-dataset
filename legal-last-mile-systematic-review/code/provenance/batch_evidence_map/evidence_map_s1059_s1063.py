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
        "study_id": "S1059",
        "study_design_class": "qualitative governmentality/counter-conduct case study",
        "evidence_level": "moderate",
        "mechanism_family": "discretion_accommodation",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "government informal-settlement upgrading program vs. resident counter-conduct",
        "institutional_context": "Makhaza and New Rest, Cape Town, South Africa",
    },
    {
        "study_id": "S1060",
        "study_design_class": "mixed-methods household survey and interview study",
        "evidence_level": "moderate",
        "mechanism_family": "participation",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "voluntary-association-mediated voice/exit; property-documentation-based complaint eligibility",
        "institutional_context": "Lagos Water Corporation; Lagos and Benin City, Nigeria",
    },
    {
        "study_id": "S1061",
        "study_design_class": "program evaluation case study",
        "evidence_level": "moderate",
        "mechanism_family": "participation",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "NGO/government site-selection participation process",
        "institutional_context": "NGO Forum for Drinking Water Supply and Sanitation, rural Bangladesh",
    },
    {
        "study_id": "S1062",
        "study_design_class": "quantitative panel-data econometric study",
        "evidence_level": "high",
        "mechanism_family": "fees",
        "outcome_family": "service_coverage",
        "quantitative_synthesis_eligible": "TRUE",
        "qualitative_synthesis_eligible": "FALSE",
        "legal_context": "operation-and-maintenance cost-recovery ratio policy",
        "institutional_context": "water utilities, 22 Sub-Saharan African countries",
    },
    {
        "study_id": "S1063",
        "study_design_class": "statutory/legal-policy analysis",
        "evidence_level": "high",
        "mechanism_family": "eligibility",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "National Water Act 1998 licence system; Priority General Authorisations proposal",
        "institutional_context": "national/provincial water-licensing authorities, South Africa",
    },
]

for r in new_rows:
    assert r["study_id"] not in existing, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
