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
    "S672",
    "cross-sectional mixed-methods case study (household interview schedules, KIIs, FGDs)",
    "moderate-high",
    "dissonance between customary and statutory water-governance institutions",
    "household water access, affordability and cost-recovery tariff burden",
    "FALSE",
    "TRUE",
    "Botswana: Water Utilities Corporation Act (1970); 2008 water-sector reform",
    "Water Utilities Corporation (WUC); District Councils; Department of Water Affairs; customary institutions",
)

add(
    "S673",
    "cross-sectional mixed-methods case study (systematic-sample household questionnaires, KIIs)",
    "moderate",
    "decentralization-policy constraints and traditional-authority governance over community water management",
    "rural community water-project sustainability and access outcomes",
    "FALSE",
    "TRUE",
    "Cameroon: decentralization policy; ministerial decree Articles 3(11) and 3(16)",
    "community-based water management committees; village traditional authorities (Chiefs)",
)

fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmppath, DB)

print(f"New total: {len(rows)}")
