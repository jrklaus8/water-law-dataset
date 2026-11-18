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

# S943 - Cobbing et al - O&M and perceived unreliability of domestic groundwater, South Africa
add("S943",
    citation="Cobbing JE, Eales K, Gibson J, Lenkoe K, Cobbing BL (2015). Operation and maintenance (O&M) and the perceived unreliability of domestic groundwater supplies in South Africa. South African Journal of Geology.",
    doi="10.2113/gssajg.118.1.17",
    publication_year="2015",
    country="South Africa",
    subnational_unit="Eastern Cape, Gauteng, Limpopo, North-West provinces; detailed case study of Mahikeng",
    legal_system="common law",
    urban_rural="rural",
    service_provider="local municipalities responsible for domestic groundwater supply operation and maintenance under South Africa's post-1994 water-services legal framework",
    regulatory_model="Two-year Water Research Commission-funded study combining interviews with hydrogeologists, technicians, planners, and managers at local-municipal level (Eastern Cape, Gauteng, Limpopo, North-West), municipal financial-flow data, and national hydrogeological/demographic datasets with a detailed case study of the town of Mahikeng, investigating why local authorities increasingly perceive groundwater as unreliable, finding that operation and maintenance (O&M) institutional capacity -- not primary/physical groundwater availability -- is the dominant driver of unreliable domestic groundwater supplies",
    population="rural and semi-rural South African communities in groundwater-dependent water-supply backlog areas",
    sample_size="multi-province interview study (4 provinces) plus detailed single-town case study (Mahikeng)",
    household_level="FALSE", community_level="TRUE",
    institutional_fragmentation="TRUE", bureaucratic_assistance="TRUE", political_coordination="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_reliability="TRUE",
    effect_measure="multi-province interview study with case-study triangulation",
    effect_estimate="Despite South Africa's domestic water-supply access rising from 61.1% (1996) to 95.2% (2013) nationally, groundwater-supply reliability -- particularly important in rural backlog areas where two-thirds of South Africans depend on groundwater -- was found to be undermined primarily by inadequate institutionalization of operation and maintenance (O&M) programs (staffing, budgeting, planning, monitoring, and inter-organizational collaboration), not by poor primary groundwater availability, as confirmed by the lack of correlation between water-supply backlog areas and low-yielding aquifers; the detailed Mahikeng case study (>90% groundwater dependent) showed that poor O&M, including failure to manage declining groundwater levels, degraded even a highly prolific aquifer resource, demonstrating that institutional/organizational capacity for water-supply management -- not physical resource constraints -- is the binding constraint on domestic water-supply reliability outcomes.",
    study_design="multi-province qualitative interview study with detailed single-town case-study triangulation",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: original multi-province interview study with case-study triangulation directly linking institutional/organizational O&M capacity (rather than physical resource availability) to domestic water-supply reliability outcomes.",
    source_document="Cobbing, Eales, Gibson, Lenkoe & Cobbing 2015, South African Journal of Geology (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established institutional-capacity inclusion precedent (Obeta Nigeria rural water, this same segment): original interview-based study directly linking institutional/organizational O&M capacity to water-supply reliability outcomes, distinguished from purely technical/hydrogeological studies by its institutional-capacity focus. NOT effect_sizes eligible: qualitative interview study, no regression-based estimate. Extracted for record_id R6B6565EFE1C9.",
    )

