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
        "study_id": "S1034",
        "study_design_class": "quasi-experimental difference-in-difference panel analysis",
        "evidence_level": "high",
        "mechanism_family": "planning",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Law 142 of 1994 (household public utilities regime); Law 60 of 1993 decentralization",
        "institutional_context": "municipalities; specialized public/private/mixed water and sewerage companies (EICE/ESP)",
    },
    {
        "study_id": "S1035",
        "study_design_class": "qualitative mixed-methods study",
        "evidence_level": "moderate",
        "mechanism_family": "fees",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "centralized tariff-approval regime requiring central-government permission for municipal tariff changes",
        "institutional_context": "urban municipal councils; Zimbabwe National Water Authority (ZINWA)",
    },
    {
        "study_id": "S1036",
        "study_design_class": "dynamic panel system GMM regression",
        "evidence_level": "high",
        "mechanism_family": "enforcement",
        "outcome_family": "sanitation_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "World Governance Indicators (corruption control, regulatory quality, voice and accountability, rule of law, government effectiveness)",
        "institutional_context": "national governments of 44 sub-Saharan African countries",
    },
    {
        "study_id": "S1037",
        "study_design_class": "qualitative case study",
        "evidence_level": "moderate",
        "mechanism_family": "participation",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "1992 Rio Declaration/Agenda 21 gender-mainstreaming commitments; community-led water management",
        "institutional_context": "community water-management groups (Mulheres das Aguas; MMTR-SC)",
    },
    {
        "study_id": "S1038",
        "study_design_class": "quantitative econometric welfare-loss estimation",
        "evidence_level": "high",
        "mechanism_family": "fees",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "TRUE",
        "qualitative_synthesis_eligible": "FALSE",
        "legal_context": "state public utility commission regulation vs. local (city council/water commission) regulation",
        "institutional_context": "municipally-owned water utilities (95 U.S. utilities, 1965 AWWA survey)",
    },
]

for r in new_rows:
    assert r["study_id"] not in existing, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
