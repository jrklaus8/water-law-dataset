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

# S960 - Narzetti & Marques - Isomorphic mimicry and WSS reforms in Brazil
add("S960",
    citation="Narzetti DA, Marques RC (2021). Isomorphic mimicry and the effectiveness of water-sector reforms in Brazil. Utilities Policy.",
    doi="10.1016/j.jup.2021.101217",
    publication_year="2021",
    country="Brazil",
    subnational_unit="national, with focus on peri-urban and rural areas",
    legal_system="civil law",
    urban_rural="both",
    service_provider="municipal WSS providers (direct, delegated, or private-concession), state companies (CESBs), consortia; regulated (from 2020) at the national level by the National Water and Basic Sanitation Agency (ANA) and by 73 decentralized state/intermunicipal/municipal regulatory agencies",
    regulatory_model="Policy-institutions-regulation (PIR) case-study analysis of Brazil's WSS legal and institutional framework across four historical reform waves (1968 PLANASA, 1986 municipalization/SNIS, 2007 Law 11.445, 2020 Law 14.026), documenting how de jure legal reforms (national WSS policy, decentralized regulatory-agency mandates, universal-access targets of 99% water/90% sanitation by 2033) have failed to translate into de facto universal access due to isomorphic mimicry -- the adoption of institutional forms modeled on higher-income countries without adaptation to local capacity/context -- particularly for peri-urban informal settlements and rural areas excluded from both the Ministry of Cities/MDR (urban, >50,000 inhabitants) and FUNASA (rural/small-municipality) institutional divide",
    population="Brazilian population lacking sustainable WSS access, with particular focus on the ~16 million peri-urban/informal-settlement residents (8% of population) and rural areas (~15% of population)",
    sample_size="national policy/institutional case-study analysis",
    household_level="FALSE", community_level="TRUE",
    eligibility="TRUE", legal_status="TRUE", institutional_fragmentation="TRUE", political_coordination="TRUE", discretion="TRUE", enforcement="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE", service_coverage="TRUE",
    effect_measure="policy/institutional/regulatory (PIR) documentary case-study analysis with national coverage statistics",
    effect_estimate="Despite four successive waves of legally well-designed WSS reforms culminating in Law 11.445 (2007) and Law 14.026 (2020) targeting 99% water and 90% sanitation coverage by 2033, in 2018 approximately 16% of Brazilians (35 million) lacked water supply and 47% (100 million) lacked wastewater collection, with peri-urban/informal-settlement populations (~16 million, 8% of the population) and rural areas (~15% of the population) essentially excluded from institutional coverage because the Ministry of Regional Development covers only municipalities over 50,000 inhabitants and FUNASA's rural mandate is chronically underfunded and uncoordinated with urban investment; of Brazil's 73 WSS regulatory agencies created under the decentralized regulatory model, the large majority do not de facto regulate service quality or informal/vulnerable-area access despite being required to do so de jure, illustrating that isomorphic mimicry -- copying institutional forms (regulatory agencies, universal-access legal mandates) from higher-income contexts without adapting to local capacity and informal-settlement realities -- is the primary driver of the persistent gap between Brazil's de jure legal framework and de facto WSS access outcomes.",
    table="Fig. 1 (WSS public policies); Fig. 2 (WSS sector institutions); Fig. 3 (WSS regulatory structure, 73 agencies)",
    study_design="policy/institutional/regulatory (PIR) documentary case-study analysis with historical legal-reform tracing and national coverage statistics",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: detailed documentary analysis directly tracing Brazil's WSS legal/regulatory framework (four reform waves, institutional mandates, regulatory-agency structure) against national coverage outcomes, explicitly diagnosing the institutional mechanism (isomorphic mimicry, de jure/de facto gap) driving persistent peri-urban and rural access exclusion.",
    source_document="Narzetti & Marques 2021, Utilities Policy (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: rigorous PIR (policy/institutions/regulation) documentary case study directly linking Brazil's legal/regulatory reform framework to persistent peri-urban and rural WSS access exclusion, consistent with the established institutional-legal-framework inclusion precedent. NOT effect_sizes eligible: documentary/descriptive institutional analysis with coverage statistics, no regression-based estimate isolating a single mechanism. Extracted for record_id R566E192D76F6.",
    )

