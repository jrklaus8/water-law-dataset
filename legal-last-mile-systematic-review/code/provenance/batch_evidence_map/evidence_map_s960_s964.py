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

add("S960",
    study_design_class="policy/institutions/regulation (PIR) documentary case-study analysis with national coverage statistics",
    evidence_level="high",
    mechanism_family="institutional_fragmentation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="Brazil WSS legal framework (Law 11.445/2007, Law 14.026/2020); isomorphic mimicry of higher-income-country regulatory models",
    institutional_context="Ministry of Regional Development (urban), FUNASA (rural), 73 decentralized WSS regulatory agencies, National Water and Basic Sanitation Agency (ANA)",
    )

add("S961",
    study_design_class="qualitative case study with interviews, focus group, and document analysis",
    evidence_level="high",
    mechanism_family="formal_connection",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="Water Committees Constitution 2003 (Temeke Municipal Council, Dar es Salaam)",
    institutional_context="community-based Water Committee vs. public water-supply system connection-processing comparison",
    )

add("S962",
    study_design_class="semi-structured interview-based qualitative case study with documentary/policy analysis",
    evidence_level="high",
    mechanism_family="institutional_fragmentation",
    outcome_family="sanitation_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="Uganda 1997 Strategic Framework for Reform, Kampala Declaration on Sanitation (devolving sanitation from state to household)",
    institutional_context="National Water and Sewerage Corporation, NGO-led decentralized onsite sanitation delivery, Kawempe District",
    )

add("S963",
    study_design_class="interview-based case-study analysis with litigation tracing and documentary policy analysis",
    evidence_level="high",
    mechanism_family="legal_status",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="South Africa National Water Act 1998, Constitutional water right, free-basic-water policy, Phiri pre-paid-meter litigation (High Court/Supreme Court of Appeal)",
    institutional_context="Johannesburg Water, City of Johannesburg, Alexandra Renewal Project",
    )

add("S964",
    study_design_class="mixed-methods case study with household survey and regulatory/contract documentary analysis",
    evidence_level="high",
    mechanism_family="discretion_accommodation",
    outcome_family="water_access",
    quantitative_synthesis_eligible="FALSE",
    qualitative_synthesis_eligible="TRUE",
    legal_context="Bolivia drinking-water/sanitation Law 2029 (1999); La Paz-El Alto private concession contract and regulatory framework",
    institutional_context="Aguas del Illimani (Suez concessionaire), Superintendence of Water and Sanitation (Regulator)",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EM))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EM)

print(f"New total: {len(rows)}")
