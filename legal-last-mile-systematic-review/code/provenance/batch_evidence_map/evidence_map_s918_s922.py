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

add("S918",
    study_design_class="econometric tariff-differential analysis of municipal water pricing",
    evidence_level="high",
    mechanism_family="fees",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="decentralized, largely unregulated urban water tariff-setting, Spain",
    institutional_context="local monopoly water utilities across Spanish cities",
    )

add("S919",
    study_design_class="comparative institutional assessment (12-city structured scoring methodology)",
    evidence_level="high",
    mechanism_family="institutional_fragmentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="fecal sludge management enabling environment/policy frameworks, 12 countries",
    institutional_context="municipal governments and FSM operators, 12 cities",
    )

add("S920",
    study_design_class="difference-in-differences with kernel propensity-score matching, national administrative panel data",
    evidence_level="high",
    mechanism_family="formal_connection",
    outcome_family="water_access",
    quantitative_synthesis_eligible="TRUE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="decentralized rural water-sector institutional framework, Brazil",
    institutional_context="water user associations vs. local government management",
    )

add("S921",
    study_design_class="two-case comparative process-tracing analysis",
    evidence_level="high",
    mechanism_family="institutional_fragmentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="Safe Drinking Water Act polycentric federalism, United States",
    institutional_context="New York City DEP; Flint, Michigan water system",
    )

add("S922",
    study_design_class="documentary/historical institutional analysis (practitioner perspective)",
    evidence_level="high",
    mechanism_family="legal_status",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="1989 UK water-industry privatisation legal framework",
    institutional_context="Thames Water Plc, OFWAT, Environment Agency, Drinking Water Inspectorate",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EM))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EM)

print(f"New total: {len(rows)}")
