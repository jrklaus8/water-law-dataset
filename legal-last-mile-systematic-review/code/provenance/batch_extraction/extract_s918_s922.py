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

# S918 - Martinez-Espineira, Garcia-Valinas & Gonzalez-Gomez - Spanish water pricing inequality
add("S918",
    citation="Martinez-Espineira R, Garcia-Valinas MA, Gonzalez-Gomez F (2012). Is the Pricing of Urban Water Services Justifiably Perceived as Unequal among Spanish Cities? International Journal of Water Resources Development.",
    doi="10.1080/07900627.2012.642231",
    publication_year="2012",
    country="Spain",
    subnational_unit="multiple Spanish cities",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="local monopoly water utilities under decentralized Spanish/EU regulatory framework (no EU-level regulation of urban water pricing)",
    regulatory_model="Econometric analysis of the absence of EU-level and limited national-level regulation of urban water tariffs in Spain, examining whether significant water-price differences among Spanish cities reflect legitimate cost differentials or arbitrary decisions by local policy and business decision-makers under a decentralized, largely unregulated local-monopoly institutional structure, with particular attention to fairness in pricing for the lowest consumption blocks associated with water as a merit good",
    population="residential water customers across multiple Spanish cities",
    sample_size="multi-city panel of Spanish urban water tariffs",
    household_level="FALSE", community_level="TRUE",
    legal_status="TRUE", fees="TRUE", institutional_fragmentation="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE",
    effect_measure="econometric tariff-differential analysis",
    effect_estimate="Significant residential water-price differences persist among Spanish cities despite the absence of clear cost-based justification; the study finds that some of these differences are attributable to arbitrary decisions by policy and business decision-makers operating under a decentralized regulatory vacuum (no EU-level regulation of urban water pricing and limited national oversight), rather than reflecting legitimate cost differentials, with particular unfairness concentrated in the lowest consumption blocks essential for basic survival needs, leading the authors to recommend adoption of regulatory criteria for tariff design to protect affordability of merit-good-level water consumption.",
    study_design="econometric tariff-differential analysis of municipal water pricing",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: econometric analysis directly linking the absence of a specific regulatory framework for urban water tariffs to quantified, unjustified price disparities affecting affordability across Spanish cities.",
    source_document="Martinez-Espineira, Garcia-Valinas & Gonzalez-Gomez 2012, International Journal of Water Resources Development (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established tariff-regulation inclusion precedent (Whittington S897): econometric analysis directly linking a specific regulatory gap to quantified water-price/affordability disparities. NOT effect_sizes eligible: descriptive tariff-differential analysis without a clean regression isolating a single institutional mechanism in the Family A/B/C sense. Extracted for record_id R8DF8439BABC3.",
    )

