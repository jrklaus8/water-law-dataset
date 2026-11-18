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
    "S646",
    "longitudinal institutional case study",
    "moderate-high",
    "flat annual-rental-value (ARV) based water-tariff policy absent metering",
    "household service reliability, affordability, and coping behavior",
    "FALSE",
    "TRUE",
    "Trinidad and Tobago: WASA flat ARV-based tariff unchanged since 1993",
    "Water and Sewerage Authority (WASA)",
)

add(
    "S647",
    "historical-archival/legal institutional case study",
    "high",
    "constitutional water-rights litigation and pre-payment-meter policy",
    "household water/sanitation service-type access and entitlement quantity",
    "FALSE",
    "TRUE",
    "South Africa: Constitution s27(1)(b), Water Services Act 108 of 1997; Mazibuko v. City of Johannesburg litigation",
    "Johannesburg Water; Constitutional Court of South Africa",
)

add(
    "S648",
    "longitudinal institutional case study",
    "moderate",
    "water-service concession privatization and civil-society transparency-law advocacy",
    "household formal connection, coverage",
    "FALSE",
    "TRUE",
    "Mexico: CADF/SACM concession contracts; 2002 Federal Transparency Law of Access to Public Information",
    "SAPSA/IASA/TECSA/AGUAMEX private consortia; COMDA civil-society coalition",
)

add(
    "S649",
    "cross-sectional quantitative study (regression)",
    "high",
    "federal intergovernmental fiscal-transfer allocation under constitutionally assigned municipal water governance",
    "household piped-water coverage",
    "TRUE",
    "TRUE",
    "Mexico: Article 115 of the Constitution (municipal water-service responsibility)",
    "municipal water utilities; federal Aportaciones Federales transfer system",
)

add(
    "S650",
    "descriptive national policy case study",
    "moderate",
    "constitutional water-rights framework and multi-agency institutional fragmentation",
    "household water/sanitation access disaggregated by ethnicity, income, region",
    "FALSE",
    "TRUE",
    "Ecuador: 2008 Constitution Article 318 (unique water authority)",
    "SENAGUA; MIDUVI; MAE; MSP; INAR",
)

add(
    "S651",
    "descriptive case study with household survey data",
    "moderate-high",
    "water-utility privatization/regulatory framework (affermage management contract)",
    "household connection, reliability, affordability, and health outcome",
    "FALSE",
    "TRUE",
    "Ghana: Public Utilities Regulatory Commission Act 538 (1997)",
    "GWCL/GUWCL; Aqua Vitens Rand Limited (AVRL); PURC",
)

add(
    "S652",
    "qualitative ethnographic case study",
    "moderate",
    "tenure-based exclusion from statutory connection and informal political-institutional water governance",
    "household water access, price, and reliability",
    "FALSE",
    "TRUE",
    "Bangladesh: informal settlement (bosti) tenure status; 2007 GOB mandate for tenure-blind DWASA service to slums",
    "Dhaka Water Supply and Sewerage Authority (DWASA); local political committees",
)

add(
    "S653",
    "cross-sectional household survey (multi-province)",
    "low-moderate",
    "post-conflict decentralized institutional/legal water-governance framework",
    "household water-service continuity/satisfaction and willingness-to-pay",
    "FALSE",
    "TRUE",
    "Iraq: 2005 Constitution decentralized federal structure; Law 21 of 2008",
    "provincial/subnational water utilities",
)

fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmppath, DB)
print(f"New total: {len(rows)}")
