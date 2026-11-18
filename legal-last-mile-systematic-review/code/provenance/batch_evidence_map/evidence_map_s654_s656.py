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
    "S654",
    "mixed-methods case study",
    "moderate",
    "weakly-enforced groundwater-extraction/transport licensing regime and land-tied groundwater-rights doctrine",
    "household water access, quality, and affordability",
    "FALSE",
    "TRUE",
    "India: Indian Easements Act 1882; Chennai Metropolitan Area Ground Water (Regulation) Act 1987/2002",
    "Chennai Metropolitan Water Supply and Sewerage Board (CMWSSB)",
)

add(
    "S655",
    "qualitative comparative case study",
    "moderate",
    "tenure-based institutional barriers to formal service extension and landowner-consent requirements",
    "household water/sanitation service access with gendered burden",
    "FALSE",
    "TRUE",
    "South Africa: Free Basic Water policy/City of Cape Town Indigent Water Policy 2003",
    "eThekwini Municipality; City of Cape Town",
)

add(
    "S656",
    "mixed-methods FGD-based study with descriptive survey context",
    "moderate-high",
    "tenure-based illegality barring statutory connection, with documented enforcement/disconnection actions",
    "household water access, quality, and affordability",
    "FALSE",
    "TRUE",
    "Kenya: Water Act No. 8 of 2002; National Water Services Strategy 2007-2015",
    "Nairobi City Water and Sewerage Company (NCWSC)",
)

fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmppath, DB)
print(f"New total: {len(rows)}")
