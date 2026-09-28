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

# S1121 -- Hanak 2008
r = blank_row(fieldnames)
r.update({
    "study_id": "S1121",
    "citation": "Hanak E (2008). Is Water Policy Limiting Residential Growth? Evidence from California. Land Economics 84(1):31-50.",
    "doi": "",
    "publication_year": "2008",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "United States",
    "subnational_unit": "California (289 jurisdictions)",
    "legal_system": "common law (US); California SB 901 (1995), SB 610 and SB 221 (2001)",
    "urban_rural": "mixed",
    "service_provider": "local water utilities; land-use authorities (cities and counties)",
    "regulatory_model": "water-adequacy screening policies (administrative review) vs. water connection impact fees (price-based)",
    "population": "new residential development / prospective homebuyers, California jurisdictions",
    "sample_size": "289-316 jurisdictions, panel 1994-2003",
    "household_level": "",
    "community_level": "TRUE",
    "income_group": "",
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
    "property": "",
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "TRUE",
    "service_area": "",
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
    "institutional_fragmentation": "",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
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
    "refusal": "TRUE",
    "delay_outcome": "TRUE",
    "effect_measure": "fixed-effects and random-effects panel regression coefficients (semi-elasticities)",
    "effect_estimate": (
        "Water adequacy rule coefficient -0.31** to -0.53** (FE models; semi-elasticity "
        "-0.26 to -0.41) and -0.18* to -0.29** (RE models; implied reduction 16%-25%). "
        "Overall, adoption of a water-adequacy screening policy reduces new residential "
        "permitting by approximately 16%-41% depending on sample/specification. Water "
        "connection impact fees (price-based mechanism) show no statistically "
        "significant effect on housing growth in any specification."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "0.10-0.21 (water adequacy rule coefficient, across specifications)",
    "p_value": "<0.05 to <0.01 (water adequacy rule); not significant (impact fees)",
    "extraction_sample_size": "289 jurisdictions (Full Sample), 1994-2003 panel",
    "adjusted_or_unadjusted": "adjusted (fixed-effects and random-effects panel regression, controlling for MSA price growth, prime rate, pre-1990 housing stock, other growth controls)",
    "covariates": "real MSA price growth rate (current and lagged), real prime rate change, ln(pre-1990 housing stock), general growth control measures",
    "model_type": "fixed-effects and random-effects panel regression",
    "study_design": "quantitative panel-regression study (original statewide survey data)",
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
        "High: rigorous panel-regression study directly isolating the causal effect of "
        "a specific administrative/legal institutional mechanism (water-adequacy "
        "screening review, an Adequate Public Facilities Ordinance-type requirement) "
        "on new-housing/water-connection growth, with a clear contrast against a "
        "price-based alternative mechanism (impact fees) showing no such effect; "
        "addresses endogeneity via Granger-causality tests and Hausman specification "
        "tests."
    ),
    "source_document": "Hanak 2008 (retrieved via Google Drive)",
    "page": "31-50",
    "table": "Tables 2, 3, 4",
    "figure": "",
    "section": "III. Housing Market Impacts of Water Adequacy Regulations; V. Results",
    "exact_location": "Tables 2-4",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous regression-based study directly "
        "isolating an administrative/legal mechanism's effect on a water-access-"
        "adjacent outcome (new residential water-connection permitting). ADDED to "
        "effect_sizes.csv as a Family A estimate."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1122 -- Dos Santos & LeGrand 2013
r = blank_row(fieldnames)
r.update({
    "study_id": "S1122",
    "citation": "Dos Santos S, LeGrand T (2013). Is the Tap Locked? An Event History Analysis of Piped Water Access in Ouagadougou, Burkina Faso. Urban Studies 50(6):1292-1310.",
    "doi": "10.1177/0042098012462613",
    "publication_year": "2013",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Burkina Faso",
    "subnational_unit": "Ouagadougou",
    "legal_system": "civil law (Burkina Faso); urban zoning/land-titling system",
    "urban_rural": "urban",
    "service_provider": "national water utility (piped water network)",
    "regulatory_model": "zoned vs. non-zoned (spontaneous settlement) land-allocation system",
    "population": "residents of Ouagadougou, by residential/tenure status and zone",
    "sample_size": "residential life-history data, multiple cohorts",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "",
    "tenure_status": "TRUE",
    "legal_status": "TRUE",
    "indigenous_population": "",
    "migrant_population": "TRUE",
    "eligibility": "TRUE",
    "burden": "",
    "discretion_accommodation": "",
    "enforcement": "",
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
    "discretion": "",
    "hardship_exception": "",
    "administrative_review": "",
    "complaint": "",
    "judicial_review": "",
    "disconnection": "TRUE",
    "reconnection": "",
    "sanction": "",
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
    "affordability": "",
    "service_continuity": "",
    "application_success": "",
    "refusal": "TRUE",
    "delay_outcome": "",
    "effect_measure": "Cox proportional-hazards regression, hazard ratios",
    "effect_estimate": (
        "Zone of residence (zoned periphery = reference): non-zoned periphery hazard "
        "ratio = 0.14*** for first access to piped water (connection 'not possible in "
        "non-zoned areas'); downtown hazard ratio = 3.12***. Residence status (owner/"
        "co-owner = reference): renting/co-renting hazard ratio = 2.56***-2.94**. "
        "Interaction terms: renting * non-zoned periphery hazard ratio = 0.00***; "
        "other's-residence * non-zoned periphery hazard ratio = 0.00***. Rural-origin "
        "migrants have approximately half the hazard of piped-water access compared "
        "with Ouagadougou natives. Access disparity: 48% of households had piped water "
        "access in the city centre vs. only 22% in zoned peripheral areas (2000)."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "p<0.001 (***), p<0.01 (**), for key zone/tenure covariates",
    "extraction_sample_size": "person-time observations across residence-status and zone-of-residence categories",
    "adjusted_or_unadjusted": "adjusted (Cox regression with residence status, zone of residence, migration origin, gender, education, employment type as covariates)",
    "covariates": "residence status (owner/renter/other), zone of residence (downtown/zoned periphery/non-zoned periphery), migration origin, gender, education, employment type",
    "model_type": "Cox proportional-hazards event-history model",
    "study_design": "quantitative event-history regression study",
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
        "High: rigorous event-history regression study directly isolating the effect "
        "of a legal/administrative zoning-status mechanism (formal connection is "
        "explicitly stated to be impossible in non-zoned/informal settlement areas) on "
        "first access to piped water, with interaction terms showing the mechanism's "
        "effect is compounded for renters in non-zoned areas (hazard ratio "
        "approximately zero)."
    ),
    "source_document": "Dos Santos & LeGrand 2013 (retrieved via Google Drive)",
    "page": "1292-1310",
    "table": "Tables 2, 3, 4",
    "figure": "",
    "section": "Multivariate results",
    "exact_location": "Tables 2-4",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous regression-based study directly "
        "isolating a legal/administrative zoning-status mechanism's effect on piped "
        "water access. ADDED to effect_sizes.csv as a Family A/C estimate."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1123 -- Mukhija & Mason 2013
r = blank_row(fieldnames)
r.update({
    "study_id": "S1123",
    "citation": "Mukhija V, Mason DR (2013). Reluctant Cities, Colonias and Municipal Underbounding in the US: Can Cities Be Convinced to Annex Poor Enclaves? Urban Studies 50(14):2959-2975.",
    "doi": "10.1177/0042098013482503",
    "publication_year": "2013",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "United States",
    "subnational_unit": "California (colonias case study)",
    "legal_system": "common law (US); municipal annexation law",
    "urban_rural": "mixed",
    "service_provider": "adjacent municipal governments",
    "regulatory_model": "municipal annexation/underbounding (unincorporated poor enclave status)",
    "population": "residents of colonias (poor unincorporated neighborhoods)",
    "sample_size": "",
    "household_level": "",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "TRUE",
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
    "service_quality": "",
    "affordability": "",
    "service_continuity": "",
    "application_success": "",
    "refusal": "TRUE",
    "delay_outcome": "",
    "effect_measure": "",
    "effect_estimate": (
        "Case study finding: cities are typically reluctant to annex adjacent poor "
        "unincorporated colonias, leaving them without potable water and sewer "
        "systems; a documented counter-example from California shows cities were "
        "convinced to annex poor colonias, with federal infrastructure funding "
        "identified as a critical enabling mechanism, alongside recommendations for "
        "deeper resident involvement in decision-making."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "case study (documentary analysis)",
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
        "Moderate-high: documents municipal underbounding (annexation refusal) as an "
        "institutional/legal mechanism excluding poor unincorporated colonias from "
        "water/sewer infrastructure, and identifies federal infrastructure funding as "
        "a mechanism that can reverse this exclusion."
    ),
    "source_document": "Mukhija & Mason 2013 (retrieved via Google Drive)",
    "page": "2959-2975",
    "table": "",
    "figure": "",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous institutional/legal-mechanism "
        "case study of municipal annexation law's effect on water/sewer access. No "
        "regression-based effect size; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1124 -- Smiley 2016
r = blank_row(fieldnames)
r.update({
    "study_id": "S1124",
    "citation": "Smiley SL (2016). Water Availability and Reliability in Dar es Salaam, Tanzania. Journal of Development Studies.",
    "doi": "10.1080/00220388.2016.1146699",
    "publication_year": "2016",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Tanzania",
    "subnational_unit": "Dar es Salaam",
    "legal_system": "civil law (Tanzania); 2002 National Water Policy",
    "urban_rural": "urban",
    "service_provider": "national water utility (piped water network)",
    "regulatory_model": "fragmented water-service provision by income area",
    "population": "households in lower-income, predominantly African-resident areas of Dar es Salaam",
    "sample_size": "household surveys and interviews",
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
    "property": "",
    "planning": "",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "TRUE",
    "procedural_steps": "TRUE",
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
    "delay_outcome": "",
    "effect_measure": "",
    "effect_estimate": (
        "New piped-water connections require upfront payment for meter, pipes, labor, "
        "connection fee, plus three months' estimated consumption -- expenses "
        "described as 'beyond the scope of affordability for many of Dar es Salaam's "
        "poorest residents.' Households surveyed in lower-income, predominantly "
        "African areas used an average of 29 L/person/day vs. 166 L/person/day in "
        "high-income Oyster Bay (UNDP 2006 data cited)."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "household surveys and interviews (Dar es Salaam)",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "mixed-methods empirical case study (household surveys, interviews)",
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
        "Moderate-high: rigorous household-survey-based documentation of connection-"
        "fee and fragmented-provision institutional mechanisms producing large "
        "differential water-consumption outcomes by income area."
    ),
    "source_document": "Smiley 2016 (retrieved via Google Drive)",
    "page": "",
    "table": "",
    "figure": "",
    "section": "Piped water provision; Environmental Justice and the Right to Water",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous empirical case study of "
        "connection-fee and service-fragmentation mechanisms. No regression-based "
        "effect size; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1125 -- Fiki et al 2007
r = blank_row(fieldnames)
r.update({
    "study_id": "S1125",
    "citation": "Fiki CO, Amupitan J, Dabi D, Nyong A (2007). From Disciplinary to Interdisciplinary Community Development: The Jos-McMaster Drought and Rural Water Use Project in Nigeria. Journal of Community Practice 15(1-2):147-170.",
    "doi": "10.1300/J125v15n01_07",
    "publication_year": "2007",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Nigeria",
    "subnational_unit": "Plateau State (Jos)",
    "legal_system": "common law (Nigeria)",
    "urban_rural": "rural",
    "service_provider": "Directorate of Food, Roads and Rural Infrastructure (DFRRI); community-managed alternative (Jos-McMaster Project)",
    "regulatory_model": "shift from centralized 'command and control' state water provision to community-centered nodal governance",
    "population": "rural communities, drought-prone north-eastern Nigeria",
    "sample_size": "",
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
    "property": "TRUE",
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "",
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
    "participation": "TRUE",
    "institutional_fragmentation": "TRUE",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "TRUE",
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
    "effect_measure": "",
    "effect_estimate": (
        "DFRRI's centralized state-directed rural water program became politicized, "
        "affecting distribution of facilities; boreholes allocated to some "
        "communities were sited on old cemeteries without consultation, rendering "
        "them unused; allocation process became corrupt, subject to political "
        "patronage; community participation was 'confined to the documents alone.' "
        "The Jos-McMaster Project's community-centered nodal-governance alternative "
        "(1993-1998, CIDA-funded) is documented as improving legitimacy and community "
        "buy-in through participatory rural appraisal and structured community "
        "conferences."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "institutional/governance case study",
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
        "Moderate-high: documents how a centralized state water-provision program's "
        "governance failures (politicization, corruption, lack of consultation) "
        "produced access failures for rural communities, contrasted with a "
        "documented institutional alternative (nodal/community governance)."
    ),
    "source_document": "Fiki et al. 2007 (retrieved via Google Drive)",
    "page": "147-170",
    "table": "",
    "figure": "",
    "section": "The Context of Community Development in Nigeria; Jos-McMaster Drought and Rural Water Use Project",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous institutional/governance-"
        "failure case study documenting centralized-state water-provision mechanism "
        "access failures. No regression-based effect size; not added to "
        "effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1126 -- Ojha et al 2020
r = blank_row(fieldnames)
r.update({
    "study_id": "S1126",
    "citation": "Ojha H, Neupane KR, Pandey CL, Singh V, Bajracharya R, Dahal N (2020). Scarcity amidst plenty: Lower Himalayan cities struggling for water security. Water 12(2):567.",
    "doi": "10.3390/w12020567",
    "publication_year": "2020",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Nepal; India",
    "subnational_unit": "5 Himalayan cities (3 Nepal, 2 western Indian Himalayas)",
    "legal_system": "mixed (civil/common law, Nepal/India)",
    "urban_rural": "urban",
    "service_provider": "mix of government, community and private water-supply systems",
    "regulatory_model": "local water-governance institutions (absence of coordinated water planning agency)",
    "population": "urban residents and tourists, 5 Himalayan cities",
    "sample_size": "5 cities, field research 2014-2018",
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
    "service_reliability": "TRUE",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "",
    "service_continuity": "TRUE",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "",
    "effect_estimate": (
        "4 of 5 Himalayan towns studied lack well-performing local institutions to "
        "manage water supply; none has a robust, coordinated system of water planning "
        "and governance despite significant regional precipitation, resulting in a "
        "fragmented mix of government, community, and private water-supply systems "
        "across both Nepal and India."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "5 cities",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "multi-city comparative field-research case study",
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
        "Moderate-high: multi-city field-research comparison documenting local "
        "water-governance institutional capacity gaps and fragmented, uncoordinated "
        "government/community/private supply systems as a mechanism shaping urban "
        "water security across 5 Himalayan cities."
    ),
    "source_document": "Ojha et al. 2020 (retrieved via Google Drive)",
    "page": "",
    "table": "",
    "figure": "",
    "section": "Abstract; throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous multi-city institutional case "
        "study of water-governance capacity gaps. No regression-based effect size; "
        "not added to effect_sizes.csv."
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
