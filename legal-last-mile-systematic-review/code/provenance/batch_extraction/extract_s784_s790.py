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

# S784 - Bhattarai et al 2021 - Nepal gender inequality
add("S784",
    citation="Bhattarai B, Upadhyaya R, Neupane KR, Devkota K, Maskey G, Shrestha S, Mainali B, Ojha H (2021). Gender inequality in urban water governance: Continuity and change in two towns of Nepal. World Water Policy.",
    doi="10.1002/wwp2.12052",
    publication_year="2021",
    country="Nepal",
    subnational_unit="two towns, Nepal",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="local-level water management bodies (with statutory 30% quota reserved for women)",
    regulatory_model="Qualitative case study of gender inequality in urban water governance, examining the effect of Nepal's statutory 30% women's-quota requirement in local water management bodies and property-ownership structures on women's voice, access to, and control over water and sanitation services",
    population="men and women involved in water management practices, and stakeholders in water resource management, two towns",
    sample_size="qualitative narrative interviews with men and women water-management participants and stakeholders",
    household_level="TRUE", community_level="TRUE",
    eligibility="TRUE", participation="TRUE", discretion_accommodation="TRUE", property="TRUE",
    water_access="TRUE", sanitation_access="TRUE",
    effect_measure="qualitative narrative/thematic analysis",
    effect_estimate="Despite the statutory 30% women's quota in local water management bodies, women's voice in water governance remains systematically excluded; gender-based disadvantage intersects with economic disadvantage and property-ownership structures that constrain women's access to water and sanitation services, producing largely tokenistic ('paper') participation",
    study_design="qualitative comparative case study (two towns)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="1",
    mechanism_certainty="Moderate: qualitative case study directly examining a statutory participation-quota mechanism (30% women's representation requirement) and property-ownership legal structures as institutional drivers of gender-differentiated water/sanitation access, finding persistent tokenistic implementation despite the formal legal requirement.",
    source_document="Bhattarai et al. 2021, World Water Policy (retrieved via Google Drive, Antigravity batch)",
    section="Sections 3-5 (Nepal water policy/governance; findings)",
    exact_location="Sections 3-5",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: examines a statutory participation-quota mechanism and property-ownership legal structures as institutional drivers of gendered water-access exclusion, matching CODEBOOK eligibility/participation/property fields. NOT effect_sizes eligible: qualitative narrative analysis, no regression-based estimate. Extracted for record_id RE3D6C0549F37.",
    )

# S785 - Wait et al 2020 - North Carolina well water
add("S785",
    citation="Wait K, Katner A, Gallagher D, Edwards M, Mize W, Jackson CLP, Pieper KJ (2020). Disparities in well water outreach and assistance offered by local health departments: A North Carolina case study. Science of the Total Environment.",
    doi="10.1016/j.scitotenv.2020.141173",
    publication_year="2020",
    country="United States",
    subnational_unit="North Carolina (statewide survey of local health departments)",
    legal_system="common law",
    urban_rural="both",
    service_provider="North Carolina local health departments (LHDs), implementing statewide private-well construction standards under the Safe Drinking Water Act framework and state well-construction law",
    regulatory_model="Statewide survey of North Carolina local health department private-well programs, evaluating variation in capacity, structure, and services (well-construction oversight mandated by law vs. discretionary outreach/testing/assistance services for existing well users) implementing state private-well regulations at the local level",
    population="private well users in North Carolina, served by local health departments",
    sample_size="survey of all North Carolina local health departments (LHD private-well programs)",
    household_level="TRUE", community_level="TRUE",
    discretion="TRUE", discretion_accommodation="TRUE", bureaucratic_assistance="TRUE", enforcement="TRUE",
    documentation="TRUE",
    water_access="TRUE", service_quality="TRUE",
    effect_measure="descriptive/comparative survey analysis of LHD program capacity and services",
    effect_estimate="All LHDs uniformly enforced legally-mandated well-construction oversight, but services to existing well users (outreach, testing assistance) were offered infrequently and inconsistently; variation in staff numbers and assigned responsibilities produced unequal access to services and information for well users across NC counties, unrelated to the number of well users served",
    study_design="statewide survey of local government agency programs",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: statewide survey directly documenting how discretionary local implementation of state private-well regulations, absent statutory mandates for existing-well-user support, produces unequal access to water-safety services and information across jurisdictions.",
    source_document="Wait et al. 2020, Science of the Total Environment (retrieved via Google Drive, Antigravity batch)",
    section="Results and discussion",
    exact_location="Sections on LHD program capacity and service variation",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: directly documents an administrative-implementation gap (state private-well law mandates construction oversight but not existing-user support) driving unequal access to water-safety services at the local government level, matching CODEBOOK discretion/bureaucratic_assistance fields. NOT effect_sizes eligible: descriptive survey analysis, no regression-based estimate. Extracted for record_id RE290B71E882F.",
    )

