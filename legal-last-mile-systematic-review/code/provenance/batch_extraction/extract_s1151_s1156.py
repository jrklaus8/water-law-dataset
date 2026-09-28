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

# S1151 -- Beall, Crankshaw & Parnell 2000, Johannesburg
r = blank_row(fieldnames)
r.update({
    "study_id": "S1151",
    "citation": "Beall J, Crankshaw O, Parnell S (2000). Victims, Villains and Fixers: The Urban Environment and Johannesburg's Poor. Journal of Southern African Studies 26(4):833-855.",
    "doi": "10.1080/713683609",
    "publication_year": "2000",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "South Africa",
    "subnational_unit": "Johannesburg (Greater Johannesburg Metropolitan Council)",
    "legal_system": "common law; post-apartheid municipal governance framework",
    "urban_rural": "urban",
    "service_provider": "Greater Johannesburg Metropolitan Council (GJMC)",
    "regulatory_model": "municipal basic-needs/pro-poor service-delivery strategy, post-apartheid",
    "population": "Johannesburg township and informal-settlement residents",
    "sample_size": "city-wide case study with sub-area (Soweto) survey comparisons",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "low-income",
    "tenure_status": "formal township housing and informal settlement",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "TRUE",
    "eligibility": "",
    "burden": "TRUE",
    "discretion_accommodation": "",
    "enforcement": "",
    "documentation": "",
    "tenure": "TRUE",
    "property": "TRUE",
    "planning": "TRUE",
    "zoning": "TRUE",
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
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "qualitative/descriptive institutional case study with survey-based access comparisons (no regression-based effect estimate)",
    "effect_estimate": (
        "Documents historical racial/housing-type determinants of water, sanitation, and "
        "electricity access disparities in Johannesburg: national post-apartheid figures showing "
        "only 21% of households had piped water and 28% sanitation access; intra-urban inequality "
        "with less than 40% of Soweto households having in-house piped water versus near-universal "
        "access in formerly white suburbs; up to 12% of informal-settlement residents dependent on "
        "non-piped water. Analyzes GJMC's basic-needs/redistributive municipal strategy as an "
        "institutional mechanism only partially addressing this inequality."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "Johannesburg, South Africa; Soweto sub-area housing-type comparison",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "qualitative/descriptive institutional case study with survey-based comparisons",
    "study_design": "qualitative institutional/legal-mechanism case study",
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
        "Moderate: documented case study linking historical racial housing-type allocation and "
        "municipal service-delivery strategy to water/sanitation access disparities, using real "
        "survey-based access figures, though descriptive rather than a designed causal-"
        "identification analysis."
    ),
    "source_document": "Beall, Crankshaw & Parnell 2000 (retrieved via Google Drive)",
    "page": "833-855",
    "table": "Table 5 (housing-type/water-access comparison)",
    "figure": "",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/administrative-mechanism study "
        "of historical racial housing-type and municipal-governance determinants of water/"
        "sanitation access inequality. Qualitative only; no effect_sizes.csv entry."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1152 -- Marra 2008, Malawi
r = blank_row(fieldnames)
r.update({
    "study_id": "S1152",
    "citation": "Marra S (2008). Bearing The Cost: An Examination Of The Gendered Impacts Of Water Policy Reform In Malawi. Rural Society 18(3):161-173.",
    "doi": "10.5172/rsj.351.18.3.161",
    "publication_year": "2008",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Malawi",
    "subnational_unit": "",
    "legal_system": "common law; post-1990s Malawian water-sector reform framework",
    "urban_rural": "mixed",
    "service_provider": "reformed (decentralized/partially privatized) water-supply system, Malawi",
    "regulatory_model": "decentralization, privatization, and user-pays water-policy reform since the mid-1990s",
    "population": "Malawian households, disaggregated by gender",
    "sample_size": "national policy-analysis case study",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "low-income",
    "tenure_status": "",
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
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "",
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
    "affordability": "TRUE",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "qualitative gender-focused policy-analysis case study (no regression-based effect estimate)",
    "effect_estimate": (
        "Analyzes Malawi's water-policy reform (decentralization, privatization, user-pays) since "
        "the mid-1990s and documents its gendered impacts: gender-blind 'community' framing in "
        "reformed policy obscures women's disproportionately constrained ability to pay user "
        "charges, with negative downstream effects on women's health, education, and empowerment "
        "even as some men begin to benefit from the reforms."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "national policy-analysis case study, Malawi",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "qualitative gender-focused policy-analysis case study",
    "study_design": "qualitative institutional/legal-mechanism case study",
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
        "Moderate: documented policy-analysis case study of a specific institutional reform "
        "(user-pays privatization) and its differential gendered effect on affordability-driven "
        "access, though descriptive/policy-analytic rather than a designed causal-identification "
        "analysis."
    ),
    "source_document": "Marra 2008 (retrieved via Google Drive)",
    "page": "161-173",
    "table": "",
    "figure": "",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/legal-mechanism study of "
        "water-policy reform's gendered effect on access/affordability. Qualitative only; no "
        "effect_sizes.csv entry."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1153 -- Das & Takahashi 2014, India
r = blank_row(fieldnames)
r.update({
    "study_id": "S1153",
    "citation": "Das P, Takahashi L (2014). Non-participation of low-income households in community-managed water supply projects in India. International Development Planning Review 36(3):267-291.",
    "doi": "10.3828/idpr.2014.16",
    "publication_year": "2014",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "three cities in central India (Bhopal, Gwalior, Jabalpur)",
    "legal_system": "common law; community-managed water-supply program framework",
    "urban_rural": "urban",
    "service_provider": "community-managed water-supply projects (donor/government-funded)",
    "regulatory_model": "mandatory community participation/labor-contribution program design",
    "population": "low-income urban households in community-managed water-project settlements",
    "sample_size": "household survey, three central Indian cities",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "low-income",
    "tenure_status": "",
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
    "effect_measure": "binary logistic regression on program-participation outcome (not a direct water-access/connection outcome; does not meet effect_sizes.csv access-outcome requirement)",
    "effect_estimate": (
        "Household survey across three central Indian cities using binary logistic regression "
        "(Prob(Participation) = a0 + a1*INCOME + a2*CASTE + a3*X) to test whether relative wealth "
        "predicts participation in, and labor contribution to, community-managed water-supply "
        "projects. Finds resource-constrained (lower-income, lower-caste) households systematically "
        "less likely to participate, identifying the community-participation program-design "
        "requirement itself as a barrier disproportionately excluding the poorest households from "
        "program benefits."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "household survey, three cities, central India",
    "adjusted_or_unadjusted": "adjusted (multivariate logistic regression, income/caste/socio-demographic covariates)",
    "covariates": "income, caste, educational attainment of household head, household size, length of residence",
    "model_type": "binary logistic regression",
    "study_design": "quantitative survey-based logistic regression",
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
        "Moderate: genuine multivariate logistic regression identifying income/caste as "
        "significant predictors of participation in a community-managed water program, but the "
        "regression's dependent variable is participation/labor-contribution, not a water-access, "
        "connection, or service outcome directly, so it does not qualify for effect_sizes.csv under "
        "this project's strict access-outcome requirement (ANALYSIS_PLAN.md S2)."
    ),
    "source_document": "Das & Takahashi 2014 (retrieved via Google Drive)",
    "page": "267-291",
    "table": "Multivariate logistic regression tables",
    "figure": "",
    "section": "Multivariate analysis",
    "exact_location": "Multivariate analysis section",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine empirical study of an administrative "
        "program-design mechanism (mandatory community participation) as a barrier to low-income "
        "household access to a water-supply program. Quantitative logistic-regression evidence "
        "exists but on a participation outcome, not a water-access outcome as this project's "
        "effect_sizes.csv strictly requires -- no effect_sizes.csv entry created; treated as "
        "qualitative-synthesis-eligible only. This distinction (participation vs. access outcome) "
        "should be revisited if ANALYSIS_PLAN.md's outcome definitions are ever broadened."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1154 -- Marumahoko, Afolabi, Sadie & Nhede 2020, Zimbabwe
r = blank_row(fieldnames)
r.update({
    "study_id": "S1154",
    "citation": "Marumahoko S, Afolabi OS, Sadie Y, Nhede NT (2020). Governance and Urban Service Delivery in Zimbabwe. Strategic Review for Southern Africa 42(1):41-63.",
    "doi": "",
    "publication_year": "2020",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Zimbabwe",
    "subnational_unit": "four urban areas, Zimbabwe",
    "legal_system": "common law; 2013 Constitution of Zimbabwe (devolution provisions)",
    "urban_rural": "urban",
    "service_provider": "urban local councils, Zimbabwe",
    "regulatory_model": "constitutional devolution of local-government functions (2013 Constitution)",
    "population": "urban residents of four Zimbabwean urban areas",
    "sample_size": "mixed-methods survey and focus-group study, four urban areas",
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
    "sanction": "",
    "participation": "",
    "institutional_fragmentation": "TRUE",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
    "formal_connection": "",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "qualitative/mixed-methods governance case study (no regression-based effect estimate)",
    "effect_estimate": (
        "Mixed-methods study (open- and closed-ended questionnaires, focus group discussions) "
        "across four Zimbabwean urban areas examining the effect of the 2013 Constitution's "
        "devolution of service functions to local government on urban water and other basic-service "
        "delivery. Finds urban service delivery, including water, has continued to decline seven "
        "years post-devolution, and attributes this primarily to national government policy "
        "constraints rather than to local-council inefficiency alone."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "four urban areas, Zimbabwe",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "qualitative/mixed-methods governance case study",
    "study_design": "qualitative institutional/legal-mechanism case study",
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
        "Moderate: mixed-methods empirical study linking a specific constitutional-devolution "
        "reform to urban water/service-delivery outcomes across four sites, though descriptive "
        "rather than a designed causal-identification analysis."
    ),
    "source_document": "Marumahoko et al. 2020 (retrieved via Google Drive)",
    "page": "41-63",
    "table": "",
    "figure": "",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/legal-mechanism study of "
        "constitutional devolution's effect on urban water/sanitation service delivery. Qualitative "
        "only; no effect_sizes.csv entry."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1155 -- Oumar & Tewari 2012, Cameroon
r = blank_row(fieldnames)
r.update({
    "study_id": "S1155",
    "citation": "Oumar SB, Tewari DD (2012). The development of water management institutions and the provision for water delivery in Cameroon: history and futures. Global Journal of Developing Areas 9(2).",
    "doi": "10.4314/gjds.v9i2.5",
    "publication_year": "2012",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Cameroon",
    "subnational_unit": "",
    "legal_system": "mixed civil/common law; Cameroonian water-institution history, pre-colonial to present",
    "urban_rural": "mixed",
    "service_provider": "national water-management institutions, Cameroon",
    "regulatory_model": "historically absent/underdeveloped water policy and water law",
    "population": "Cameroonian population (18 million)",
    "sample_size": "national historical-institutional case study",
    "household_level": "",
    "community_level": "",
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
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "qualitative historical-institutional case study using secondary data and personal observation (no regression-based effect estimate)",
    "effect_estimate": (
        "Historical-institutional analysis reconstructing the development of Cameroon's water-"
        "management institutions from the pre-colonial period to the present, using secondary "
        "sources and personal-observation data. Concludes that despite Cameroon's status as a "
        "water-surplus country (285.5 km3/year renewable supply), the absence of coherent water "
        "policy and water law, combined with piecemeal institutional development, is a primary "
        "structural cause of poor water provisioning for its 18 million residents."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "national historical case study, Cameroon",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "qualitative historical-institutional case study",
    "study_design": "qualitative institutional/legal-mechanism case study",
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
        "Low-moderate: historical-institutional narrative drawing on secondary sources and "
        "personal observation rather than a designed empirical study, but grounded in documented "
        "institutional history rather than invented claims."
    ),
    "source_document": "Oumar & Tewari 2012 (retrieved via Google Drive)",
    "page": "",
    "table": "",
    "figure": "",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/legal-mechanism history of "
        "water-policy/water-law absence as a structural cause of poor water provisioning. "
        "Qualitative only; no effect_sizes.csv entry."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1156 -- Goldman 2007, Water for All / World Bank
r = blank_row(fieldnames)
r.update({
    "study_id": "S1156",
    "citation": "Goldman M (2007). How 'Water for All!' policy became hegemonic: The power of the World Bank and its transnational policy networks. Geoforum 38(5):786-800.",
    "doi": "10.1016/j.geoforum.2005.10.008",
    "publication_year": "2007",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "South Africa (case study); global (policy-diffusion analysis)",
    "subnational_unit": "Orange Farm township, South Africa; KwaZulu-Natal (rural)",
    "legal_system": "common law; World Bank/transnational-policy-network global water-governance framework",
    "urban_rural": "mixed",
    "service_provider": "private water concessionaires (e.g. Suez) under World Bank-promoted privatization policy",
    "regulatory_model": "World Bank-driven global 'Water for All' privatization/cost-recovery policy paradigm",
    "population": "South African township and rural households affected by prepaid metering and service cutoffs",
    "sample_size": "national South African cutoff-incidence data plus Orange Farm case study",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "low-income",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "",
    "burden": "TRUE",
    "discretion_accommodation": "",
    "enforcement": "TRUE",
    "documentation": "",
    "tenure": "",
    "property": "",
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "",
    "fees": "TRUE",
    "procedural_steps": "",
    "delay": "",
    "discretion": "",
    "hardship_exception": "",
    "administrative_review": "",
    "complaint": "",
    "judicial_review": "",
    "disconnection": "TRUE",
    "reconnection": "TRUE",
    "sanction": "",
    "participation": "",
    "institutional_fragmentation": "",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
    "formal_connection": "",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "TRUE",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "qualitative political-economy case study with documented national incidence figures (no regression-based effect estimate)",
    "effect_estimate": (
        "Documents how World Bank-facilitated transnational policy networks diffused a global "
        "'Water for All' privatization/cost-recovery policy paradigm, with direct South African "
        "case evidence: a 2001 national study found more than 10 million (of 44 million) South "
        "Africans had experienced water and electricity cutoffs; a rural KwaZulu-Natal cutoff "
        "affecting 1,000 people over a $7 reconnection fee; prepaid water meters installed in "
        "Orange Farm township as a pay-as-you-go mechanism; and epidemiological linkage of these "
        "cutoffs to a national cholera outbreak infecting over 140,000 people."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "national South African cutoff data (10 million of 44 million); Orange Farm case study",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "qualitative political-economy case study",
    "study_design": "qualitative institutional/legal-mechanism case study",
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
        "Moderate: genuine documented case study connecting a specific global institutional "
        "mechanism (World Bank policy-network-driven privatization) to concrete national cutoff "
        "incidence figures and a disease-outbreak linkage, though a political-economy/documentary "
        "analysis rather than a designed causal-identification study."
    ),
    "source_document": "Goldman 2007 (retrieved via Google Drive)",
    "page": "786-800",
    "table": "",
    "figure": "",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/legal-mechanism study of "
        "global water-privatization-policy diffusion's effect on household water/electricity "
        "access. Qualitative only; no effect_sizes.csv entry."
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
