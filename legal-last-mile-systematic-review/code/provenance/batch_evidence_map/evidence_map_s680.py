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
    "S680",
    "historical-archival/oral-history institutional case study",
    "moderate-high",
    "DISCRETION_ACCOMMODATION",
    "primary_connection",
    "FALSE",
    "TRUE",
    "1971 legalization of Orcasitas' Neighborhood Association as a legal public entity; Spanish Ministry of Housing expropriation/property regulations",
    "Canal de Isabel II water-canal company; Madrid city council; Orcasitas Neighborhood Association (Asociacion de Vecinos)",
)

fd, tmp = tempfile.mkstemp(dir="/home/user/water-law-dataset/legal-last-mile-systematic-review")
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)
os.replace(tmp, DB)

print(f"New total: {len(rows)}")
