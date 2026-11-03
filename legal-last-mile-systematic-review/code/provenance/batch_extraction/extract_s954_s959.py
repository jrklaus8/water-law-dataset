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

# S954 - Mwendera - Rural water supply and sanitation coverage in Swaziland
add("S954",
    citation="Mwendera EJ (2006). Rural water supply and sanitation (RWSS) coverage in Swaziland: Toward achieving millennium development goals. Physics and Chemistry of the Earth.",
    doi="10.1016/j.pce.2006.08.040",
    publication_year="2006",
    country="Swaziland",
    subnational_unit="four administrative regions (Hhohho, Manzini, Shiselweni, Lubombo)",
    legal_system="mixed (customary and statutory law)",
    urban_rural="rural",
    service_provider="Rural Water Supply Branch (RWSB) of the Ministry of Natural Resources and Energy, community-elected Water Supply and Sanitation Committees (WSSC), NGOs, and bilateral/multilateral support agencies, under the African Development Bank's Rural Water Supply and Sanitation Initiative (RWSSI)",
    regulatory_model="Government-commissioned institutional assessment (interviews with central and field-station government staff, NGOs, external support agencies, and private-sector actors, plus field visits) of Swaziland's rural water supply and sanitation sector, examining institutional structures (community Water Supply and Sanitation Committees, government cost-sharing rules requiring 25% community investment contribution and 50%/50% government/community-funded major repairs), funding-allocation constraints (RWSB budget subsumed within the broader Water Resources Management budget category), and their effects on rural water/sanitation coverage progress toward national and Millennium Development Goal targets",
    population="rural population of Swaziland (approximately 1,162,000 nationally)",
    sample_size="national institutional assessment with interviews across 4 administrative regions and field visits",
    household_level="FALSE", community_level="TRUE",
    legal_status="TRUE", fees="TRUE", institutional_fragmentation="TRUE", participation="TRUE", bureaucratic_assistance="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE", service_coverage="TRUE",
    effect_measure="government-commissioned institutional assessment with quantified coverage-trend data",
    effect_estimate="Rural water supply coverage in Swaziland rose from 9% (1980) to 56% (2004), and rural sanitation coverage rose from 19% (1980) to 63% (2004), driven by a community-institutional model requiring elected Water Supply and Sanitation Committees (WSSC) to mobilize community contributions of at least 25% of system investment cost and full O&M responsibility (with government covering 50% of major-component replacement costs); however, the study finds that RWSB's institutional funding is structurally constrained because its budget is subsumed within the broader Water Resources Management budget category (just 0.8% of national recurrent expenditure and 4% of capital expenditure in 2004/05), with the bulk of funds diverted to large water-resources projects rather than rural water/sanitation, demonstrating that a specific budget-institutional-allocation structure -- not merely aggregate national investment levels -- is a binding constraint on achieving national and MDG rural water/sanitation coverage targets.",
    table="Table 2 (RWSS coverage trends 1980-2022); Tables 5-6 (water-sector recurrent and capital expenditure analysis)",
    study_design="government-commissioned institutional assessment with interviews, field visits, and quantified coverage/budget-trend analysis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: original institutional assessment (interviews, field visits, budget-allocation analysis) directly linking a specific government funding-institutional structure and community cost-sharing governance model to quantified rural water/sanitation coverage outcomes.",
    source_document="Mwendera 2006, Physics and Chemistry of the Earth (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, distinguished from prior excluded general water-scarcity/multi-indicator studies by its dedicated, detailed institutional analysis of the RWSS sector's funding-allocation and community-governance structure with quantified coverage outcomes. NOT effect_sizes eligible: institutional assessment with descriptive coverage-trend data, no regression-based estimate isolating a single institutional mechanism. Extracted for record_id R5AE001CE6E9E.",
    )

