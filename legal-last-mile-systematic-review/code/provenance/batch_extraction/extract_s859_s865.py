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

# S859 - Masanyiwa, Niehof & Termeer - Decentralized rural water services, Tanzania
add("S859",
    citation="Masanyiwa ZS, Niehof A, Termeer CJAM (2015). Users' perspectives on decentralized rural water services in Tanzania. Gender, Place & Culture.",
    doi="10.1080/0966369X.2014.917283",
    publication_year="2015",
    country="Tanzania",
    subnational_unit="Kondoa and Kongwa districts",
    legal_system="common law",
    urban_rural="rural",
    service_provider="village-level water management committees under decentralized district-level governance",
    regulatory_model="Mixed-methods study (household survey plus qualitative methods) comparing household- and village-level domestic-water-access outcomes before and after Tanzania's water-sector decentralization reforms (2002 vs. 2011), applying a users' and gender perspective to assess whether gender-sensitive water-service delivery improved, including analysis of women's representation in water-management committees",
    population="rural households in Kondoa and Kongwa districts, Tanzania",
    sample_size="household survey plus qualitative interviews/focus groups, 2002 and 2011 comparison",
    household_level="TRUE", community_level="TRUE",
    institutional_fragmentation="TRUE", participation="TRUE",
    water_access="TRUE", service_quantity="TRUE", service_reliability="TRUE",
    effect_measure="mixed-methods comparative household survey (descriptive statistics, chi-square tests)",
    effect_estimate="The proportion of households using improved domestic water sources increased between 2002 and 2011 following decentralization reforms, but more than half of users still travel over a kilometre and spend more than an hour collecting water in the dry season; despite an increased proportion of women on water-management committees, the outcomes of decentralized water governance differ systematically for men and women, and the reforms produced contradictory effects -- improving access for some users while creating or reinforcing existing inter- and intra-village inequalities",
    study_design="mixed-methods comparative study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: household survey and qualitative data directly comparing water-access outcomes before and after a specific national decentralization reform, with gender-disaggregated institutional participation data.",
    source_document="Masanyiwa, Niehof & Termeer 2015, Gender, Place & Culture (retrieved via Google Drive)",
    section="Findings",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: mixed-methods study directly documenting a specific water-sector decentralization reform and its differentiated household-level access outcomes by gender. NOT effect_sizes eligible: descriptive comparative survey with chi-square tests, no regression-based estimate isolating the reform's effect. Extracted for record_id R7A3F1A708032.",
    )

# S860 - Singh - Mapping Poverty to Reach the Urban Poor, Madhya Pradesh
add("S860",
    citation="Singh K (2014). Mapping Poverty to Reach the Urban Poor. Social Change.",
    doi="10.1177/0049085714548542",
    publication_year="2014",
    country="India",
    subnational_unit="Bhopal, Indore, Gwalior, Jabalpur (Madhya Pradesh)",
    legal_system="common law",
    urban_rural="urban",
    service_provider="municipal corporations under the ADB/UN-HABITAT Water for Asian Cities Programme",
    regulatory_model="UN-HABITAT-supported Poverty Pocket Situation Analysis (PPSA) survey across four Madhya Pradesh cities, mapping infrastructural deficiencies across notified and non-notified slums/poverty pockets to prioritize investment via Municipal Action Plans for Poverty Reduction (MAPP), documenting how official notification status affects service eligibility and how the survey identified far more poverty pockets (55-65% more households) than official municipal/census records",
    population="households in 1,540 poverty pockets/slums across four Madhya Pradesh cities",
    sample_size="citywide poverty-pocket mapping survey (key informant interviews and group discussions) plus household-level baseline surveys in selected slums (20,000 families, 65 slums)",
    household_level="TRUE", community_level="TRUE", tenure_status="TRUE",
    documentation="TRUE", eligibility="TRUE", fees="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE", affordability="TRUE",
    effect_measure="citywide poverty-mapping survey with quantified access statistics",
    effect_estimate="Official records severely under-reported poverty pockets (55-65% gap): Bhopal's 2001 Census recorded 125,720 slum residents while the 2012 survey found 640,850 people in 380 poverty pockets; across the four cities, access to piped water supply among households in poverty pockets ranged from only 28% (Indore) to 65.14% (Gwalior), and access to improved sanitation ranged from 54% (Jabalpur) to 84% (Indore), with non-notified (formally unrecognized) slums systematically excluded from municipal service-delivery planning until identified through this mapping exercise",
    study_design="citywide poverty-mapping survey with pilot intervention",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: a systematic, citywide survey directly documenting the notification/non-notification status of informal settlements as a determinant of municipal water/sanitation service-delivery eligibility, with quantified access statistics across four cities.",
    source_document="Singh 2014, Social Change (retrieved via Google Drive)",
    table="Table 1 (Poverty Pockets in Four Project Cities)",
    section="Poverty Mapping Framework for Infrastructure Interventions",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: systematic citywide survey directly documenting slum notification status as a formal-eligibility barrier to municipal water/sanitation service-delivery planning, with quantified household-level access statistics across four cities. NOT effect_sizes eligible: descriptive survey, no regression-based estimate. Extracted for record_id R9BEC06E5E577.",
    )

