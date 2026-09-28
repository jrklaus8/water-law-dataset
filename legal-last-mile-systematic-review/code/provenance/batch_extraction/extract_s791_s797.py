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

# S791 - Fuente & Bartram - GLAAS pro-poor governance
add("S791",
    citation="Fuente D, Bartram J (2018). Pro-poor governance in water and sanitation service delivery: evidence from Global Analysis and Assessment of Sanitation and Drinking Water surveys. Perspectives in Public Health.",
    doi="10.1177/1757913918788109",
    publication_year="2018",
    country="multiple (global, cross-national GLAAS survey analysis)",
    subnational_unit="national governments, 94-100+ countries responding to GLAAS surveys",
    legal_system="mixed (cross-national)",
    urban_rural="both",
    service_provider="national governments and water/sanitation regulators reporting to UN-Water's GLAAS monitoring programme",
    regulatory_model="Qualitative document analysis and iterative coding of UN-Water GLAAS survey questionnaires and reports (2008-2016) to identify pro-poor governance themes (equity criteria, targeting of vulnerable populations, affordability measures, human right to water) and a quantitative summary of countries' reported policy/regulatory actions to reach the poor",
    population="national governments reporting to GLAAS (94 countries in 2013-2014 survey, more in 2015-2016)",
    sample_size="94-100+ countries per GLAAS survey round, 2008-2016",
    household_level="", community_level="TRUE",
    eligibility="TRUE", fees="TRUE", documentation="TRUE", discretion_accommodation="TRUE",
    water_access="TRUE", sanitation_access="TRUE", affordability="TRUE",
    effect_measure="qualitative document analysis with quantitative cross-country policy-survey summary",
    effect_estimate="Approximately three-quarters of countries reported having policies/plans for both water and sanitation with explicit provisions to reach the poor, but a smaller share had specific financing measures targeting these populations and very few reported consistent implementation; increasing block tariffs (IBTs) were the most commonly reported affordability measure despite strong evidence they are an ineffective/inefficient means of delivering subsidies to the poor; 54% of countries provided no specific examples of affordability measures taken",
    study_design="cross-national policy-document analysis (qualitative coding + quantitative survey summary)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: systematic cross-national analysis of governments' formal pro-poor governance policies (equity criteria, targeting provisions, affordability tariff mechanisms) using primary GLAAS survey response data, finding a substantial implementation gap between stated policy and consistently-applied, effective measures.",
    source_document="Fuente & Bartram 2018, Perspectives in Public Health (retrieved via Google Drive, Antigravity batch)",
    figure="Figures 1-5",
    section="Results",
    exact_location="Sections on GLAAS survey trends and specific pro-poor governance actions",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: original empirical document/data analysis of primary government survey responses (GLAAS) on pro-poor water/sanitation governance policy and its implementation gap, distinct from pure secondary-literature reviews excluded under E05 (cf. Ezeudu 2019, Nallathiga 2011). NOT effect_sizes eligible: qualitative document analysis with descriptive cross-country summary, no regression-based estimate. Extracted for record_id RDE1EDA735C46.",
    )

# S792 - Swatuk & Kgomotso - Botswana Ngamiland
add("S792",
    citation="Swatuk LA, Kgomotso PK (2007). The challenges of supplying water to small, scattered communities in the Lower Okavango Basin (LOB), Ngamiland, Botswana: An evaluation of government policy and performance. Physics and Chemistry of the Earth.",
    doi="10.1016/j.pce.2007.07.036",
    publication_year="2007",
    country="Botswana",
    subnational_unit="Ngamiland District",
    legal_system="common law",
    urban_rural="rural",
    service_provider="Botswana government water supply agencies",
    regulatory_model="Field-based case study evaluating government water-supply policy and performance in remote rural Ngamiland District, examining how limited human/financial resource capacity and a deliberate government policy of under-serving remote areas (to encourage resettlement) produce unresolved water-supply problems",
    population="small, scattered rural communities in Ngamiland District",
    sample_size="critical analysis of government/secondary data, participant observation and key stakeholder interviews, 2004-2006",
    household_level="TRUE", community_level="TRUE",
    eligibility="TRUE", discretion="TRUE", service_area="TRUE",
    institutional_fragmentation="TRUE",
    water_access="TRUE", service_coverage="TRUE",
    effect_measure="qualitative policy-evaluation case study (document analysis, participant observation, interviews)",
    effect_estimate="Despite Botswana's good aggregate national record on water/sanitation coverage, remote Ngamiland communities face serious unresolved supply problems attributable to a deliberate government policy that under-serves remote areas to encourage resettlement, combined with limited institutional capacity and decision-maker complacence",
    study_design="qualitative field-based policy-evaluation case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: field-based case study with primary interview/observation data directly identifying a deliberate government policy of under-serving remote communities as the institutional mechanism driving unresolved rural water-access problems.",
    source_document="Swatuk & Kgomotso 2007, Physics and Chemistry of the Earth (retrieved via Google Drive, Antigravity batch)",
    section="Findings and discussion",
    exact_location="Sections on government policy and institutional capacity",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: field-based case study with original interview/observation data directly identifying a deliberate government under-service policy as the institutional-eligibility mechanism driving rural water-access exclusion. NOT effect_sizes eligible: qualitative policy-evaluation case study, no regression-based estimate. Extracted for record_id RDCFFEDDA5CAF.",
    )