# S919 - Peal, Evans, Blackett, Hawkins & Heymans - FSM comparative analysis 12 cities
add("S919",
    citation="Peal A, Evans B, Blackett I, Hawkins P, Heymans C (2014). Fecal sludge management: a comparative analysis of 12 cities. Journal of Water, Sanitation and Hygiene for Development.",
    doi="10.2166/washdev.2014.139",
    publication_year="2014",
    country="Bolivia; Honduras; Nicaragua; Mozambique; Senegal; Uganda; Bangladesh; India; Cambodia; Indonesia; Philippines",
    subnational_unit="12 cities: Santa Cruz, Tegucigalpa, Managua, Maputo, Dakar, Kampala, Dhaka, Delhi, Phnom Penh, Palu, Dumaguete, Manila",
    legal_system="mixed (civil and common law jurisdictions)",
    urban_rural="urban",
    service_provider="municipal governments and private/informal fecal-sludge-management operators across 12 cities in low- and middle-income countries",
    regulatory_model="Comparative institutional assessment (key-informant interviews plus secondary data, structured using a modified Service Delivery Assessment (SDA) tool and fecal-waste-flow-diagram methodology) of fecal sludge management (FSM) institutional context and outcomes across 12 cities, scoring each city's enabling environment (policy, budget, institutional responsibility), service development, and service sustainability, developing a three-type city typology (poor/basic/improving FSM) linked to the percentage of fecal waste safely managed",
    population="urban residents relying on on-site sanitation (non-sewered) systems across 12 cities",
    sample_size="12-city comparative institutional assessment (key-informant interviews plus secondary data)",
    household_level="FALSE", community_level="TRUE",
    documentation="TRUE", institutional_fragmentation="TRUE", eligibility="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_quality="TRUE",
    effect_measure="comparative institutional scoring (modified Service Delivery Assessment) with quantified outcome data",
    effect_estimate="Across all 12 cities studied, none achieved a complete FSM institutional framework, but institutional-context scores (enabling environment: policy, budget, institutional responsibility) correlated with the percentage of fecal waste safely managed: in Type 1 'poor FSM' cities with little or no institutional framework (e.g., Dhaka, Delhi, Phnom Penh), 0% of on-site-generated fecal waste was safely managed; in the Type 3 'improving FSM' city with the strongest enabling-environment framework (Dakar, benefiting from a World Bank institutional/infrastructure investment project), safe management was substantially higher; only the two smallest cities with simple, well-designed institutional/technical containment systems (Palu, Dumaguete) achieved 95% safe management, demonstrating that specific, scored institutional/regulatory framework strength directly predicts sanitation-service safe-management outcomes across a diverse 12-city sample.",
    table="Table 1 (12 city case studies); Table 2 (safe fecal-waste management by city); Figures 1-9 (SDA scorecards, typology, waste-flow diagrams)",
    study_design="comparative institutional assessment (12-city structured scoring methodology)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: structured comparative institutional assessment (key-informant interviews plus a standardized scoring tool) directly linking institutional/regulatory enabling-environment strength to quantified sanitation-service safe-management outcomes across 12 cities.",
    source_document="Peal, Evans, Blackett, Hawkins & Heymans 2014, Journal of Water, Sanitation and Hygiene for Development (retrieved via Google Drive)",
    section="Results; Discussion",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established institutional-governance/FSM inclusion precedent (Akumuntu S905, Batch 180), distinguished from the excluded market-efficiency-framed Frenoux/Tsitsikalis Cambodia paper (Batch 179): despite the journal's 'Review Paper' article-type label, this is genuine original comparative institutional research (key-informant interviews, a standardized scoring tool applied across 12 cities) rather than a synthesis of prior published studies, consistent with the E12 precedent applying only to literature-synthesis reviews (cf. Dos Santos, Batch 177; Devkar, Batch 178). NOT effect_sizes eligible: comparative institutional scoring across 12 cities, no regression-based estimate. Extracted for record_id R8C6C4D410F39.",
    )

