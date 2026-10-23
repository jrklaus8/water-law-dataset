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

add("S754", "ethnographic case study", "high", "legal_status",
    "service_reliability", "FALSE", "TRUE",
    "criminalization of water infrastructure mediating legal reclassification of a settlement",
    "Mumbai Municipal Corporation water department, Shivajinagar-Bainganwadi, India")

add("S755", "case study synthesis", "moderate-high", "tenure",
    "service_coverage", "FALSE", "TRUE",
    "Water Reserve land-use declarations over private land with eviction powers; unenacted water-ownership legislation",
    "national government, South/North Tarawa and outer islands, Kiribati")

add("S756", "qualitative case study", "moderate", "institutional_fragmentation",
    "service_coverage", "FALSE", "TRUE",
    "Strategic Framework for Water Services 2003 district water sector plan requirement",
    "Dr Kenneth Kaunda District Municipality, South Africa")

add("S757", "cross-sectional users' satisfaction survey", "moderate-high", "enforcement",
    "service_quality", "FALSE", "TRUE",
    "public/private/community institutional arrangements for sanitation delivery",
    "local government waste management departments, Accra/Kumasi/Tema, Ghana")

add("S758", "structural econometric model with counterfactual simulation", "moderate-high", "enforcement",
    "affordability", "FALSE", "TRUE",
    "rate-of-return regulation under asymmetric information",
    "California Public Utilities Commission, 32 water districts, USA")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
