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

# S938 - Bontianti, Hungerford, Younsa & Noma - Niamey Niger fluid experiences
add("S938",
    citation="Bontianti A, Hungerford H, Younsa HH, Noma A (2014). Fluid experiences: Comparing local adaptations to water inaccessibility in two disadvantaged neighborhoods in Niamey, Niger. Habitat International.",
    doi="10.1016/j.habitatint.2014.04.001",
    publication_year="2014",
    country="Niger",
    subnational_unit="two disadvantaged neighborhoods, Niamey",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="public-private partnership water utility (since 2001) alongside informal water vendors filling access gaps in disadvantaged neighborhoods",
    regulatory_model="Small-scale, neighborhood-level comparative qualitative study examining why Niger's 2001 public-private partnership water-sector reform (aimed at increasing supply rates and financial self-sufficiency) has not translated into increased water access for residents in two disadvantaged Niamey neighborhoods, showing that location, tenure status, and settlement age are poor predictors of piped-water access despite continuing to guide normative urban water policy, and that informal water vendors fill institutional gaps in locally-responsive ways that normative policy models fail to accommodate",
    population="residents of two disadvantaged neighborhoods in Niamey, Niger",
    sample_size="neighborhood-scale comparative qualitative fieldwork",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", tenure_status="TRUE", institutional_fragmentation="TRUE", discretion="TRUE",
    formal_connection="TRUE", water_access="TRUE",
    effect_measure="neighborhood-scale comparative qualitative fieldwork analysis",
    effect_estimate="Despite Niger's 2001 institutional reform introducing a public-private partnership for urban water services (which achieved financial self-sufficiency within five years but failed to meet its water-access-expansion goal for poor neighborhoods), water access in Niamey's disadvantaged neighborhoods remains highly variable and poorly explained by standard predictors (location, tenure status, settlement age); the rigidity of institutional reforms and normative policy models fails to accommodate local geographic and household contexts, with informal water vendors emerging to fill the resulting service gaps in ways that formal policy has not been able to replicate, demonstrating that a nationally uniform institutional reform can produce starkly unequal neighborhood-level water-access outcomes even among similarly disadvantaged communities.",
    study_design="neighborhood-scale comparative qualitative case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: original comparative fieldwork directly documenting how a specific national public-private-partnership institutional reform produced highly variable, locally-contingent household water-access outcomes across two similarly disadvantaged neighborhoods.",
    source_document="Bontianti, Hungerford, Younsa & Noma 2014, Habitat International (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established institutional-reform/neighborhood-scale inclusion precedent (Wahby Cairo; Hossain Dhaka bosti): original comparative fieldwork directly documenting how a specific national PPP institutional reform produced variable household water-access outcomes at the neighborhood scale. NOT effect_sizes eligible: qualitative comparative case study, no regression-based estimate. Extracted for record_id R706085F2592E.",
    )

