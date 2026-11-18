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

add("S932",
    study_design_class="documentary/institutional case-study analysis with national regulatory-history review",
    evidence_level="moderate",
    mechanism_family="institutional_fragmentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="1906 Public Domain and Water Use Act; post-2006 Ministry of Water reforms, Bolivia",
    institutional_context="publicly-owned Sucre water-services company",
    )

add("S933",
    study_design_class="four-year multi-city participatory action-research/implementation study",
    evidence_level="high",
    mechanism_family="institutional_fragmentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="South Africa post-1994 progressive water-services rights legislation",
    institutional_context="local municipal authorities; 'Raising Citizens' Voice' methodology",
    )

add("S934",
    study_design_class="documentary/policy analysis with comparative case studies",
    evidence_level="moderate",
    mechanism_family="institutional_fragmentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="India rural water-supply sector-reform pilot projects, 63 districts",
    institutional_context="state Rural Water Supply Departments; NGO-led community-management models",
    )

add("S935",
    study_design_class="original narrative-interview ethnographic fieldwork",
    evidence_level="high",
    mechanism_family="discretion",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="South Africa constitutional right to basic water",
    institutional_context="eThekwini municipality differentiated service-delivery technologies",
    )

add("S936",
    study_design_class="mail-questionnaire survey with before/after self-reported comparison",
    evidence_level="moderate",
    mechanism_family="legal_status",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="1935 Missouri Public Water Supply District enabling legislation",
    institutional_context="Boone County PWSD No. 5; Barton County PWSD No. 1",
    )

add("S937",
    study_design_class="ex-ante regulatory impact assessment (MCDA, MACBETH method)",
    evidence_level="moderate",
    mechanism_family="enforcement",
    outcome_family="sanitation_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="Federal Law 11445/2007; Minas Gerais State Law 13317/1999, Brazil",
    institutional_context="ARSAE water/wastewater regulatory agency; COPASA/COPANOR",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EM))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EM)

print(f"New total: {len(rows)}")
