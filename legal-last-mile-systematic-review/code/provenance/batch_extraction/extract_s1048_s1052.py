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

# S1048 -- Heller 2007
r = blank_row(fieldnames)
r.update({
    "study_id": "S1048",
    "citation": "Heller L (2007). Basic Sanitation in Brazil: Lessons from the Past, Opportunities from the Present, Challenges for the Future. Journal of Comparative Social Welfare 23(2):141-153.",
    "doi": "10.1080/17486830701494640",
    "publication_year": "2007",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Brazil",
    "subnational_unit": "national, with state/municipal comparison",
    "legal_system": "civil law (Brazil)",
    "urban_rural": "both",
    "service_provider": "state-owned WSS utilities (PLANASA concession model); municipal utilities",
    "regulatory_model": "PLANASA concession model (municipalities grant concession to state utilities); 2007 National Sanitation Law (Law 11,445) universalization framework",
    "population": "national population, with urban/rural and income-group breakdowns",
    "sample_size": "national administrative/census data (IBGE) analysis",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "TRUE",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "",
    "burden": "TRUE",
    "discretion_accommodation": "",
    "enforcement": "",
    "documentation": "",
    "tenure": "",
    "property": "",
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
    "judicial_review": "",
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
    "service_coverage": "TRUE",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "TRUE",
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
    "study_design": "descriptive/institutional policy analysis using national administrative (IBGE) coverage data",
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
        "Moderate: traces how the PLANASA concession model (1970s, transferring WSS "
        "administration from municipalities to state-owned utilities via concession "
        "contracts) shaped documented coverage asymmetries -- by 2000, higher-income "
        "households (>20 minimum wages) had significantly higher WSS coverage than "
        "low-income households (<1 minimum wage); rural coverage (25%) lagged urban "
        "(91.4%); PLANASA gave less priority to municipalities under 20,000 residents and "
        "was less successful in more developed/high-HDI municipalities that exercised "
        "autonomy and declined concession contracts. The 2007 National Sanitation Law "
        "(Law 11,445) subsequently established universalization-with-equity as an explicit "
        "institutional objective."
    ),
    "source_document": "Heller 2007 (retrieved via Google Drive)",
    "page": "141-153",
    "table": "",
    "figure": "Figure 1 (health-risk distribution map)",
    "section": "Current State of Access to the Services; Current Political, Institutional and Legal Situation",
    "exact_location": "Throughout, especially the PLANASA/coverage-asymmetry and National Sanitation Law sections",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine legal/institutional mechanism "
        "(concession model, state-vs-municipal utility structure, national sanitation law) "
        "study with documented differential water/sanitation-access outcomes by income and "
        "region. Descriptive/administrative-data analysis, not a regression isolating a "
        "single mechanism's marginal effect; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1049 -- Murungi & van Dijk 2014
r = blank_row(fieldnames)
r.update({
    "study_id": "S1049",
    "citation": "Murungi C, van Dijk MP (2014). Emptying, transportation and disposal of feacal sludge in informal settlements of Kampala Uganda: the economics of sanitation. Habitat International 42:69-75.",
    "doi": "10.1016/j.habitatint.2013.10.011",
    "publication_year": "2014",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Uganda",
    "subnational_unit": "Katoogo slum, Bwaise III Parish, Kawempe Division, Kampala",
    "legal_system": "common law (Uganda)",
    "urban_rural": "urban",
    "service_provider": "Kampala City Council Authority (KCCA); Private Emptiers' Association Uganda (PEAU); 2000 Trinity Agencies Limited; illegal manual emptiers",
    "regulatory_model": "unregulated/free-market emptying-fee pricing; institutional fragmentation between public (KCCA) and private operators",
    "population": "informal-settlement (slum) residents relying on on-site sanitation (pit latrines) in Kampala",
    "sample_size": "semi-structured interviews with PEAU, KCCA officials, cesspool truck operators, 2000 Trinity Agencies, NWSC, and manual emptiers; observation; secondary data",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "TRUE",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "",
    "documentation": "",
    "tenure": "",
    "property": "",
    "planning": "",
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
    "judicial_review": "",
    "disconnection": "",
    "reconnection": "",
    "sanction": "",
    "participation": "",
    "institutional_fragmentation": "TRUE",
    "political_coordination": "",
    "bureaucratic_assistance": "",
    "formal_connection": "",
    "water_access": "",
    "sanitation_access": "TRUE",
    "service_coverage": "",
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
    "study_design": "qualitative case study (semi-structured interviews, observation, secondary data review)",
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
        "Moderate: documents complete absence of government price regulation for pit-latrine "
        "emptying services, institutional fragmentation and lack of coordination between the "
        "public KCCA and private cesspool-truck operators (PEAU, 2000 Trinity Agencies), and "
        "shows how the resulting high, unregulated emptying fees (UGX 50,000-150,000 per "
        "trip) exclude poorer slum dwellers from formal emptying services, pushing them "
        "toward illegal manual emptiers who dump sludge in open environments/channels, "
        "creating an institutional/affordability barrier mechanism directly shaping "
        "informal-settlement sanitation access."
    ),
    "source_document": "Murungi & van Dijk 2014 (retrieved via Google Drive)",
    "page": "69-75",
    "table": "Tables 1-5 (emptying fee breakdowns by provider)",
    "figure": "",
    "section": "Modes of operation and breakdown of emptying costs; Actors determining emptying charges; Discussion",
    "exact_location": "Throughout, especially Discussion on lack of price regulation and institutional gap between KCCA and private operators",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: institutional/administrative-barrier "
        "(unregulated pricing, institutional fragmentation) mechanism study with a "
        "documented sanitation-affordability/access outcome for informal-settlement "
        "residents. Qualitative case study, no regression-based effect size; not added to "
        "effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1050 -- Gerlach & Franceys 2010
r = blank_row(fieldnames)
r.update({
    "study_id": "S1050",
    "citation": "Gerlach E, Franceys R (2010). Regulating Water Services for All in Developing Economies. World Development 38(9):1229-1240.",
    "doi": "10.1016/j.worlddev.2010.02.006",
    "publication_year": "2010",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "multi-country (11 metropolitan areas across Africa and Asia)",
    "subnational_unit": "11 metropolitan areas (Indonesia, India, Philippines, UK/Ghana research consortium coverage)",
    "legal_system": "mixed (multi-country comparative)",
    "urban_rural": "urban",
    "service_provider": "utilities and alternative/informal providers, under newly-introduced economic regulators",
    "regulatory_model": "economic regulation of water services introduced as part of sector reform in low/lower-middle income countries",
    "population": "urban consumers, particularly the poor in informal settlements",
    "sample_size": "11 city case studies (DFID KAR R8320 research program)",
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
    "property": "",
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "TRUE",
    "procedural_steps": "",
    "delay": "",
    "discretion": "TRUE",
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
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "TRUE",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "",
    "application_success": "",
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
    "study_design": "comparative multi-case-study analysis (11 metropolitan-area regulatory case studies)",
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
        "High: comparative case-study evidence across 11 metropolitan areas finds pro-poor "
        "regulatory outcomes constrained by inadequate framework conditions and a limited "
        "understanding by regulators of alternative/informal providers serving low-income "
        "and informal settlements; documents how operational difficulties, perceived "
        "business risk, and political reluctance deter utilities from extending formal "
        "connections into low-income/illegal settlements, leaving the urban poor reliant on "
        "unregulated alternative providers charging high prices for uncertain-quality water."
    ),
    "source_document": "Gerlach & Franceys 2010 (retrieved via Google Drive)",
    "page": "1229-1240",
    "table": "",
    "figure": "Figure 1 (regulator-government-provider relationship)",
    "section": "Introduction; comparative case-study findings across 11 metropolitan areas",
    "exact_location": "Throughout, especially the pro-poor regulatory-outcome findings",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/legal mechanism "
        "(economic regulation design) study directly examining its differential effect on "
        "water access for the urban poor across 11 developing-country cities. Comparative "
        "case-study evidence, not a single regression-based effect size; not added to "
        "effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1051 -- van Dijk, Etajak, Mwalwega & Ssempebwa 2014
r = blank_row(fieldnames)
r.update({
    "study_id": "S1051",
    "citation": "van Dijk MP, Etajak S, Mwalwega B, Ssempebwa J (2014). Financing sanitation and cost recovery in the slums of Dar es Salaam and Kampala. Habitat International 43:206-213.",
    "doi": "10.1016/j.habitatint.2014.02.003",
    "publication_year": "2014",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Uganda; Tanzania",
    "subnational_unit": "one slum in Kampala; one slum in Dar es Salaam",
    "legal_system": "common law (Uganda); mixed (Tanzania)",
    "urban_rural": "urban",
    "service_provider": "households; small enterprises; CBOs; NGOs; government",
    "regulatory_model": "mixed household/CBO/NGO/government governance structures for sanitation facilities, absent formal regulation",
    "population": "slum-dwelling households in Kampala and Dar es Salaam",
    "sample_size": "household surveys and stakeholder interviews, two slums",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "TRUE",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "",
    "documentation": "",
    "tenure": "",
    "property": "TRUE",
    "planning": "",
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
    "judicial_review": "",
    "disconnection": "",
    "reconnection": "",
    "sanction": "",
    "participation": "TRUE",
    "institutional_fragmentation": "TRUE",
    "political_coordination": "",
    "bureaucratic_assistance": "TRUE",
    "formal_connection": "",
    "water_access": "",
    "sanitation_access": "TRUE",
    "service_coverage": "",
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
    "study_design": "qualitative and quantitative mixed-methods case study (household surveys, stakeholder interviews)",
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
        "Moderate: documents how the governance structure of a sanitation facility -- "
        "privately household-owned, informally shared between households, CBO-managed "
        "community toilet (membership-restricted, contribution-based), or publicly-approved "
        "shared facility -- determines both payment obligations and eligibility conditions "
        "for access, with CBO-managed toilets explicitly 'open to a limited number of "
        "people being member of that community and contributing something.' An "
        "institutional/administrative-mechanism study of governance-structure-dependent "
        "eligibility and affordability barriers in informal-settlement sanitation access."
    ),
    "source_document": "van Dijk, Etajak, Mwalwega & Ssempebwa 2014 (retrieved via Google Drive)",
    "page": "206-213",
    "table": "",
    "figure": "",
    "section": "Type of toilet, payment and location (governance-structure table); financing/cost-recovery findings",
    "exact_location": "Throughout, especially the governance-structure/eligibility table",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: institutional/administrative-mechanism "
        "(governance-structure-dependent eligibility and fee) study with documented "
        "differential sanitation-access conditions across facility-governance types. "
        "Mixed-methods case study, no isolated regression-based effect size; not added to "
        "effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1052 -- Kurup 1991
r = blank_row(fieldnames)
r.update({
    "study_id": "S1052",
    "citation": "Kurup KB (1991). Community Based Approaches in Water Supply and Sanitation Programme -- An Indian Experience. Social Indicators Research 24:403-414.",
    "doi": "",
    "publication_year": "1991",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "Kerala (North, Central, and Southern Socio-Economic Unit project areas)",
    "legal_system": "common law (India)",
    "urban_rural": "rural",
    "service_provider": "Kerala Water Authority (KWA); Socio-Economic Units (SEU); Ward Water Committees",
    "regulatory_model": "participatory community-based site-selection process introduced alongside statutory KWA/panchayat administration",
    "population": "rural and poor/below-poverty-line households in Kerala panchayats",
    "sample_size": "73 panchayats, 11 bilateral water-supply schemes, ~1.8 million population across 3 project areas; 60+ ward committees over 8 months",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "TRUE",
    "burden": "",
    "discretion_accommodation": "TRUE",
    "enforcement": "",
    "documentation": "",
    "tenure": "",
    "property": "",
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "TRUE",
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
    "participation": "TRUE",
    "institutional_fragmentation": "",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "TRUE",
    "formal_connection": "",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "",
    "service_continuity": "",
    "application_success": "TRUE",
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
    "study_design": "program case study/process evaluation (before/after descriptive comparison of site-selection process)",
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
        "Moderate: documents that before the SEU programme, public-standpost site-selection "
        "was driven by an opaque KWA/panchayat process with criteria 'not convincing or "
        "known,' resulting in standposts poorly located relative to need; after the SEU "
        "introduced Ward Water Committees to jointly map deserving areas ('concentration of "
        "people below the poverty line'), site-selection explicitly targeted poor "
        "households, and 95% of built latrines were documented in active, well-maintained "
        "use. An institutional/participatory mechanism with a documented before/after "
        "improvement in targeting of water/sanitation provision to the poor."
    ),
    "source_document": "Kurup 1991 (retrieved via Google Drive)",
    "page": "403-414",
    "table": "",
    "figure": "",
    "section": "Location of Public Standposts and Coverage Study; Sanitation",
    "exact_location": "Paragraphs 8-9 (standpost site-selection before/after SEU); paragraphs 13-18 (sanitation pilot programme)",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: institutional/participatory-mechanism study "
        "with a documented before/after improvement in the targeting of water-access "
        "provision to the poor. Descriptive process-evaluation case study, no "
        "regression-based effect size; not added to effect_sizes.csv."
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