# S955 - Monney et al - Accelerating rural sanitation coverage in Ghana
add("S955",
    citation="Monney I, Baffoe-Kyeremeh A, Amissah-Reynolds PK (2015). Accelerating rural sanitation coverage in Ghana: what are the speed bumps impeding progress? Journal of Water, Sanitation and Hygiene for Development.",
    doi="10.2166/washdev.2015.005",
    publication_year="2015",
    country="Ghana",
    subnational_unit="Tain district, three rural communities",
    legal_system="common law",
    urban_rural="rural",
    service_provider="local district assembly (local government) sanitation-promotion budget and staff, alongside household-level toilet-construction decisions",
    regulatory_model="Mixed-methods study (key informant interviews, focus group discussions, field observations, and face-to-face interviews of 400 residents from 249 houses) in three rural Tain district communities, examining household-level and institutional-level constraints and opportunities for in-house toilet construction, including analysis of local district-assembly expenditure patterns showing low institutional priority for sanitation promotion, constrained by low donor support, inadequate logistics, and poor human-resource capacity",
    population="400 residents across 249 houses in three rural communities, Tain district, Ghana",
    sample_size="400 residents, 249 houses, 3 rural communities",
    household_level="TRUE", community_level="TRUE",
    institutional_fragmentation="TRUE", bureaucratic_assistance="TRUE", discretion="TRUE",
    formal_connection="TRUE", sanitation_access="TRUE",
    effect_measure="mixed-methods household survey with institutional expenditure-pattern analysis",
    effect_estimate="Rural sanitation coverage in Ghana increased by just 4% over two decades; the study finds that in-house toilet scarcity, and consequent reliance on open defecation and communal toilets, is driven by both household-level barriers (perceived high cost, low priority given to latrine ownership, ignorance of low-cost technologies) and institutional-level constraints, with analysis of local assembly expenditure patterns revealing that sanitation promotion is afforded low budgetary priority, further constrained by low donor support, lack of requisite logistics, and poor human-resource capacity at the local government level, demonstrating that institutional/administrative resource-allocation failures at the local-government level are a key 'speed bump' impeding rural sanitation-coverage progress alongside household-level demand barriers.",
    study_design="mixed-methods study with 400-respondent household survey, key informant interviews, and focus group discussions",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: original mixed-methods study (400-respondent survey plus qualitative institutional analysis) directly linking local-government institutional resource-allocation constraints to rural sanitation-coverage outcomes.",
    source_document="Monney, Baffoe-Kyeremeh & Amissah-Reynolds 2015, Journal of Water, Sanitation and Hygiene for Development (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established local-government institutional-capacity inclusion precedent (Obeta Nigeria; Cobbing South Africa O&M, this segment): original mixed-methods study directly linking local-government institutional resource-allocation constraints to sanitation-coverage outcomes. NOT effect_sizes eligible: mixed-methods survey with descriptive institutional analysis, no regression-based estimate. Extracted for record_id R58857C935BCF.",
    )

# S956 - Tantoh & McKay - community-based water management and governance, North-West Cameroon
add("S956",
    citation="Tantoh HB, McKay TJM (2021). Assessing community-based water management and governance systems in North-West Cameroon using a Cultural Theory and Systems Approach. Journal of Cleaner Production.",
    doi="10.1016/j.jclepro.2020.125467",
    publication_year="2021",
    country="Cameroon",
    subnational_unit="rural districts of North-West Cameroon",
    legal_system="civil law",
    urban_rural="rural",
    service_provider="Community-Based Water Management (CBWM) systems relying on local inhabitants, extended community networks, and diaspora contributions, operating alongside centralized national-government water-resource management despite decentralization laws",
    regulatory_model="Study of rural water systems in North-West Cameroon using Cultural Theory (to classify social groups and stakeholder power relations) and Systems Thinking Analysis (to evaluate causal feedback relationships between stakeholders and water-management systems), examining how centralized national-government control over water-resource management -- despite the promulgation of decentralization laws supporting local decision-making -- shapes the emergence and functioning of Community-Based Water Management (CBWM) systems and the distribution of power among local elites, government officials, and community members",
    population="rural residents of North-West Cameroon districts reliant on community-based water systems",
    sample_size="multi-district study across North-West Cameroon rural water systems",
    household_level="FALSE", community_level="TRUE",
    legal_status="TRUE", institutional_fragmentation="TRUE", discretion="TRUE", political_coordination="TRUE", participation="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_reliability="TRUE",
    effect_measure="Cultural Theory and Systems Thinking Analysis institutional/governance assessment",
    effect_estimate="Despite Cameroon's promulgation of laws supporting decentralization of water-resource decision-making, the national government continues to centrally determine how water resources are managed, creating significant hurdles for domestic water provisioning to rural residents; Community-Based Water Management (CBWM) systems have emerged and persist due to substantial contributions from local inhabitants, extended community networks, and the diaspora, but these CBWM systems simultaneously reinforce the status and situational power of local elites and government officials (and, to a lesser degree, men), such that a concerted effort toward more democratic and transparent politico-cultural water-governance mechanisms is identified as necessary to resolve water-management conflicts and sustainably improve rural domestic water access.",
    study_design="Cultural Theory and Systems Thinking Analysis institutional/governance assessment across multiple rural districts",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: original institutional/governance assessment directly documenting how the disconnect between decentralization law and continued centralized government control shapes community-based water-management institutions and household water-access outcomes.",
    source_document="Tantoh & McKay 2021, Journal of Cleaner Production (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established community-based-management/decentralization-law inclusion precedent (Golooba-Mutebi Rwanda/Uganda; Avidar Kenya devolution): original institutional/governance assessment directly documenting the disconnect between decentralization legal reform and continued centralized control over community-based water-management systems. NOT effect_sizes eligible: qualitative institutional/governance assessment, no regression-based estimate. Extracted for record_id R582D32CAA4B0.",
    )

