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

add("S965",
    study_design_class="ethnographic case study with follow-along and operator participant observation, interviews",
    evidence_level="high",
    mechanism_family="enforcement",
    outcome_family="sanitation_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="KCCA regulatory legitimization of gulper pit-emptying technology, Kampala Water and Sanitation Forum",
    institutional_context="Kampala Capital City Authority (KCCA), Water for People NGO, gulper operator small businesses",
    )

add("S966",
    study_design_class="problem-driven governance and political economy analysis (PGPE) with document review and interviews",
    evidence_level="high",
    mechanism_family="institutional_fragmentation",
    outcome_family="sanitation_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="Tanzania decentralization-by-devolution policy (1998); National Sanitation Campaign, draft Sanitation and Hygiene Policy 2011",
    institutional_context="district councils, PMO-RALG, Ministry of Health and Social Welfare",
    )

add("S967",
    study_design_class="case study with interviews, focus groups, and stakeholder survey",
    evidence_level="moderate",
    mechanism_family="participation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="California Water Code Section 79505.5, Disadvantaged Community Pilot Project Study, Integrated Regional Water Management program",
    institutional_context="Kings Basin Water Authority, California Department of Water Resources",
    )

add("S968",
    study_design_class="ethnographic fieldwork with documentary analysis and practitioner interviews",
    evidence_level="high",
    mechanism_family="institutional_fragmentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="fragmented government funding responsibility for Indigenous housing infrastructure maintenance, Australia",
    institutional_context="state/territory Water Authorities, Housing for Health program, public housing agencies",
    )

add("S969",
    study_design_class="cross-national OLS regression analysis, 43 African countries",
    evidence_level="high",
    mechanism_family="legal_status",
    outcome_family="water_access",
    quantitative_synthesis_eligible="TRUE",
    qualitative_synthesis_eligible="FALSE",
    legal_context="colonial-era governance duration and institutional/infrastructural legacy across 43 African countries",
    institutional_context="colonial and post-independence national/municipal water and sanitation authorities",
    )

add("S970",
    study_design_class="comparative qualitative political-economy case-study analysis, three countries",
    evidence_level="high",
    mechanism_family="legal_status",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="constitutional human-right-to-water reforms, Uruguay (2004), Bolivia and Ecuador plurinational constitutions",
    institutional_context="Obras Sanitarias del Estado (Uruguay), SEMAPA (Cochabamba, Bolivia), national water ministries",
    )

add("S971",
    study_design_class="qualitative case study with document review, semi-structured interviews, and field residence",
    evidence_level="high",
    mechanism_family="institutional_fragmentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="Kenya Water Act 2002, Water Service Provider licensing, Water Resource Users Association membership",
    institutional_context="Kisayani community water committee, Water Resources Management Authority, Tanathi Water Services Board",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EM))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EM)

print(f"New total: {len(rows)}")
