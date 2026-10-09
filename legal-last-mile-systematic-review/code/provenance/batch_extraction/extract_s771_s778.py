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

# S771 - Hendry 2016 - Customer Forum, Scotland
add("S771",
    citation="Hendry S (2016). The customer forum - putting customers at the centre of regulating water services. Water Policy.",
    doi="10.2166/wp.2016.199",
    publication_year="2016",
    country="United Kingdom (Scotland)",
    subnational_unit="Scotland",
    legal_system="common law",
    urban_rural="both",
    service_provider="Scottish Water (public corporation), regulated by the Water Industry Commission for Scotland (WICS) under the Water Industry (Scotland) Act 2002 and Water Services (Scotland) Act 2005",
    regulatory_model="Legal/regulatory case study of the Customer Forum, a negotiated-settlement body established under a cooperation agreement between WICS, Scottish Water and the National Consumer Council to represent customers (including affordability/social-tariff considerations for the poor and unserved) in the 2015 strategic price-setting review",
    population="Scottish Water customers, represented through Customer Forum members (consumer, business, licensed-provider representatives)",
    sample_size="single case study (Customer Forum, 2015 strategic review of charges); comparative discussion of the English Customer Challenge Group model",
    household_level="", community_level="TRUE",
    fees="TRUE", institutional_fragmentation="TRUE", participation="TRUE",
    service_area="TRUE", procedural_steps="TRUE",
    affordability="TRUE", service_quality="TRUE",
    effect_measure="qualitative/doctrinal legal-institutional analysis (regulatory process tracing)",
    effect_estimate="The negotiated-settlement Customer Forum model, backed by statutory regulatory authority (WISA, 2005 Act), produced a business-plan agreement incorporating customer/affordability interests in price setting, contrasted with the weaker English Customer Challenge Group model which lacked equivalent regulatory backing",
    study_design="qualitative case study (participant-researcher legal/regulatory analysis)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="Moderate-high: detailed statutory/regulatory analysis (Water Industry (Scotland) Act 2002, Water Services (Scotland) Act 2005) of a specific institutional mechanism (Customer Forum negotiated settlement) for incorporating customer and affordability interests into water-service price regulation, with a comparative English baseline.",
    source_document="Hendry 2016, Water Policy (retrieved via Google Drive, Antigravity batch)",
    section="Sections 2-4 (regulatory model, governance, Customer Forum establishment)",
    exact_location="Sections 2-4",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: detailed statutory/regulatory institutional analysis of customer representation and affordability in water-services price regulation, developed-country context consistent with the project's comparative administrative-law scope (cf. Family A California SGMA precedent, Bakker 2003 foundational theory). NOT effect_sizes eligible: qualitative regulatory process-tracing, no regression-based estimate. Extracted for record_id RF04979D5CC95.",
    )

# S772 - Nagaraj & Namasivayam 2010 - Cuddalore Tamil Nadu
add("S772",
    citation="Nagaraj V, Namasivayam D (2010). Institutions, access, and entitlements to water supply: the case of urban households in the Cuddalore district, Tamil Nadu. International Journal of Regulation and Governance.",
    publication_year="2010",
    country="India",
    subnational_unit="Cuddalore municipality, Tamil Nadu",
    legal_system="common law",
    urban_rural="urban",
    service_provider="Cuddalore municipality (municipal taps), self-provision (groundwater), and water vendors/retail sources",
    regulatory_model="Application of Sen's entitlements approach to analyse institutional arrangements and access inequality between planned/legally-approved urban areas and unplanned slum clusters lying outside the legal purview for water connections in the Cuddalore municipality",
    population="urban households in slum clusters and developed regions, Cuddalore municipality",
    sample_size="100 households (50 slum area, 50 developed area), 2008/09 household survey",
    household_level="TRUE", community_level="TRUE", income_group="TRUE",
    legal_status="TRUE", documentation="TRUE", eligibility="TRUE",
    service_area="TRUE", fees="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_quantity="TRUE", affordability="TRUE",
    effect_measure="descriptive/comparative statistics (per capita water endowment by institution, income group and region)",
    effect_estimate="Households in the legally-approved 'planned urban limit' had access to individual tap connections while slum households in the 'unplanned urban limit' fell outside the legal purview, precluding tap connections and forcing dependence on shared public taps; average per capita water endowment was 51 lpcd in the slum area vs. 95 lpcd in the developed area (74.8 lpcd average); developed-area households accessed 324 litres more per household per day than slum households",
    study_design="cross-sectional household survey with institutional/entitlements analysis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: explicitly identifies planned/unplanned urban-limit legal status as the institutional mechanism determining eligibility for formal water connections, with quantitative per-capita water-access disparities by legal/planning status and income group.",
    source_document="Nagaraj & Namasivayam 2010, International Journal of Regulation and Governance (retrieved via Google Drive, Antigravity batch)",
    table="Tables 1-4",
    section="Water supply institutions; Access to water supply; Entitlements",
    exact_location="Sections on institutional arrangements and per capita water endowment",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: explicit legal/institutional mechanism (planned vs. unplanned urban-limit legal status determining connection eligibility) directly driving quantified water-access inequality, applying Sen's entitlements framework. NOT effect_sizes eligible: descriptive/comparative cross-tabulations by income group and region, not a regression-based estimate isolating the legal mechanism. Extracted for record_id REFCB6826A20A.",
    )