# S944 - Johnson et al - Racial Apartheid in a Small North Carolina Town
add("S944",
    citation="Johnson JH Jr, Parnell A, Joyner AM, Christman CJ, Marsh B (2004). Racial Apartheid in a Small North Carolina Town. Review of Black Political Economy.",
    doi="10.1007/s12114-004-1007-6",
    publication_year="2004",
    country="United States",
    subnational_unit="Mebane, North Carolina",
    legal_system="common law",
    urban_rural="rural",
    service_provider="Town of Mebane municipal government, using North Carolina's Extraterritorial Jurisdiction (ETJ) law, annexation authority, and Water Quality Critical Area zoning-overlay regulations to control sewer-service extension",
    regulatory_model="GIS-based case study combining Census 2000 demographic data, geo-coded public records (zoning, annexation, sewer-line locations) from state and local community-development agencies, participant observation, and content analysis of town council deliberations to document how Mebane officials used exclusionary zoning, extraterritorial jurisdiction (ETJ) manipulation, satellite annexation, and selective Water Quality Critical Area overlay application to systematically deny sewer service to three century-old African American neighborhoods while extending it to new, predominantly White developments",
    population="African American residents of three century-old Mebane neighborhoods (West End, White Level, Buckhorn/Perry Hill)",
    sample_size="single-town GIS-based case study with Census 2000 block-level data and geo-coded public-records analysis",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", indigenous_population="FALSE", zoning="TRUE", service_area="TRUE", discretion="TRUE", administrative_review="TRUE",
    formal_connection="TRUE", sanitation_access="TRUE",
    effect_measure="GIS-based spatial analysis of zoning, annexation, and sewer-infrastructure records against Census demographic data",
    effect_estimate="All three of Mebane's African American neighborhoods fall within the town's Extraterritorial Jurisdiction (ETJ) but none had been annexed as of the study period, denying residents political representation while subjecting them to town land-use control; sewer lines were extended to a newly built, predominantly White upscale development (The Club at Mill Creek) immediately adjacent to the historic White Level African American community, which remained unserved and reliant on failing septic systems (confirmed via EPA-funded water-quality sampling showing fecal-coliform, E. coli, and enterococci contamination exceeding EPA/state limits following rain events); repeated formal petitions for sewer-service extension by White Level residents (1997, in conjunction with an annexation request) were rejected, with the town citing a $720,000 cost estimate, while in the same council meeting the town approved $268,000 in financing for a lift station serving a newly annexed, predominantly White subdivision, demonstrating a directly documented pattern of institutionalized, race-differentiated denial of sanitation-infrastructure access through the town's zoning, annexation, and service-extension decision-making authority.",
    table="GIS-based figures mapping racial composition, ETJ boundaries, and sewer-line distribution",
    study_design="single-town GIS-based case study with Census data, geo-coded public records, participant observation, and content analysis of council deliberations",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: rigorous GIS-based spatial and documentary analysis directly linking specific municipal legal/institutional mechanisms (ETJ manipulation, selective annexation, zoning-overlay application, service-extension decisions) to race-differentiated sanitation-access denial for identified communities.",
    source_document="Johnson, Parnell, Joyner, Christman & Marsh 2004, Review of Black Political Economy (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established environmental-justice/discriminatory-infrastructure-denial inclusion precedent: rigorous GIS-based case study directly documenting how specific municipal legal/institutional mechanisms (ETJ, annexation, zoning) produced race-differentiated sanitation-access outcomes for identified communities. NOT effect_sizes eligible: GIS-based documentary case study, no regression-based estimate. Extracted for record_id R75F551BE4748.",
    )

