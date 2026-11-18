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

add("S834", "ethnographic case study", "high", "eligibility",
    "water_access", "FALSE", "TRUE",
    "1995 settlement-cutoff eligibility rule, water-audit/privatization politics, India",
    "Mumbai Municipal Corporation water department")

add("S835", "institutional/regulatory case study", "high", "documentation",
    "water_access", "FALSE", "TRUE",
    "15-year mixed public-private service contract under Public Water Supply and Sewerage Act, Estonia",
    "mixed public-private water company, municipal supervisory authority")

add("S836", "documentary/policy analysis", "moderate-high", "documentation",
    "water_access", "FALSE", "TRUE",
    "Law 142/1994, Decree 1898/2016 differentiated schemes, absence of legal recognition, Colombia",
    "community water-management associations, PDET post-conflict program")

add("S837", "quantitative panel study (hierarchical Bayesian regression)", "high", "institutional_fragmentation",
    "water_access", "FALSE", "TRUE",
    "special purpose water district fragmentation, regulatory enforcement, USA",
    "500+ special purpose water districts, Houston metro area")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
