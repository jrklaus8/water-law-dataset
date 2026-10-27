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

add("S938",
    study_design_class="neighborhood-scale comparative qualitative case study",
    evidence_level="moderate",
    mechanism_family="institutional_fragmentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="2001 public-private partnership water-sector reform, Niger",
    institutional_context="PPP water utility; informal water vendors",
    )

add("S939",
    study_design_class="mixed-methods content analysis and statewide administrative-data comparison",
    evidence_level="high",
    mechanism_family="legal_status",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="California 2012 legislated Human Right to Water (AB 685); AB 1830 CPUC complaint mechanism",
    institutional_context="mobile home park water systems; State Water Resource Control Board",
    )

add("S940",
    study_design_class="single-city institutional/policy case-study analysis",
    evidence_level="moderate",
    mechanism_family="tenure",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="Harare Slum Upgrading Programme, post-2005 Operation Restore Order",
    institutional_context="City of Harare municipal government; urban-poor community alliances",
    )

add("S941",
    study_design_class="two-country documentary/institutional policy analysis (field note)",
    evidence_level="moderate",
    mechanism_family="institutional_fragmentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="Malawi and Zambia Poverty Reduction Strategy Papers",
    institutional_context="national water/sanitation sector agencies; donor coordination bodies",
    )

add("S942",
    study_design_class="four-town inductive comparative institutional-governance case study",
    evidence_level="high",
    mechanism_family="institutional_fragmentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="municipal vs. para-statal water-governance institutional arrangements, Karnataka and Tamil Nadu, India",
    institutional_context="municipal governments; para-statal water agencies",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EM))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EM)

print(f"New total: {len(rows)}")
