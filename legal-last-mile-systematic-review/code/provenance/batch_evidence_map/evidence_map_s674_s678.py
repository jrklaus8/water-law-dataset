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
    "S674",
    "mixed-methods institutional case study (archival, census, field survey, regression)",
    "moderate-high",
    "administrative-territory legal codification determining eligibility for officially funded water infrastructure",
    "village-level improved drinking water source access and coverage",
    "FALSE",
    "TRUE",
    "Mali: administrative-territory legal codification under successive governments",
    "local/municipal government; decentralized administrative institutions",
)

add(
    "S675",
    "historical-institutional case study (documentary/policy analysis, administrative statistics)",
    "high",
    "Free Basic Water policy, means-testing, disconnection enforcement, and litigated constitutional challenge",
    "household water/sanitation access, disconnection, and affordability",
    "FALSE",
    "TRUE",
    "South Africa: Free Basic Water policy; Manquele v. eThekwini litigation",
    "eThekwini Water and Sanitation (EWS); Umgeni Water",
)

add(
    "S676",
    "qualitative case study (semi-structured interviews, structured questionnaire)",
    "moderate-high",
    "statutory exclusion of informal settlements from public water services",
    "household water access, affordability, and coping strategies",
    "FALSE",
    "TRUE",
    "Mexico: Sustainable Water Law of Mexico City (2017)",
    "SACMEX; local government (Alcaldia); community water committees (paradas)",
)

add(
    "S677",
    "cross-sectional mixed-methods case study (household survey, interviews, participant observation)",
    "moderate-high",
    "state-planned rural water-network expansion producing intervillage and caste/gender differentiation",
    "household water access, network connection, and collection-time burden",
    "FALSE",
    "TRUE",
    "India: state-planned Indira Gandhi Canal water-supply network expansion",
    "state water-supply agencies; government engineers",
)

add(
    "S678",
    "ethnographic-historical case study (interviews, participant observation, archival review)",
    "high",
    "dissonance between statutory water law and customary/project-based water rights",
    "household water access across four historical development periods",
    "FALSE",
    "TRUE",
    "Ghana: 1992 constitution Article 257/6; Water Resources Commission Act 522 (1996)",
    "Community Water and Sanitation Agency (CWSA); Water and Sanitation Development Boards (WSDBs)",
)

fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmppath, DB)

print(f"New total: {len(rows)}")
