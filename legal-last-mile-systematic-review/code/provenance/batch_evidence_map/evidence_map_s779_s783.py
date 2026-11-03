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

add("S779", "historical-institutional case study", "moderate", "enforcement",
    "service_coverage", "FALSE", "TRUE",
    "sewer-connection legality, Parliamentary investment-approval regulation, 19th c. London",
    "eight private water companies, Metropolitan Water Board")

add("S780", "quantitative county-level regression analysis", "high", "eligibility",
    "service_coverage", "TRUE", "TRUE",
    "ethnic-minority-autonomous-area legal status, China",
    "MWR National Rural Drinking Water Safety Project, Guizhou Province")

add("S781", "qualitative comparative case study", "moderate-high", "institutional_fragmentation",
    "water_access", "FALSE", "TRUE",
    "national water policy vs. local infrastructure governance modes, Peru",
    "municipal, community-managed, and excluded committee systems, Cusco")

add("S782", "quantitative city-level regression analysis", "moderate-high", "institutional_fragmentation",
    "affordability", "FALSE", "TRUE",
    "city incorporation date and water-system governance type, California",
    "municipal/private/special-district providers, 482 California cities")

add("S783", "action-research participatory policy-design study", "moderate-high", "enforcement",
    "affordability", "FALSE", "TRUE",
    "ONEA concession, affermage contracts, price-cap regulation, Burkina Faso",
    "private operators, small-town piped water schemes")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