# S773 - Clifford-Holmes et al - South Africa muddled middle
add("S773",
    citation="Clifford-Holmes JK, Slinger JH, de Wet C, Palmer CG. Modelling in the 'Muddled Middle': A Case Study of Water Service Delivery in Post-Apartheid South Africa. In: Social Systems Engineering: The Design of Complexity.",
    publication_year="2016",
    country="South Africa",
    subnational_unit="Greater Kirkwood, Sundays River Valley Local Municipality",
    legal_system="common law (mixed civil/common law, South Africa)",
    urban_rural="both",
    service_provider="Sundays River Valley Local Municipality, operating under the National Water Act (1998) and Water Services Act (1997) legislative framework and the developmental local government (DLG) policy",
    regulatory_model="System dynamics modelling (causal loop diagram) case study of water service delivery grounded in South Africa's post-apartheid legislative framework (National Water Act 1998, Water Services Act 1997), examining the 'muddled middle' -- local government's intersection between national legal frameworks and community-level service delivery -- and its effect on household connection rates and infrastructure capacity gaps",
    population="households in Greater Kirkwood connected to municipal reticulation for water and sanitation",
    sample_size="case study; household waterborne-sanitation coverage rose from 22% (2001) to 77% (2011)",
    household_level="TRUE", community_level="TRUE",
    institutional_fragmentation="TRUE", political_coordination="TRUE",
    delay="TRUE", bureaucratic_assistance="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE", service_coverage="TRUE",
    effect_measure="system dynamics modelling / descriptive case study (causal loop diagram, historical coverage trend)",
    effect_estimate="Waterborne sanitation coverage in Greater Kirkwood rose from 22% (2001, municipality formation) to 77% (2011), driven by the feedback dynamics between demand growth, infrastructure-construction delay, and municipal capacity constrained by the local government/water legislative framework",
    study_design="system dynamics modelling case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="1",
    mechanism_certainty="Moderate: system-dynamics case study explicitly grounded in South Africa's National Water Act 1998 and Water Services Act 1997 legislative framework, modelling how local-government institutional capacity within that legal framework drives household connection-rate and service-coverage outcomes.",
    source_document="Clifford-Holmes, Slinger, de Wet & Palmer, Social Systems Engineering (retrieved via Google Drive, Antigravity batch)",
    figure="Figure 11.1 (causal loop diagram)",
    section="Introduction and modes-of-failure analysis",
    exact_location="Section 11.1 and system dynamics results",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: legal/institutional case study of South African water/local-government legislation's effect on municipal water service delivery capacity, extending the established South African post-apartheid water-governance precedent line (Weaver et al., Sutherland et al.). NOT effect_sizes eligible: system-dynamics/descriptive case study, no regression-based estimate. Extracted for record_id REF1851D5AE3F.",
    )

