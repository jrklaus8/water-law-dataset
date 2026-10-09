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

# S866 - Mwihaki - Decentralisation, Kenya
add("S866",
    citation="Mwihaki NJ (2018). Decentralisation as a tool in improving water governance in Kenya. Water Policy.",
    doi="10.2166/wp.2018.102",
    publication_year="2018",
    country="Kenya",
    subnational_unit="Thika and Kiambu-west sub-counties",
    legal_system="common law",
    urban_rural="both",
    service_provider="THIWASCO/Athi Water Services Board (Thika); Nairobi City Water and Sewerage Company (Kiambu-west)",
    regulatory_model="Household survey (766 respondents) plus key-informant interviews and secondary government records comparing decentralisation types (pluralism/delegation in Thika vs. de-concentrated/centralised NCWSC control in Kiambu-west) under Kenya's 1974 and 2002 Water Acts, assessing sustainability, accountability, efficiency and effectiveness performance indicators for water and sanitation service delivery in each sub-county",
    population="households in Thika and Kiambu-west sub-counties, central Kenya",
    sample_size="766 households (364 Thika, 402 Kiambu-west) plus key-informant interviews",
    household_level="TRUE", community_level="TRUE",
    institutional_fragmentation="TRUE", political_coordination="TRUE", participation="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE",
    service_coverage="TRUE", service_reliability="TRUE",
    effect_measure="mixed-methods comparative household survey with quantified performance indicators",
    effect_estimate="Thika sub-county, characterised by pluralistic/delegated decentralisation (THIWASCO working jointly with Athi Water Services Board), outperformed the more centralised Kiambu-west (served by NCWSC) across every measured indicator: water losses (15% vs. 45%), service-coverage improvement (2010-2015: 47% to 62% in Thika vs. 33% to 38% in Kiambu-west), repair-time reduction (56% reduction vs. no change), and knowledge of water-price changes (46% vs. 28% of respondents) and evaluation feedback received (36% vs. 4%), demonstrating that decentralisation type/institutional arrangement under the Water Act is directly associated with water-service accountability, efficiency and coverage outcomes",
    study_design="mixed-methods comparative household survey study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: large household survey (n=766) plus key-informant interviews directly comparing two sub-counties operating under different decentralisation arrangements pursuant to a specific national Water Act, with quantified comparative performance indicators.",
    source_document="Mwihaki 2018, Water Policy (retrieved via Google Drive)",
    table="Tables 3, 4, 5, 6, 7 (role distribution, sustainability, accountability, efficiency, effectiveness)",
    section="Results and discussions",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established institutional-fragmentation/devolution-mechanism inclusion precedent (S837 Scott/Moldogaziev/Greer; S840 Grant): large household survey directly comparing water/sanitation service outcomes across sub-counties with differing decentralisation arrangements under a specific national Water Act. NOT effect_sizes eligible: descriptive comparative survey with performance-indicator tables, no regression-based estimate isolating the mechanism's effect. Extracted for record_id RAE228938C27E.",
    )