# S957 - Rydhagen - Feminist Sanitary Engineering, Vioolsdrif, South Africa
add("S957",
    citation="Rydhagen B (2002). Feminist Sanitary Engineering in Vioolsdrif, South Africa. Gender, Technology and Development.",
    doi="10.1080/09718524.2002.11910043",
    publication_year="2002",
    country="South Africa",
    subnational_unit="Vioolsdrif, north-western South Africa",
    legal_system="common law",
    urban_rural="rural",
    service_provider="local actors across engineering, user, environmental, cultural, and socio-economic contexts negotiating water supply and sanitation provision in Vioolsdrif",
    regulatory_model="Empirical fieldwork with interviews identifying the actors and activities involved in present and future water supply and sanitation provision attempts in Vioolsdrif, examining the gender aspects of water/sanitation access and participation in decision-making, developing the concept of 'feminist sanitary engineering' grounded in the observed negotiations between actors over infrastructure and service-provision decisions",
    population="residents of Vioolsdrif, rural north-western South Africa, lacking adequate water supply and sanitation facilities",
    sample_size="interview-based fieldwork identifying and analyzing multiple local actors and stakeholders",
    household_level="TRUE", community_level="TRUE",
    institutional_fragmentation="TRUE", discretion="TRUE", participation="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE",
    effect_measure="interview-based fieldwork analysis of decision-making actors and gender dynamics",
    effect_estimate="Successful improvement of water supply and sanitation access in Vioolsdrif is found to require negotiations among a wide range of actors spanning engineering, user, environmental, cultural, and socio-economic contexts, with women's distinct priorities and responsibilities for water supply, hygiene, and childcare systematically underrepresented in formal decision-making processes about new water schemes and sanitation infrastructure; the study identifies specific gender-differentiated barriers to women's meaningful participation in water/sanitation governance decisions and proposes a 'feminist sanitary engineering' framework -- centering gender-inclusive participation in decision-making -- as necessary for water/sanitation interventions to adequately address the needs of the community.",
    study_design="interview-based fieldwork with identification and analysis of decision-making actors",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="Moderate: original interview-based fieldwork directly documenting how gender-differentiated participation in local water/sanitation decision-making institutions shapes service-provision outcomes, though without a quantified comparative estimate.",
    source_document="Rydhagen 2002, Gender, Technology and Development (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established gender-participation/decision-making institutional inclusion precedent (O'Reilly Rajasthan gender participation; Roncoli-type participation studies): original interview-based fieldwork directly documenting gender-differentiated participation in local water/sanitation decision-making institutions. NOT effect_sizes eligible: qualitative interview-based fieldwork, no regression-based estimate. Extracted for record_id R6A629E95E47B.",
    )

