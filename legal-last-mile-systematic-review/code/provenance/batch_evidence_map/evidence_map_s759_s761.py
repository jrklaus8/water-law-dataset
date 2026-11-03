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

add("S759", "theoretical/comparative institutional analysis", "moderate-high", "enforcement",
    "service_coverage", "FALSE", "TRUE",
    "privatization vs. commercialization/regulatory change of water utilities",
    "private water companies and public utilities, global South cities")

add("S760", "field research case study", "moderate-high", "enforcement",
    "affordability", "FALSE", "TRUE",
    "market-competition/formalization policy for small-scale independent water providers",
    "informal water market, Maputo, Mozambique")

add("S761", "quasi-experimental comparative field study", "high", "discretion_accommodation",
    "affordability", "FALSE", "TRUE",
    "Kenya Water Act 2002 commercialization framework, delegated management model",
    "KIWASCO utility and master-/kiosk-operators, Kisumu, Kenya")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