# S867 - Lenneiye - Community Empowerment Strategies, Zimbabwe
add("S867",
    citation="Lenneiye M (2000). Testing Community Empowerment Strategies in Zimbabwe: Examples from Nutrition Supplementation, and Water Supply and Sanitation Programmes. IDS Bulletin.",
    doi="",
    publication_year="2000",
    country="Zimbabwe",
    subnational_unit="national, with district/village-level programme detail",
    legal_system="common law",
    urban_rural="rural",
    service_provider="Integrated Rural Water Supply and Sanitation Programme (IRWSSP) implemented through Village/Ward/District Development Committees (VIDCO/WADCO/DDC) under the 1985 Prime Minister's Directive on Decentralisation",
    regulatory_model="Documentary institutional case study drawing on programme evaluations and the author's direct involvement, tracing how Zimbabwe's Democratic Development Structures (directly- and indirectly-elected VIDCOs/WADCOs/DDCs, Water Point Committees) were formally assigned legally-binding roles in needs identification, planning, coordination, implementation, advocacy and monitoring of the national rural water supply and sanitation programme from 1980-2000, and how the transition from state-employed to civil-servant Village Community Workers reduced downward accountability",
    population="rural communities in Zimbabwe served by the Integrated Rural Water Supply and Sanitation Programme",
    sample_size="documentary institutional case study drawing on multiple programme evaluations (1984, 1987-88, 1997)",
    household_level="TRUE", community_level="TRUE",
    institutional_fragmentation="TRUE", participation="TRUE", bureaucratic_assistance="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE",
    effect_measure="documentary institutional case study with programme-evaluation evidence",
    effect_estimate="The IRWSSP's formal devolution of needs-identification, planning and water-point-committee-maintenance roles to elected Village/Ward Development Committees improved community participation in siting and maintaining hand-dug wells and boreholes and produced many maintained water points, but implementation consistently fell short of infrastructure targets (in many districts, planned three-year targets for VIP toilets and water points per population were not met even after ten years), and accountability of Village Community Workers to communities was reduced once they became centrally-paid civil servants rather than remaining answerable to the district council, illustrating that formal devolution of programme roles without full fiscal/administrative devolution constrains sustainable water-access outcomes",
    study_design="documentary institutional case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: detailed documentary case study of the formal legal/institutional structures (Democratic Development Structures) governing a specific national rural water programme, drawing on multiple internal programme evaluations spanning two decades.",
    source_document="Lenneiye 2000, IDS Bulletin (retrieved via Google Drive)",
    section="Programming community mobilisation; Critical issues and lessons learnt",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established documentary institutional-case-study inclusion precedent (Derman Zimbabwe; Akpabio Nigeria): case study documenting the formal decentralised governance structures assigned legal roles in a national rural water supply and sanitation programme and their effect on implementation/accountability outcomes. NOT effect_sizes eligible: documentary case study drawing on qualitative programme evaluations, no regression-based estimate. Extracted for record_id RC373C4B7C2DE.",
    )

# S868 - Mbanaso - Urban service delivery, Lagos Festac
add("S868",
    citation="Mbanaso MU (1989). Urban Service Delivery System and Federal Government Bureaucracy: A Structural Analysis of Spatial Distribution of Water Supply in a Suburban Community of Metropolitan Lagos. Dissertation, Portland State University.",
    doi="10.15760/etd.1233",
    publication_year="1989",
    country="Nigeria",
    subnational_unit="Festival Town (Festac), Lagos",
    legal_system="common law",
    urban_rural="urban",
    service_provider="Federal Housing Authority (F.H.A.), Nigerian federal government bureaucracy",
    regulatory_model="Dissertation combining field research, household survey, historical analysis of Nigerian federal-government and F.H.A. budget records/Annual Reports (1977-1987), and extensive interviews of F.H.A. bureaucratic officials, technical personnel and workers, testing patron-client and bureaucratic-decision-rule/structural theoretical models to explain the spatial distribution of water-supply service delivery in a purpose-built federal new town",
    population="residents of Festival Town (Festac), a federally-planned suburb of Lagos",
    sample_size="household survey plus historical/documentary analysis of F.H.A. budget records (1977-1987) and bureaucratic interviews",
    household_level="TRUE", community_level="TRUE",
    bureaucratic_assistance="TRUE", discretion="TRUE", enforcement="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_reliability="TRUE",
    effect_measure="mixed-methods structural/bureaucratic case study with government budget-record analysis",
    effect_estimate="Despite Festac being purpose-planned with modern water infrastructure, water-supply scarcity persisted and mirrored problems found elsewhere in Lagos; the dissertation finds that neither patron-clientelism nor bureaucratic inefficiency alone explains this scarcity, but rather that technology/infrastructural dependence and dwindling federal state revenues -- rooted in the fiscal capacity of the Nigerian federal state and the structural articulation between the export sector and public-service financing -- are the central factors constraining F.H.A.'s capacity to maintain water-service delivery, demonstrating that federal bureaucratic financing structures directly determine household water-access reliability even in a planned new town",
    study_design="mixed-methods structural/bureaucratic case study (dissertation)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: doctoral dissertation combining household survey, extensive interviews of bureaucratic officials, and historical analysis of federal agency budget records directly documenting how federal bureaucratic/fiscal structures determine water-service delivery in a specific planned community.",
    source_document="Mbanaso 1989, Portland State University dissertation (retrieved via Google Drive)",
    section="Abstract; Findings",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established bureaucratic/institutional-mechanism inclusion precedent (S861 Das & Walton, Delhi Jal Board): dissertation combining primary field research, household survey and government budget-record analysis directly documenting how federal bureaucratic/fiscal structures determine household water-service delivery. NOT effect_sizes eligible: structural/historical case study, no regression-based estimate. Extracted for record_id R1CEF7787CF8F.",
    )