# S786 - Lloyd Owen 2013 - Glas Cymru Wales
add("S786",
    citation="Lloyd Owen D (2013). Glas Cymru: lessons from nine years as a not-for-profit public-private partnership. International Journal of Water Resources Development.",
    doi="10.1080/07900627.2012.721671",
    publication_year="2013",
    country="United Kingdom (Wales)",
    subnational_unit="Wales",
    legal_system="common law",
    urban_rural="both",
    service_provider="Dwr Cymru Welsh Water (DCWW), owned by the not-for-profit company Glas Cymru Cyfyngedig since 2001, regulated by Ofwat under the Water Industry (Wales/England) price-cap regulatory framework",
    regulatory_model="Case study of the Glas Cymru not-for-profit public-private partnership ownership/financing model for DCWW (2001-2010), comparing financial, tariff, and affordability outcomes against the ten privatized-for-profit water and sewerage companies (WaSCs) in England under the same Ofwat price-cap regulatory regime, and against the statutory 1999 ban on domestic water disconnections",
    population="DCWW customers, Wales, compared with customers of the nine other privatized WaSCs in England",
    sample_size="company-level financial/tariff panel data, 2001-2010 (10-year regulatory case study)",
    household_level="TRUE", community_level="TRUE",
    fees="TRUE", disconnection="TRUE", enforcement="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE", service_continuity="TRUE",
    effect_measure="comparative descriptive financial/tariff analysis (company-level panel, 2001-2010)",
    effect_estimate="Customer rebates ('customer dividends') worth GBP9-22 per household were distributed 2003-2009 (no other WaSC offered comparable rebates); DCWW household bills fell from 23% above sector average in 2001 to 12% above average by 2010; statutory ban on domestic disconnections since 1999 meant affordability support relied on assistance schemes (e.g., Welsh Water Assist capped-bill scheme, used by 8,000 households in 2009/10)",
    study_design="single-company regulatory case study with sector-comparative descriptive statistics",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: detailed institutional/regulatory case study of a not-for-profit ownership model operating under Ofwat price-cap regulation and the statutory disconnection ban, with concrete affordability outcome data (customer rebates, bill comparisons, assistance-scheme uptake).",
    source_document="Lloyd Owen 2013, International Journal of Water Resources Development (retrieved via Google Drive, Antigravity batch)",
    table="Tables 1-9",
    section="Financial performance; Customer charges; Affordability and nonpayment",
    exact_location="Sections on customer charges and affordability",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: institutional/regulatory case study of a specific ownership-model/regulatory mechanism (not-for-profit PPP under price-cap regulation, statutory disconnection ban) with concrete affordability outcome data, extending the established regulatory-mechanism precedent line. NOT effect_sizes eligible: descriptive company-level panel/sector comparison, no regression-based estimate. Extracted for record_id RE27DBC552685.",
    )

