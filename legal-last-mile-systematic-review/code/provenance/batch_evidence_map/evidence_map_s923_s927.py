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

add("S923",
    study_design_class="instrumental-variable econometric analysis of national household survey data",
    evidence_level="high",
    mechanism_family="fees",
    outcome_family="affordability",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="1992 RMI law right to water/energy access; municipal delegation contracts (management, lease, concession); Sapin Law bidding transparency, France",
    institutional_context="municipal water services, directly managed or delegated to private companies",
    )

add("S924",
    study_design_class="documentary/policy case-study analysis",
    evidence_level="high",
    mechanism_family="institutional_fragmentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="Ontario Municipal Acts; Safe Drinking Water Act 2002; Clean Water Act 2006 (post-Walkerton reregulation)",
    institutional_context="Ontario municipal water utilities; alternative service delivery (ASD) models",
    )

add("S925",
    study_design_class="qualitative case study with semi-structured elite interviews",
    evidence_level="high",
    mechanism_family="institutional_fragmentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="Ghana Water Company Limited governance/organizational-autonomy reform",
    institutional_context="Ghana Water Company Limited (GWCL); Ministry of Water Works and Housing; international donors",
    )

add("S926",
    study_design_class="institutional/programmatic case study with before/after district-level data",
    evidence_level="high",
    mechanism_family="bureaucratic_assistance",
    outcome_family="sanitation_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="Total Sanitation Campaign; Nirmal Bharat Abhiyan; MGNREGA; National Rural Livelihoods Mission, India",
    institutional_context="Nadia District administration; Gram Panchayats",
    )

add("S927",
    study_design_class="ten-year longitudinal anthropological/ethnographic case study",
    evidence_level="high",
    mechanism_family="discretion",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="Central Saanich municipal watermain extension decision, British Columbia, Canada",
    institutional_context="Central Saanich municipal council and municipal engineers",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EM))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EM)

print(f"New total: {len(rows)}")