# S945 - Bassi & Kabir - Sustainability Versus Local Management, rural water India
add("S945",
    citation="Bassi N, Kabir Y (2016). Sustainability Versus Local Management: Comparative Performance of Rural Water Supply Schemes. In Rural Water Systems for Multiple Uses and Livelihood Security, Elsevier.",
    doi="10.1016/B978-0-12-804132-1.00005-6",
    publication_year="2016",
    country="India",
    subnational_unit="six regions of Maharashtra state",
    legal_system="common law",
    urban_rural="rural",
    service_provider="individual (village-level) piped water supply schemes versus regional (multi-village) piped water supply schemes, under Maharashtra's rural water-supply institutional and decentralization reforms",
    regulatory_model="Comparative performance-assessment study of 12 rural water supply schemes (7 individual, 5 regional) across six regions of Maharashtra, using 850-household surveys across 17 villages plus interviews with local political leaders, civil society groups, state rural water supply bureaucracy officials, regulatory-agency officials, and user communities, to assess how policy reforms, techno-institutional characteristics (scheme type, decentralization, governance, community participation), and water-supply administration affect scheme managerial performance and water-supply adequacy, reliability, and quality",
    population="850 households across 17 villages in Maharashtra, India",
    sample_size="850 households, 17 villages, 12 rural water supply schemes",
    household_level="TRUE", community_level="TRUE",
    institutional_fragmentation="TRUE", participation="TRUE", political_coordination="TRUE", bureaucratic_assistance="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_reliability="TRUE", service_quality="TRUE",
    effect_measure="12-scheme comparative institutional performance assessment with household survey and stakeholder interviews",
    effect_estimate="Comparative performance assessment of individual (village-managed) versus regional (multi-village) piped water supply schemes in Maharashtra's hard-rock, groundwater-scarce geo-hydrological setting reveals that techno-institutional model choice -- not physical/geological constraints alone -- significantly determines scheme sustainability and household-level water-supply adequacy, reliability, and quality outcomes, with governance, decentralization, and community-participation characteristics identified as key differentiators between well-performing and poorly-performing schemes of the same physical type, informing policy recommendations on which techno-institutional model works best under water-scarce hard-rock conditions.",
    study_design="12-scheme comparative institutional performance assessment with 850-household survey and stakeholder interviews",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: original large-sample (850-household) comparative institutional performance study directly linking specific techno-institutional water-supply management models (individual vs. regional, degree of decentralization/community participation) to measured household water-access, reliability, and quality outcomes.",
    source_document="Bassi & Kabir 2016, Rural Water Systems for Multiple Uses and Livelihood Security, Elsevier (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established institutional-comparative-governance inclusion precedent (Lele et al south India, this same segment; Rama Mohan India): original large-sample comparative institutional study directly linking techno-institutional water-management models to measured household water-access and reliability outcomes. NOT effect_sizes eligible: comparative institutional performance assessment across 12 schemes, no regression-based estimate isolating a single mechanism with a formal comparator. Extracted for record_id R6A459D59A92A.",
    )

# S946 - Boex et al - Political Economy of Urban Governance in Asian Cities
add("S946",
    citation="Boex J, Malik AA, Brookins D, Edwards B, Zaidi H (2020). The Political Economy of Urban Governance in Asian Cities: Delivering Water, Sanitation and Solid Waste Management Services. In New Urban Agenda in Asia-Pacific, Springer.",
    doi="10.1007/978-981-13-6709-0_11",
    publication_year="2020",
    country="multiple (South and Southeast Asia)",
    subnational_unit="18 cities across 6 countries",
    legal_system="mixed (civil and common law jurisdictions)",
    urban_rural="urban",
    service_provider="urban local governments across 18 cities in 6 South and Southeast Asian countries, operating under varying intergovernmental institutional structures determining their authority and discretion over water, sanitation, and solid-waste-management service delivery",
    regulatory_model="Original assessment framework designed and applied to 18 cities across 6 countries in South and Southeast Asia, evaluating the functional, administrative, and political dimensions determining the quality and coverage of water, sanitation, and solid-waste-management services, examining how intergovernmental institutional structures constrain (or enable) urban local governments' authority and discretion to deliver these basic public services",
    population="urban residents of 18 cities across 6 South and Southeast Asian countries",
    sample_size="18-city comparative institutional assessment across 6 countries",
    household_level="FALSE", community_level="TRUE",
    legal_status="TRUE", institutional_fragmentation="TRUE", discretion="TRUE", political_coordination="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE", service_coverage="TRUE",
    effect_measure="18-city comparative institutional assessment framework",
    effect_estimate="Across 18 cities in 6 South and Southeast Asian countries, urban local governments are found to be systematically constrained in their legal authority and administrative discretion to deliver water, sanitation, and solid-waste-management services, with intergovernmental institutional structures -- the division of functional responsibilities, revenue authority, and political accountability between national, provincial/state, and municipal levels -- identified as the central determinant of service quality and coverage variation across cities; the authors conclude that reforming intergovernmental institutional structures to better match assigned responsibilities with the authority and resources needed to fulfill them is essential for realizing cities' potential to expand water/sanitation service coverage and meet SDG and New Urban Agenda targets.",
    study_design="18-city comparative institutional assessment framework across 6 countries",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: original comparative institutional assessment across 18 cities directly linking intergovernmental legal/institutional structures (authority and discretion allocation) to water/sanitation service-delivery quality and coverage outcomes.",
    source_document="Boex, Malik, Brookins, Edwards & Zaidi 2020, New Urban Agenda in Asia-Pacific, Springer (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established intergovernmental-institutional-structure inclusion precedent (Furlong Ontario; Saleth & Sastry Karnataka): original multi-city comparative institutional assessment directly linking intergovernmental legal/institutional authority structures to water/sanitation service-delivery outcomes across 18 cities. NOT effect_sizes eligible: comparative institutional assessment framework, no regression-based estimate. Extracted for record_id R69C019A0A542.",
    )

