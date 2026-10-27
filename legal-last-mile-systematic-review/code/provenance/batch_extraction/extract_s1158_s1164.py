#!/usr/bin/env python3
import csv, tempfile, os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/03_extraction/extracted_data/extraction_database.csv"
RESEARCHER = "Claude-AI-fulltext-2026-09-28"
DATE = "2026-09-28"


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

# S1158 -- Behnke et al 2020, displacement WASH scoping review
r = blank_row(fieldnames)
r.update({
    "study_id": "S1158",
    "citation": "Behnke NL, Cronk R, Shackelford BB, Cooper B, Tu R, Heller L, Bartram J (2020). Environmental health conditions in protracted displacement: A systematic scoping review. Science of the Total Environment 726:138234.",
    "doi": "10.1016/j.scitotenv.2020.138234",
    "publication_year": "2020",
    "publication_type": "journal article (systematic scoping review)",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "multiple (global scoping review)",
    "subnational_unit": "",
    "legal_system": "mixed (global review)",
    "urban_rural": "mixed",
    "service_provider": "varies by displacement setting",
    "regulatory_model": "humanitarian/institutional response frameworks in protracted displacement",
    "population": "populations in protracted displacement",
    "sample_size": "213 studies (systematic scoping review)",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "",
    "tenure_status": "displaced/informal",
    "legal_status": "TRUE",
    "indigenous_population": "",
    "migrant_population": "TRUE",
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
    "fees": "",
    "procedural_steps": "",
    "delay": "",
    "discretion": "",
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
    "formal_connection": "",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "systematic scoping review synthesis (no single regression-based effect estimate)",
    "effect_estimate": (
        "Systematic scoping review of 213 studies on environmental-health (including WASH) "
        "conditions among populations in protracted displacement. Identifies institutional and "
        "political factors as the most frequently cited barriers to environmental-health service "
        "access, including water/sanitation, across displacement settings globally."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "213 studies (scoping review)",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "systematic scoping review",
    "study_design": "qualitative evidence synthesis",
    "risk_of_bias_tool": "CASP Qualitative Checklist",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "",
    "attrition": "",
    "reporting_bias": "",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": (
        "Moderate: a systematic scoping review synthesizing a large body of literature on "
        "institutional/political barriers to WASH/environmental-health access in displacement, "
        "but a review rather than a single designed causal-identification study."
    ),
    "source_document": "Behnke et al. 2020 (retrieved via Google Drive)",
    "page": "",
    "table": "",
    "figure": "",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine systematic evidence synthesis of "
        "institutional/political barriers to water/sanitation access among displaced "
        "populations. Qualitative only; no effect_sizes.csv entry."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1159 -- de Lima et al 2026, ESG strategies Brazil sanitation utilities
r = blank_row(fieldnames)
r.update({
    "study_id": "S1159",
    "citation": "de Lima MDS, Silva WDO, Neto MM, Fontana ME, Silva AEA (2026). Expert group decision-making on ESG strategies for water public sanitation utilities under fiscal and budgetary constraints in Brazil.",
    "doi": "",
    "publication_year": "2026",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Brazil",
    "subnational_unit": "Maceio",
    "legal_system": "civil law; Brazilian sanitation-utility governance framework",
    "urban_rural": "urban",
    "service_provider": "public sanitation utility, Maceio, Brazil",
    "regulatory_model": "ESG (environmental/social/governance) strategy framework under fiscal/budgetary constraint",
    "population": "sanitation-utility stakeholders (researchers, utility staff, service users)",
    "sample_size": "expert group (Nominal Group Technique)",
    "household_level": "",
    "community_level": "TRUE",
    "income_group": "",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "",
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
    "institutional_fragmentation": "",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
    "formal_connection": "",
    "sanitation_access": "TRUE",
    "water_access": "",
    "service_coverage": "",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "qualitative expert-elicitation study (Nominal Group Technique; no regression-based effect estimate)",
    "effect_estimate": (
        "Uses Nominal Group Technique with researchers, utility staff, and service users in "
        "Maceio, Brazil, to identify ESG (environmental/social/governance) strategies for a "
        "public sanitation utility operating under fiscal and budgetary constraints, addressing "
        "institutional/governance mechanisms affecting sanitation-service delivery."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "expert group, Maceio sanitation utility, Brazil",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "qualitative expert-elicitation study",
    "study_design": "qualitative institutional/governance case study",
    "risk_of_bias_tool": "CASP Qualitative Checklist",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "",
    "attrition": "",
    "reporting_bias": "",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": (
        "Moderate: genuine expert-elicitation study of institutional/fiscal governance "
        "strategies for sanitation-service delivery, though qualitative/consultative rather "
        "than a designed causal-identification analysis."
    ),
    "source_document": "de Lima et al. 2026 (retrieved via Google Drive)",
    "page": "",
    "table": "",
    "figure": "",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/governance/fiscal-policy "
        "study of sanitation-utility service delivery. Qualitative only; no effect_sizes.csv "
        "entry."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1160 -- Ananga 2015, Kisumu community participation dissertation
r = blank_row(fieldnames)
r.update({
    "study_id": "S1160",
    "citation": "Ananga EO (2015). The Role of Community Participation in Water Production and Management: Lessons From Sustainable Aid in Africa International Sponsored Water Schemes in Kisumu, Kenya. PhD dissertation, University of South Florida.",
    "doi": "",
    "publication_year": "2015",
    "publication_type": "dissertation",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "FALSE",
    "country": "Kenya",
    "subnational_unit": "Kisumu",
    "legal_system": "common law; NGO-sponsored community water-scheme governance",
    "urban_rural": "urban informal settlement",
    "service_provider": "NGO-sponsored (Sustainable Aid in Africa International) community water schemes",
    "regulatory_model": "community water-management-committee governance model",
    "population": "households served by four NGO-sponsored water/sanitation schemes",
    "sample_size": "household survey plus focus group discussions, four schemes",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "low-income",
    "tenure_status": "informal settlement",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "",
    "burden": "TRUE",
    "discretion_accommodation": "",
    "enforcement": "",
    "documentation": "",
    "tenure": "",
    "property": "",
    "planning": "",
    "zoning": "",
    "building_permit": "",
    "service_area": "",
    "fees": "",
    "procedural_steps": "",
    "delay": "",
    "discretion": "",
    "hardship_exception": "",
    "administrative_review": "",
    "complaint": "TRUE",
    "judicial_review": "",
    "disconnection": "",
    "reconnection": "",
    "sanction": "",
    "participation": "TRUE",
    "institutional_fragmentation": "",
    "political_coordination": "",
    "bureaucratic_assistance": "TRUE",
    "formal_connection": "",
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
    "effect_measure": "logistic regression and chi-square tests on a participation/satisfaction outcome (not a water-access outcome; does not meet effect_sizes.csv access-outcome requirement)",
    "effect_estimate": (
        "Mixed-methods study of four NGO-sponsored water/sanitation schemes in Kisumu informal "
        "settlements. Logistic regression and chi-square tests on household survey data examine "
        "whether community-participation variables (labor contribution, meeting attendance, "
        "complaint behavior) predict beneficiary satisfaction with water-management committees "
        "and water-handling hygiene practices, supplemented by qualitative focus-group data on "
        "institutional/participatory factors affecting scheme performance."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "four NGO-sponsored water schemes, Kisumu, Kenya",
    "adjusted_or_unadjusted": "adjusted (logistic regression)",
    "covariates": "labor contribution, meeting attendance, complaint behavior",
    "model_type": "logistic regression and chi-square tests",
    "study_design": "quantitative survey-based logistic regression plus qualitative FGDs",
    "risk_of_bias_tool": "MMAT",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "",
    "attrition": "",
    "reporting_bias": "",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": (
        "Moderate: genuine mixed-methods study of a participatory community-management "
        "mechanism, but the regression's outcome is participation-linked satisfaction/hygiene "
        "behavior, not a water-access, connection, or service outcome directly, so it does not "
        "qualify for effect_sizes.csv under this project's strict access-outcome requirement "
        "(same treatment as S1153, Das & Takahashi, Batch 236)."
    ),
    "source_document": "Ananga 2015 (retrieved via Google Drive)",
    "page": "",
    "table": "",
    "figure": "",
    "section": "Results/Discussion",
    "exact_location": "Results/Discussion",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/participatory-governance "
        "study of community water-scheme management. Quantitative regression exists but on a "
        "participation/satisfaction outcome, not a water-access outcome -- no effect_sizes.csv "
        "entry; treated as qualitative-synthesis-eligible only."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1161 -- Ikeda 2024, Florianopolis dam-rupture governance case study
r = blank_row(fieldnames)
r.update({
    "study_id": "S1161",
    "citation": "Ikeda VY (2024). (Des) governanca da agua e desastre: um estudo de caso sobre o rompimento da barragem da Lagoa da Conceicao em Florianopolis. Master's dissertation, Universidade do Estado de Santa Catarina.",
    "doi": "",
    "publication_year": "2024",
    "publication_type": "dissertation",
    "language": "Portuguese",
    "database_source": "",
    "peer_reviewed": "FALSE",
    "country": "Brazil",
    "subnational_unit": "Florianopolis",
    "legal_system": "civil law; Brazilian environmental/sanitation regulatory framework",
    "urban_rural": "urban",
    "service_provider": "CASAN (state sanitation utility); Civil Defense; environmental regulators",
    "regulatory_model": "institutional/adaptive water-governance framework, disaster response",
    "population": "Florianopolis residents affected by the 2021 dam-rupture disaster",
    "sample_size": "qualitative case study (document analysis + 2 interviews)",
    "household_level": "",
    "community_level": "TRUE",
    "income_group": "",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "",
    "burden": "",
    "discretion_accommodation": "",
    "enforcement": "TRUE",
    "documentation": "",
    "tenure": "",
    "property": "",
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "",
    "procedural_steps": "",
    "delay": "",
    "discretion": "",
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
    "formal_connection": "",
    "water_access": "",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "",
    "service_continuity": "TRUE",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "qualitative case study (document analysis and interviews; no regression-based effect estimate)",
    "effect_estimate": (
        "Qualitative case study reconstructing institutional/regulatory failure surrounding the "
        "2021 sewage-dam-rupture disaster in Florianopolis, documenting that only 65.71% of the "
        "city had sanitation-service access, and analyzing interaction (and breakdown) among "
        "public agencies (CASAN, Civil Defense, environmental regulators) and civil society "
        "through institutional/adaptive water-governance theory."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "Florianopolis, Brazil, single disaster case study",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "qualitative case study",
    "study_design": "qualitative institutional/regulatory-mechanism case study",
    "risk_of_bias_tool": "CASP Qualitative Checklist",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "",
    "attrition": "",
    "reporting_bias": "",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": (
        "Moderate: genuine institutional case study of regulatory/governance failure in a "
        "disaster context affecting sanitation access, though a single-case qualitative "
        "analysis rather than a designed causal-identification study."
    ),
    "source_document": "Ikeda 2024 (retrieved via Google Drive)",
    "page": "",
    "table": "",
    "figure": "",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/regulatory-mechanism study "
        "of sanitation-service access failure in a disaster-governance context. Qualitative "
        "only; no effect_sizes.csv entry."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1162 -- Subramanyam 2020, India multilevel water-coverage regression
r = blank_row(fieldnames)
r.update({
    "study_id": "S1162",
    "citation": "Subramanyam N (2020). A small improvement: small cities lag in expanding household water coverage across urban India. Water Policy 22(3):468-482.",
    "doi": "10.2166/wp.2020.116",
    "publication_year": "2020",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "3,547 urban local governments across 21 states",
    "legal_system": "common law; Indian municipal-governance category system (municipal corporation / municipality / town panchayat)",
    "urban_rural": "urban",
    "service_provider": "urban local governments, India",
    "regulatory_model": "multilevel urban-governance framework; local-government administrative category",
    "population": "urban households, India",
    "sample_size": "3,547 cities/towns nested within 21 states",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "",
    "burden": "",
    "discretion_accommodation": "",
    "enforcement": "",
    "documentation": "",
    "tenure": "",
    "property": "",
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "",
    "procedural_steps": "",
    "delay": "",
    "discretion": "",
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
    "bureaucratic_assistance": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "TRUE",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "regression coefficient (percentage-point difference in water-coverage growth)",
    "effect_estimate": "-4.062 (municipality vs. municipal corporation, reference category); -4.034 (town panchayat and others vs. municipal corporation)",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "1.254 (municipality); 1.540 (town panchayat)",
    "p_value": "<0.01 (both)",
    "extraction_sample_size": "3,547 cities/towns, 21 states, India, 2001-2011",
    "adjusted_or_unadjusted": "adjusted (multilevel linear regression, controlling for population, population growth, initial coverage, density, distance to metro, intergovernmental aid, state income, urbanization, decentralization index)",
    "covariates": "ln(population), population growth rate, initial water coverage (2001), distance to nearest metro, ln(population density), intergovernmental aid, state urban population share, state income, decentralization index",
    "model_type": "multilevel (hierarchical) linear regression",
    "study_design": "quantitative panel/cross-sectional multilevel regression",
    "risk_of_bias_tool": "RoB 2",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "",
    "attrition": "",
    "reporting_bias": "",
    "legal_measurement_quality": "2",
    "outcome_measurement_quality": "2",
    "mechanism_certainty": (
        "High: a large-N (3,547 cities), multilevel regression directly isolating local-"
        "government administrative-category effects on household water-coverage growth, "
        "controlling for a substantial set of city- and state-level confounders. A genuine "
        "institutional/administrative-mechanism effect estimate on a water-access outcome."
    ),
    "source_document": "Subramanyam 2020 (retrieved via Google Drive)",
    "page": "468-482",
    "table": "Table 3, Table 4 (multilevel regression model results)",
    "figure": "",
    "section": "Results and discussion",
    "exact_location": "Results and discussion, Table 4",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine, well-identified institutional/"
        "administrative-mechanism study of local-government category's effect on household "
        "water-coverage growth across a large sample of Indian cities. Added to "
        "effect_sizes.csv as Family C (administrative-capacity/access inequality across "
        "local-government categories)."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1163 -- Cronk et al 2021, 14-LMIC rural schools WASH regression
r = blank_row(fieldnames)
r.update({
    "study_id": "S1163",
    "citation": "Cronk R, Guo A, Fleming L, Bartram J (2021). Factors associated with water quality, sanitation, and hygiene in rural schools in 14 low- and middle-income countries. Science of the Total Environment 761:144226.",
    "doi": "10.1016/j.scitotenv.2020.144226",
    "publication_year": "2021",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "multiple (14 low- and middle-income countries)",
    "subnational_unit": "13 countries surveyed (subnational districts within each)",
    "legal_system": "mixed (multi-country study)",
    "urban_rural": "rural",
    "service_provider": "rural schools, 14 LMICs",
    "regulatory_model": "external WaSH-program funding/support; parent-teacher-association (PTA) governance",
    "population": "rural schoolchildren, 14 LMICs",
    "sample_size": "2,677 schools, 13 countries surveyed",
    "household_level": "",
    "community_level": "TRUE",
    "income_group": "low-income",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "",
    "burden": "",
    "discretion_accommodation": "",
    "enforcement": "",
    "documentation": "",
    "tenure": "",
    "property": "",
    "planning": "",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "",
    "procedural_steps": "",
    "delay": "",
    "discretion": "",
    "hardship_exception": "",
    "administrative_review": "",
    "complaint": "",
    "judicial_review": "",
    "disconnection": "",
    "reconnection": "",
    "sanction": "",
    "participation": "TRUE",
    "institutional_fragmentation": "",
    "political_coordination": "",
    "bureaucratic_assistance": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "",
    "service_reliability": "TRUE",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "",
    "service_continuity": "TRUE",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "odds ratio",
    "effect_estimate": "1.4",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "0.021",
    "extraction_sample_size": "2,677 schools, 13 countries",
    "adjusted_or_unadjusted": "adjusted (multilevel mixed-effects logistic regression)",
    "covariates": "school enrollment size, pre-primary status, water accessibility to youngest children, shared water source with community, PTA presence, number of water points, country",
    "model_type": "multilevel mixed-effects logistic regression",
    "study_design": "quantitative cross-sectional multilevel regression",
    "risk_of_bias_tool": "RoB 2",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "",
    "attrition": "",
    "reporting_bias": "",
    "legal_measurement_quality": "2",
    "outcome_measurement_quality": "2",
    "mechanism_certainty": (
        "High: a large-N (2,677 schools, 13 countries), multilevel regression directly "
        "isolating the effect of external WaSH-program funding/support (an institutional/"
        "administrative-assistance mechanism) on school-level basic on-premises water-service "
        "access, controlling for school and country-level confounders. Also finds absence of a "
        "parent-teacher association (participatory-governance mechanism) significantly "
        "predicts lower water-service access (OR=0.6, p=0.001), a second candidate institutional "
        "mechanism from the same model not separately extracted as an effect_sizes.csv row."
    ),
    "source_document": "Cronk et al. 2021 (retrieved via Google Drive)",
    "page": "",
    "table": "Table 3 (multilevel logistic regression, water-service outcome)",
    "figure": "",
    "section": "Results, 3.1 Basic water services",
    "exact_location": "Results, 3.1 Basic water services, Table 3",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine, well-identified institutional/"
        "administrative-assistance-mechanism study of external WaSH-program funding's effect "
        "on school-level water-service access. Added to effect_sizes.csv as Family B "
        "(administrative assistance/access), using the externally-funded-WaSH-program OR. Unit "
        "of analysis is school, not household -- recorded explicitly per REPRODUCIBILITY.md "
        "scope-discipline reminder against conflating units of analysis."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1164 -- Kurian & McCarney eds 2010, peri-urban WSS edited volume
r = blank_row(fieldnames)
r.update({
    "study_id": "S1164",
    "citation": "Kurian M, McCarney P (eds.) (2010). Peri-urban Water and Sanitation Services: Policy, Planning and Method. Dordrecht: Springer.",
    "doi": "",
    "publication_year": "2010",
    "publication_type": "edited book (comparative case studies)",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "multiple (Africa, Asia, South America, Netherlands)",
    "subnational_unit": "multiple peri-urban case-study sites",
    "legal_system": "mixed (multi-country comparative volume)",
    "urban_rural": "peri-urban",
    "service_provider": "varies by case study",
    "regulatory_model": "peri-urban water/sanitation governance arrangements (comparative)",
    "population": "peri-urban residents, multiple countries",
    "sample_size": "edited volume of comparative case studies",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "",
    "burden": "",
    "discretion_accommodation": "",
    "enforcement": "",
    "documentation": "",
    "tenure": "",
    "property": "",
    "planning": "TRUE",
    "zoning": "TRUE",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "",
    "procedural_steps": "",
    "delay": "",
    "discretion": "",
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
    "formal_connection": "",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "edited volume of qualitative comparative case studies (no single regression-based effect estimate)",
    "effect_estimate": (
        "Edited volume presenting comparative institutional/governance case studies of "
        "peri-urban water and sanitation service-delivery arrangements across Africa, Asia, "
        "South America, and the Netherlands, examining policy, planning, and methodological "
        "approaches to peri-urban service governance."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "multi-country edited comparative case-study volume",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "edited comparative case-study volume",
    "study_design": "qualitative comparative case-study collection",
    "risk_of_bias_tool": "CASP Qualitative Checklist",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "",
    "attrition": "",
    "reporting_bias": "",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": (
        "Moderate: a genuine, substantial comparative institutional case-study collection on "
        "peri-urban water/sanitation governance, though an edited volume rather than a single "
        "designed empirical study."
    ),
    "source_document": "Kurian & McCarney (eds.) 2010 (retrieved via Google Drive)",
    "page": "",
    "table": "",
    "figure": "",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/governance-focused "
        "comparative case-study volume on peri-urban water/sanitation service delivery. "
        "Qualitative only; no effect_sizes.csv entry (edited multi-case volume, not a single "
        "regression)."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

for r in new_rows:
    assert r["study_id"] not in existing_ids, r["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"extraction_database.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
