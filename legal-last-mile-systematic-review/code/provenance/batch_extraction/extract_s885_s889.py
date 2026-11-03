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

# S885 - Von Schnitzler - Traveling Technologies, South Africa prepaid meters
add("S885",
    citation="Von Schnitzler A (2013). Traveling Technologies: Infrastructure, Ethical Regimes, and the Materiality of Politics in South Africa. Cultural Anthropology.",
    doi="10.1111/cuan.12032",
    publication_year="2013",
    country="South Africa",
    subnational_unit="Phiri, Soweto, Johannesburg",
    legal_system="common law",
    urban_rural="urban",
    service_provider="Johannesburg Water / City of Johannesburg, via the Operation Gcin'amanzi prepaid water-meter conversion project",
    regulatory_model="Ethnographic and genealogical study of prepaid water/electricity meters as a legal/technical enforcement mechanism, tracing the meter's history (Victorian Britain, late-apartheid counterinsurgency against rent boycotts) and ethnographic fieldwork with metering-industry engineers and Soweto/Phiri residents during Operation Gcin'amanzi, a multiyear project converting flat-fee unmetered water connections to prepaid meters that impose automatic self-disconnection for non-advance-payment, including the resulting Mazibuko constitutional court case in which five Phiri residents unsuccessfully challenged the legality of prepaid water meters",
    population="residents of Phiri, Soweto, and the broader Johannesburg metropolitan area",
    sample_size="long-term ethnographic fieldwork with residents, engineers and utility officials; documentary/genealogical analysis",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", fees="TRUE", enforcement="TRUE", disconnection="TRUE", judicial_review="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_continuity="TRUE",
    effect_measure="ethnographic and genealogical case study, including documented constitutional litigation",
    effect_estimate="Operation Gcin'amanzi's conversion of Soweto households from unmetered flat-fee water connections to prepaid meters requiring advance payment to avoid automatic self-disconnection provoked sustained protest and low-intensity technical resistance (residents bypassing/disabling meters to obtain de facto free water), and was formally challenged in the Mazibuko constitutional court case by five Phiri residents (ultimately unsuccessful) as violating the constitutional right to sufficient water; the study documents how a specific legal/technical enforcement mechanism (the prepaid meter, embedding automatic self-disconnection) directly reconfigures the terms and continuity of household water access and becomes itself a site of legal and political contestation over the right to water",
    study_design="ethnographic case study with genealogical/documentary analysis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: extended ethnographic fieldwork combined with documentary/legal analysis (including the Mazibuko constitutional court case) directly documenting a specific technical/legal enforcement mechanism (prepaid water meters with automatic self-disconnection) and its contested effects on household water-access continuity.",
    source_document="Von Schnitzler 2013, Cultural Anthropology (retrieved via Google Drive)",
    section="Tracking the Life of the Prepaid Meter",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established prepaid-meter/disconnection-enforcement inclusion precedent: ethnographic and legal-documentary study directly documenting a specific enforcement mechanism (prepaid meters, automatic self-disconnection) and litigated contestation over its effect on water-access continuity. NOT effect_sizes eligible: ethnographic/documentary case study, no regression-based estimate. Extracted for record_id RC8422265D240.",
    )