# S869 - Silvestre, Marques, Dollery & Correia - Regional consortia, Brazil
add("S869",
    citation="Silvestre HC, Marques RC, Dollery B, Correia AM (2022). Regional consortia and transaction costs for sanitation services in Brazil. Utilities Policy.",
    doi="10.1016/j.jup.2022.101408",
    publication_year="2022",
    country="Brazil",
    subnational_unit="Brazilian municipalities, panel 2013-2020",
    legal_system="civil law",
    urban_rural="both",
    service_provider="Brazilian municipal local governments, individually or through intermunicipal consortia (supra-regional entities) under formal program contracts",
    regulatory_model="Panel-data (1157-1159 observations, 2013-2020) multivariate general linear model regression with bootstrapped stratified sampling, examining the effect of a binary intermunicipal-cooperation variable (municipality engaged in a formal consortium contract for water/sewage service delivery vs. stand-alone provision, pursuant to Brazil's 1988 Constitution decentralisation framework, the 2007 federal sanitation guidelines and the 2020 Sanitation Legal Framework Act) and transaction-cost indicators (asset specificity, contract management complexity) on total sanitation expenditure, water-service coverage and sewage-service coverage",
    population="Brazilian municipalities (local government units) as service owners",
    sample_size="1157-1159 municipality-year panel observations (2013-2020); bootstrapped to 1000 samples at 95% CI, stratified by State",
    household_level="FALSE", community_level="TRUE",
    institutional_fragmentation="TRUE", political_coordination="TRUE", fees="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE", service_coverage="TRUE",
    effect_measure="bootstrapped multivariate GLM regression coefficients (F-Wald test, robust standard errors)",
    effect_estimate="Formal intermunicipal cooperation (consortia) under Brazil's decentralised sanitation legal framework was not a statistically significant predictor of water-service coverage (cooperation coefficient p=.494 in the bootstrapping regression; p=.240 in the parameter-estimation model) but WAS a significant positive predictor of sewage-service coverage (p=.026, F-statistic 4.938) and of total sanitation expenditure (p=.034); investment in water infrastructure (asset specificity) was a significant positive predictor of water-service coverage (p=.000, F-statistic 12.559); cooperating municipalities exhibited lower mean water/sewage coverage overall (M=41.58) than non-cooperating stand-alone municipalities (M=59.45), indicating that the formal legal cooperation mechanism raises transaction costs and expenditure while producing mixed, service-specific effects on coverage outcomes",
    study_design="panel-data regression analysis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: large multi-year municipal panel dataset with a regression model isolating a specific, formally documented legal/institutional mechanism (intermunicipal consortium program contracts under Brazil's constitutional decentralisation and sanitation-legal-framework regime) and its effect on directly-measured water- and sewage-service coverage outcomes.",
    source_document="Silvestre, Marques, Dollery & Correia 2022, Utilities Policy (retrieved via Google Drive)",
    table="Table 3 (Bootstrapping regression), Table 4 (Parameter estimation)",
    section="Empirical strategy; Results and discussion",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md. EFFECT_SIZES ELIGIBLE (Family A/B/C): panel regression isolating a specific documented legal/institutional mechanism (formal intermunicipal cooperation consortium contracts under Brazil's sanitation legal framework) with water/sewage-service coverage as the directly-measured water-access outcome -- distinguished from the S837 Houston precedent (excluded there because the outcome was capital investment/debt, not a water-access measure); here the outcome is literally population-served coverage. Extracted for record_id R7FA19A7B8819.",
    )

# S870 - Cleaver - Rural Water Supply Planning, Nkayi, Zimbabwe
add("S870",
    citation="Cleaver F (1994). Problems in the planning of rural water supply projects: Lessons from Nkayi District, Zimbabwe. Journal of International Development.",
    doi="",
    publication_year="1994",
    country="Zimbabwe",
    subnational_unit="Nkayi District",
    legal_system="common law",
    urban_rural="rural",
    service_provider="colonial and post-independence Zimbabwean state water authorities; NGOs (Lutheran World Federation, UNICEF); Dutch-aid-funded integrated water and sanitation project (1988)",
    regulatory_model="Five-month ethnographic fieldwork study (Leverhulme Trust funded) tracing the historical legacy of state water-supply policy in Nkayi District from the 1920s to 1994 -- including colonial-era borehole siting to serve cattle-grazing/export-trade policy rather than household needs, use of water supplies as an instrument of forced 'African' resettlement policy in the 1940s-50s, and politically-motivated borehole disconnection as punishment during the 1960s-80s liberation war and post-independence security period -- and how this institutional history continues to shape community members' willingness to participate in post-independence community-based waterpoint management",
    population="rural households in Nkayi District, north-western Zimbabwe (population 109,000)",
    sample_size="5 months of ethnographic fieldwork across multiple villages",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", enforcement="TRUE", discretion="TRUE", participation="TRUE",
    formal_connection="TRUE", water_access="TRUE",
    effect_measure="ethnographic case study with historical institutional documentation",
    effect_estimate="Historical state water-supply policies -- boreholes sited for cattle/export-trade purposes rather than household need, water infrastructure used as an instrument of forced resettlement, and borehole disconnection deployed as political punishment against suspected liberation-war sympathizers -- produced lasting community distrust that directly undermines present-day voluntary participation in community-based waterpoint maintenance (e.g., residents disclaiming ownership/responsibility for boreholes installed under forced resettlement, and reluctance to report broken pumps due to historical association of state water officials with political surveillance), demonstrating that the historical legal/institutional character of water-supply provision causally shapes present household and community water-access-management behavior",
    study_design="ethnographic case study with historical institutional analysis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: extended ethnographic fieldwork combined with documentary historical analysis (National Archives of Zimbabwe Native Commissioner reports) directly linking specific historical state water-supply/resettlement/security policies to present-day community water-management participation outcomes.",
    source_document="Cleaver 1994, Journal of International Development (retrieved via Google Drive)",
    section="Throughout (field report)",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established customary/state-institutional-tension inclusion precedent (Akpabio Nigeria; Derman Zimbabwe): ethnographic fieldwork directly documenting how historical state legal/institutional water policy (resettlement, political disconnection) shapes present-day community water-access management. NOT effect_sizes eligible: ethnographic field report, no regression-based estimate. Extracted for record_id RFFE28947EC31.",
    )

# S871 - Ogle - Culture of privatism, 19th c. American city
add("S871",
    citation="Ogle M (1999). Water supply, waste disposal, and the culture of privatism in the mid-nineteenth-century American city. Journal of Urban History.",
    doi="",
    publication_year="1999",
    country="United States",
    subnational_unit="multiple mid-19th-century American cities (Chicago, New York, Boston, Louisville)",
    legal_system="common law",
    urban_rural="urban",
    service_provider="private well/cistern owners; municipal corporations; sanitary reform boards of health",
    regulatory_model="Historical institutional analysis using primary sources (municipal court rulings, sanitary reform reports, Board of Health documents) of mid-19th-century American municipal law and finance, documenting how a 'culture of privatism' -- courts consistently protecting individual property-owner control over 'chargeable real estate' and financing via special assessments in proportion to owner interest, rather than redistributive general taxation -- legally and financially structured resistance to constructing centrally managed municipal waterworks despite available technology and legal/financial mechanisms (special assessments, user taxes, bond issues, state legislative authorization) for doing so",
    population="residents of mid-19th-century American cities",
    sample_size="historical documentary case study (municipal court rulings, sanitary board reports, multiple cities)",
    household_level="FALSE", community_level="TRUE",
    legal_status="TRUE", fees="TRUE", formal_connection="TRUE",
    water_access="TRUE",
    effect_measure="historical documentary institutional analysis with court-ruling and municipal-finance evidence",
    effect_estimate="Mid-19th-century American courts consistently upheld municipal legal doctrine (the 'segmented system') under which property owners financed and controlled the water/sewer services in which they held a chargeable interest, rather than general redistributive taxation for centrally managed waterworks; this legal/financial framework -- not lack of technology or awareness of superior European alternatives -- explains why most mid-century American cities relied on privately-owned wells, cisterns and short private sewer mains rather than centrally managed municipal water systems until the 1870s and later, despite the legal and financial mechanisms (special assessments, bond issues, state legislative authorization) for building such systems having existed since the 1840s",
    study_design="historical institutional case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: detailed historical documentary analysis of specific municipal court rulings and municipal-finance legal doctrine directly explaining variation in the adoption of centrally managed water infrastructure across mid-19th-century American cities.",
    source_document="Ogle 1999, Journal of Urban History (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established historical-institutional-case-study inclusion precedent (S840 Grant, Nashville; S863 Liu Haiyan, Tianjin): historical documentary case study directly linking specific municipal legal doctrine and financing mechanisms to variation in centrally-managed water-infrastructure adoption. NOT effect_sizes eligible: historical documentary case study, no regression-based estimate. Extracted for record_id RF2447F982F89.",
    )

# S872 - Prieto - Chilean water markets, Atacameno
add("S872",
    citation="Prieto M (2016). Practicing costumbres and the decommodification of nature: The Chilean water markets and the Atacameno people. Geoforum.",
    doi="10.1016/j.geoforum.2016.10.004",
    publication_year="2016",
    country="Chile",
    subnational_unit="Atacameno communities, Atacama Desert, II Antofagasta Region",
    legal_system="civil law",
    urban_rural="rural",
    service_provider="Atacameno indigenous community water-user associations (regantes); Chilean state water-rights administration under the 1981 Water Code",
    regulatory_model="Ethnographic fieldwork (participant observation of canal-cleaning/water rituals, interviews) examining how Atacameno indigenous communities have used internal customary rules (costumbres) -- including a formal prohibition on selling water rights to the mining sector and community rules governing internal water distribution -- to subvert and decommodify Chile's radical pro-market Water Code, imposed by the military dictatorship in 1981, which otherwise establishes water rights as freely tradable private property separable from land",
    population="Atacameno indigenous communities (21,015 people per 2002 census) in the Atacama Desert, Chile",
    sample_size="ethnographic fieldwork with participant observation and interviews in multiple Atacameno communities",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", indigenous_population="TRUE", tenure="TRUE", property="TRUE",
    formal_connection="TRUE", water_access="TRUE",
    effect_measure="ethnographic case study with documented customary institutional rules",
    effect_estimate="Although Chile's 1981 Water Code establishes water rights as fully tradable private commodities separable from land, internal customary rules (costumbres) adopted by Atacameno community water-user associations formally forbid the sale of water rights to the mining sector and regulate internal distribution of water among community members in ways that function as institutional barriers to market transactions, meaning that in these communities water rights have not flowed to the highest-value economic use (mining or urban consumption) as neoliberal market theory predicts, demonstrating that community-level customary legal institutions can directly override or subvert a national market-based water-rights legal framework to determine actual water allocation and access outcomes",
    study_design="ethnographic case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: extended ethnographic fieldwork directly documenting specific customary institutional rules that determine water-rights allocation outcomes in direct tension with a specific, well-documented national water-rights legal framework (Chile's 1981 Water Code).",
    source_document="Prieto 2016, Geoforum (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established customary/Indigenous-institutional-tension inclusion precedent (Akpabio Nigeria; Derman Zimbabwe): ethnographic case study directly documenting customary Indigenous institutional rules overriding a national market-based water-rights legal framework. NOT effect_sizes eligible: ethnographic case study, no regression-based estimate. Extracted for record_id REED4B1701A21.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
