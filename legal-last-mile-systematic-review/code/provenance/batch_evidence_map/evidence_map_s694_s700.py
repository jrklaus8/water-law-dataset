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
    "S694",
    "legal/regulatory documentary case study",
    "moderate",
    "REGULATORY_MODEL",
    "affordability",
    "FALSE",
    "TRUE",
    "Higher Court of Catalonia ruling on household-size water pricing; 1999 Catalan Water Taxation Law",
    "municipal concession regime; AGBAR and public water companies, Spain",
)

add(
    "S695",
    "qualitative institutional case study",
    "moderate",
    "administrative discretion in tariff-setting",
    "affordability",
    "FALSE",
    "TRUE",
    "formal and informal utility tariff-setting negotiations",
    "Lilongwe Water Board, two service modalities",
)

add(
    "S696",
    "cross-national panel regression with country fixed effects",
    "moderate-high",
    "democratization as institutional accountability mechanism moderating pro-urban bias",
    "effective_access",
    "TRUE",
    "TRUE",
    "Polity IV polity2 democracy index as institutional mechanism",
    "national government water-infrastructure siting decisions, 112 developing countries",
)

add(
    "S697",
    "systematic_review_secondary (meta-analysis)",
    "moderate",
    "MULTIPLE",
    "effective_access",
    "TRUE",
    "TRUE",
    "NGO/CBO bottom-up service delivery vs. conventional provision",
    "community-based organizations, multi-country synthesis",
)

add(
    "S698",
    "historical-institutional case study",
    "moderate",
    "institutional_fragmentation",
    "formal_connection",
    "FALSE",
    "TRUE",
    "1991 community expulsion of national water corporation",
    "Kumbo Water Authority, Cameroon",
)

add(
    "S699",
    "empirical case study (documentary/field-based)",
    "moderate",
    "customary common property resource management institutions",
    "effective_access",
    "FALSE",
    "TRUE",
    "traditional/customary land and water access rights",
    "pastoralist common property institutions, Zamfara Forest Reserve, Nigeria",
)

add(
    "S700",
    "mixed-methods empirical field study",
    "moderate-high",
    "PARTICIPATION",
    "effective_access",
    "FALSE",
    "TRUE",
    "Tanzanian decentralisation reforms creating village-level participation spaces",
    "decentralized local government water/health service delivery",
)

fd, tmp = tempfile.mkstemp(dir="/home/user/water-law-dataset/legal-last-mile-systematic-review")
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)
os.replace(tmp, DB)

print(f"New total: {len(rows)}")
