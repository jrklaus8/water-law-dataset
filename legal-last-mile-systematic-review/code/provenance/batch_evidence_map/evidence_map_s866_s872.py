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

add("S866", "mixed-methods comparative household survey study", "high", "institutional_fragmentation",
    "water_access", "FALSE", "TRUE",
    "1974 and 2002 Water Acts, Kenya",
    "THIWASCO, Athi Water Services Board, Nairobi City Water and Sewerage Company")

add("S867", "documentary institutional case study", "moderate-high", "institutional_fragmentation",
    "water_access", "FALSE", "TRUE",
    "1985 Prime Minister's Directive on Decentralisation, Zimbabwe",
    "VIDCO/WADCO/DDC Democratic Development Structures, IRWSSP")

add("S868", "mixed-methods structural/bureaucratic case study", "moderate-high", "bureaucratic_assistance",
    "water_access", "FALSE", "TRUE",
    "Nigerian federal government fiscal/administrative structure",
    "Federal Housing Authority, Metropolitan Lagos")

add("S869", "panel-data regression analysis", "high", "institutional_fragmentation",
    "water_access", "TRUE", "TRUE",
    "1988 Constitution, 2007 federal sanitation guidelines, 2020 Sanitation Legal Framework Act, Brazil",
    "intermunicipal consortia, municipal local governments")

add("S870", "ethnographic case study with historical institutional analysis", "high", "enforcement",
    "water_access", "FALSE", "TRUE",
    "colonial and post-independence state water-supply policy, Zimbabwe",
    "District Development Fund, Native Commissioner administration")

add("S871", "historical institutional case study", "moderate-high", "documentation",
    "water_access", "FALSE", "TRUE",
    "mid-19th-century municipal law and finance, United States",
    "municipal courts, boards of health, sanitary reform movement")

add("S872", "ethnographic case study", "high", "documentation",
    "water_access", "FALSE", "TRUE",
    "1981 Water Code, Chile",
    "Atacameno indigenous community water-user associations (regantes)")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
