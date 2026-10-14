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

# S1110 -- Mafuta, Zuwarimwe & Mwale 2021
r = blank_row(fieldnames)
r.update({
    "study_id": "S1110",
    "citation": "Mafuta W, Zuwarimwe J, Mwale M (2021). WASH Financial and Social Investment Dynamics in a Conflict-Arid District of Jariban in Somalia. Sustainability 13(9):4836.",
    "doi": "10.3390/su13094836",
    "publication_year": "2021",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Somalia",
    "subnational_unit": "Jariban district (19 villages)",
    "legal_system": "civil law (Somalia); collapsed central-state statistical/regulatory system since 1991",
    "urban_rural": "rural",
    "service_provider": "NGOs; diaspora community; community self-financing",
    "regulatory_model": "absence of functioning state WASH investment/regulatory capacity (failed-state governance)",
    "population": "vulnerable rural communities, Jariban district, Somalia",
    "sample_size": "19 villages; 38 focus group discussions",
    "household_level": "",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "",
    "migrant_population": "TRUE",
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
    "water_access": "TRUE",
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
    "effect_measure": "",
    "effect_estimate": (
        "WASH infrastructure financing sources in Jariban district: NGOs 54.3%, diaspora "
        "community 34.5%, community contributions 11.2%, state government investment near "
        "zero. Findings link this near-total absence of state investment (attributable to "
        "collapse of the central government/statistical system since 1991) to a WASH "
        "infrastructure backlog and low water/sanitation access."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "19 villages; 38 focus group discussions",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "mixed-methods case study (transect walks, focus group discussions, desktop review)",
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
        "High: quantifies WASH infrastructure financing-source shares (NGO/diaspora/"
        "community vs. near-zero state investment) and directly attributes this pattern to "
        "the collapse of Somalia's central-state statistical and regulatory capacity since "
        "1991, documenting a state-fragility institutional mechanism's effect on WASH "
        "infrastructure backlog and access."
    ),
    "source_document": "Mafuta, Zuwarimwe & Mwale 2021 (retrieved via Google Drive)",
    "page": "1-17",
    "table": "",
    "figure": "",
    "section": "Introduction; Methodology; Results",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous institutional/governance-failure case "
        "study directly documenting state fragility's effect on WASH access. No "
        "regression-based effect size; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1111 -- Faure, Faust & Kaminsky 2019
r = blank_row(fieldnames)
r.update({
    "study_id": "S1111",
    "citation": "Faure JC, Faust KM, Kaminsky J (2019). Legitimization of the Inclusion of Cultural Practices in the Planning of Water and Sanitation Services for Displaced Persons. Water 11(2):359.",
    "doi": "10.3390/w11020359",
    "publication_year": "2019",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Germany",
    "subnational_unit": "multiple cities (2015 asylum applications 4,230-54,324 per city)",
    "legal_system": "civil law (Germany); EU/German asylum administrative framework",
    "urban_rural": "urban",
    "service_provider": "German government agencies; aid organizations",
    "regulatory_model": "institutional response to the 2015-2016 refugee/asylum crisis; WASH facility planning for asylum-seeker accommodation",
    "population": "asylum seekers and refugees, Germany (2015-2016 crisis)",
    "sample_size": "28 semi-structured interviews",
    "household_level": "",
    "community_level": "TRUE",
    "income_group": "",
    "tenure_status": "",
    "legal_status": "TRUE",
    "indigenous_population": "",
    "migrant_population": "TRUE",
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
    "service_area": "",
    "fees": "",
    "procedural_steps": "",
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
    "institutional_fragmentation": "",
    "political_coordination": "TRUE",
    "bureaucratic_assistance": "TRUE",
    "formal_connection": "",
    "water_access": "TRUE",
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
    "effect_estimate": (
        "Qualitative thematic finding from 28 interviews: the institutional response to "
        "the 2015-2016 refugee crisis in Germany was predominantly reactive rather than "
        "proactive in accommodating cultural practices in WASH facility planning for "
        "asylum seekers; interviewees primarily invoked comprehensibility legitimacy "
        "(personal experience) and procedural legitimacy (moral considerations) to "
        "justify decisions."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "28 semi-structured interviews",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "qualitative institutional case study (semi-structured interviews, thematic/legitimacy analysis)",
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
        "Moderate-high: rigorous qualitative analysis of institutional decision-making and "
        "legitimation processes shaping WASH facility planning for a legally distinct, "
        "administratively processed population (asylum seekers) during an acute crisis "
        "period; documents institutional discretion and reactive administrative posture as "
        "mechanisms shaping service design."
    ),
    "source_document": "Faure, Faust & Kaminsky 2019 (retrieved via Google Drive)",
    "page": "1-20",
    "table": "",
    "figure": "",
    "section": "Introduction; Methods; Results",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous institutional/administrative-"
        "decision-making case study documenting how legitimacy-based discretion shapes "
        "WASH service design for asylum seekers. No regression-based effect size; not "
        "added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1112 -- Martinez Moscoso, Aguilar Feijo & Verdugo Silva 2018
r = blank_row(fieldnames)
r.update({
    "study_id": "S1112",
    "citation": "Martinez Moscoso A, Aguilar Feijo VG, Verdugo Silva T (2018). The Vital Minimum Amount of Drinking Water Required in Ecuador. Resources 7(1):15.",
    "doi": "10.3390/resources7010015",
    "publication_year": "2018",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Ecuador",
    "subnational_unit": "Cuenca, Gualaceo, Suscal (Azuay/Canar provinces)",
    "legal_system": "civil law (Ecuador); 2008 Constitution; Organic Law on Water Resources, Uses and Exploitation of Water",
    "urban_rural": "mixed (large city, intermediate city, small indigenous-majority city)",
    "service_provider": "municipal/public water utilities (ETAPA-Cuenca and equivalents), Drinking Water Boards",
    "regulatory_model": "SENAGUA Ministerial Agreements No. 2017-1522/1523 establishing a constitutionally-guaranteed minimum vital amount of raw water (200 L/capita/day) with cost-recovery charge for excess raw-water use",
    "population": "households, including extreme-poverty and indigenous-majority households, Cuenca/Gualaceo/Suscal, Ecuador",
    "sample_size": "3 municipalities; National Survey of Employment and Underemployment (Dec. 2016) data",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "TRUE",
    "migrant_population": "",
    "eligibility": "TRUE",
    "burden": "TRUE",
    "discretion_accommodation": "",
    "enforcement": "TRUE",
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
    "hardship_exception": "TRUE",
    "administrative_review": "",
    "complaint": "",
    "judicial_review": "TRUE",
    "disconnection": "",
    "reconnection": "",
    "sanction": "",
    "participation": "",
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
    "affordability": "TRUE",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "cross-municipality comparative formula-based calculation (not a regression model)",
    "effect_estimate": (
        "Impact of the raw-water-excess cost-recovery charge (USD $0.0039/m3 above the "
        "200 LPCPD minimum vital amount) on extreme-poverty households' income, by "
        "municipality: Cuenca (large, most efficient, 28.66% unaccounted-for water losses) "
        "IH = 0.31% of income; Gualaceo (small, intermediate, 51.78% losses) IH = 0.81%; "
        "Suscal (micro, indigenous-majority, highest losses/consumption) IH = 4.17%. "
        "Smaller, less-efficient, more-indigenous municipalities bear a disproportionately "
        "larger share of the legal cost-recovery burden."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "3 municipalities (Cuenca, Gualaceo, Suscal)",
    "adjusted_or_unadjusted": "unadjusted (formula-based comparative calculation across 3 units, not a regression model)",
    "covariates": "",
    "model_type": "formula-based comparative calculation (TAC, RWE, IH formulas)",
    "study_design": "doctrinal/normative/economic mixed-methods comparative case study",
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
        "High: directly isolates the differential effect of a specific legal cost-recovery "
        "provision (SENAGUA Ministerial Agreements 2017-1522/1523, raw-water-excess charge "
        "above the constitutionally guaranteed 200 LPCPD minimum) on extreme-poverty "
        "household income across three municipalities of varying size, efficiency and "
        "indigenous population share, using an original formula-based methodology applied "
        "to official survey data."
    ),
    "source_document": "Martinez Moscoso, Aguilar Feijo & Verdugo Silva 2018 (retrieved via Google Drive)",
    "page": "1-16",
    "table": "Table 2 (WHO service levels); Table 4 (excess consumption by municipality)",
    "figure": "Figure 4 (typical water consumption); Figure 5 (excess use of raw water)",
    "section": "Methodology; Results (5.1 Economic Analysis)",
    "exact_location": "Throughout, esp. Section 5.1.2 and Table 4",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous legal/institutional-mechanism case "
        "study with quantified cross-municipality comparative estimates. Not added to "
        "effect_sizes.csv: the IH percentages are formula-based comparative calculations "
        "across only 3 units, not a regression-based estimate with statistical inference, "
        "per ANALYSIS_PLAN.md S2/Family A-C eligibility criteria (parallel to Debbane & "
        "Keil 2004, S1101, Batch 222, not added despite quantitative percentages)."
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