# S861 - Das & Walton - Political Leadership and the Urban Poor, Delhi
add("S861",
    citation="Das V, Walton M (2015). Political Leadership and the Urban Poor: Local Histories. Current Anthropology.",
    doi="10.1086/682420",
    publication_year="2015",
    country="India",
    subnational_unit="two unplanned settlements, National Capital Region of Delhi",
    legal_system="common law",
    urban_rural="urban",
    service_provider="Delhi Jal Board and municipal bureaucracy, mediated by informal local political leaders",
    regulatory_model="Survey research and ethnographic interviews examining how local political leaders in two low-income 'unplanned settlements' learn to engage institutional processes of law and bureaucracy to secure housing and water/electricity infrastructure access, documenting household-level multi-source water-collection strategies and the overlapping movements of law, bureaucracy, markets, and democratic mobilization through which infrastructure access is achieved for the urban poor",
    population="residents of two unplanned/informal settlements in Delhi's National Capital Region",
    sample_size="household survey (multiple localities) plus ethnographic interviews",
    household_level="TRUE", community_level="TRUE", tenure_status="TRUE",
    legal_status="TRUE", documentation="TRUE", discretion="TRUE", bureaucratic_assistance="TRUE",
    formal_connection="TRUE", water_access="TRUE",
    effect_measure="survey research and ethnographic interviews",
    effect_estimate="In Punjabi Basti, all surveyed households used more than one source for accessing water, reflecting the absence of secure, singular formal connections; local political leaders emerge specifically through learning to navigate institutional/bureaucratic and legal processes (e.g., address regularization for cost recovery, informal electricity connections later formalized) to secure infrastructure for their communities, demonstrating that infrastructure access for the urban poor is produced through the interaction of law, bureaucracy, markets, and local democratic political mobilization rather than through formal entitlement alone",
    study_design="mixed-methods ethnographic/survey case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: combined household survey and extended ethnographic fieldwork directly documenting how local political leaders' navigation of bureaucratic/legal institutional processes determines infrastructure access for two informal settlements.",
    source_document="Das & Walton 2015, Current Anthropology (retrieved via Google Drive)",
    section="Water access and multi-source household strategies; political leadership and bureaucratic engagement",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: mixed-methods study directly documenting how local political leaders' engagement with bureaucratic/legal institutional processes determines informal-settlement infrastructure access, with household-level water-source survey data. NOT effect_sizes eligible: ethnographic/survey case study, no regression-based estimate. Extracted for record_id R9F1FB9F1D75D.",
    )

# S862 - Galvin & Roux - Dam state capture, DWS South Africa
add("S862",
    citation="Galvin M, Roux S (2019). Dam state capture: its cascading effect on the Department of Water and Sanitation. Transformation: Critical Perspectives on Southern Africa.",
    doi="10.1353/trn.2019.0026",
    publication_year="2019",
    country="South Africa",
    subnational_unit="national (Department of Water and Sanitation) with municipal-level service-delivery examples",
    legal_system="common law",
    urban_rural="both",
    service_provider="Department of Water and Sanitation (DWS) and municipal Water Services Authorities",
    regulatory_model="Documentary institutional analysis using primary data (Parliamentary reports, Promotion of Access to Information Act (PAIA) requests, and a South African Water Caucus fact-finding report) examining how 'state capture' has cascaded through DWS, undermining its regulatory oversight of municipal Water Services Authorities and its own water-services provision role, examined through three mechanisms: securing/weakening control over the public service, centralising control over institutions, and 'shaking down' regulation (declining Blue Drop water-quality-assessment pass rates)",
    population="South African municipal residents dependent on DWS-regulated water services, including townships in Makhanda municipality documented as experiencing extended periods without running water",
    sample_size="documentary analysis of Parliamentary reports and PAIA-obtained government records",
    household_level="TRUE", community_level="TRUE",
    enforcement="TRUE", institutional_fragmentation="TRUE", discretion="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_reliability="TRUE", service_quality="TRUE",
    effect_measure="documentary institutional analysis with quantified regulatory-compliance data",
    effect_estimate="State capture of DWS -- including weakening of ministerial/departmental controls, centralising power away from constitutionally-designated municipal competences, and disrupting regulatory enforcement -- is documented alongside a near-halving of municipalities achieving 'Blue Drop' water-quality-assessment status (from 98 in 2012 to 44 in 2014) and extended periods without running water or with severely contaminated water in townships such as those in Makhanda municipality, demonstrating a direct cascading effect from national-level institutional capture to household-level water-service failures",
    study_design="documentary institutional analysis (primary government records)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: analysis of primary government records (Parliamentary reports, PAIA requests) directly documenting specific institutional-capture mechanisms within a national water-regulatory department and their cascading, quantified effects on municipal water-quality compliance and household-level service delivery.",
    source_document="Galvin & Roux 2019, Transformation (retrieved via Google Drive)",
    section="Cascading effects of state capture in DWS",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: documentary institutional analysis using primary government records directly documenting regulatory-capture mechanisms within a national water-sector department and their cascading effect on household-level water-service delivery and quality compliance. NOT effect_sizes eligible: documentary institutional analysis, no regression-based estimate. Extracted for record_id R9D838E8FBB65.",
    )

