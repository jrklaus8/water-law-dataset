#!/usr/bin/env python3
import csv, tempfile, os

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
EXTR = f"{BASE}/03_extraction/extracted_data/extraction_database.csv"
TODAY = "2026-09-27"
RESEARCHER = "Claude-AI-fulltext-2026-09-27"

with open(EXTR, newline="") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    rows = list(r)
    existing_ids = {row["study_id"] for row in rows}

def blank_row(fieldnames):
    return {fn: "" for fn in fieldnames}

def add(sid, **kwargs):
    assert sid not in existing_ids, f"{sid} already exists"
    row = blank_row(fieldnames)
    row["study_id"] = sid
    row["researcher"] = RESEARCHER
    row["date_extracted"] = TODAY
    row["peer_reviewed"] = "TRUE"
    row["publication_type"] = "journal article"
    row["language"] = "English"
    row["evidence_status"] = "OBSERVED"
    row.update(kwargs)
    rows.append(row)

# S779 - Tynan 2013 - 19th century London
add("S779",
    citation="Tynan N (2013). Nineteenth century London water supply: Processes of innovation and improvement. Review of Austrian Economics.",
    doi="10.1007/s11138-012-0182-8",
    publication_year="2013",
    country="United Kingdom",
    subnational_unit="London",
    legal_system="common law",
    urban_rural="urban",
    service_provider="Eight private water companies (later purchased by the Metropolitan Water Board)",
    regulatory_model="Historical case study of nineteenth-century London water supply examining how legal/regulatory constraints -- illegal private sewer connections requiring official-bricklayer construction and household fees, the 1848 Metropolitan Commission of Sewers mandate, and later Parliamentary-approval requirements for company investment -- interacted with private water companies' network-expansion and quality-improvement investment over the century",
    population="London households, 1801-1900 (population grew from 959,000 to 6.3 million in Water London)",
    sample_size="historical case study, century-long panel of company/regulatory records",
    household_level="TRUE", community_level="TRUE",
    fees="TRUE", procedural_steps="TRUE", delay="TRUE", enforcement="TRUE", sanction="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE", service_coverage="TRUE", service_quality="TRUE",
    effect_measure="historical/qualitative economic-process analysis (comparison of company investment timing vs. regulatory timing)",
    effect_estimate="Private water companies expanded network coverage and invested in filtration/quality improvements ahead of government regulation in most cases; late-century regulations requiring Parliamentary approval for additional investment slowed infrastructure improvements; private sewer connections were illegal until 1815 and required official-bricklayer construction paid by households, constraining household uptake",
    study_design="historical-institutional case study (Austrian economic-process approach)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="1",
    mechanism_certainty="Moderate: detailed historical-legal analysis of how sewer-connection legality/procedural requirements and Parliamentary investment-approval regulation shaped private water-company network-expansion behavior over the nineteenth century, though framed through an ideological Austrian-economics lens critical of regulation.",
    source_document="Tynan 2013, Review of Austrian Economics (retrieved via Google Drive, Antigravity batch)",
    section="Sections 2-3 (demand/supply/technology; water pollution and entrepreneurial response)",
    exact_location="Sections 2-3",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: historical-institutional case study of legal/regulatory constraints (illegal sewer connections, Parliamentary approval requirements) on water/sanitation network expansion, matching the established institutional-history precedent line (cf. Heller et al. 2014 Brazil, Smith 2004 Cape Town). NOT effect_sizes eligible: historical narrative/economic-process analysis, no regression-based estimate. Extracted for record_id REA98E915A1CD.",
    )

