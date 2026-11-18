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

add("S712", "policy analysis with qualitative interviews", "high", "enforcement",
    "affordability", "FALSE", "TRUE",
    "Kenya Water Act 2002 (WRMA, WSRB licensing and tariff regulation)",
    "commercialized municipal water companies, Kenya")

add("S713", "comparative legal/regulatory analysis", "high", "tenure",
    "service_continuity", "FALSE", "TRUE",
    "UK Water Industry Act 1999 disconnection prohibition; UN General Comment 15",
    "privatized UK water utilities under license conditions")

add("S714", "comparative ethnographic case study", "moderate-high", "eligibility",
    "effective_access", "FALSE", "TRUE",
    "Peru's new water law redefining rights/obligations",
    "local water user associations, Peruvian Andes")

add("S715", "historical-institutional review", "high", "property",
    "service_coverage", "FALSE", "TRUE",
    "colonial legislative fiat and successive Kenyan water-sector reforms",
    "colonial and post-colonial Kenyan state water administration")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
