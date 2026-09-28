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

add("S954",
    study_design_class="government-commissioned institutional assessment with quantified coverage/budget data",
    evidence_level="high",
    mechanism_family="institutional_fragmentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="African Development Bank Rural Water Supply and Sanitation Initiative, Swaziland",
    institutional_context="Rural Water Supply Branch; community Water Supply and Sanitation Committees",
    )

add("S955",
    study_design_class="mixed-methods 400-respondent household survey with institutional expenditure analysis",
    evidence_level="high",
    mechanism_family="institutional_fragmentation",
    outcome_family="sanitation_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="Ghana Tain district local assembly sanitation-promotion budget",
    institutional_context="local district assembly",
    )

add("S956",
    study_design_class="Cultural Theory and Systems Thinking Analysis institutional/governance assessment",
    evidence_level="high",
    mechanism_family="institutional_fragmentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="Cameroon decentralization laws vs. centralized government water-resource control",
    institutional_context="Community-Based Water Management (CBWM) systems",
    )

add("S957",
    study_design_class="interview-based fieldwork with actor/decision-making analysis",
    evidence_level="moderate",
    mechanism_family="participation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="local water/sanitation decision-making institutions, Vioolsdrif South Africa",
    institutional_context="engineering, user, environmental, cultural, socio-economic actors",
    )

add("S958",
    study_design_class="single-county documentary/case-study analysis with enforcement records",
    evidence_level="high",
    mechanism_family="enforcement",
    outcome_family="sanitation_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="Alabama state sanitary-handling-of-sewage health code; heir-property land-tenure system",
    institutional_context="Lowndes County public health department and courts",
    )

add("S959",
    study_design_class="single-settlement empirical case study of informal regulatory practices",
    evidence_level="high",
    mechanism_family="institutional_fragmentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="statutory exclusion of bosti (informal settlement) residents, Dhaka Bangladesh",
    institutional_context="informal local associations, NGOs, powerful well-connected inhabitants",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EM))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EM)

print(f"New total: {len(rows)}")