# S780 - Pizzi 2020 - Ethnicity and drinking water, China (EFFECT_SIZES ELIGIBLE)
add("S780",
    citation="Pizzi E (2020). Ethnicity and Government Provision of Drinking Water Infrastructure in Rural China. Asian Survey.",
    doi="10.1525/AS.2020.60.4.607",
    publication_year="2020",
    country="China",
    subnational_unit="Guizhou Province (61 counties)",
    legal_system="civil law",
    urban_rural="rural",
    service_provider="Ministry of Water Resources (MWR) National Rural Drinking Water Safety Project",
    regulatory_model="OLS regression analysis of >10,000 government drinking-water infrastructure projects across 61 counties, testing whether official Chinese ethnic-minority-autonomous-area legal status and minority population share affect project beneficiary numbers and funding, despite stated central-government policy prioritizing minority areas",
    population="rural county populations, Guizhou Province, disaggregated by ethnic-minority share and autonomous-county legal status",
    sample_size="61 counties; >10,000 individual drinking water projects",
    household_level="", community_level="TRUE",
    eligibility="TRUE", discretion="TRUE", legal_status="TRUE", documentation="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_coverage="TRUE",
    effect_measure="OLS regression with robust standard errors (county-level, n=61)",
    effect_estimate="Percentage Minority coefficient on project beneficiaries: -75,817.29 (SE 36,428.49), p<0.05 (Model 2, full model), controlling for economic/demographic/geographic factors including Autonomous County legal status: -41,810.91 (SE 25,959.55), not statistically significant. Fewer people benefit from drinking-water projects in counties with larger minority population shares, despite official policy prioritizing minority areas, attributed to street-level bureaucratic implementation ease favoring Han-majority areas",
    lower_CI="", upper_CI="", standard_error="25,959.55 (Autonomous County legal-status coefficient)",
    p_value="not significant (Autonomous County legal-status coefficient)",
    extraction_sample_size="61",
    adjusted_or_unadjusted="adjusted (economic, demographic, geographic controls)",
    covariates="GDP (logged), average expenditure, population (logged), population density, share urban, outmigration, number of villages, total water points, karst landform %, average slope",
    model_type="OLS regression with robust standard errors",
    study_design="quantitative county-level regression analysis of administrative project-allocation data",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: genuine regression-based analysis isolating official ethnic-minority-autonomous-area legal status (a formal Chinese administrative-law designation) as an exposure variable, alongside minority-population-share, on drinking-water infrastructure beneficiary counts, with region/county-level controls.",
    source_document="Pizzi 2020, Asian Survey (retrieved via Google Drive, Antigravity batch)",
    table="Tables 2, 3, 4",
    section="Results",
    exact_location="Table 2 (minority population and project beneficiaries)",
    extraction_note="INCLUDE and EFFECT_SIZES ELIGIBLE per PROJECT_SPEC.md Section 8 Family A framework (legal recognition/status): genuine OLS regression directly testing official autonomous-county legal status as an exposure on drinking-water infrastructure beneficiaries; recorded faithfully as a null result (not significant), consistent with the S037 precedent of recording null Family A findings. Extracted for record_id RE992755C7ABF.",
    )

# S781 - Crawford & Bell 2012 - Cusco Peru
add("S781",
    citation="Crawford C, Bell S (2012). Analysing the Relationship between Urban Livelihoods and Water Infrastructure in Three Settlements in Cusco, Peru. Urban Studies.",
    doi="10.1177/0042098011408140",
    publication_year="2012",
    country="Peru",
    subnational_unit="Cusco (San Blas, Angostura, Manco Capac settlements)",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="Municipal water utility (San Blas), community-managed system (Angostura), poorly-managed committee-run system (Manco Capac)",
    regulatory_model="Comparative three-settlement case study applying a sustainable-livelihoods/infrastructure-governance framework, examining how differing modes of water infrastructure organisation (commercialised municipal supply, community-managed decentralised system, excluded/poorly-governed committee system) co-exist within the same city despite national water-policy prescriptions, and their effects on household vulnerability",
    population="households in three Cusco settlements differentiated by water infrastructure governance mode",
    sample_size="qualitative three-settlement comparative case study",
    household_level="TRUE", community_level="TRUE",
    institutional_fragmentation="TRUE", participation="TRUE", discretion_accommodation="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_reliability="TRUE",
    effect_measure="qualitative comparative case-study analysis",
    effect_estimate="Manco Capac, excluded from the centralised municipal system and served by a poorly-managed committee-run water system, suffered the greatest household vulnerability; unequal access to water infrastructure within and between settlements amplified household vulnerability, which in turn undermined local autonomous governance of water",
    study_design="qualitative comparative case study (three settlements)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="1",
    mechanism_certainty="Moderate-high: comparative case study directly matching the established 'splintering urbanism'/informal-governance precedent line (cf. Kooy & Bakker, Ranganathan), documenting how differing institutional modes of water infrastructure organisation privilege some groups and bypass others within the same city.",
    source_document="Crawford & Bell 2012, Urban Studies (retrieved via Google Drive, Antigravity batch)",
    section="Sections 2-4 (infrastructure governance framework, Peruvian water reform, case studies)",
    exact_location="Sections 2-4",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: extends the established informal-governance/splintering-urbanism precedent (Marvin & Graham, van Vliet et al. framework) to Cusco, Peru, documenting institutional-mode-driven exclusion and vulnerability. NOT effect_sizes eligible: qualitative comparative case study, no regression-based estimate. Extracted for record_id RE8EDE45DF049.",
    )

