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

add("S716", "institutional/ethnographic case study", "moderate-high", "discretion_accommodation",
    "affordability", "FALSE", "TRUE",
    "colonial-legacy centralized water infrastructure and decentralization proposals",
    "Darjeeling Waterworks Department vs. informal private tanker ('water mafia') network")

add("S717", "legal-doctrinal analysis", "moderate-high", "administrative_review",
    "effective_access", "FALSE", "TRUE",
    "South Africa's Promotion of Administrative Justice Act (PAJA); constitutional right to water",
    "administrative-law safeguards in water privatization")

add("S718", "institutional case study", "high", "fees",
    "service_coverage", "FALSE", "TRUE",
    "national legislation mandating stratified (income-differentiated) water tariff pricing",
    "EAAB public water utility, Bogota, Colombia")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
