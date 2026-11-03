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

# S1143 -- Jones, Greenberg, Kaufman & Drew 1978
r = blank_row(fieldnames)
r.update({
    "study_id": "S1143",
    "citation": "Jones BD, Greenberg SR, Kaufman C, Drew J (1978). Service Delivery Rules and the Distribution of Local Government Services: Three Detroit Bureaucracies. The Journal of Politics 40(2):332-368.",
    "doi": "",
    "publication_year": "1978",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "United States",
    "subnational_unit": "City of Detroit, Michigan (420 census tracts)",
    "legal_system": "common law; US municipal administrative law",
    "urban_rural": "urban",
    "service_provider": "City of Detroit Environmental Protection and Maintenance Department (Sanitation Division, Environmental Enforcement Division), Department of Parks and Recreation",
    "regulatory_model": "administrative service-delivery rules (garbage-collection route allocation by 'weight rule' plus explicit center-city equity supplement)",
    "population": "Detroit residents, by census tract, 1973",
    "sample_size": "1,300 sanitation routes / 260 sections mapped to 420 census tracts; July and October 1973 data",
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
    "procedural_steps": "TRUE",
    "delay": "",
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
    "formal_connection": "",
    "water_access": "",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "service_quantity": "TRUE",
    "service_quality": "",
    "affordability": "",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "OLS regression / Pearson correlation coefficients",
    "effect_estimate": (
        "Table 6/7: the explicit 'weight rule' (routes allocated by garbage tonnage generated) "
        "produces a strong correlation between resource allocation and garbage collected per "
        "person (r=.842 for routes-per-1000-persons; r=.699 for man-hours-per-1000-persons; "
        "the two resource-allocation measures intercorrelate r=.849). Garbage generated per "
        "person is itself significantly higher in neighborhoods with greater distance from the "
        "central business district (higher social well-being) and higher proportion of white "
        "residents (Table 6 regression, independent effects). When the weight-rule effect is "
        "controlled (Table 7 regression of routes/man-hours per 1000 persons on garbage per "
        "person, distance from CBD, percent black), distance from CBD is significantly and "
        "negatively related to resource allocation (percent black not significant), indicating "
        "the Division's explicit supplementary 'center-city' equity rule allocates additional "
        "resources to the less-well-off inner city beyond what the weight rule alone would "
        "produce -- resulting in an overall U-shaped distributional curve (both poorer and "
        "wealthier neighborhoods receive more sanitation resources than middle-well-being "
        "neighborhoods). Comparable regression analyses (Tables 1-3) for the Environmental "
        "Enforcement Division found field pickups and violations driven primarily by citizen "
        "complaints, with residual differential (more field pickups/reinvestigations) favoring "
        "better-off, lower-housing-age-decline neighborhoods."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "coefficients reported as significant/not significant per regression table (Tables 1,2,3,6,7)",
    "extraction_sample_size": "420 Detroit census tracts, July/October 1973",
    "adjusted_or_unadjusted": "adjusted (OLS regressions control for demographic covariates: housing age/distance from CBD, percent black)",
    "covariates": "distance from central business district (social well-being proxy), percent black, garbage generated per person",
    "model_type": "OLS regression",
    "study_design": "quantitative regression-based institutional/administrative-mechanism study",
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
        "High: rigorous, multi-table OLS-regression analysis directly isolating explicit "
        "administrative service-delivery rules (the sanitation 'weight rule' and its "
        "center-city equity supplement) as the mechanism producing differential sanitation-"
        "resource allocation and service distribution across Detroit neighborhoods by social "
        "well-being and race."
    ),
    "source_document": "Jones, Greenberg, Kaufman & Drew 1978 (retrieved via Google Drive)",
    "page": "332-368",
    "table": "Tables 1, 2, 3, 6, 7",
    "figure": "Figures 1-3",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous regression-based institutional/"
        "administrative-mechanism study directly isolating explicit service-delivery rules' "
        "effect on differential sanitation-service resource distribution. Added to "
        "effect_sizes.csv as Family C (administrative/legal barriers and access inequality)."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1144 -- Tukahirwa 2011
r = blank_row(fieldnames)
r.update({
    "study_id": "S1144",
    "citation": "Tukahirwa JT (2011). Civil society in urban sanitation and solid waste management: The role of NGOs and CBOs in metropolises of East Africa. Doctoral thesis, Wageningen University. Chapter 3 published as Tukahirwa JT, Mol APJ, Oosterveer P (2011), Access of urban poor to NGO/CBO-supplied sanitation and solid waste services in Uganda: The role of social proximity, Habitat International 35:582-591.",
    "doi": "10.1016/j.habitatint.2011.03.005",
    "publication_year": "2011",
    "publication_type": "journal article (thesis chapter)",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Uganda",
    "subnational_unit": "12 poor informal settlements, Kampala",
    "legal_system": "common law; Uganda decentralized municipal governance framework",
    "urban_rural": "urban",
    "service_provider": "NGOs and CBOs supplying sanitation/solid-waste services in slum settlements",
    "regulatory_model": "NGO/CBO social-network/trust-based service access (non-state administrative-assistance mechanism)",
    "population": "urban poor households in Kampala informal settlements",
    "sample_size": "192 households (NGO sanitation-access model), 189 households (CBO sanitation-access model)",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "low-income",
    "tenure_status": "informal settlement",
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
    "institutional_fragmentation": "TRUE",
    "political_coordination": "",
    "bureaucratic_assistance": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "",
    "sanitation_access": "TRUE",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "service_quantity": "",
    "service_quality": "TRUE",
    "affordability": "TRUE",
    "service_continuity": "",
    "application_success": "TRUE",
    "refusal": "TRUE",
    "delay_outcome": "",
    "effect_measure": "Logit regression, coefficients and marginal effects (robust standard errors)",
    "effect_estimate": (
        "Table 3.6: logit models of access to NGO-supplied (n=192) and CBO-supplied (n=189) "
        "sanitation services in Kampala slums. Social-proximity trust is the strongest and "
        "most significant predictor for both models: NGO access coefficient 7.014 (robust SE "
        "1.352, p<0.01), marginal effect 1.010; CBO access coefficient 9.029 (robust SE 1.706, "
        "p<0.01), marginal effect 0.173 -- far exceeding the marginal effects of spatial "
        "proximity, perception (attitude/competence), and socio-economic (education, income) "
        "factors. Distance to toilet significantly negative for NGO access (coefficient -4.390, "
        "SE 1.744, p<0.01, marginal effect -0.632) but not significant for CBO access. Model "
        "fit: NGO model pseudo R2=0.4381 (Wald chi2(10)=192, p<0.001); CBO model pseudo "
        "R2=0.2631 (Wald chi2(10)=47.38, p<0.001)."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "1.352 (NGO trust coefficient); 1.706 (CBO trust coefficient); robust standard errors throughout (Table 3.6)",
    "p_value": "p<0.01 for trust in both NGO and CBO models (Table 3.6)",
    "extraction_sample_size": "192 households (NGO model), 189 households (CBO model), Kampala slums",
    "adjusted_or_unadjusted": "adjusted (controls for age, gender, competence, attitude, education, income, spatial-proximity distance measures)",
    "covariates": "age, gender, competence, attitude, education, income, distance to office, distance to toilet",
    "model_type": "logit regression",
    "study_design": "quantitative regression-based institutional/administrative-assistance-mechanism study",
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
        "High: rigorous logit-regression analysis with robust standard errors directly "
        "isolating a social-proximity/trust-based access mechanism's effect on differential "
        "urban-poor household access to NGO/CBO-supplied sanitation services in Kampala slums, "
        "with a large, highly significant, and dominant marginal effect relative to competing "
        "explanatory factors."
    ),
    "source_document": "Tukahirwa 2011 (retrieved via Google Drive)",
    "page": "38-59 (thesis); 582-591 (journal version)",
    "table": "Table 3.6",
    "figure": "",
    "section": "Chapter 3",
    "exact_location": "Chapter 3, Section 3.4.2",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous regression-based institutional/"
        "administrative-assistance-mechanism study directly isolating a social-network/trust "
        "access mechanism's effect on differential sanitation-service access among the urban "
        "poor. Added to effect_sizes.csv as Family B (administrative assistance/access)."
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
