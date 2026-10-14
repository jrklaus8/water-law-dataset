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

# S808 - Koelble & LiPuma - South Africa institutional obstacles
add("S808",
    citation="Koelble TA, LiPuma E (2010). Institutional obstacles to service delivery in South Africa. Social Dynamics.",
    doi="10.1080/02533952.2010.518002",
    publication_year="2010",
    country="South Africa",
    subnational_unit="18 municipalities, Eastern and Western Cape",
    legal_system="common law (mixed, post-apartheid constitutional)",
    urban_rural="both",
    service_provider="municipal government (water, electricity, sanitation, refuse collection)",
    regulatory_model="Detailed institutional case-study profiles of 18 municipalities (metropolitan, city, and rural, stratified by average spending per resident), examining a national service-delivery crisis attributable to skills shortages at the local level and a lack of central-government enforcement of existing financial-control and accountability rules and regulations on municipal officials, despite constitutional commitments to basic-service rights",
    population="residents of 18 South African municipalities across the Eastern and Western Cape",
    sample_size="18 municipality case-study profiles",
    household_level="", community_level="TRUE",
    institutional_fragmentation="TRUE", enforcement="TRUE", political_coordination="TRUE",
    water_access="TRUE", service_coverage="TRUE", sanitation_access="TRUE",
    effect_measure="comparative institutional case-study analysis (18 municipalities)",
    effect_estimate="South Africa's persistent service-delivery crisis (water, sanitation, electricity, refuse collection) is caused primarily by a severe skills shortage in financial and technical matters at the local-government level and by the central state's unwillingness or inability to enforce existing statutory rules and regulations on municipal officials, rather than by demographic pressure or an overall lack of funding; national policy papers (Project Consolidate, the Local Government Turnaround Strategy) had produced very few visible enforcement actions to date",
    study_design="comparative institutional case study (18 municipality profiles)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: detailed comparative case-study analysis directly identifying a lack of central-government enforcement of existing accountability and financial-control regulations, and local-level skills shortages, as the institutional mechanisms driving basic-service (including water/sanitation) delivery failure across 18 municipalities.",
    source_document="Koelble & LiPuma 2010, Social Dynamics (retrieved via Google Drive)",
    table="Table 1",
    section="Methods of inquiry and the cases chosen; Findings",
    exact_location="Sections on institutional obstacles and enforcement failures",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: detailed comparative institutional case study (18 municipalities) directly identifying enforcement-gap and skills-shortage mechanisms driving water/sanitation service-delivery failure. NOT effect_sizes eligible: comparative qualitative case-study analysis, no regression-based estimate. Extracted for record_id RC8E4D27449CF.",
    )

# S809 - Hirvi & Whitfield - clientelist political settlements, Ghana
add("S809",
    citation="Hirvi M, Whitfield L (2015). Public-Service Provision in Clientelist Political Settlements: Lessons from Ghana's Urban Water Sector. Development Policy Review.",
    doi="10.1111/dpr.12095",
    publication_year="2015",
    country="Ghana",
    subnational_unit="Ghana Water Company Limited (national urban water utility)",
    legal_system="common law",
    urban_rural="urban",
    service_provider="Ghana Water Company Limited (GWCL), with private-sector-participation arrangements",
    regulatory_model="Interview- and documentary-evidence-based political-settlement-theory analysis of networks of political interference and informal clientelist practice within Ghana's public urban water utility, examining how the country-specific political settlement shapes the success or failure of private-sector-participation arrangements in public-service provision",
    population="Ghana Water Company Limited customers and staff; national political-economic context",
    sample_size="interviews and documentary evidence (field research, British Academy and Nordic Africa Institute funded)",
    household_level="", community_level="TRUE",
    discretion="TRUE", political_coordination="TRUE", institutional_fragmentation="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_reliability="TRUE",
    effect_measure="qualitative political-economy case study (interviews, documentary evidence)",
    effect_estimate="Clientelist political-settlement dynamics -- patron-client networks and political interference in appointments, contracting, and operational decisions within Ghana Water Company Limited -- shape the success or failure of private-sector-participation arrangements in the urban water sector; understanding the informal institutional context of the specific political settlement is necessary to explain why similar private-sector-participation reforms produce different outcomes across developing countries",
    study_design="qualitative political-economy case study (interviews, documentary evidence)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: primary interview and documentary evidence directly tracing clientelist political-settlement dynamics as the institutional mechanism shaping public water-utility performance and private-sector-participation outcomes.",
    source_document="Hirvi & Whitfield 2015, Development Policy Review (retrieved via Google Drive)",
    section="Findings on political interference and informal practices in GWCL",
    exact_location="Sections on clientelism and political settlement theory applied to Ghana's water sector",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: primary interview and documentary-evidence case study directly tracing clientelist political-settlement dynamics as an institutional mechanism shaping public water-utility governance and service outcomes. NOT effect_sizes eligible: qualitative political-economy case study, no regression-based estimate. Extracted for record_id RC3F88BC83E64.",
    )

