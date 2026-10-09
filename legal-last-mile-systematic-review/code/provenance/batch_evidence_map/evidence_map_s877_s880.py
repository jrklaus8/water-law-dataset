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

add("S877", "historical institutional case study", "moderate-high", "enforcement",
    "water_access", "FALSE", "TRUE",
    "colonial-era municipal sanitary regulation and English water concession, Tangier",
    "international Sanitary Council, makhzan administration")

add("S878", "comparative case-study analysis", "moderate-high", "fees",
    "water_access", "FALSE", "TRUE",
    "1985 New Economic Policy / capitalization law, Bolivia",
    "Aguas de Tunari, Aguas del Illimani, Coordinadora, Federacion de Juntas Vecinales")

add("S879", "randomized controlled trial", "high", "enforcement",
    "water_access", "TRUE", "TRUE",
    "utility connection-loan contract disconnection clause, Nairobi",
    "Nairobi City Water and Sewerage Company")

add("S880", "qualitative interview-based political-economy study", "moderate-high", "documentation",
    "water_access", "FALSE", "TRUE",
    "Human Right to Water and Sanitation, local licensing/regulatory frameworks, Vietnam/Cambodia/Indonesia",
    "local government WASH-market regulators, small-scale enterprises")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
