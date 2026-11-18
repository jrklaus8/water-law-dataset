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

add("S838", "ethnographic case study", "high", "eligibility",
    "water_access", "FALSE", "TRUE",
    "Water Act 1998 s.32(1) primary vs. commercial water classification, Zimbabwe",
    "ZINWA, catchment councils")

add("S839", "legal-doctrinal case study", "moderate-high", "fees",
    "water_access", "FALSE", "TRUE",
    "Mazibuko v City of Johannesburg litigation, Free Basic Water policy, South Africa",
    "City of Johannesburg, Johannesburg Water")

add("S840", "institutional/regulatory case study", "moderate-high", "institutional_fragmentation",
    "water_access", "FALSE", "TRUE",
    "Tennessee State Utility District Act of 1937, special water utility districts, USA",
    "City of Nashville, four suburban special utility districts")

add("S841", "national survey-based quantitative study (multinomial logistic regression)", "moderate", "institutional_fragmentation",
    "affordability", "FALSE", "TRUE",
    "institutional trust (legislative, executive, judicial), Ghana",
    "national Afrobarometer survey, courts and executive")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