# S939 - Pierce & Gonzalez - California mobile home parks water access
add("S939",
    citation="Pierce G, Gonzalez SR (2017). Public Drinking Water System Coverage and Its Discontents: The Prevalence and Severity of Water Access Problems in California's Mobile Home Parks. Environmental Justice.",
    doi="10.1089/env.2017.0006",
    publication_year="2017",
    country="United States",
    subnational_unit="California (statewide, mobile home park water systems)",
    legal_system="common law",
    urban_rural="both",
    service_provider="publicly-regulated community water systems operated by private mobile-home-park (MHP) owners/operators, under California's 2012 legislated Human Right to Water (AB 685) and AB 1830 (CPUC complaint mechanism for MHP water-service overcharging/quality)",
    regulatory_model="Mixed-methods study combining content analysis of 1,300+ California newspaper stories (2000-2015) with administrative data (State Water Resource Control Board SDWIS database, American Community Survey, American Housing Survey) to evaluate drinking-water quality, reliability, and affordability in mobile home park (MHP) water systems against the three dimensions stated in California's legislated Human Right to Water, comparing MHP systems to other public water systems statewide",
    population="California mobile home park residents (about 75% of the state's mobile-home population, itself about 4% of housing stock)",
    sample_size="1,300+ news stories (2000-2015); 383 of 2,976 statewide public water systems identified as MHP systems (August 2016); AHS n=542 California MHP respondents",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", complaint="TRUE", administrative_review="TRUE", institutional_fragmentation="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_reliability="TRUE", service_quality="TRUE", affordability="TRUE",
    effect_measure="mixed-methods content analysis and administrative-data comparison",
    effect_estimate="Despite California's 2012 legislated Human Right to Water, mobile home park (MHP) water systems -- representing 13% of all state public water systems despite housing only 3% of the state population -- experience substantially worse service on all three legislated dimensions: MHP systems are more likely to incur health-related (MCL) violations (one-third of MHP systems vs. one-fourth of other systems) and incur more violations on average (5.85 vs. 5.22); MHP residents are four times more likely to experience a significant water-service shutoff (13% vs. under 4% of the general population) and MHP systems are 40% more likely to rely exclusively on groundwater (96% vs. two-thirds of other systems), a known reliability risk factor; affordability evidence, drawn from content analysis and CPUC complaint-mechanism records (AB 1830), is less conclusive but indicates an outsized burden for at least some MHP residents, who often face unaffordable per-unit connection fees when seeking to switch to municipal water supply.",
    table="Table 1 (data sources and analytical dimensions)",
    study_design="mixed-methods content analysis and statewide administrative-data comparison",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: original mixed-methods analysis directly evaluating household water-access outcomes for a specific institutionally-regulated population (MHP residents) against a specific state legal framework (California's legislated Human Right to Water and its CPUC complaint mechanism).",
    source_document="Pierce & Gonzalez 2017, Environmental Justice (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established constitutional/statutory-rights-framework inclusion precedent (Allison Cape Town; Espinoza & Viers California SGMA, S037): original mixed-methods study directly evaluating a marginalized population's household water-access outcomes against a specific legislated water-rights framework. NOT effect_sizes eligible: mixed-methods content analysis and descriptive administrative-data comparison, no regression-based estimate isolating a single institutional mechanism. Extracted for record_id R700E3084D85D.",
    )

# S940 - Muchadenyika - Harare Zimbabwe slum upgrading inclusive governance
add("S940",
    citation="Muchadenyika D (2015). Slum upgrading and inclusive municipal governance in Harare, Zimbabwe: New perspectives for the urban poor. Habitat International.",
    doi="10.1016/j.habitatint.2015.03.010",
    publication_year="2015",
    country="Zimbabwe",
    subnational_unit="Harare (capital city)",
    legal_system="common law",
    urban_rural="urban",
    service_provider="City of Harare municipal government, engaging urban-poor community alliances through the Harare Slum Upgrading Programme's incremental-development institutional structure, following the 2005 Operation Restore Order mass-eviction campaign",
    regulatory_model="Case-study institutional analysis of the Harare Slum Upgrading Programme, documenting how participatory urban planning, a new slum-upgrading institutional structure, and community profiling/enumeration are producing gradual institutional change in municipal governance culture -- shifting from a history of evictions toward incremental development that allows the urban poor to settle on land first and access municipal services (water, sanitation, tenure security, roads) gradually over time",
    population="urban poor residents of Harare informal settlements",
    sample_size="single-city institutional/policy case study of the Harare Slum Upgrading Programme",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", tenure="TRUE", planning="TRUE", participation="TRUE", institutional_fragmentation="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE",
    effect_measure="case-study institutional/policy analysis",
    effect_estimate="Following a decade in which Operation Restore Order (2005) left over 700,000 people homeless, the Harare Slum Upgrading Programme is producing gradual institutional change in municipal governance -- allowing urban-poor residents to settle on land first and access municipal water, sanitation, tenure security, and road services incrementally over time, rather than requiring full formal compliance before any service access -- driven by both a changing City of Harare governance culture (gradual 'opening up' to the urban poor) and a strengthened, vibrant urban-poor community alliance acting as a medium of participation in city governance, demonstrating that incremental, institutionally-negotiated legal/regulatory pathways can expand basic-service access for informal settlers even absent immediate full land-tenure formalization.",
    study_design="single-city institutional/policy case-study analysis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: case-study institutional analysis directly documenting how a specific municipal slum-upgrading institutional structure and incremental-development legal/regulatory approach produces household water/sanitation access gains for previously excluded informal settlers.",
    source_document="Muchadenyika 2015, Habitat International (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established informal-settlement/institutional-inclusion inclusion precedent (Wahby Cairo; Hossain Dhaka bosti; Avidar Kenya devolution): case-study institutional analysis directly documenting how a specific municipal governance/legal mechanism produces incremental household water/sanitation access gains for informal settlers. NOT effect_sizes eligible: qualitative case-study institutional analysis, no regression-based estimate. Extracted for record_id R6DB58AA8E6EA.",
    )

# S941 - Gutierrez - Malawi/Zambia pro-poor water/sanitation delivery
add("S941",
    citation="Gutierrez E (2007). Delivering pro-poor water and sanitation services: The technical and political challenges in Malawi and Zambia. Geoforum.",
    doi="10.1016/j.geoforum.2005.09.010",
    publication_year="2007",
    country="Malawi; Zambia",
    subnational_unit="nationwide (national Poverty Reduction Strategy Papers)",
    legal_system="common law",
    urban_rural="both",
    service_provider="national government water/sanitation sector agencies and donor coordination bodies, operating under Malawi's and Zambia's respective Poverty Reduction Strategy Papers (PRSPs, the key national policy/funding frameworks submitted to the World Bank/IMF)",
    regulatory_model="Documentary/institutional field-note analysis examining the technical and political challenges undermining implementation of the Millennium Development Goal water/sanitation targets within Malawi's and Zambia's national Poverty Reduction Strategy Papers, documenting how water and sanitation were under-prioritized late additions to both PRSPs (not structured as consultation priorities, absent from core expenditure prioritization), and analyzing weak state institutional support, unreliable/contested coverage indicators, poor inter-sectoral coordination, and fragmented donor efforts as the primary institutional barriers to translating PRSP legal/policy commitments into actual water-access outcomes",
    population="rural and urban poor populations of Malawi and Zambia",
    sample_size="two-country documentary/institutional policy analysis with budget and PRSP-text review",
    household_level="FALSE", community_level="TRUE",
    legal_status="TRUE", institutional_fragmentation="TRUE", political_coordination="TRUE", documentation="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE",
    effect_measure="documentary/institutional policy analysis with budget and PRSP-text review",
    effect_estimate="In both Malawi and Zambia, water and sanitation were recognized only as late, under-prioritized additions within the national Poverty Reduction Strategy Papers (PRSPs) that govern World Bank/IMF-linked funding and policy -- in Zambia's 2001 provincial consultations water/sanitation was not structured as a discussion priority, and in Malawi's 2000 Interim PRSP it was subsumed as a mere component of health-services provision -- despite studies showing that poor people themselves identified water supply as their most important problem; this institutional under-prioritization, combined with weak state support, unreliable and contested coverage indicators, poor inter-sectoral coordination, and fragmented donor aid efforts, is identified as the central reason why substantial PRSP legal/policy commitments to water and sanitation have not translated into meaningful improvements in water-access outcomes toward the MDG target in either country.",
    study_design="two-country documentary/institutional policy analysis (field note)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="Moderate: documentary/institutional policy analysis (PRSP text and budget-allocation review) directly linking specific national poverty-reduction legal/policy frameworks' institutional under-prioritization to water/sanitation-access shortfalls in two countries, though presented as a preliminary field note rather than a fully systematic empirical study.",
    source_document="Gutierrez 2007, Geoforum (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established national policy-framework/institutional-analysis inclusion precedent (Guidi Gutierrez Sucre, Rama Mohan India, this same segment): documentary/institutional analysis directly linking a specific national poverty-reduction legal/policy framework's institutional gaps to water/sanitation-access outcomes, supported by budget and policy-text documentation despite the author's self-description as a preliminary 'field note'. NOT effect_sizes eligible: documentary/institutional policy analysis, no regression-based estimate. Extracted for record_id R6C0CBAFA3F7A.",
    )

# S942 - Lele et al - south Indian small towns institutional water governance
add("S942",
    citation="Lele S, Madhyastha K, Sulagna S, Dhavamani R, Srinivasan V (2018). Match, don't mix: implications of institutional and technical service modalities for water governance outcomes in south Indian small towns. Water Policy.",
    doi="10.2166/wp.2018.019",
    publication_year="2018",
    country="India",
    subnational_unit="four small towns across Karnataka and Tamil Nadu states",
    legal_system="common law",
    urban_rural="urban",
    service_provider="a spectrum of institutional arrangements from fully municipal management to combined municipal-parastatal management to complete para-statal management, deploying groundwater-only or mixed ground-and-surface-water resources",
    regulatory_model="Inductive comparative analysis of water service delivery and governance across four small towns in southern India, using a water-governance framework (adequacy/affordability, equity, sustainability, responsiveness) and expanding the 'service modality' concept to include both institutional arrangements and water-resource deployment; data gathered via household surveys, water metering, administrative records, and interviews to compare governance outcomes across different institutional-technical combinations",
    population="households in four small towns in Karnataka and Tamil Nadu, India",
    sample_size="four-town comparative study with household surveys, metering, records, and interviews",
    household_level="TRUE", community_level="TRUE",
    institutional_fragmentation="TRUE", administrative_review="TRUE", political_coordination="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_quantity="TRUE", affordability="TRUE",
    effect_measure="inductive comparative institutional-technical governance analysis",
    effect_estimate="Parallel supply of ground and surface water resulted in more adequate supply and better end-use optimization than single-source (groundwater-only) supply; inter-household inequity was driven primarily by socio-economic differences among households, but could be mitigated by increasing public-tap frequency; most water-supply arrangements were found to be financially unsustainable regardless of institutional model; critically, responsiveness to citizen needs was significantly higher when water distribution was managed by local (municipal) governments rather than para-statal agencies, leading the authors to conclude that an optimal institutional service modality separates roles by function -- para-statal agencies providing bulk surface-water supply, with local governments managing the actual distribution of both bulk surface water and groundwater to households -- rather than mixing bulk-supply and distribution functions within a single institutional actor.",
    study_design="four-town inductive comparative institutional-governance case study with household surveys, metering, records, and interviews",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: original four-town comparative study combining household surveys, metering, and interviews to directly link specific institutional service-delivery arrangements (municipal vs. para-statal management) to measured water-governance outcomes including responsiveness, equity, and access.",
    source_document="Lele, Madhyastha, Sulagna, Dhavamani & Srinivasan 2018, Water Policy (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established institutional-comparative-governance inclusion precedent (Saleth & Sastry Karnataka; Gopakumar Bengaluru): original multi-town comparative study directly linking specific institutional service-delivery arrangements to measured household water-access and governance-responsiveness outcomes. NOT effect_sizes eligible: inductive comparative case-study analysis across four towns, no regression-based estimate isolating a single mechanism with a formal comparator. Extracted for record_id R6B7F134E71E2.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