# S961 - Kachenje - Community-based water supply scheme, Dar es Salaam
add("S961",
    citation="Kachenje YE (2019). Strengths and Weaknesses of Community-Based Systems in Municipal Services Delivery: The Case of a Community-Based Water Supply Scheme in Dar es Salaam, Tanzania. In: Social Responsibility and Sustainability, World Sustainability Series, Springer.",
    doi="10.1007/978-3-030-03562-4_23",
    publication_year="2019",
    country="Tanzania",
    subnational_unit="Mamboleo 'B' and Kisiwani, Temeke Municipality, Dar es Salaam",
    legal_system="common law",
    urban_rural="urban",
    service_provider="community-based Water Committee (WC), operating under the Water Committees Constitution of 2003 prepared by Temeke Municipal Council, with oversight from the Municipal Water Engineer, Ward Executive Officer, and Mtaa (sub-ward) Committee",
    regulatory_model="Qualitative case-study methodology (key informant interviews, focus group discussion with 14 members/leaders, household interviews, document analysis) of one of 130 community-based water supply schemes in Dar es Salaam, examining institutional structure, rules (Water Committees Constitution 2003), financial sustainability, and connection-processing efficiency, in an area where public piped water supply has never been available",
    population="approximately 8,225 residents (2,228 households) of Mamboleo 'B' and Kisiwani sub-wards, Temeke Municipality, Dar es Salaam",
    sample_size="qualitative case study: 5 Mtaa leaders, 3 water committee leaders, 3 water sales attendants, 4 municipal officials, 4 public service provider officials, plus household interviews and 14-member focus group",
    household_level="TRUE", community_level="TRUE",
    eligibility="TRUE", discretion_accommodation="TRUE", institutional_fragmentation="FALSE", procedural_steps="TRUE", delay="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_reliability="TRUE",
    effect_measure="qualitative case-study analysis of institutional rules, financial performance, and connection-processing timelines",
    effect_estimate="The community-based Water Committee (WC), operating under a formal municipal-council-issued constitution (2003) with defined institutional levels (Mtaa/Ward/Municipality) and an accountability chain, achieves cost-recovery financial sustainability (December 2014: TZS 3,248,540 revenue vs. TZS 3,180,200 expenditure) and processes new water-supply-connection applications in just 3-6 days, compared to approximately 4 weeks (28 days) under the public water-supply system serving other parts of the city, demonstrating that the community-based institutional/legal governance structure -- not merely infrastructure investment -- directly determines faster and more accessible household water-connection outcomes relative to the comparator public-system institutional model; weaknesses identified include outdated ICT/data-management systems and uncertainty over the schemes' long-term institutional status as the public system expands into community-based scheme areas.",
    figure="Fig. 6 (efficient water-supply connection process, 3-6 days vs. 4 weeks under public system)",
    table="Table 3 (scheme revenue/expenditure, December 2014)",
    study_design="qualitative case study with key informant interviews, focus group discussion, household interviews, and document analysis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: original qualitative case study directly documenting how a formally constituted community-based institutional governance structure (Water Committees Constitution 2003, accountability chain) produces measurably faster household water-connection processing than the comparator public-system institutional model.",
    source_document="Kachenje 2019, Social Responsibility and Sustainability (Springer) (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established community-based water-institution governance inclusion precedent: original qualitative case study directly comparing community-based vs. public institutional connection-processing outcomes. NOT effect_sizes eligible: qualitative case study with descriptive comparison, no regression-based estimate. Extracted for record_id R5597D1B7A139.",
    )

# S962 - Rusca, Alda-Vidal & Kooy - Sanitation justice, Kampala
add("S962",
    citation="Rusca M, Alda-Vidal C, Kooy M (2018). Sanitation Justice? The Multiple Dimensions of Urban Sanitation Inequalities. In: Water Justice, Cambridge University Press.",
    doi="10.1017/9781316831847.014",
    publication_year="2018",
    country="Uganda",
    subnational_unit="Kawempe District, Kampala",
    legal_system="common law",
    urban_rural="urban",
    service_provider="National Water and Sewerage Corporation (parastatal, nominally responsible for sewerage), private/community-based small-scale sanitation providers, and NGOs (Plan International, WaterAid, CIDI, SSWARS) promoting decentralized onsite sanitation following the 1997 Strategic Framework for Reform (SFR) and Declaration on Sanitation, which shifted sanitation from a state to a household responsibility",
    population="approximately 260,000 inhabitants of Kawempe District, one of Kampala's fastest-growing informal settlements",
    sample_size="semi-structured interviews with local government, residents, donors, and international/local NGOs/CBOs (2011), complemented by documentary analysis of World Bank and other project reports and policy documents",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", discretion_accommodation="TRUE", institutional_fragmentation="TRUE", participation="TRUE", fees="TRUE",
    formal_connection="TRUE", sanitation_access="TRUE", affordability="TRUE",
    effect_measure="interview-based qualitative case-study analysis of distributive, procedural, and recognitional dimensions of sanitation policy",
    effect_estimate="Following Uganda's 1997 Strategic Framework for Reform, which institutionally transferred sanitation-provision responsibility from the state (National Water and Sewerage Corporation) to individual households while positioning the state merely to facilitate private/NGO-led delivery, between 64% and 75% of Kawempe District's approximately 260,000 inhabitants lack access to adequate sanitation despite ongoing NGO programs; the study documents that this decentralized, demand-based, commercially-oriented institutional model produces distributionally unjust outcomes because construction/maintenance/pit-emptying costs and responsibilities fall on individual households (with the poorest resorting to open defecation or 'flying toilets'), and that participatory approaches promoted under this model function as consumer-oriented demand generation (landlords incentivized by rental-income gains, 'sanitation marketing') rather than genuine procedural inclusion in decisions about what constitutes adequate sanitation, demonstrating that a specific institutional/legal policy shift (1997 SFR devolving state sanitation responsibility to households) is a direct driver of persistent low-income urban sanitation-access inequality.",
    study_design="semi-structured interview-based qualitative case study with documentary/policy analysis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: original interview-based case study directly tracing a specific national policy/institutional reform (1997 Strategic Framework for Reform devolving sanitation responsibility to households) to quantified sanitation-access-coverage outcomes in a low-income urban settlement.",
    source_document="Rusca, Alda-Vidal & Kooy 2018, Water Justice (Cambridge University Press) (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established decentralization-policy/sanitation-access inclusion precedent: original interview-based case study directly linking a specific national institutional policy reform to sanitation-access outcomes in an informal settlement. NOT effect_sizes eligible: qualitative interview-based case study, no regression-based estimate. Extracted for record_id R5088AD87DF7C.",
    )

