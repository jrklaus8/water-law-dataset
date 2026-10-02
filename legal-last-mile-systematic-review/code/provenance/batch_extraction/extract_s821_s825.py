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

# S821 - Whittington, Lauria & Mu - Onitsha Nigeria water vending
add("S821",
    citation="Whittington D, Lauria DT, Mu X (1991). A Study of Water Vending and Willingness to Pay for Water in Onitsha, Nigeria. World Development.",
    publication_year="1991",
    country="Nigeria",
    subnational_unit="Onitsha, Anambra State",
    legal_system="common law",
    urban_rural="urban",
    service_provider="Anambra State Water Corporation (ASWC), private water vendors",
    regulatory_model="Household reconnaissance survey and market study of Onitsha's informal, private-sector-run water vending system (tanker trucks, boreholes, small retailers), documenting that only about 8,000 households had functioning connections to the public water utility while the vast majority relied on an elaborate private vending market, and discussing the public utility's regulatory/monopoly status and revenue underperformance relative to the informal market",
    population="households in Onitsha, Nigeria, connected and unconnected to the public water utility",
    sample_size="household reconnaissance survey; water vending market census (~275 tanker trucks, ~20 major boreholes)",
    household_level="TRUE", community_level="TRUE",
    fees="TRUE", formal_connection="TRUE",
    water_access="TRUE", affordability="TRUE", service_coverage="TRUE",
    effect_measure="household survey and market study with willingness-to-pay estimation",
    effect_estimate="Only about 8,000 households in Onitsha had functioning connections to the public water utility (ASWC); the vast majority obtained water from an elaborate, well-organized private-sector water vending system (approximately 275 tanker trucks purchasing from ~20 major private boreholes) that, during the dry season, collected about 24 times as much revenue as the public utility; households paid water vendors over twice the operation-and-maintenance cost of a piped distribution system on an annual basis, illustrating the affordability and access consequences of the public utility's severely limited connection coverage and its status as an underperforming regulated monopoly",
    study_design="household reconnaissance survey with informal-market census and WTP estimation",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="1",
    mechanism_certainty="Moderate-high: primary household and market survey data directly documenting the public utility's severely limited connection coverage and the resulting emergence of a costly informal private water market, with the public utility's monopoly/regulatory status raised as an institutional factor limiting its expansion and revenue performance.",
    source_document="Whittington, Lauria & Mu 1991, World Development (retrieved via Google Drive)",
    section="Description of water-vending practices; Discussion and policy implications",
    exact_location="Sections 4-6",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: seminal household/market survey directly documenting a public utility's severely limited connection coverage and the resulting informal water market and affordability burden. NOT effect_sizes eligible: household WTP/market-survey study, no regression-based estimate isolating a legal/institutional mechanism's effect on a water-access outcome as required by PROJECT_SPEC.md S8. Extracted for record_id R49BC05123474.",
    )

