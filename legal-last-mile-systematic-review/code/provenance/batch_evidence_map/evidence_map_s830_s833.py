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

add("S830", "institutional/historical infrastructure-coverage case study", "moderate-high", "documentation",
    "water_access", "FALSE", "TRUE",
    "administrative-law disruption via utility privatization/re-regulation, Brazil",
    "SABESP, municipal/state utility structures, Sao Paulo")

add("S831", "comparative qualitative institutional case study", "high", "institutional_fragmentation",
    "water_access", "FALSE", "TRUE",
    "working rules and accountability mechanisms, community-based water organizations, Costa Rica",
    "1,000+ CBDWOs serving 60% of rural population")

add("S832", "longitudinal ethnographic case study", "high", "fees",
    "water_access", "FALSE", "TRUE",
    "hybrid neoliberal governance reform, payment-for-accountability design, India",
    "Government of Rajasthan, village community-participation institutions")

add("S833", "ethnographic case study with descriptive household tables", "high", "fees",
    "water_access", "FALSE", "TRUE",
    "formally-registered community water organization, connection-fee governance, Sri Lanka",
    "Vishaka Women's Society, Pradeshiya Sabha local government")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
