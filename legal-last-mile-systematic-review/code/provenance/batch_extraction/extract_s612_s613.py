#!/usr/bin/env python3
import csv, os, tempfile

DB = "03_extraction/extracted_data/extraction_database.csv"
RESEARCHER = "Claude-AI-fulltext-2026-09-21"
DATE = "2026-09-22"


def blank_row(fieldnames):
    return {f: "" for f in fieldnames}


def main():
    with open(DB, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    existing_ids = {r["study_id"] for r in rows}
    new_rows = []

    # S612: Chapman et al. 2020, Gressier Haiti
    r = blank_row(fieldnames)
    r.update({
        "study_id": "S612",
        "citation": "Chapman KS, Merceron A, Myers NC, Wood EA (2020). Women's lived-experiences of water infrastructure in Gressier, Haiti. Water International 45(7-8):901-920.",
        "doi": "10.1080/02508060.2020.1839836",
        "publication_year": "2020",
        "publication_type": "journal article",
        "language": "English",
        "peer_reviewed": "TRUE",
        "country": "Haiti",
        "subnational_unit": "Gressier commune, Ouest department (population 36,000-75,000)",
        "legal_system": "civil law",
        "urban_rural": "peri-urban",
        "service_provider": "Informal neighbor-to-neighbor pipe networks; community-managed pumps/springs/kiosks; DINEPA (national water/sanitation directorate); NGOs (Haiti Outreach, Respire Haiti, Christianville)",
        "regulatory_model": "Largely informal/unregulated -- no accessible government records of existing water infrastructure; DINEPA and international NGO/relief-agency presence is the nominal but largely absent formal regulatory authority",
        "population": "Women aged 16+ residing in Gressier with knowledge of household water situation",
        "sample_size": "32 in-depth follow-up interviews, drawn from a 304-participant larger study population (66 eligible key informants identified via a cultural-consensus instrument, 32 of whom agreed to participate)",
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
        "documentation": "TRUE",
        "tenure": "TRUE",
        "property": "TRUE",
        "planning": "",
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
        "judicial_review": "",
        "disconnection": "TRUE",
        "reconnection": "",
        "sanction": "",
        "participation": "TRUE",
        "institutional_fragmentation": "TRUE",
        "political_coordination": "",
        "bureaucratic_assistance": "",
        "formal_connection": "TRUE",
        "water_access": "TRUE",
        "sanitation_access": "",
        "service_coverage": "TRUE",
        "service_reliability": "TRUE",
        "service_quantity": "TRUE",
        "service_quality": "TRUE",
        "affordability": "TRUE",
        "service_continuity": "TRUE",
        "application_success": "",
        "refusal": "TRUE",
        "delay_outcome": "TRUE",
        "effect_measure": "Qualitative thematic coding (NVivo) of semi-structured interviews; descriptive statistic cited (40% monthly service-restriction rate for non-payment), no regression",
        "effect_estimate": "An estimated 40% of Haitian households with piped water access have their services restricted each month due to non-payment (Haiti Outreach data); households reported paying up to US$100 for pipe installation/labour that never produced functioning water, a major hardship where 59% of the population earns <US$3/day; scheduled water-delivery days were frequently missed or only partially honored (valve-control failures), forcing households to wait until the following week.",
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "",
        "p_value": "",
        "extraction_sample_size": "32 in-depth interviews",
        "adjusted_or_unadjusted": "not applicable (qualitative thematic analysis)",
        "covariates": "",
        "model_type": "Qualitative ethnographic investigation with semi-structured interviews, thematic coding",
        "study_design": "Qualitative ethnographic/interview study",
        "risk_of_bias_tool": "",
        "risk_of_bias_rating": "",
        "selection_bias": "",
        "measurement_bias": "",
        "confounding": "",
        "attrition": "",
        "reporting_bias": "",
        "legal_measurement_quality": "2",
        "outcome_measurement_quality": "3",
        "mechanism_certainty": "Moderate: documents a genuine institutional mechanism (the near-total absence of formal government regulation, documentation, or oversight of informal neighbor-to-neighbor water-pipe networks, and the resulting informal payment/non-payment/service-restriction dynamics) directly against household-level water access, reliability, and affordability outcomes reported by 32 in-depth interviewees; the qualitative ethnographic method captures lived experience rather than a statistically tested exposure-outcome relationship.",
        "source_document": "Chapman et al. 2020, Water International 45(7-8):901-920 (retrieved via Google Drive inbox)",
        "page": "901-920",
        "table": "",
        "figure": "Fig. 2 (distribution of household water insecurity among ethnographic informants)",
        "section": "Water pipes; Source management; Health and physical barriers; Solutions and barriers to solutions",
        "exact_location": "Water pipes section (informal pipe networks, non-payment/service restriction); Source management section (source-manager disputes)",
        "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Qualitative ethnographic study of household water access in Gressier, Haiti, documenting the informal/unregulated institutional vacuum around neighbor-to-neighbor pipe networks against household-level access, reliability, and affordability outcomes. Not effect_sizes eligible: qualitative interview-based study, no regression. Extracted for record_id RB27F53708057.",
        "researcher": RESEARCHER,
        "date_extracted": DATE,
        "evidence_status": "OBSERVED",
    })
    new_rows.append(r)

    # S613: McCulligh, Arellano-Garcia & Casas-Beltran 2020, Western Mexico
    r = blank_row(fieldnames)
    r.update({
        "study_id": "S613",
        "citation": "McCulligh C, Arellano-Garcia L, Casas-Beltran D (2020). Unsafe waters: the hydrosocial cycle of drinking water in Western Mexico. Local Environment 25(8):576-596.",
        "doi": "10.1080/13549839.2020.1805598",
        "publication_year": "2020",
        "publication_type": "journal article",
        "language": "English",
        "peer_reviewed": "TRUE",
        "country": "Mexico",
        "subnational_unit": "Jalisco state: Guadalajara Metropolitan Area, El Salto municipality, San Juan de los Lagos municipality",
        "legal_system": "civil law",
        "urban_rural": "mixed",
        "service_provider": "SIAPA (Intermunicipal Drinking Water and Sewerage Services System); municipal water operators (El Salto, San Juan de los Lagos); private concession-holder FYPASA/Operadora de Ecosistemas (Toluquilla water treatment plant)",
        "regulatory_model": "1992 National Waters Law (transferrable water-extraction/discharge concession system); CONAGUA (National Water Commission) permitting and monitoring; NOM-127-SSA1-1994 drinking-water standard; 1983 constitutional decentralization of water services to municipalities; 2012 constitutional human-right-to-water reform",
        "population": "Households in Guadalajara Metropolitan Area, El Salto, and San Juan de los Lagos, Jalisco",
        "sample_size": "293-household survey across 4 Jalisco municipalities (El Salto n=89); semi-structured interviews with municipal/state water officials, industrial/agroindustrial associations, and local activists (2017-2018 fieldwork)",
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
        "enforcement": "TRUE",
        "documentation": "TRUE",
        "tenure": "",
        "property": "TRUE",
        "planning": "TRUE",
        "zoning": "",
        "building_permit": "",
        "service_area": "TRUE",
        "fees": "TRUE",
        "procedural_steps": "",
        "delay": "TRUE",
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
        "service_quantity": "TRUE",
        "service_quality": "TRUE",
        "affordability": "TRUE",
        "service_continuity": "TRUE",
        "application_success": "",
        "refusal": "",
        "delay_outcome": "TRUE",
        "effect_measure": "Household survey descriptive statistics (n=293) combined with qualitative case-study/document analysis; comparative regulatory-standard scoring (Mexico vs. 5 other countries against WHO guidelines); no regression",
        "effect_estimate": "CONAGUA reports 94.4% household drinking-water-connection coverage nationally, but only 42.6% of the population receives 'safely managed' water under JMP criteria; CONAGUA conducted an average of only 269 inspections/year across 41,116 water extraction/discharge concessions in Jalisco (would take 150+ years to inspect all users); household survey (n=293, 4 municipalities) found only 34.1% of respondents receive water daily, 38.6% every third day, and 27.3% twice a week or less; 48% of respondents purchased tanker-truck water in the previous year at 358% higher cost per cubic metre than piped SIAPA water ($62.22 MXN vs $13.60 MXN); Mexico's NOM-127-SSA1-1994 drinking-water standard scored second-worst of 6 countries compared against WHO guidelines (score of 25, only above Colombia).",
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "",
        "p_value": "",
        "extraction_sample_size": "293 households (4 municipalities); interviews with officials/associations",
        "adjusted_or_unadjusted": "not applicable (descriptive survey statistics and comparative case-study analysis)",
        "covariates": "",
        "model_type": "Mixed-methods case study (household survey plus semi-structured interviews and document/regulatory analysis)",
        "study_design": "Mixed-methods comparative case study (political-ecology/hydrosocial-cycle framework)",
        "risk_of_bias_tool": "",
        "risk_of_bias_rating": "",
        "selection_bias": "",
        "measurement_bias": "",
        "confounding": "",
        "attrition": "",
        "reporting_bias": "",
        "legal_measurement_quality": "3",
        "outcome_measurement_quality": "3",
        "mechanism_certainty": "Moderate-high: documents a genuine legal/institutional mechanism (Mexico's 1992 concession system, CONAGUA's near-nonexistent enforcement capacity, and the weak NOM-127 drinking-water standard) directly against household-level water-service intermittency and affordability outcomes measured via a 293-household survey across 4 municipalities, corroborated by official interviews and government data; however, the survey results are reported descriptively rather than through a regression linking the legal/institutional exposure to the outcome.",
        "source_document": "McCulligh, Arellano-Garcia & Casas-Beltran 2020, Local Environment 25(8):576-596 (retrieved via Google Drive inbox)",
        "page": "576-596",
        "table": "",
        "figure": "Fig. 1 (safely-managed water vs GDP per capita); Fig. 2 (national standards vs WHO guidelines); Fig. 3 (standards performance by component)",
        "section": "The management of unsafe waters; Differentiated supply from the Toluquilla aquifer; San Juan de los Lagos: drinking water not fit for human consumption",
        "exact_location": "Household survey results (Section 4.1, El Salto intermittency data); CONAGUA inspection-rate discussion (Section 2)",
        "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Mixed-methods case study of drinking-water regulation and access in Jalisco, Mexico, documenting weak/unenforced legal-institutional water regulation (CONAGUA concession/inspection regime, NOM-127 standard) against household-level survey-measured intermittency and affordability outcomes. Not effect_sizes eligible: descriptive survey statistics within a qualitative case-study narrative, no regression-based exposure-comparator effect estimate. Extracted for record_id R70C06383A22C.",
        "researcher": RESEARCHER,
        "date_extracted": DATE,
        "evidence_status": "OBSERVED",
    })
    new_rows.append(r)

    for r in new_rows:
        assert r["study_id"] not in existing_ids, f"{r['study_id']} already exists"

    rows.extend(new_rows)

    fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmppath, DB)

    print("Appended", len(new_rows), "rows:", [r["study_id"] for r in new_rows])


if __name__ == "__main__":
    main()
