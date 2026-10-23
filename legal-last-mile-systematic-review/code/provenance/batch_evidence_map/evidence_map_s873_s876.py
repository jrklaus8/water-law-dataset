#!/usr/bin/env python3
import csv, tempfile, os

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
EMAP = f"{BASE}/05_analysis/descriptive/evidence_map.csv"

with open(EMAP, newline="") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    rows = list(r)
    existing_ids = {row["study_id"] for row in rows}

def add(sid, study_design_class, evidence_level, mechanism_family, outcome_family,
        quant_eligible, qual_eligible, legal_context, institutional_context):
    assert sid not in existing_ids, f"{sid} already in evidence_map"
    rows.append({
        "study_id": sid,
        "study_design_class": study_design_class,
        "evidence_level": evidence_level,
        "mechanism_family": mechanism_family,
        "outcome_family": outcome_family,
        "quantitative_synthesis_eligible": quant_eligible,
        "qualitative_synthesis_eligible": qual_eligible,
        "legal_context": legal_context,
        "institutional_context": institutional_context,
    })

add("S873", "mixed-methods policy-arrangement case study", "moderate-high", "institutional_fragmentation",
    "water_access", "FALSE", "TRUE",
    "Water Services Industry Act 2006, SPANA Act, Malaysia",
    "National Water Services Commission, Pengurusan Aset Air Berhad, PBAPP, SADA")

add("S874", "fieldwork case study (field report)", "moderate-high", "eligibility",
    "water_access", "FALSE", "TRUE",
    "ODA-funded rural water entitlement scheme, Maharashtra, India",
    "village water committees, caste-based asset-ownership structures")

add("S875", "mixed-methods program-evaluation household survey", "high", "formal_connection",
    "water_access", "FALSE", "TRUE",
    "Dhaka/Chittagong metropolitan Water and Sewerage Authority connection rules",
    "WaterAid-Bangladesh, local NGO partners, community water-point management committees")

add("S876", "original survey research with newspaper content analysis", "moderate-high", "tenure",
    "water_access", "FALSE", "TRUE",
    "Papago Tribal Constitution, Southern Arizona Water Rights Settlement Act 1982, Spanish-derived acequia law",
    "Papago Tribal Council/Water Commissioners, Hispanic acequia associations")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
