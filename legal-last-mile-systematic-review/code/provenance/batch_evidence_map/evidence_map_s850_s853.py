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

add("S850", "comparative household survey with multivariate regression", "high", "eligibility",
    "affordability", "FALSE", "TRUE",
    "Zonal Improvement Program tenure legalization, Philippines",
    "National Housing Authority ZIP program")

add("S851", "comparative institutional case study", "high", "institutional_fragmentation",
    "water_access", "FALSE", "TRUE",
    "water privatization concession contracts, investor type, Argentina",
    "14 concessionaires, Corrientes provincial regulator")

add("S852", "comparative institutional/legal-text case study", "high", "fees",
    "water_access", "FALSE", "TRUE",
    "Water Services Act 1997 private-provider provision, South Africa",
    "municipal water-services authorities, private concessionaires")

add("S853", "cross-national panel regression study", "moderate-high", "institutional_fragmentation",
    "water_access", "FALSE", "TRUE",
    "World Bank governance indicators (rule of law, regulatory quality), multi-country",
    "national governance/institutional capacity")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
