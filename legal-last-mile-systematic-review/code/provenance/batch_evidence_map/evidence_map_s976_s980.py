#!/usr/bin/env python3
import csv
import tempfile
import os

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
        "study_id": "S976",
        "study_design_class": "policy/legal review article with national program analysis",
        "evidence_level": "moderate",
        "mechanism_family": "legal_status",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "National Water Act (Act No. 36 of 1998), Water Services Act (Act No. 108 of 1997), ss.61/62 financial-assistance provisions",
        "institutional_context": "Department of Water Affairs and Forestry (DWAF) Pilot Programme for domestic rainwater harvesting",
    },
    {
        "study_id": "S977",
        "study_design_class": "cross-sectional mixed-methods household survey",
        "evidence_level": "high",
        "mechanism_family": "fees",
        "outcome_family": "sanitation_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Major Village Infrastructure Programme cost-recovery-for-O&M-only institutional policy",
        "institutional_context": "government-funded capital connection cost, household connection-fee and tariff structure",
    },
    {
        "study_id": "S978",
        "study_design_class": "cross-sectional mixed-methods case study",
        "evidence_level": "high",
        "mechanism_family": "participation",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Ghana National Community Water and Sanitation Programme",
        "institutional_context": "Water and Sanitation Management Teams (WSMTs), WATSAN committees, Water Management Boards (WMBs)",
    },
    {
        "study_id": "S979",
        "study_design_class": "legal/documentary analysis",
        "evidence_level": "high",
        "mechanism_family": "institutional_fragmentation",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "Palestinian Water Law No. 3 (2002); Hague Regulations 1907; Fourth Geneva Convention 1949; ICESCR",
        "institutional_context": "Palestinian Water Authority, Oslo II Areas A/B/C jurisdictional division, Israeli occupation authority",
    },
    {
        "study_id": "S980",
        "study_design_class": "cross-sectional mixed-methods household survey",
        "evidence_level": "moderate",
        "mechanism_family": "enforcement",
        "outcome_family": "sanitation_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "urban planning/environmental sanitation regulatory regime, Ghana",
        "institutional_context": "municipal planning authority (Wa municipality); limited monitoring systems, inadequate logistics and personnel",
    },
]

for r in new_rows:
    assert r["study_id"] not in existing_ids, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"evidence_map.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
