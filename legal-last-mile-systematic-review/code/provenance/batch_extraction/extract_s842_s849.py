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

# S842 - Swyngedouw - Contradictions of Urban Water Provision, Guayaquil
add("S842",
    citation="Swyngedouw EA (1995). The Contradictions of Urban Water Provision: A Study of Guayaquil, Ecuador. Third World Planning Review.",
    doi="",
    publication_year="1995",
    country="Ecuador",
    subnational_unit="Guayaquil",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="municipal public water utility",
    regulatory_model="Political-economy case study of Guayaquil's public water utility, examining chronic financial deficits, structural dependence on external financing, below-cost lump-sum tariff structures (absence of water meters), and clientelist-populist politics that keep tariffs low while under-investing in network expansion into 'invasiones' (informally invaded/occupied land settlements), producing systematic exclusion of the poorest residents from piped water access despite abundant regional water resources",
    population="urban poor in invasion settlements and informal areas of Guayaquil (35% of the city's 1.6 million residents lacking adequate/reliable water supply)",
    sample_size="institutional/documentary case study with city-level coverage statistics",
    household_level="TRUE", community_level="TRUE", tenure_status="TRUE",
    fees="TRUE", service_area="TRUE", institutional_fragmentation="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE", service_reliability="TRUE",
    effect_measure="institutional/political-economy case study with descriptive coverage statistics",
    effect_estimate="35% of Guayaquil's 1.6 million official residents lack access to adequate and reliable water supply despite the confluence of two major rivers at the city; below-cost, unmetered lump-sum tariffs combined with chronic utility financial deficits and clientelist-populist political pressure to keep prices low produce systematic under-investment in network expansion into informally-occupied 'invasion' settlements, where poor residents instead rely on informal water vendors and illegal tapping as the only means of securing affordable access",
    study_design="institutional/political-economy case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: detailed institutional/financial analysis of the specific tariff-setting and utility-financing mechanisms producing documented, quantified city-wide water-access exclusion.",
    source_document="Swyngedouw 1995, Third World Planning Review (retrieved via Google Drive)",
    section="Latin American urban water institutions; The 'productionist logic'",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: seminal urban-political-ecology institutional case study directly documenting tariff-setting/utility-financing mechanisms and their quantified effect on household water-access exclusion in informal settlements. NOT effect_sizes eligible: institutional/political-economy case study, no regression-based estimate. Extracted for record_id R4EF71E7E284E.",
    )

# S843 - Kooy & Walter - Packaged Drinking Water Supply, Jakarta
add("S843",
    citation="Kooy M, Walter CT (2019). Towards A Situated Urban Political Ecology Analysis of Packaged Drinking Water Supply. Water.",
    doi="10.3390/w11020225",
    publication_year="2019",
    country="Indonesia",
    subnational_unit="Jakarta",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="PDAM (municipal piped water utility), informal Nyelang resellers, packaged drinking water (PDW) vendors",
    regulatory_model="Urban political ecology case study of low-income Jakarta neighborhoods, documenting that eligibility for a direct piped water connection requires proof of land/building tax payment (or equivalent documentation, unavailable to renters), and comparing household survey data on direct piped connections, informal indirect 'Nyelang' connections (buying piped water from a directly-connected neighbor), groundwater, and packaged drinking water (PDW) reliance across two research sites",
    population="low-income households in Penjaringan (North Jakarta) and Gedong/Ciracas (South Jakarta)",
    sample_size="two household surveys (Survey A and a second survey) across two research sites",
    household_level="TRUE", community_level="TRUE", tenure_status="TRUE",
    documentation="TRUE", eligibility="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_quality="TRUE",
    effect_measure="household survey with descriptive statistics on connection type by documentation status",
    effect_estimate="Land/building tax payment receipts (unavailable to renters) are required for eligibility for a direct piped water connection; among surveyed low-income households accessing piped water, only 55% in Penjaringan had a direct connection while the remainder relied on informal indirect 'Nyelang' connections purchased from directly-connected neighbors, and in the second survey site only slightly above one-quarter of households had a direct connection, with packaged drinking water consumption used to supplement both direct and indirect/informal piped-water access",
    study_design="urban political ecology case study with household survey data",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: household survey data directly linking a specific documented eligibility requirement (land/building tax proof) for formal piped-water connections to quantified disparities between direct and informal indirect connection types.",
    source_document="Kooy & Walter 2019, Water (retrieved via Google Drive)",
    section="Understanding PDW Supply in Low Income Neighborhoods of Jakarta",
    exact_location="Section 4",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: household-survey-based study directly documenting a specific formal-connection eligibility/documentation requirement and its quantified effect on direct vs. informal-indirect piped water access. NOT effect_sizes eligible: descriptive survey case study, no regression-based estimate. Extracted for record_id R85BDB2AE39E0.",
    )