# S810 - Kelly-Richards & Banister - Nogales Sonora
add("S810",
    citation="Kelly-Richards SH, Banister JM (2017). A state of suspended animation: Urban sanitation and water access in Nogales, Sonora. Political Geography.",
    doi="10.1016/j.polgeo.2015.04.002",
    publication_year="2017",
    country="Mexico",
    subnational_unit="Nogales, Sonora",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="municipal water/sanitation utility and government officials",
    regulatory_model="Ethnographic and political-geography case study (colonia resident and government-official interactions) of how informal ('invasion') land-tenure status and lack of regularized land titles determine colonia residents' access to piped water and sanitation infrastructure in a rapidly growing US-Mexico border city, examining the ambiguous, unevenly-applied formal/informal governance distinction",
    population="residents of informally-settled colonias, Nogales, Sonora",
    sample_size="ethnographic fieldwork and interviews with residents and government officials",
    household_level="TRUE", community_level="TRUE", tenure_status="TRUE",
    tenure="TRUE", legal_status="TRUE", documentation="TRUE", discretion="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE",
    effect_measure="ethnographic/political-geography case study (resident and official interviews)",
    effect_estimate="Colonia residents in informally-settled ('invasion') neighborhoods of Nogales are caught in a 'state of suspended animation' between hope for and trepidation about ever receiving formal piped water and sanitation infrastructure; officials frame these settlements as 'illegal' and outside formal governance, and land-title regularization functions as a key, ambiguously and unevenly applied axis determining whether and when residents obtain formal service connections",
    study_design="ethnographic political-geography case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: primary ethnographic interview data with both residents and government officials directly documenting land-tenure regularization as the legal/institutional access-control mechanism determining formal water/sanitation connection in informal settlements.",
    source_document="Kelly-Richards & Banister 2017, Political Geography (retrieved via Google Drive)",
    section="Findings on formal/informal governance and services provision",
    exact_location="Sections on land-title regularization and water/sanitation access",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: primary ethnographic interview study directly documenting land-tenure regularization as the legal/institutional access-control mechanism for informal-settlement water/sanitation connection. NOT effect_sizes eligible: ethnographic case study, no regression-based estimate. Extracted for record_id RC2F103D94FC7.",
    )

