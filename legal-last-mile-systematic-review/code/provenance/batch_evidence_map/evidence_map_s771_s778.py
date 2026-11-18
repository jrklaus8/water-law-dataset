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

add("S771", "qualitative case study (participant-researcher legal analysis)", "moderate-high", "institutional_fragmentation",
    "affordability", "FALSE", "TRUE",
    "Water Industry (Scotland) Act 2002, Water Services (Scotland) Act 2005",
    "Customer Forum, WICS, Scottish Water")

add("S772", "cross-sectional household survey with institutional analysis", "moderate-high", "eligibility",
    "water_access", "FALSE", "TRUE",
    "planned vs. unplanned urban-limit legal status, Tamil Nadu",
    "municipal taps, groundwater self-provision, vendors, Cuddalore")

add("S773", "system dynamics modelling case study", "moderate", "institutional_fragmentation",
    "service_coverage", "FALSE", "TRUE",
    "National Water Act 1998, Water Services Act 1997, South Africa",
    "Sundays River Valley Local Municipality, Greater Kirkwood")

add("S774", "qualitative case study (interviews)", "moderate", "institutional_fragmentation",
    "service_quality", "FALSE", "TRUE",
    "water governance and billing institutions, Nigeria",
    "Abuja Water Board, FCTA engineering department")

add("S775", "qualitative regulatory case study (documentary + fieldwork)", "moderate-high", "enforcement",
    "affordability", "FALSE", "TRUE",
    "NWASCO regulatory framework, Zambia water sector reform",
    "commercial water utilities, urban/peri-urban poor")

add("S776", "comparative two-district case study", "high", "institutional_fragmentation",
    "service_coverage", "FALSE", "TRUE",
    "Local Government Act 1993, CWSA Act 1998, District Assemblies Common Fund Act 1993, Ghana",
    "GWCL vs. CWSA/District Assembly, Tamale and Savelugu-Nanton")

add("S777", "mixed-methods case study", "moderate-high", "documentation",
    "service_reliability", "FALSE", "TRUE",
    "Cameroonian water law, exclusive urban utility mandate",
    "GWM community water scheme vs. CAMWATER/CDE, Buea")

add("S778", "historical-institutional case study with national descriptive statistics", "moderate-high", "institutional_fragmentation",
    "service_coverage", "FALSE", "TRUE",
    "Concessions Law No. 8987/1995, Planasa 1971, Brazil",
    "public/municipal/state/private WSS management models, national")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
