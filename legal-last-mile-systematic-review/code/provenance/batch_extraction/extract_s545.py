import csv, tempfile, os

path = "03_extraction/extracted_data/extraction_database.csv"

with open(path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

def blank_row():
    return {k: "" for k in fieldnames}

row = blank_row()
row.update({
    "study_id": "S545",
    "citation": 'Dobbin KB (2020). "\'Good Luck Fixing the Problem\': Small Low-Income Community Participation in Collaborative Groundwater Governance and Implications for Drinking Water Source Protection." Society & Natural Resources, 33(12), 1468-1485.',
    "doi": "10.1080/08941920.2020.1772925",
    "publication_year": "2020",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "United States",
    "subnational_unit": "San Joaquin Valley, California (Tulare Lake and San Joaquin hydrologic regions)",
    "legal_system": "common law",
    "urban_rural": "rural (small low-income communities, populations under 10,000)",
    "service_provider": "Small public water systems (cities, community services districts), privately-owned community water systems, and domestic well owners, all overseen by Groundwater Sustainability Agencies (GSAs) formed under California's Sustainable Groundwater Management Act (SGMA)",
    "regulatory_model": "SGMA (2014) requires local agencies in 127 high/medium-priority groundwater basins to form Groundwater Sustainability Agencies (GSAs) and develop Groundwater Sustainability Plans (GSPs) by 2020/2022; the statute lists 11 categories of beneficial users that must be involved, including Disadvantaged Communities (DACs, defined by median household income) and domestic well owners, but leaves the specific form of representation (voting member, non-voting member, advisory/stakeholder committee, or no formal relationship) to local GSA discretion; privately-owned water systems are legally barred from acting as a GSA independently and, per this study, none achieved formal representation despite technically available pathways; formal voting representation typically requires a financial contribution (e.g., one community's non-voting seat saved $8,000 versus a voting seat).",
    "population": "Small, low-income (Disadvantaged Community) drinking water stakeholders -- public water system staff/elected officials, residents/community leaders, and domestic well owners -- in California's San Joaquin Valley",
    "sample_size": "27 semi-structured interviews with 35 individuals, representing 23 unique communities, conducted October 2018-May 2019",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "TRUE",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "TRUE",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "TRUE",
    "documentation": "",
    "tenure": "",
    "property": "",
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "TRUE",
    "procedural_steps": "TRUE",
    "delay": "TRUE",
    "discretion": "TRUE",
    "hardship_exception": "",
    "administrative_review": "",
    "complaint": "",
    "judicial_review": "TRUE",
    "disconnection": "",
    "reconnection": "",
    "sanction": "",
    "participation": "TRUE",
    "institutional_fragmentation": "TRUE",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "TRUE",
    "formal_connection": "",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "",
    "service_reliability": "TRUE",
    "service_quantity": "TRUE",
    "service_quality": "TRUE",
    "affordability": "TRUE",
    "service_continuity": "TRUE",
    "application_success": "",
    "refusal": "TRUE",
    "delay_outcome": "TRUE",
    "effect_measure": "Qualitative thematic analysis (Dedoose-coded, structural and thematic coding of 1,066 coded excerpts) of 27 interviews; no statistical contrast",
    "effect_estimate": "Half (12 of 23) of represented communities had representatives actively involved in SGMA/GSA implementation; in no case did a privately-owned community water system or domestic-well community achieve formal GSA representation, though all types of local public water providers (including cities) lacked formal representation in at least one case. Financial barriers directly shaped participation: one community chose a non-voting GSA role over a voting one to save $8,000. Interviewees with advisory/stakeholder (non-voting) positions repeatedly described having 'voice but not vote,' and even those with formal voting seats often felt uninfluential ('majority rules'). Transparency failures were common: non-Brown-Act-compliant meetings, last-minute cancellations, and one community's first notification about SGMA arriving in 2018, three years after the law took effect. Across nearly all interviews, drinking-water/water-quality considerations were reported as absent or a minimal part of GSA deliberations and Groundwater Sustainability Plan (GSP) development, and 25% of interviewees explicitly expected SGMA's net effect on their community to be negative (new fees/costs for already-unaffordable water, moratoria/reductions risking existing wells running dry) rather than a source-water-protection benefit.",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "35",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "qualitative case study (semi-structured interviews, purposive plus snowball sampling, constant comparative coding)",
    "study_design": "qualitative case study of small low-income community participation in collaborative groundwater governance under California's Sustainable Groundwater Management Act, based on 27 semi-structured interviews with 35 individuals across 23 San Joaquin Valley communities",
    "risk_of_bias_tool": "CASP Qualitative Studies Checklist",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "",
    "attrition": "",
    "reporting_bias": "",
    "legal_measurement_quality": "",
    "outcome_measurement_quality": "",
    "mechanism_certainty": "2",
    "source_document": "Dobbin 2020, Society & Natural Resources 33(12):1468-1485",
    "page": "",
    "table": "Table 2",
    "figure": "",
    "section": "Community Participation in SGMA Implementation; Challenges (Lack of Access; Lack of Influence); Implications for Source Water Protection and Rural Drinking Water Provision",
    "exact_location": "Table 2 (types and prevalence of formal relationship between small DACs and overlying GSAs); Challenges section (financial, technical, and institutional barriers to representation); Implications section (absence of drinking-water considerations in GSP development)",
    "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Documents a genuine legal-administrative participation regime: SGMA statutorily lists Disadvantaged Communities and domestic well owners among 11 mandatory beneficial-user categories, but leaves the form of representation to GSA discretion, resulting in privately-owned water systems and domestic-well communities never achieving formal voting representation; financial cost of voting seats, technical/staff capacity disparities, and transparency failures (non-Brown-Act-compliant meetings, delayed notification) compound exclusion; drinking-water needs are largely unaddressed in resulting Groundwater Sustainability Plans. record_id RC85926098F35.",
    "researcher": "Claude-AI-fulltext-2026-09-21",
    "date_extracted": "2026-09-21",
    "evidence_status": "OBSERVED",
})

rows.append(row)

fd, tmp = tempfile.mkstemp(dir="03_extraction/extracted_data")
with os.fdopen(fd, "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmp, path)

print("done, extraction rows now", len(rows))
