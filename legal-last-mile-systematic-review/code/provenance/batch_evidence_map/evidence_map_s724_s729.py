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

add("S724", "mixed-methods survey with statistical analysis", "moderate-high", "tenure",
    "service_coverage", "FALSE", "TRUE",
    "land ownership status (public/private/government/church) post-earthquake",
    "IDP camps, NGO management, and municipal authorities, Haiti")

add("S725", "case study with groundwater flow modeling", "high", "enforcement",
    "service_quality", "FALSE", "TRUE",
    "Wisconsin state well-construction code's lack of local regulatory authority (vs. Kansas/Utah)",
    "rural unsewered subdivisions, southern Wisconsin")

add("S726", "comparative institutional/regulatory analysis", "moderate", "participation",
    "effective_access", "FALSE", "TRUE",
    "consumer-involvement regulatory design across multiple countries",
    "water-utility regulatory agencies, low-income/informal consumers")

add("S727", "ethnographic case study", "high", "eligibility",
    "service_quantity", "FALSE", "TRUE",
    "Indonesian national water law, presidential decrees, Local Government Regulation of Bali",
    "subak irrigation institution vs. PDAM/PLN/tourism licensing, South Bali")

add("S728", "institutional/constitutional case study", "high", "participation",
    "service_coverage", "FALSE", "TRUE",
    "2004 Uruguayan Constitutional Water Referendum",
    "OSE public water utility vs. Maldonado private concessions")

add("S729", "household survey case study", "moderate-high", "legal_status",
    "effective_access", "FALSE", "TRUE",
    "settlement legal status (illegal vs. formal)",
    "local government water utility, Xochimilco, Mexico City")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
