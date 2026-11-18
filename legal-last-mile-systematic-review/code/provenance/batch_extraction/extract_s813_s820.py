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

# S813 - Hylton & Charles - Sao Paulo favelas
add("S813",
    citation="Hylton E, Charles KJ (2018). Informal mechanisms to regularize informal settlements: Water services in Sao Paulo's favelas. Habitat International.",
    doi="10.1016/j.habitatint.2018.07.010",
    publication_year="2018",
    country="Brazil",
    subnational_unit="Sao Paulo favelas",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="municipal water utility (Sao Paulo)",
    regulatory_model="Semi-structured interviews with water supply decision makers plus two community-level case studies, identifying four informal 'negotiated institution' mechanisms (two forms of municipal-level non-opposition permission, a local elected official signing a law without legal standing, and a unique court-victory instance) that communities use to overcome the legal barrier that informal settlement status poses to formal water-service extension, and examining the resulting effect on de facto tenure security",
    population="favela (informal settlement) residents, Sao Paulo",
    sample_size="semi-structured interviews with water supply decision makers, two community-level case studies",
    household_level="TRUE", community_level="TRUE", tenure_status="TRUE",
    tenure="TRUE", legal_status="TRUE", documentation="TRUE", discretion="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE",
    effect_measure="qualitative case-study analysis (interviews, community case studies)",
    effect_estimate="Informal settlement status is a legal barrier to formal water-service extension in Sao Paulo favelas; communities and decision-makers negotiate four informal mechanisms (municipal non-opposition permissions, a local official's non-legally-binding signed law, and a court victory) to obtain service extension, which improves de facto and perceived tenure security without changing formal legal tenure status; the impact of these 'negotiated institutions' depends on the level of political support from the entity holding eviction power",
    study_design="qualitative case study (semi-structured interviews, community case studies)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: primary interview data with water-supply decision makers directly identifying four specific informal legal/institutional mechanisms used to overcome the formal legal barrier that informal settlement status poses to water-service extension, and their effect on de facto tenure security.",
    source_document="Hylton & Charles 2018, Habitat International (retrieved via Google Drive)",
    section="Findings on negotiated institutions and tenure security",
    exact_location="Sections on the four service-extension approval mechanisms",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: primary interview-based case study directly identifying informal legal/institutional mechanisms overcoming a formal legal barrier (informal settlement status) to water-service extension. NOT effect_sizes eligible: qualitative case study, no regression-based estimate. Extracted for record_id RBDEF2943A1C3.",
    )

# S814 - Costa, Costa, Dias & Welter - Belo Horizonte municipal committees
add("S814",
    citation="Costa GM, Costa HSM, Dias JB, Welter MG (2009). The role of municipal committees in the development of an integrated urban water policy in Belo Horizonte, Brazil. Water Science & Technology.",
    doi="10.2166/wst.2009.742",
    publication_year="2009",
    country="Brazil",
    subnational_unit="Belo Horizonte",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="Municipal Secretariat for Urban Policies (SMURBE) and five municipal deliberative/consultative committees",
    regulatory_model="Interview-based institutional case study of the constitutional and institutional role of five Belo Horizonte municipal committees dealing with water governance (COMPUR, COMUSA, COMAM, CMH, CMS), established under the 1990 Belo Horizonte Organic Law and Municipal Laws 8146 (2000) and 9011 (2005), examining civil-society participatory representation and the main constraints to achieving integrated urban water governance and reducing social inequalities in urban water use",
    population="Belo Horizonte residents (2.2 million), particularly those affected by sanitation and drainage policy",
    sample_size="interviews with selected members of the Municipal Sanitation Committee (COMUSA) and other committee stakeholders",
    household_level="", community_level="TRUE",
    institutional_fragmentation="TRUE", political_coordination="TRUE", participation="TRUE", documentation="TRUE",
    sanitation_access="TRUE", water_access="TRUE",
    effect_measure="qualitative institutional case study (interviews with committee members)",
    effect_estimate="Municipal law (Law 8146/2000, later Law 9011/2005) established mandatory deliberative/consultative committees with equal public-administration/civil-society membership for urban water governance; interviews found the Municipal Sanitation Committee (COMUSA) remained relatively fragile, restricted to discussing administration-initiated proposals rather than developing its own, with over-representation of public administration limiting civil-society influence, and most conflict-resolution decisions made by the executive without consulting COMUSA, constraining the committees' capacity to reduce social inequalities in urban water access",
    study_design="qualitative institutional case study (interviews with committee members)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: direct statutory analysis (named municipal laws establishing participatory water-governance committees) combined with primary interview data documenting specific institutional constraints (over-representation of public administration, restricted committee mandate) limiting the committees' capacity to reduce water/sanitation-related social inequalities.",
    source_document="Costa, Costa, Dias & Welter 2009, Water Science & Technology (retrieved via Google Drive)",
    figure="Figure 1",
    section="Approaching urban water management through the municipal committees; Concluding remarks",
    exact_location="Sections on COMUSA findings and institutional constraints",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: direct statutory/institutional case study of legally-established participatory water-governance committees, with primary interview data on specific institutional constraints. NOT effect_sizes eligible: qualitative institutional case study, no regression-based estimate. Extracted for record_id RBDD2A9AC8690.",
    )

