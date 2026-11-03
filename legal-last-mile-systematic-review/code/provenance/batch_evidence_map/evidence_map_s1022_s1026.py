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
        "study_id": "S1022",
        "study_design_class": "case study (ethnographic observation, documentary/legal analysis)",
        "evidence_level": "high",
        "mechanism_family": "legal_status",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "73rd/74th Constitutional Amendments empowering panchayats over natural resources",
        "institutional_context": "panchayat (local governing body), Joint Parliamentary Committee",
    },
    {
        "study_id": "S1023",
        "study_design_class": "qualitative case study (community workshops, semi-structured interviews)",
        "evidence_level": "high",
        "mechanism_family": "fees",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "differentiated connection technology and tiered free-basic-water tariff system",
        "institutional_context": "eThekwini Water Services",
    },
    {
        "study_id": "S1024",
        "study_design_class": "case study (key-informant interviews, documentary analysis)",
        "evidence_level": "moderate",
        "mechanism_family": "participation",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "'Social Control' participatory-governance model; elected Citizen Directors",
        "institutional_context": "SEMAPA (Cochabamba public water and sanitation company)",
    },
    {
        "study_id": "S1025",
        "study_design_class": "quantitative regression analysis (heterogeneous choice ordinal models, household survey)",
        "evidence_level": "moderate",
        "mechanism_family": "tenure",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "TRUE",
        "qualitative_synthesis_eligible": "FALSE",
        "legal_context": "formal vs. informal dwelling-title ownership; community/government water-service-establishment status",
        "institutional_context": "municipal water service authorities, San Salvador",
    },
    {
        "study_id": "S1026",
        "study_design_class": "case study (institutional/political-economy analysis, household distribution data)",
        "evidence_level": "high",
        "mechanism_family": "political_coordination",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "principal-agent institutional-accountability structure (state-legislature-accountable water board)",
        "institutional_context": "Chennai Metropolitan Water Supply and Sewerage Board (Metro Water Board)",
    },
]

for r in new_rows:
    assert r["study_id"] not in existing, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
