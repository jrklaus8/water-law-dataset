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

add("S701", "ethnographic case study", "moderate-high", "discretion_accommodation",
    "effective_access", "FALSE", "TRUE",
    "Jyotirgram Scheme groundwater/electrification policy and groundwater legislation",
    "caste-based discretionary control of village water infrastructure ('water lords'), Gujarat, India")

add("S702", "legal/institutional case study", "moderate-high", "institutional_fragmentation",
    "service_coverage", "FALSE", "TRUE",
    "1975 Tunisian Water Code (Code des Eaux) water-allocation institution",
    "state water resources administration, Tunisia")

add("S703", "historical-institutional case study", "high", "discretion_accommodation",
    "effective_access", "FALSE", "TRUE",
    "unregulated private water monopolies pre-1852 Metropolis Water Act",
    "private water monopoly companies, London, 1820-1852")

add("S704", "political ecology case study", "moderate-high", "institutional_fragmentation",
    "affordability", "FALSE", "TRUE",
    "Indonesian Law No. 7/2004 on Water Resources, well-permitting regime, Governor's Decree No. 16/2009",
    "PDAM utility vs. tourism-sector water competition, Bali, Indonesia")

add("S705", "qualitative comparative institutional case study", "moderate", "institutional_fragmentation",
    "affordability", "FALSE", "TRUE",
    "state water laws (Lagos State Water Sector Law 2004, Rivers State Water Policy 2012, Kaduna State Water Board Law 2004)",
    "four Nigerian state water utilities' legal autonomy and tariff-setting")

add("S706", "historical-institutional case study", "high", "tenure",
    "service_coverage", "FALSE", "TRUE",
    "taxable-area/connection-extension regulation; 1948 Electricity Supply Act nationalization",
    "peri-urban semi-legal/illegal tenure ('revenue layouts'), Bangalore, India")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
