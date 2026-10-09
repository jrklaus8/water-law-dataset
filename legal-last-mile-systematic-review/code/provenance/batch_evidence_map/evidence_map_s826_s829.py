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

add("S826", "ethnographic case study", "high", "eligibility",
    "water_access", "FALSE", "TRUE",
    "1995 settlement-cutoff eligibility rule, discretionary accommodation, India",
    "Mumbai Municipal Corporation water department")

add("S827", "ethnographic case study", "high", "institutional_fragmentation",
    "affordability", "FALSE", "TRUE",
    "Community-Based Management devolution and water pricing, Namibia",
    "communal water-point committees, Ministry of Agriculture Water and Forestry")

add("S828", "comparative policy/legal-text discourse analysis", "moderate-high", "documentation",
    "water_access", "FALSE", "TRUE",
    "national WatSan law tenure/housing provisions, Brazil",
    "national/municipal water and sanitation providers")

add("S829", "cross-cultural qualitative interview study", "moderate-high", "institutional_fragmentation",
    "affordability", "FALSE", "TRUE",
    "institutional rules and norms across four national contexts",
    "local water institutions, Bolivia/Fiji/Arizona/New Zealand")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
