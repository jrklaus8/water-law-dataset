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

# S1053 -- Sahu 2008
r = blank_row(fieldnames)
r.update({
    "study_id": "S1053",
    "citation": "Sahu BK (2008). Pani Panchayat in Orissa, India: The practice of participatory water management. Development 51(1):121-125.",
    "doi": "10.1057/palgrave.development.1100448",
    "publication_year": "2008",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "Nabarangpur and Jagatsinghpur districts, Orissa",
    "legal_system": "common law (India)",
    "urban_rural": "rural",
    "service_provider": "Pani Panchayat (PP) / Water User Associations (WUAs), statutory bodies under Orissa PP Act 2002",
    "regulatory_model": "Orissa Pani Panchayat Act 2002 and Orissa PP Rules 2003, transferring irrigation O&M from government to farmer WUAs",
    "population": "115 households (29% marginal, 41% small, 30% medium/large) across 4 villages",
    "sample_size": "115 households, 4 villages, 2 districts",
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
    "formal_connection": "",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "",
    "service_reliability": "",
    "service_quantity": "TRUE",
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
    "study_design": "qualitative case study (interviews and participatory research, 115 households, 4 villages)",
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
        "High: documents that under the statutory Pani Panchayat framework, the right to "
        "receive irrigation water is conditional on payment of WUA user fees and state water "
        "tax, so 'access to water depends on paying capacity of the users'; marginal farmers "
        "and landless cultivators who cannot afford operating-expense contributions 'would "
        "not get any of the benefits and hence get excluded from part of the state's capital "
        "spending on irrigation infrastructure,' while dominant/elite members capture "
        "disproportionate benefit and management control -- 'Under this situation PP "
        "excludes marginal groups.'"
    ),
    "source_document": "Sahu 2008 (retrieved via Google Drive)",
    "page": "121-125",
    "table": "",
    "figure": "",
    "section": "The impact of PP in different regions; Assessment of PP",
    "exact_location": "Throughout, especially the Assessment of PP section on exclusion of marginal groups",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine legal/institutional mechanism "
        "(statutory WUA fee-based access, ill-defined property rights) with documented "
        "differential access-exclusion outcomes for marginal and landless households. "
        "Qualitative case study, no regression-based effect size; not added to "
        "effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1054 -- Jacobs 1978
r = blank_row(fieldnames)
r.update({
    "study_id": "S1054",
    "citation": "Jacobs SE (1978). \"Top-Down Planning\": Analysis of Obstacles to Community Development in an Economically Poor Region of the Southwestern United States. Human Organization 37(3):246-256.",
    "doi": "",
    "publication_year": "1978",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "United States",
    "subnational_unit": "Espanola Valley, New Mexico",
    "legal_system": "common law (US), with treaty-protected traditional/customary water rights",
    "urban_rural": "rural",
    "service_provider": "acequia system (community irrigation ditches) governed by elected mayordomos; US Bureau of Reclamation; State Engineer",
    "regulatory_model": "traditional acequia water-rights institution (protected by the Treaty of Guadalupe Hidalgo 1848) vs. proposed state water-rights adjudication",
    "population": "Chicano/Hispanic farming communities along nine ditch areas, Espanola Valley",
    "sample_size": "Social Impact Assessment fieldwork, 1975",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "",
    "tenure_status": "TRUE",
    "legal_status": "TRUE",
    "indigenous_population": "TRUE",
    "migrant_population": "",
    "eligibility": "",
    "burden": "",
    "discretion_accommodation": "TRUE",
    "enforcement": "TRUE",
    "documentation": "TRUE",
    "tenure": "TRUE",
    "property": "TRUE",
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
    "sanitation_access": "",
    "service_coverage": "",
    "service_reliability": "",
    "service_quantity": "TRUE",
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
    "study_design": "qualitative case study (Social Impact Assessment fieldwork, community records, interviews)",
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
        "High: documents that top-down federal/state development planning (Bureau of "
        "Reclamation's Llano Unit project) recommended adjudication of water rights in the "
        "Espanola Valley that would extinguish some farmers' inherited traditional water "
        "rights obtained through the acequia (ditch) system and dissolve the acequia's "
        "dual role as water-management and local-governance institution, despite the "
        "acequia system's protection under the Treaty of Guadalupe Hidalgo (1848) "
        "guaranteeing land grants and water rights to descendants of Spanish settlers and "
        "Indian Pueblos."
    ),
    "source_document": "Jacobs 1978 (retrieved via Google Drive)",
    "page": "246-256",
    "table": "",
    "figure": "",
    "section": "Indigenous Water System",
    "exact_location": "Discussion of water-rights adjudication threat to the acequia system",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine legal/institutional mechanism "
        "(water-rights adjudication vs. treaty-protected traditional water-governance "
        "institution) study documenting the threatened loss of water access/rights for a "
        "specific marginalized community. Qualitative case study, no regression-based "
        "effect size; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1055 -- Menon 2013
r = blank_row(fieldnames)
r.update({
    "study_id": "S1055",
    "citation": "Menon GA (2013). Citizens and 'Squatters': The Contested Subject of Public Policy in Neoliberal Mumbai. Ethics and Social Welfare 7(2):155-169.",
    "doi": "10.1080/17496535.2013.779007",
    "publication_year": "2013",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "Mumbai",
    "legal_system": "common law (India)",
    "urban_rural": "urban",
    "service_provider": "Municipal Corporation; informal water vendors; illegal connections",
    "regulatory_model": "citizenship/legal-subject status ('citizen' vs. 'squatter') determining eligibility for public infrastructure",
    "population": "pavement-dwelling and squatter communities in Mumbai",
    "sample_size": "qualitative case study (illustrative pavement-dwelling settlement)",
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
    "documentation": "TRUE",
    "tenure": "TRUE",
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
    "sanction": "TRUE",
    "participation": "",
    "institutional_fragmentation": "",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "TRUE",
    "service_coverage": "",
    "service_reliability": "",
    "service_quantity": "TRUE",
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
    "study_design": "theoretical-empirical case study (illustrative ethnographic vignette, secondary sources)",
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
        "Moderate: documents how legal citizenship-subject status ('citizen' vs. "
        "'squatter') determines eligibility for public infrastructure including water and "
        "sanitation; pavement dwellers, excluded from formal connections, rely on illegal "
        "water connections procured through pre-election political patronage, pay informal "
        "vendors far above the municipal tariff (approx. Rs. 30/month for 80-100 litres/day "
        "vs. 50 paise/1,000 litres for housed residents charged by the Municipality), and "
        "lack functioning access to public toilets (nearest one 'in a state of absolute "
        "disrepair')."
    ),
    "source_document": "Menon 2013 (retrieved via Google Drive)",
    "page": "155-169",
    "table": "",
    "figure": "",
    "section": "Ethnographic vignette on pavement-dwelling water/sanitation access",
    "exact_location": "Discussion of illegal water connections and public toilets for pavement dwellers",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: legal/institutional mechanism "
        "(citizenship/legal-subject status determining infrastructure eligibility) study "
        "with documented differential water/sanitation-access and affordability outcomes "
        "for a marginalized urban population. Qualitative case study, no regression-based "
        "effect size; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1056 -- Motiram & Osberg 2010
r = blank_row(fieldnames)
r.update({
    "study_id": "S1056",
    "citation": "Motiram S, Osberg L (2010). Social Capital and Basic Goods: The Cautionary Tale of Drinking Water in India. Economic Development and Cultural Change 59(1):63-94.",
    "doi": "",
    "publication_year": "2010",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "national (rural and urban)",
    "legal_system": "common law (India)",
    "urban_rural": "both",
    "service_provider": "community-level water-supply organization",
    "regulatory_model": "informal community collective action / social capital, not a formal statutory mechanism",
    "population": "Indian households, Indian Time Use Survey 1998-99",
    "sample_size": "Indian Time Use Survey microdata, approx. 140 million people represented (2001 census)",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
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
    "property": "TRUE",
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
    "service_quantity": "TRUE",
    "service_quality": "",
    "affordability": "",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "correlation coefficients (caste, land inequality, social-capital index vs. water-supply/collection-time outcomes)",
    "effect_estimate": "",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "",
    "adjusted_or_unadjusted": "unadjusted/correlational (authors explicitly caveat: cross-sectional data restrict claims to statistically significant correlations, not causality)",
    "covariates": "caste, land inequality, community-/group-level social capital",
    "model_type": "correlational/cross-sectional (not causal regression)",
    "study_design": "quantitative cross-sectional survey analysis (Indian Time Use Survey 1998-99)",
    "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "TRUE",
    "attrition": "",
    "reporting_bias": "",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": (
        "Moderate: examines correlations between community- and group-level social capital, "
        "inequality in land, and caste with the organization and supply of community-level "
        "water provision, within a collective-action model in which inequality in net "
        "individual benefits from collective water supply is the central obstacle; documents "
        "16% of rural and 9.6% of urban Indian households (1999) had no water on tap, "
        "spending on average ~45 minutes/day fetching water, and finds statistically "
        "significant correlations between social capital/caste/land-inequality and "
        "community water-supply outcomes, though the authors explicitly caveat these as "
        "correlational given endogeneity concerns in cross-sectional data."
    ),
    "source_document": "Motiram & Osberg 2010 (retrieved via Google Drive)",
    "page": "63-94",
    "table": "",
    "figure": "",
    "section": "Section III: correlations between water supply and social capital, land inequality, caste",
    "exact_location": "Section III empirical findings",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: institutional/social-structural mechanism "
        "(caste-based exclusion, social capital, land inequality) study of community "
        "water-provision organization with a documented water-collection-burden outcome. "
        "NOT added to effect_sizes.csv despite being quantitative: the authors themselves "
        "characterize the relationships as correlational rather than a regression isolating "
        "a specific legal/institutional mechanism's causal effect (unlike Isham & Kahkonen "
        "2001, S1057, this batch, which reports comparable OLS/IV coefficients for an "
        "institutional-participation mechanism), so this does not cleanly satisfy the "
        "strict Family A/B/C direct-mechanism-isolation requirement -- following the "
        "reasoning applied to Greiner 2016 (S1041, Batch 209)."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1057 -- Isham & Kahkonen 2001
r = blank_row(fieldnames)
r.update({
    "study_id": "S1057",
    "citation": "Isham J, Kahkonen S (2001). Institutional Determinants of the Impact of Community-Based Water Services: Evidence from Sri Lanka and India. World Bank working paper.",
    "doi": "",
    "publication_year": "2001",
    "publication_type": "working paper",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "FALSE",
    "country": "Sri Lanka; India",
    "subnational_unit": "Karnataka; Maharashtra",
    "legal_system": "mixed (Sri Lanka); common law (India)",
    "urban_rural": "rural",
    "service_provider": "community-based rural water services (government demand-responsive programs)",
    "regulatory_model": "community-based/demand-responsive approach; joint community-government design, construction, O&M",
    "population": "rural households served by community-based water projects, Sri Lanka, Karnataka, Maharashtra",
    "sample_size": "288-381 households across 16-20 communities per site (3 sites)",
    "household_level": "TRUE",
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
    "sanitation_access": "",
    "service_coverage": "",
    "service_reliability": "TRUE",
    "service_quantity": "TRUE",
    "service_quality": "TRUE",
    "affordability": "",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "OLS coefficients (log household time-saving); multivariate probit (design satisfaction); IV/2SLS (social-capital index)",
    "effect_estimate": "Community design satisfaction on log household water-collection time-saving: Sri Lanka 1.63 (p<.10), Karnataka 2.92 (p<.01), Maharashtra 1.06 (p<.01) (Table 3). Design participation and local decision-making both significantly increase community design satisfaction (Table 4, p<.01 to p<.05 across sites).",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "0.95 (Sri Lanka); 0.95 (Karnataka); 0.38 (Maharashtra) [Huber-adjusted, Table 3]",
    "p_value": "<.10 (Sri Lanka); <.01 (Karnataka); <.01 (Maharashtra)",
    "extraction_sample_size": "288 (Sri Lanka); 188 (Karnataka); 249 (Maharashtra) households",
    "adjusted_or_unadjusted": "adjusted",
    "covariates": "hygiene class, household size, household assets (Table 3); local initiation, design participation, local decision-making, community fixed effects (Table 4)",
    "model_type": "OLS (time-savings); multivariate probit (design satisfaction, construction quality); IV/2SLS (social capital endogeneity)",
    "study_design": "quantitative econometric study (household survey, 3 sites)",
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
        "High: rigorous econometric evidence (OLS, multivariate probit, IV/2SLS) directly "
        "isolates an institutional/participatory mechanism -- household-level participation "
        "in service design and local decision-making -- and shows it significantly predicts "
        "community design satisfaction, which in turn significantly predicts household water-"
        "collection time-savings across all three study sites; social-capital levels (active "
        "community groups/associations) are shown via IV estimation to endogenously "
        "determine these service-level institutions."
    ),
    "source_document": "Isham & Kahkonen 2001 (retrieved via Google Drive)",
    "page": "",
    "table": "Tables 1-9, especially Table 3 (time savings) and Table 4 (design satisfaction)",
    "figure": "",
    "section": "Empirical results",
    "exact_location": "Tables 2-9",
    "extraction_note": (
        "INCLUDE and effect_sizes-eligible per INCLUSION_EXCLUSION.md and the strict Family "
        "A/B/C framework: a genuine regression-based estimate (OLS with Huber-adjusted "
        "standard errors) directly isolates an institutional/participatory mechanism's "
        "(community design participation/satisfaction) effect on a water-access-relevant "
        "outcome (household water-collection time-savings), with reported coefficients, "
        "standard errors, and significance levels across three independent sites. Added to "
        "effect_sizes.csv as S1057 (Family A)."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1058 -- Cheng 2013
r = blank_row(fieldnames)
r.update({
    "study_id": "S1058",
    "citation": "Cheng D (2013). (In)visible urban water networks: the politics of non-payment in Manila's low-income communities. Environment and Urbanization 26(1):249-263.",
    "doi": "10.1177/0956247812469926",
    "publication_year": "2013",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Philippines",
    "subnational_unit": "Metro Manila",
    "legal_system": "civil law (Philippines)",
    "urban_rural": "urban",
    "service_provider": "two private water concessionaires (Metro Manila)",
    "regulatory_model": "differentiated non-payment/revenue-recovery enforcement mechanisms by customer income level",
    "population": "low-income and high-volume water consumers, Metro Manila",
    "sample_size": "qualitative case study",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "TRUE",
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
    "disconnection": "TRUE",
    "reconnection": "",
    "sanction": "TRUE",
    "participation": "",
    "institutional_fragmentation": "",
    "political_coordination": "",
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
    "study_design": "qualitative case study",
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
        "High: documents that Manila's two private water concessionaires apply asymmetric "
        "institutional/administrative payment-recovery mechanisms -- increased policing and "
        "transfer of responsibility onto communities/individuals for low-income consumers, "
        "versus technical improvements and arrears settlement for high-volume (wealthier) "
        "customers -- resulting in higher effective costs in poorer areas, continued "
        "invisibility of unserved/underserved populations behind aggregate coverage "
        "statistics, and small water providers increasingly functioning as a policing arm "
        "of the utilities rather than competitive alternatives."
    ),
    "source_document": "Cheng 2013 (retrieved via Google Drive)",
    "page": "249-263",
    "table": "",
    "figure": "",
    "section": "Politics of non-payment; differentiated treatment of poor and non-poor consumers",
    "exact_location": "Throughout, especially the four documented failures of the visibility/payment-recovery mechanism",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/administrative-"
        "enforcement mechanism (differentiated non-payment policing) study with documented "
        "differential water-service-access and affordability outcomes between poor and "
        "non-poor consumers. Qualitative case study, no regression-based effect size; not "
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
