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

add("S895",
    study_design_class="mixed-methods ethnographic/documentary fieldwork study",
    evidence_level="moderate-high",
    mechanism_family="documentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="state water supply and sanitation (WSS) development programs, Vietnam",
    institutional_context="Can Tho City local government cadres, Mekong Delta",
    )

add("S896",
    study_design_class="comparative field study across seven communities",
    evidence_level="high",
    mechanism_family="formal_connection",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="Kenya Water Act 2002; 1974 National Water Master Plan",
    institutional_context="community-organized spring-protection and piped homestead-connection systems, Nyando basin",
    )

add("S897",
    study_design_class="household survey with regression analysis of administrative tariff/billing data",
    evidence_level="high",
    mechanism_family="fees",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="increasing block tariff (IBT) rate structure, Ghana",
    institutional_context="Ghana municipal water utility, Kumasi",
    )

add("S898",
    study_design_class="documentary and field-based institutional/planning case study",
    evidence_level="moderate-high",
    mechanism_family="institutional_fragmentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="urban water/sanitation planning institutions and strategies, Tanzania",
    institutional_context="Dar es Salaam Water and Sewerage Authority (DAWASA)",
    )

add("S899",
    study_design_class="comparative case study (5 water systems, household surveys, key-informant interviews)",
    evidence_level="high",
    mechanism_family="institutional_fragmentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="Local Government Act 462 (1993), Ghana",
    institutional_context="District Assemblies, Water and Sanitation Development Boards, Private Operators",
    )

add("S900",
    study_design_class="socio-technical field study (institutional/materiality analysis)",
    evidence_level="moderate-high",
    mechanism_family="documentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="water network norms, standards, design and operating regulations, Malawi",
    institutional_context="Lilongwe Water Board",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EM))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EM)

print(f"New total: {len(rows)}")
