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

    # S614: Agbemor & Smiley 2021, Sunyani West District Ghana
    r = blank_row(fieldnames)
    r.update({
        "study_id": "S614",
        "citation": "Agbemor BD, Smiley SL (2021). Tensions between Formal and Informal Water Providers: Receptivity toward Mechanised Boreholes in the Sunyani West District, Ghana. The Journal of Development Studies 57(3):383-399.",
        "doi": "10.1080/00220388.2020.1786059",
        "publication_year": "2021",
        "publication_type": "journal article",
        "language": "English",
        "peer_reviewed": "TRUE",
        "country": "Ghana",
        "subnational_unit": "Sunyani West District, Bono Region (8 communities: Nsoatre, Chiraa, Odumase, Fiapre, Dumasua, Kwatire, Adantia, Asuakwaa)",
        "legal_system": "common law",
        "urban_rural": "mixed",
        "service_provider": "Ghana Water Company Limited (GWCL); Sunyani West District Authority; privately managed mechanised boreholes (informal)",
        "regulatory_model": "Water Resources Commission Act/L.I. 1692 (2001) groundwater abstraction permitting; Community Water and Sanitation Agency regulations (L.I. 2007, 2011); Local Government Act 1993 (Act 462); District Operational Manual/CWSA Small Towns Sector Guidelines",
        "population": "Households in the Sunyani West District's 8 study communities",
        "sample_size": "Census of 98 mechanised boreholes; interviews with 89 private operators + 2 Water and Sanitation Management Teams + 98 vendors; 2,439 water-user interviews (average 25 per borehole)",
        "household_level": "TRUE",
        "community_level": "TRUE",
        "income_group": "",
        "tenure_status": "",
        "legal_status": "TRUE",
        "indigenous_population": "",
        "migrant_population": "",
        "eligibility": "",
        "burden": "TRUE",
        "discretion_accommodation": "TRUE",
        "enforcement": "TRUE",
        "documentation": "",
        "tenure": "",
        "property": "TRUE",
        "planning": "TRUE",
        "zoning": "",
        "building_permit": "TRUE",
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
        "application_success": "TRUE",
        "refusal": "",
        "delay_outcome": "",
        "effect_measure": "Descriptive service-indicator assessment (CWSA reliability/distance/quantity/quality framework) applied to a census of 98 boreholes; no regression",
        "effect_estimate": "91 of 93 assessed mechanised boreholes (in operation >=12 months) were reliable, functioning for at least 347 of the past 365 days; all water users had access within CWSA's 500m/30-minute standard, with 84% accessing within 5 minutes; 16% of households used >=288 L/day, 72% used 144-252 L/day, 12% used >=108 L/day, implying >=25 L/capita/day given the district's 4.3 average household size (above CWSA's 20 L/capita/day minimum); none of the 98 boreholes had undergone the mandatory biannual water-quality testing; none of the 76 privately drilled boreholes had sought WRC groundwater-abstraction permits or District Authority approval, and no enforcement action was taken by regulators despite this being a stated legal violation.",
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "",
        "p_value": "",
        "extraction_sample_size": "98 boreholes; 2,439 water-user interviews",
        "adjusted_or_unadjusted": "not applicable (descriptive census/survey statistics)",
        "covariates": "",
        "model_type": "Case-study census survey with the Receptivity framework (qualitative) applied to stakeholder perceptions",
        "study_design": "Case study (census of water facilities plus operator/vendor/user surveys and key-informant interviews)",
        "risk_of_bias_tool": "",
        "risk_of_bias_rating": "",
        "selection_bias": "",
        "measurement_bias": "",
        "confounding": "",
        "attrition": "",
        "reporting_bias": "",
        "legal_measurement_quality": "3",
        "outcome_measurement_quality": "3",
        "mechanism_certainty": "Moderate-high: documents a genuine legal-status mechanism (privately managed mechanised boreholes operating in explicit, unenforced violation of Ghana's Water Resources Commission groundwater-abstraction permitting and District Authority approval requirements) directly against household-level water access, reliability, quantity, and affordability outcomes measured via a near-complete census of the district's 98 mechanised boreholes and 2,439 water-user interviews; however, the relationship is documented descriptively rather than through a regression linking legal status to the outcome.",
        "source_document": "Agbemor & Smiley 2021, Journal of Development Studies 57(3):383-399 (retrieved via Google Drive inbox)",
        "page": "383-399",
        "table": "Table 1 (water facilities by community); Table 2 (categories of mechanised borehole operators)",
        "figure": "",
        "section": "3.1 The geography of water production and the growth of informal providers; 3.2 Contributions of the mechanised boreholes to enhancing access to water; 3.3 Traditional service providers, regulators and water users' perception",
        "exact_location": "Section 3.2 (service-indicator results); Section 3.3 (legal-status/enforcement discussion)",
        "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Case-study census of privately managed, legally unauthorized mechanised boreholes in Ghana's Sunyani West District, documenting their legal status (illegal under WRC/CWSA regulations, unenforced) against household-level water access, reliability, quantity, and affordability outcomes. Not effect_sizes eligible: descriptive census/survey statistics, no regression. Extracted for record_id R7CD58D2E7BE3.",
        "researcher": RESEARCHER,
        "date_extracted": DATE,
        "evidence_status": "OBSERVED",
    })
    new_rows.append(r)

    # S615: Tantoh & McKay 2020, Northwest Cameroon
    r = blank_row(fieldnames)
    r.update({
        "study_id": "S615",
        "citation": "Tantoh HB, McKay TJM (2020). Rural self-empowerment: the case of small water supply management in Northwest, Cameroon. GeoJournal 85:159-171.",
        "doi": "10.1007/s10708-018-9952-6",
        "publication_year": "2020",
        "publication_type": "journal article",
        "language": "English",
        "peer_reviewed": "TRUE",
        "country": "Cameroon",
        "subnational_unit": "Ndu, Njinikom, and Mbengwi rural districts, Northwest Region (6 villages: Njimkang, Ngarum, Muloin, Baicham, Tugi, Zang-Tabi)",
        "legal_system": "mixed (civil law/customary)",
        "urban_rural": "rural",
        "service_provider": "Community-based organizations (CBOs); village development associations (VDAs); community Water Management Committees (WMCs); village chiefs ('Fon')",
        "regulatory_model": "1998 water law (authorizing private individuals and community groups as water-development actors, following 1991 liberty/liberalization laws); centralized national water utilities CAMWATER/CDE (urban-only); Ministry of Energy and Water Resources (MINEE) abstraction/discharge licensing",
        "population": "Rural households in Northwest Cameroon community-based water-supply systems",
        "sample_size": "108 households surveyed (18 households per village x 6 villages), drawn from a 180-household population list via adaptive sequential procedure with 60% margin of error",
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
        "disconnection": "TRUE",
        "reconnection": "",
        "sanction": "TRUE",
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
        "service_continuity": "",
        "application_success": "TRUE",
        "refusal": "",
        "delay_outcome": "",
        "effect_measure": "Household survey descriptive statistics by connection type and village; per capita consumption comparison (private connection vs communal stand tap); no significance test or regression",
        "effect_estimate": "34% of surveyed households achieved private water connections vs 66% relying on communal stand taps (average distance 350m); mean water consumption was 35.6 L/capita/day for households with private connections vs 24.7 L/capita/day for households using communal stand taps (both below the WHO/UHCHR-recommended 100 L/capita/day); communal-tap users spent an average of 71.6 minutes/day collecting water (41.6 minutes above the WHO 30-minute standard); 71 of 108 households could not afford the connection fees to establish a private water system, and 54% were unable to regularly pay the monthly USD1 communal-tap maintenance fee; households failing to contribute financially to system establishment faced sanctions (e.g. denial of authorization to perform funeral rites) or relegation from private to communal-tap access.",
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "",
        "p_value": "",
        "extraction_sample_size": "108 households (6 villages)",
        "adjusted_or_unadjusted": "not applicable (descriptive per-village/per-connection-type means)",
        "covariates": "",
        "model_type": "Household survey with descriptive statistics",
        "study_design": "Cross-sectional household survey (structured questionnaires) combined with qualitative community-based-management analysis",
        "risk_of_bias_tool": "",
        "risk_of_bias_rating": "",
        "selection_bias": "",
        "measurement_bias": "",
        "confounding": "",
        "attrition": "",
        "reporting_bias": "",
        "legal_measurement_quality": "3",
        "outcome_measurement_quality": "3",
        "mechanism_certainty": "Moderate: documents a genuine legal/institutional mechanism (Cameroon's 1998 water law authorizing community-based water management, and Water Management Committee-set upfront cash-eligibility and monthly-fee requirements determining private vs communal connection access) directly against household-level water access, consumption, and affordability outcomes measured via a 108-household survey across 6 villages; however, the comparison is a descriptive difference in means with no reported significance test, and the per-village samples are small (n=18).",
        "source_document": "Tantoh & McKay 2020, GeoJournal 85:159-171 (retrieved via Google Drive inbox)",
        "page": "159-171",
        "table": "Table 1 (financial contributions towards CBWM systems); Table 2 (households' access to piped water supply); Table 3 (average time spent in water portage)",
        "figure": "Fig. 1 (map of study sites)",
        "section": "Water and accessibility to potable water supply in Cameroon; Results; Discussion",
        "exact_location": "Table 2 (private vs communal connection consumption comparison); Results section (financial contributions and eligibility)",
        "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Household survey of community-based water management in rural Northwest Cameroon under the 1998 water law, documenting Water Management Committee eligibility/fee requirements against household-level water access and consumption outcomes. Not effect_sizes eligible: descriptive per-village means, no significance test or regression, small samples (n=18/village). Extracted for record_id R77355A6C9E10.",
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
