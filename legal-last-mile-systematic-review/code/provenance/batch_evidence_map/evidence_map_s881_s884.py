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

add("S881", "historical econometric case study", "moderate-high", "documentation",
    "water_access", "FALSE", "TRUE",
    "Prussian wealth-weighted three-class electoral franchise",
    "municipal governments, waterworks investment decisions")

add("S882", "mixed-methods household survey with multiple regression analysis", "high", "formal_connection",
    "water_access", "TRUE", "TRUE",
    "utility connection fee/eligibility framework, Baguio City, Philippines",
    "Baguio Water District (BWD)")

add("S883", "mixed-methods descriptive study with institutional/policy analysis", "moderate-high", "institutional_fragmentation",
    "water_access", "FALSE", "TRUE",
    "National Water Policy, SDG 6, Ghana",
    "community groundwater point-source stakeholder governance")

add("S884", "quantitative welfare-distribution decomposition analysis", "high", "fees",
    "water_access", "FALSE", "TRUE",
    "2001 SAUR concession contract, Mali",
    "Energie du Mali (EDM), independent water/electricity regulator")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