# S822 - Nolan, Bloom & Subbaraman - India slums legal status
add("S822",
    citation="Nolan LB, Bloom DE, Subbaraman R (2017/2018). Legal Status and Deprivation in India's Urban Slums: An Analysis of Two Decades of National Sample Survey Data. IZA Discussion Paper No. 10639.",
    publication_year="2018",
    country="India",
    subnational_unit="2,901 slums across all states (10 largest slum-population states for the multivariable model)",
    legal_system="common law",
    urban_rural="urban",
    service_provider="state and local governments (slum notification authority)",
    regulatory_model="Multilevel regression analysis of four waves (1993, 2002, 2008, 2012) of India's National Sample Survey (NSS) data on 2,901 slums, testing whether 'non-notified' status (lack of formal government legal recognition) is associated with greater deprivation in access to basic services (piped water, latrines, solid waste disposal, schools, health centers), using a constructed Basic Services Deprivation Score (BSDS), and a second multilevel logistic regression testing whether legal status predicts receipt of government slum-improvement-scheme financial aid",
    population="residents of notified and non-notified urban slums across India",
    sample_size="2,901 slums (four NSS survey waves); multivariable model restricted to 2,390 slums (10 largest states) with non-missing data",
    household_level="", community_level="TRUE",
    legal_status="TRUE", eligibility="TRUE", documentation="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE", service_coverage="TRUE",
    effect_measure="multilevel regression (BSDS as outcome; years-notified as key predictor) and multilevel logistic regression (receipt of government slum-improvement aid as outcome)",
    effect_estimate="Every additional year of slum notification is associated with a 0.768-point decline in the Basic Services Deprivation Score (95% CI -0.914 to -0.622, p<0.001), controlling for slum size, land ownership, location, and state random effects; legal status explains the largest share of variance in deprivation (9.3%) of any covariate; predicted BSDS is 50 for never-notified slums versus 24 for slums notified 40 years; disparity between notified and non-notified slums widened over 1993-2012 (mean BSDS for notified slums declined 34%, p<0.001, versus a non-significant 8% decline for non-notified slums); despite greater deprivation, non-notified slums using 2012 data were found much less likely to receive government slum-improvement-scheme financial aid",
    lower_CI="-0.914", upper_CI="-0.622", standard_error="",
    p_value="<0.001",
    extraction_sample_size="2,390 slums (10 largest states), estimated N=168,901",
    adjusted_or_unadjusted="adjusted (slum size, land ownership, location, area type, community association, survey-year and state random effects)",
    covariates="number of households, land ownership type, slum location (fringe/central), surrounding area type, community association presence, survey year, state random effects",
    model_type="multilevel (mixed-effects) linear regression; multilevel logistic regression (secondary analysis)",
    study_design="quasi-experimental panel regression analysis of repeated national cross-sectional survey data",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: rigorous national multilevel regression analysis across four survey waves and 2,901 slums, directly isolating legal notification status (a formal government legal-recognition mechanism) as the strongest predictor of a services-deprivation index that includes piped water access among its components, with a large, statistically significant, and robust coefficient.",
    source_document="Nolan, Bloom & Subbaraman 2018, IZA Discussion Paper No. 10639 (retrieved via Google Drive)",
    table="Tables 2-5",
    figure="Figures 1-3",
    section="Results: trends in slum notification, trends in access to services, predictors of deprivation",
    exact_location="Section 3, Tables 3-5",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md and matches PROJECT_SPEC.md Family A exposure/outcome definition (legal recognition vs. unrecognized settlement -> water/sanitation access) as closely as any study in the corpus. NOT ADDED TO effect_sizes.csv: despite the very strong regression evidence (beta=-0.768, 95% CI -0.914 to -0.622, p<0.001, per year of notification), the regression's dependent variable is a composite Basic Services Deprivation Score combining piped water, latrines, solid waste disposal, schools, and health centers, not an outcome isolated to water/sanitation access as PROJECT_SPEC.md S8 requires -- matching the S794 Vasquez precedent for excluding regressions on composite/non-water-specific outcomes from the strict effect_sizes table. Table 3's descriptive (non-regression) breakdown does show a widening notified-vs-non-notified gap specifically in 'lack of piped water' prevalence over 1993-2012. Extracted for record_id R3BE9653C9842.",
    )