# S811 - Devas - Cambodia Battambang
add("S811",
    citation="Devas N (1996). Reshaping government at the local level in Cambodia: with an example of urban water supply in Battambang. Public Administration and Development.",
    doi="10.1002/(SICI)1099-162X(199602)16:1<31::AID-PAD843>3.0.CO;2-J",
    publication_year="1996",
    country="Cambodia",
    subnational_unit="Battambang province and town",
    legal_system="civil law (post-communist transitional)",
    urban_rural="urban",
    service_provider="provincial water enterprise (Regie des Eaux) under the Ministry of Industry, plus private vendors and community/NGO provision",
    regulatory_model="Institutional/fiscal case study of Cambodia's post-communist decentralization/recentralization debate and local-government financing constraints, examining the provincial water enterprise's institutional capacity limitations (no clear cost-recovery system pre-1993, dependency on Ministry for capital investment, historic under-coverage) alongside unregulated informal private water vending and community/NGO-provided wells",
    population="Battambang town residents (population ~100,000), served by a mix of formal utility, private vendors, and community sources",
    sample_size="institutional/fiscal case study (ODA Battambang Urban Water Development Project reports)",
    household_level="TRUE", community_level="TRUE", income_group="TRUE",
    institutional_fragmentation="TRUE", fees="TRUE", discretion="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE", service_coverage="TRUE",
    effect_measure="institutional/fiscal case study with descriptive coverage and pricing data",
    effect_estimate="The provincial water enterprise served only about 8% of Battambang town's population (around 1,200 connections) due to institutional capacity constraints (no clear cost-recovery system, dependence on central Ministry for capital investment, colonial-era infrastructure); most residents relied on private water vendors charging 4-5 times the enterprise's tariff, or on communal wells/ponds/rainwater; the enterprise's post-1993 shift to autonomous status, dollar-indexed tariffs, and improved billing raised cost recovery, but expansion remained constrained by weak institutional and regulatory capacity to manage a much larger system or effectively regulate the informal private vending sector",
    study_design="institutional/fiscal case study (documentary/report-based analysis)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: detailed institutional/fiscal case-study analysis directly linking the provincial water enterprise's institutional capacity constraints and lack of cost-recovery/regulatory systems to severely limited (8%) formal water-service coverage, with quantified private-vendor price premiums for the unconnected majority.",
    source_document="Devas 1996, Public Administration and Development (retrieved via Google Drive)",
    section="The case of water supplies in Battambang",
    exact_location="Sections on the water enterprise and expanding water supplies",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: institutional/fiscal case study directly linking water-utility institutional capacity constraints to severely limited formal coverage (8%) and quantified informal-vendor price premiums. NOT effect_sizes eligible: descriptive institutional/fiscal case study, no regression-based estimate. Extracted for record_id RC2ADB3C483ED.",
    )

# S812 - Jimu - Nkolokoti water kiosks, Malawi
add("S812",
    citation="Jimu IM (2008). The role of stakeholders in the provision and management of water kiosks in Nkolokoti, Blantyre (Malawi). Physics and Chemistry of the Earth.",
    doi="10.1016/j.pce.2008.06.017",
    publication_year="2008",
    country="Malawi",
    subnational_unit="Nkolokoti Township, Blantyre",
    legal_system="common law",
    urban_rural="urban",
    service_provider="Blantyre Water Board and Blantyre City Assembly, with kiosk management committees and local political leaders",
    regulatory_model="Case study based on informal observation and formal/semi-structured key-informant interviews, examining incongruent interests and unfulfilled aspirations among stakeholders (city assembly, water utility, local political leaders, water users) managing public water kiosks intended to provide affordable water to households unable to afford private connections, documenting institutional weaknesses/failures of the Blantyre Water Board and Blantyre City Assembly and political interference in kiosk revenue management",
    population="low-income households relying on public water kiosks, Nkolokoti Township",
    sample_size="informal observations plus formal/semi-structured key-informant interviews",
    household_level="TRUE", community_level="TRUE", income_group="TRUE",
    institutional_fragmentation="TRUE", discretion="TRUE", fees="TRUE", participation="TRUE",
    water_access="TRUE", affordability="TRUE", service_reliability="TRUE",
    effect_measure="qualitative stakeholder case study (observation, key-informant interviews)",
    effect_estimate="Political interference and inefficient management of kiosk revenues by multiple overlapping stakeholders (Blantyre Water Board, Blantyre City Assembly, local political leaders, kiosk committees) undermine the intended goal of affordable water access for low-income households through public kiosks; the study challenges the assumption that community involvement alone solves access problems, demonstrating that institutional weaknesses and role-clarity failures among the formal utility and city government are equally decisive",
    study_design="qualitative stakeholder case study (observation, key-informant interviews)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: primary key-informant interviews and observation directly documenting institutional weaknesses of the formal water utility and city government, and political interference in kiosk revenue management, as the mechanisms undermining affordable water access for low-income households.",
    source_document="Jimu 2008, Physics and Chemistry of the Earth (retrieved via Google Drive)",
    section="Findings on stakeholder roles and kiosk management",
    exact_location="Sections on institutional weaknesses and political interference",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: primary key-informant interview and observation study directly documenting institutional weaknesses of the formal water utility/city government and political interference as mechanisms undermining affordable low-income water access via public kiosks. NOT effect_sizes eligible: qualitative stakeholder case study, no regression-based estimate. Extracted for record_id RC00FA37AB2F9.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