# S815 - Bakker, Simms, Joe & Harris - Indigenous Peoples Canada
add("S815",
    citation="Bakker K, Simms R, Joe N, Harris L. Indigenous Peoples and Water Governance in Canada: Regulatory Injustice and Prospects for Reform. Book chapter.",
    publication_year="2018",
    doi="10.1017/9781316831847.013",
    country="Canada",
    subnational_unit="First Nations reserves, national",
    legal_system="common law",
    urban_rural="both",
    service_provider="federal government (Indigenous water rights, on-reserve infrastructure), provincial governments (fresh water regulation), municipalities (delegated drinking water)",
    regulatory_model="Legal/regulatory analysis of Indigenous water governance injustice in Canada, examining two interrelated dimensions: limited access to safe water (high-risk water systems affecting one-third of on-reserve First Nations people) and exclusion from water governance/management; analyzes the unsettled legal question of whether water is included within Aboriginal title, the fragmented jurisdictional division among federal, provincial, and municipal governments, and historical colonial exclusion of Indigenous peoples from water governance",
    population="Indigenous (First Nations) peoples in Canada, particularly those on reserves with high-risk water systems",
    sample_size="national legal/regulatory case study",
    household_level="", community_level="TRUE", indigenous_population="TRUE",
    institutional_fragmentation="TRUE", legal_status="TRUE", eligibility="TRUE",
    water_access="TRUE", service_quality="TRUE",
    effect_measure="legal/institutional case study (statutory and jurisdictional analysis)",
    effect_estimate="Canada's fragmented water-governance system -- provincial responsibility for fresh water (delegated to municipalities for drinking water) versus federal responsibility for Indigenous water rights and on-reserve infrastructure -- combined with the unresolved legal question of whether water is included within Aboriginal title, produces persistent injustice: high-risk water systems with major deficiencies threaten the health of one-third of First Nations people living on reserves, and Indigenous communities remain historically excluded from water governance and management by the colonial settler state",
    study_design="legal/institutional case study (statutory and jurisdictional analysis)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: direct legal analysis of the unresolved Aboriginal-title water-rights question and the fragmented federal/provincial/municipal jurisdictional division as institutional mechanisms producing documented water-access and water-governance injustice for Indigenous peoples in Canada.",
    source_document="Bakker, Simms, Joe & Harris 2018, book chapter (retrieved via Google Drive)",
    section="Introduction and analysis of regulatory injustice",
    exact_location="Section 10.1 Introduction",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: direct legal/institutional analysis of unresolved Aboriginal-title water rights and fragmented federal/provincial/municipal jurisdiction as mechanisms of documented water-access injustice for Indigenous peoples. NOT effect_sizes eligible: legal/institutional case study, no regression-based estimate. Extracted for record_id RBB42A504E371.",
    )

