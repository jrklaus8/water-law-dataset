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

add("S854", "institutional/political-governance case study", "high", "participation",
    "water_access", "FALSE", "TRUE",
    "SEMAPA remunicipalization, 'social control' participatory governance, Bolivia",
    "SEMAPA public utility, autonomous small-scale providers")

add("S855", "comparative household survey with institutional benchmark data", "high", "fees",
    "water_access", "FALSE", "TRUE",
    "Community Ownership and Management model, district assembly trusteeship, Ghana",
    "WSMTs, district assemblies, CWSA")

add("S856", "comparative institutional case study", "high", "fees",
    "water_access", "FALSE", "TRUE",
    "cross-subsidy/bulk-water lease/landowner contracts, Vietnam/Cambodia/Indonesia",
    "PPWSA, HWBC, Can Tho Water Company, PDAM")

add("S857", "ethnographic case study", "moderate-high", "eligibility",
    "water_access", "FALSE", "TRUE",
    "customary land-tenure water rights vs. state cost-recovery framework, Nigeria",
    "traditional institutions, Cross River Basin Development Authority")

add("S858", "longitudinal ethnographic case study", "high", "eligibility",
    "affordability", "FALSE", "TRUE",
    "2002 national water policy decentralization mandate, Tanzania",
    "Uchira Water Users Association")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
