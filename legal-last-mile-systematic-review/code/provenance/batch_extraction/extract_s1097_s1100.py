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

# S1097 -- Botton & de Gouvello 2008
r = blank_row(fieldnames)
r.update({
    "study_id": "S1097",
    "citation": "Botton S, de Gouvello B (2008). Water and sanitation in the Buenos Aires metropolitan region: Fragmented markets, splintering effects? Geoforum 39(6):1859-1870.",
    "doi": "",
    "publication_year": "2008",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Argentina",
    "subnational_unit": "Buenos Aires metropolitan region (BAMR)",
    "legal_system": "civil law (Argentina)",
    "urban_rural": "urban",
    "service_provider": "Aguas Argentinas S.A. (AASA); multiple independent municipal/provincial providers",
    "regulatory_model": "ETOSS (AASA concession area regulator); ORAB (remainder of BAMR regulator)",
    "population": "non-connected and informally-connected urban residents, Buenos Aires metropolitan region",
    "sample_size": "",
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
    "sanction": "TRUE",
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
    "study_design": "institutional/regulatory comparative case study",
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
        "High: documents that ETOSS's AASA concession agreement designated AASA as the "
        "sole authorized water/sanitation provider within its service area and required "
        "existing private wells to be blocked up during network expansion, foreclosing "
        "informal alternatives, while ORAB (regulating the rest of the metropolitan "
        "region) tolerates private wells, illegal connections, and 'desvinculados' "
        "informal collective networks -- the latter later granted formal institutional "
        "recognition via provincial decree 878/2003 -- producing starkly differentiated "
        "formal and informal access opportunities for non-connected users depending on "
        "which regulatory jurisdiction they fall under."
    ),
    "source_document": "Botton & de Gouvello 2008 (retrieved via Google Drive)",
    "page": "1859-1870",
    "table": "",
    "figure": "",
    "section": "Institutional fragmentation and access to services",
    "exact_location": "Sections 3-4",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous institutional/regulatory-"
        "fragmentation mechanism study directly documenting how differing regulatory "
        "frameworks produce differentiated formal/informal water-access opportunities. "
        "No regression-based effect size; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1098 -- Whittington 2003
r = blank_row(fieldnames)
r.update({
    "study_id": "S1098",
    "citation": "Whittington D (2003). Municipal water pricing and tariff design: a reform agenda for South Asia. Water Policy 5(1):61-76.",
    "doi": "10.2166/wp.2003.0003",
    "publication_year": "2003",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "South Asia (regional)",
    "subnational_unit": "multiple South Asian cities",
    "legal_system": "mixed (South Asia)",
    "urban_rural": "urban",
    "service_provider": "municipal water utilities, South Asia",
    "regulatory_model": "tariff and connection-policy reform agenda",
    "population": "unconnected poor households, South Asian cities",
    "sample_size": "",
    "household_level": "TRUE",
    "community_level": "",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "TRUE",
    "indigenous_population": "",
    "migrant_population": "",
    "eligibility": "TRUE",
    "burden": "TRUE",
    "discretion_accommodation": "TRUE",
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
    "hardship_exception": "TRUE",
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
    "service_reliability": "",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "",
    "application_success": "TRUE",
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
    "study_design": "policy-reform analysis",
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
        "High: finds current South Asian municipal water tariffs are 'not helping the "
        "majority of the poor households, many of whom are not connected to the piped "
        "distribution system,' and prescribes specific institutional/legal reforms: "
        "guaranteeing poor households a private connection when wanted, subsidizing "
        "upfront connection costs rather than volumetric use, providing public taps as a "
        "last-resort source, legalizing water vending and neighbor-to-neighbor selling, "
        "and prohibiting exclusive service-area rights for private operators -- directly "
        "targeting connection-eligibility and legal-status barriers to formal access."
    ),
    "source_document": "Whittington 2003 (retrieved via Google Drive)",
    "page": "61-76",
    "table": "",
    "figure": "",
    "section": "Pro-poor policy recommendations",
    "exact_location": "Abstract and throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous institutional/legal-mechanism "
        "policy analysis directly targeting connection-eligibility and legal-status "
        "barriers to formal water access for the poor. Policy-reform analysis paper, no "
        "regression-based effect size; not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1099 -- Adubofour, Obiri-Danso & Quansah 2013
r = blank_row(fieldnames)
r.update({
    "study_id": "S1099",
    "citation": "Adubofour K, Obiri-Danso K, Quansah C (2013). Sanitation survey of two urban slum Muslim communities in the Kumasi metropolis, Ghana. Environment and Urbanization 25(1):189-207.",
    "doi": "10.1177/0956247812468255",
    "publication_year": "2013",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Ghana",
    "subnational_unit": "Aboabo and Asawase, Asawase constituency, Kumasi",
    "legal_system": "common law (Ghana)",
    "urban_rural": "urban",
    "service_provider": "Ghana Water Company Limited",
    "regulatory_model": "block tariff structure (nationally set); informal legal status of slum settlements",
    "population": "urban slum Muslim residents, Kumasi",
    "sample_size": "331 households (Aboabo), 457 households (Asawase); 33 key-informant interviews",
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
    "service_reliability": "TRUE",
    "service_quantity": "",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "",
    "application_success": "",
    "refusal": "TRUE",
    "delay_outcome": "",
    "effect_measure": "descriptive survey statistics",
    "effect_estimate": "Total improved water coverage 94% (Aboabo) and 92% (Asawase), but many households not legally connected due to low income; informal water purchase from neighbors costs US$3.45-3.83/m3 vs. official block tariff of 35.86 cents/m3 (10-11x markup). Total improved toilet coverage only 7% (Aboabo) and 3% (Asawase); 58% of households use public toilets or open defecation, at 13.7 cents/adult use.",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "788 households total",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "quantitative household survey with key-informant interviews and transect walks",
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
        "High: documents that these slum settlements are 'classified as illegal by city "
        "authorities,' and that many households using pipe-borne water 'were not legally "
        "connected to a private tap at the household level because of low income levels,' "
        "relying instead on illegal tap connections or purchasing water from neighbors at "
        "10-11 times the official tariff rate; also documents landlords preventing on-"
        "plot latrine construction and a 'pay-to-dump' solid-waste fee scheme that "
        "low-income households evade through illegal dumping."
    ),
    "source_document": "Adubofour, Obiri-Danso & Quansah 2013 (retrieved via Google Drive)",
    "page": "189-207",
    "table": "Table 2-5",
    "figure": "Figures 2-8",
    "section": "Results and Discussion",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: rigorous quantitative survey directly "
        "documenting legal-status-based exclusion from formal water connections and "
        "specific fee/landlord barriers to sanitation access for the urban poor. "
        "Descriptive survey statistics and Spearman correlation (unrelated to access "
        "mechanism), no regression-based effect size on an access-eligibility outcome; "
        "not added to effect_sizes.csv."
    ),
    "researcher": RESEARCHER,
    "date_extracted": DATE,
    "evidence_status": "OBSERVED",
})
new_rows.append(r)