# S920 - Barde - Brazil WUA vs local government piped water access DiD
add("S920",
    citation="Barde JA (2017). What Determines Access to Piped Water in Rural Areas? Evidence from Small-Scale Supply Systems in Rural Brazil. World Development.",
    doi="10.1016/j.worlddev.2017.02.012",
    publication_year="2017",
    country="Brazil",
    subnational_unit="rural municipalities nationwide",
    legal_system="civil law",
    urban_rural="rural",
    service_provider="water user associations (WUAs, community-based/participatory institutional model) versus local municipal governments (non-participatory institutional model), both implementing small-scale rural water supply systems under Brazil's decentralized post-1990s water-sector institutional framework",
    regulatory_model="Difference-in-differences estimator combined with kernel matching (Brazilian census 2000/2010 plus national water and sanitation survey data), comparing the causal effect of water-supply project institutional type -- community-based water user association (WUA) management versus non-participatory local government management -- on rural piped-water access rate increases, with endogeneity of project-type choice addressed via matching informed by semi-structured expert interviews, and heterogeneity analysis examining accountability channels (local media presence, political competition, pre-implementation social-group demand) as mechanisms",
    population="rural Brazilian municipalities and their populations, nationwide",
    sample_size="national municipality-level panel (Brazilian census 2000 and 2010, national water and sanitation survey)",
    household_level="FALSE", community_level="TRUE",
    legal_status="TRUE", institutional_fragmentation="TRUE", enforcement="TRUE",
    formal_connection="TRUE", water_access="TRUE",
    effect_measure="Difference-in-differences estimator with kernel propensity-score matching",
    effect_estimate="Municipalities with community-based water user association (WUA) rural water-supply projects experienced piped-water access-rate increases of approximately 6 percentage points above the national average trend (statistically significant, robust to specification changes), while municipalities with non-participatory local-government-implemented projects showed no increase significantly different from the national trend; rural access rates overall rose from 15-16% (2000) to 33.4% in WUA-served areas versus only 24.9% in local-government-served areas by 2010; heterogeneity analysis shows that in local-government-project municipalities where accountability was independently strengthened (via local media presence, higher political competition, or pre-implementation social-group mobilization demanding the project), access-rate increases became comparable to WUA-area increases, indicating that participatory institutional accountability -- not project type per se -- is the underlying causal mechanism driving better rural water-access outcomes.",
    table="results tables (DiD/kernel-matching ATT estimates); heterogeneity analysis tables (accountability channels)",
    study_design="difference-in-differences with kernel propensity-score matching, national administrative panel data",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: quasi-experimental difference-in-differences design with kernel matching directly isolating the causal effect of a specific institutional/governance mechanism (participatory community-based water management vs. non-participatory local government management) on rural piped-water access rates at national scale.",
    source_document="Barde 2017, World Development (retrieved via Google Drive)",
    section="Results; Section 5-6",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md. This is a genuine Family A (legal recognition/formal institutional-management-model and access) effect_sizes candidate -- see effect_sizes.csv addition this batch. Extracted for record_id R9502CE771F1E.",
    )

# S921 - Biddle & Baehler - NYC vs Flint polycentric governance
add("S921",
    citation="Biddle JC, Baehler KJ (2019). Breaking bad: When does polycentricity lead to maladaptation rather than adaptation? Environmental Policy and Governance.",
    doi="10.1002/eet.1864",
    publication_year="2019",
    country="United States",
    subnational_unit="New York City, New York; Flint, Michigan",
    legal_system="common law",
    urban_rural="urban",
    service_provider="New York City Department of Environmental Protection; Flint, Michigan water system, both operating under the U.S. Safe Drinking Water Act's devolved polycentric federalism structure",
    regulatory_model="Two-case comparative process-tracing study contrasting New York City's water system (an internationally recognized model of sustainable, collaborative polycentric governance) with Flint, Michigan's water system (which suffered catastrophic governance failure and a lead-contamination crisis in the mid-2010s), tracing how both cities began from the same shared polycentric-federalism governance structure under the Safe Drinking Water Act but diverged sharply due to differing cross-cutting conditions -- norms of rule enforcement, blame-avoidance incentives, power imbalances, wealth inequality, and social capital/leadership deficits",
    population="New York City and Flint, Michigan drinking-water-system service populations",
    sample_size="two-case comparative process-tracing study",
    household_level="FALSE", community_level="TRUE",
    legal_status="TRUE", institutional_fragmentation="TRUE", enforcement="TRUE", discretion="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_quality="TRUE", service_reliability="TRUE",
    effect_measure="two-case comparative process-tracing analysis",
    effect_estimate="Although both New York City and Flint, Michigan operate under the same polycentric federal governance structure devolved by the Safe Drinking Water Act, process tracing reveals that polycentricity produced starkly divergent water-system outcomes -- sustainable, adaptive governance in New York City versus a catastrophic lead-contamination governance failure in Flint -- because of differing cross-scale conditions including norms of quiescent rule enforcement, incentives favoring blame avoidance over problem-solving, persistent power imbalances, large wealth inequalities, and deficits of social capital and local leadership, demonstrating that the mere structural presence of a polycentric legal/institutional governance arrangement does not by itself determine water-access and water-quality outcomes; the functional conditions under which that structure operates are decisive.",
    study_design="two-case comparative process-tracing analysis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: rigorous two-case comparative process-tracing analysis directly documenting how the same formal polycentric governance structure under a specific federal legal framework (Safe Drinking Water Act) produced starkly divergent water-access/quality outcomes depending on cross-cutting institutional conditions.",
    source_document="Biddle & Baehler 2019, Environmental Policy and Governance (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established polycentric-governance/comparative-case inclusion precedent (Kornberg S888 Detroit): two-case comparative process-tracing analysis directly documenting how a specific federal legal governance structure (Safe Drinking Water Act polycentric federalism) produces divergent water outcomes across cross-cutting institutional conditions. NOT effect_sizes eligible: qualitative two-case comparative process-tracing, no regression-based estimate. Extracted for record_id R94E2C2B0C8C2.",
    )

