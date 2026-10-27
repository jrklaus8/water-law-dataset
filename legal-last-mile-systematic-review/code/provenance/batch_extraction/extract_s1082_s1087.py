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

# S1082 -- Etongo et al 2018
r = blank_row(fieldnames)
r.update({
    "study_id": "S1082",
    "citation": "Etongo D, Fagan GH, Kabonesa C, Asaba RB (2018). Community-Managed Water Supply Systems in Rural Uganda: The Role of Participation and Capacity Development. Water 10(9):1271.",
    "doi": "10.3390/w10091271",
    "publication_year": "2018",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Uganda",
    "subnational_unit": "Lwengo district, southern Uganda",
    "legal_system": "common law (Uganda)",
    "urban_rural": "rural",
    "service_provider": "Water User Committees (WUCs), community-managed boreholes/shallow wells",
    "regulatory_model": "community-based management (CBM) model",
    "population": "rural households, Lwengo district",
    "sample_size": "642 households across 17 villages, two Parishes",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "TRUE",
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
    "formal_connection": "",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "TRUE",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "chi-square test of independence",
    "effect_estimate": "Mobilization has no significant impact on household financial contributions to a WUC (chi-square test); no significant difference between better-off and relatively poor households in WUC contributions. 41.7% of surveyed households used an unprotected source; 30% had a WUC member; 52% never made financial contributions to a WUC, 34.6% contributed ad hoc.",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "not significant (mobilization x contribution; wealth x contribution)",
    "extraction_sample_size": "642 households",
    "adjusted_or_unadjusted": "unadjusted (chi-square)",
    "covariates": "mobilization status, household wealth",
    "model_type": "chi-square test of independence",
    "study_design": "cross-sectional household survey with shared dialogue workshop",
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
        "Moderate: examines Water User Committees (WUCs) as the institutional mechanism "
        "governing community-managed rural water supply, finding 52% of households never "
        "contributed financially to WUCs, no significant difference in contribution "
        "behavior between wealthier and poorer households, and that abandoned boreholes "
        "and lack of rehabilitation reflect weak technical, financial, and institutional "
        "performance of the CBM model."
    ),
    "source_document": "Etongo et al. 2018 (retrieved via Google Drive)",
    "page": "1-18",
    "table": "",
    "figure": "",
    "section": "Results and Discussion",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/community-management "
        "mechanism study examining WUC financial-contribution requirements as a "
        "determinant of rural water-system functionality. NOT added to effect_sizes.csv: "
        "only a chi-square test of independence is reported (not a regression-based "
        "estimate isolating an effect on a water-access outcome per the strict Family "
        "A/B/C framework)."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1083 -- Badri & Joshi 2018
r = blank_row(fieldnames)
r.update({
    "study_id": "S1083",
    "citation": "Badri R, Joshi P (2018). Significance of Granular Real Time Data for studying ground realities, addressing gaps in governance, and for measuring impact. IEEE PuneCon 2018.",
    "doi": "10.1109/PUNECON.2018.8745386",
    "publication_year": "2018",
    "publication_type": "conference paper",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "Kolhapur, Navi Mumbai, Pimpri-Chinchwad, Pune, Maharashtra",
    "legal_system": "common law (India)",
    "urban_rural": "urban",
    "service_provider": "Shelter Associates (NGO), Urban Local Bodies",
    "regulatory_model": "One Home-One Toilet (OHOT) cost-sharing household sanitation delivery model",
    "population": "urban slum households, four Maharashtra cities",
    "sample_size": "386-463 households (pre-post impact assessment)",
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
    "enforcement": "",
    "documentation": "TRUE",
    "tenure": "",
    "property": "",
    "planning": "TRUE",
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
    "participation": "TRUE",
    "institutional_fragmentation": "",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "TRUE",
    "formal_connection": "",
    "water_access": "",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "TRUE",
    "affordability": "TRUE",
    "service_continuity": "",
    "application_success": "TRUE",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "pre-post case-control impact assessment (percentage-point comparison)",
    "effect_estimate": "Households using CTBs (community toilet blocks) reduced from 96.1% to 11.0% (male) and 96.3% to 8.8% (female) post-intervention; UTI symptoms declined from 23% to 13%; night-time food restriction reduced from 27% to 5%. 99% of households expressed satisfaction with the cost-sharing (OHOT) model.",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "386-463 households, 2,263 individuals",
    "adjusted_or_unadjusted": "unadjusted (descriptive pre-post comparison)",
    "covariates": "",
    "model_type": "pre-post case-control impact assessment",
    "study_design": "practitioner impact-assessment study",
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
        "Moderate: documents the OHOT model's institutional/administrative mechanism -- "
        "a triangular partnership between an NGO (Shelter Associates), Urban Local "
        "Bodies, and community members, in which the NGO provides construction materials "
        "at the household's doorstep while beneficiaries bear the labour cost -- as the "
        "specific cost-sharing arrangement enabling household sanitation facility access "
        "in urban slums, with documented reductions in use of community toilet blocks and "
        "improved health/safety outcomes."
    ),
    "source_document": "Badri & Joshi 2018 (retrieved via Google Drive)",
    "page": "1-8",
    "table": "Table 1-4",
    "figure": "Figures 1-9",
    "section": "Impact Assessment Study",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/administrative-"
        "assistance mechanism study directly enabling household sanitation access for the "
        "urban poor. NOT added to effect_sizes.csv: descriptive pre-post percentage "
        "comparison, not a regression-based estimate isolating a mechanism's effect per "
        "the strict Family A/B/C framework."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1084 -- Behera, Rahut & Sethi 2020
r = blank_row(fieldnames)
r.update({
    "study_id": "S1084",
    "citation": "Behera B, Rahut DB, Sethi N (2020). Analysis of household access to drinking water, sanitation, and waste disposal services in urban areas of Nepal. Utilities Policy 62:100996.",
    "doi": "10.1016/j.jup.2019.100996",
    "publication_year": "2020",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Nepal",
    "subnational_unit": "national (urban areas, five development regions)",
    "legal_system": "civil law (Nepal)",
    "urban_rural": "urban",
    "service_provider": "national water/sanitation/waste-disposal service infrastructure",
    "regulatory_model": "Nepal Living Standard Survey (NLSS) panel, 1995-2011",
    "population": "urban households, Nepal",
    "sample_size": "Nepal Living Standard Survey, three waves (1995-96, 2003-04, 2010-11)",
    "household_level": "TRUE",
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
    "effect_measure": "multinomial logit regression (odds ratio)",
    "effect_estimate": "Age of household head positively/significantly (p<0.01) associated with piped-water access; female-headed household negative/significant (p<0.10) for wells/hand pumps vs. piped water; household size positively/significantly (p<0.05) associated with wells/hand pumps; distance to market negative/significant (p<0.01) for drainage access; education levels of male/female adult members positively/significantly (p<0.01) associated with improved sanitation and waste-disposal access.",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "<0.01 to <0.10 depending on variable, see effect_estimate",
    "extraction_sample_size": "Nepal Living Standard Survey, urban subsample",
    "adjusted_or_unadjusted": "adjusted (multinomial logit)",
    "covariates": "age of household head, gender of household head, household size, education, distance to market, ecological belt, development region",
    "model_type": "multinomial logit regression",
    "study_design": "quantitative panel survey regression study",
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
        "Moderate: rigorous multinomial logit regression across three NLSS waves finds "
        "household demographic and geographic circumstance variables (age, gender, "
        "household size, education, distance to market, ecological region) are "
        "significant determinants of household access to drinking water, sanitation, and "
        "waste-disposal services, rather than isolating a single specific legal/"
        "institutional eligibility or barrier mechanism."
    ),
    "source_document": "Behera, Rahut & Sethi 2020 (retrieved via Google Drive)",
    "page": "",
    "table": "Tables 3-6",
    "figure": "",
    "section": "Results",
    "exact_location": "Tables 3-6 and accompanying discussion",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous quantitative regression study of "
        "water/sanitation access determinants. NOT added to effect_sizes.csv: the "
        "significant predictors are broad socioeconomic/geographic circumstance "
        "variables, not a specific legal/institutional eligibility or barrier mechanism "
        "isolated per the strict Family A/B/C framework, following the reasoning applied "
        "to Antunes & Martins 2020 (S1079, Batch 217) and Motiram & Osberg 2010 (S1056, "
        "Batch 213)."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1085 -- Tigabu, Nicholson, Collick & Steenhuis
r = blank_row(fieldnames)
r.update({
    "study_id": "S1085",
    "citation": "Tigabu AD, Nicholson CF, Collick AS, Steenhuis TS. Determinants of household participation in the management of rural water supply systems: A case from Ethiopia. Water Policy.",
    "doi": "",
    "publication_year": "",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Ethiopia",
    "subnational_unit": "Achefer area, Amhara region",
    "legal_system": "civil law (Ethiopia)",
    "urban_rural": "rural",
    "service_provider": "Water User Committees (WUCs)",
    "regulatory_model": "community-based management (CBM) model, WUC-set contribution/tariff levels",
    "population": "rural households, Achefer area, Amhara region",
    "sample_size": "160 households, 16 water supply systems",
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
    "service_area": "",
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
    "political_coordination": "",
    "bureaucratic_assistance": "TRUE",
    "formal_connection": "",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "",
    "service_reliability": "TRUE",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "TRUE",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "Tobit (censored linear) regression",
    "effect_estimate": "Household cash and labour contributions (CASHCONT, LABORCONT) positively and significantly affected by participation in project design/implementation, advocacy intensity, and household income. WUC-set tariffs ranged from ETB 0 to 6 per household per period; average annual contribution (~19% of estimated full O&M cost) was ETB 4,500/year across 85 users.",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "significant, exact values not fully extractable from PDF-to-text conversion",
    "extraction_sample_size": "160 households",
    "adjusted_or_unadjusted": "adjusted (Tobit regression)",
    "covariates": "participation in project design/implementation, advocacy intensity, household income, gender of household head, household responsibility perception",
    "model_type": "Tobit (censored) regression",
    "study_design": "quantitative household survey regression study",
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
        "High: Tobit regression finds household cash/labour contributions to WUC-managed "
        "water-system maintenance are significantly determined by participation in "
        "project design and implementation, advocacy intensity, and household income, "
        "with WUCs directly setting the tariff/contribution levels; current contributions "
        "cover only about 19% of estimated full operations-and-maintenance costs, "
        "indicating a direct institutional link between the WUC contribution mechanism "
        "and the continued functionality of the water supply system."
    ),
    "source_document": "Tigabu et al. (retrieved via Google Drive)",
    "page": "",
    "table": "",
    "figure": "",
    "section": "Results",
    "exact_location": "Section 3.2 and Tobit regression results",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/community-management "
        "mechanism study (WUC-set tariffs/participation) directly relevant to functional "
        "water-access continuity. NOT added to effect_sizes.csv: the Tobit regression's "
        "dependent variable is household contribution amount (a financing-sustainability "
        "measure), not a direct water-access outcome (connection, coverage, collection "
        "time, service continuity) per the strict Family A/B/C framework."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1086 -- Ranganathan 2014
r = blank_row(fieldnames)
r.update({
    "study_id": "S1086",
    "citation": "Ranganathan M (2014). Paying for Pipes, Claiming Citizenship: Political Agency and Water Reforms at the Urban Periphery. International Journal of Urban and Regional Research 38(2):590-608.",
    "doi": "10.1111/1468-2427.12028",
    "publication_year": "2014",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "Bommanahalli, peripheral Bangalore, Karnataka",
    "legal_system": "common law (India)",
    "urban_rural": "urban peri-urban periphery",
    "service_provider": "Bangalore Water Supply and Sewerage Board (BWSSB); Karnataka Urban Infrastructure Development and Finance Corporation",
    "regulatory_model": "Greater Bangalore water project, market-oriented 'beneficiary capital contribution' cost-recovery policy",
    "population": "'peripheralized middle class,' informally-tenured 'revenue layout' residents",
    "sample_size": "1,864 payment receipts (Bommanahalli ward); 50 KIIs; 44 semi-structured resident interviews",
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
    "hardship_exception": "",
    "administrative_review": "",
    "complaint": "TRUE",
    "judicial_review": "TRUE",
    "disconnection": "",
    "reconnection": "",
    "sanction": "",
    "participation": "TRUE",
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
    "affordability": "TRUE",
    "service_continuity": "",
    "application_success": "TRUE",
    "refusal": "",
    "delay_outcome": "TRUE",
    "effect_measure": "",
    "effect_estimate": "As a result of RWA lobbying and petitions, the water board waived the requirement of formal, permanent proof of tenure for a water connection and meter; proof of payment for water pipes alone was accepted as sufficient to demonstrate residence. One-time cash contributions averaged over $260/household (roughly one month's household income, at times up to 1.5 months'). 80% of Bangalore's outskirts still lacked access to piped water via the project several years after collections began.",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "1,864 payment receipts",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "mixed quantitative/ethnographic case study",
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
        "High: documents that as a direct result of resident welfare associations' "
        "political mobilization, Bangalore's water utility formally waived the "
        "requirement of proof of permanent land tenure for a water connection and meter, "
        "accepting proof of payment for water pipes alone as sufficient to demonstrate "
        "residence -- i.e., formal land tenure was successfully removed as an eligibility "
        "requirement for water-service delivery to informally-tenured 'revenue layout' "
        "households, in exchange for substantial capital-cost contributions (often "
        "exceeding one month's household income)."
    ),
    "source_document": "Ranganathan 2014 (retrieved via Google Drive)",
    "page": "590-608",
    "table": "Table 1",
    "figure": "",
    "section": "Payment, tenure and consent for cost recovery",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous legal/institutional mechanism study "
        "documenting a specific, named change to a formal water-connection eligibility "
        "requirement (tenure proof replaced by payment proof) for informally-tenured "
        "urban peripheral households. NOT added to effect_sizes.csv: the study reports a "
        "descriptive payment table and a cited secondary regression (World Bank 2005, not "
        "the author's own analysis, outcome = willingness to pay, not water access), not "
        "an original regression-based effect size on a water-access outcome."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1087 -- Chng 2012
r = blank_row(fieldnames)
r.update({
    "study_id": "S1087",
    "citation": "Chng NR (2012). Regulatory mobilization and service delivery at the edge of the regulatory state. Regulation & Governance.",
    "doi": "10.1111/j.1748-5991.2012.01137.x",
    "publication_year": "2012",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Philippines",
    "subnational_unit": "Metro Manila",
    "legal_system": "civil law (Philippines)",
    "urban_rural": "urban",
    "service_provider": "Metropolitan Waterworks and Sewerage System (MWSS); small-scale water providers (SSWPs)",
    "regulatory_model": "National Water Resources Board (NWRB) Certificate of Public Convenience (CPC) licensing framework",
    "population": "urban poor communities, Metro Manila",
    "sample_size": "extensive fieldwork (Philippines)",
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
    "documentation": "TRUE",
    "tenure": "",
    "property": "",
    "planning": "",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "TRUE",
    "procedural_steps": "TRUE",
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
    "service_reliability": "TRUE",
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
    "study_design": "fieldwork-based institutional/regulatory case study",
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
        "High: documents the NWRB's Certificate of Public Convenience (CPC) licensing "
        "framework governing small-scale water providers (SSWPs) operating at the 'edge "
        "of the regulatory state' following Metro Manila's 1997 water privatization, "
        "with only 223 CPCs issued by June 2000 and tariff rate adjustments capped at a "
        "12% return on investment, and how NGOs and community groups engaged in "
        "'regulatory mobilization' to influence these formal rules and secure water "
        "access for urban poor communities left underserved by the privatized utility."
    ),
    "source_document": "Chng 2012 (retrieved via Google Drive)",
    "page": "",
    "table": "",
    "figure": "",
    "section": "The NWRB and small-scale water providers; Regulatory mobilization",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/regulatory mechanism "
        "study directly examining formal licensing/tariff-regulation barriers and "
        "mobilization strategies affecting urban-poor water access. Qualitative fieldwork "
        "case study, no regression-based effect size; not added to effect_sizes.csv."
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
