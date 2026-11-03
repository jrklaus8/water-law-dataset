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

    # S643: Appelblad Fredby & Nilsson 2013, Kampala Uganda pro-poor water provision
    r = blank_row(fieldnames)
    r.update({
        "study_id": "S643",
        "citation": "Appelblad Fredby J, Nilsson D (2013). From 'All for some' to 'Some for all'? A historical geography of pro-poor water provision in Kampala. Journal of Eastern African Studies 7(1):40-57.",
        "doi": "10.1080/17531055.2012.708543",
        "publication_year": "2013",
        "publication_type": "journal article",
        "language": "English",
        "peer_reviewed": "TRUE",
        "country": "Uganda",
        "subnational_unit": "Kisenyi I and Kisenyi II Parishes, later extended to Bwaise II, Kampala",
        "legal_system": "common law (Uganda)",
        "urban_rural": "urban (informal settlements)",
        "service_provider": "National Water and Sewerage Corporation (NWSC), operated locally as Kampala Water",
        "regulatory_model": "NWSC's 2004 connection policy (subsidizing connection installation costs, up to 50m of service line) aimed to encourage individual private connections; informal settlements face institutional barriers of unclear land tenure/property rights preventing conventional piped connections; since 2006 the 'Water to the Urban Poor' project introduced pre-paid meter technology at standpipes/yard-taps via a dedicated pro-poor branch office with formal eligibility criteria (income below Shs. 80,000/month, low private-connection density, low consumption)",
        "population": "residents of Kampala informal settlements (over 100,000 people in project parishes)",
        "sample_size": "qualitative case study with interviews (utility officials, community leaders, vendors, project consultants) and documentary/historical archival analysis, project area >100,000 people",
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
        "delay": "",
        "discretion": "TRUE",
        "hardship_exception": "",
        "administrative_review": "",
        "complaint": "",
        "judicial_review": "",
        "disconnection": "TRUE",
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
        "service_quantity": "TRUE",
        "service_quality": "",
        "affordability": "TRUE",
        "service_continuity": "",
        "application_success": "TRUE",
        "refusal": "",
        "delay_outcome": "",
        "effect_measure": "historical documentary analysis plus semi-structured interviews; connection-count time-series",
        "effect_estimate": "In 2007, of 170,000 total water connections across all Ugandan towns, only around 6,000 were found within poor urban areas. After the 2004 connection-cost-subsidy policy, the number of new customers per month doubled in the first year, with national new connections continuing to grow at over 20,000/year, though the policy's benefits did not primarily reach informal-settlement residents due to persisting land-tenure/property-rights barriers. The pre-paid meter pilot ('Water to the Urban Poor') installed about 390 water meters by 2009 at yard taps and public stand posts; the pro-poor tariff sold water at roughly one-third of the price charged by informal water vendors in the same area.",
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "",
        "p_value": "",
        "extraction_sample_size": "qualitative case study; project area population >100,000",
        "adjusted_or_unadjusted": "not applicable (historical documentary/interview case study, not a regression model)",
        "covariates": "",
        "model_type": "historical institutional case study with qualitative interviews and documentary/archival analysis",
        "study_design": "historical-institutional case study",
        "risk_of_bias_tool": "Legal Institutional Evidence Appraisal Framework",
        "risk_of_bias_rating": "",
        "selection_bias": "",
        "measurement_bias": "",
        "confounding": "",
        "attrition": "",
        "reporting_bias": "",
        "legal_measurement_quality": "3",
        "outcome_measurement_quality": "3",
        "mechanism_certainty": "Moderate-high: documents genuine legal/administrative mechanisms (the 2004 NWSC connection-subsidy policy, land-tenure/property-rights barriers to piped connections in informal settlements, and a formally-defined pro-poor eligibility framework for a pre-paid meter pilot) against real, tracked connection-count data over time and interview evidence; the study is historical/documentary rather than a formal statistical comparison of exposure versus outcome.",
        "source_document": "Appelblad Fredby & Nilsson 2013, Journal of Eastern African Studies 7(1):40-57 (retrieved via Google Drive inbox)",
        "page": "40-57",
        "table": "",
        "figure": "Figure 1; Figure 2; Figure 3; Figure 4",
        "section": "The era of sector reforms; Public service provision and the urban poor; The return of the 'coin-in-the-slot machine'",
        "exact_location": "Sections on the 2004 connection policy, land-tenure barriers, and the Water to the Urban Poor pre-paid meter pilot project",
        "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). Historical-institutional case study of Kampala's pro-poor water provision, documenting the 2004 connection policy, land-tenure barriers, and a pre-paid meter pilot project against real tracked connection-count data. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: historical/interview-based case study. Extracted for record_id RC4A4206BDF16.",
        "researcher": RESEARCHER,
        "date_extracted": DATE,
        "evidence_status": "OBSERVED",
    })
    new_rows.append(r)

    # S644: Vasquez & Franceschi 2013, Nicaragua water service decentralization
    r = blank_row(fieldnames)
    r.update({
        "study_id": "S644",
        "citation": "Vasquez WF, Franceschi D (2013). System Reliability and Water Service Decentralization: Investigating Household Preferences in Nicaragua. Water Resources Management 27:4913-4926.",
        "doi": "10.1007/s11269-013-0447-4",
        "publication_year": "2013",
        "publication_type": "journal article",
        "language": "English",
        "peer_reviewed": "TRUE",
        "country": "Nicaragua",
        "subnational_unit": "Leon, Nicaragua",
        "legal_system": "civil law (Nicaragua)",
        "urban_rural": "urban",
        "service_provider": "Nicaraguan Company of Water and Sanitation (ENACAL, centralized national utility); Municipality of Leon (proposed decentralized alternative)",
        "regulatory_model": "Nicaragua's Law of Municipalities (article 7) assigns responsibility for water-service provision to municipalities, and the 2005-2015 National Water Strategy designates decentralization as a fundamental development element, but as of the study only 26 of 152 municipalities operated their own water systems; the study elicits household preferences (via contingent valuation and choice experiments) between the status-quo centralized institution (ENACAL) and a proposed decentralized municipal provider",
        "population": "urban households in Leon, Nicaragua's second-largest city",
        "sample_size": "690 households (74% response rate), split-sample experimental design (2x2)",
        "household_level": "TRUE",
        "community_level": "",
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
        "formal_connection": "",
        "water_access": "TRUE",
        "sanitation_access": "",
        "service_coverage": "",
        "service_reliability": "TRUE",
        "service_quantity": "",
        "service_quality": "TRUE",
        "affordability": "TRUE",
        "service_continuity": "TRUE",
        "application_success": "",
        "refusal": "",
        "delay_outcome": "",
        "effect_measure": "censored logistic regression (Cameron 1988 referendum-data WTP estimation); logit choice models; binomial tests of provider-characteristic preferences",
        "effect_estimate": "Households are willing to pay a substantial premium for reliable (24-hour) water service: median WTP of 327 Cordobas/month (~15.95 USD, ~11.6% of median household income) when ENACAL is the provider, versus 234 Cordobas/month (~8.3% of median income) when the municipality is the provider; the ENACAL-municipality WTP gap (~93 Cordobas/month) is not statistically significant (wide overlapping confidence intervals). In the pooled model, coefficients on QUALITY and CITY (centralized-vs-decentralized provider) are both statistically insignificant. However, in a separate categorical-preference exercise, approximately 75% of households believe ENACAL would provide better service and 63% believe ENACAL would invest more in infrastructure than the municipality, with all such preference differentials favoring ENACAL statistically significant at the 1% level via binomial tests.",
        "lower_CI": "69.82 to 1,421.37 (Model 1, ENACAL WTP 95% CI)",
        "upper_CI": "",
        "standard_error": "",
        "p_value": "0.006 (likelihood ratio test across split-sample treatments); <0.01 (binomial tests of ENACAL-preference differentials)",
        "extraction_sample_size": "690 households",
        "adjusted_or_unadjusted": "adjusted (income, hours of daily water supply, subjective reliability perception, bottled-water consumption, storage-device ownership, age, education, sex, household size, home ownership, survey-consequentiality indicators)",
        "covariates": "income, service hours, reliability perception, bottled-water use, storage devices, age, education, sex, household size, home ownership",
        "model_type": "censored logistic regression (contingent valuation, referendum format) and logit choice models",
        "study_design": "quantitative household survey with split-sample contingent-valuation experiment",
        "risk_of_bias_tool": "JBI Critical Appraisal Checklist for Analytical Cross Sectional Studies",
        "risk_of_bias_rating": "",
        "selection_bias": "",
        "measurement_bias": "",
        "confounding": "",
        "attrition": "",
        "reporting_bias": "",
        "legal_measurement_quality": "3",
        "outcome_measurement_quality": "4",
        "mechanism_certainty": "Moderate: a genuine institutional-governance exposure (centralized national utility vs. decentralized municipal provider, grounded in Nicaragua's Law of Municipalities and National Water Strategy) is tested via a rigorous contingent-valuation/choice-experiment design against household-level willingness-to-pay and provider-preference outcomes; however, the key centralization-vs-decentralization (CITY) coefficient is not statistically significant in the pooled willingness-to-pay regression, limiting causal certainty about the institutional-governance mechanism itself, though the categorical preference-distribution findings are significant.",
        "source_document": "Vasquez & Franceschi 2013, Water Resources Management 27:4913-4926 (retrieved via Google Drive inbox)",
        "page": "4913-4926",
        "table": "Table 1; Table 2; Table 3; Table 4; Table 5",
        "figure": "Figure 1",
        "section": "Survey Design; Results",
        "exact_location": "Section 5 (Results), Table 4 (WTP models) and Table 5 (median WTP comparison)",
        "extraction_note": "Extracted from full-text PDF (retrieved via Google Drive inbox). 690-household contingent-valuation survey testing household preferences for centralized versus decentralized water-service governance in Leon, Nicaragua. Included per INCLUSION_EXCLUSION.md criteria 1-9. Not effect_sizes eligible: the centralization-vs-decentralization coefficient is not statistically significant in the pooled WTP regression. Extracted for record_id R14B39B9D52E2.",
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
