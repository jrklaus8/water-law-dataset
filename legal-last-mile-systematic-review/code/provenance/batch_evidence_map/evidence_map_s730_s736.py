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

add("S730", "research synthesis of primary multi-stakeholder research", "moderate", "participation",
    "effective_access", "FALSE", "TRUE",
    "municipal institutional capacity and national urban-biased delivery programmes",
    "The Water Dialogues, 8 South African municipalities")

add("S731", "historical-institutional case study", "moderate-high", "enforcement",
    "service_continuity", "FALSE", "TRUE",
    "permissive regulatory environment for private water companies",
    "private water companies, London, late 19th century")

add("S732", "institutional/legal policy analysis", "moderate-high", "documentation",
    "service_quantity", "FALSE", "TRUE",
    "South Africa's National Water Act 1998 permit/license system",
    "national water resources management authority, South Africa")

add("S733", "ethnographic case study", "high", "legal_status",
    "sanitation_access", "FALSE", "TRUE",
    "settlement legal status (illegal slums vs. legal resettlement colony)",
    "Delhi Jal Board vs. informal water vendors, South Delhi")

add("S734", "historical-institutional genealogy", "high", "legal_status",
    "service_coverage", "FALSE", "TRUE",
    "colonial and contemporary kampung/formal-settlement legal classification",
    "colonial and contemporary Jakarta water administration")

add("S735", "institutional/political-economy case study", "moderate", "institutional_fragmentation",
    "affordability", "FALSE", "TRUE",
    "national resource-governance reforms and local hybrid privatization",
    "BWUI public/private water utility, Tagbilaran City, Philippines")

add("S736", "institutional/policy case study", "moderate-high", "discretion_accommodation",
    "service_coverage", "FALSE", "TRUE",
    "Vietnam's Rural Water Supply (RWS) policy, formal vs. informal implementation",
    "state RWS programme institutions, Vietnam")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
