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

# S890 - Aleixo, Rezende, Pena, Zapata & Heller - Brazil PLANSAB
add("S890",
    citation="Aleixo B, Rezende S, Pena JL, Zapata G, Heller L (2016). Human Right in Perspective: Inequalities in Access to Water in a Rural Community of the Brazilian Northeast. Ambiente & Sociedade.",
    doi="10.1590/1809-4422ASOC150125R1V1912016",
    publication_year="2016",
    country="Brazil",
    subnational_unit="Cristais community, Ceara state (Northeast Brazil)",
    legal_system="civil law",
    urban_rural="rural",
    service_provider="rural water supply and sanitation management model implemented under the DESAFIO governance-innovation project, evaluated against Brazil's National Basic Sanitation Plan (PLANSAB) legal framework (Act No. 11.445/2007)",
    regulatory_model="Household survey (232 questionnaires, May-July 2014) documenting within-community inequalities in water access conditions in a rural community about to receive a piped Water Supply System (WSS), examined against Brazil's national legal framework for universalizing water/sanitation access (PLANSAB, Act 11.445/2007), measuring quantity used (liters/person/day), physical accessibility (collection time) and economic accessibility (% of income spent on water) as part of a before/after evaluation of a rural water-supply-and-sanitation governance intervention",
    population="households in the Cristais rural community, Ceara, Brazil",
    sample_size="232 household questionnaires (May-July 2014)",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", tenure="TRUE", fees="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE",
    effect_measure="household survey with quantified access/affordability indicators",
    effect_estimate="Within the Cristais community, which lacked a formal piped Water Supply System (WSS), the study found significant inequalities in water access conditions -- quantity consumed, physical accessibility (collection time), and economic accessibility (percentage of income spent) -- even among households equally lacking WSS connections, demonstrating that inequality in water access is not solely a function of formal WSS connection status but also varies systematically among unconnected households depending on alternative-source reliance (rainwater, cisterns, public fountains, river-basin integration canals), directly informing Brazil's PLANSAB legal mandate to progressively eliminate inequality of access alongside expanding formal coverage",
    study_design="household survey (part of a before/after governance-innovation evaluation)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: a 232-household survey directly measuring quantity, physical and economic accessibility of water in a community targeted for a specific legal/institutional water-supply intervention under Brazil's national PLANSAB legal framework.",
    source_document="Aleixo, Rezende, Pena, Zapata & Heller 2016, Ambiente & Sociedade (retrieved via Google Drive)",
    section="Methodology; Results",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established national legal-framework/household-survey inclusion precedent: original household survey directly documenting water-access inequalities in a community targeted by Brazil's PLANSAB national legal framework. NOT effect_sizes eligible: descriptive household survey, no regression-based estimate isolating a specific mechanism. Extracted for record_id RB96E8D94B2BD.",
    )

# S891 - Bellaubi & Boehm - Corruption risks, Kenya and Ghana
add("S891",
    citation="Bellaubi F, Boehm F (2018). Management practices and corruption risks in water service delivery in Kenya and Ghana. Water Policy.",
    doi="10.2166/wp.2018.017",
    publication_year="2018",
    country="Kenya; Ghana",
    subnational_unit="three case studies in Kenya, two in Ghana",
    legal_system="common law",
    urban_rural="both",
    service_provider="post-1990s-reform water utilities and regulatory bodies in Kenya and Ghana",
    regulatory_model="Case-study analysis (three Kenya, two Ghana) of corruption risks in water service delivery (WSD) after 1990s water-sector reforms, applying a principal-agent framework to analyze power distribution among actors at policy/regulatory, provision and consumption levels, documenting specific institutional corruption-risk mechanisms including regulatory-capture (ministerial appointment of regulator staff), political-opportunism (Municipal Council appointment of utility Board of Directors in Kenya), and state-capture (unmonitored service management contracts in Ghana)",
    population="water utility customers in Kenya and Ghana",
    sample_size="5 case studies (3 Kenya, 2 Ghana)",
    household_level="FALSE", community_level="TRUE",
    institutional_fragmentation="TRUE", enforcement="TRUE", discretion="TRUE", documentation="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_reliability="TRUE",
    effect_measure="qualitative case-study analysis with a principal-agent institutional framework",
    effect_estimate="Post-reform water-sector institutional structures in Kenya and Ghana created specific, documented corruption-risk pathways at each level of water service delivery: regulatory capture through ministerial appointment of regulatory-body staff; political opportunism through Municipal Councils' direct appointment of utility Boards of Directors in Kenya; and state capture through poorly monitored service-management contracts between national water agencies and contracted operators in Ghana; these institutional corruption risks coincided with persistently poor service outcomes, including non-revenue water frequently exceeding 50% and severe water rationing, illustrating how specific post-reform governance/appointment structures directly shape water-service-delivery performance and access reliability",
    study_design="qualitative case-study analysis (principal-agent institutional framework)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: multi-case-study analysis directly documenting specific post-reform institutional appointment/oversight structures and their corruption-risk implications for water-service-delivery performance across five case studies in two countries.",
    source_document="Bellaubi & Boehm 2018, Water Policy (retrieved via Google Drive)",
    section="Introduction; case-study analysis of Kenya and Ghana WSD levels",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established institutional-corruption/governance-mechanism inclusion precedent (referenced by S866 Mwihaki, Kenya): multi-case-study analysis directly documenting specific institutional appointment/oversight structures and corruption-risk mechanisms shaping water-service-delivery performance. NOT effect_sizes eligible: qualitative case-study analysis, no regression-based estimate. Extracted for record_id RB70B7542FFB9.",
    )