# S958 - Carrera & Flowers - Sanitation Inequity, Lowndes County Alabama
add("S958",
    citation="Carrera JS, Flowers CC (2018). Sanitation Inequity and the Cumulative Effects of Racism in Colorblind Public Health Policies. American Journal of Economics and Sociology.",
    doi="10.1111/ajes.12228",
    publication_year="2018",
    country="United States",
    subnational_unit="Lowndes County, Alabama",
    legal_system="common law",
    urban_rural="rural",
    service_provider="Lowndes County public health department and courts enforcing Alabama state sanitary-handling-of-sewage health code, against a backdrop of the heir-property land-tenure system and historic racial housing patterns",
    regulatory_model="Documentary/case-study analysis tracing the structural dimensions of race in land tenure (heir property system), housing availability, and public health law enforcement in Lowndes County, Alabama's Black Belt, showing how cumulative, facially colorblind public-health sanitation-law enforcement -- overlain on explicitly racist historical foundations (Jim Crow-era racial exclusion, land dispossession) -- operates as a persistent mechanism producing contemporary racial stratification in access to legal, functioning sanitation infrastructure, illustrated by a documented case of a Black family facing $500/day fines, eviction, and arrest for a failing septic system they could not afford to replace (estimated $15,000-$20,000, exceeding the value of their home)",
    population="Black residents of Lowndes County, Alabama's Black Belt (majority-Black rural county)",
    sample_size="single-county documentary/case-study analysis with an illustrative enforcement case",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", property="TRUE", enforcement="TRUE", sanction="TRUE", tenure="TRUE",
    formal_connection="TRUE", sanitation_access="TRUE", affordability="TRUE",
    effect_measure="documentary/case-study analysis of land-tenure, housing, and public-health-law enforcement records",
    effect_estimate="Between 50% and 90% of households in Lowndes County, Alabama live with failing or completely absent septic systems, with residents relying on buried holding drums, 'straight piping,' open cesspools, or broken systems; when residents cannot afford advanced treatment systems costing $15,000-$20,000 (exceeding the median value of Black-owned homes, $45,400, and far exceeding mobile-home values around $23,900), they face public-health-code enforcement actions including fines up to $500/day, eviction, and arrest, as documented in a specific case; a subsequent parasitological study found more than one-third of tested residents positive for soil-transmitted helminths associated with poor sanitation typical of developing-country conditions; the authors demonstrate that this outcome results from the cumulative effect of facially colorblind sanitation-law enforcement operating atop structurally racist land-tenure (heir property) and historical housing-exclusion patterns, constituting public health sanitation law as a persistent mechanism of racial stratification.",
    study_design="single-county documentary/case-study analysis with land-tenure, housing, and legal-enforcement records",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: rigorous documentary/case-study analysis directly linking specific legal/institutional mechanisms (public-health sanitation-law enforcement, heir-property land-tenure system) to race-differentiated household sanitation-access denial, illustrated by a documented enforcement case.",
    source_document="Carrera & Flowers 2018, American Journal of Economics and Sociology (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established environmental-justice/discriminatory-infrastructure-denial inclusion precedent (Johnson et al Mebane NC racial apartheid, this same segment): rigorous documentary case study directly linking public-health sanitation-law enforcement and land-tenure legal structures to race-differentiated sanitation-access denial. NOT effect_sizes eligible: documentary case-study analysis, no regression-based estimate. Extracted for record_id R57B19F9E60B7.",
    )

# S959 - Hossain - informal practice of appropriation and social control, Dhaka bosti
add("S959",
    citation="Hossain S (2011). The informal practice of appropriation and social control - experience from a bosti in Dhaka. Environment and Urbanization.",
    doi="10.1177/0956247811418734",
    publication_year="2011",
    country="Bangladesh",
    subnational_unit="an inner-city bosti (informal settlement), Dhaka",
    legal_system="common law",
    urban_rural="urban",
    service_provider="informal, non-statutory local actors (local associations, NGOs, and powerful/well-connected inhabitants) supplying and regulating land allocation and water supply, given bosti residents' exclusion from statutory institutional access to municipal services",
    regulatory_model="Empirical case study of an inner-city bosti in Dhaka examining the local practices of land allocation and water supply, analyzing the contestation and negotiation processes in an informal regulatory sphere that continuously (re)defines inhabitants' differential access to urban utilities based on their individual position within prevailing local power relations, characterizing this informal regulatory sphere as a 'closed system' dominated by powerful and relatively well-off inhabitants that actively limits others' ability to enter the negotiation process",
    population="inhabitants of an inner-city bosti (informal settlement) in Dhaka, over one-third of the city's total population lives in bosti",
    sample_size="single-settlement empirical case study",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", institutional_fragmentation="TRUE", discretion="TRUE", bureaucratic_assistance="TRUE",
    formal_connection="TRUE", water_access="TRUE",
    effect_measure="empirical case-study analysis of informal land-allocation and water-supply regulatory practices",
    effect_estimate="Because bosti inhabitants cannot comply with statutory institutional obligations for accessing municipal services, they are formally excluded from state public provision, resulting in non-statutory actors (local associations, NGOs, and powerful well-connected inhabitants) mobilizing informal relationships to make water supply and other urban utilities available; the study documents that this informal regulatory sphere functions as a 'closed system' in which the powerful and relatively well-off dominate the contestation and negotiation process over land allocation and water access, actively benefiting from it, while poorer and less-connected inhabitants' dependency on these powerful actors limits any possibility of countering the closed regulatory system, demonstrating that informal, non-statutory institutional arrangements -- not merely the absence of formal infrastructure -- directly determine differential household water-access outcomes within the settlement.",
    study_design="single-settlement empirical case study of informal land and water-supply regulatory practices",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: original empirical case study directly documenting how informal, non-statutory regulatory institutions determine differential household water-access outcomes within an informal settlement excluded from statutory service provision.",
    source_document="Hossain 2011, Environment and Urbanization (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established informal-settlement state-non-recognition ethnographic inclusion precedent (Wahby Cairo; earlier Hossain Dhaka bosti studies): original empirical case study directly documenting how informal regulatory institutions determine differential household water-access outcomes for statutorily excluded informal-settlement residents. NOT effect_sizes eligible: single-settlement qualitative case study, no regression-based estimate. Extracted for record_id R567A3B014963.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
