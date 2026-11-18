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

add("S804", "descriptive utility-performance case study", "moderate", "documentation",
    "affordability", "FALSE", "TRUE",
    "statutory full-cost-recovery mandate, Water Works Act 1995, Malawi",
    "Blantyre Water Board, low-income customer interviews")

add("S805", "institutional/legal case study", "high", "institutional_fragmentation",
    "water_access", "FALSE", "TRUE",
    "UNMIK Regulations and Laws consolidating water utilities, independent economic regulator, Kosova",
    "7 Regional Water Companies, Water and Waste Regulatory Office")

add("S806", "qualitative institutional case study", "high", "documentation",
    "water_access", "FALSE", "TRUE",
    "land-tenure regularization requirement for WS&S universal access, Brazil",
    "SABESP state water utility, Sao Paulo state government")

add("S807", "household survey with institutional/regulatory analysis", "moderate-high", "eligibility",
    "affordability", "FALSE", "TRUE",
    "economic regulation of private water-management contract, Jordan",
    "quasi-regulator, water authorities, private management contractor, Amman")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
