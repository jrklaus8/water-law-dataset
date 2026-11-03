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
    "S659",
    "longitudinal institutional case study",
    "moderate-high",
    "water-supply concession-contract regulatory framework and cross-subsidy policy for the urban poor",
    "household formal connection, coverage",
    "FALSE",
    "TRUE",
    "Indonesia: Law No. 7/2004 on Water Resources; Government Regulation No. 16/2005; Presidential Decree No. 67/2005",
    "Jakarta Water Supply Regulatory Body (JWSRB); PALYJA; TPJ",
)

add(
    "S660",
    "historical-institutional case study",
    "high",
    "judicial-review-driven statutory disconnection ban and vulnerable-consumer protection regulations",
    "household water access and affordability protection",
    "FALSE",
    "TRUE",
    "United Kingdom: Water Industry Act 1999; BPU judicial review case",
    "Ofwat (Director General of Water Services)",
)

add(
    "S661",
    "mixed-methods case study (qualitative interviews plus secondary administrative data)",
    "moderate-high",
    "privatization-driven institutional shift from social-equity to market-environmental water charging",
    "household water affordability and consumption",
    "FALSE",
    "TRUE",
    "United Kingdom: Water Act 2003; EU Water Framework Directive 2000/60/EC",
    "Ofwat; Environment Agency; privatized water and sewerage companies",
)

fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmppath, DB)
print(f"New total: {len(rows)}")