# S844 - Hordijk, Sara & Sutherland - comparative water governance, 4 southern cities
add("S844",
    citation="Hordijk M, Sara LM, Sutherland C (2014). Resilience, transition or transformation? A comparative analysis of changing water governance systems in four southern cities. Environment and Urbanization.",
    doi="10.1177/0956247813519044",
    publication_year="2014",
    country="Brazil; Peru; South Africa",
    subnational_unit="Guarulhos; Arequipa; Lima; Durban",
    legal_system="mixed (civil law Brazil/Peru, common law South Africa)",
    urban_rural="urban",
    service_provider="municipal governments and regional water bodies under decentralized/delegated water governance arrangements",
    regulatory_model="Comparative case study of legal and institutional framework changes in water governance across four Global South cities (Guarulhos, Arequipa, Lima, Durban), examining the decentralization/rescaling of state responsibility for water-resource management to regional bodies and drinking-water/sanitation provision to municipalities, and assessing whether these changes reflect resilience, transition, or transformation given persistent underlying power structures",
    population="urban residents across the four case-study cities, particularly those affected by decentralized service provision arrangements",
    sample_size="four comparative city case studies",
    household_level="", community_level="TRUE",
    institutional_fragmentation="TRUE", political_coordination="TRUE", participation="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE", service_coverage="TRUE",
    effect_measure="comparative institutional case study",
    effect_estimate="All four cities show clear indications of transition in water governance configurations following decentralization/delegation of state responsibilities, with Guarulhos and Durban showing some signs of deeper transformation; however, transformative changes in the legal and institutional framework (and even in values and attitudes) have not yet altered the underlying power structures that shape unequal water/sanitation access, raising doubts about whether the transformative potential of these reforms will be realized",
    study_design="comparative institutional case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: structured four-city comparative analysis directly examining specific legal/institutional framework changes (decentralization of water-resource management and service delegation) and their effects on urban water/sanitation governance and access outcomes.",
    source_document="Hordijk, Sara & Sutherland 2014, Environment and Urbanization (retrieved via Google Drive)",
    section="Comparative analysis of governance configurations across four cities",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: comparative institutional case study directly documenting legal/institutional framework changes (decentralization, service delegation) across four cities and their effects on water/sanitation governance and access. NOT effect_sizes eligible: comparative case study, no regression-based estimate. Extracted for record_id R8DBAA192D598.",
    )

