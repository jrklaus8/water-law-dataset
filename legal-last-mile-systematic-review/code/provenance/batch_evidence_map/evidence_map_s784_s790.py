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

add("S784", "qualitative comparative case study", "moderate", "eligibility",
    "water_access", "FALSE", "TRUE",
    "statutory 30% women's quota, local water management bodies, Nepal",
    "two towns, local water governance institutions")

add("S785", "statewide survey of local government programs", "moderate-high", "discretion",
    "service_quality", "FALSE", "TRUE",
    "state private-well construction regulations, North Carolina",
    "local health department private-well programs")

add("S786", "single-company regulatory case study", "moderate-high", "enforcement",
    "affordability", "FALSE", "TRUE",
    "Ofwat price-cap regulation, statutory disconnection ban, Wales/England",
    "Glas Cymru not-for-profit PPP, Dwr Cymru Welsh Water")

add("S787", "longitudinal qualitative institutional-theory case study", "moderate-high", "enforcement",
    "affordability", "FALSE", "TRUE",
    "municipal water-shutoff policy, Detroit bankruptcy context",
    "Detroit Water and Sewerage Department")

add("S788", "regulatory-design case study", "moderate", "institutional_fragmentation",
    "service_coverage", "FALSE", "TRUE",
    "ARE multi-sector regulator, Cape Verde",
    "national water utilities, small island developing state")

add("S789", "legal-institutional case analysis", "high", "eligibility",
    "affordability", "FALSE", "TRUE",
    "constitutional right to water, South Africa (UN GC15)",
    "municipal water service providers and consumers")

add("S790", "qualitative comparative political-ecology case study", "moderate", "institutional_fragmentation",
    "service_coverage", "FALSE", "TRUE",
    "state/donor drinking water scheme governance, India/Nepal",
    "six small-town water supply schemes, lower Himalayas")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