# S823 - Alvez Marin - Chile constitutional Indigenous water rights
add("S823",
    citation="Alvez Marin A (2016). Constitutional Challenges of the South: Indigenous Water Rights in Chile - Another Step in the 'Civilizing Mission'? Windsor Yearbook of Access to Justice.",
    publication_year="2016",
    country="Chile",
    subnational_unit="national (Mapuche and other Indigenous territories)",
    legal_system="civil law",
    urban_rural="both",
    service_provider="national government (Chilean state, water-rights administrative system)",
    regulatory_model="Constitutional/legal-doctrinal analysis of Chile's 1980 Constitution (adopted under military rule), which established water as a commodity subject to market allocation rules, examining the resulting conflict with Indigenous (Mapuche) ancestral water rights and with ratified international treaties, and evaluating the emancipatory potential of proposals in Chile's 2015 constituent process (including articulating water as a human right) through Third World Approaches to International Law (TWAIL) and Latin American International Law (LAIL) legal scholarship",
    population="Indigenous (Mapuche) peoples and communities in Chile",
    sample_size="constitutional/legal-doctrinal analysis (not a primary empirical sample)",
    household_level="", community_level="TRUE", indigenous_population="TRUE",
    legal_status="TRUE", eligibility="TRUE",
    water_access="TRUE",
    effect_measure="constitutional/legal-doctrinal analysis",
    effect_estimate="Chile's 1980 Constitution's commodification of water as a good subject to market allocation is in direct tension with Indigenous ancestral water-rights claims and with international treaties Chile has ratified; the article traces a continuum of rejection of Indigenous water claims since colonial times, and evaluates whether the 2015 Chilean constituent process's proposals -- including recognizing water as a human right and revisiting national sovereignty over natural resources -- could create constitutional space for non-extractive, non-market Indigenous perspectives on water",
    study_design="constitutional/legal-doctrinal analysis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="3",
    mechanism_certainty="High: direct constitutional/legal-doctrinal analysis of Chile's 1980 water-commodification constitutional provision as the mechanism producing documented conflict with Indigenous water rights, situated within an active 2015 constitutional-reform process.",
    source_document="Alvez Marin 2016, Windsor Yearbook of Access to Justice (retrieved via Google Drive)",
    section="Constitutional water-commodification analysis and Indigenous rights",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: direct constitutional/legal-doctrinal analysis of a water-commodification constitutional provision as an institutional/legal mechanism affecting Indigenous water rights, matching the project's inclusion of doctrinal legal-scholarship articles alongside empirical studies (cf. S815 Bakker et al., Canada). NOT effect_sizes eligible: doctrinal legal analysis, no empirical regression-based estimate. Extracted for record_id R2D16CA4C51A0.",
    )

# S824 - Cook & Wei - China Gansu rainwater harvesting
add("S824",
    citation="Cook S, Wei H (2002). The Anomalous Nature of Development Success: A Case Study from China. Development.",
    publication_year="2002",
    country="China",
    subnational_unit="Gansu province",
    legal_system="civil law (socialist)",
    urban_rural="rural",
    service_provider="provincial and local government (Gansu Water Conservancy Bureau), the '1-2-1' rainwater-harvesting programme",
    regulatory_model="Case study of the government-run '1-2-1' rainwater-harvesting programme in Gansu province, which provided concrete materials for household water-storage tank construction (with villagers supplying sand and labor) to address drinking-water shortages, examining why the programme succeeded where most rural development projects fail, and documenting the programme's inclusion/exclusion mechanisms: villages excluded because they were in remote, road-inaccessible areas or because local government officials failed to identify their water-shortage severity, and households excluded because they lacked sufficient labor or could not afford the sand needed for construction",
    population="rural households in semi-arid Gansu province, China",
    sample_size="qualitative case study drawing on academic, official, and local informant sources; programme reported to have addressed drinking-water problems of over one million people",
    household_level="TRUE", community_level="TRUE", income_group="TRUE",
    eligibility="TRUE", discretion="TRUE", service_area="TRUE",
    water_access="TRUE", affordability="TRUE",
    effect_measure="qualitative government-programme case study",
    effect_estimate="The government-funded '1-2-1' rainwater-harvesting programme successfully solved household drinking-water shortages for over one million people in semi-arid Gansu province by providing construction materials while requiring household labor/sand contributions and household ownership of the resulting tanks (unlike land improvements that remained government property); however, some rural households could not take advantage of the programme because they lacked sufficient labor or could not afford the cost of sand, and many villages in other semi-arid counties still lacked adequate drinking water because they were not included in the programme, either due to remote, road-inaccessible locations or because local government officials failed to perceive the severity of their water shortages",
    study_design="qualitative government-programme case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: case-study documentation of a specific government rural water-supply programme's eligibility and inclusion/exclusion mechanisms (remoteness, local-official identification failures, household labor/material affordability) determining which villages and households gained water access.",
    source_document="Cook & Wei 2002, Development (retrieved via Google Drive)",
    section="Sources of the project's success; discussion of exclusion factors",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: government rural water-supply programme case study documenting specific village- and household-level inclusion/exclusion mechanisms (remoteness, official oversight, affordability of required household contribution). NOT effect_sizes eligible: qualitative case study, no regression-based estimate. Extracted for record_id R003523574784.",
    )