# S963 - Nastar & Ramasar - South African water governance transition, Johannesburg
add("S963",
    citation="Nastar M, Ramasar V (2012). Transition in South African water governance: Insights from a perspective on power. Environmental Innovation and Societal Transitions.",
    doi="10.1016/j.eist.2012.05.001",
    publication_year="2012",
    country="South Africa",
    subnational_unit="Alexandra and Soweto (Phiri), City of Johannesburg",
    legal_system="common law",
    urban_rural="urban",
    service_provider="Johannesburg Water (independent municipal-owned utility company, established January 2001), City of Johannesburg, Alexandra Renewal Project, under the National Water Act 1998 and the 1996 Constitution's basic-water-access right",
    regulatory_model="Interview-based case-study analysis (5 in-depth resident interviews plus 5 expert interviews in Alexandra; documentary/secondary-source analysis and narrative walks in Soweto/Phiri) applying a transition-heuristic and power-analysis framework to the post-apartheid legal/institutional transformation of Johannesburg's water service delivery, tracing the National Water Act 1998, the free-basic-water policy (2001, 6,000 L/household/month or 25 L/person/day), and the pre-paid water meter litigation in Phiri (Mazibuko v City of Johannesburg) through South African courts",
    population="residents of Alexandra (formal houses, apartment blocks, informal shacks; ~19 households per stand in Old Alexandra) and Soweto/Phiri, former apartheid-era townships in Johannesburg",
    sample_size="5 in-depth resident interviews and 5 expert interviews in Alexandra; documentary/secondary-source case analysis of the Phiri pre-paid-meter court case in Soweto",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", discretion_accommodation="TRUE", fees="TRUE", administrative_review="TRUE", judicial_review="TRUE", disconnection="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE",
    effect_measure="interview-based case-study and litigation-tracing analysis of legal/institutional water-governance transition",
    effect_estimate="Post-apartheid legal reform (National Water Act 1998, Constitutional right to basic water access, free-basic-water policy of 6,000 L/household/month) produced markedly uneven water-service outcomes across two similarly disadvantaged former townships: in Alexandra, ~90% of households are formally connected but service levels remain highly unequal (up to 19 households sharing one communal tap/toilet in Old Alexandra vs. individual in-house connections in wealthier East Bank), with the state's subsidized free-water allocation accepted without resistance; in Soweto's Phiri neighborhood, Johannesburg Water's 2001 introduction of mandatory pre-paid water meters (restricting consumption once the free allocation was exhausted) was challenged by residents in court, and in April 2008 the South African High Court ruled the practice unconstitutional and ordered the free-water allocation raised from 25 L to 50 L per person per day with an ordinary credit-metered option, before the Supreme Court of Appeal overturned this ruling in October 2009 and declared pre-paid meters lawful (while ordering indigent-registered households receive 42 L/person/day); this demonstrates that formally equivalent constitutional/statutory water-access rights produce divergent household water-access and payment-mechanism outcomes depending on the specific municipal-level institutional implementation and its contestation through the judicial system.",
    figure="Fig. 2 (access to water by population group); Fig. 3 (water infrastructure in Alexandra)",
    study_design="interview-based case-study analysis with litigation tracing (High Court and Supreme Court of Appeal rulings) and documentary policy analysis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: original interview-based case study directly tracing specific legal/institutional mechanisms (National Water Act, free-basic-water policy, pre-paid-meter litigation and appellate reversal) to divergent household water-access and payment outcomes across two comparable townships.",
    source_document="Nastar & Ramasar 2012, Environmental Innovation and Societal Transitions (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, strong match to Family A/C framework: original case study directly linking a specific legal/institutional mechanism (constitutional water right, free-basic-water policy, pre-paid-meter court litigation) to household water-access and disconnection/payment outcomes. NOT effect_sizes eligible: qualitative interview-based case study with litigation tracing, no regression-based estimate. Extracted for record_id R5207E9C3B055.",
    )