# S793 - Beisheim et al - transnational PPPs
add("S793",
    citation="Beisheim M, Liese A, Janetschek H, Sarre J. Transnational Partnerships: Conditions for Successful Service Provision in Areas of Limited Statehood.",
    publication_year="2014",
    country="Bangladesh, India, Kenya",
    subnational_unit="10 projects across areas of limited statehood",
    legal_system="mixed (common law, South Asia and East Africa)",
    urban_rural="both",
    service_provider="transnational public-private partnerships (PPPs) providing water, sanitation, and food access services",
    regulatory_model="Comparative analysis of 10 projects carried out by two transnational public-private partnerships differing in institutional design and legitimacy, examining conditions (empirical legitimacy, participatory approach, institutional design addressing capacity/monitoring/local-needs-tailoring) under which PPPs successfully provide basic services in areas of limited statehood",
    population="residents of areas of limited statehood served by PPP basic-service projects, Bangladesh/India/Kenya",
    sample_size="10 projects across two transnational PPPs",
    household_level="TRUE", community_level="TRUE",
    institutional_fragmentation="TRUE", participation="TRUE", bureaucratic_assistance="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE",
    effect_measure="comparative qualitative case-study analysis (10 projects)",
    effect_estimate="Partnerships with high empirical legitimacy (achieved through participatory approaches) and appropriate institutional design (providing capacity-development resources, adequate monitoring, local-needs tailoring) were best able to fulfill complex basic-service-provision tasks in areas of limited statehood; projects lacking legitimacy were prone to failure",
    study_design="comparative qualitative case study (10 projects, two PPPs)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="1",
    mechanism_certainty="Moderate-high: comparative analysis of 10 transnational PPP projects directly examining institutional design and legitimacy as mechanisms determining successful basic water/sanitation service provision in areas of limited statehood.",
    source_document="Beisheim et al., journal article (retrieved via Google Drive, Antigravity batch)",
    section="Findings across 10 PPP projects",
    exact_location="Comparative case analysis sections",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: comparative institutional-design case study of transnational PPP water/sanitation service provision in areas of limited statehood, matching CODEBOOK institutional_fragmentation/participation/bureaucratic_assistance fields. NOT effect_sizes eligible: comparative qualitative case study, no regression-based estimate. Extracted for record_id RDC175D72AFE5.",
    )

# S794 - Vasquez - WTP/WTW Guatemala
add("S794",
    citation="Vasquez WF (2015). Willingness to pay and willingness to work for improvements of municipal and community-managed water services. Water Resources Research.",
    doi="10.1002/2014WR015913",
    publication_year="2015",
    country="Guatemala",
    subnational_unit="areas served by municipal and community-managed (CBWO) water systems",
    legal_system="civil law",
    urban_rural="both",
    service_provider="municipal water utilities and community-based water organizations (CBWOs)",
    regulatory_model="Household contingent-valuation survey comparing willingness to pay and willingness to work for water-service improvements under two governance approaches -- municipal management vs. community-managed systems -- within Guatemala's fragmented and ambiguous water-sector institutional framework",
    population="households served by municipal and community-managed water systems, Guatemala",
    sample_size="household contingent-valuation survey (bivariate probit models)",
    household_level="TRUE", community_level="TRUE",
    institutional_fragmentation="TRUE", documentation="TRUE",
    fees="TRUE",
    water_access="TRUE", affordability="TRUE", service_reliability="TRUE",
    effect_measure="bivariate probit regression models of WTP and WTW (contingent valuation)",
    effect_estimate="Households served by municipal systems were willing to pay more than 200% increases in water bills and approximately 19 hours/month in labor for reliable safe-water supply improvements; in contrast, households with community-managed (CBWO) services were not willing to pay or work for improvements despite reporting substantial dissatisfaction with current unreliable service (CBWOs providing less pressure than municipal systems)",
    lower_CI="", upper_CI="", standard_error="",
    p_value="",
    extraction_sample_size="",
    adjusted_or_unadjusted="adjusted (household covariates)",
    covariates="household demographic and economic characteristics",
    model_type="bivariate probit (contingent valuation, WTP/WTW as outcome, not a water-access outcome)",
    study_design="household contingent-valuation survey with governance-type comparison",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="2",
    mechanism_certainty="Moderate: household survey directly comparing two water-governance institutional models (municipal vs. community-managed) and finding starkly different household willingness-to-pay/work for service improvements, within an explicitly fragmented and ambiguous institutional framework, though the outcome (WTP/WTW) is an economic preference rather than an observed water-access outcome.",
    source_document="Vasquez 2015, Water Resources Research (retrieved via Google Drive, Antigravity batch)",
    table="Tables 1-3",
    section="Sections 2-5 (institutional framework, results)",
    exact_location="Sections 2 and 5",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: household-level comparison of municipal vs. community-managed water governance models within Guatemala's fragmented institutional framework. NOT effect_sizes eligible: the bivariate probit models' dependent variables (willingness to pay/work) are economic preference outcomes, not a water-access outcome as required by PROJECT_SPEC.md S8's Family A/B/C framework. Extracted for record_id RDB3CF0A8AAED.",
    )

