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

add("S901",
    study_design_class="documentary/statistical policy analysis of administrative regulatory data",
    evidence_level="high",
    mechanism_family="legal_status",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="1981 Water Code; 1980 Constitution Article 24, Chile",
    institutional_context="privatized regional water/sewage utilities, Superintendency of Sanitary Services",
    )

add("S902",
    study_design_class="mixed-methods documentary and field study",
    evidence_level="moderate-high",
    mechanism_family="institutional_fragmentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="2010 Constitution devolution framework; Water Acts 2002/2016, Kenya",
    institutional_context="Siaya County water-governance institutions",
    )

add("S903",
    study_design_class="multiple-case study (embedded design, 2 CBOs)",
    evidence_level="moderate-high",
    mechanism_family="institutional_fragmentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="constitutional bill-of-rights (healthy living environment), South Africa",
    institutional_context="local government and community-based organizations, Cape Town",
    )

add("S904",
    study_design_class="two-case-study ethnographic institutional analysis",
    evidence_level="moderate-high",
    mechanism_family="discretion",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="state water-governance authority amid water-privatization transition, Egypt",
    institutional_context="informal settlement community water systems; gated-community private governance, Cairo",
    )

add("S905",
    study_design_class="case study with normative institutional-governance-framework analysis",
    evidence_level="moderate-high",
    mechanism_family="institutional_fragmentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="sanitation-sector bylaws and government institutional responsibilities, Rwanda",
    institutional_context="Rwanda Water & Sanitation Corporation (WASAC), Kigali",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EM))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EM)

print(f"New total: {len(rows)}")
