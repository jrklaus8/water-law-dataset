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

# S1074 -- Anand 2012
r = blank_row(fieldnames)
r.update({
    "study_id": "S1074",
    "citation": "Anand N (2012). Municipal disconnect: On abject water and its urban infrastructures. Ethnography 13(4):487-509.",
    "doi": "10.1177/1466138111435743",
    "publication_year": "2012",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "Premnagar, northern Mumbai suburb",
    "legal_system": "common law (India)",
    "urban_rural": "urban",
    "service_provider": "Mumbai Municipal Corporation (BMC)",
    "regulatory_model": "deliberate administrative inaction/neglect of formal municipal network extension",
    "population": "Muslim settlers in Premnagar, Mumbai",
    "sample_size": "two years of ethnographic fieldwork",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "TRUE",
    "legal_status": "TRUE",
    "indigenous_population": "",
    "migrant_population": "TRUE",
    "eligibility": "",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "",
    "documentation": "",
    "tenure": "TRUE",
    "property": "",
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "TRUE",
    "procedural_steps": "",
    "delay": "TRUE",
    "discretion": "TRUE",
    "hardship_exception": "",
    "administrative_review": "",
    "complaint": "TRUE",
    "judicial_review": "",
    "disconnection": "",
    "reconnection": "",
    "sanction": "",
    "participation": "",
    "institutional_fragmentation": "",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "service_quantity": "",
    "service_quality": "TRUE",
    "affordability": "TRUE",
    "service_continuity": "",
    "application_success": "",
    "refusal": "TRUE",
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
    "study_design": "ethnographic case study",
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
        "High: documents that Muslim settlers in Premnagar are rendered 'abject' -- "
        "denied, not merely lacking, entitlements -- through the deliberate inaction of "
        "BMC engineers and technocrats, who have left 40-year-old municipal pipes to "
        "rust and run dry without replacement, while state/federal legislators sponsor "
        "alternative bore-well construction (requiring ~$100 household connection fees "
        "plus monthly charges for water residents themselves regard as inferior/impure) "
        "rather than actually extending the municipal network into the settlement."
    ),
    "source_document": "Anand 2012 (retrieved via Google Drive)",
    "page": "487-509",
    "table": "",
    "figure": "",
    "section": "Ethnographic account of Premnagar water infrastructure",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/administrative-"
        "discrimination mechanism (deliberate municipal inaction) study with documented "
        "differential water-access outcomes for a marginalized religious/ethnic "
        "community. Ethnographic case study, no regression-based effect size; not added "
        "to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1075 -- Silvestre 2012
r = blank_row(fieldnames)
r.update({
    "study_id": "S1075",
    "citation": "Silvestre HC (2012). Public-private partnership and corporate public sector organizations: Alternative ways to increase social performance in the Portuguese water sector? Utilities Policy 22:41-49.",
    "doi": "10.1016/j.jup.2012.01.002",
    "publication_year": "2012",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Portugal",
    "subnational_unit": "national",
    "legal_system": "civil law (Portugal)",
    "urban_rural": "both",
    "service_provider": "public-private partnerships and corporate public sector water utilities, Portugal",
    "regulatory_model": "Portuguese Water Sector Regulator (ERSAR) survey framework; PPP vs. corporate public ownership",
    "population": "water-service users, Portugal",
    "sample_size": "survey data from the Portuguese Water Sector Regulator",
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
    "discretion": "",
    "hardship_exception": "",
    "administrative_review": "",
    "complaint": "",
    "judicial_review": "",
    "disconnection": "",
    "reconnection": "",
    "sanction": "",
    "participation": "",
    "institutional_fragmentation": "",
    "political_coordination": "",
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "TRUE",
    "affordability": "TRUE",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "empirical correlation/regression analysis (exact model type not extracted)",
    "effect_estimate": "User prices more strongly related to organizational costs than to ownership/property or management model; service quality more strongly related to ownership/property than to organizational costs or management model. Exact numeric coefficients not extracted from available text.",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "",
    "adjusted_or_unadjusted": "",
    "covariates": "organizational costs, property/ownership, management model",
    "model_type": "empirical regression/correlation analysis",
    "study_design": "quantitative empirical study using national regulator survey data",
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
        "Moderate: empirical analysis of Portuguese Water Sector Regulator survey data "
        "finds user prices are more strongly related to organizational costs than to "
        "ownership/property or management model, while service quality is more strongly "
        "related to ownership/property than to organizational costs or management model "
        "-- contradicting New Public Management assumptions that private-sector "
        "participation via PPPs inevitably yields lower prices and higher quality."
    ),
    "source_document": "Silvestre 2012 (retrieved via Google Drive)",
    "page": "41-49",
    "table": "",
    "figure": "",
    "section": "Empirical results on price and quality determinants",
    "exact_location": "Results section",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional-arrangement (PPP vs. "
        "corporate public ownership) comparative study with documented empirical price/"
        "quality outcomes. NOT added to effect_sizes.csv: exact numeric regression "
        "coefficients were not extractable from the available text, and the ownership/"
        "management-model variables are broad institutional-arrangement categories "
        "rather than a specific legal/institutional eligibility or barrier mechanism in "
        "the strict Family A/B/C sense."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1076 -- Valerio 2024
r = blank_row(fieldnames)
r.update({
    "study_id": "S1076",
    "citation": "Valerio AS (2024). Institutional Fragmentation and Service Performance in Decentralized Urban Water Governance: Evidence from Zamboanga City, Philippines. Lex Localis 22(S4):785-791.",
    "doi": "",
    "publication_year": "2024",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Philippines",
    "subnational_unit": "Zamboanga City",
    "legal_system": "civil law (Philippines)",
    "urban_rural": "urban",
    "service_provider": "Zamboanga City Water District (ZCWD)",
    "regulatory_model": "multi-level governance: national (LWUA, NWRB, DOH), local government (board appointments), utility",
    "population": "Zamboanga City households (~977,000 residents)",
    "sample_size": "documentary/policy analysis, 2018-2023 administrative and performance data",
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
    "administrative_review": "TRUE",
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
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "",
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
    "study_design": "mixed qualitative-quantitative institutional case study (Multi-Level Governance + IAD framework)",
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
        "High: documents persistent institutional fragmentation -- overlapping "
        "regulatory mandates across national agencies (LWUA tariff approval, NWRB water-"
        "rights allocation, DOH water-quality standards), tariff-approval timelines "
        "exceeding 12 months, and politicized water-district board appointments by the "
        "mayor -- producing stagnant service coverage (48% of households in 2022), with "
        "the majority of the remaining population relying on wells, communal sources, or "
        "vendors, arrangements that 'typically impose higher effective costs and greater "
        "quality risks on poorer households.'"
    ),
    "source_document": "Valerio 2024 (retrieved via Google Drive)",
    "page": "785-791",
    "table": "Table 1 (service indicators); Table 2 (financial performance); Table 3 (institutional roles)",
    "figure": "Figure 1 (governance framework)",
    "section": "Governance Interactions and Institutional Performance; Discussion; Conclusion",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/administrative-"
        "fragmentation mechanism study with documented differential water-access/"
        "affordability outcomes for the poor. Mixed-methods institutional case study, no "
        "regression-based effect size; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1077 -- Panda 2007
r = blank_row(fieldnames)
r.update({
    "study_id": "S1077",
    "citation": "Panda SM (2007). Mainstreaming Gender in Water Management: A Critical View. Gender, Technology and Development 11(3):321-338.",
    "doi": "10.1177/097185240701100302",
    "publication_year": "2007",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "national",
    "legal_system": "common law (India)",
    "urban_rural": "both",
    "service_provider": "water-sector reform institutions, including privatized entities",
    "regulatory_model": "water-sector reform (privatization) and gender-mainstreaming policy",
    "population": "women water users and managers, India",
    "sample_size": "critical policy analysis (SEWA 'Women, Water and Work' campaign as case example)",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "",
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
    "property": "TRUE",
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "",
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
    "bureaucratic_assistance": "",
    "formal_connection": "",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "",
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
    "study_design": "critical policy-analysis essay with case examples",
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
        "Moderate: critically examines how gender-mainstreaming rhetoric in Indian water "
        "management diverges from effective practice, analyzing SEWA's 'Women, Water and "
        "Work' campaign (which by and large excluded men) alongside water-sector reforms "
        "including privatization that marginalize women in decision-making processes, "
        "arguing that effective gender mainstreaming requires transformation of gender "
        "relations and treatment of water as a human right."
    ),
    "source_document": "Panda 2007 (retrieved via Google Drive)",
    "page": "321-338",
    "table": "",
    "figure": "",
    "section": "Analysis of SEWA campaign and water-sector reform gender impacts",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: critical institutional/policy analysis "
        "directly examining how specific water-sector reform mechanisms (privatization, "
        "gender-mainstreaming implementation) differentially affect women's water-"
        "management roles and access. Critical essay with case examples, no regression-"
        "based effect size; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1078 -- Eguavoen 2008
r = blank_row(fieldnames)
r.update({
    "study_id": "S1078",
    "citation": "Eguavoen I (2008). Changing Household Water Rights in Rural Northern Ghana. Development 51(1):126-129.",
    "doi": "10.1057/palgrave.development.1100462",
    "publication_year": "2008",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Ghana",
    "subnational_unit": "Upper East Region, Nankani settlement",
    "legal_system": "common law with customary law (Ghana)",
    "urban_rural": "rural",
    "service_provider": "Community Water and Sanitation Agency (CWSA); pump communities/water user committees",
    "regulatory_model": "National Community Water and Sanitation Program (NCWSP) community-based management policy",
    "population": "rural households, Upper East Region, Ghana",
    "sample_size": "fieldwork 2004-2006",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "TRUE",
    "indigenous_population": "",
    "migrant_population": "TRUE",
    "eligibility": "TRUE",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "TRUE",
    "documentation": "TRUE",
    "tenure": "TRUE",
    "property": "TRUE",
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "TRUE",
    "procedural_steps": "TRUE",
    "delay": "TRUE",
    "discretion": "TRUE",
    "hardship_exception": "TRUE",
    "administrative_review": "",
    "complaint": "",
    "judicial_review": "",
    "disconnection": "",
    "reconnection": "",
    "sanction": "",
    "participation": "TRUE",
    "institutional_fragmentation": "TRUE",
    "political_coordination": "",
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "TRUE",
    "service_reliability": "",
    "service_quantity": "TRUE",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "",
    "application_success": "TRUE",
    "refusal": "TRUE",
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
    "study_design": "qualitative institutional/legal case study (fieldwork)",
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
        "High: documents that Ghana's NCWSP formal community-based management policy -- "
        "with formal registration/membership, a 5% community-contribution capital-cost "
        "fee (~US$210), and water-user committees -- replaced pre-existing customary "
        "equal-use water rights (open to all community members without institutional "
        "exclusion) with a system that formally excludes non-members; non-resident "
        "farmers are formally excluded from pump use despite customary rights; some "
        "households failed to qualify for years because they could not raise the "
        "required community contribution; a hierarchy of restricted use rights was "
        "imposed for non-members. The policy increased physical but not institutional "
        "access, with use rights becoming 'more regulated and more restricted.'"
    ),
    "source_document": "Eguavoen 2008 (retrieved via Google Drive)",
    "page": "126-129",
    "table": "",
    "figure": "",
    "section": "Water programmes in northern Ghana; Conclusion",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous legal/institutional mechanism "
        "study documenting how a formal community-based management policy directly "
        "restricted and formalized exclusion from water access that had previously been "
        "open under customary law. Qualitative case study, no regression-based effect "
        "size; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1079 -- Antunes & Martins 2020
r = blank_row(fieldnames)
r.update({
    "study_id": "S1079",
    "citation": "Antunes M, Martins R (2020). Determinants of access to improved water sources: Meeting the MDGs. Utilities Policy 63:101019.",
    "doi": "10.1016/j.jup.2020.101019",
    "publication_year": "2020",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "multi-country (111 countries)",
    "subnational_unit": "national",
    "legal_system": "mixed (multi-country)",
    "urban_rural": "both",
    "service_provider": "national water-sector institutions",
    "regulatory_model": "human right to water (UN Resolution 64/292, 2010); MDG/SDG policy framework",
    "population": "national populations, 111 countries with <95% coverage",
    "sample_size": "111 countries, 1991-2015 panel (1,453 observations)",
    "household_level": "",
    "community_level": "",
    "income_group": "TRUE",
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
    "service_area": "",
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
    "institutional_fragmentation": "",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
    "formal_connection": "",
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
    "effect_measure": "fixed-effects panel regression coefficients (Driscoll-Kraay corrected)",
    "effect_estimate": "Gross capital formation (investment): +0.0490, t=3.886, p<0.01. Agricultural value-added share: -0.1055, t=-3.988, p<0.01. Vulnerable female employment share: -0.1056, t=-3.244, p<0.01 (1 p.p. increase associated with ~0.11 p.p. decrease in water-access coverage). Primary-school gross enrollment: +0.0620, t=6.190, p<0.01. Urban population share: +0.8647, t=9.239, p<0.01. Political stability change: +0.0097, not significant.",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "<0.01 for gcf, agr_va, vuln_empl_fem, enrol_prim_gross, urban_pop; not significant for pol_stab",
    "extraction_sample_size": "111 countries, 1,453 observations",
    "adjusted_or_unadjusted": "adjusted (fixed effects, Driscoll-Kraay standard errors)",
    "covariates": "gross capital formation, agricultural value-added share, vulnerable female employment share, primary enrollment, urban population share, political stability, MDG-period interaction terms by region",
    "model_type": "fixed-effects panel regression with Driscoll-Kraay correction",
    "study_design": "quantitative cross-national panel regression study",
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
        "Moderate: rigorous cross-national fixed-effects panel regression (111 countries, "
        "1991-2015) finds infrastructure investment, primary education enrollment, and "
        "urbanization positively predict access to improved water sources, while "
        "agricultural-sector economic concentration and vulnerable female employment "
        "negatively predict it -- documenting broad socioeconomic/structural determinants "
        "of national water-access coverage rather than isolating a single specific legal/"
        "institutional eligibility or barrier mechanism."
    ),
    "source_document": "Antunes & Martins 2020 (retrieved via Google Drive)",
    "page": "",
    "table": "Table 4 (estimation results)",
    "figure": "",
    "section": "Results",
    "exact_location": "Table 4 and accompanying discussion",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous cross-national panel-regression "
        "study of water-access determinants. NOT added to effect_sizes.csv: the "
        "significant predictors (investment share, agricultural value-added share, "
        "vulnerable female employment, education, urbanization) are broad socioeconomic/"
        "structural circumstance variables, not a single specific legal/institutional "
        "eligibility or barrier mechanism (fees, tenure, permits) isolated per the strict "
        "Family A/B/C framework, following the reasoning applied to Jemmali & Amara 2015 "
        "(S1065, Batch 215) and Motiram & Osberg 2010 (S1056, Batch 213)."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1080 -- Crook & Ayee 2006
r = blank_row(fieldnames)
r.update({
    "study_id": "S1080",
    "citation": "Crook R, Ayee J (2006). Urban Service Partnerships, 'Street-Level Bureaucrats' and Environmental Sanitation in Kumasi and Accra, Ghana: Coping with Organisational Change in the Public Bureaucracy. Development Policy Review 24(1):51-73.",
    "doi": "10.1111/j.1467-7679.2006.00313.x",
    "publication_year": "2006",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Ghana",
    "subnational_unit": "Kumasi; Accra",
    "legal_system": "common law (Ghana)",
    "urban_rural": "urban",
    "service_provider": "Environmental Health Department; privatized/contracted sanitation providers",
    "regulatory_model": "privatization and contracting-out of environmental sanitation services",
    "population": "urban residents, Kumasi and Accra",
    "sample_size": "empirical case study of street-level regulatory officials",
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
    "discretion": "TRUE",
    "hardship_exception": "",
    "administrative_review": "",
    "complaint": "",
    "judicial_review": "",
    "disconnection": "",
    "reconnection": "",
    "sanction": "TRUE",
    "participation": "",
    "institutional_fragmentation": "TRUE",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
    "formal_connection": "",
    "water_access": "",
    "sanitation_access": "TRUE",
    "service_coverage": "",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "TRUE",
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
    "study_design": "empirical case study of regulatory street-level bureaucrats",
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
        "Moderate: examines how privatization and contracting-out of environmental "
        "sanitation services in Kumasi and Accra imposed new client-oriented working "
        "practices on Environmental Health Officers, finding that while officers' "
        "positive organizational culture aided adaptation, 'politically protected "
        "privatisations' undermined their ability to enforce sanitary standards, "
        "compounded by deficiencies in training and incentive structures."
    ),
    "source_document": "Crook & Ayee 2006 (retrieved via Google Drive)",
    "page": "51-73",
    "table": "",
    "figure": "",
    "section": "Analysis of Environmental Health Officers' organizational adaptation",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/administrative-"
        "enforcement mechanism study documenting how privatization reform undermined "
        "regulatory enforcement capacity for environmental sanitation. Empirical case "
        "study, no regression-based effect size; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1081 -- Alam et al 2020
r = blank_row(fieldnames)
r.update({
    "study_id": "S1081",
    "citation": "Alam MU, Sharior F, Ferdous S, Ahsan A, Ahmed T, Afrin A, Sarker S, Akand F, Archie RJ, Hasan K, Renouf R, Drabble S, Norman G, Rahman M, Tidwell JB (2020). Strategies to Connect Low-Income Communities with the Proposed Sewerage Network of the Dhaka Sanitation Improvement Project, Bangladesh: A Qualitative Assessment of the Perspectives of Stakeholders. International Journal of Environmental Research and Public Health 17(19):7201.",
    "doi": "10.3390/ijerph17197201",
    "publication_year": "2020",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Bangladesh",
    "subnational_unit": "Dhaka",
    "legal_system": "common law (Bangladesh)",
    "urban_rural": "urban",
    "service_provider": "Dhaka Water Supply and Sewerage Authority (DWASA)",
    "regulatory_model": "Dhaka Sanitation Improvement Project (DSIP) sewerage network connection policy",
    "population": "low-income communities (LICs) near the proposed DSIP catchment area",
    "sample_size": "9 key-informant interviews (DWASA, City Corporation); 23 focus-group discussions across 16 LICs",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "TRUE",
    "legal_status": "",
    "indigenous_population": "",
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
    "procedural_steps": "TRUE",
    "delay": "",
    "discretion": "TRUE",
    "hardship_exception": "TRUE",
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
    "formal_connection": "TRUE",
    "water_access": "",
    "sanitation_access": "TRUE",
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
    "extraction_sample_size": "16 low-income communities",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "qualitative assessment (key-informant interviews, focus-group discussions)",
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
        "Moderate: identifies institutional/infrastructural barriers to formal sewerage-"
        "network connection for low-income communities in Dhaka -- requirement of "
        "improved toilet infrastructure and road access to the main network, need for "
        "communal septic tanks where individual connections are infeasible -- and "
        "stakeholder-recommended solutions including income-based or area-based "
        "connection subsidies and per-household or divided fee models for maintenance "
        "financing."
    ),
    "source_document": "Alam et al. 2020 (retrieved via Google Drive)",
    "page": "",
    "table": "",
    "figure": "",
    "section": "Findings on connection requirements and financing strategies for LICs",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/administrative-"
        "mechanism study directly examining barriers to formal sanitation-service "
        "connection for low-income urban communities. Qualitative assessment, no "
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
