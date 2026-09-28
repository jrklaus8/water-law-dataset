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

add("S798", "qualitative policy-document analysis with key-informant interviews", "moderate-high", "institutional_fragmentation",
    "water_access", "FALSE", "TRUE",
    "absence of enabling legislation blocking Catchment Management Authorities, Malawi",
    "Ministry of Water Development, proposed river-basin authorities")

add("S799", "policy-document analysis with descriptive water-quality sampling", "moderate-high", "documentation",
    "water_access", "FALSE", "TRUE",
    "JNNURM urban reform conditions, land-tenure documentation, Delhi India",
    "municipal government, Delhi Jal Board, resettlement colonies")

add("S800", "cross-sectional municipal regression and comparison analysis", "moderate", "institutional_fragmentation",
    "water_access", "FALSE", "TRUE",
    "local vs. central administrative authority over water infrastructure, Kenya",
    "32-35 Kenyan municipalities")

add("S801", "qualitative key-informant interview study", "moderate-high", "discretion_accommodation",
    "water_access", "FALSE", "TRUE",
    "potable water regulation capacity/transparency, Tijuana Mexico",
    "Ministry of Public Health, CESPT water utility")

add("S802", "cross-sectional survey of water-sector governance and pricing", "moderate-high", "institutional_fragmentation",
    "affordability", "FALSE", "TRUE",
    "fragmented decentralised rural/public water-pricing regulation, Ireland",
    "34 local authorities, 104 Group Water Schemes")

add("S803", "qualitative semi-structured interview study", "moderate-high", "political_coordination",
    "service_quality", "FALSE", "TRUE",
    "institutional determinants of municipal water-service quality, Guatemala",
    "municipal water-service officials")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
