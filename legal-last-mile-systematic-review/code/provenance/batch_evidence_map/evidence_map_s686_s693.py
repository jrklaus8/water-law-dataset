import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/descriptive/evidence_map.csv"

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

existing_ids = {r["study_id"] for r in rows}

def add(sid, design_class, evidence_level, mech_family, outcome_family, quant, qual, legal_ctx, inst_ctx):
    assert sid not in existing_ids
    rows.append({
        "study_id": sid,
        "study_design_class": design_class,
        "evidence_level": evidence_level,
        "mechanism_family": mech_family,
        "outcome_family": outcome_family,
        "quantitative_synthesis_eligible": quant,
        "qualitative_synthesis_eligible": qual,
        "legal_context": legal_ctx,
        "institutional_context": inst_ctx,
    })

add(
    "S686",
    "legal/regulatory documentary case study",
    "moderate",
    "REGULATORY_MODEL",
    "affordability",
    "FALSE",
    "TRUE",
    "Ofwat statutory duty; High Court ruling against prepayment meters; disconnection-protection legislation",
    "privatized water/sewerage companies regulated by Ofwat, England and Wales",
)

add(
    "S687",
    "longitudinal qualitative case study",
    "moderate-high",
    "TENURE",
    "formal_connection",
    "FALSE",
    "TRUE",
    "acquisition of legal land tenure by an informal settlement",
    "community organization negotiating with municipal government and public utilities, Buenos Aires",
)

add(
    "S688",
    "mixed-methods primary field study",
    "moderate",
    "PARTICIPATION",
    "effective_access",
    "FALSE",
    "TRUE",
    "Guidelines for Participatory Water Management (MoWR 2000) mandating gender-inclusive WMG/WMA membership",
    "Water Management Groups/Associations, rural Bangladesh",
)

add(
    "S689",
    "comparative multi-site primary qualitative research",
    "moderate-high",
    "ELIGIBILITY",
    "effective_access",
    "FALSE",
    "TRUE",
    "policy-driven (rights-based) vs. needs-driven (informal/market) access frameworks",
    "mixed public/private/informal providers across 5 metropolitan areas' peri-urban interfaces",
)

add(
    "S690",
    "institutional case study with household entitlements analysis",
    "moderate",
    "REGULATORY_MODEL",
    "service_quantity",
    "TRUE",
    "TRUE",
    "1919 Madras Municipal Corporation Act; 1978 state water board creation removing local-government control",
    "Chennai Metropolitan Water Supply and Sewerage Board",
)

add(
    "S691",
    "historical-institutional documentary case study",
    "moderate-high",
    "REGULATORY_MODEL",
    "formal_connection",
    "FALSE",
    "TRUE",
    "1848 Public Health Act; citizenship-status-differentiated state intervention",
    "private water/sewer companies; local boards of health, 19th-century England",
)

add(
    "S692",
    "comparative institutional performance study",
    "moderate",
    "institutional_fragmentation",
    "service_coverage",
    "TRUE",
    "TRUE",
    "single metropolitan water board vs. fragmented Urban Local Bodies governance",
    "BWSSB and ten Urban Local Bodies/KUWSDB, Bangalore Metropolitan Region",
)

add(
    "S693",
    "mixed-methods primary field study (narrative + composite index)",
    "moderate-high",
    "institutional_fragmentation",
    "sanitation_access",
    "TRUE",
    "TRUE",
    "Total Sanitation Campaign; Nirmal Gram Puraskar fiscal-incentive scheme",
    "Panchayati Raj Institutions (Gram Panchayats), Kerala",
)

fd, tmp = tempfile.mkstemp(dir="/home/user/water-law-dataset/legal-last-mile-systematic-review")
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)
os.replace(tmp, DB)

print(f"New total: {len(rows)}")