# S886 - Brown - Unequal burden, Tanzania water privatisation and women's rights
add("S886",
    citation="Brown R (2010). Unequal burden: water privatisation and women's human rights in Tanzania. Gender & Development.",
    doi="10.1080/13552071003600042",
    publication_year="2010",
    country="Tanzania",
    subnational_unit="Dar es Salaam",
    legal_system="common law",
    urban_rural="urban",
    service_provider="City Water (Biwater/Gauff/Superdoll consortium), under a concession contract with Dar es Salaam Water and Sewerage Authority (DAWASA), later replaced by publicly-owned Dar es Salaam Water and Sewerage Corporation (DAWASCO)",
    regulatory_model="Documentary/policy analysis of Tanzania's late-1990s/2000s privatization of the Dar es Salaam municipal water utility, tracing the specific concession contract with City Water (US$164.6 million project, only US$8.5 million private investment), its termination in 2005 after government allegations of contract non-performance, the resulting ICSID arbitration claim, and gendered impacts documented via a Tanzania Gender Networking Programme (TGNP) household study (n=40) on HIV/AIDS home-based caregiving water burdens",
    population="women and girls in Dar es Salaam and rural Tanzania affected by water privatization and access disparities",
    sample_size="TGNP household study (n=40) on HIV/AIDS caregiving water burden; documentary/policy analysis of the privatization contract and its termination",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", fees="TRUE", enforcement="TRUE", disconnection="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE",
    effect_measure="documentary policy analysis with supporting household survey data",
    effect_estimate="Under the City Water concession contract, only 4% of Dar es Salaam households had a direct water connection by 2003, and 98% of water-sector spending in Dar es Salaam had gone to improving access for the wealthiest 20% of the population; after service deterioration, rising prices and disconnections for non-payment, the government terminated the contract in 2005, triggering an ICSID arbitration claim by City Water; a TGNP survey of 40 households found that 31 reported greatly increased water needs due to HIV/AIDS home-based care burdens, with 35 of the 40 primary caregivers being women, and one household reporting paying Tshs 4,500/day for water against a national average annual income of US$760, demonstrating that a specific privatization concession-contract mechanism produced gender-differentiated, highly unequal water-access and affordability outcomes",
    study_design="documentary policy analysis with supporting household survey data",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: documentary analysis of a specific, well-documented privatization concession contract and its termination, combined with quantified TGNP household survey data on gendered water-access/affordability burdens.",
    source_document="Brown 2010, Gender & Development (retrieved via Google Drive)",
    section="The privatisation of water in Tanzania; Women in Tanzania respond",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established water-privatization concession-contract inclusion precedent (S884 Estache & Grifell-Tatje, Mali): documentary analysis of a specific privatization contract's termination and gendered household-level access/affordability impacts, with supporting quantified survey data. NOT effect_sizes eligible: documentary policy analysis with descriptive survey statistics, no regression-based estimate. Extracted for record_id RC819F87A16F8.",
    )

# S887 - Marcos - Governing Urban Water in a Decentralized System, Zamboanga Peninsula
add("S887",
    citation="Marcos AR (2024). Governing Urban Water in a Decentralized System: Institutions, Incentives, and Utility Performance across Cities in the Zamboanga Peninsula, Philippines. Lex Localis - Journal of Local Self-Government.",
    doi="",
    publication_year="2024",
    country="Philippines",
    subnational_unit="Zamboanga City, Pagadian City, Dipolog City, Dapitan City, Isabela City (Region IX, Zamboanga Peninsula)",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="local water districts operating under the Local Water Utilities Administration (LWUA), regulated by the National Water Resources Board (NWRB), under the Local Government Code of 1991",
    regulatory_model="Comparative case-design study using publicly verifiable secondary administrative data (2022-2024, utility performance reports and administrative records) across five cities to trace how a multi-level institutional/incentive framework -- national regulators (NWRB), sector financing/technical-assistance agency (LWUA), local government units, and city water districts -- produces divergent water-governance outcomes despite a common national legal framework (Local Government Code 1991), examining tariff-setting authority, access to national financing, technical capacity, and cross-agency coordination mechanisms",
    population="urban water-district customers across five cities in the Zamboanga Peninsula, Philippines",
    sample_size="comparative case-design study, 5 cities, secondary administrative/utility performance data 2022-2024",
    household_level="FALSE", community_level="TRUE",
    institutional_fragmentation="TRUE", enforcement="TRUE", fees="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_coverage="TRUE", service_reliability="TRUE",
    effect_measure="comparative case-design study with quantified utility performance indicators (coverage, continuity, non-revenue water)",
    effect_estimate="Despite operating under a common national legal framework (the 1991 Local Government Code and shared NWRB/LWUA regulatory oversight), the five Zamboanga Peninsula cities showed persistent intra-regional disparities in water-service coverage, continuity of supply, and non-revenue water; outcomes tracked less with formal decentralization status than with fragmented institutional mandates, weak regulatory enforcement, politically constrained tariff governance, and limited performance-linked financing -- larger systems (Zamboanga City) achieved the highest coverage but also the highest system losses, while smaller systems (Pagadian, Dipolog, Dapitan, Isabela) had lower coverage and more intermittent supply with only marginally better efficiency, demonstrating that institutional fragmentation and incentive misalignment, not the formal legal decentralization framework itself, drive water-access disparities across administratively similar cities",
    study_design="comparative case-design study using secondary administrative data",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: comparative multi-city case-design analysis using official utility administrative data directly documenting how institutional fragmentation and incentive structures under a shared national legal framework (LWUA/NWRB regulatory system) produce divergent water-access outcomes across cities.",
    source_document="Marcos 2024, Lex Localis - Journal of Local Self-Government (retrieved via Google Drive)",
    section="Empirical findings; Theory and Literature Review",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established institutional-fragmentation/multi-city comparative inclusion precedent (S873 Kim, Malaysia; S837 Scott/Moldogaziev/Greer, Houston): comparative case-design study directly documenting how institutional fragmentation under a shared national legal/regulatory framework produces water-access disparities across cities, with quantified utility performance indicators. NOT effect_sizes eligible: comparative case-design study with descriptive/qualitative institutional comparison, no regression-based estimate isolating a specific mechanism. Extracted for record_id RC660CF868FA0.",
    )

