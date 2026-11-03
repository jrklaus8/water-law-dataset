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

add("S821", "household survey with informal-market census", "moderate-high", "documentation",
    "affordability", "FALSE", "TRUE",
    "public utility monopoly/regulatory status, limited connection coverage, Nigeria",
    "Anambra State Water Corporation, private water vending market")

add("S822", "quasi-experimental panel regression (repeated national cross-sectional survey)", "high", "eligibility",
    "water_access", "FALSE", "TRUE",
    "government slum legal notification status, India",
    "state and local governments, National Sample Survey")

add("S823", "constitutional/legal-doctrinal analysis", "high", "eligibility",
    "water_access", "FALSE", "TRUE",
    "1980 Constitution water-commodification provision, Indigenous water rights, Chile",
    "Chilean state, Mapuche communities")

add("S824", "qualitative government-programme case study", "moderate-high", "eligibility",
    "water_access", "FALSE", "TRUE",
    "government rainwater-harvesting programme eligibility mechanisms, China",
    "Gansu Water Conservancy Bureau, provincial/local government")

add("S825", "legal-doctrinal case analysis", "high", "disconnection",
    "affordability", "FALSE", "TRUE",
    "constitutional water-rights litigation, Free Basic Water Policy, prepayment meters, South Africa",
    "City of Johannesburg, Johannesburg Water, Constitutional Court")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
