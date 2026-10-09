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

add("S842", "institutional/political-economy case study", "high", "fees",
    "water_access", "FALSE", "TRUE",
    "below-cost tariff/utility financing, clientelist politics, Ecuador",
    "municipal public water utility, invasion settlements")

add("S843", "urban political ecology case study with household survey", "high", "documentation",
    "water_access", "FALSE", "TRUE",
    "land/building tax documentation eligibility for connection, Indonesia",
    "PDAM, informal Nyelang resellers")

add("S844", "comparative institutional case study", "high", "institutional_fragmentation",
    "water_access", "FALSE", "TRUE",
    "decentralization/delegation of water governance, Brazil/Peru/South Africa",
    "municipal governments, regional water bodies, 4 cities")

add("S845", "comparative institutional case study", "high", "institutional_fragmentation",
    "water_access", "FALSE", "TRUE",
    "neoliberal privatization/concession reform, Mexico/Argentina",
    "SACM, Aguas Argentinas/AySA")

add("S846", "participatory role-playing-game case study", "moderate", "eligibility",
    "water_access", "FALSE", "TRUE",
    "land tenure insecurity, peri-urban catchment periphery, Brazil",
    "municipal water company, district government")

add("S847", "cross-sectional survey study", "moderate-high", "bureaucratic_assistance",
    "water_access", "FALSE", "TRUE",
    "SMS e-governance fault-reporting mechanism, South Africa",
    "City of Cape Town municipal water/sanitation department")

add("S848", "qualitative case study synthesis", "high", "eligibility",
    "water_access", "FALSE", "TRUE",
    "Indian Act reserve system, decentralized water governance, Canada",
    "federal/provincial governments, First Nations band water systems")

add("S849", "legal/regulatory case analysis", "high", "documentation",
    "water_access", "FALSE", "TRUE",
    "absence of formal regulation of small independent water vendors, Kenya/Ethiopia",
    "small independent water vendors, municipal utilities")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
