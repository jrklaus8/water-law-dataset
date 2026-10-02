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

add("S906",
    study_design_class="comparative qualitative case study (10 PPPs)",
    evidence_level="moderate-high",
    mechanism_family="legal_status",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="water PPP contract structures, Southern California",
    institutional_context="10 sustainability-oriented water public-private partnerships",
    )

add("S907",
    study_design_class="documentary/financial policy analysis of state administrative data",
    evidence_level="high",
    mechanism_family="fees",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="state coverage-criteria and subsidy policy, Karnataka, India",
    institutional_context="Karnataka state water supply and sanitation sector",
    )

add("S908",
    study_design_class="three-essay econometric dissertation (spatial panel; hedonic/quantile; OLS regression)",
    evidence_level="high",
    mechanism_family="enforcement",
    outcome_family="water_access",
    quantitative_synthesis_eligible="TRUE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="Safe Drinking Water Act; West Virginia Source Water Protection Act (SB 373, 2014)",
    institutional_context="public water systems; West Virginia public service districts",
    )

add("S909",
    study_design_class="documentary policy/governance-framework analysis",
    evidence_level="high",
    mechanism_family="legal_status",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="National Water Act 1998, South Africa",
    institutional_context="national Department of Water and Sanitation, municipal groundwater schemes",
    )

add("S910",
    study_design_class="documentary/statistical program-allocation analysis of national administrative data",
    evidence_level="high",
    mechanism_family="eligibility",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="Jawaharlal Nehru National Urban Renewal Mission; 74th Constitutional Amendment Act, India",
    institutional_context="65 JnNURM mission cities and non-mission towns",
    )

add("S911",
    study_design_class="household survey with DPSIR institutional-framework analysis",
    evidence_level="moderate-high",
    mechanism_family="legal_status",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="groundwater rights tied to land rights, absent independent regulation, India",
    institutional_context="Guwahati Municipal Corporation, Assam Urban Water Supply and Sewerage Board",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EM))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EM)

print(f"New total: {len(rows)}")