# S787 - Montgomery & Dacin - Detroit water wars
add("S787",
    citation="Montgomery AW, Dacin MT. Water Wars in Detroit: Custodianship and the Work of Institutional Renewal. Academy of Management Journal.",
    publication_year="2020",
    country="United States",
    subnational_unit="Detroit, Michigan",
    legal_system="common law",
    urban_rural="urban",
    service_provider="Detroit Water and Sewerage Department (DWSD), under municipal bankruptcy/emergency-management institutional context",
    regulatory_model="Longitudinal qualitative institutional-theory study of the 2014 mass water-shutoff crisis (33,000 of 130,000 DWSD household accounts) and the subsequent institutional-renewal process, examining institutional custodians (operatives, warriors, converts, agnostics) working to restore/reform the neglected public water-service institution",
    population="Detroit water utility customers, particularly marginalized low-income households facing shutoffs",
    sample_size="longitudinal qualitative study, prior to 2014 shutoffs through 2017",
    household_level="TRUE", community_level="TRUE",
    fees="TRUE", disconnection="TRUE", reconnection="TRUE", enforcement="TRUE", sanction="TRUE",
    institutional_fragmentation="TRUE", political_coordination="TRUE", participation="TRUE",
    water_access="TRUE", affordability="TRUE", service_continuity="TRUE",
    effect_measure="longitudinal qualitative institutional-theory analysis (interviews, participant observation)",
    effect_estimate="DWSD issued shutoff notices to roughly half its 130,000 customer accounts in 2014 (accounts 60+ days or $150+ past due); the crisis catalyzed distributed and heterogeneous institutional-custodian responses working to renew the neglected public water-service institution, with direct implications for resource access and affordability in marginalized communities",
    study_design="longitudinal qualitative institutional-theory case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: in-depth longitudinal case study of a major institutional/administrative water-disconnection crisis (33,000 household shutoffs) and the resulting institutional-renewal process, directly documenting resource-access and affordability effects in marginalized communities, though framed through an institutional-theory/organizational-studies lens.",
    source_document="Montgomery & Dacin, Academy of Management Journal (retrieved via Google Drive, Antigravity batch)",
    section="Introduction and findings",
    exact_location="Introduction and custodianship findings sections",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: unlike organisational-framework-development studies excluded under E01 (cf. Weaver et al. 2019 CoP theory), this paper's core empirical content is the actual mass water-disconnection crisis and institutional response, directly matching the established corporatization/disconnection precedent line (cf. Smith 2004, Sutherland et al.). NOT effect_sizes eligible: qualitative institutional-theory case study, no regression-based estimate. Extracted for record_id RE26DB8683A1F.",
    )

# S788 - Marques, Simoes & Berg 2013 - Cape Verde
add("S788",
    citation="Marques RC, Simoes P, Berg S (2013). Water sector regulation in small island developing states: an application to Cape Verde. Water Policy.",
    publication_year="2013",
    country="Cape Verde",
    subnational_unit="national (archipelago)",
    legal_system="civil law",
    urban_rural="both",
    service_provider="water utilities regulated by ARE (Agencia de Regulacao Economica), the multi-sector regulator created in 2003",
    regulatory_model="Institutional/regulatory design study developing a benchmarking and yardstick-competition performance-evaluation regulatory model for ARE, Cape Verde's multi-sector water regulator, aimed at improving water utility performance and network coverage in a small island developing state context",
    population="water utility customers across Cape Verde's archipelago",
    sample_size="regulatory design/benchmarking case study",
    household_level="", community_level="TRUE",
    institutional_fragmentation="TRUE", enforcement="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_coverage="TRUE", service_quality="TRUE",
    effect_measure="regulatory-design analysis (benchmarking/yardstick competition performance-evaluation model)",
    effect_estimate="Socioeconomic conditions and severe water scarcity have constrained water-service coverage and quality; ARE's creation in 2003 was intended to improve sector performance in meeting citizens' expectations, with a benchmarking/yardstick-competition regulatory model recommended to achieve significant network expansion and cost containment",
    study_design="regulatory-design case study with comparative benchmarking analysis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="1",
    mechanism_certainty="Moderate: institutional/regulatory design study of a multi-sector regulator (ARE) benchmarking framework aimed at improving water-utility performance and coverage in a small island developing state, matching the established regulatory-mechanism precedent line, though primarily prescriptive/design-oriented rather than an ex-post outcome evaluation.",
    source_document="Marques, Simoes & Berg 2013, Water Policy (retrieved via Google Drive, Antigravity batch)",
    section="Introduction and regulatory model design",
    exact_location="Sections on ARE regulator and benchmarking model design",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: institutional/regulatory-mechanism case study of a specific national water regulator (ARE) and its performance-benchmarking design, matching the established regulatory precedent line (cf. Marson & van Dijk 2016 Zambia, Pezon 2017 Burkina Faso). NOT effect_sizes eligible: regulatory-design/benchmarking-framework analysis, no regression-based estimate. Extracted for record_id RE080CB357B2C.",
    )