# S888 - Kornberg - Structural Origins of Territorial Stigma, Detroit
add("S888",
    citation="Kornberg D (2016). The Structural Origins of Territorial Stigma: Water and Racial Politics in Metropolitan Detroit, 1950s-2010s. International Journal of Urban and Regional Research.",
    doi="10.1111/1468-2427.12343",
    publication_year="2016",
    country="United States",
    subnational_unit="City of Detroit and surrounding suburban municipalities, Michigan",
    legal_system="common law",
    urban_rural="both",
    service_provider="Detroit Water and Sewerage Department (DWSD), superseded in 2016 by the regionalized Great Lakes Water Authority",
    regulatory_model="Historical institutional case study combining archival newspaper analysis (750+ Detroit News articles, 1999-2014), primary DWSD annual reports and ordinances obtained via a Freedom of Information Act request, City Clerk financial records, and stakeholder interviews, tracing how DWSD's 1950s-1960s infrastructure expansion (serving 96 suburban wholesale-customer municipalities by 1973, financed by $147.5 million in bonds against inaccurate population growth projections) created a structurally overbuilt, high-cost regional water system that became a site of racialized political contestation once a black mayor (Coleman Young) took office in 1974, with suburban leaders using judicial and state-legislative channels to contest rate increases and governance structure",
    population="residents of the City of Detroit and its water-system-connected suburban municipalities, Michigan",
    sample_size="750+ archival newspaper articles; DWSD annual reports 1970-2011 (FOIA-obtained); ordinances and financial statements; 4 stakeholder interviews",
    household_level="FALSE", community_level="TRUE",
    legal_status="TRUE", institutional_fragmentation="TRUE", fees="TRUE", enforcement="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_reliability="TRUE",
    effect_measure="historical institutional case study with archival/documentary quantitative data",
    effect_estimate="DWSD's 1956-1973 infrastructure expansion under director Gerald Remus grew the system from serving 44 to 96 suburban wholesale-customer municipalities based on population projections (7.15 million regional residents by 2000) that proved drastically overstated (actual 2000 population was 4.68 million, only 65% of the 1959 projection), producing a structurally overbuilt and expensive system; the resulting cost burden, combined with the 1974 transition to a black-led city administration, triggered organized suburban political resistance via judicial claims over unfair rate increases and state-legislative efforts to replace the Detroit-run department with a suburban-majority board, demonstrating how specific historical infrastructure-financing and governance-structure decisions produced durable racialized institutional conflict over regional water-system access and control",
    study_design="historical institutional case study (archival/FOIA-based)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: FOIA-obtained primary agency records, archival newspaper analysis, and financial/ordinance documents directly tracing specific historical infrastructure-financing and governance decisions to durable racialized institutional conflict over regional water-system administration and access.",
    source_document="Kornberg 2016, International Journal of Urban and Regional Research (retrieved via Google Drive)",
    table="Table 1 (1959 population projections vs. actual census data)",
    section="The structural problem: an overbuilt water system; Generating stigma to reduce costs",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established historical institutional case-study inclusion precedent, extended here to a specifically water-focused (not merely water-adjacent) racialized-politics analysis distinguished from the excluded Presbey/Safransky Detroit precedent (water as minor topic in broader analysis): the entire study concerns DWSD administration and racial politics of regional water governance. NOT effect_sizes eligible: historical institutional case study, no regression-based estimate. Extracted for record_id RBEA8F34FFA53.",
    )

