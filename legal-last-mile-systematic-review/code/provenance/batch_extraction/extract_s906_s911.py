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

# S906 - Nizkorodov - Southern California water PPP risk allocation
add("S906",
    citation="Nizkorodov E (2021). Evaluating risk allocation and project impacts of sustainability-oriented water public-private partnerships in Southern California: A comparative case analysis. World Development.",
    doi="10.1016/j.worlddev.2020.105232",
    publication_year="2021",
    country="United States",
    subnational_unit="Southern California",
    legal_system="common law",
    urban_rural="urban",
    service_provider="10 water public-private partnerships (PPPs) across Southern California water utilities",
    regulatory_model="Exploratory qualitative comparative case study (interviews, observations, shadowing, document analysis) of 10 sustainability-oriented water public-private partnerships (PPPs) in Southern California, examining risk allocation between public and private partners under PPP contract structures and the economic, political, environmental and social distributional impacts of these partnership arrangements, with particular attention to how contract structure, permitting processes and regulatory evolution shape outcomes for ratepayers and marginalized low-income populations",
    population="Southern California water utility ratepayers, particularly low-income populations",
    sample_size="10 public-private partnership case studies (interviews, observations, shadowing, document analysis)",
    household_level="FALSE", community_level="TRUE",
    legal_status="TRUE", fees="TRUE", institutional_fragmentation="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE", service_quality="TRUE",
    effect_measure="comparative qualitative case-study analysis with distributional-impact assessment",
    effect_estimate="Sustainability-oriented water PPPs in Southern California can produce environmentally beneficial outcomes (resource diversification, improved utility efficiency) when carefully managed, but face a structural tension between private-partner profitability and public welfare that a complex permitting process and evolving regulations exacerbate through cost overruns and project delays; risks to the public partner and ratepayers -- including the potential for reduced service quality and marginalization of low-income populations documented in prior studies -- can be reduced through mutual agreement of project goals, robust contract structure, and inclusion of end-users and affected stakeholders in project design, demonstrating that specific legal/contractual risk-allocation design directly shapes distributional outcomes of water PPP arrangements.",
    study_design="comparative qualitative case study (10 PPPs)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: comparative qualitative case-study analysis directly documenting how PPP contract/risk-allocation design shapes distributional water-service outcomes across 10 partnerships.",
    source_document="Nizkorodov 2021, World Development (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established PPP-contract/risk-allocation inclusion precedent: comparative qualitative case study directly documenting how PPP contract design shapes distributional water-service outcomes. NOT effect_sizes eligible: qualitative comparative case study, no regression-based estimate. Extracted for record_id RA6A6B0425E70.",
    )

# S907 - Saleth & Sastry - Karnataka water/sanitation sector
add("S907",
    citation="Saleth RM, Sastry GS (2004). Water supply and sanitation sector of Karnataka, India: status, performance and change. Water Policy.",
    doi="10.2166/wp.2004.0011",
    publication_year="2004",
    country="India",
    subnational_unit="Karnataka",
    legal_system="common law",
    urban_rural="both",
    service_provider="Karnataka state government water supply and sanitation sector institutions",
    regulatory_model="Documentary and financial-policy analysis (1990-2001 data) of Karnataka's water supply and sanitation sector, assessing state budgetary subsidy dynamics, cost-recovery performance, and institutional reform strategies against the backdrop of specific coverage-criteria policy changes (distance-to-source standard reduced from 1.6km to 1.0km; consumption-target increase to 70 lpcd for piped schemes), evaluating recent institutional reform initiatives and their implications for closing the state's unmet water/sanitation access backlog",
    population="Karnataka state residents, urban and rural",
    sample_size="state-level administrative/financial data, 1990-2001",
    household_level="FALSE", community_level="TRUE",
    legal_status="TRUE", fees="TRUE", eligibility="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE",
    effect_measure="documentary/financial policy analysis with quantified coverage and subsidy data",
    effect_estimate="Karnataka's state government policy decisions -- a four-fold budget increase for rural water supply, revised coverage-criteria standards (distance and elevation thresholds), and an increased per-capita consumption target for piped schemes -- directly enabled the state to become one of the first in India to provide at least one safe drinking water source for all villages by 1991, achieving above-national-average service levels; however, about 25% of the population (mostly rural) still lacked adequate safe drinking water access and 75% of the rural population lacked sanitary latrine access as of the study period, with growing budgetary subsidy dependence and inadequate cost recovery threatening the sector's financial sustainability and future investment capacity, demonstrating how specific state institutional/financial policy decisions directly shape water/sanitation access outcomes and their sustainability.",
    table="Table 3 (rising domestic water needs by district, urban/rural, 1991-2001)",
    study_design="documentary/financial policy analysis of state administrative data",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: documentary/financial analysis directly linking specific state institutional policy decisions (coverage-criteria changes, budget allocation, subsidy dynamics) to quantified water/sanitation access-coverage outcomes.",
    source_document="Saleth & Sastry 2004, Water Policy (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established government financial/institutional-policy inclusion precedent (Larrain Chile, Jocoy PENNVEST): documentary/financial analysis directly linking specific state policy decisions to quantified water/sanitation access-coverage outcomes. NOT effect_sizes eligible: descriptive documentary/financial-policy analysis, no regression-based estimate isolating the mechanism. Extracted for record_id R9E1C92EFDCBB.",
    )