# S845 - Romero Lankao & Gunther - Neoliberal modernization, Mexico City/Buenos Aires
add("S845",
    citation="Romero Lankao P, Gunther G (2011). Missing the multiple dimensions of water? Neoliberal modernization in Mexico City and Buenos Aires. Policy and Society.",
    doi="10.1016/j.polsoc.2011.10.007",
    publication_year="2011",
    country="Mexico; Argentina",
    subnational_unit="Mexico City Metropolitan Area; Buenos Aires",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="Water System of Mexico City (SACM), Water Commissions of the Federal District/State of Mexico; Aguas Argentinas/AySA (Buenos Aires)",
    regulatory_model="Comparative institutional case study of neoliberal water-sector reform (private participation/concessions) in two Latin American megacities, examining outcomes across economic (connection registration, billing), environmental (overexploitation, contamination), and political (institutional fragmentation) dimensions of water governance",
    population="urban residents of Mexico City Metropolitan Area and Buenos Aires",
    sample_size="two-city comparative institutional case study",
    household_level="", community_level="TRUE",
    institutional_fragmentation="TRUE", fees="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_quality="TRUE",
    effect_measure="comparative institutional case study",
    effect_estimate="Neoliberal water-sector reform in Mexico City and Buenos Aires produced improvements primarily in the economic dimension (registered connections and billing), but did not resolve unequal access to water, water overexploitation and contamination (environmental dimension), or fragmented and weak institutional settings (political dimension); the authors conclude that transferring utilities to private (or public) management alone cannot address the multiple, interdependent social and environmental dimensions of urban water systems",
    study_design="comparative institutional case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: detailed comparative institutional analysis of a specific reform mechanism (privatization/concession) across two megacities, documenting differentiated effects across economic, environmental, and political-institutional dimensions of water access.",
    source_document="Romero Lankao & Gunther 2011, Policy and Society (retrieved via Google Drive)",
    section="Findings across economic, environmental, and political dimensions",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: comparative institutional case study directly documenting a specific legal/institutional reform mechanism (water-sector privatization/concession) and its differentiated effects on connection/billing outcomes and persistent unequal access. NOT effect_sizes eligible: comparative case study, no regression-based estimate. Extracted for record_id RBD155EDBD079.",
    )

# S846 - Ducrot, Bueno, Barban & Reydon - land tenure gaming approach, Sao Paulo periphery
add("S846",
    citation="Ducrot R, Bueno AK, Barban V, Reydon BP (2010). Integrating land tenure, infrastructure and water catchment management in Sao Paulo's periphery: lessons from a gaming approach. Environment and Urbanization.",
    doi="10.1177/0956247810380168",
    publication_year="2010",
    country="Brazil",
    subnational_unit="Sao Paulo periphery (water catchment/reservoir area)",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="municipal water company, district government",
    regulatory_model="Role-playing game methodology (participatory simulation with mayor, water company, district representatives, and different types of landowners) exploring interactions between land tenure insecurity, water/sanitation infrastructure access, and pollution in São Paulo's peri-urban water-catchment periphery, assessing divergent institutional-actor and community-actor perceptions of priorities and negotiation arrangements",
    population="informal settlers and institutional actors in São Paulo's peri-urban catchment periphery",
    sample_size="structured role-playing game sessions with institutional and community actors",
    household_level="TRUE", community_level="TRUE", tenure_status="TRUE",
    tenure="TRUE", legal_status="TRUE", discretion_accommodation="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE",
    effect_measure="participatory role-playing-game case study with qualitative assessment of actor perceptions",
    effect_estimate="Community actors' priorities center on land tenure insecurity, access to public transport, health and education rather than water/sanitation infrastructure per se, while institutional actors misunderstand this hierarchy and fail to recognize how access to infrastructure and land tenure are jointly shaped by power-based relationships; these discrepancies call into question the effectiveness of legal, technical and institutional solutions institutional actors promote to address water-catchment pollution, since land-tenure insecurity (not solely a water/sanitation deficit) is a root barrier to formalizing infrastructure access in the periphery",
    study_design="participatory role-playing-game case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="2",
    mechanism_certainty="Moderate: a structured participatory-simulation methodology directly eliciting institutional- and community-actor perspectives on land tenure as a barrier to water/sanitation infrastructure access, though based on simulated negotiation rather than observed real-world outcomes.",
    source_document="Ducrot, Bueno, Barban & Reydon 2010, Environment and Urbanization (retrieved via Google Drive)",
    section="Game assessment; institutional vs. community actor perspectives",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: qualitative institutional/participatory study directly examining land tenure insecurity as a legal/institutional barrier to water/sanitation infrastructure access, consistent with the project's tenure-focused Family A/C scope. NOT effect_sizes eligible: participatory case-study methodology, no regression-based estimate. Extracted for record_id R8A2445A92C67.",
    )