# S789 - Grimes 2011 - right to water South Africa
add("S789",
    citation="Grimes HJ (2011). The right to water and its relevance to sustainable water governance. Proceedings of the Institution of Civil Engineers - Engineering Sustainability.",
    doi="10.1680/ensu.2011.164.2.119",
    publication_year="2011",
    country="South Africa",
    subnational_unit="national, with reference to specific municipal water-services disputes (e.g. Mazibuko litigation)",
    legal_system="common law (mixed civil/common law, South Africa)",
    urban_rural="urban",
    service_provider="municipal water services institutions operating under South Africa's constitutional right of access to water (1996 Constitution Bill of Rights) and subsequent water legislation",
    regulatory_model="Legal-institutional analysis applying the UN General Comment No. 15 on the right to water to South Africa's constitutional and legislative water-rights framework, examining conflicts between water service providers and consumers over rights violations (e.g. prepaid meters, disconnections) that arose during implementation of the constitutional right to water",
    population="South African water consumers in disputes with municipal water service providers",
    sample_size="legal-institutional case analysis (South African water-rights litigation and implementation disputes)",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", documentation="TRUE", judicial_review="TRUE", complaint="TRUE",
    disconnection="TRUE", enforcement="TRUE",
    water_access="TRUE", affordability="TRUE",
    effect_measure="legal-institutional case analysis (doctrinal + implementation review)",
    effect_estimate="Although the right of access to water is enshrined in South Africa's constitution and defined in subsequent legislation, implementation of water governance reforms has been less straightforward, bringing water service providers into conflict with consumers who consider their constitutional right to water violated (e.g. through disconnections and prepaid-meter policies)",
    study_design="legal-institutional case analysis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: direct legal-institutional analysis of South Africa's constitutional right to water and its contested implementation (disconnection/prepaid-meter disputes), applying the UN General Comment No. 15 framework -- a core legal-rights mechanism study matching the project's administrative-law/rights scope.",
    source_document="Grimes 2011, Proceedings of the ICE Engineering Sustainability (retrieved via Google Drive, Antigravity batch)",
    section="Sections 1-2 (introduction; water sector governance)",
    exact_location="Sections 1-2",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: direct legal analysis of South Africa's constitutional right to water and implementation disputes (disconnections, prepaid meters) between providers and consumers, core to the project's administrative-law/rights-based exclusion scope. NOT effect_sizes eligible: legal-institutional case analysis, no regression-based estimate. Extracted for record_id RDF291C6CC5DD.",
    )

# S790 - Krasznai Kovacs et al 2019 - political ecology Himalayas
add("S790",
    citation="Krasznai Kovacs E, Ojha H, Neupane KR, Niven T, Agarwal C, Chauhan D, Dahal N, Devkota K, Guleria V, Joshi T, Michael NK, Pandey A, Singh N, Singh V, Thadani R, Vira B (2019). A political ecology of water and small-town urbanisation across the lower Himalayas. Geoforum.",
    doi="10.1016/j.geoforum.2019.10.008",
    publication_year="2019",
    country="India, Nepal",
    subnational_unit="six small towns across the lower Himalayas, India and Nepal",
    legal_system="civil law (mixed common/civil law across India and Nepal)",
    urban_rural="both",
    service_provider="state- and donor-funded drinking water supply schemes, small-town municipal institutions",
    regulatory_model="Political-ecology/hydro-social case study of six state- and donor-led drinking water supply schemes across small urbanising Himalayan towns, examining how new water infrastructure investments stretch institutional and governance capacity (energy, finance, expertise) and create power differentials/conflicts between urban downstream and rural upstream communities over water access",
    population="urban small-town residents and rural upstream source-region communities, India and Nepal",
    sample_size="six case-study towns",
    household_level="TRUE", community_level="TRUE",
    institutional_fragmentation="TRUE", bureaucratic_assistance="TRUE", political_coordination="TRUE",
    service_area="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_coverage="TRUE", service_reliability="TRUE",
    effect_measure="qualitative comparative political-ecology case study",
    effect_estimate="State- and donor-funded water infrastructure investments introduce new institutional dependencies (energy, finance, expertise) that stretch small-town governance capacity, create power differentials favoring urban downstream communities over rural upstream source regions, and disrupt customary water-access arrangements, producing new conflicts over water access as availability changes",
    study_design="qualitative comparative political-ecology case study (six towns)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="1",
    mechanism_certainty="Moderate: comparative political-ecology case study documenting how state/donor water-infrastructure institutional arrangements produce differential water-access outcomes and governance-capacity strain across six small Himalayan towns.",
    source_document="Krasznai Kovacs et al. 2019, Geoforum (retrieved via Google Drive, Antigravity batch)",
    section="Sections 4-5 (intervention trends; evolving rural-urban relations)",
    exact_location="Sections 4-5",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: political-ecology/institutional case study of donor/state water-infrastructure governance arrangements and their differential effects on water access across urban and rural communities in small Himalayan towns, matching CODEBOOK institutional_fragmentation/bureaucratic_assistance fields. NOT effect_sizes eligible: qualitative comparative case study, no regression-based estimate. Extracted for record_id RDE788100646E.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