# S908 - Alzahrani - Three Essays on Water Economics
add("S908",
    citation="Alzahrani F (2019). Three Essays on Water Economics. PhD Dissertation, West Virginia University.",
    doi="",
    publication_year="2019",
    country="United States",
    subnational_unit="48 contiguous states (Essay 1); Marion County, West Virginia (Essay 2); statewide, West Virginia (Essay 3)",
    legal_system="common law",
    urban_rural="both",
    service_provider="public water systems regulated under the federal Safe Drinking Water Act; public service districts (PSDs), West Virginia",
    regulatory_model="Three-essay econometric dissertation: (1) spatial and non-spatial panel regression (2000-2011, 48 states) of Safe Drinking Water Act (SDWA) health-based-standard violations (population exposed) on per-capita health care expenditures; (2) spatial and non-spatial hedonic property-price regression (1,985 housing transactions, 2012-2017, Marion County WV) of boil-water-notice (BWN) episodes on residential property values; (3) regression analysis (110 public service districts, West Virginia) of raw-water-source type -- including the effect of West Virginia's Source Water Protection Act (Senate Bill 373, 2014) encouraging multiple water sources -- on residential water charges",
    population="US public water system service populations (Essay 1); Marion County, WV homeowners (Essay 2); West Virginia public service district ratepayers (Essay 3)",
    sample_size="48-state panel 2000-2011 (Essay 1); 1,985 housing transactions/350 BWNs (Essay 2); 110 public service districts (Essay 3)",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", enforcement="TRUE", eligibility="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE", service_reliability="TRUE",
    effect_measure="Spatial Durbin Model regression (Essay 1); hedonic and quantile regression (Essay 2); OLS regression (Essay 3)",
    effect_estimate="Essay 1: a 1% decrease in the population exposed to SDWA health-based-standard violations is associated with reductions of 0.005% ($0.32) in-state and 0.035% ($2.26) regional per-capita health care expenditures (Spatial Durbin Model). Essay 2: boil-water notices in the year prior to a home sale significantly depreciate housing prices by 0.57%-18% depending on measurement, with larger impacts on low-price homes (quantile regression: $2,100-$2,700 increase in value at the lower price quantile per one-day BWN reduction, versus no significant effect at the 0.7+ quantile); aggregate marginal willingness to pay for a one-day BWN reduction equals $4.60 million. Essay 3: public service districts using multiple raw-water sources -- as encouraged by West Virginia's Source Water Protection Act (Senate Bill 373, 2014) -- have residential water charges approximately 29% higher than single-source PSDs, indicating that this specific legislative policy mechanism, while protecting source-water resilience, carries a quantified affordability tradeoff for ratepayers.",
    table="Essay 3 regression results (110 PSDs, raw-water-source type and residential water-charge determinants)",
    study_design="three-essay econometric dissertation (spatial panel regression; hedonic/quantile regression; OLS regression)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: dissertation-level econometric analysis directly linking specific federal (SDWA enforcement) and state (Source Water Protection Act) legal/institutional mechanisms to quantified water-affordability, water-reliability and health-expenditure outcomes via regression models with substantial sample sizes.",
    source_document="Alzahrani 2019, West Virginia University Research Repository (retrieved via Google Drive)",
    section="Abstract; Essays 1-3",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md. Essay 3's regression of residential water charges on raw-water-source type, explicitly linked to West Virginia's Source Water Protection Act (Senate Bill 373, 2014) as the institutional mechanism, IS effect_sizes eligible under Family A/B (a real statute directly regressed against a water-affordability outcome) -- see effect_sizes.csv addition this batch. Essays 1-2 (SDWA violations/health expenditure; BWN/property values) are documented here but not separately added to effect_sizes, as their outcomes (health expenditure, property value) fall outside the project's water-access outcome family even though their exposures are institutional/regulatory. Extracted for record_id RA2C6963F84B8.",
    )

