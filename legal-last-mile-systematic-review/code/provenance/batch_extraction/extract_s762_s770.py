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

# S762 - Kumasi, Agbemor & Burr 2019 - Ghana rural water asset management
add("S762",
    citation="Kumasi TC, Agbemor BD, Burr P (2019). Rural water asset management practices in Ghana: the gaps and needs. Water and Environment Journal.",
    doi="10.1111/wej.12396",
    publication_year="2019",
    country="Ghana",
    subnational_unit="Akatsi and East Gonja districts",
    legal_system="common law",
    urban_rural="rural",
    service_provider="District Assemblies / District Water and Sanitation Teams (DWST) under Ghana's decentralised rural water governance framework, regulated by the Community Water and Sanitation Agency (CWSA)",
    regulatory_model="Mixed-methods case study (asset inventory + interviews) of asset management practices and institutional capacity under Ghana's decentralised water-sector governance framework (CWSA Regulations 2011, Legislative Instrument 2007), assessing why the prevailing 'fix on failure' repair model produces high non-functionality and low service levels",
    population="rural water system users and district-level water service institutions",
    sample_size="asset inventory across systems in 2 districts; key informant interviews with district officials",
    household_level="", community_level="TRUE", income_group="",
    institutional_fragmentation="TRUE", political_coordination="TRUE",
    fees="TRUE", enforcement="",
    service_reliability="TRUE", service_continuity="TRUE", service_coverage="TRUE", water_access="TRUE",
    delay="TRUE",
    effect_measure="descriptive/comparative (functionality rates, coverage rates, breakdown durations by district)",
    effect_estimate="East Gonja: 47% water coverage vs 61% in Akatsi; 29% handpump breakdown rate; systems down >18 days/year, failing the reliability indicator; repairs delayed by the time needed to mobilise financing from 'post-paid' users under the fix-on-failure model",
    study_design="mixed-methods case study (asset inventory + key informant interviews)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="2",
    mechanism_certainty="Moderate: descriptive case-study evidence that Ghana's decentralised, post-paid financing/maintenance institutional model ('fix on failure', District Assembly/DWST capacity gaps under CWSA's regulatory framework) produces delayed repairs and reduced rural water-service reliability, but no isolated regression-based estimate of the institutional mechanism's effect.",
    source_document="Kumasi, Agbemor & Burr 2019, Water and Environment Journal (retrieved via Google Drive, Antigravity batch)",
    section="Results and discussion",
    exact_location="Sections on asset inventory findings and rural water governance/decentralisation",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: analyzes an institutional/financing mechanism (decentralised district governance, post-paid cost-recovery model under CWSA's regulatory framework) that determines maintenance responsiveness and hence rural water-service reliability/access, distinguishing it from purely technical asset-management-tool papers (cf. E06 exclusions of Mitchell et al. 2009). NOT effect_sizes eligible: descriptive/comparative case-study statistics, no regression-based estimate isolating the institutional mechanism. Extracted for record_id RF6E405620386.",
    )

# S763 - Nzengya 2015 - Lake Victoria kiosks/master operators DMM
add("S763",
    citation="Nzengya DM (2015). Exploring the challenges and opportunities for master operators and water kiosks under Delegated Management Model (DMM): A study in Lake Victoria region, Kenya. Cities.",
    doi="10.1016/j.cities.2015.04.005",
    publication_year="2015",
    country="Kenya",
    subnational_unit="Lake Victoria region (Kisumu)",
    legal_system="common law",
    urban_rural="urban",
    service_provider="Water utility delegating bulk distribution/kiosk operation to master operators under Kenya's Water Act 2002 commercialisation/DMM framework",
    regulatory_model="Institutional Analysis and Development (IAD) Framework case study of the Delegated Management Model (DMM) -- an institutional arrangement under Kenya's Water Act 2002 -- as applied to master operators and water kiosks",
    population="master operators, kiosk operators, and slum residents purchasing water from kiosks",
    sample_size="qualitative/mixed case study (interviews with master operators, kiosk operators, utility staff)",
    household_level="TRUE", community_level="TRUE", income_group="TRUE", legal_status="",
    discretion_accommodation="TRUE", enforcement="TRUE",
    service_area="TRUE", fees="TRUE", procedural_steps="TRUE", discretion="TRUE",
    institutional_fragmentation="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_reliability="TRUE", affordability="TRUE",
    effect_measure="qualitative/descriptive (IAD framework analysis of DMM outcomes)",
    effect_estimate="DMM modestly lowered water costs and improved utility revenue collection relative to non-DMM baseline, but overall water access had not significantly improved; unreliability persisted due to unintentional pipe damage from vehicles, poor maintenance, and vandalism",
    study_design="qualitative institutional case study (IAD framework)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="1",
    mechanism_certainty="Moderate: qualitative institutional-analysis case study of the DMM delegation arrangement under Kenya's Water Act 2002, companion study to Nzengya 2018 (S761), finding cost/revenue improvements without a corresponding significant improvement in access reliability.",
    source_document="Nzengya 2015, Cities (retrieved via Google Drive, Antigravity batch)",
    section="Findings and discussion",
    exact_location="Sections on master operator performance and kiosk service outcomes",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: applies the formal IAD Framework to Kenya's Water Act 2002 DMM delegation arrangement, directly matching the S761 Nzengya 2018 precedent line. NOT effect_sizes eligible: qualitative/descriptive institutional-analysis findings, no regression-based point estimate. Extracted for record_id RF6B313F45217.",
    )

# S764 - Helgegren et al 2021 - Bolivia multi-regime analysis
add("S764",
    citation="Helgegren I, McConville J, Landaeta G, Rauch S (2021). A multiple regime analysis of the water and sanitation sectors in the Kanata metropolitan region, Bolivia. Technological Forecasting and Social Change.",
    doi="10.1016/j.techfore.2021.120638",
    publication_year="2021",
    country="Bolivia",
    subnational_unit="Kanata metropolitan region (Cochabamba)",
    legal_system="civil law",
    urban_rural="urban and peri-urban",
    service_provider="Individual/community/municipal water and sanitation service regimes, evaluated through institutionalization of infrastructure, actors/organization, internal coordination, sector values, financing, and legislation",
    regulatory_model="Multi-regime institutional analysis identifying individual, community, and municipal water/sanitation service regimes and evaluating each regime's stability across institutionalization dimensions including legislation, financing, and organizational coordination",
    population="households and community/municipal service providers across regime types",
    sample_size="qualitative multi-regime case study (regime-level institutional analysis)",
    household_level="TRUE", community_level="TRUE",
    institutional_fragmentation="TRUE", political_coordination="TRUE",
    fees="TRUE", documentation="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE", service_coverage="TRUE",
    effect_measure="qualitative regime-stability assessment (institutionalization scoring across dimensions)",
    effect_estimate="Individual, community, and municipal regimes show differing degrees of institutional stability; regimes lacking legislative recognition or stable financing show weaker service continuity and coordination",
    study_design="qualitative multi-regime institutional case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="1",
    mechanism_certainty="Moderate: structured qualitative institutional-regime analysis explicitly incorporating legislation as one of the core institutionalization dimensions evaluated for its effect on water/sanitation service regime stability.",
    source_document="Helgegren, McConville, Landaeta & Rauch 2021, Technological Forecasting and Social Change (retrieved via Google Drive, Antigravity batch)",
    section="Regime analysis and discussion",
    exact_location="Sections presenting the multi-regime institutionalization framework and findings",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: formal institutional-regime analysis with legislation as an explicit institutionalization dimension affecting water/sanitation service stability in individual/community/municipal regimes. NOT effect_sizes eligible: qualitative regime-stability assessment, no regression-based point estimate. Extracted for record_id RF69CDD7A3484.",
    )

# S765 - Meeks 2018 - Peru land titling (EFFECT_SIZES ELIGIBLE)
add("S765",
    citation="Meeks R (2018). Property Rights and Water Access: Evidence from Land Titling in Rural Peru. World Development.",
    doi="10.1016/j.worlddev.2017.07.011",
    publication_year="2018",
    country="Peru",
    subnational_unit="rural Peru (PETT land-titling program areas)",
    legal_system="civil law",
    urban_rural="rural",
    service_provider="household-level infrastructure investment and utility connections under varying land-title status",
    regulatory_model="Modified difference-in-differences quasi-experimental design exploiting the phased-in timing of Peru's PETT (Proyecto Especial de Titulacion de Tierras) rural land-titling program to identify the causal effect of land title acquisition on household water, sanitation, and electricity access",
    population="rural households in PETT program areas, disaggregated by title-acquisition status and timing",
    sample_size="n=3,182 household observations (DiD regressions); n=648/1,076/1,480 by title category (descriptive Table 3)",
    household_level="TRUE", community_level="", income_group="",
    tenure="TRUE", property="TRUE", legal_status="TRUE", documentation="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE", service_coverage="TRUE",
    effect_measure="marginal effects (Table 4) and modified difference-in-differences interaction terms (Table 5, program x no-prior-title), OLS/probit-based regression with region fixed effects and household-characteristic controls",
    effect_estimate="Table 4 marginal effects of PETT title: improved water source 0.001 (0.003, ns); sanitation 0.078*** (0.012); electricity 0.071*** (0.015); tanker truck/vendor -0.016 (0.025, ns); river reliance -0.083*** (0.025). Table 5 core DiD estimate (program x no prior title): improved water source 0.005 (0.009, ns) [tanker truck/vendor column]; river 0.043* (0.024); improved water source 0.059** (0.027); sanitation 0.151*** (0.0347); electricity 0.0882** (0.0352)",
    lower_CI="", upper_CI="", standard_error="0.027 (improved water source, core DiD estimate)",
    p_value="<0.05 (improved water source, core DiD estimate)",
    extraction_sample_size="3182",
    adjusted_or_unadjusted="adjusted (region fixed effects, household-characteristic controls)",
    covariates="region fixed effects, household characteristics",
    model_type="modified difference-in-differences (regression-based)",
    study_design="quasi-experimental modified difference-in-differences (phased program rollout)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: a genuine quasi-experimental modified difference-in-differences design exploiting the phased timing of a national land-titling program (PETT), directly isolating land title/tenure security as the exposure, with statistically significant regression coefficients on improved water access (5.9 percentage points, p<0.05), and larger significant effects on sanitation and electricity access.",
    source_document="Meeks 2018, World Development (retrieved via Google Drive, Antigravity batch)",
    table="Tables 3, 4, 5",
    section="Results",
    exact_location="Table 3 (access by title status), Table 4 (marginal effects), Table 5 (modified DiD program x no-prior-title interaction)",
    extraction_note="INCLUDE and EFFECT_SIZES ELIGIBLE per PROJECT_SPEC.md Section 8 Family A framework (legal recognition/tenure): clean quasi-experimental DiD design directly isolating land title acquisition (PETT program) as a legal/institutional mechanism, with a real regression coefficient (0.059, SE 0.027, p<0.05) on improved water source access. Extracted for record_id RF611C2722057.",
    )

# S766 - Jones, Reed & Bevan 2003 - disability WASH
add("S766",
    citation="Jones H, Reed R, Bevan J (2003). Water and sanitation for the disabled in low-income countries. Municipal Engineer (ICE Proceedings).",
    doi="10.1680/muen.2003.156.2.135",
    publication_year="2003",
    country="multiple (global, with field visits to Uganda and Bangladesh)",
    subnational_unit="Uganda and Bangladesh field sites; 17-country e-conference/questionnaire",
    legal_system="mixed (common law and civil law jurisdictions covered)",
    urban_rural="both",
    service_provider="WEDC research project synthesising a literature review, global questionnaire (165 NGOs), 40-participant e-conference across 17 countries, and field visits",
    regulatory_model="WEDC research project examining disability-based institutional/eligibility barriers to WASH access, including legislative commitments (e.g. South Africa disability legislation) not implemented in low-income housing/infrastructure design, and NGO policy-practice gaps in tracking disabled-people participation",
    population="disabled people and WASH service providers/NGOs in low-income countries",
    sample_size="165 surveyed NGOs (questionnaire); 40 e-conference participants across 17 countries; field visits to Uganda and Bangladesh",
    household_level="TRUE", community_level="TRUE",
    eligibility="TRUE", burden="TRUE", hardship_exception="TRUE",
    discretion_accommodation="TRUE", documentation="TRUE",
    participation="TRUE", bureaucratic_assistance="TRUE",
    water_access="TRUE", sanitation_access="TRUE",
    effect_measure="descriptive/qualitative (questionnaire and e-conference synthesis)",
    effect_estimate="South Africa's disability legislation not implemented in low-income housing bathroom design; USAID policy commitment to disability inclusion vs. 165 surveyed NGOs not systematically tracking disabled-people participation in WASH programming",
    study_design="mixed-methods research synthesis (literature review, global questionnaire, e-conference, field visits)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="1",
    mechanism_certainty="Moderate: multi-method WEDC research project documenting disability-based institutional/eligibility exclusion from WASH infrastructure, including a specific legislation-implementation gap (South Africa) and a policy-practice tracking gap across surveyed NGOs.",
    source_document="Jones, Reed & Bevan 2003, Municipal Engineer/ICE Proceedings (retrieved via Google Drive, Antigravity batch)",
    section="Findings and discussion",
    exact_location="Sections on legislative commitments, NGO questionnaire results, and field visit findings",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: documents disability-based eligibility/accommodation barriers (external institutional practices, legislation-implementation gaps) to WASH access, matching CODEBOOK eligibility/burden/hardship_exception fields. NOT effect_sizes eligible: descriptive/qualitative multi-method synthesis, no regression-based point estimate. Extracted for record_id RF564D516EE5E.",
    )

# S767 - Ravnborg & Jensen 2012 - five-country water governance
add("S767",
    citation="Ravnborg HM, Jensen KM (2012). The water governance challenge: the discrepancy between what is and what should be. Water Science & Technology: Water Supply.",
    doi="10.2166/ws.2012.056",
    publication_year="2012",
    country="Bolivia, Mali, Nicaragua, Vietnam, Zambia",
    subnational_unit="Tiraque (Bolivia), Douentza (Mali), Condega (Nicaragua), Con Cuong (Vietnam), Namwala (Zambia) districts",
    legal_system="mixed (civil law and customary/statutory hybrid systems across 5 countries)",
    urban_rural="rural",
    service_provider="wide array of formal and informal institutions (community leaders, water committees, district authorities, ministries, local lawyers, NGOs) called upon to allocate water and mediate access disputes",
    regulatory_model="Comparative institutional analysis (Competing for Water research programme) of the discrepancy between statutory water governance frameworks and actual local water-allocation institutions/practices across 5 countries",
    population="rural households, disaggregated by poverty category, in 5 districts across 5 countries",
    sample_size="714 water-related events documented in sample communities (extrapolated to 6,089 events, 1,954 situations); household poverty survey n=1,995 across 5 districts (400 per district)",
    household_level="TRUE", community_level="TRUE", income_group="TRUE",
    institutional_fragmentation="TRUE", political_coordination="TRUE", participation="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_coverage="TRUE", affordability="TRUE",
    effect_measure="descriptive/comparative statistics and Pearson chi-square tests on institutional-mediation patterns and access outcomes by poverty category",
    effect_estimate="Poor households systematically lose access to water in multiple-use conflicts (domestic users 'won' only 11% of conflictive multiple-use events vs. losing 39%); non-poor households had markedly higher access to public/gravity-fed water schemes (e.g. Tiraque: 86% non-poor vs. 64% poorest households); formal water-mandated institutions (basin/watershed committees) were rarely called upon as third parties compared to community-level or general-mandate authorities (chi-square significant at 0.001 level)",
    study_design="comparative multi-country institutional case study with quantitative event-inventory and household survey components",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: multi-country comparative institutional analysis with quantitative documentation of the informal/formal institutional-mediation mechanisms governing water access and their disproportionate outcomes for poor households, though relying on chi-square/descriptive rather than regression-based estimates.",
    source_document="Ravnborg & Jensen 2012, Water Science & Technology: Water Supply (retrieved via Google Drive, Antigravity batch)",
    table="Tables 1-3",
    section="Competition for water in five rural districts; Water governance in an institutional perspective",
    exact_location="Sections presenting event/situation inventory data and third-party institution tables",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: matches the established informal-governance/customary-institution precedent line (cf. Ranganathan/Munala & Kainz water-mafia precedent), documenting the gap between statutory water-allocation frameworks and actual local institutions, with quantitative evidence of poor households' disadvantaged access outcomes in institutionally-mediated conflicts. NOT effect_sizes eligible: Pearson chi-square tests and descriptive comparisons, not regression-based estimates isolating a legal/institutional mechanism (cf. S724 chi-square precedent). Extracted for record_id RF2B2F583825D.",
    )

# S768 - Smith 2004 - Cape Town corporatization
add("S768",
    citation="Smith L (2004). The murky waters of the second wave of neoliberalism: corporatization as a service delivery model in Cape Town. Geoforum.",
    doi="10.1016/j.geoforum.2003.05.003",
    publication_year="2004",
    country="South Africa",
    subnational_unit="Cape Town (township communities)",
    legal_system="common law (mixed civil/common law, South Africa)",
    urban_rural="urban",
    service_provider="Cape Town local authority water utility, undergoing corporatization/commercialization (1997-2001)",
    regulatory_model="Case study tracing Cape Town's adoption of three cost-recovery policies (credit control measures, disconnections, IKAPA area-wide disconnection practice) as part of the local authority's corporatization/commercialization of water service delivery (1997-2001) and their equity impacts on low-income township households",
    population="low-income township households in Cape Town",
    sample_size="five-year case study (1997-2001) of local authority cost-recovery policy implementation",
    household_level="TRUE", community_level="TRUE", income_group="TRUE",
    fees="TRUE", enforcement="TRUE", disconnection="TRUE", reconnection="TRUE", sanction="TRUE",
    institutional_fragmentation="TRUE",
    water_access="TRUE", service_continuity="TRUE", affordability="TRUE",
    effect_measure="descriptive/comparative case-study analysis (disconnection rates by area, credit-control policy interpretation)",
    effect_estimate="Highest disconnection rates concentrated in poorest township areas; IKAPA area-wide disconnection practice (disconnecting an entire area until all accounts settled) disproportionately affected low-income households; civil society disobedience emerged in response to draconian credit-control measures",
    study_design="qualitative case study (policy process tracing, 1997-2001)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="1",
    mechanism_certainty="Moderate-high: case study directly matching the established Sutherland et al./eThekwini corporatization precedent line, documenting how a local authority's shift to a private-sector-modeled institutional form (corporatization) and its cost-recovery/credit-control/disconnection policies produced disproportionately negative water-access outcomes for low-income township communities.",
    source_document="Smith 2004, Geoforum (retrieved via Google Drive, Antigravity batch)",
    section="Water service delivery at the local level; case study",
    exact_location="Sections on Cape Town cost-recovery policies and disconnection/credit-control practices",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: extends the established Sutherland et al./eThekwini corporatization precedent to Cape Town, analyzing corporatization as a legal/institutional restructuring mechanism producing disconnection-driven water-access barriers for low-income households. NOT effect_sizes eligible: qualitative case-study/policy process-tracing, no regression-based estimate. Extracted for record_id RF289721552FD.",
    )

# S769 - Adeoti & Fati 2020 - Ekiti State Nigeria
add("S769",
    citation="Adeoti O, Fati BO (2020). Barriers to extending piped water distribution networks: The case of Ekiti State, Nigeria. Utilities Policy.",
    doi="10.1016/j.jup.2019.100983",
    publication_year="2020",
    country="Nigeria",
    subnational_unit="Ekiti State",
    legal_system="common law",
    urban_rural="both",
    service_provider="Ekiti State Water Corporation (EKSWC), established and empowered under the Ekiti State Water Corporation Law No. 4 of 1997, CAP E36",
    regulatory_model="Institutional-theory case study (questionnaire survey of EKSWC senior staff plus documentary/legal analysis) identifying barriers to piped water distribution network extension: political interference, limited technical manpower, corruption, lack of government policy, lack of budgetary funding, and inadequate tariff recovery, analyzed against the Ekiti State Water Corporation Law No. 4 of 1997 and Ekiti State Public Procurement Law No. 2 of 2010",
    population="EKSWC senior staff and documentary/legal record; indirectly, ~581 towns/communities in Ekiti State (only 26% served)",
    sample_size="38 of 52 purposively-sampled EKSWC senior staff questionnaires returned (73%)",
    household_level="", community_level="TRUE",
    institutional_fragmentation="TRUE", political_coordination="TRUE",
    fees="TRUE", service_area="TRUE", documentation="TRUE",
    water_access="TRUE", service_coverage="TRUE", formal_connection="TRUE",
    effect_measure="thematic/comparative content analysis (frequency counts of barrier factors reported by respondents, >40% threshold for 'major' factor)",
    effect_estimate="Piped water distribution networks covered only ~26% of towns/communities in Ekiti State (153 of 581); political interference was the most frequently cited barrier; the Ekiti State Water Corporation Law No. 4 of 1997 lacked provisions on implementation targets, cross-sectoral coordination, or extension planning mandates; capital budgetary allocations to EKSWC network extension were near-zero across 2015-2018 (0-0.5% released)",
    study_design="qualitative case study (institutional theory framework; questionnaire + documentary/legal analysis)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: explicit statutory/legal analysis (Ekiti State Water Corporation Law No. 4 of 1997, Ekiti State Public Procurement Law No. 2 of 2010) combined with an institutional-theory framework and staff survey, directly identifying legal/regulatory gaps (missing implementation-target and coordination provisions) as barriers to water-network extension and hence access.",
    source_document="Adeoti & Fati 2020, Utilities Policy (retrieved via Google Drive, Antigravity batch)",
    table="Table 1, 2, 3; Fig. 2",
    section="Results and discussion",
    exact_location="Sections 3.1-3.6 (political interference, technical manpower, corruption, policy, budgetary funding, tariff recovery)",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: strong legal/institutional case study directly citing and analyzing statutory text (Water Corporation Law, Public Procurement Law) as the mechanism constraining piped water network extension. NOT effect_sizes eligible: thematic/frequency-count qualitative analysis, no regression-based estimate. Extracted for record_id RF12971C35B2E.",
    )

# S770 - Novotny et al 2018 - Ethiopia latrines
add("S770",
    citation="Novotny J, Humnalova H, Kolomaznikova J (2018). The social and political construction of latrines in rural Ethiopia. Journal of Rural Studies.",
    doi="10.1016/j.jrurstud.2018.08.003",
    publication_year="2018",
    country="Ethiopia",
    subnational_unit="Kindo-Koysha and Diguna Fango woredas, Wolaita Zone, Southern Nations, Nationalities and Peoples Region",
    legal_system="civil law",
    urban_rural="rural",
    service_provider="Health Extension Program / Community-Led Total Sanitation and Hygiene (CLTSH) campaign under Ethiopia's centralised woreda/kebele administrative system",
    regulatory_model="Mixed-methods case study (household survey + key informant interviews) examining the political construction of latrine adoption in Ethiopia's command-and-control governance system, including formal/semi-formal sanctions (fines, in-kind sanctions, denouncement, arrest) used to enforce latrine construction under the CLTSH campaign",
    population="rural households and health extension workers/kebele leaders in 11 villages",
    sample_size="368 households (structured interviews + direct observation); 20 semi-structured interviews with health workers and village leaders",
    household_level="TRUE", community_level="TRUE",
    enforcement="TRUE", sanction="TRUE", discretion="TRUE",
    sanitation_access="TRUE", service_quality="TRUE",
    effect_measure="binary logistic regression (improved latrine ownership) and descriptive statistics on sanction prevalence",
    effect_estimate="Formal or semi-formal sanctions (fines of 50-100 Ethiopian Birr, in-kind sanctions, denouncement, one-day arrests) reported in two-thirds of surveyed communities to enforce latrine construction under CLTSH; regression on improved latrine ownership found female-headed households significantly less likely to have improved latrines (B=-0.840, SE=0.345, p<0.05); most common reason for initial latrine adoption was 'someone told me I had to' (48% of respondents), indicating coercive institutional pressure rather than voluntary uptake",
    lower_CI="", upper_CI="", standard_error="0.345 (female-headed household coefficient)",
    p_value="<0.05 (female-headed household coefficient)",
    extraction_sample_size="368",
    adjusted_or_unadjusted="adjusted (village-level fixed effects, multiple household/individual covariates)",
    covariates="age, gender, household size, female-headed status, illiteracy, house type, income, livestock, land, water source, water collection time",
    model_type="binary logistic regression (demographic/contextual predictors of latrine ownership, not isolating the sanction/enforcement mechanism as exposure)",
    study_design="mixed-methods case study (household survey + key informant interviews)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="2",
    mechanism_certainty="Moderate: documents a concrete state institutional-enforcement mechanism (command-and-control governance, formal/semi-formal sanctions including fines and arrest) driving sanitation-facility adoption in rural Ethiopia, though the regression analysis models demographic/contextual predictors of latrine ownership rather than isolating the legal-enforcement mechanism itself as the regression exposure.",
    source_document="Novotny, Humnalova & Kolomaznikova 2018, Journal of Rural Studies (retrieved via Google Drive, Antigravity batch)",
    table="Tables 2-7",
    section="National and regional political context of sanitation; Psychosocial factors",
    exact_location="Section 4 (political context, sanctions) and Section 7.1 (motivations for latrine adoption)",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: documents a state enforcement/sanctions institutional mechanism (command-and-control governance, formal fines/arrest) directly shaping sanitation-facility adoption, distinct from the project's established exclusions of pure discourse/perception-clustering studies (cf. Bischoff-Mattson Q-method) because the coercive institutional mechanism is the central, empirically-documented driver of the outcome. NOT effect_sizes eligible: the reported regression isolates demographic/contextual predictors of latrine ownership, not the legal/institutional enforcement mechanism itself as the exposure variable. Extracted for record_id RF0C8946FC9E3.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