# S774 - Abubakar 2016 - Abuja quality dimensions
add("S774",
    citation="Abubakar IR (2016). Quality dimensions of public water services in Abuja, Nigeria. Utilities Policy.",
    publication_year="2016",
    country="Nigeria",
    subnational_unit="Abuja (Federal Capital Territory)",
    legal_system="common law",
    urban_rural="urban",
    service_provider="Federal Capital Territory Abuja Water Board and FCTA engineering department",
    regulatory_model="Qualitative case study (in-depth interviews with residents and city officials) examining institutional and governance dimensions -- billing systems, public involvement, institutional efficiency and accountability -- underlying water service quality (reliability, pressure, maintenance, spatial equity) in Abuja",
    population="Abuja residents and city officials",
    sample_size="in-depth interviews with residents (unspecified n) and Abuja Water Board (18) and FCTA engineering department (12) officials",
    household_level="TRUE", community_level="TRUE",
    institutional_fragmentation="TRUE", participation="TRUE", fees="TRUE",
    service_reliability="TRUE", service_quality="TRUE", service_coverage="TRUE",
    effect_measure="qualitative thematic analysis (in-depth interviews and observations)",
    effect_estimate="Lack of institutional efficiency and transparency in water governance, inefficient billing systems, and lack of public involvement were found to undermine water service quality and produce spatial inequality in service delivery across Abuja",
    study_design="qualitative case study (in-depth interviews, observation)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="1",
    mechanism_certainty="Moderate: qualitative institutional-governance case study identifying billing-system design, public-involvement mechanisms, and institutional efficiency/accountability as the drivers of water service-quality and spatial-equity outcomes in Abuja.",
    source_document="Abubakar 2016, Utilities Policy (retrieved via Google Drive, Antigravity batch)",
    section="Findings and discussion; Good water governance",
    exact_location="Sections on quality dimensions and water governance recommendations",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: qualitative institutional/governance case study of billing, public-involvement and institutional-efficiency mechanisms shaping water service quality and spatial-equity outcomes, matching the established institutional-mechanism case-study precedent (cf. Kumasi et al. 2019, Adeoti & Fati 2020). NOT effect_sizes eligible: qualitative interview-based analysis, no regression-based estimate. Extracted for record_id RED1DDE4608AA.",
    )

# S775 - Marson & van Dijk 2016 - Zambia regulation
add("S775",
    citation="Marson M, van Dijk MP (2016). Does the Zambian water sector regulation have pro-poor tools and outcomes? International Journal of Water.",
    publication_year="2016",
    country="Zambia",
    subnational_unit="national (commercial utilities regulated by NWASCO)",
    legal_system="common law",
    urban_rural="both",
    service_provider="Commercial water utilities regulated by the National Water Supply and Sanitation Council (NWASCO)",
    regulatory_model="Case study analysis of NWASCO's regulatory tools -- minimum service level (MSL)/licensing (command-and-control regulation), the Devolution Trust Fund (DTF) financing connections for the urban/peri-urban poor, regulation of alternative/informal providers, tariff regulation, and benchmarking/performance awards -- and their pro-poor water-access outcomes over 13 years",
    population="urban and peri-urban poor households served or unserved by NWASCO-regulated commercial utilities",
    sample_size="analysis of NWASCO official reports (2002-2013) plus interviews with NWASCO staff and representatives of 5 commercial utilities (fieldwork December 2014)",
    household_level="", community_level="TRUE", income_group="TRUE",
    enforcement="TRUE", fees="TRUE", institutional_fragmentation="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE", service_coverage="TRUE",
    effect_measure="document/fieldwork-based regulatory-tool analysis (documentary review + interviews)",
    effect_estimate="Zambian utilities achieved joint efficiency gains and social-performance improvements over 13 years under NWASCO's regulatory tools, though pro-poor regulation was limited by shortage of investment finance for network extension",
    study_design="qualitative regulatory case study (documentary analysis + fieldwork interviews)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="Moderate-high: detailed institutional analysis of a national regulatory body's (NWASCO) specific pro-poor regulatory tools (DTF financing, tariff regulation, informal-provider regulation) and their documented effect on water-access outcomes for the urban/peri-urban poor.",
    source_document="Marson & van Dijk 2016, International Journal of Water (retrieved via Google Drive, Antigravity batch)",
    section="Sections 2-5 (literature review, methodology, regulatory tools analysis, outcomes)",
    exact_location="Sections 2-5",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: detailed regulatory-institutional case study of NWASCO's pro-poor regulatory tools and their water-access outcomes, matching the established regulatory-mechanism precedent line (cf. Hendry 2016, Adeoti & Fati 2020). NOT effect_sizes eligible: qualitative documentary/fieldwork regulatory analysis, no regression-based estimate. Extracted for record_id RED031F3340F7.",
    )

