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

# S1064 -- Walsh 2011
r = blank_row(fieldnames)
r.update({
    "study_id": "S1064",
    "citation": "Walsh C (2011). Managing Urban Water Demand in Neoliberal Northern Mexico. Human Organization 70(1):54-62.",
    "doi": "10.17730/humo.70.1.5675v706667047l2",
    "publication_year": "2011",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Mexico",
    "subnational_unit": "Matamoros, Tamaulipas",
    "legal_system": "civil law (Mexico)",
    "urban_rural": "urban",
    "service_provider": "Junta de Agua y Drenaje (JAD, Water and Drainage Council)",
    "regulatory_model": "neoliberal demand-side management: cost recovery, water metering, decentralized surveillance/enforcement",
    "population": "urban residents of Matamoros, including peripheral low-income immigrant neighborhoods",
    "sample_size": "ethnographic fieldwork 2004-2008, interviews with JAD staff and school-based program participants",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "TRUE",
    "indigenous_population": "",
    "migrant_population": "TRUE",
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
    "delay": "",
    "discretion": "TRUE",
    "hardship_exception": "TRUE",
    "administrative_review": "",
    "complaint": "",
    "judicial_review": "",
    "disconnection": "TRUE",
    "reconnection": "",
    "sanction": "TRUE",
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
        "High: documents JAD's cost-recovery program including water-meter installation "
        "(installed first in wealthy/middle-class neighborhoods to counter perceptions of "
        "fleecing the poor, later extended to the majority), a debt-amnesty program, "
        "monthly payment plans, and disconnection/fines for wasteful use -- operating "
        "within a legal constraint that water users 'by law, cannot be denied the service' "
        "since water is recognized in Mexico's constitution as more a right than a "
        "commodity. Simultaneously documents extension of water lines, communal taps, and "
        "truck delivery to peripheral low-income immigrant neighborhoods."
    ),
    "source_document": "Walsh 2011 (retrieved via Google Drive)",
    "page": "54-62",
    "table": "",
    "figure": "Figures 1-2 (Water Culture Program characters)",
    "section": "Teaching a Culture of Water in the Borderlands",
    "exact_location": "Throughout, especially discussion of water-meter installation sequencing and legal non-denial constraint",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/administrative "
        "mechanism (cost-recovery/tariff enforcement, water-meter rollout sequencing) "
        "study with documented differential water-access/affordability dynamics for poor "
        "vs. wealthy neighborhoods. Ethnographic case study, no regression-based effect "
        "size; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1065 -- Jemmali & Amara 2015
r = blank_row(fieldnames)
r.update({
    "study_id": "S1065",
    "citation": "Jemmali H, Amara M (2015). Assessing Inequality of Human Opportunities: A New Approach for Public Policy in Tunisia. Applied Research in Quality of Life 10(3):473-497.",
    "doi": "10.1007/s11482-014-9315-5",
    "publication_year": "2015",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Tunisia",
    "subnational_unit": "eastern (littoral) vs. western (inland) regions",
    "legal_system": "civil law (Tunisia)",
    "urban_rural": "both",
    "service_provider": "national water/sanitation infrastructure",
    "regulatory_model": "Human Opportunity Index (HOI) framework applied to regional service-access disparities",
    "population": "Tunisian households, national household survey data",
    "sample_size": "national household survey (Human Opportunity Index estimation)",
    "household_level": "TRUE",
    "community_level": "TRUE",
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
    "institutional_fragmentation": "",
    "political_coordination": "",
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
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "Human Opportunity Index (HOI); logistic regression on 'circumstance' variables",
    "effect_estimate": "Large and statistically significant disparities in access to safe water and sanitation between eastern (littoral) and western (inland) Tunisian regions; residence area, household-head education, and per capita household expenditure identified as the most important circumstances driving regional disparities (specific coefficient values not extracted from available text).",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "significant (per source text; exact values not extracted)",
    "extraction_sample_size": "",
    "adjusted_or_unadjusted": "adjusted (seven circumstance variables per Roemer's theory)",
    "covariates": "residence area, household-head education, per capita household expenditure, and four other circumstance variables",
    "model_type": "logistic regression (Human Opportunity Index methodology)",
    "study_design": "quantitative cross-sectional survey analysis",
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
        "Moderate: applies the Human Opportunity Index methodology (logistic regressions "
        "on circumstances not controllable by individuals) to find large, statistically "
        "significant regional disparities in water/sanitation access between Tunisia's "
        "eastern and western regions, driven primarily by residence area, household-head "
        "education, and household expenditure -- documents disparity but does not isolate "
        "a specific legal/institutional eligibility or barrier mechanism (fees, permits, "
        "tenure) in the strict Family A/B/C sense; circumstance variables are broader "
        "socioeconomic/geographic factors."
    ),
    "source_document": "Jemmali & Amara 2015 (retrieved via Google Drive)",
    "page": "473-497",
    "table": "",
    "figure": "",
    "section": "HOI estimation results for water and sanitation access",
    "exact_location": "Results section on regional water/sanitation access disparities",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: quantitative disparity-documentation study "
        "of water/sanitation access inequality by region and socioeconomic circumstance. "
        "NOT added to effect_sizes.csv: circumstance variables (region, education, "
        "expenditure) are general socioeconomic/demographic predictors, not a specific "
        "legal/institutional mechanism (fees, tenure, permits, eligibility rules) directly "
        "isolated per the strict Family A/B/C framework, following the reasoning applied "
        "to Motiram & Osberg 2010 (S1056, Batch 213)."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1066 -- Dawson 2010
r = blank_row(fieldnames)
r.update({
    "study_id": "S1066",
    "citation": "Dawson M (2010). The cost of belonging: exploring class and citizenship in Soweto's water war. Citizenship Studies 14(4):381-394.",
    "doi": "10.1080/13621025.2010.490033",
    "publication_year": "2010",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "South Africa",
    "subnational_unit": "Soweto, Johannesburg",
    "legal_system": "common law (South Africa)",
    "urban_rural": "urban",
    "service_provider": "Johannesburg Water (Operation Gcin'amanzi prepaid metering program)",
    "regulatory_model": "prepaid water metering and disconnection enforcement",
    "population": "Soweto residents, differentiated by class",
    "sample_size": "qualitative case study",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "TRUE",
    "legal_status": "TRUE",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "",
    "burden": "TRUE",
    "discretion_accommodation": "",
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
    "discretion": "",
    "hardship_exception": "",
    "administrative_review": "",
    "complaint": "TRUE",
    "judicial_review": "",
    "disconnection": "TRUE",
    "reconnection": "",
    "sanction": "TRUE",
    "participation": "TRUE",
    "institutional_fragmentation": "",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
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
        "High: examines Operation Gcin'amanzi, Johannesburg Water's prepaid water-meter "
        "program in Soweto, and its class-differentiated implementation and reception; "
        "analyzes how formal citizenship and belonging are constructed through residents' "
        "differential relationships to metered, paying water access versus informal, "
        "illegal-connection resistance, documenting a legal/institutional mechanism "
        "(prepaid metering, disconnection enforcement) with class-based differential "
        "water-access outcomes."
    ),
    "source_document": "Dawson 2010 (retrieved via Google Drive)",
    "page": "381-394",
    "table": "",
    "figure": "",
    "section": "Operation Gcin'amanzi and class-differentiated citizenship",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine legal/institutional mechanism "
        "(prepaid water metering, disconnection enforcement) study documenting class-based "
        "differential water-access outcomes. Qualitative case study, no regression-based "
        "effect size; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1067 -- Schoeffel 1995
r = blank_row(fieldnames)
r.update({
    "study_id": "S1067",
    "citation": "Schoeffel P (1995). Cultural and institutional issues in the appraisal of projects in developing countries: South Pacific water resources. Project Appraisal 10(3):155-161.",
    "doi": "10.1080/02688867.1995.9726989",
    "publication_year": "1995",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "South Pacific island country (pseudonymized as 'Vaika')",
    "subnational_unit": "Hinterland and Coast areas",
    "legal_system": "customary/statutory mixed (South Pacific)",
    "urban_rural": "rural",
    "service_provider": "government rural water supply agency (RWSS); Local Government Council (LGC); donor-funded project",
    "regulatory_model": "donor-funded rural water project relying on locally-formed water-users committees for fee collection and O&M",
    "population": "Melanesian rural villagers, Hinterland and Coast areas",
    "sample_size": "project case study (27-49 villages across two scheme components)",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "",
    "tenure_status": "TRUE",
    "legal_status": "",
    "indigenous_population": "TRUE",
    "migrant_population": "",
    "eligibility": "",
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
    "delay": "TRUE",
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
    "sanitation_access": "",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "TRUE",
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
    "study_design": "detailed qualitative case study (project evaluation)",
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
        "High: documents multiple compounding institutional/administrative failure "
        "mechanisms in a donor-funded rural water project -- local-government inability "
        "to collect water-user fees amid widespread 'no tax' political opposition "
        "(only 4 of 18 villages paid fully in the second year); complete exclusion of "
        "women from water-user committees and technical (village-plumber) training "
        "despite women bearing the water-collection burden; customary land-tenure "
        "disputes in which landowners blocked headworks construction pending large "
        "payments; and political-party-based allocation disputes in which factional "
        "rivalries were blamed for which villages received service -- collectively "
        "producing project failure and denied/unreliable water access."
    ),
    "source_document": "Schoeffel 1995 (retrieved via Google Drive)",
    "page": "155-161",
    "table": "",
    "figure": "",
    "section": "Institutional impediments; Gender impediments",
    "exact_location": "Throughout, especially Institutional impediments and Gender impediments sections",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rich institutional/administrative-mechanism "
        "case study with multiple documented access-barrier mechanisms (fee-collection "
        "failure, gender exclusion, land tenure, political discretion) directly producing "
        "denied water access. Qualitative case study, no regression-based effect size; "
        "not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1068 -- Schur 2017
r = blank_row(fieldnames)
r.update({
    "study_id": "S1068",
    "citation": "Schur EL (2017). Potable or Affordable? A Comparative Study of Household Water Security Within a Transboundary Aquifer Along the U.S.-Mexico Border. Journal of Latin American Geography 16(3):29-58.",
    "doi": "10.1353/lag.2017.0051",
    "publication_year": "2017",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "United States; Mexico",
    "subnational_unit": "Columbus, New Mexico; Palomas, Chihuahua",
    "legal_system": "common law (US) and civil law (Mexico), binational water policy",
    "urban_rural": "rural",
    "service_provider": "local water utilities, Columbus (US) and Palomas (Mexico)",
    "regulatory_model": "distinct national/binational institutional approaches to shared transboundary aquifer contamination",
    "population": "households in Palomas (pop. 5,748) and Columbus (pop. 1,625)",
    "sample_size": "152-household survey, 60 semi-structured interviews, 1996 baseline comparison, 2016 fieldwork",
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
    "participation": "",
    "institutional_fragmentation": "TRUE",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "",
    "service_reliability": "TRUE",
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
    "extraction_sample_size": "152 households",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "comparative mixed-methods case study (survey, interviews, participant observation)",
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
        "High: documents that Palomas (Mexico) and Columbus (US), sharing the arsenic- and "
        "fluoride-contaminated Mimbres Basin Aquifer, adopted distinct institutional "
        "approaches to groundwater contamination structured by differing national and "
        "binational water policy and institutional parameters -- Columbus's centralized "
        "water-filtration technology improved potability but made water less affordable, "
        "while Palomas's decentralized filtration technology did not resolve household "
        "contamination problems -- demonstrating that binational institutional "
        "asymmetries directly produce differential water-affordability and -potability "
        "access outcomes across the same shared resource."
    ),
    "source_document": "Schur 2017 (retrieved via Google Drive)",
    "page": "29-58",
    "table": "",
    "figure": "",
    "section": "Comparative findings on institutional approaches and water security outcomes",
    "exact_location": "Throughout, especially findings on centralized vs. decentralized filtration outcomes",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/policy-mechanism "
        "comparative study directly documenting differential water-affordability and "
        "access outcomes shaped by binational institutional parameters. Mixed-methods "
        "comparative case study, no regression-based effect size; not added to "
        "effect_sizes.csv."
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
