#!/usr/bin/env python3
import csv, tempfile, os

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
EMAP = f"{BASE}/05_analysis/descriptive/evidence_map.csv"

with open(EMAP, newline="") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    rows = list(r)
    existing_ids = {row["study_id"] for row in rows}

def add(sid, study_design_class, evidence_level, mechanism_family, outcome_family,
        quant_eligible, qual_eligible, legal_context, institutional_context):
    assert sid not in existing_ids, f"{sid} already in evidence_map"
    rows.append({
        "study_id": sid,
        "study_design_class": study_design_class,
        "evidence_level": evidence_level,
        "mechanism_family": mechanism_family,
        "outcome_family": outcome_family,
        "quantitative_synthesis_eligible": quant_eligible,
        "qualitative_synthesis_eligible": qual_eligible,
        "legal_context": legal_context,
        "institutional_context": institutional_context,
    })

add("S813", "qualitative case study (interviews, community case studies)", "high", "documentation",
    "water_access", "FALSE", "TRUE",
    "informal-settlement legal barrier to service extension, negotiated institutions, Brazil",
    "municipal water utility decision makers, Sao Paulo favelas")

add("S814", "qualitative institutional case study", "high", "institutional_fragmentation",
    "sanitation_access", "FALSE", "TRUE",
    "municipal laws establishing participatory water-governance committees, Brazil",
    "Municipal Sanitation Committee (COMUSA), Belo Horizonte")

add("S815", "legal/institutional case study", "high", "institutional_fragmentation",
    "water_access", "FALSE", "TRUE",
    "unresolved Aboriginal-title water rights, fragmented federal/provincial jurisdiction, Canada",
    "federal, provincial, and municipal governments, First Nations reserves")

add("S816", "household questionnaire survey", "high", "eligibility",
    "affordability", "FALSE", "TRUE",
    "National Water Policy cost-recovery mandate, human right to water, Tanzania",
    "Itumba/Isongole Urban Water Authority, village water committees")

add("S817", "qualitative institutional case study", "high", "institutional_fragmentation",
    "water_access", "FALSE", "TRUE",
    "absence of specific WASH legal framework, jurisdictional disconnect, Malawi",
    "local council, Northern Region Water Board, Karonga Town")

add("S818", "documentation review with interviews", "high", "eligibility",
    "water_access", "FALSE", "TRUE",
    "statutory water board discretionary connection policy, Waterworks Act 1995, Malawi",
    "Northern Region Water Board, Mzuzu City")

add("S819", "institutional/legal case study", "high", "fees",
    "affordability", "FALSE", "TRUE",
    "national WSS tariff and concession regulatory framework, Chile",
    "Superintendencia de Servicios Sanitarios (SISS), 53 WSS providers")

add("S820", "household demand/affordability survey", "moderate-high", "fees",
    "affordability", "FALSE", "TRUE",
    "municipal water-utility tariff/connection-fee structure, Indonesia",
    "PDAM Kota Padang, PAMSIMAS")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