# S892 - Truelove - Negotiating states of water, Delhi
add("S892",
    citation="Truelove Y (2018). Negotiating states of water: Producing illegibility, bureaucratic arbitrariness, and distributive injustices in Delhi. Environment and Planning D: Society and Space.",
    doi="10.1177/0263775818759967",
    publication_year="2018",
    country="India",
    subnational_unit="Delhi",
    legal_system="common law",
    urban_rural="urban",
    service_provider="Delhi Jal Board and associated state water-measurement/administration agencies",
    regulatory_model="Ethnographic and documentary analysis of how Delhi's state water-supply agencies produce an 'appearance of legibility' in official water-access statistics (some of the highest claimed access levels in urban South Asia) through fragmented measurement and bureaucratic practices that build material ambiguity into the system, examining the political and material effects of this bureaucratic illegibility, including arbitrary water allocation across areas and the deliberate attribution of water wastage/loss to the populations and urban spaces most excluded from formal grid access",
    population="Delhi residents, particularly those in informal/excluded urban spaces",
    sample_size="ethnographic and documentary fieldwork",
    household_level="TRUE", community_level="TRUE",
    documentation="TRUE", discretion="TRUE", eligibility="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_quantity="TRUE",
    effect_measure="ethnographic and documentary institutional analysis",
    effect_estimate="Delhi's state water-supply administration maintains an appearance of high water-access legibility (official statistics claiming some of the highest access levels in urban South Asia) through deliberately fragmented measurement and bureaucratic practices that produce material ambiguity, which in turn produces both inadvertent arbitrary outcomes (unequal water allotment across areas) and deliberate ones (blame for water wastage/loss attributed to the very populations and urban spaces most excluded from formal grid access), demonstrating that bureaucratic knowledge-production/measurement practices themselves function as an institutional mechanism generating and masking distributive injustice in water access, disproportionately affecting populations already excluded from formal connections",
    study_design="ethnographic and documentary institutional analysis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: ethnographic and documentary analysis directly documenting how state bureaucratic measurement/knowledge-production practices function as an institutional mechanism producing arbitrary and unequal water-access outcomes.",
    source_document="Truelove 2018, Environment and Planning D (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established bureaucratic/institutional-mechanism inclusion precedent (S861 Das & Walton, Delhi Jal Board; S892 companion Delhi studies): ethnographic/documentary analysis directly documenting bureaucratic measurement practices as an institutional mechanism producing distributive water-access injustice. NOT effect_sizes eligible: ethnographic/documentary analysis, no regression-based estimate. Extracted for record_id RB709D82B9922.",
    )