# S825 - Perumal - Mazibuko v City of Johannesburg feminist legal analysis, South Africa
add("S825",
    citation="Perumal DN (2011). Women's socio-economic [in]equality and gender [in]justice: Feminist reflections on the right of access to water in Mazibuko and Others v City of Johannesburg and Others [2009] ZACC 28. Agenda: Empowering Women for Gender Equity.",
    doi="10.1080/10130950.2011.575991",
    publication_year="2011",
    country="South Africa",
    subnational_unit="Phiri, Soweto, City of Johannesburg",
    legal_system="common law (constitutional)",
    urban_rural="urban",
    service_provider="City of Johannesburg and Johannesburg Water (Pty) Ltd, under the Water Services Act 108 of 1997",
    regulatory_model="Feminist legal-doctrinal case analysis of the Mazibuko litigation (High Court, Supreme Court of Appeal, Constitutional Court) challenging Johannesburg's Free Basic Water Policy (6,000 litres/household/month, i.e. 25 litres/person/day under an assumed 8-person household) and the installation of prepayment water meters in the low-income Phiri township, which automatically disconnect water supply once the free allocation is exhausted, examining the Constitutional Court's 'reasonableness' review under section 27 of the Constitution and critiquing the Court's failure to account for the gendered burden of water collection",
    population="poor women residents of Phiri, Soweto, and other low-income households subject to prepayment water meters",
    sample_size="single landmark case analysis with individual-applicant factual narratives",
    household_level="TRUE", community_level="TRUE", income_group="TRUE",
    eligibility="TRUE", fees="TRUE", disconnection="TRUE", discretion_accommodation="TRUE",
    judicial_review="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE", service_continuity="TRUE",
    effect_measure="legal-doctrinal case analysis with individual-applicant factual narratives",
    effect_estimate="Johannesburg's Free Basic Water Policy provided only 6,000 litres/household/month (25 litres/person/day assuming 8 residents) via prepayment meters that automatically disconnect the water supply once exhausted, with no provision for larger households (Phiri households averaged 13-14 members); the High Court initially found the policy unlawful and ordered 50 litres/person/day, the Supreme Court of Appeal set 42 litres/person/day, but the Constitutional Court overturned both, upholding the 25-litre policy and prepayment meters as 'reasonable' and lawful under section 27 of the Constitution; applicants documented routinely running out of water 12-15 days before month's end, forcing reduced bathing/laundry/toilet-flushing and disproportionately burdening women as primary water-collection and household-care providers",
    study_design="legal-doctrinal case analysis (feminist jurisprudential critique)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: direct analysis of a landmark constitutional water-rights case tracing a specific legal/administrative mechanism (prepayment-meter automatic disconnection under a fixed free-basic-water allocation) through three court levels, with detailed factual documentation of household-level water-access consequences and their disproportionate gendered burden.",
    source_document="Perumal 2011, Agenda (retrieved via Google Drive)",
    section="Factual background; High Court, Supreme Court of Appeal, and Constitutional Court decisions; feminist critique",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: detailed legal-doctrinal case analysis of a landmark constitutional water-access case (Mazibuko), with a specific administrative mechanism (prepayment-meter disconnection under a fixed household water allocation) traced through three court levels and documented household-level consequences. NOT effect_sizes eligible: legal case analysis, no regression-based estimate. Extracted for record_id R7B1FE35F1E88.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