# S863 - Liu Haiyan - Water supply and urban space, Tianjin
add("S863",
    citation="Liu Haiyan (2011). Water supply and the reconstruction of urban space in early twentieth-century Tianjin. Urban History.",
    doi="10.1017/S096392681100054X",
    publication_year="2011",
    country="China",
    subnational_unit="Tianjin (British and Japanese foreign settlements vs. the Chinese-administered Old City)",
    legal_system="mixed (foreign concession municipal by-laws vs. Chinese municipal administration)",
    urban_rural="urban",
    service_provider="British Settlement Municipal Council; Japanese Settlement Municipal Council; Old City Chinese municipal administration",
    regulatory_model="Historical institutional case study of early twentieth-century Tianjin's divided treaty-port governance, documenting formal water-supply agreements/contracts between settlement Municipal Councils and private water companies (e.g., a 10-year agreement for the Japanese Settlement Municipal Council to resell water to settlement households; British Settlement Municipal Council takeover of the water company in 1923), and comparing the resulting rapid extension of household tap-water connections in the foreign settlements against the much slower, more fragmented adoption in the Chinese-administered Old City",
    population="residents of Tianjin's foreign settlements and Old City in the early twentieth century",
    sample_size="historical documentary case study (municipal council reports, land regulations)",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", institutional_fragmentation="TRUE", fees="TRUE",
    formal_connection="TRUE", water_access="TRUE",
    effect_measure="historical documentary institutional case study with quantified connection data",
    effect_estimate="In the British Settlement, more than half of households received tap water in the early twentieth century, with the number of connected households increasing rapidly (in less than one year, late 1922-early 1923) following Municipal Council takeover of the water company and coordinated ending of manure-cart-based sanitation, under a specific 10-year municipal water-resale agreement; by contrast, the Chinese-administered Old City -- governed separately and lacking equivalent formal municipal water-supply agreements -- saw far slower and more fragmented tap-water adoption among its traditional multi-household courtyard-compound residents, demonstrating that differential municipal-governance and contractual arrangements across administratively divided zones of the same city directly produced differential household water-connection outcomes",
    study_design="historical institutional case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: detailed historical documentary analysis of specific formal municipal water-supply contracts/agreements across differently-governed administrative zones of the same city, with quantified household-connection outcomes.",
    source_document="Liu Haiyan 2011, Urban History (retrieved via Google Drive)",
    section="Water supply in the foreign settlements vs. the Old City",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established historical-institutional-fragmentation inclusion precedent (S840 Grant, Nashville): historical case study directly documenting specific formal municipal water-supply agreements across administratively divided governance zones of the same city and their differential household-connection outcomes. NOT effect_sizes eligible: historical documentary case study, no regression-based estimate. Extracted for record_id R9CCA5D7854A6.",
    )