# S795 - Hailu, Osorio & Tsukada - Bolivia privatization/renationalization (EFFECT_SIZES ELIGIBLE)
add("S795",
    citation="Hailu D, Osorio RG, Tsukada R (2012). Privatization and Renationalization: What Went Wrong in Bolivia's Water Sector? World Development.",
    publication_year="2012",
    country="Bolivia",
    subnational_unit="La Paz, El Alto, Santa Cruz de la Sierra, Cochabamba",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="private concessionaire (La Paz/El Alto), cooperative (Santa Cruz), public utility (Cochabamba)",
    regulatory_model="Difference-in-differences probit regression comparing household piped-water access before/after water-utility privatization in La Paz and El Alto against non-privatized comparison cities (cooperative-managed Santa Cruz, publicly-managed Cochabamba), isolating the causal effect of privatization on access, controlling for household wealth and city fixed effects",
    population="households in four major Bolivian cities, 1996-2005",
    sample_size="household survey panel data (Instituto Nacional de Estadistica de Bolivia), 1996, 2001, 2005",
    household_level="TRUE", community_level="TRUE", income_group="TRUE",
    fees="TRUE", documentation="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE",
    effect_measure="probit difference-in-differences regression (interaction of post-privatization period x privatized-city dummy)",
    effect_estimate="Effect (privatization x post-period interaction) coefficient on household piped-water-access probability, 1996-2005: 0.077 (SE 0.016), p<0.01, and 0.075 (SE 0.015), p<0.01 in alternate model specifications, both statistically significant; the shorter-run 1996-2001 effect was not significant (0.025, SE 0.025); the concessionaire ultimately failed to meet contract targets and tariff increases required for cost recovery led to public outrage that forced renationalization",
    lower_CI="", upper_CI="", standard_error="0.016",
    p_value="<0.01",
    extraction_sample_size="household panel across 4 cities, 1996/2001/2005",
    adjusted_or_unadjusted="adjusted (household wealth controls, city fixed effects)",
    covariates="electricity provision, number of rooms, wall material (wealth proxies), city dummies, year dummy",
    model_type="probit difference-in-differences",
    study_design="quasi-experimental difference-in-differences (comparative multi-city panel)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: genuine quasi-experimental probit DiD design directly isolating water-utility privatization (a legal/institutional ownership-structure mechanism) as the exposure, with a statistically significant regression coefficient (0.077, SE 0.016, p<0.01) on household piped-water access over the 1996-2005 period, while also documenting the eventual renationalization driven by tariff/affordability backlash.",
    source_document="Hailu, Osorio & Tsukada 2012, World Development (retrieved via Google Drive, Antigravity batch)",
    table="Tables 5, 6, 12",
    section="Sections 4-6 (model, results, econometric results)",
    exact_location="Table 12 (regression results)",
    extraction_note="INCLUDE and EFFECT_SIZES ELIGIBLE per PROJECT_SPEC.md Section 8: genuine probit DiD regression directly isolating water-utility privatization as a legal/institutional mechanism, with a real, significant coefficient on piped-water access. Ownership/regulatory-structure exposure does not cleanly map to a defined Family A/B/C category, so synthesis_family is left blank per the S749 Barbosa & Brusca precedent. Extracted for record_id RDAD1B5F3B10E.",
    )

