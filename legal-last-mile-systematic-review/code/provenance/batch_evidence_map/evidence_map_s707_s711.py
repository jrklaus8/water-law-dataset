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

add("S707", "policy analysis", "moderate-high", "tenure",
    "sanitation_access", "FALSE", "TRUE",
    "national urban sanitation policy framework (National Urban Sanitation Policy, Swachh Bharat Mission)",
    "tenure/legal status of settlements shaping sanitation access for the urban poor, India")

add("S708", "comparative case study (political economy)", "moderate-high", "institutional_fragmentation",
    "service_coverage", "FALSE", "TRUE",
    "74th Constitutional Amendment decentralization reform",
    "political clientelism and elite capture of water supply decentralization, Kolkata slums, India")

add("S709", "institutional/legal case study", "moderate-high", "property",
    "affordability", "FALSE", "TRUE",
    "de jure/de facto groundwater rights gap; Rajasthan Water Policy",
    "state water sector institutional reform, Rajasthan, India")

add("S710", "institutional/policy analysis", "high", "institutional_fragmentation",
    "service_coverage", "FALSE", "TRUE",
    "1992/2004 Mexican Water Law reforms creating decentralized Basin Organisms; NOM-001 wastewater norm",
    "National Water Commission decentralization, Mexico")

add("S711", "descriptive field study", "moderate", "tenure",
    "formal_connection", "FALSE", "TRUE",
    "absence of slum-regularization legislation for unauthorized colonies",
    "unauthorized/encroached slum colonies, Panchkula, Haryana, India")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