# S816 - Kibassa - Ileje Tanzania cost recovery
add("S816",
    citation="Kibassa D (2011). The impact of cost recovery and sharing system on water policy implementation and human right to water: a case of Ileje, Tanzania. Water Science & Technology.",
    doi="10.2166/wst.2011.482",
    publication_year="2011",
    country="Tanzania",
    subnational_unit="Ileje district, Itumba ward (4 villages)",
    legal_system="common law",
    urban_rural="rural",
    service_provider="Itumba/Isongole Urban Water Authority, village water committees",
    regulatory_model="Household survey (145 structured questionnaires) assessing the impact of Tanzania's 2002 National Water Policy (NAWAPO) cost-recovery and cost-sharing mandate on water availability, affordability, and human-right-to-water implementation in four villages, examining tariff-setting without user consultation, disconnection/reduced service following price increases, and the water authority's refusal to extend piped service to two villages citing unrecoverable costs",
    population="households in Itumba, Mlale, Yenzebwe, and Ilanga villages, Ileje district",
    sample_size="145 structured questionnaires, purposive sampling across 4 villages plus water authority staff",
    household_level="TRUE", community_level="TRUE", income_group="TRUE",
    fees="TRUE", eligibility="TRUE", service_area="TRUE", disconnection="TRUE",
    water_access="TRUE", affordability="TRUE", service_coverage="TRUE",
    effect_measure="household questionnaire survey with descriptive statistics (SPSS frequency analysis)",
    effect_estimate="Following the 2002 National Water Policy's cost-recovery mandate, water availability in Itumba village decreased from 180 to 60 liters/household/day (2002-2006) as prices rose from 400 to 3,000 TSh/month, with number of operational standpipes falling from 571 to 216 after a further price increase to 5,000 TSh, disconnecting households from taps for non-payment; the water authority denied piped-service requests from Yenzebwe and Ilanga villages, citing that they were outside its area of operation and that costs would not be recoverable, leaving these villages reliant on seasonal rivers; more than 92% of villagers were aware of their human right to water, and disconnection-for-non-payment litigation in South Africa (Constitution Section 27(1)(a)) is cited as a comparative precedent for using rights-based legal claims against cost-recovery-driven service denial",
    lower_CI="", upper_CI="", standard_error="",
    p_value="",
    extraction_sample_size="145 households",
    adjusted_or_unadjusted="unadjusted (descriptive frequency statistics)",
    model_type="descriptive statistics (SPSS frequency/percentage analysis)",
    study_design="household questionnaire survey",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: primary household questionnaire survey (145 households) directly documenting the cost-recovery water policy's effect on service coverage, affordability, and outright denial of piped-service extension to two villages, framed against Tanzania's National Water Policy human-right-to-water provisions.",
    source_document="Kibassa 2011, Water Science & Technology (retrieved via Google Drive)",
    table="Table 1",
    figure="Figure 1",
    section="Research findings and discussion",
    exact_location="Sections on water availability, pricing, and human rights to water",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: primary household questionnaire survey directly documenting cost-recovery water policy's effect on affordability, disconnection, and denial of service extension, framed against a national human-right-to-water policy. NOT effect_sizes eligible: descriptive frequency-analysis survey, no regression-based estimate. Extracted for record_id RBA427862C34C.",
    )

# S817 - Wanda et al - Karonga Town WASH governance, Malawi
add("S817",
    citation="Wanda EMM, Manda M, Kamlomo D, Kushe J, Mphande C, Kaunda J, Msiska O (2017). Governing WASH for disaster risk reduction in Karonga Town, Malawi. International Journal of Disaster Risk Reduction.",
    doi="10.1016/j.ijdrr.2017.09.034",
    publication_year="2017",
    country="Malawi",
    subnational_unit="Karonga Town",
    legal_system="common law",
    urban_rural="urban",
    service_provider="local council (Local Government Act mandate) and Northern Region Water Board (NRWB)",
    regulatory_model="Interview- and documentary-analysis-based case study of WASH governance in the context of disaster risk reduction, examining the absence of a specific local/national WASH legal framework and of a governance structure for the town, and the jurisdictional overlap/disconnect between the local council (mandated by the Local Government Act for governance and enforcement of WASH services) and the Northern Region Water Board, which produces conflicts between the council, NRWB, and residents, with village-oriented rural governance structures imposed on an urban context",
    population="Karonga Town residents",
    sample_size="interviews and documentary analysis",
    household_level="", community_level="TRUE",
    institutional_fragmentation="TRUE", enforcement="TRUE", documentation="TRUE",
    water_access="TRUE", sanitation_access="TRUE",
    effect_measure="qualitative institutional case study (interviews, documentary analysis)",
    effect_estimate="The absence of a specific local and national WASH legal framework for Karonga Town, combined with a governance disconnect between the local council (Local Government Act mandate) and the Northern Region Water Board, creates conflicts between institutional actors and residents and impedes urban-appropriate WASH service delivery, since the imposed governance structure is based on rural, traditional-chief-oriented organizational models rather than urban-focused institutions; this governance gap negatively impacts both routine WASH service delivery and disaster risk reduction",
    study_design="qualitative institutional case study (interviews, documentary analysis)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: primary interview and documentary-analysis data directly identifying the absence of a specific WASH legal framework and jurisdictional fragmentation between the local council and NRWB as the institutional mechanisms undermining WASH governance and service delivery.",
    source_document="Wanda et al. 2017, International Journal of Disaster Risk Reduction (retrieved via Google Drive)",
    section="Findings on WASH governance and institutional arrangements",
    exact_location="Sections on legal framework absence and jurisdictional disconnect",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: primary interview/documentary case study directly identifying an absence of WASH legal framework and jurisdictional fragmentation between local council and NRWB as institutional mechanisms undermining WASH access. NOT effect_sizes eligible: qualitative institutional case study, no regression-based estimate. Extracted for record_id RB932E7855B82.",
    )

