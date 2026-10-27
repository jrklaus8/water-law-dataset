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

add("S808", "comparative institutional case study", "high", "enforcement",
    "water_access", "FALSE", "TRUE",
    "central-government non-enforcement of municipal accountability regulations, South Africa",
    "18 municipality profiles, Eastern and Western Cape")

add("S809", "qualitative political-economy case study", "high", "discretion_accommodation",
    "water_access", "FALSE", "TRUE",
    "clientelist political-settlement dynamics, private-sector-participation arrangements, Ghana",
    "Ghana Water Company Limited")

add("S810", "ethnographic political-geography case study", "high", "documentation",
    "water_access", "FALSE", "TRUE",
    "informal land-tenure status, formal/informal governance distinction, Mexico border",
    "municipal utility and government officials, Nogales Sonora")

add("S811", "institutional/fiscal case study", "high", "institutional_fragmentation",
    "affordability", "FALSE", "TRUE",
    "post-communist decentralization, provincial water enterprise capacity, Cambodia",
    "provincial water enterprise, private vendors, community/NGO wells")

add("S812", "qualitative stakeholder case study", "high", "institutional_fragmentation",
    "affordability", "FALSE", "TRUE",
    "overlapping stakeholder governance of public water kiosks, Malawi",
    "Blantyre Water Board, Blantyre City Assembly, kiosk committees")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
