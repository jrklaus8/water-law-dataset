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

add("S742", "ethnographic case study", "moderate-high", "discretion_accommodation",
    "service_quantity", "FALSE", "TRUE",
    "formal and informal (customary) rules governing community and private water sources",
    "sabuku traditional authority, borehole committees, DNR, Romwe micro-catchment, Zimbabwe")

add("S743", "historical-institutional/political-ecology case study", "moderate", "enforcement",
    "affordability", "FALSE", "TRUE",
    "federal groundwater-extraction permits (unmetered, uncompensated) granted to private bottler",
    "municipal water system vs. Coca-Cola bottling plant, San Cristobal de las Casas, Chiapas, Mexico")

add("S744", "ethnographic case study", "high", "legal_status",
    "service_continuity", "FALSE", "TRUE",
    "everyday formal/informal status distinctions in water access",
    "Karachi Water and Sewerage Board, Samandar Colony, Karachi, Pakistan")

add("S745", "historical-institutional archival case study", "moderate-high", "enforcement",
    "affordability", "FALSE", "TRUE",
    "collectivized worker management of a private water utility, single citywide tariff and social price",
    "Sociedad General de Aguas de Barcelona, Spanish Civil War, Barcelona")

add("S746", "mixed-methods field study", "high", "enforcement",
    "service_quantity", "FALSE", "TRUE",
    "county-council-issued sand-extraction permits externally destroying a community water source",
    "Machakos County Council, Katheka Sublocation, Kenya")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