# S847 - Hill - E-Governance: Silencing Vulnerable Populations, Cape Town
add("S847",
    citation="Hill WC (2015). E-Governance: Silencing Vulnerable Populations. Procedia Engineering.",
    doi="10.1016/j.proeng.2015.06.072",
    publication_year="2015",
    country="South Africa",
    subnational_unit="Imizamo Yethu township, Hout Bay, Cape Town",
    legal_system="common law (post-apartheid constitutional)",
    urban_rural="urban",
    service_provider="City of Cape Town municipal water and sanitation department (SMS-based fault-reporting e-governance system)",
    regulatory_model="Cross-sectional survey study (168 survey-based interviews) in an informal township, examining whether Cape Town's SMS-based e-governance fault-reporting system for water/sanitation problems is accessible to vulnerable populations (elderly, disabled, infirm), using chi-square tests to identify statistically significant relationships between mobility/health status, physical access to public water/sanitation facilities, and technological capacity to report service problems",
    population="residents of Imizamo Yethu informal township, Cape Town (elderly, disabled, and infirm subpopulations)",
    sample_size="168 survey-based interviews",
    household_level="TRUE", community_level="TRUE",
    bureaucratic_assistance="TRUE", complaint="TRUE",
    water_access="TRUE", sanitation_access="TRUE", service_quality="TRUE",
    effect_measure="cross-sectional survey with chi-square tests",
    effect_estimate="Elderly, disabled, and infirm residents face significant barriers to using public water/sanitation facilities (average travel time to a public toilet: ~14 minutes for disabled, ~15 minutes for those with poor health, ~20 minutes for the elderly, vs. ~10 minutes for those without disabilities/health issues) and to communicating problems via the municipality's SMS-based fault-reporting e-governance system (only 25% of respondents 50+ and ~30% of those with disabilities/poor health used SMS, vs. ~60% of the sampled population overall), such that the very groups most acutely affected by water/sanitation service delivery shortcomings have the least capacity to engage the municipal reporting mechanism intended to redress them",
    study_design="cross-sectional survey study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: a purpose-built cross-sectional survey (168 interviews) with statistical (chi-square) testing directly linking vulnerability status to both physical water/sanitation-facility access and capacity to use a specific municipal administrative reporting mechanism.",
    source_document="Hill 2015, Procedia Engineering (retrieved via Google Drive)",
    table="Figure 1 demographic comparison",
    section="Results; Discussion",
    exact_location="Sections 4-5",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: quantitative survey study directly documenting a specific municipal administrative-assistance/complaint mechanism (SMS fault-reporting) and vulnerable populations' differential capacity to access both physical water/sanitation facilities and this redress channel, fitting Family B (administrative assistance and access) and Family C (administrative barriers and access inequality). NOT effect_sizes eligible per the strict Family A/B/C framework: findings are reported via chi-square tests and descriptive comparisons rather than a regression-based estimate isolating the institutional mechanism's effect. Extracted for record_id RB279F6DED9CF.",
    )

# S848 - Hanrahan - Water (in)security in Canada, Indigenous exclusion
add("S848",
    citation="Hanrahan M (2017). Water (in)security in Canada: national identity and the exclusion of Indigenous peoples. British Journal of Canadian Studies.",
    doi="10.3828/bjcs.2017.4",
    publication_year="2017",
    country="Canada",
    subnational_unit="multiple First Nations reserves (five case studies)",
    legal_system="common law",
    urban_rural="rural",
    service_provider="federal/provincial governments; First Nations band water systems under the Indian Act's decentralized/underfunded governance structure",
    regulatory_model="Five short case studies documenting Indigenous water insecurity in Canada, situating persistent Indigenous/non-Indigenous water-infrastructure disparities (Indigenous people ninety times more likely than other Canadians to lack piped water) within the Indian Act's reserve system and the neo-liberal decentralization of water governance responsibility to under-resourced First Nations without commensurate transfer of funding or capacity",
    population="First Nations, Metis, and Inuit communities across Canada",
    sample_size="five case studies of water insecurity",
    household_level="TRUE", community_level="TRUE", indigenous_population="TRUE",
    legal_status="TRUE", institutional_fragmentation="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_reliability="TRUE", service_quality="TRUE",
    effect_measure="qualitative case study synthesis with descriptive disparity statistics",
    effect_estimate="Indigenous people in Canada are ninety times more likely than other Canadians to lack piped water; these disparities are shown, across five case studies, to result from the Indian Act's reserve system and a decentralized, neo-liberal water-governance model that transfers water-infrastructure responsibility to First Nations band governments without adequate accompanying federal funding, technical capacity, or regulatory oversight, reproducing a colonial relationship between the Canadian state and Indigenous nations",
    study_design="qualitative case study synthesis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: direct documentation of a specific statutory/institutional framework (Indian Act reserve system, decentralized water governance) and a striking, well-sourced quantified disparity (90-fold) in piped-water access between Indigenous and non-Indigenous Canadians.",
    source_document="Hanrahan 2017, British Journal of Canadian Studies (retrieved via Google Drive)",
    section="Water infrastructure disparities; case studies of water insecurity",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established Indigenous/customary water-governance inclusion precedent (Bakker et al. Canada; S823 Alvez Marin Chile): direct documentation of a specific statutory/institutional framework (Indian Act reserve system) causing a quantified, extreme water-access disparity for Indigenous peoples. NOT effect_sizes eligible: qualitative case-study synthesis, no regression-based estimate. Extracted for record_id R8D4D5CF53A02.",
    )

