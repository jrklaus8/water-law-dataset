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

# S1145 -- Gopakumar 2012
r = blank_row(fieldnames)
r.update({
    "study_id": "S1145",
    "citation": "Gopakumar G (2012). Transforming Urban Water Supplies in India: The role of reform and partnerships in globalization. Routledge Contemporary South Asia Series. London: Routledge.",
    "doi": "",
    "publication_year": "2012",
    "publication_type": "book",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "India",
    "subnational_unit": "Bangalore, Chennai, Kochi",
    "legal_system": "common law; Indian municipal/state water-board governance framework",
    "urban_rural": "urban",
    "service_provider": "Bangalore Water Supply and Sewerage Board (BWSSB), Chennai Metropolitan Water Supply and Sewerage Board (Metrowater), Kerala Water Authority (KWA)",
    "regulatory_model": "public-private-partnership-driven water-supply reform; comparative institutional case study across three metropolitan cities",
    "population": "urban residents, including slum-dweller federations and village/neighborhood water-supply committees, Bangalore/Chennai/Kochi",
    "sample_size": "comparative institutional case study, 3 Indian metropolitan cities",
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
    "building_permit": "",
    "service_area": "TRUE",
    "fees": "TRUE",
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
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "qualitative comparative institutional case study (no regression-based effect estimate)",
    "effect_estimate": (
        "Qualitative comparative case study of water-supply reform politics across Bangalore, Chennai, "
        "and Kochi, examining how public-private-partnership-driven reform processes reshape "
        "state-society relations governing water-supply access at state, city, and neighborhood "
        "levels. Documents specific institutional actors and mechanisms -- municipal water boards, "
        "slum-dweller federations (e.g., Karnataka Slum Dwellers Federation), village/neighborhood "
        "water-supply committees, community-based organizations -- and how reform-era institutional "
        "arrangements condition differential household access to water-supply infrastructure and "
        "services across formal and informal settlement contexts."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "3 Indian metropolitan cities (Bangalore, Chennai, Kochi)",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "qualitative comparative institutional case study",
    "study_design": "qualitative institutional/governance-reform case study",
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
        "Moderate-high: detailed institutional case study documenting reform-era water-supply "
        "governance arrangements and their effect on access across three Indian metropolitan cities, "
        "though primarily descriptive/political-economy analysis rather than a designed comparison "
        "isolating a single mechanism's effect."
    ),
    "source_document": "Gopakumar 2012 (retrieved via Google Drive)",
    "page": "book-length",
    "table": "",
    "figure": "",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine qualitative institutional-mechanism case study "
        "of water-supply governance reform (PPP-driven) affecting household/neighborhood access "
        "across three Indian cities. Qualitative only; no effect_sizes.csv entry."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1146 -- Breen & Gillanders 2024
r = blank_row(fieldnames)
r.update({
    "study_id": "S1146",
    "citation": "Breen M, Gillanders R (2024). Money down the drain: Corruption and water service quality in Africa. Governance 37(1):119-135.",
    "doi": "10.1111/gove.12753",
    "publication_year": "2024",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "multi-country (Africa, Afrobarometer round 7 sample)",
    "subnational_unit": "sub-national regions across Afrobarometer-surveyed African countries",
    "legal_system": "mixed (multi-country)",
    "urban_rural": "mixed (urban and rural, coded)",
    "service_provider": "national/regional water utilities",
    "regulatory_model": "utilities-sector corruption as an administrative/institutional barrier to service access",
    "population": "households, Afrobarometer round 7 respondents",
    "sample_size": "N = 44,778 (ordered probit model, Table 3)",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "",
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
    "sanction": "",
    "participation": "",
    "institutional_fragmentation": "",
    "political_coordination": "",
    "bureaucratic_assistance": "",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "TRUE",
    "service_reliability": "TRUE",
    "service_quantity": "TRUE",
    "service_quality": "TRUE",
    "affordability": "",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "Probit / ordered probit regression, marginal effects (region-clustered standard errors, country fixed effects)",
    "effect_estimate": (
        "Table 2 (probit models): regional incidence of utilities-sector corruption has a "
        "statistically significant negative marginal effect on the likelihood a household reports "
        "access to enough clean water, robust to controlling for individual bribery experience "
        "(Column 3). Presence of a piped water system increases access likelihood by 4%; urban "
        "location by 2%. Magnitude: a household in the most-corrupt sampled area is approximately "
        "10% less likely to report adequate clean-water access than one in the 'cleanest' area; a "
        "one-standard-deviation increase in corruption is associated with an approximate 0.5% drop "
        "in reported access likelihood. Table 3 (ordered probit, N=44,778, country fixed effects) "
        "confirms the direction and significance of the relationship. Table 4 extends the analysis "
        "to the location of water infrastructure itself as an outcome, finding a related corruption "
        "association."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "clustered by region (Tables 2-4)",
    "p_value": "statistically significant, exact p-values in Table 2 (main text does not restate table values in prose)",
    "extraction_sample_size": "N = 44,778 (Table 3, ordered probit)",
    "adjusted_or_unadjusted": "adjusted (controls for piped-water-system presence, urban location, gender, individual bribery experience, country fixed effects)",
    "covariates": "piped water system presence, urban/rural location, gender, wealth/poverty, individual bribery experience, country fixed effects",
    "model_type": "probit / ordered probit regression",
    "study_design": "quantitative regression-based institutional/administrative-barrier study",
    "risk_of_bias_tool": "ROBINS-I",
    "risk_of_bias_rating": "",
    "selection_bias": "",
    "measurement_bias": "",
    "confounding": "",
    "attrition": "",
    "reporting_bias": "",
    "legal_measurement_quality": "1",
    "outcome_measurement_quality": "1",
    "mechanism_certainty": (
        "High: rigorous large-N probit/ordered-probit regression analysis with country fixed effects "
        "and region-clustered standard errors, directly isolating a corruption-based administrative "
        "mechanism's effect on differential household water access across Africa, with a robustness "
        "check (individual bribery experience) and a meaningful, clearly stated effect magnitude."
    ),
    "source_document": "Breen & Gillanders 2024 (retrieved via Google Drive)",
    "page": "119-135",
    "table": "Tables 2, 3, 4",
    "figure": "Figure A1 (appendix)",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous regression-based institutional/administrative-"
        "barrier study directly isolating a corruption mechanism's effect on differential household "
        "water access. Added to effect_sizes.csv as Family C (administrative/legal barriers and "
        "access inequality)."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1147 -- Romero 2022
r = blank_row(fieldnames)
r.update({
    "study_id": "S1147",
    "citation": "Romero CM (2022). Manejo privado y publico de los sistemas de abastecimiento urbano de agua y saneamiento: De la privatizacion a la remunicipalizacion [Private and public management of urban water supply and sanitation systems: From privatization to remunicipalisation]. Ingenieria y Competitividad 24(1):e30611042.",
    "doi": "10.25100/iyc.v24i1.11042",
    "publication_year": "2022",
    "publication_type": "journal article",
    "language": "Spanish",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Colombia",
    "subnational_unit": "Barranquilla, Bogota, Medellin, Cartagena, Pereira, Cali (EMCALI), Medellin (EPM)",
    "legal_system": "civil law; Colombian municipal/national public-utility regulatory framework",
    "urban_rural": "urban",
    "service_provider": "concession-era private acueductos; INSFOPAL (1950-1986); post-1986 decentralized municipal utilities (EMCALI, EPM)",
    "regulatory_model": "historical institutional shift: private concession contracts -> national public institute (INSFOPAL) -> decentralized municipal/mixed-ownership utilities",
    "population": "urban water/sanitation service users, Colombia, 1880-present",
    "sample_size": "institutional/regulatory history case study, multiple Colombian cities",
    "household_level": "",
    "community_level": "TRUE",
    "income_group": "low-income (documented investment-risk barrier)",
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
    "property": "TRUE",
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
    "affordability": "TRUE",
    "service_continuity": "",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "qualitative institutional/regulatory history (no regression-based effect estimate)",
    "effect_estimate": (
        "Qualitative institutional history documenting Colombia's water/sanitation service-provision "
        "regulatory model over time: private concession contracts in major cities (Barranquilla 1880, "
        "Bogota 1886, Medellin 1891, Cartagena 1905, Pereira 1918); creation of the national public "
        "institute INSFOPAL (Decree 289 of 1950) consolidating municipal water/sanitation companies "
        "under state provision; INSFOPAL's 1986 liquidation (Law 12 of 1986) on grounds of "
        "insufficient capacity to extend infrastructure, followed by decentralization transferring "
        "utilities to departments/municipalities and incentivizing private capital investment. "
        "Documents structural barriers to private investment in extending connections to poorer "
        "customers with low payment capacity, as a driver of the privatization-to-remunicipalisation "
        "cycle."
    ),
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "institutional history, multiple Colombian cities, 1880-present",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "qualitative institutional/regulatory history",
    "study_design": "qualitative institutional/legal-history case study",
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
        "Moderate: documented institutional/regulatory history of Colombia's water-service provision "
        "model shifts and their stated relationship to service-extension outcomes, though primarily "
        "descriptive/historical rather than a designed comparison isolating a single mechanism's "
        "effect."
    ),
    "source_document": "Romero 2022 (retrieved via Google Drive)",
    "page": "1-26",
    "table": "",
    "figure": "",
    "section": "Throughout",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/legal-history case study of "
        "water-service provision regulatory-model shifts (privatization/remunicipalisation) in "
        "Colombia. Qualitative only; no effect_sizes.csv entry."
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
