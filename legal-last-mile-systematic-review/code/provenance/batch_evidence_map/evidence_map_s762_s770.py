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

add("S762", "mixed-methods case study", "moderate", "financing_enforcement",
    "service_reliability", "FALSE", "TRUE",
    "Ghana decentralised water governance (CWSA Regulations 2011/Legislative Instrument 2007)",
    "District Assemblies/District Water and Sanitation Teams, rural water systems, Akatsi and East Gonja districts")

add("S763", "qualitative institutional case study (IAD framework)", "moderate", "discretion_accommodation",
    "affordability", "FALSE", "TRUE",
    "Kenya Water Act 2002 commercialization framework, Delegated Management Model",
    "master operators and water kiosks, Lake Victoria region, Kenya")

add("S764", "qualitative multi-regime institutional analysis", "moderate", "institutional_fragmentation",
    "service_coverage", "FALSE", "TRUE",
    "individual/community/municipal water-sector regimes, legislative institutionalization dimension",
    "Kanata metropolitan region, Bolivia")

add("S765", "quasi-experimental difference-in-differences", "high", "tenure",
    "water_access", "TRUE", "TRUE",
    "PETT land-titling program, Peru",
    "rural households, phased land-title acquisition")

add("S766", "mixed-methods research synthesis", "moderate", "eligibility",
    "sanitation_access", "FALSE", "TRUE",
    "disability legislation and WASH policy commitments, multiple countries",
    "WEDC research project, NGOs, Uganda and Bangladesh field sites")

add("S767", "comparative multi-country institutional case study", "moderate-high", "institutional_fragmentation",
    "water_access", "FALSE", "TRUE",
    "statutory vs. actual water governance institutions, 5 countries",
    "community, district, and customary institutions, Bolivia/Mali/Nicaragua/Vietnam/Zambia")

add("S768", "qualitative case study (policy process tracing)", "moderate-high", "enforcement",
    "service_continuity", "FALSE", "TRUE",
    "corporatization/commercialization of water utility, South Africa",
    "Cape Town local authority, low-income townships")

add("S769", "qualitative case study (institutional theory + legal analysis)", "high", "institutional_fragmentation",
    "service_coverage", "FALSE", "TRUE",
    "Ekiti State Water Corporation Law No. 4 of 1997, Public Procurement Law No. 2 of 2010",
    "Ekiti State Water Corporation, Nigeria")

add("S770", "mixed-methods case study", "moderate", "enforcement",
    "sanitation_access", "FALSE", "TRUE",
    "command-and-control CLTSH sanitation campaign, formal/semi-formal sanctions",
    "kebele/woreda administration, Wolaita Zone, Ethiopia")

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EMAP))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EMAP)

print(f"New total: {len(rows)}")