# S849 - Ayalew, Chenoweth, Malcolm, Mulugetta, Okotto & Pedley - small independent water providers, Kenya/Ethiopia
add("S849",
    citation="Ayalew M, Chenoweth J, Malcolm R, Mulugetta Y, Okotto LG, Pedley S (2014). Small Independent Water Providers: Their Position in the Regulatory Framework for the Supply of Water in Kenya and Ethiopia. Journal of Environmental Law.",
    doi="10.1093/jel/eqt028",
    publication_year="2014",
    country="Kenya; Ethiopia",
    subnational_unit="peri-urban neighborhoods (multiple case sites)",
    legal_system="common law (Kenya); civil law (Ethiopia)",
    urban_rural="urban",
    service_provider="small independent water vendors/kiosk operators alongside formal municipal water utilities",
    regulatory_model="Multidisciplinary legal/regulatory research project examining the absence of formal recognition and regulation of small independent water vendors -- who fill a critical supply gap in peri-urban neighborhoods where municipal networks do not reach -- and assessing the case for regulating their competition, pricing, and water quality under Kenyan and Ethiopian water law",
    population="peri-urban residents in Kenya and Ethiopia dependent on small independent water vendors for their primary water supply",
    sample_size="multidisciplinary legal/regulatory research project across multiple peri-urban case sites in Kenya and Ethiopia",
    household_level="TRUE", community_level="TRUE",
    service_area="TRUE", fees="TRUE", enforcement="TRUE", eligibility="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE", service_quality="TRUE",
    effect_measure="legal/regulatory research project (multidisciplinary case analysis)",
    effect_estimate="Small independent water vendors are often the only water-supply option in peri-urban neighborhoods but operate entirely outside Kenya's and Ethiopia's formal water-regulatory frameworks, leaving their pricing and water quality unregulated and unmonitored; the authors conclude that formally recognizing and regulating these vendors as part of the water-sector regulatory framework -- rather than continuing to treat them as invisible to law -- would increase access to water for the poor and advance the Millennium Development Goals and the right to water",
    study_design="legal/regulatory case analysis (multidisciplinary research project)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: dedicated multidisciplinary legal-regulatory research project (published in a leading environmental law journal) directly examining the absence of formal legal recognition/regulation of a specific water-access mechanism (small independent vendors) serving peri-urban populations otherwise excluded from municipal networks.",
    source_document="Ayalew, Chenoweth, Malcolm, Mulugetta, Okotto & Pedley 2014, Journal of Environmental Law (retrieved via Google Drive)",
    section="Introduction; case for regulation of small independent water vendors",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: legal/regulatory research project directly examining the absence of formal legal recognition/regulation of a specific water-access mechanism (small independent vendors) filling a municipal-network gap for peri-urban populations. NOT effect_sizes eligible: legal/regulatory case analysis, no regression-based estimate. Extracted for record_id R96660AABF429.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
