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

add("S747", "legal-doctrinal/institutional analysis", "moderate-high", "participation",
    "service_quantity", "FALSE", "TRUE",
    "Water Act 2002 participatory-governance provisions (WRMA, WAB, CAACs, WRUAs)",
    "Ministry of Water and Irrigation, national water governance, Kenya")

add("S748", "qualitative case study", "moderate-high", "institutional_fragmentation",
    "service_coverage", "FALSE", "TRUE",
    "ambiguous statutory governance of urban water bodies (ponds)",
    "neighbourhood clubs, political parties, municipal authorities, Bardhaman, West Bengal, India")

add("S749", "quasi-experimental panel-data regression", "high", "enforcement",
    "affordability", "TRUE", "TRUE",
    "ownership type and regulatory-agency/regime structure of water utilities",
    "51 water and sanitation business corporations, Brazil")

add("S750", "comparative case study", "moderate-high", "enforcement",
    "affordability", "FALSE", "TRUE",
    "self-regulation vs. bipartite negotiation vs. independent regulation of water tariffs",
    "Vitens (Netherlands); Agbar/EMA (Barcelona); Scottish Water/WICS (Scotland)")

add("S751", "mixed-methods georeferenced case study", "moderate", "institutional_fragmentation",
    "service_quality", "FALSE", "TRUE",
    "historical infrastructure legacy and contemporary municipal water-management policy",
    "Ahmedabad Municipal Corporation, two administrative wards, India")

add("S752", "political-economy/institutional case study", "moderate-high", "enforcement",
    "affordability", "FALSE", "TRUE",
    "corporatisation/ring-fencing institutional restructuring of municipal water utility",
    "Durban Metro Water Services, eThekwini Municipality, South Africa")

add("S753", "historical-institutional case study", "high", "legal_status",
    "service_coverage", "FALSE", "TRUE",
    "colonial-era infrastructure design targeting affluent groups",
    "National Water and Sewerage Corporation, Kampala, Uganda")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