# S776 - Laryea-Adjei & van Dijk 2012 - Ghana decentralisation
add("S776",
    citation="Laryea-Adjei G, van Dijk MP (2012). Changing water governance in Ghana through decentralisation. International Journal of Water.",
    publication_year="2012",
    country="Ghana",
    subnational_unit="Tamale and Savelugu-Nanton districts",
    legal_system="common law",
    urban_rural="both",
    service_provider="Ghana Water Company Limited (GWCL, deconcentrated) in Tamale vs. Community Water and Sanitation Agency (CWSA, established by Act 564 of 1998) and District Assembly (Savelugu-Nanton), under the Local Government Law 1988/Local Government Act 1993 (Act 462) decentralisation framework and the 1992 Constitution of Ghana",
    regulatory_model="Comparative institutional case study of two districts under Ghana's decentralisation legislation (Local Government Law 1988 PNDC Law 207, Local Government Act 1993 Act 462, District Assemblies' Common Fund Act 1993 Act 455, CWSA Act 1998 Act 564), analysing how differing institutional/legal arrangements (deconcentrated GWCL model vs. devolved/plural CWSA-District Assembly model) affect water/sanitation service delivery performance",
    population="households in Tamale (GWCL-served) and Savelugu-Nanton (CWSA/District-Assembly-served) districts",
    sample_size="766 households (402 Tamale, 364 Savelugu-Nanton)",
    household_level="TRUE", community_level="TRUE",
    institutional_fragmentation="TRUE", political_coordination="TRUE", participation="TRUE",
    documentation="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE",
    service_coverage="TRUE", service_reliability="TRUE",
    effect_measure="comparative before/after case-study indicators (effectiveness, efficiency, accountability, sustainability) across two districts under differing decentralisation legislation, 1998-2003",
    effect_estimate="Coverage of safe water: 0% change 1998-2003 in Tamale (deconcentrated GWCL) vs. 263% change in Savelugu-Nanton (devolved/plural CWSA-District Assembly model); water loss 48% (Tamale) vs. 10% (Savelugu-Nanton); repair time reduced by 64% in Savelugu-Nanton with no change in Tamale; reliability days/week increased from >1 to 3 in Savelugu-Nanton vs. decreased from 5 to 2.3 in Tamale",
    study_design="comparative two-district case study (household survey + key informant interviews + documentary analysis)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: explicit statutory analysis (Local Government Act 1993, CWSA Act 1998, District Assemblies' Common Fund Act 1993) combined with a clean two-district natural comparison isolating decentralisation-model type as the institutional mechanism, with large quantified differences in water coverage, reliability, and efficiency outcomes.",
    source_document="Laryea-Adjei & van Dijk 2012, International Journal of Water (retrieved via Google Drive, Antigravity batch)",
    table="Tables 2-7",
    section="Analytical framework; Indications of performance",
    exact_location="Sections 4-5 (analytical framework and performance tables)",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: strong statutory/legal analysis (multiple named decentralisation Acts) combined with a two-district comparison showing large water-access/reliability differences by institutional/legal arrangement. NOT effect_sizes eligible: two-district before/after indicator comparison without regression controlling for confounders, not a regression-based estimate isolating the legal mechanism (consistent with prior treatment of case-comparison studies, e.g. S761 Nzengya ANOVA exclusion). Extracted for record_id REC9BE7729D00.",
    )

