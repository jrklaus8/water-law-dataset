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

add("S885", "ethnographic case study with genealogical/documentary analysis", "high", "enforcement",
    "water_access", "FALSE", "TRUE",
    "prepaid water meter enforcement, Mazibuko constitutional case, South Africa",
    "Johannesburg Water, Operation Gcin'amanzi")

add("S886", "documentary policy analysis with supporting household survey data", "moderate-high", "fees",
    "water_access", "FALSE", "TRUE",
    "DAWASA privatisation concession contract, Tanzania",
    "City Water (Biwater/Gauff/Superdoll), DAWASCO, TGNP")

add("S887", "comparative case-design study using secondary administrative data", "moderate-high", "institutional_fragmentation",
    "water_access", "FALSE", "TRUE",
    "Local Government Code 1991, Philippines",
    "National Water Resources Board, Local Water Utilities Administration, city water districts")

add("S888", "historical institutional case study (archival/FOIA-based)", "high", "institutional_fragmentation",
    "water_access", "FALSE", "TRUE",
    "regional water-system governance structure, Detroit, Michigan",
    "Detroit Water and Sewerage Department, suburban wholesale-customer municipalities")

add("S889", "participatory action-research case study", "moderate-high", "fees",
    "water_access", "FALSE", "TRUE",
    "municipal street-hydrant system, Chittagong, Bangladesh",
    "Chittagong Water Supply and Sewerage Authority, community Water Committee")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
