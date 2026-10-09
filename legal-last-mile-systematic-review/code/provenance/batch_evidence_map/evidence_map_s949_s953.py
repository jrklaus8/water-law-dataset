#!/usr/bin/env python3
import csv, tempfile, os

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
EM = f"{BASE}/05_analysis/descriptive/evidence_map.csv"

with open(EM, newline="") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    rows = list(r)
    existing_ids = {row["study_id"] for row in rows}

def add(sid, **kwargs):
    assert sid not in existing_ids, f"{sid} already exists"
    row = {fn: "" for fn in fieldnames}
    row["study_id"] = sid
    row.update(kwargs)
    rows.append(row)

add("S949",
    study_design_class="Delphi expert-consensus study with national legal-reform policy analysis",
    evidence_level="moderate",
    mechanism_family="institutional_fragmentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="Chile Law No. 20.998 (2017), rural water governance reform",
    institutional_context="community-managed rural water organizations (APR)",
    )

add("S950",
    study_design_class="longitudinal ethnography (construction and post-construction phases)",
    evidence_level="high",
    mechanism_family="discretion",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="neoliberal water-sector reform, village water-governance institutions, Rajasthan India",
    institutional_context="village-scale water-governance institutions; state power",
    )

add("S951",
    study_design_class="single-community ethnography with participant-observation and official interviews",
    evidence_level="moderate",
    mechanism_family="discretion",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="community drinking-water management institutions, Valley of Mexico",
    institutional_context="local civil and religious water-distribution officials",
    )

add("S952",
    study_design_class="NGO program-implementation case study with governance/rights-based policy analysis",
    evidence_level="moderate",
    mechanism_family="institutional_fragmentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="Bangladesh arsenic-contamination governance failure and human-rights framing",
    institutional_context="Arsenic Mitigation and Research Foundation (AMRF)",
    )

add("S953",
    study_design_class="household survey with logit regression analysis",
    evidence_level="high",
    mechanism_family="legal_status",
    outcome_family="water_access",
    quantitative_synthesis_eligible="TRUE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="India 74th Constitutional Amendment local self-governance; notified vs. non-notified (NN) slum legal status",
    institutional_context="Kolkata Municipal Corporation; municipal councilors",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EM))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EM)

print(f"New total: {len(rows)}")