# S909 - Adams, Braune, Cobbing, Fourie & Riemann - South Africa groundwater 20yr
add("S909",
    citation="Adams S, Braune E, Cobbing J, Fourie F, Riemann K (2015). Critical reflections on 20 years of groundwater research, development and implementation in South Africa. South African Journal of Geology.",
    doi="10.2113/gssajg.118.1.5",
    publication_year="2015",
    country="South Africa",
    subnational_unit="national",
    legal_system="common law",
    urban_rural="both",
    service_provider="national Department of Water and Sanitation (formerly Department of Water Affairs and Forestry); municipal groundwater-scheme administrations",
    regulatory_model="Documentary policy assessment applying a groundwater-governance framework (policy level, national institutions/instruments, local-level institutions and actions) to trace 20 years (1994-2014) of South African groundwater resource governance following the country's democratic transition, documenting the National Water Act 1998's reclassification of groundwater's legal status from private property ('private water') to a public 'significant resource' integral to integrated water resource management, and connecting this legal reform plus post-1994 infrastructure investment to national water-access coverage outcomes",
    population="South African population, particularly historically unserved communities reliant on groundwater",
    sample_size="national policy/institutional documentary analysis, 1994-2014",
    household_level="FALSE", community_level="TRUE",
    legal_status="TRUE", institutional_fragmentation="TRUE",
    formal_connection="TRUE", water_access="TRUE",
    effect_measure="documentary policy/governance-framework analysis with quantified national coverage data",
    effect_estimate="Following South Africa's 1994 democratic transition and the National Water Act 1998's reclassification of groundwater from private property to a public significant resource under integrated water resource management, basic water infrastructure coverage rose to more than 95% of the population within two decades, providing access to an improved water supply to approximately 27 million people, with groundwater becoming the primary water source for between 50% and 90% of previously unserved communities depending on province; the paper identifies that while national-level policy and institutional development advanced substantially, the transfer of thousands of groundwater schemes from national/community management to newly established municipal administrations post-1994 created urgent, still-unmet local-level institutional-capacity challenges, demonstrating that a specific legal reclassification and governance framework directly enabled major national water-access gains while also generating new sub-national institutional-fragmentation risks.",
    study_design="documentary policy/governance-framework analysis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: documentary policy analysis directly linking a specific national legal reform (National Water Act 1998 groundwater reclassification) to quantified 20-year national water-access coverage outcomes.",
    source_document="Adams, Braune, Cobbing, Fourie & Riemann 2015, South African Journal of Geology (retrieved via Google Drive)",
    section="Introduction; Governance as an organising framework",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established national-legal-reform/water-access-coverage inclusion precedent (Larrain Chile): documentary analysis directly linking a specific legal reclassification (National Water Act 1998) to quantified national water-access coverage outcomes. NOT effect_sizes eligible: descriptive documentary/policy analysis, no regression-based estimate isolating the mechanism. Extracted for record_id R9ACCC3D2E6C2.",
    )

# S910 - Kundu - JnNURM urban development programmes critique
add("S910",
    citation="Kundu D (2014). Urban Development Programmes in India: A Critique of JnNURM. Social Change.",
    doi="10.1177/0049085714548546",
    publication_year="2014",
    country="India",
    subnational_unit="65 mission cities and non-mission towns, nationwide",
    legal_system="common law",
    urban_rural="urban",
    service_provider="Jawaharlal Nehru National Urban Renewal Mission (JnNURM), a national reform-linked infrastructure-investment program tied to the 74th Constitutional Amendment Act (1992) urban local body governance reforms",
    regulatory_model="Documentary and statistical analysis of JnNURM (2005-2014), India's largest national urban-infrastructure-investment program, examining sector-wise and city-size-class distribution of program funding (with water supply and sewerage the largest funded sectors, 37-63% of released funds) against 74th CAA-linked mandatory governance-reform compliance, quantifying systematic coverage disparities by city size (76% of class-I-city population covered versus 14-21% in smaller size classes) and identifying a persistent 'big city bias' in fund allocation",
    population="urban India residents across 5,161 towns/cities (2001 Census), disaggregated by city-size class",
    sample_size="national administrative program data, JnNURM funds released 2005-2014",
    household_level="FALSE", community_level="TRUE",
    legal_status="TRUE", eligibility="TRUE", institutional_fragmentation="TRUE",
    formal_connection="TRUE", water_access="TRUE",
    effect_measure="documentary/statistical program-allocation analysis with quantified coverage disparities",
    effect_estimate="Under JnNURM's reform-linked infrastructure-investment legal framework, water supply and sewerage together attracted 60% of funds released in mission cities and 76% in non-mission cities (the largest sectoral shares), but program coverage systematically favored larger cities: 76% of class-I-city population was covered by JnNURM investment versus only 21% in class-II cities and 14-18% in classes III-VI, with only 58% of urban India's population reached overall by 2009 and 4,207 of 5,161 towns/cities (2001 Census) never covered, demonstrating that this specific national government infrastructure-aid-allocation legal/institutional mechanism produced a persistent, quantified 'big city bias' systematically disadvantaging smaller towns' access to water-supply infrastructure investment.",
    table="Tables 4-8 (sector-wise fund distribution, city-size-class coverage disparities, state-wise completion rates)",
    study_design="documentary/statistical program-allocation analysis of national administrative data",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: documentary/statistical analysis directly linking a specific national infrastructure-aid-allocation legal/institutional program to quantified, systematic city-size-based coverage disparities in water-supply investment, consistent with the established Jocoy PENNVEST aid-allocation precedent.",
    source_document="Kundu 2014, Social Change (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established government infrastructure-aid-allocation-program inclusion precedent (Jocoy S893, Batch 177): documentary/statistical analysis directly linking a specific national program's institutional design to quantified inequitable water-supply-investment distribution. Distinguished from the same author's excluded 'Urban poverty in India' piece (Batch 177, E01) by this paper's dedicated focus on a specific infrastructure-funding program with water as the dominant, separately-quantified sector rather than water as one of several minor 'basic amenities' in a general poverty analysis. NOT effect_sizes eligible: descriptive documentary/statistical program analysis, no regression-based estimate isolating the mechanism. Extracted for record_id R999C3CB53A0C.",
    )