# S777 - Sally et al 2014 - Buea Cameroon
add("S777",
    citation="Sally Z, Gaskin SJ, Folifac F, Kometa SS (2014). The effect of urbanization on community-managed water supply: case study of Buea, Cameroon. Community Development Journal.",
    doi="10.1093/cdj/bst054",
    publication_year="2014",
    country="Cameroon",
    subnational_unit="Buea, South West Region",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="Community-managed water scheme (Great Soppo, Wokoko, Molyko, GWM) alongside the public-private CAMWATER/Camerounaise Des Eaux (CDE) utility",
    regulatory_model="Case study examining the ambiguous legal status of urban community-managed water schemes under Cameroonian water law, which assigns urban water supply as the sole responsibility of the utility CDE, leaving community schemes without a clear legal framework or access to institutional/technical support",
    population="households and student hostels served by the GWM community water scheme",
    sample_size="46 households/hostel residents surveyed (of ~130), out of an estimated 1,420 people served",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", documentation="TRUE", eligibility="TRUE",
    institutional_fragmentation="TRUE", bureaucratic_assistance="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_reliability="TRUE",
    effect_measure="descriptive survey statistics and qualitative institutional analysis",
    effect_estimate="88% of surveyed users were forced to supplement community water with unsafe sources due to poor/unreliable service; the Cameroonian water law's exclusive assignment of urban water supply to the utility CDE denies community schemes official institutional/legal recognition, precluding access to technical support needed for sustainable operation",
    study_design="mixed-methods case study (household survey, semi-structured interviews, participant observation)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: explicit legal analysis of how Cameroonian water law's exclusive assignment of urban water-supply responsibility to the CDE utility denies legal recognition to community-managed schemes, directly linked to documented service unreliability and reliance on unsafe alternative sources.",
    source_document="Sally, Gaskin, Folifac & Kometa 2014, Community Development Journal (retrieved via Google Drive, Antigravity batch)",
    table="Tables 1-2",
    section="Changing the Cameroonian legal context of community water",
    exact_location="Section on legal context and conclusions",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: explicit legal-institutional mechanism (Cameroonian water law's exclusive utility mandate denying community schemes legal recognition) directly causing documented water-access/reliability barriers. NOT effect_sizes eligible: descriptive survey statistics, no regression-based estimate. Extracted for record_id REC4A13B5CAD0.",
    )

# S778 - Heller, Rezende & Cairncross 2014 - Brazil public-private pendulum
add("S778",
    citation="Heller L, Rezende SC, Cairncross S (2014). Water and sanitation in Brazil: the public-private pendulum. Proceedings of the Institution of Civil Engineers - Municipal Engineer.",
    doi="10.1680/muen.13.00019",
    publication_year="2014",
    country="Brazil",
    subnational_unit="national, with regional breakdown (North, Northeast, Southeast, South, Centre-West)",
    legal_system="civil law",
    urban_rural="both",
    service_provider="Varying institutional models over time: public administration, municipally-owned enterprises (autarquias), state-owned basic sanitation companies, and private companies, under the Concessions Law No. 8987 (1995), Planasa (1971 national sanitation plan), and the 1891/1934 Constitutions",
    regulatory_model="Historical-institutional case study tracing Brazil's oscillation between public and private WSS management models (Concessions Law 1995, Planasa 1971, constitutional decentralisation), comparing institutional model against household water/sewerage connection coverage across five macro-regions and two time points (2000, 2008/2010)",
    population="urban households in Brazil, by macro-region and institutional service-provider model",
    sample_size="national census/survey data (IBGE 2001, 2009, 2011) across 5 macro-regions and >5,600 municipalities",
    household_level="TRUE", community_level="TRUE",
    institutional_fragmentation="TRUE", political_coordination="TRUE",
    documentation="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE", service_coverage="TRUE",
    effect_measure="descriptive comparative statistics (% house-connection coverage by institutional model and macro-region)",
    effect_estimate="Water supply house-connection coverage by institutional model (2010, national): public administration 78.8%, municipally-owned enterprise 93.1%, state-owned company 89.8%, private company 82.3%; municipally-owned enterprises achieved the highest coverage in most regions; sewerage coverage showed private company management as 'unremarkable' relative to municipally-owned enterprises",
    study_design="historical-institutional case study with descriptive national comparative statistics",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: detailed legal/institutional history (Concessions Law 1995, Planasa 1971) combined with a national quantitative comparison of water/sewerage connection coverage by institutional management model and region, though the comparison is descriptive rather than regression-adjusted for confounders.",
    source_document="Heller, Rezende & Cairncross 2014, Proceedings of the ICE Municipal Engineer (retrieved via Google Drive, Antigravity batch)",
    table="Tables 1-5",
    section="Brief history of WSS management; Swinging between different management models",
    exact_location="Sections 2-3",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: strong historical-legal analysis (Concessions Law No. 8987/1995, Planasa 1971, constitutional decentralisation) combined with a national institutional-model-by-coverage comparison. NOT effect_sizes eligible: descriptive cross-tabulation by institutional model and region, not a regression-based estimate isolating the legal/institutional mechanism controlling for confounders. Extracted for record_id REB42ED2971BB.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