# S864 - Chng - Privatization and Citizenship, Philippines
add("S864",
    citation="Chng NR (2008). Privatization and Citizenship: Local politics of water in the Philippines. Development.",
    doi="10.1057/palgrave.development.1100444",
    publication_year="2008",
    country="Philippines",
    subnational_unit="Taguig City, Metro Manila",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="Manila Water Company Inc. (MWCI) and community-based bulk-water People's Organizations (POs)",
    regulatory_model="Ethnographic/interview-based case study (original interviews with PO leaders and MWCI officials, 2007) of small-scale water providers in Taguig's urban poor community of Sitio Imelda, documenting a specific bulk-water contract mechanism under which POs purchase water from MWCI at a bulk tariff (PhP19/m3), install and finance their own secondary-pipe connections and mother meters, and independently collect payment from member households (roughly 1,200-1,500 residents per PO, ~90 POs in Taguig by 2007), including documented regulatory arbitration disputes between POs and MWCI over service-area infringement",
    population="urban poor households in Taguig City, Metro Manila served by community-managed bulk-water Peoples' Organizations",
    sample_size="ethnographic case study with original interviews (PO leaders, MWCI officials, June 2007)",
    household_level="TRUE", community_level="TRUE", tenure_status="TRUE",
    fees="TRUE", administrative_review="TRUE", enforcement="TRUE", disconnection="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE", service_continuity="TRUE",
    effect_measure="ethnographic case study with original interview data",
    effect_estimate="Under a bulk-water contract mechanism, ~90 community-based Peoples' Organizations in Taguig purchased water from MWCI at PhP19/m3 and resold it to member households at PhP25-35/m3, financing their own connection infrastructure and using flexible, socially-embedded payment/collection practices (interest-free balance carryover, no automatic cutoffs) that sustained service continuity for populations MWCI itself could not profitably reach directly; however, MWCI's later attempts to offer direct connections to PO customers (undermining its own bulk-water contracts) triggered a formal regulatory arbitration dispute in which 13 POs sought redress, illustrating both the mechanism's success in extending access and its institutional fragility",
    study_design="ethnographic case study with original interview data",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: original interview-based fieldwork directly documenting a specific bulk-water contractual mechanism, its household-level connection/payment outcomes, and a formal regulatory arbitration dispute over its continuation.",
    source_document="Chng 2008, Development (retrieved via Google Drive)",
    section="Water politics in Taguig",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: original ethnographic/interview-based case study directly documenting a specific bulk-water contractual mechanism (community Peoples' Organizations under bulk-water contracts with MWCI) and its household-level water-access, affordability, and continuity outcomes, plus a documented regulatory arbitration dispute. NOT effect_sizes eligible: ethnographic case study, no regression-based estimate. Extracted for record_id R9D4088D1FDFD.",
    )

# S865 - Abrahams, Mhlongo & Napo - Gendered analysis of water/sanitation policies, South Africa
add("S865",
    citation="Abrahams Y, Mhlongo S, Napo V (2011). A gendered analysis of water and sanitation services policies and programmes in South Africa: 2006-2010. Agenda: Empowering Women for Gender Equity.",
    doi="10.1080/10130950.2011.575998",
    publication_year="2011",
    country="South Africa",
    subnational_unit="national, with province-level data",
    legal_system="common law",
    urban_rural="both",
    service_provider="Department of Water Affairs (DWA)/Department of Water Affairs and Forestry (DWAF), Water Boards, local government Water Services Authorities",
    regulatory_model="Policy review by South Africa's Commission for Gender Equality (a constitutional body) of the statutory and policy framework governing water/sanitation service provision -- the Water Services Act 1997, National Water Act 1998, Municipal Structures Act 1998, Municipal Systems Act 2000, and the Free Basic Services Policy (6 kilolitres/household/month) -- assessing gender mainstreaming and drawing on Statistics South Africa's General Household Survey (2002-2009) province-level water/sanitation access data",
    population="South African households, disaggregated where possible by province and gender of household head",
    sample_size="review of national legislation/policy plus Statistics South Africa General Household Survey data (2002-2009)",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", fees="TRUE", participation="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE", affordability="TRUE",
    effect_measure="legal/policy review with government household-survey statistics",
    effect_estimate="Access to piped/tap water (on- or off-site) increased across all South African provinces between 2002 and 2009, most dramatically in the Eastern Cape (56.8% to 75%, a 19.3 percentage-point increase) and Limpopo (74.1% to 80.8%), attributed to the post-1994 statutory framework (Water Services Act 1997, National Water Act 1998, Free Basic Services Policy); however, the underlying gender-disaggregated data needed to assess whether women and female-headed households have benefited equally from this legal/institutional framework was found not to exist, despite the Water Services Act's specific mandate that services be gender-sensitive and equitably rendered",
    study_design="legal/policy review with government survey statistics",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: systematic review of specific national water-sector legislation (Water Services Act 1997, National Water Act 1998, Free Basic Services Policy) combined with province-level government household-survey access data, conducted by a constitutional gender-equality oversight body, though without original primary data collection or gender-disaggregated access outcomes.",
    source_document="Abrahams, Mhlongo & Napo 2011, Agenda (retrieved via Google Drive)",
    table="Graph i (Access to Water Services per Province, 2002-2009)",
    section="Historical overview; Constitutional and legal framework; Poverty and water and sanitation",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established descriptive/regulatory-performance national-case-study precedent (S805 Kosova, S819 Chile, S828 Brazil WatSan law, S830 Sao Paulo): detailed statutory-framework analysis (Water Services Act 1997, National Water Act 1998, Free Basic Services Policy) drawing on a national statistical agency's own published household-survey access data, conducted by a constitutional oversight body (Commission for Gender Equality). NOT effect_sizes eligible: legal/policy review with descriptive survey statistics, no regression-based estimate. Extracted for record_id RA268D41C7EFC.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
