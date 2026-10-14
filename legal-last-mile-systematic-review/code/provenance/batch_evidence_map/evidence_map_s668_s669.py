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
    assert sid not in existing_ids, f"Duplicate study_id: {sid}"
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
    "S668",
    "qualitative case study (interviews and reconnaissance observation)",
    "moderate-high",
    "informal/unwritten institutional rules governing non-state water provision alongside statutory utility limited capacity",
    "household water access, coverage and affordability",
    "FALSE",
    "TRUE",
    "Tanzania: informal/unwritten governance rules; DAWASA statutory utility mandate",
    "non-state water service providers (mechanised boreholes, kiosks, wells, standpipes, tankers); DAWASA; Ubungo municipality",
)

add(
    "S669",
    "qualitative comparative case study (institutional/documentary analysis)",
    "moderate",
    "municipal water/sanitation regulatory constraint and negotiated co-production institutional workaround",
    "settlement-level water and sanitation infrastructure access and quality",
    "FALSE",
    "TRUE",
    "South Africa: City of Cape Town Water & Sanitation Department regulations on communal-facility siting",
    "CoCT Inter-Departmental Task Team; Water & Sanitation Department; community leadership (Malawi Camp, Klipheuwel)",
)

for r in rows[-2:]:
    assert r["study_id"] in {"S668", "S669"}

fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmppath, DB)

print(f"New total: {len(rows)}")