# S922 - Rachwal - UK Thames Water 30-year privatisation history
add("S922",
    citation="Rachwal T (2007). 30 Years of technical and organisational development in the UK water sector: Thames Water's experiences of moving from public to private sector. Journal of Water Supply: Research and Technology-AQUA.",
    doi="10.2166/aqua.2007.014",
    publication_year="2007",
    country="United Kingdom",
    subnational_unit="Thames Water service region (London and surrounding Thames catchment)",
    legal_system="common law",
    urban_rural="both",
    service_provider="Thames Water Plc, under the UK's 1989 water-industry privatisation legal framework and OFWAT/Environment Agency/Drinking Water Inspectorate regulatory structure",
    regulatory_model="Documentary/historical practitioner analysis of 30 years (1974-2006) of UK water-sector institutional change, tracing the 1974 formation of publicly-owned integrated river-basin Water Authorities, the 1989 privatisation of the water industry into shareholder-owned companies with a new three-regulator institutional framework (OFWAT for prices/investment, Environment Agency for water resources, Drinking Water Inspectorate for quality), and quantifying the resulting effects on household water/wastewater bills, service-quality compliance, capital investment, and customer-service standards over the post-privatisation period",
    population="Thames Water and England/Wales water-utility household customers",
    sample_size="documentary/historical institutional analysis, 1974-2006/07",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", fees="TRUE", enforcement="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE", service_quality="TRUE",
    effect_measure="documentary/historical institutional analysis with quantified regulatory and pricing data",
    effect_estimate="Following the UK's 1989 water-industry privatisation legal framework, average annual household water/wastewater bills in England and Wales rose from a 1989 baseline to GBP294 by 2006/07 (a real-terms increase of 39%, or 2% per year) alongside GBP55 billion in private capital investment over 17 years, with the new OFWAT/Environment Agency/Drinking Water Inspectorate regulatory framework producing substantial improvements in drinking-water and river-water-quality compliance (UK moving from having one of the worst water-quality compliance records in Europe to one of the highest) and instituting five-year price-and-investment review cycles (AMP1-AMP4) with formula-based price regulation (RPI-X+Q); a notable post-privatisation consumer protection was the removal of water utilities' ability to disconnect customers for non-payment, unlike privatised electricity/gas utilities, demonstrating how the specific post-privatisation regulatory legal framework directly shaped both affordability outcomes (rising bills) and access-protection outcomes (disconnection prohibition) for household customers.",
    table="Figure 1 (average household bills 1989-2006); Figure 2 (comparison of water/sewerage companies' household bills by region)",
    study_design="documentary/historical institutional analysis (practitioner perspective)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: documentary/historical analysis with quantified regulatory and pricing data directly linking a specific national privatisation legal framework and its regulatory institutions to household water-affordability and access-protection outcomes over a 17-year period.",
    source_document="Rachwal 2007, Journal of Water Supply: Research and Technology-AQUA (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established water-privatisation/regulatory-framework inclusion precedent (Larrain S901 Chile): documentary/historical institutional analysis directly linking a national privatisation legal framework to quantified household affordability and access-protection outcomes. NOT effect_sizes eligible: descriptive documentary/historical analysis, no regression-based estimate isolating the mechanism. Extracted for record_id R88AA43E1DE4C.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
