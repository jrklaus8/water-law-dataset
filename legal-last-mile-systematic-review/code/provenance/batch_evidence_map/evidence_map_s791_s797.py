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

add("S791", "cross-national policy-document analysis", "moderate-high", "eligibility",
    "affordability", "FALSE", "TRUE",
    "national pro-poor water/sanitation governance policy, cross-national (GLAAS)",
    "national governments, UN-Water GLAAS monitoring programme")

add("S792", "qualitative field-based policy-evaluation case study", "moderate-high", "eligibility",
    "water_access", "FALSE", "TRUE",
    "government under-service policy for remote areas, Botswana",
    "government water supply agencies, Ngamiland District")

add("S793", "comparative qualitative case study", "moderate-high", "institutional_fragmentation",
    "water_access", "FALSE", "TRUE",
    "transnational PPP institutional design, areas of limited statehood",
    "10 projects, two transnational PPPs, Bangladesh/India/Kenya")

add("S794", "household contingent-valuation survey", "moderate", "institutional_fragmentation",
    "affordability", "FALSE", "TRUE",
    "fragmented water-sector institutional framework, Guatemala",
    "municipal vs. community-managed water systems")

add("S795", "quasi-experimental difference-in-differences", "high", "documentation",
    "water_access", "TRUE", "TRUE",
    "water utility privatization/renationalization, Bolivia",
    "private concessionaire, cooperative, and public utility, 4 cities")

add("S796", "comparative-historical qualitative case study", "moderate-high", "political_coordination",
    "sanitation_access", "FALSE", "TRUE",
    "local-state bureaucratic embeddedness and cohesion, Brazil",
    "municipal/state/federal agencies, Sao Paulo favelas")

add("S797", "qualitative socio-technical institutional case study", "high", "institutional_fragmentation",
    "water_access", "FALSE", "TRUE",
    "1974 complementary law establishing metropolitan region, Brazil",
    "CEDAE state water company, Rio de Janeiro Metropolitan Region")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