# S1100 -- Willis, Pearce, McCarthy, Ryan & Wadham 2008
r = blank_row(fieldnames)
r.update({
    "study_id": "S1100",
    "citation": "Willis E, Pearce M, McCarthy C, Ryan F, Wadham B (2008). Indigenous Responses to Water Policymaking in Australia. Development 51(3):418-424.",
    "doi": "10.1057/dev.2008.30",
    "publication_year": "2008",
    "publication_type": "journal article",
    "language": "English",
    "database_source": "",
    "peer_reviewed": "TRUE",
    "country": "Australia",
    "subnational_unit": "Yarilena, west of Ceduna, South Australia",
    "legal_system": "common law (Australia)",
    "urban_rural": "rural remote",
    "service_provider": "SA Water; District Council of Ceduna",
    "regulatory_model": "National Water Initiative (NWI) Agreement, full-cost-recovery clause (66(v))",
    "population": "Aboriginal homeland community, Yarilena",
    "sample_size": "population of 57, 15 households",
    "household_level": "TRUE",
    "community_level": "TRUE",
    "income_group": "TRUE",
    "tenure_status": "",
    "legal_status": "",
    "indigenous_population": "TRUE",
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
    "procedural_steps": "",
    "delay": "",
    "discretion": "",
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
    "bureaucratic_assistance": "TRUE",
    "formal_connection": "TRUE",
    "water_access": "TRUE",
    "sanitation_access": "",
    "service_coverage": "",
    "service_reliability": "TRUE",
    "service_quantity": "TRUE",
    "service_quality": "",
    "affordability": "TRUE",
    "service_continuity": "TRUE",
    "application_success": "",
    "refusal": "",
    "delay_outcome": "",
    "effect_measure": "",
    "effect_estimate": "Tiered water pricing: US$0.44/kL for first 125kL, then $1.03/kL thereafter, billed as a single bulk connection despite serving 15 separate households -- meaning the community quickly exceeds the low-rate threshold and is charged at the higher rate. Average daily per capita water use 209 L/d, below metropolitan Adelaide (268 L/d) and SA country towns (220 L/d). A 57% discrepancy between mains and household meter readings was traced to leaks from piping incompatible with mains pressure.",
    "lower_CI": "",
    "upper_CI": "",
    "standard_error": "",
    "p_value": "",
    "extraction_sample_size": "15 households, 57 residents",
    "adjusted_or_unadjusted": "",
    "covariates": "",
    "model_type": "",
    "study_design": "institutional case study",
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
        "High: documents that the National Water Initiative's full-cost-recovery tariff "
        "clause (66(v)) is applied to Yarilena as a single bulk-billed connection despite "
        "serving 15 separate households, causing the community to quickly exceed the "
        "lower-rate threshold (125kL) and be charged at the higher per-kilolitre rate; "
        "the community responded through internal cost-sharing arrangements (each "
        "household paying a fixed weekly amount via rent deduction) and self-funded "
        "infrastructure repairs (pressure-reducing valves, corrosion-resistant fittings) "
        "to manage the burden of this national tariff policy applied without adjustment "
        "for its collective, multi-household connection structure."
    ),
    "source_document": "Willis et al. 2008 (retrieved via Google Drive)",
    "page": "418-424",
    "table": "",
    "figure": "",
    "section": "Water use at Yarilena; Community capacity to deal with infrastructure breakdown",
    "exact_location": "Throughout",
    "extraction_note": (
        "INCLUDE per INCLUSION_EXCLUSION.md: genuine institutional/legal mechanism study "
        "directly examining how a national water-policy tariff and cost-recovery "
        "framework applies to and burdens an Indigenous community's collective water "
        "access. Institutional case study, no regression-based effect size; not added to "
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
