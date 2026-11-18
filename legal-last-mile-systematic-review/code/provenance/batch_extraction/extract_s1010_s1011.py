#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/03_extraction/extracted_data/extraction_database.csv"
RESEARCHER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"


def blank_row(fieldnames):
    return {k: "" for k in fieldnames}


def atomic_write(path, fieldnames, rows):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path))
    with os.fdopen(fd, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp, path)


with open(PATH, newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

existing_ids = {r["study_id"] for r in rows}

new_rows = []

# S1010 -- Sarkar 2019, Mathare, Nairobi, Kenya
r = blank_row(fieldnames)
r.update({
    "study_id": "S1010",
    "citation": "Sarkar A (2019). Can shared standpipes fulfil the Sustainable Development Goal of universal access to safe water for urban poor in Kenya? Water Policy 21(5):1034-1049.",
    "doi": "10.2166/wp.2019.047",
    "publication_year": "2019",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Kenya",
    "subnational_unit": "Mathare informal settlement, Nairobi",
    "legal_system": "common law (Kenya, post-colonial)",
    "urban_rural": "urban informal settlement",
    "service_provider": "Water Service Providers (WSPs) -- CBOs, self-help groups, private operators -- licensed by Water Service Boards under the Water Services Regulatory Board",
    "regulatory_model": "Water Act 2002 institutional framework (WSBs, WSPs, WSRB tariff/licensing regulation); colonial-era Vagrancy Act 1902 legacy shaping infrastructure distribution",
    "population": "residents of Mathare slum, Nairobi, relying on paid community standpipes",
    "sample_size": "258 households surveyed; focus group discussions; key-informant interviews",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "TRUE",
    "legal_status": "TRUE",
    "indigenous_population": "",
    "migrant_population": "TRUE",
    "eligibility": "TRUE",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "TRUE",
    "documentation": "",
    "tenure": "TRUE",
    "property": "TRUE",
    "planning": "",
    "zoning": "TRUE",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "TRUE",
    "procedural_steps": "TRUE",
    "delay": "TRUE",
    "discretion": "TRUE",
    "hardship_exception": "",
    "administrative_review": "TRUE",
    "complaint": "TRUE",
    "judicial_review": "",
    "disconnection": "",
    "reconnection": "",
    "sanction": "",
    "participation": "",
    "institutional_fragmentation": "TRUE",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "service_quantity": "TRUE",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "TRUE",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "TRUE",
    "effect_measure": "",
    "effect_estimate": "",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "mixed-methods case study: household survey, focus group discussions, key-informant interviews, and secondary macro-trend data analysis",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "",
    "attrition": "",
    "reporting_bias": "",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": "High: the Water Act 2002 licensing/tariff-regulation framework is documented, via household survey and interviews, to be weakly enforced at the standpipe level, permitting standpipe managers to charge tariffs 5-7x the regulated bulk rate, engage in tribal-affiliation-based favouritism in queue priority, and monopolize supply -- directly producing measured price disparities and access hardship for Mathare slum residents; the colonial-era Vagrancy Act 1902 pass-system legacy is explicitly traced as the origin of the segregated infrastructure that persists today.",
    "source_document": "Sarkar 2019, Water Policy (retrieved via Google Drive)",
    "page": "",
    "table": "Table 1 (standpipe tariffs and profits); Table 2 (comparative prices by source); Table 3 (willingness to pay)",
    "figure": "Fig. 1 (piped water coverage trend); Fig. 2 (institutional framework for water supply)",
    "section": "Throughout, esp. 'Socio-economic implications of accessing water from standpipes' and 'Management of standpipes'",
    "exact_location": "Throughout results sections",
    "extraction_note": "INCLUDE per INCLUSION_EXCLUSION.md: statutory regulatory framework (Water Act 2002) and its weak enforcement at the point of service directly and documentably produce differential water-access/affordability outcomes for the urban poor, with an explicit colonial-legal-legacy mechanism. Extends the colonial-legacy precedent (Njoh & Akiwumi S969; Kooy & Bakker S1001) and institutional-capture precedent (Giglioli & Swyngedouw S990). No regression-based effect size isolating the legal mechanism's marginal effect on a water-access outcome is reported (descriptive mixed-methods case study); not added to effect_sizes.csv per the strict Family A/B/C framework.",
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1011 -- Romano 2012, Nicaragua
r = blank_row(fieldnames)
r.update({
    "study_id": "S1011",
    "citation": "Romano ST (2012). From Protest to Proposal: The Contentious Politics of the Nicaraguan Anti-Water Privatisation Social Movement. Bulletin of Latin American Research 31(4):499-514.",
    "doi": "10.1111/j.1470-9856.2012.00700.x",
    "publication_year": "2012",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Nicaragua",
    "subnational_unit": "national (Managua, Matagalpa, Jinotega departments)",
    "legal_system": "civil law (Nicaragua)",
    "urban_rural": "national (rural CAPS and urban ENACAL service)",
    "service_provider": "Comites de Agua Potable y Saneamiento (CAPS) community water-user associations; ENACAL (national water utility)",
    "regulatory_model": "General Water Law (Law 620, 2007) and Special CAPS Law (Law 722, 2010) granting formal legal status/recognition to community water-management committees previously operating without legal basis since the 1970s",
    "population": "over 1 million rural Nicaraguan residents served by CAPS-managed water systems",
    "sample_size": "roughly 40 semi-structured interviews; observation of meetings/forums; focus groups with 5 rural water users' associations",
    "household_level": "",
    "community_level": "TRUE",
    "income_group": "",
    "tenure_status": "",
    "legal_status": "TRUE",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "",
    "burden": "",
    "discretion_accommodation": "TRUE",
    "enforcement": "TRUE",
    "documentation": "TRUE",
    "tenure": "",
    "property": "",
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "",
    "procedural_steps": "TRUE",
    "delay": "",
    "discretion": "",
    "hardship_exception": "",
    "administrative_review": "TRUE",
    "complaint": "",
    "judicial_review": "",
    "disconnection": "",
    "reconnection": "",
    "sanction": "",
    "participation": "TRUE",
    "institutional_fragmentation": "TRUE",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "",
    "service_continuity": "TRUE",
    "application_success": "TRUE",
    "refusal": "TRUE",
    "delay_outcome": "",
    "effect_measure": "",
    "effect_estimate": "",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "qualitative case study using semi-structured interviews, participant observation, and legislative/documentary analysis",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "",
    "attrition": "",
    "reporting_bias": "",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": "Moderate-high: documents that CAPS -- which provide the primary water access mechanism for over 1 million rural Nicaraguans -- operated for over three decades with no legal basis or formal state recognition, that this legal void was reproduced even in the comprehensive General Water Law (620), and that subsequent social-movement mobilization achieved formal legal recognition via the Special CAPS Law (722), directly affecting CAPS' capacity to access funding, technical support, and legal standing for water-system investment and maintenance.",
    "source_document": "Romano 2012, Bulletin of Latin American Research (retrieved via Google Drive)",
    "page": "",
    "table": "",
    "figure": "",
    "section": "Throughout, esp. 'Key Anti-Privatisation Organisations and Coalitions' and 'Democratising Representative Institutions through Inclusive Policy Formation'",
    "exact_location": "Throughout results/discussion sections",
    "extraction_note": "INCLUDE per INCLUSION_EXCLUSION.md: legal recognition/non-recognition of community water-management institutions (CAPS) is documented as a direct institutional mechanism affecting rural water-governance capacity and access for over 1 million residents. Extends the Nelson et al Fiji statutory water-committee governance precedent (S991-family, Batch 196) and Harvey Uganda WASH regulatory/committee legal-status precedent (Batch 196). No regression-based effect size is reported (qualitative case study); not added to effect_sizes.csv.",
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

for r in new_rows:
    assert r["study_id"] not in existing_ids, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"extraction_database.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
