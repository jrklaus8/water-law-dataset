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

add("S890",
    study_design_class="household survey (before/after governance-innovation evaluation)",
    evidence_level="moderate-high",
    mechanism_family="fees",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="National Basic Sanitation Plan (PLANSAB), Act No. 11.445/2007, Brazil",
    institutional_context="DESAFIO rural water/sanitation governance-innovation project, Cristais community, Ceara",
    )

add("S891",
    study_design_class="multi-case-study analysis (principal-agent institutional framework)",
    evidence_level="moderate-high",
    mechanism_family="institutional_fragmentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="post-1990s water-sector reform regulatory frameworks, Kenya and Ghana",
    institutional_context="water utility regulators, Municipal Councils, contracted service operators",
    )

add("S892",
    study_design_class="ethnographic and documentary institutional analysis",
    evidence_level="moderate-high",
    mechanism_family="documentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="state water-measurement and administrative practices, Delhi, India",
    institutional_context="Delhi Jal Board",
    )

add("S893",
    study_design_class="quantitative statistical analysis of government aid-allocation administrative data",
    evidence_level="high",
    mechanism_family="eligibility",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="Safe Drinking Water Act infrastructure financial assistance, Pennsylvania",
    institutional_context="Pennsylvania Infrastructure Investment Authority (PENNVEST)",
    )

add("S894",
    study_design_class="original household survey with hydropolitical/institutional analysis",
    evidence_level="moderate-high",
    mechanism_family="legal_status",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="1995 Oslo Interim Agreement, Joint Water Committee allocation regime",
    institutional_context="Palestinian Hydrology Group, CERTE Tunisia",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EM))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EM)

print(f"New total: {len(rows)}")