# S796 - Bradlow - Sao Paulo embeddedness/cohesion
add("S796",
    citation="Bradlow BH (2021). Embeddedness and cohesion: regimes of urban public goods distribution. Theory and Society.",
    doi="10.1007/s11186-021-09456-y",
    publication_year="2021",
    country="Brazil",
    subnational_unit="Sao Paulo",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="municipal, state, and federal government agencies distributing housing and sanitation public goods",
    regulatory_model="Comparative-historical case study (original interviews and archival research) of variation over time (1989-2016) in Sao Paulo's local-state governance of housing and sanitation, arguing that sequential configurations of 'embeddedness' (state-civil-society ties) and 'cohesion' (horizontal/vertical bureaucratic coordinating capacity) explain when urban governing regimes achieve programmatic, redistributive public-goods delivery to previously-excluded favela residents",
    population="previously-excluded favela (informal settlement) residents, Sao Paulo",
    sample_size="original interviews and archival research, 1989-2016 period",
    household_level="TRUE", community_level="TRUE",
    institutional_fragmentation="TRUE", political_coordination="TRUE", bureaucratic_assistance="TRUE", participation="TRUE",
    formal_connection="TRUE", sanitation_access="TRUE", water_access="TRUE",
    effect_measure="comparative-historical qualitative analysis (interviews, archival research)",
    effect_estimate="Local government interventions in Sao Paulo produced surprisingly effective redistribution of sanitation and housing between 1989 and 2016 when bureaucratic 'embeddedness' in civil-society movements and cross-agency/cross-scale 'cohesion' were both present, generating the coordinating capacity for programmatic, inclusive public-goods distribution to previously-excluded favela residents",
    study_design="comparative-historical qualitative case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="1",
    mechanism_certainty="Moderate-high: in-depth comparative-historical case study with original interview/archival evidence directly identifying specific bureaucratic-institutional mechanisms (embeddedness, cohesion) that determine whether excluded urban residents gain access to sanitation and housing public goods.",
    source_document="Bradlow 2021, Theory and Society (retrieved via Google Drive, Antigravity batch)",
    section="Findings across the 1989-2016 period",
    exact_location="Comparative-historical analysis sections",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: comparative-historical case study identifying specific bureaucratic-institutional mechanisms (embeddedness, cohesion) determining sanitation/housing access for excluded favela residents, matching CODEBOOK institutional_fragmentation/political_coordination/bureaucratic_assistance fields. NOT effect_sizes eligible: qualitative comparative-historical case study, no regression-based estimate. Extracted for record_id RD93C9D05E8F4.",
    )

# S797 - Britto, Maiello & Quintslr - Rio de Janeiro
add("S797",
    citation="Britto AL, Maiello A, Quintslr S (2018). Water supply system in the Rio de Janeiro Metropolitan Region: open issues, contradictions, and challenges for water access in an emerging megacity. Journal of Hydrology.",
    doi="10.1016/j.jhydrol.2018.02.045",
    publication_year="2018",
    country="Brazil",
    subnational_unit="Rio de Janeiro Metropolitan Region",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="Companhia Estadual de Aguas e Esgotos (CEDAE), the state water company created under Rio de Janeiro's post-1974 metropolitan governance framework",
    regulatory_model="Socio-technical systems case study examining the institutional mechanisms (state water company CEDAE, metropolitan-region governance body, the 1974 complementary law merging municipalities into the metropolitan region) shaping water supply governance and access challenges in the Rio de Janeiro megacity, based on interviews with government institution key informants",
    population="Rio de Janeiro Metropolitan Region residents",
    sample_size="interviews with key informants from government institutions, archival/institutional document analysis",
    household_level="TRUE", community_level="TRUE",
    institutional_fragmentation="TRUE", political_coordination="TRUE", documentation="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_coverage="TRUE",
    effect_measure="qualitative socio-technical/institutional case study (key-informant interviews, archival document analysis)",
    effect_estimate="The 1974 complementary law establishing the Rio de Janeiro Metropolitan Region and creating the state water company CEDAE produced a metropolitan water-governance structure with ongoing institutional contradictions and financial-autonomy constraints, generating open issues and challenges for equitable water access in the megacity",
    study_design="qualitative socio-technical institutional case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: direct institutional/legal analysis (1974 complementary law establishing the metropolitan region and the CEDAE state water company) combined with key-informant interviews from government institutions, tracing the governance structure's effect on ongoing water-access challenges in the Rio de Janeiro megacity.",
    source_document="Britto, Maiello & Quintslr 2018, Journal of Hydrology (retrieved via Google Drive, Antigravity batch)",
    section="Institutional history and socio-technical governance analysis",
    exact_location="Sections on CEDAE creation and metropolitan governance",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: direct legal/institutional case study (1974 complementary law, state water company CEDAE, metropolitan governance body) with primary government key-informant interviews, examining water-access challenges in a major Brazilian metropolitan region. NOT effect_sizes eligible: qualitative socio-technical/institutional case study, no regression-based estimate. Extracted for record_id RD864FBEE0D54.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
