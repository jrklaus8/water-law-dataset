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

add("S737", "mixed-methods field study", "moderate-high", "eligibility",
    "service_coverage", "FALSE", "TRUE",
    "caste-blind numerical siting criterion for public water infrastructure (one source per 250 population)",
    "state rural water supply programme, Madhya Pradesh/Bihar/Jharkhand, India")

add("S738", "cross-sectional survey", "moderate", "enforcement",
    "affordability", "FALSE", "TRUE",
    "weak regulatory enforcement and inter-agency coordination over informal water vendors",
    "KIWASCO corporatised municipal utility, informal settlements, Kisumu, Kenya")

add("S739", "qualitative multi-case comparative case study", "high", "discretion_accommodation",
    "service_coverage", "FALSE", "TRUE",
    "constitutional right to water, Free Basic Water Policy, Municipal Structures Act spatial differentiation",
    "eThekwini Water and Sanitation Unit, Durban, South Africa")

add("S740", "quasi-experimental multivariate regression", "moderate-high", "institutional_fragmentation",
    "service_quantity", "FALSE", "TRUE",
    "centralised vs. decentralised government management of rural water utilities",
    "Public Health Engineering Department vs. panchayats, Madhya Pradesh/Chhattisgarh, India")

add("S741", "comparative qualitative discourse analysis", "moderate", "enforcement",
    "service_coverage", "FALSE", "TRUE",
    "legal human right to water and sanitation (HRtWS) implementation discourse",
    "UN Special Rapporteur on HRtWS; national water utilities, Bolivia")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