# S911 - Hazarika & Nitivattananon - Guwahati groundwater rights DPSIR
add("S911",
    citation="Hazarika N, Nitivattananon V (2016). Strategic assessment of groundwater resource exploitation using DPSIR framework in Guwahati city, India. Environmental Science & Policy.",
    doi="10.1016/j.envsci.2015.10.012",
    publication_year="2016",
    country="India",
    subnational_unit="Guwahati, Assam",
    legal_system="common law",
    urban_rural="urban",
    service_provider="Guwahati Municipal Corporation, Assam Urban Water Supply and Sewerage Board, Public Health Engineering department; informal groundwater self-supply (tube wells, ring wells, bore wells)",
    regulatory_model="Household survey (n=150) and DPSIR (Driver-Pressure-State-Impact-Response) framework analysis of groundwater exploitation in Guwahati, examining how the legal linkage of groundwater rights to land rights (i.e., the absence of independent groundwater regulation, treating groundwater as a landowner's common-pool entitlement) combines with formal water-supply coverage of only 27% of the city's population to drive over-extraction and declining household water accessibility among the 69% of the population relying on unregulated groundwater self-supply",
    population="Guwahati urban households, particularly the 69% relying on groundwater self-supply outside the formal 27%-coverage piped network",
    sample_size="150 household questionnaire survey plus official/literature records",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", eligibility="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE",
    effect_measure="household survey with DPSIR institutional-driver framework analysis",
    effect_estimate="In Guwahati, groundwater rights are legally tied to land rights with no independent regulatory mechanism (groundwater treated as an unregulated common-pool resource for individual landowners), and this institutional gap -- combined with formal piped water-supply coverage of only 27% of the city's over-one-million population -- has driven groundwater extraction (79 million liters/day) beyond safe yield levels; the household survey found this institutional/legal vacuum has produced increasing water-accessibility problems among households reliant on groundwater self-supply, including declining water tables, rising water-affordability concerns, and the emergence of a distinct 'water poor' population segment, demonstrating that the specific legal linkage of groundwater rights to land rights, absent independent regulation, is a direct institutional driver of deteriorating household water access.",
    study_design="household survey with DPSIR institutional-framework analysis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: original 150-household survey combined with a structured institutional-driver framework directly linking a specific legal gap (groundwater rights tied to land rights, absent independent regulation) to household water-accessibility outcomes.",
    source_document="Hazarika & Nitivattananon 2016, Environmental Science & Policy (retrieved via Google Drive)",
    section="Abstract; Introduction",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: original household survey with DPSIR institutional-framework analysis directly linking a specific legal gap (groundwater/land rights linkage, absent independent regulation) to household water-access outcomes, distinguished from the excluded Salmoral et al. Arequipa nexus-governance paper (this batch, E01) by its explicit household-level survey data and specific legal-mechanism framing rather than broad multi-sector resource-governance stakeholder mapping. NOT effect_sizes eligible: household survey with descriptive DPSIR framework, no regression-based estimate isolating the mechanism. Extracted for record_id R9926E6BB7498.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