# S782 - Pierce & Gmoser-Daskalakis 2021 - California intra-city
add("S782",
    citation="Pierce G, Gmoser-Daskalakis K (2021). Multifaceted intra-city water system arrangements in California: Influences and implications for residents. Utilities Policy.",
    doi="10.1016/j.jup.2021.101231",
    publication_year="2021",
    country="United States",
    subnational_unit="California (482 incorporated cities)",
    legal_system="common law",
    urban_rural="both",
    service_provider="Municipal utilities, private investor-owned utilities (IOUs), special districts, and mutual water systems, in varying single and multi-provider intra-city arrangements",
    regulatory_model="Empirical city-level analysis of drinking-water service-provider governance arrangements (municipal/private/special-district) across all 482 incorporated California cities, using multivariate regression to identify influences (especially city incorporation date, a legal/administrative status) on arrangement type, and descriptive analysis of intra-city water-rate variance implications for affordability",
    population="residents of 482 California cities",
    sample_size="482 cities (regression models n=475-476); intra-city rate analysis of Los Angeles County cities with 5+ systems",
    household_level="", community_level="TRUE",
    institutional_fragmentation="TRUE", documentation="TRUE",
    fees="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE", service_coverage="TRUE",
    effect_measure="binary logistic and multinomial logistic regression (institutional arrangement type as dependent variable) plus descriptive intra-city rate-variance analysis",
    effect_estimate="City incorporation date most profoundly influences the mix of water systems in a city, especially special-district or multiple-system-type arrangements; cities with multiple water systems show wide intra-city variance in water rates at constant consumption (e.g., some IOU-served neighborhoods paying more than double the rate of city- or mutual-served neighborhoods in the same city)",
    study_design="quantitative city-level regression analysis plus descriptive rate-variance case comparison",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: regression-based analysis of city incorporation date (a legal/administrative status) as a driver of water-system institutional-arrangement type, combined with descriptive evidence that resulting fragmentation produces intra-city affordability disparities; regression dependent variable is the institutional arrangement itself rather than a water-access outcome.",
    source_document="Pierce & Gmoser-Daskalakis 2021, Utilities Policy (retrieved via Google Drive, Antigravity batch)",
    table="Tables 1-4",
    section="Sections 4.2-4.3 (regression results; conservation and affordability)",
    exact_location="Sections 4.2-4.3",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: companion California water-institution study to the S037 Espinoza & Viers SGMA precedent, with regression evidence on the legal/administrative driver (incorporation date) of institutional fragmentation and its affordability implications. NOT effect_sizes eligible: the regression models institutional arrangement type as the dependent variable (not a water-access outcome regressed on a legal mechanism), and the affordability/rate-variance evidence (Table 4) is a small descriptive case comparison, not a regression-based estimate. Extracted for record_id RE57362A779FA.",
    )

# S783 - Pezon 2017 - Burkina Faso price-cap regulation
add("S783",
    citation="Pezon C (2017). Price-cap regulation of private water services for small towns in Burkina Faso based on solar energy. International Journal of Sustainable Development.",
    publication_year="2017",
    country="Burkina Faso",
    subnational_unit="small towns (semi-urban centres, 2,000-10,000 inhabitants)",
    legal_system="civil law",
    urban_rural="both",
    service_provider="Professional operators contracted for ten years under affermage (lease) contracts by the National Department for Water; ONEA (Office National de l'Eau et de l'Assainissement) holds the urban concession",
    regulatory_model="Action-research study developing and analysing a price-cap regulation framework, combined with a switch to solar energy, for ten-year affermage contracts governing private operators of small-town piped water schemes in Burkina Faso, aimed at achieving equitable and financially sustainable universal water access by 2030",
    population="residents of Burkinabe small towns served by affermage-contracted water schemes",
    sample_size="action-research participatory process (one year), sector stakeholder engagement",
    household_level="TRUE", community_level="TRUE",
    fees="TRUE", procedural_steps="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE", service_continuity="TRUE",
    effect_measure="action-research/policy-design analysis (price-cap methodology)",
    effect_estimate="A consistent price-cap regulation combined with a switch to solar energy is identified as the condition for achieving equitable and financially sustainable universal safe-water access in Burkinabe small towns under the existing affermage/PPP contractual framework",
    study_design="action-research participatory policy-design study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="Moderate-high: detailed institutional/regulatory analysis (ONEA concession framework, ten-year affermage contracts, price-cap tariff regulation) directly addressing the equity and financial-sustainability implications of the regulatory mechanism for small-town water access.",
    source_document="Pezon 2017, International Journal of Sustainable Development (retrieved via Google Drive, Antigravity batch)",
    section="Sections 2.2-2.3 (tariff equity challenge; regulation challenge)",
    exact_location="Sections 2.2-2.3",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: detailed regulatory-mechanism case study (price-cap regulation, affermage contracts) matching the established regulatory precedent line (cf. Marson & van Dijk 2016 Zambia, Adeoti & Fati 2020). NOT effect_sizes eligible: action-research/policy-design analysis, no regression-based estimate. Extracted for record_id RE54EF28A4406.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