# S889 - Hasna - Street Hydrant Project, Chittagong
add("S889",
    citation="Hasna MK (1995). Street Hydrant Project in Chittagong Low-Income Settlement. Environment and Urbanization.",
    doi="",
    publication_year="1995",
    country="Bangladesh",
    subnational_unit="Chittagong",
    legal_system="common law",
    urban_rural="urban",
    service_provider="Chittagong Water Supply and Sewerage Authority (CWASA)",
    regulatory_model="Participatory action-research case study (Participatory Urban Appraisal, PUA) in a ~200-household low-income Chittagong settlement, documenting CWASA's institutional responsibility for 588 street hydrants (serving an estimated 0.2 million people, versus 21,000 household connections serving 0.4 million people), the Authority's practice of sealing off non-functioning hydrants and considering water meters/per-household charging after donor (Asian Development Bank) financing ended, and a community-led process to design a formal Water Committee with defined tariff collection, caretaker payment, and payment-default sanction rules for community-based hydrant management",
    population="approximately 200 households and shops in a low-income Chittagong settlement served by street hydrants",
    sample_size="participatory action-research with a 10-person PUA team over 3 days; long-term researcher engagement",
    household_level="TRUE", community_level="TRUE",
    tenure_status="TRUE", fees="TRUE", enforcement="TRUE", participation="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE",
    effect_measure="participatory action-research case study",
    effect_estimate="CWASA's street-hydrant system served the lowest-income segment of Chittagong's population (0.2 million people via 588 hydrants, versus 0.4 million via 21,000 household connections held by better-off residents), with the Authority unilaterally sealing off non-functioning hydrants and, after donor financing ended, proposing household metering/charging without prior community consultation; the participatory process documented the community's own design of a formal Water Committee (identifying caretaker couples, a rent collector, a flat monthly tariff rate, allocation of revenue to caretaker wages/utility bill payment/a repair fund, and sanctions for payment defaults), illustrating both the institutional exclusion embedded in the pre-existing hydrant-access system and a community-negotiated institutional alternative for formalizing tariff-based access and maintenance responsibility",
    study_design="participatory action-research case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: long-term participatory action-research fieldwork directly documenting a specific municipal water-authority institutional mechanism (street-hydrant system, unilateral sealing/metering decisions) and a community-negotiated formal governance alternative (Water Committee with tariff/sanction rules).",
    source_document="Hasna 1995, Environment and Urbanization (retrieved via Google Drive)",
    section="Hydrant Committee Responsibilities; Background",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established community-institution-formation case-study inclusion precedent (S864 Chng, Manila; S867 Lenneiye, Zimbabwe): participatory action-research directly documenting a municipal water-authority's institutional practices toward low-income street-hydrant users and a community-negotiated formal water-committee governance mechanism. NOT effect_sizes eligible: participatory action-research case study, no regression-based estimate. Extracted for record_id RBDD5DD14AEFB.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