# S947 - Tadadjeu et al - natural resource dependence and access to water/sanitation, Africa
add("S947",
    citation="Tadadjeu S, Njangang H, Ningaye P, Nourou M (2020). Linking natural resource dependence and access to water and sanitation in African countries. Resources Policy.",
    doi="10.1016/j.resourpol.2020.101880",
    publication_year="2020",
    country="44 African countries",
    subnational_unit="national-level panel, urban and rural populations",
    legal_system="mixed (civil and common law jurisdictions across 44 countries)",
    urban_rural="both",
    service_provider="national governments across 44 African countries, with institutional/regulatory quality (regulation quality index) as a key governance moderator",
    regulatory_model="Two-step System Generalized Method of Moments (GMM) panel regression across 44 African countries (1995-2017) estimating the effect of total natural-resource rents (and disaggregated by resource type: oil, coal, gas, forest, mineral) on access to water and sanitation for total, urban, and rural populations and the urban-rural access gap, controlling for regulation quality, GDP per capita, trade openness, foreign direct investment, and urban population share, and separately testing whether democracy/governance quality moderates the natural-resource-access relationship",
    population="national populations of 44 African countries, 1995-2017",
    sample_size="unbalanced panel of 44 African countries, 570-741 country-year observations depending on specification",
    household_level="FALSE", community_level="TRUE",
    legal_status="TRUE", institutional_fragmentation="TRUE", enforcement="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE", service_coverage="TRUE",
    effect_measure="two-step System GMM panel regression",
    effect_estimate="Total natural-resource rents have a negative and statistically significant effect on access to water and sanitation, both for total population and separately for urban and rural populations, and a U-shaped relationship between resource rents and access is established; disaggregating by resource type shows oil, coal, and gas rents significantly reduce access to water and sanitation while forest rent (a diffuse, non-point resource) increases access; natural-resource dependence is also shown to widen the urban-rural access gap. Critically, regulation quality -- an institutional/governance-quality index -- has a positive and statistically significant direct effect on access to drinking water and sanitation (coefficient 0.0121, p<0.01, for total-population water access) and significantly reduces the urban-rural access gap (coefficient -0.0511, p<0.01), and separate analysis shows that democratic institutional quality mitigates the negative resource-curse effect of natural-resource dependence on water/sanitation access, indicating that stronger institutional/regulatory governance is an effective mechanism for offsetting the access-reducing effects of natural-resource dependence in Africa.",
    lower_CI="", upper_CI="", standard_error="0.00346 (regulation quality, water access total, Table 2 column 2)",
    p_value="<0.01 (regulation quality, water access total and urban-rural gap)",
    extraction_sample_size="570-741 country-year observations (43 countries)",
    adjusted_or_unadjusted="adjusted (GDP per capita, trade openness, FDI, urban population share, lagged dependent variable)",
    covariates="GDP per capita, trade openness, foreign direct investment, urban population share, lagged access rate",
    model_type="two-step System Generalized Method of Moments (GMM) dynamic panel regression",
    table="Table 2 (effects of total natural resource rent on access to water and sanitation, including regulation quality); Table 3 (effects by resource type)",
    study_design="44-country dynamic panel GMM regression, 1995-2017",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: rigorous dynamic panel GMM regression directly isolating the effect of institutional/regulatory governance quality on water/sanitation access and the urban-rural access gap across a large 44-country panel, controlling for confounders and addressing dynamic panel bias.",
    source_document="Tadadjeu, Njangang, Ningaye & Nourou 2020, Resources Policy (retrieved via Google Drive)",
    section="Section 4; Table 2",
    exact_location="Table 2",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md. Genuine Family C (institutional/legal barriers and access inequality) effect_sizes candidate -- see effect_sizes.csv addition this batch (regulation-quality institutional-governance effect on water/sanitation access and urban-rural gap). Extracted for record_id R7189977C3E95.",
    )