# S964 - Laurie & Crespo - La Paz-El Alto water politics, Bolivia
add("S964",
    citation="Laurie N, Crespo C (2007). Deconstructing the best case scenario: lessons from water politics in La Paz-El Alto, Bolivia. Geoforum.",
    doi="10.1016/j.geoforum.2006.08.008",
    publication_year="2007",
    country="Bolivia",
    subnational_unit="La Paz and El Alto",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="Aguas del Illimani (private concessionaire, Suez/Lyonnaise des Eaux-led consortium, 1997-2005 concession), regulated by the Superintendence of Water and Sanitation (Regulator) established 1997, under drinking-water/sanitation Law 2029 (1999)",
    regulatory_model="Mixed-methods case study (household-to-household survey of 10% of households across 4 communities with differing service levels, in-depth fieldwork February 2002, discourse analysis of the Bolivian regulatory framework and two private water-company contracts) examining the 1997-2005 La Paz-El Alto water concession, its 'mandate to extend' connection clause, tariff/metering structure, the pilot condominial (low-cost simplified sewerage) system, and the regulatory framework's lack of formal user-participation requirements in rate-setting, against the concession's internationally promoted 'pro-poor' reputation",
    population="poor households in El Alto and La Paz, Bolivia, particularly the 4 surveyed communities (Rio Seco, Villa Ingenio, Kenko, 27 de Mayo) with differing service levels",
    sample_size="household-to-household survey of 10% of households across 4 communities; in-depth fieldwork February 2002; documentary/contract analysis",
    household_level="TRUE", community_level="TRUE",
    eligibility="TRUE", fees="TRUE", discretion_accommodation="TRUE", institutional_fragmentation="TRUE", participation="TRUE", procedural_steps="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE", affordability="TRUE",
    effect_measure="mixed-methods household survey and documentary/contract analysis of concession regulatory framework and connection/tariff outcomes",
    effect_estimate="The La Paz-El Alto water concession's 'mandate to extend' clause, internationally promoted as a pro-poor best practice, is shown to have produced coverage figures inflated by counting network densification in already-served areas (79% of new potable-water connections and 54% of new sewerage connections were densification rather than true network expansion to unconnected poor areas), with the Superintendent of Water publicly conceding in 2005 that reported 100% El Alto potable-water coverage referred only to the already-served area rather than the full concession area; the Bolivian regulatory framework (established under Law 2029, 1999, two years after the concession itself) requires only direct negotiation between the Regulator and company with no formal mechanism for user participation in tariff-setting, and a tariff hike of 57.7% imposed by the state immediately prior to privatization (generating an estimated $157 million in extra company profit over the 30-year concession) combined with un-metered connections charged at higher average rates to disproportionately burden poor households; sustained social protest and 2007 litigation-adjacent contestation eventually forced early termination of the concession in 2005, demonstrating that the specific legal/regulatory design of a private-concession contract and its associated regulatory-oversight framework -- not aggregate private investment -- directly determined which households received genuine new water/sanitation access versus merely nominal, cost-inflating densification.",
    figure="Fig. 2 (new connections vs. densification, 2006); Fig. 3 (tariff rates by category and consumption range); Fig. 4 (condominial vs. conventional connection costs)",
    study_design="mixed-methods case study with 10%-household survey across 4 communities, fieldwork, and regulatory/contract documentary analysis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: rigorous mixed-methods case study directly tracing a specific concession contract's legal design (connection mandate, tariff-setting regulatory process, densification-counting practices) to differential household water/sanitation connection outcomes for the poor.",
    source_document="Laurie & Crespo 2007, Geoforum (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, strong match to Family A/C framework: rigorous mixed-methods case study directly linking a specific private-concession legal/regulatory contract design to differential household water/sanitation connection outcomes for the poor. NOT effect_sizes eligible: mixed-methods case study with descriptive coverage/tariff analysis, no regression-based estimate isolating a single mechanism. Extracted for record_id R4DBC86E42AB3.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
