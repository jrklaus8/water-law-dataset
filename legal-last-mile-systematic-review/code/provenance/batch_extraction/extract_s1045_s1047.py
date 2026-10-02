#!/usr/bin/env python3
import csv, tempfile, os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/03_extraction/extracted_data/extraction_database.csv"
RESEARCHER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"


def atomic_write(path, fieldnames, rows):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path))
    with os.fdopen(fd, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp, path)


def blank_row(fieldnames):
    return {fn: "" for fn in fieldnames}


with open(PATH, newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

existing_ids = {r["study_id"] for r in rows}

new_rows = []

# S1045 -- Jimenez, Cortobius & Kjellen 2014
r = blank_row(fieldnames)
r.update({
    "study_id": "S1045",
    "citation": "Jimenez A, Cortobius M, Kjellen M (2014). Water, sanitation and hygiene and indigenous peoples: a review of the literature. Water International 39(3):277-293.",
    "doi": "10.1080/02508060.2014.903453",
    "publication_year": "2014",
    "publication_type": "journal article (systematic literature review)",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "multi-country (global review; concentrated in US, Canada, New Zealand, Australia)",
    "subnational_unit": "",
    "legal_system": "mixed (review spans multiple legal systems)",
    "urban_rural": "rural",
    "service_provider": "government/development agencies; community-based water-service delivery structures",
    "regulatory_model": "review of legislative frameworks and indigenous water/land rights recognition, joint management agreements, pluralistic legal systems (customary + statutory law)",
    "population": "indigenous peoples and ethnic minorities (185 peer-reviewed articles reviewed, from 782 initially identified)",
    "sample_size": "185 articles (systematic 3-stage review: keyword search, abstract review, thematic content review)",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "",
    "tenure_status": "",
    "legal_status": "TRUE",
    "indigenous_population": "TRUE",
    "migrant_population": "",
    "eligibility": "TRUE",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "",
    "documentation": "",
    "tenure": "TRUE",
    "property": "TRUE",
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "TRUE",
    "procedural_steps": "",
    "delay": "",
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
    "bureaucratic_assistance": "",
    "formal_connection": "",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
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
    "study_design": "systematic literature review (185 articles, 3-stage search/selection/thematic-review process)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "",
    "attrition": "",
    "reporting_bias": "",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": (
        "Moderate: systematic review synthesizing 185 articles finds indigenous peoples "
        "systematically have lower WASH access than non-indigenous populations wherever data "
        "exist; documents a dedicated 'Legislative frameworks and indigenous rights' theme "
        "(18 articles) covering international/domestic legal recognition of indigenous water "
        "rights, joint management agreements (e.g. New Zealand Waikato River Settlement "
        "co-management), and pluralistic legal systems, plus direct WaSH-service-access "
        "findings on tariff-system barriers specific to indigenous communities and the "
        "structural disadvantage indigenous peoples face participating in Western-dominated "
        "water-management/legal processes despite formal rights recognition."
    ),
    "source_document": "Jimenez, Cortobius & Kjellen 2014 (retrieved via Google Drive)",
    "page": "277-293",
    "table": "Table 1 (thematic distribution of 185 reviewed articles)",
    "figure": "",
    "section": "Legislative frameworks and indigenous rights; Planning, participation and traditional knowledge; Water, sanitation and hygiene (WaSH) results sections",
    "exact_location": "Results sections on legislative frameworks/indigenous rights and WaSH, and Discussion",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md criterion 3 (systematic empirical synthesis): "
        "unlike Novotny et al. 2018 (Batch 209, EXCLUDE E01, institutional factors only a "
        "minor 4.4% subcategory of a broad multi-factor review), legal/institutional content "
        "here is a central, substantial organizing theme of the review (legislative "
        "frameworks/indigenous rights as a dedicated 18-article category, plus extensive "
        "institutional-governance content within the 81-article participation category), "
        "directly synthesizing how legal/institutional mechanisms affect a marginalized "
        "population's water/sanitation access. No regression-based effect size reported "
        "(review of qualitative/descriptive literature); not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1046 -- Alda-Vidal, Kooy & Rusca 2018
r = blank_row(fieldnames)
r.update({
    "study_id": "S1046",
    "citation": "Alda-Vidal C, Kooy M, Rusca M (2018). Mapping operation and maintenance: an everyday urbanism analysis of inequalities within piped water supply in Lilongwe, Malawi. Urban Geography.",
    "doi": "10.1080/02723638.2017.1292664",
    "publication_year": "2018",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Malawi",
    "subnational_unit": "Lilongwe",
    "legal_system": "common law (Malawi)",
    "urban_rural": "urban",
    "service_provider": "Lilongwe Water Board (LWB)",
    "regulatory_model": "centralized piped water utility; everyday administrative/operational maintenance practices",
    "population": "residents of low-income areas (LIAs)/informal settlements and high-end residential areas served by LWB's centralized network (78% of ~1 million residents)",
    "sample_size": "38 semi-structured interviews with LWB employees (operators to managers); 4 months of fieldwork (2014), participant observation, participatory mapping, 1 focus group",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "",
    "documentation": "",
    "tenure": "",
    "property": "",
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "",
    "procedural_steps": "TRUE",
    "delay": "",
    "discretion": "TRUE",
    "hardship_exception": "",
    "administrative_review": "",
    "complaint": "",
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
    "service_coverage": "",
    "service_reliability": "TRUE",
    "service_quantity": "TRUE",
    "service_quality": "",
    "affordability": "",
    "service_continuity": "TRUE",
    "application_success": "",
    "refusal": "",
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
    "study_design": "qualitative process-based analysis (semi-structured interviews, participant observation, participatory mapping, focus group)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "",
    "attrition": "",
    "reporting_bias": "",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": (
        "High: in-depth fieldwork with Lilongwe Water Board staff documents how everyday "
        "administrative/operational maintenance practices (e.g. discretionary prioritization "
        "of repairs, valve operation, scheduling) performed by utility engineers and operators "
        "produce differential water-supply continuity and quantity between low-income "
        "areas/informal settlements (served via kiosks, much higher supply infrequency) and "
        "high-end residential areas (in-house connections), within a single nominally "
        "universal centralized network serving 78% of the city's population -- an "
        "institutional/administrative-practice mechanism directly producing intra-network "
        "access inequality."
    ),
    "source_document": "Alda-Vidal, Kooy & Rusca 2018 (retrieved via Google Drive)",
    "page": "",
    "table": "",
    "figure": "",
    "section": "Everyday Practices and urban water inequalities; empirical findings on LWB operational practices",
    "exact_location": "Introduction and empirical sections documenting LIA vs. high-end-area supply differentials",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: qualitative institutional/administrative-practice "
        "mechanism study with a documented differential water-supply-continuity/quantity "
        "outcome between poorer and wealthier areas within the same centralized network. No "
        "regression-based effect size reported (qualitative process-based analysis); not "
        "added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1047 -- Haglund 2014
r = blank_row(fieldnames)
r.update({
    "study_id": "S1047",
    "citation": "Haglund L (2014). Water governance and social justice in Sao Paulo, Brazil. Water Policy 16(1):78-96.",
    "doi": "10.2166/wp.2014.208",
    "publication_year": "2014",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Brazil",
    "subnational_unit": "Sao Paulo metropolitan region",
    "legal_system": "civil law (Brazil)",
    "urban_rural": "urban",
    "service_provider": "municipal/state water and sanitation utilities; courts; Ministerio Publico (Public Prosecutor's Office)",
    "regulatory_model": "litigation-based rights adjudication; Ministerio Publico legal advocacy for water/sanitation access and environmental protection",
    "population": "irregular/peripheral communities in Sao Paulo metropolitan region (~20 million people sharing water resources)",
    "sample_size": "40 key-informant interviews (lawyers, litigants, judges, water/sanitation experts, public administrators, activists); historical/archival court-case and policy-document analysis, 2009-2012",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "TRUE",
    "legal_status": "TRUE",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "TRUE",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "TRUE",
    "documentation": "",
    "tenure": "TRUE",
    "property": "TRUE",
    "planning": "TRUE",
    "zoning": "TRUE",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "",
    "procedural_steps": "",
    "delay": "",
    "discretion": "TRUE",
    "hardship_exception": "",
    "administrative_review": "TRUE",
    "complaint": "TRUE",
    "judicial_review": "TRUE",
    "disconnection": "",
    "reconnection": "",
    "sanction": "",
    "participation": "TRUE",
    "institutional_fragmentation": "TRUE",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
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
    "study_design": "qualitative case study (historical/archival data, 40 key-informant interviews, court-case and policy-document analysis)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "",
    "attrition": "",
    "reporting_bias": "",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": (
        "High: documents how legal adjudication through Brazilian courts, with the Ministerio "
        "Publico acting as a key advocate for both human rights and environmental protection, "
        "increasingly resolves conflicts over irregular/peripheral communities' water and "
        "sanitation access versus watershed-protection and other competing uses; based on "
        "archival case analysis and 40 key-informant interviews (lawyers, litigants, judges, "
        "administrators), documents how legal intervention reshapes both water-governance "
        "outcomes for marginalized communities and the legal field itself (broadening "
        "conceptions of 'justice' toward collective, substantive, and systemic remedies)."
    ),
    "source_document": "Haglund 2014 (retrieved via Google Drive)",
    "page": "78-96",
    "table": "",
    "figure": "",
    "section": "Introduction; methodology; analysis of legal adjudication and water/sanitation access conflicts",
    "exact_location": "Throughout, especially the analysis of court cases involving irregular-settlement water/sanitation access vs. watershed protection",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/legal mechanism "
        "(litigation-based rights advocacy via the Ministerio Publico) study documenting "
        "effects on water/sanitation service-access equity for marginalized peripheral "
        "communities, following the Hoogesteger (S1043, Batch 210) legal-advocacy-mechanism "
        "precedent. No regression-based effect size reported (qualitative case study); not "
        "added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

for nr in new_rows:
    assert nr["study_id"] not in existing_ids, nr["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"extraction_database.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