# S818 - Wanda, Gulula & Phiri - Mzuzu City appraisal, Malawi
add("S818",
    citation="Wanda EMM, Gulula LC, Phiri G (2012). An appraisal of public water supply and coverage in Mzuzu City, northern Malawi. Physics and Chemistry of the Earth.",
    doi="10.1016/j.pce.2012.09.010",
    publication_year="2012",
    country="Malawi",
    subnational_unit="Mzuzu City",
    legal_system="common law",
    urban_rural="urban",
    service_provider="Northern Region Water Board (NRWB), established under the Waterworks Act No. 17 of 1995",
    regulatory_model="Documentation review (NRWB annual business plans/reports 2004-2009) plus face-to-face and semi-structured interviews with 420 purposively-selected stakeholders (NRWB officials, community leaders, users), appraising inequitable distribution of water points, service unreliability, and financial losses in a statutory water-board service area, and documenting the board's discretionary decision to halt new-connection campaigns in unplanned settlements due to limited infrastructure capacity",
    population="Mzuzu City residents, particularly unplanned/informal settlements",
    sample_size="420 purposively-selected respondents; documentary review 2004-2009",
    household_level="TRUE", community_level="TRUE",
    eligibility="TRUE", discretion="TRUE", service_area="TRUE", fees="TRUE",
    water_access="TRUE", service_coverage="TRUE", service_reliability="TRUE",
    effect_measure="documentation review with descriptive statistics (SPSS) and semi-structured interviews",
    effect_estimate="Only 68% of Mzuzu City's studied population was covered by NRWB (17% piped in-dwelling, 51% via community standpipes); 32% relied on boreholes, unprotected wells, or rivers; unplanned settlements such as Lupaso, Kang'ona, and Ching'ambo had little or no NRWB access because NRWB officials confirmed the board had deliberately slowed new-connection campaigns in unplanned settlements, citing limited infrastructure capacity to manage difficult, non-gridded pipe networks; NRWB's chronic financial losses (net loss of MK521 million in 2007/2008) attributable to high unaccounted-for water (28-36%) and unsustainable loan-servicing costs further constrained its ability to expand equitable coverage",
    study_design="documentation review with structured/semi-structured interviews",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: primary interview data (420 respondents) combined with utility document review directly documenting a statutory water board's discretionary policy of halting new connections in unplanned settlements due to capacity constraints, and the financial-loss mechanisms underlying reduced service expansion.",
    source_document="Wanda, Gulula & Phiri 2012, Physics and Chemistry of the Earth (retrieved via Google Drive)",
    table="Table 1, Table 2",
    figure="Figure 1, Figure 2",
    section="Results and discussion",
    exact_location="Sections 3.1-3.3 (distribution/coverage, financial losses, staffing)",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: primary interview and document-review case study directly documenting a statutory water board's discretionary connection policy excluding unplanned settlements, and the financial mechanisms constraining equitable coverage expansion. NOT effect_sizes eligible: descriptive documentation-review/interview study, no regression-based estimate. Extracted for record_id RB894AA51801F.",
    )

