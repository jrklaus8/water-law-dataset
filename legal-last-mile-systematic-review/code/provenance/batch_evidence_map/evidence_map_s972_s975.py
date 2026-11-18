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

add("S972",
    study_design_class="documentary/archival case-study analysis of municipal financial and legal records",
    evidence_level="high",
    mechanism_family="enforcement",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="federal court oversight (1977-2013), Michigan emergency-manager bankruptcy law, interest rate swap contracts",
    institutional_context="Detroit Water and Sewerage Department, state-appointed emergency manager",
    )

add("S973",
    study_design_class="policy/institutional impact analysis with national infrastructure and economic statistics",
    evidence_level="high",
    mechanism_family="legal_status",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="Italy Galli Law (Law 36/1994), Optimal Territorial Area (ATO) revenue-cap regulation",
    institutional_context="municipally owned enterprises, ATO aggregated utilities",
    )

add("S974",
    study_design_class="exploratory qualitative case study with semi-structured interviews",
    evidence_level="moderate",
    mechanism_family="legal_status",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="unauthorised (illegal) settlement status, Delhi Jal Board regularisation guidelines",
    institutional_context="Delhi Jal Board, informal bore-well operators, resident welfare associations",
    )

add("S975",
    study_design_class="documentary/policy analysis of institutional budgets, legislation, and archival news sources",
    evidence_level="high",
    mechanism_family="fees",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="EU Water Framework Directive, Urban Wastewater Treatment Directive, Drinking Water Directive; Catalan water-tax financing law",
    institutional_context="Agencia Catalana de l'Aigua, Aigues Ter-Llobregat, Aigues de Barcelona/AGBAR",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EM))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EM)

print(f"New total: {len(rows)}")