# S893 - Jocoy - Who gets clean water, Pennsylvania
add("S893",
    citation="Jocoy CL (2000). Who gets clean water? Aid allocation to small water systems in Pennsylvania. Journal of the American Water Resources Association.",
    doi="10.1111/j.1752-1688.2000.tb04308.x",
    publication_year="2000",
    country="United States",
    subnational_unit="Pennsylvania",
    legal_system="common law",
    urban_rural="rural",
    service_provider="Pennsylvania Infrastructure Investment Authority (PENNVEST), the state's primary Safe Drinking Water Act-related financial assistance program for water-supply infrastructure",
    regulatory_model="Quantitative analysis (chi-square, Mann-Whitney U tests) of PENNVEST loan/grant application and award data (1988-1997, 509 construction-program applications, 384 unique water systems) linked to a state inventory of 2,331 community water systems, comparing the size distribution of PENNVEST applicants and award recipients to the overall population of Pennsylvania water systems to determine whether the state's primary infrastructure-financial-assistance program under the Safe Drinking Water Act systematically under-serves the smallest water systems",
    population="community water systems (CWS) in Pennsylvania, particularly very small systems serving 500 or fewer people",
    sample_size="384 unique water systems, 509 applications (1988-1997), sample of 241 PENNVEST projects analyzed; state inventory of 2,331 CWS",
    household_level="FALSE", community_level="TRUE",
    fees="TRUE", eligibility="TRUE", documentation="TRUE",
    formal_connection="TRUE", water_access="TRUE",
    effect_measure="chi-square and Mann-Whitney U statistical tests",
    effect_estimate="Very small water systems (serving 25-500 people) comprised 62% of all Pennsylvania community water systems but only 5% submitted a PENNVEST application between 1988-1997 (chi-square = 173.628, p<0.01); among applicants, very small systems had a lower funding success rate (59%) than small systems (79%) and the funded very small systems were themselves significantly larger on average than denied very small applicants (mean 271 vs. 166 population served, p=0.004, Mann-Whitney U), demonstrating that Pennsylvania's primary Safe Drinking Water Act infrastructure-financial-assistance program systematically under-serves the smallest, most capital-constrained water systems -- both in application rates and in funding success conditional on applying",
    study_design="quantitative statistical analysis of government aid-allocation administrative data",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: comprehensive administrative-data analysis (chi-square, Mann-Whitney U) directly documenting how a specific state financial-assistance program's allocation outcomes systematically disadvantage the smallest, most capital-constrained water systems by size.",
    source_document="Jocoy 2000, Journal of the American Water Resources Association (retrieved via Google Drive)",
    table="Tables 2, 3, 4 (application rates, funding success, size characteristics by system size)",
    section="Results",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: comprehensive statistical analysis of administrative data directly documenting how a specific state infrastructure-aid-allocation program systematically disadvantages the smallest water systems. NOT effect_sizes eligible: the tested exposure (water-system size category) is a physical/scale characteristic, not itself a documented legal/institutional mechanism in the Family A/B/C sense, even though the outcome (funding receipt from a specific government aid program) is institutional -- an exposure-side mismatch analogous to the S841/S853 precedent. Extracted for record_id RB6BFA3BE24E5.",
    )

# S894 - Anzera, Belotti, Bousselmi & Rabi - Hydropolitics, Palestine and Tunisia
add("S894",
    citation="Anzera G, Belotti F, Bousselmi L, Rabi A (2016). The hydropolitical challenges of domestic water conservation. Palestine and Tunisia case studies. International Review of Sociology.",
    doi="10.1080/03906701.2016.1155348",
    publication_year="2016",
    country="Palestine; Tunisia",
    subnational_unit="West Bank (Palestine); Tunisia (national)",
    legal_system="civil law (Tunisia); mixed/contested (Palestine, under the Oslo Interim Agreement water-allocation regime)",
    urban_rural="both",
    service_provider="Palestinian Hydrology Group (PHG) and CERTE (Tunisia), operating within a broader hydropolitical context in which Israel administers water allocation from the shared mountain aquifer via the Oslo Agreement (1995) Joint Water Committee (JWC)",
    regulatory_model="Original household survey (structured/semi-standardized 49-question questionnaire, EU SWMED project) documenting domestic water conditions, conservation practices, and socio-economic circumstances of families in Palestine and Tunisia, examined against the specific bilateral legal/institutional water-allocation mechanism established by the 1995 Oslo Agreement's Joint Water Committee (JWC), which the study documents Israel as often exceeding limits on without JWC approval, constraining Palestinian household water access",
    population="households in Palestine (West Bank) and Tunisia",
    sample_size="structured 49-question household survey (purposive sampling of key-informant householders)",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", eligibility="TRUE",
    water_access="TRUE", service_quantity="TRUE", service_quality="TRUE",
    effect_measure="original household survey with quantified consumption data",
    effect_estimate="In areas governed by the Oslo Agreement's Joint Water Committee allocation regime, water withdrawals by Israel from the shared mountain aquifer often exceed JWC-approved limits without approval, constraining the water available to Palestinian households; the household survey found per-capita water consumption in some Palestinian communities as low as 10-15 liters per capita per day (far below the WHO minimum), with half of surveyed households reporting drinking-water-quality problems, directly linking a specific bilateral legal/institutional water-allocation mechanism (the Oslo Agreement JWC framework) to severely constrained household water access and quality outcomes",
    study_design="original household survey with hydropolitical/institutional analysis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: original structured household survey data combined with documentary analysis of a specific bilateral legal/institutional water-allocation mechanism (the 1995 Oslo Agreement Joint Water Committee) directly linked to constrained Palestinian household water-access and quality outcomes.",
    source_document="Anzera, Belotti, Bousselmi & Rabi 2016, International Review of Sociology (retrieved via Google Drive)",
    section="Introduction; Mediterranean basin and 'tipping points'; survey methodology and results",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established bilateral water-allocation-treaty inclusion precedent: original household survey combined with documentary analysis of a specific bilateral legal/institutional water-allocation mechanism (Oslo Agreement JWC) directly linked to household-level water-access constraints. NOT effect_sizes eligible: descriptive household survey, no regression-based estimate isolating the mechanism. Extracted for record_id RB7D025C8BB6D.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