# S819 - Donoso - Urban water pricing, Chile
add("S819",
    citation="Donoso G (2017). Urban water pricing in Chile: cost recovery, affordability, and water conservation. WIREs Water.",
    doi="10.1002/WAT2.1194",
    publication_year="2017",
    country="Chile",
    subnational_unit="national, 53 WSS providers, 13 regions",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="53 privatized regional/local water and sanitation companies, regulated by the Superintendencia de Servicios Sanitarios (SISS)",
    regulatory_model="Institutional/legal case study of Chile's urban water and sanitation (WSS) regulatory framework, analyzing Law 19549 (1988, reformed 1998) establishing separated regulator/provider roles and full-cost-recovery tariffs, the Tariff Law (DFL MOP No. 70/88) and Tariff Act Regulation (DS MINECON 453/89) governing tariff-setting procedure, WSS concession regulation (Decree 1199-2005), and the means-tested subsidy system (using the Encuesta Casen household-income survey) intended to ensure affordability for low-income households, drawing on SISS's own published regulatory-performance reports (2008-2014)",
    population="Chilean urban WSS customers (over 4.5 million clients, 94.4% domestic)",
    sample_size="national regulatory-performance data, 53 WSS providers, SISS annual reports 2008-2014",
    household_level="TRUE", community_level="TRUE", income_group="TRUE",
    fees="TRUE", eligibility="TRUE", documentation="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE", service_quality="TRUE",
    effect_measure="institutional/legal case study with national regulatory-performance statistics",
    effect_estimate="Chile's WSS legal/regulatory framework (separated regulator SISS, full-cost-recovery tariff formula, means-tested subsidy targeting via Encuesta Casen) achieved near-universal urban water coverage (99.9% by 2013, up from 99.3% in 1999) and a large increase in wastewater treatment coverage (10% in 1990 to over 99.8% in 2014); however, the subsidy-targeting mechanism, despite being relatively sophisticated, shows large errors of inclusion and exclusion -- 60% of subsidies accrue to households outside the lowest income deciles -- while only 13.4% of households (665,196 families) receive the affordability subsidy",
    study_design="institutional/legal case study using national regulatory-performance data",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: detailed statutory/regulatory analysis (named laws, decrees, and the SISS regulator's tariff-setting formula and subsidy-targeting mechanism) directly linked to documented national coverage outcomes and quantified subsidy-targeting errors affecting affordability for low-income households.",
    source_document="Donoso 2017, WIREs Water (retrieved via Google Drive)",
    figure="Figures 1-6",
    section="Legal and institutional framework; Performance of the framework; Water tariffs and affordability",
    exact_location="Sections on the legal/institutional framework and subsidy-targeting performance",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: detailed statutory/regulatory case study of a national water-tariff legal framework with documented coverage outcomes and quantified subsidy-targeting errors, matching the Begolli & Lajci (S805) institutional-case-study precedent for national regulatory-framework analyses that do not require original primary interviews. NOT effect_sizes eligible: descriptive regulatory-performance statistics from secondary SISS reports, no regression-based estimate isolating the mechanism's effect. Extracted for record_id RB7A0171C272A.",
    )

# S820 - Komala, Nur & Septanisa - Padang real demand survey, Indonesia
add("S820",
    citation="Komala PS, Nur A, Septanisa S (2020). Real demand survey of the water supply system in Padang city. AIP Conference Proceedings.",
    doi="10.1063/5.0002397",
    publication_year="2020",
    country="Indonesia",
    subnational_unit="Padang city (11 sub-districts)",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="PDAM Kota Padang (regional water company) and PAMSIMAS (community-based water supply)",
    regulatory_model="Household survey (200 samples, stratified random sampling across 11 sub-districts, per Indonesian Minister of Public Works Regulation No. 27/2016 and No. 18/2007) assessing real demand for piped water connection, examining household reasons for non-subscription to the municipal utility (PDAM), connection-fee and monthly-tariff affordability thresholds, and service-reliability complaints among connected households",
    population="households in Padang city, served and unserved by PDAM",
    sample_size="200 household samples across 11 sub-districts",
    household_level="TRUE", community_level="TRUE", income_group="TRUE",
    fees="TRUE", formal_connection="TRUE",
    water_access="TRUE", affordability="TRUE", service_reliability="TRUE", service_continuity="TRUE",
    effect_measure="household survey with descriptive statistics (percentage/frequency analysis)",
    effect_estimate="Of Padang households, 51% were served by PDAM, 44% relied on non-piped sources, and 5% on community-based PAMSIMAS; of unserved households, only 45% expressed interest in a PDAM connection, with 55% uninterested, citing unreliable supply (43%) and excessive cost (42%) as the primary reasons for not subscribing; households' ability to pay a connection fee clustered at IDR 100,000-500,000, and monthly tariff affordability at IDR 50,000-150,000 (roughly 3-10% of household income), figures the study uses to recommend future PDAM tariff and connection-fee design",
    lower_CI="", upper_CI="", standard_error="",
    p_value="",
    extraction_sample_size="200 households",
    adjusted_or_unadjusted="unadjusted (descriptive percentage/frequency statistics)",
    model_type="descriptive statistics (stratified random sampling survey)",
    study_design="household demand/affordability survey",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="1",
    mechanism_certainty="Moderate-high: primary household survey directly quantifying connection-fee and tariff affordability thresholds and reliability-driven non-subscription among unconnected households, though framed as an engineering master-planning demand survey rather than a dedicated legal/institutional mechanism study.",
    source_document="Komala, Nur & Septanisa 2020, AIP Conference Proceedings (retrieved via Google Drive)",
    figure="Figures 4-7, Table 1",
    section="Results and discussion (willingness to obtain PDAM connection and ability to pay)",
    exact_location="Sections on connection willingness and reasons for non-subscription",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: primary household survey directly documenting affordability and reliability barriers to formal water-utility connection. NOT effect_sizes eligible: descriptive percentage/frequency survey analysis, no regression-based estimate. Extracted for record_id RB76C55D87C12.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
