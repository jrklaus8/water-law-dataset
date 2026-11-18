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

# S1059 -- Massey 2014
r = blank_row(fieldnames)
r.update({
    "study_id": "S1059",
    "citation": "Massey RT (2014). Exploring counter-conduct in upgraded informal settlements: The case of women residents in Makhaza and New Rest (Cape Town), South Africa. Habitat International 44:290-296.",
    "doi": "10.1016/j.habitatint.2014.07.007",
    "publication_year": "2014",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "South Africa",
    "subnational_unit": "Makhaza and New Rest, Cape Town",
    "legal_system": "common law (South Africa)",
    "urban_rural": "urban",
    "service_provider": "municipal government (informal-settlement upgrading program)",
    "regulatory_model": "government informal-settlement upgrading program vs. resident counter-conduct (illegal connections)",
    "population": "women residents of upgraded informal settlements",
    "sample_size": "two case-study settlements (Makhaza, New Rest)",
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
    "administrative_review": "",
    "complaint": "",
    "judicial_review": "",
    "disconnection": "",
    "reconnection": "",
    "sanction": "TRUE",
    "participation": "TRUE",
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
    "study_design": "qualitative governmentality/counter-conduct case study (two informal settlements)",
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
        "Moderate: documents that government informal-settlement upgrading programs in "
        "Makhaza and New Rest, Cape Town failed to meet residents' actual housing and "
        "infrastructure needs, prompting the most prevalent form of resident 'counter-"
        "conduct' to be the establishment of illegal water and electricity connections, "
        "alongside backyard-shack construction and informal home-based businesses -- "
        "arising from conflicting governmentalities between residents and the "
        "state's upgrading institutions."
    ),
    "source_document": "Massey 2014 (retrieved via Google Drive)",
    "page": "290-296",
    "table": "",
    "figure": "",
    "section": "Findings on counter-conduct activities in Makhaza and New Rest",
    "exact_location": "Discussion of illegal water/electricity connections as counter-conduct",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: institutional/administrative mechanism "
        "(government upgrading-program design failing to meet needs) study with "
        "documented resident resort to illegal water-connection practices as an access "
        "outcome. Qualitative case study, no regression-based effect size; not added to "
        "effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1060 -- Acey 2010
r = blank_row(fieldnames)
r.update({
    "study_id": "S1060",
    "citation": "Acey C (2010). Gender and community mobilisation for urban water infrastructure investment in southern Nigeria. Gender & Development 18(1):11-26.",
    "doi": "10.1080/13552071003599970",
    "publication_year": "2010",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Nigeria",
    "subnational_unit": "Lagos; Benin City",
    "legal_system": "common law (Nigeria)",
    "urban_rural": "urban",
    "service_provider": "Lagos Water Corporation; informal water vendors; landlords",
    "regulatory_model": "voluntary-association-mediated citizen voice/exit/loyalty in response to water-service problems",
    "population": "women and men in poor urban communities, Lagos and Benin City",
    "sample_size": "783 household ethnographic surveys (18 neighborhoods) plus 4 semi-structured interviews",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "TRUE",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "TRUE",
    "eligibility": "",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
    "enforcement": "",
    "documentation": "TRUE",
    "tenure": "TRUE",
    "property": "TRUE",
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
    "complaint": "TRUE",
    "judicial_review": "",
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
    "service_coverage": "",
    "service_reliability": "TRUE",
    "service_quantity": "TRUE",
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
    "study_design": "mixed-methods household survey and interview study (exit-voice-loyalty framework)",
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
        "Moderate: finds women are generally unable to influence decision-making in the "
        "water sector through voluntary associations and are excluded from participation "
        "in the business of water supply and associated economic opportunities; "
        "male-dominated neighbourhood/community-development associations are linked to "
        "'exit' behavior (switching providers/self-provision) rather than civic engagement, "
        "while women's religious-association membership is linked to greater use of "
        "'voice' (complaint/protest); documents institutional/procedural barriers to formal "
        "complaint, including that tenants (disproportionately women) cannot complain "
        "directly to the water utility without property-ownership documentation held by "
        "the landlord."
    ),
    "source_document": "Acey 2010 (retrieved via Google Drive)",
    "page": "11-26",
    "table": "Table 1 (respondent demographics); Figure 2 (water-supply problems)",
    "figure": "Figure 2",
    "section": "Access and mobilisation; Women's responses to problems in the urban water sector",
    "exact_location": "Throughout, especially findings on voluntary-association membership and voice/exit patterns by gender",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: institutional/participatory mechanism "
        "(gendered exclusion from water-governance voice channels) study with documented "
        "differential water-access-improvement outcomes by gender. Descriptive survey "
        "statistics (e.g., 'twice as likely,' '18 times as likely'), not a formal "
        "regression model with reported coefficients/SEs; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1061 -- Hoque & Hoque 1994
r = blank_row(fieldnames)
r.update({
    "study_id": "S1061",
    "citation": "Hoque BA, Hoque MM (1994). Partnership in rural water supply and sanitation: a case study from Bangladesh. Health Policy and Planning 9(3):288-293.",
    "doi": "",
    "publication_year": "1994",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Bangladesh",
    "subnational_unit": "national (rural)",
    "legal_system": "common law (Bangladesh)",
    "urban_rural": "rural",
    "service_provider": "NGO Forum for Drinking Water Supply and Sanitation; 295 partner NGOs; Association of Development Agencies in Bangladesh (ADAB)",
    "regulatory_model": "multi-agency NGO/government partnership; community site-selection process",
    "population": "rural underserved/unserved population, Bangladesh",
    "sample_size": "192 families, 32 pump caretakers, 42 NGO trainers/field officers interviewed; ~100,000 people served",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "",
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
    "formal_connection": "TRUE",
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
    "study_design": "program evaluation case study (interviews with users, caretakers, trainers)",
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
        "Moderate: male users participated in the tubewell site-selection process at "
        "essentially all visited sites, while female users participated in the site-"
        "selection process at only 5 of the visited sites (15%); non-participating women "
        "reported they had simply never been asked by NGO fieldworkers to participate, "
        "despite reporting pride and empowerment where they were included. A documented "
        "institutional/administrative-participation mechanism with a gender-differentiated "
        "outcome directly shaping water/sanitation-facility siting decisions."
    ),
    "source_document": "Hoque & Hoque 1994 (retrieved via Google Drive)",
    "page": "288-293",
    "table": "Table 1 (training methods)",
    "figure": "",
    "section": "Community participation",
    "exact_location": "Community participation section on gendered site-selection participation",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: institutional/administrative-participation "
        "mechanism (NGO/government site-selection process) study with a documented gender-"
        "differentiated participation outcome. Descriptive program-evaluation statistics, "
        "no regression-based effect size; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1062 -- Marson & Savin 2015
r = blank_row(fieldnames)
r.update({
    "study_id": "S1062",
    "citation": "Marson M, Savin I (2015). Ensuring Sustainable Access to Drinking Water in Sub Saharan Africa: Conflict Between Financial and Social Objectives. World Development 76:26-39.",
    "doi": "10.1016/j.worlddev.2015.06.002",
    "publication_year": "2015",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "multi-country (22 Sub-Saharan African countries)",
    "subnational_unit": "utility-level (mostly urban reference areas)",
    "legal_system": "mixed (multi-country, Sub-Saharan Africa)",
    "urban_rural": "urban",
    "service_provider": "water utilities, Sub-Saharan Africa",
    "regulatory_model": "operation-and-maintenance cost-recovery ratio as a financial-regulatory policy mechanism",
    "population": "urban populations served by SSA water utilities",
    "sample_size": "225 observations, 22 countries, utility-level panel data 1995-2009",
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
    "effect_measure": "panel regression coefficients (pooled OLS, fixed effects, random effects)",
    "effect_estimate": "O&M cost-recovery ratio (cr): positive and significant coefficient on water-coverage change across all model specifications; squared cost-recovery term (cr^2): negative and significant coefficient of comparable magnitude, indicating a curvilinear (inverted-U) relationship -- coverage gains from cost recovery diminish and reverse beyond a threshold. Exact numeric coefficient/SE values in source Table 4 were not cleanly extractable from PDF-to-text conversion; direction and significance as stated are drawn from the paper's own reported results (Section 4).",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "significant (exact values not cleanly extractable from PDF conversion; paper states significant in all model specifications)",
    "extraction_sample_size": "225 observations, 22 countries",
    "adjusted_or_unadjusted": "adjusted (controls: initial coverage, public expenditure, Non-Revenue Water, ODA, regional dummies)",
    "covariates": "initial water coverage, public expenditure, Non-Revenue Water, Official Development Assistance, region dummy",
    "model_type": "panel regression: pooled OLS, fixed effects, random effects",
    "study_design": "quantitative panel-data econometric study",
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
        "High: rigorous panel-regression evidence (pooled OLS, fixed and random effects) "
        "directly isolates the effect of a financial/regulatory institutional mechanism "
        "(utility O&M cost-recovery policy) on water-coverage change, finding a "
        "significant curvilinear relationship in which a narrow focus on financial "
        "sustainability, beyond a threshold, diverts utility priorities away from "
        "expanding universal water access, consistent across all tested model "
        "specifications (22 SSA countries)."
    ),
    "source_document": "Marson & Savin 2015 (retrieved via Google Drive)",
    "page": "26-39",
    "table": "Table 4 (regression results)",
    "figure": "",
    "section": "4. Regression results",
    "exact_location": "Section 4, discussion of cost-recovery coefficient and its square",
    "extraction_note": (
        "INCLUDE and effect_sizes-eligible per INCLUSION_EXCLUSION.md and the strict "
        "Family A/B/C framework: a genuine panel-regression estimate directly isolates a "
        "financial/regulatory institutional mechanism's (cost-recovery policy) effect on "
        "a water-access outcome (coverage change), significant across all specifications. "
        "Added to effect_sizes.csv as S1062 (Family C). Note: precise numeric "
        "coefficient/SE values from source Table 4 could not be cleanly extracted from "
        "the PDF-to-text conversion (table structure garbled); direction and significance "
        "are drawn directly from the paper's own prose description of its results."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1063 -- van Koppen & Schreiner 2014
r = blank_row(fieldnames)
r.update({
    "study_id": "S1063",
    "citation": "van Koppen B, Schreiner B (2014). Priority General Authorisations in rights-based water use authorisation in South Africa. Water Policy 16(1):59-77.",
    "doi": "10.2166/wp.2014.110",
    "publication_year": "2014",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "South Africa",
    "subnational_unit": "national, with Sub-Saharan African comparative context",
    "legal_system": "civil law (South Africa, continental European licence/permit tradition)",
    "urban_rural": "both",
    "service_provider": "national/provincial water-licensing authorities",
    "regulatory_model": "statutory water-use licence (permit) system under the National Water Act 1998; proposed Priority General Authorisations reform",
    "population": "small-scale, predominantly poor and Black water users, South Africa and Sub-Saharan Africa",
    "sample_size": "legal/policy-text analysis (National Water Act 1998, National Water Resource Strategy-2 2013)",
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
    "documentation": "TRUE",
    "tenure": "TRUE",
    "property": "TRUE",
    "planning": "TRUE",
    "zoning": "",
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "",
    "procedural_steps": "TRUE",
    "delay": "TRUE",
    "discretion": "TRUE",
    "hardship_exception": "TRUE",
    "administrative_review": "TRUE",
    "complaint": "",
    "judicial_review": "",
    "disconnection": "",
    "reconnection": "",
    "sanction": "",
    "participation": "",
    "institutional_fragmentation": "TRUE",
    "political_coordination": "",
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "",
    "service_reliability": "",
    "service_quantity": "TRUE",
    "service_quality": "",
    "affordability": "",
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
    "study_design": "statutory/legal-policy analysis",
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
        "High: rigorous statutory-law analysis identifies three specific forms of legal "
        "injustice for small-scale (typically poor, Black) water users under South "
        "Africa's licence-based statutory water law: (1) reinforcement of historical "
        "colonial-era capture of water-resource ownership undermining customary water "
        "law; (2) administrative discrimination arising from government licensing-"
        "capacity constraints disproportionately burdening the large numbers of small-"
        "scale applicants; and (3) a 'second-class' water entitlement for the smallest-"
        "scale users, who are exempted from the licence-application requirement "
        "altogether and thereby relegated to an insecure, unenforceable entitlement. "
        "Proposes Priority General Authorisations as a transformative legal reform tool "
        "to equalize access to minimum water quantities."
    ),
    "source_document": "van Koppen & Schreiner 2014 (retrieved via Google Drive)",
    "page": "59-77",
    "table": "",
    "figure": "",
    "section": "Three forms of injustice in statutory water law; Priority General Authorisations proposal",
    "exact_location": "Throughout, especially the analysis of the three forms of injustice",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous statutory-law analysis directly "
        "documenting a legal/institutional water-use-licensing mechanism's differential "
        "access effects on poor and historically marginalized users, with a proposed "
        "legal reform. Legal/policy-text analysis, no regression-based effect size; not "
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