# S948 - Kujinga et al - household water security, Ngamiland Botswana
add("S948",
    citation="Kujinga K, Vanderpost C, Mmopelwa G, Wolski P (2013). An analysis of factors contributing to household water security problems and threats in different settlement categories of Ngamiland, Botswana. Physics and Chemistry of the Earth.",
    doi="10.1016/j.pce.2013.09.017",
    publication_year="2013",
    country="Botswana",
    subnational_unit="Ngamiland district, primary/secondary/tertiary/ungazetted settlement categories",
    legal_system="common law",
    urban_rural="both",
    service_provider="government water-supply institutions differentiated by formal settlement legal status (gazetted vs. ungazetted settlements) under Botswana's water-resources management and settlement-classification legal framework",
    regulatory_model="Mixed-methods study (household structured questionnaires, key informant interviews, observation, focus group discussions, informal interviews, literature review) analyzing factors contributing to household water security problems across different settlement categories (primary, secondary, tertiary, and ungazetted) in Ngamiland district, Botswana, examining how formal settlement legal/administrative status (gazetted vs. ungazetted), climatic/hydrological factors, and water-governance challenges jointly determine water security outcomes",
    population="households across primary, secondary, tertiary, and ungazetted settlements in Ngamiland district, Botswana",
    sample_size="mixed-methods household survey, key informant interviews, observation, and focus group discussions across multiple settlement categories",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", institutional_fragmentation="TRUE", discretion="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_reliability="TRUE",
    effect_measure="mixed-methods comparative analysis across settlement legal-status categories",
    effect_estimate="Water security across all settlement categories in Ngamiland is significantly affected by the settlement's formal legal/administrative status -- gazetted versus ungazetted -- alongside climatic/hydrological factors and water-governance challenges; large villages (e.g., Maun) face water-security threats from population growth, urbanization, management challenges, and aging infrastructure, while ungazetted settlements -- lacking formal government recognition and the associated planning/infrastructure-investment mandate -- face the most severe access constraints and need better access to clean water, demonstrating that formal settlement legal status is a key institutional determinant of differential household water-security outcomes across settlement categories, requiring a settlement-category-specific water-resources management strategy.",
    study_design="mixed-methods comparative study across settlement legal-status categories (household surveys, interviews, focus groups)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: original mixed-methods study directly linking a specific legal/administrative status distinction (gazetted vs. ungazetted settlement recognition) to differentiated household water-security and access outcomes across settlement categories.",
    source_document="Kujinga, Vanderpost, Mmopelwa & Wolski 2013, Physics and Chemistry of the Earth (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established settlement-legal-recognition inclusion precedent (Wahby Cairo; Hossain Dhaka bosti; Parsa Dar es Salaam-type formalization studies): original mixed-methods study directly linking formal settlement legal-status recognition (gazetted vs. ungazetted) to differentiated household water-security outcomes. NOT effect_sizes eligible: mixed-methods comparative study across settlement categories, no regression-based estimate. Extracted for record_id R6F22E1AE923A.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
