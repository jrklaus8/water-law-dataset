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

add("S719", "political-economy case study", "moderate-high", "fees",
    "affordability", "FALSE", "TRUE",
    "Private Sector Participation (PSP) policy and World Bank-mandated lease contract",
    "Ghana Water Company privatization politics")

add("S720", "historical-institutional case study", "moderate-high", "documentation",
    "formal_connection", "FALSE", "TRUE",
    "municipal permit system for private sewer connections",
    "Morelia, Mexico municipal government, 1880-1930")

add("S721", "mixed-methods fieldwork study", "moderate-high", "discretion_accommodation",
    "effective_access", "FALSE", "TRUE",
    "differential regulation of state vs. non-state water-market actors",
    "hybrid urban water markets, Lagos and Benin City, Nigeria")

add("S722", "comparative multi-city institutional study", "high", "enforcement",
    "service_coverage", "FALSE", "TRUE",
    "state utility monopoly-rights laws; Peru's water-management law; Paraguay's SENASA performance-based regulation",
    "independent/informal small-scale water and sanitation providers, multi-country")

add("S723", "spatial regression (ecological/neighborhood-level)", "moderate-high", "planning",
    "formal_connection", "FALSE", "TRUE",
    "colonias/colonias populares outside formal municipal annexation; institutional racism; national budgeting process",
    "binational municipal utilities, El Paso, Texas and Ciudad Juarez, Mexico")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
