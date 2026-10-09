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

# S912 - Hossain - Dhaka bosti utility negotiation
add("S912",
    citation="Hossain S (2012). The production of space in the negotiation of water and electricity supply in a bosti of Dhaka. Habitat International.",
    doi="10.1016/j.habitatint.2011.04.010",
    publication_year="2012",
    country="Bangladesh",
    subnational_unit="Dhaka",
    legal_system="common law",
    urban_rural="urban",
    service_provider="local associations and informal vendors negotiating with Dhaka Water Supply and Sewerage Authority (DWASA) and Dhaka Electricity Supply Company (DESCO) staff, political leaders and community leaders",
    regulatory_model="Ethnographic case study of a Dhaka bosti (informal settlement) documenting how DWASA and DESCO's refusal to provide direct utility connections in informal settlements (where over one-third of Dhaka's population lives) produces a hybrid institutional sphere of informal regulation, in which a local association negotiates access to water and electricity on behalf of residents through continuously changing arrangements with administrative staff, political leaders and community leaders",
    population="residents of a bosti (informal settlement), Dhaka",
    sample_size="ethnographic case study",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", discretion="TRUE", institutional_fragmentation="TRUE",
    formal_connection="TRUE", water_access="TRUE",
    effect_measure="ethnographic case-study institutional analysis",
    effect_estimate="Because DWASA does not provide direct utility supply in Dhaka's informal settlements, residents access water only through a local association's continuous informal negotiation with DWASA administrative staff, political leaders and community leaders, operating in a hybrid regulatory 'third space'; this negotiated, informally regulated access arrangement is a necessary condition for continued utility supply to a population formally excluded from direct connection, demonstrating that the state utility's formal non-recognition of informal settlements produces an entirely negotiation-dependent, institutionally precarious mode of water access for a third of the city's population.",
    study_design="ethnographic case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: ethnographic case study directly documenting how formal utility non-recognition of informal settlements produces a negotiated, informally regulated water-access arrangement.",
    source_document="Hossain 2012, Habitat International (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established informal-settlement/formal-non-recognition inclusion precedent (Wahby Cairo, S904): ethnographic case study directly documenting how formal utility non-recognition produces negotiated informal water-access arrangements. NOT effect_sizes eligible: ethnographic case study, no regression-based estimate. Extracted for record_id R98EE7A8CD53B.",
    )

# S913 - Baud & Dhanalakshmi - Chennai sewerage governance
add("S913",
    citation="Baud I, Dhanalakshmi R (2007). Governance in urban environmental management: Comparing accountability and performance in multi-stakeholder arrangements in South India. Cities.",
    doi="10.1016/j.cities.2006.11.003",
    publication_year="2007",
    country="India",
    subnational_unit="two municipalities around Chennai",
    legal_system="common law",
    urban_rural="urban",
    service_provider="municipal government and multi-stakeholder arrangements including Resident Welfare Associations (RWAs), Chennai",
    regulatory_model="Comparative case study (strategic interviews with governmental and civil-society organizations, on-site observations) of underground sewerage-system investment in two municipalities around Chennai, comparing a successful and a non-successful case to identify the multi-stakeholder governance factors -- citizen/stakeholder inclusion, decision-making patterns, accountability mechanisms -- that produced different equity-of-distribution outcomes in service provision",
    population="residents of two municipalities around Chennai, India",
    sample_size="comparative 2-municipality case study with strategic interviews and on-site observation",
    household_level="FALSE", community_level="TRUE",
    institutional_fragmentation="TRUE", discretion="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_quality="TRUE",
    effect_measure="comparative case-study governance analysis",
    effect_estimate="Multi-stakeholder governance arrangements for underground sewerage investment succeeded in producing more accountable and equitable service outcomes only where a high level of Resident Welfare Association organization existed (limited in practice to middle-class neighborhoods) and where trusted political leadership was present; political interference from opposing parties at the higher state level was identified as a key factor explaining why comparable multi-stakeholder arrangements failed in the non-successful case, demonstrating that the specific institutional design and political conditions of multi-stakeholder governance arrangements directly determine whether service investment reaches equitable distribution or remains limited to already-advantaged neighborhoods.",
    study_design="comparative case study (2 municipalities, successful vs. non-successful sewerage investment)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: comparative case-study analysis directly documenting how multi-stakeholder governance design and political conditions shape equitable sanitation-service-investment outcomes.",
    source_document="Baud & Dhanalakshmi 2007, Cities (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established multi-stakeholder-governance inclusion precedent: comparative case study directly documenting how governance design shapes equitable sanitation-investment outcomes. NOT effect_sizes eligible: qualitative comparative case study, no regression-based estimate. Extracted for record_id R95641AC1C405.",
    )

# S914 - Dugard - South Africa urban basic services rights
add("S914",
    citation="Dugard J (2011). Urban Basic Services: Rights, Reality, and Resistance. In Malcolm Langford et al. (eds.), Socio-Economic Rights in South Africa: Symbols or Substance? Cambridge University Press.",
    doi="10.1017/CBO9781139108591.013",
    publication_year="2011",
    country="South Africa",
    subnational_unit="national, with local case examples (Madibeng Municipality, North West Province)",
    legal_system="common law",
    urban_rural="both",
    service_provider="local government municipalities operating under South Africa's constitutional and statutory basic-services legal framework",
    regulatory_model="Documentary and case-based legal analysis of South Africa's basic-services rights framework -- the Constitution's entrenched right to water, national Free Basic Water/Electricity/Sanitation policies, and the Water Services Act 108 of 1997's minimum-standards requirements -- documenting the divergence between this rights-protective legal framework and local-level service-delivery reality, tracing this divergence to a cost-recovery-driven municipal governance model, widespread service disconnections in poor urban areas, and municipal governance collapses (more than 20 municipalities placed under Section 139 administration in 2010), illustrated through service-delivery-protest case examples and constitutional test litigation",
    population="urban poor residents of South African municipalities",
    sample_size="documentary/legal analysis with illustrative case examples",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", enforcement="TRUE", fees="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_reliability="TRUE",
    effect_measure="documentary/legal case-based analysis",
    effect_estimate="Despite South Africa's constitutionally entrenched right to water and a Water Services Act 108 of 1997 legal framework mandating basic minimum standards, local-level service delivery has widely failed to match this rights framework, as a cost-recovery-driven municipal governance model (basic services treated as a commercial revenue stream rather than a public-health entitlement) has produced widespread limitation and disconnection of existing water services in poor urban areas, rolling back post-apartheid connection gains; municipal governance collapse (with more than 20 municipalities placed under Section 139 constitutional administration in 2010) and rising service-delivery protests and constitutional test litigation document this divergence between the formal legal rights framework and the material reality of urban basic-services access.",
    study_design="documentary/legal analysis with illustrative case examples",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: documentary/legal analysis directly documenting the gap between a specific constitutional/statutory rights framework and municipal-level water-service delivery, illustrated with concrete disconnection and governance-collapse evidence.",
    source_document="Dugard 2011, in Socio-Economic Rights in South Africa (Cambridge University Press, retrieved via Google Drive)",
    section="Introduction",
    exact_location="pp. 275-276 and throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established constitutional-rights/service-delivery-gap inclusion precedent (Von Schnitzler S885, Mazibuko line): documentary/legal analysis directly documenting the gap between South Africa's constitutional water-rights framework and municipal service-delivery/disconnection reality. NOT effect_sizes eligible: documentary/legal case-based analysis, no regression-based estimate. Extracted for record_id R9499AFC94021.",
    )

# S915 - Gopakumar - Bengaluru water PPP experiments
add("S915",
    citation="Gopakumar G (2014). Experiments and Counter-Experiments in the Urban Laboratory of Water-Supply Partnerships in India. International Journal of Urban and Regional Research.",
    doi="10.1111/1468-2427.12076",
    publication_year="2014",
    country="India",
    subnational_unit="Bengaluru",
    legal_system="common law",
    urban_rural="urban",
    service_provider="a public-private partnership water-supply pilot project in an informal settlement, Bengaluru",
    regulatory_model="Qualitative case study (STS/political-ecology synthesis) of a public-private-partnership pilot project as an 'experimental' institutional intervention aimed at enrolling informal water users in a Bengaluru informal settlement into standardized, marketized modes of water-supply provision, documenting both the marketization strategies pursued by the partnership and the 'counter-experimentation' networks residents, local associations and activists formed in response, exposing recurring 'governance failures' in the neoliberal reconfiguration of water-supply provision",
    population="residents of an informal settlement served by a water-supply PPP pilot, Bengaluru",
    sample_size="qualitative case study of one PPP pilot project",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", institutional_fragmentation="TRUE", discretion="TRUE",
    formal_connection="TRUE", water_access="TRUE",
    effect_measure="qualitative case-study institutional analysis",
    effect_estimate="A public-private-partnership water-supply pilot project in a Bengaluru informal settlement, designed to enroll previously informal water users into standardized marketized water-supply provision, simultaneously advanced this marketization agenda while inadvertently generating opportunities for residents, local associations and activists to organize 'counter-experimentation' networks contesting the partnership's terms, revealing persistent institutional 'governance failures' in the water-supply-partnership model that complicate a purely instrumental, top-down understanding of how such partnerships expand formal water access to informal settlements.",
    study_design="qualitative case study (single PPP pilot project)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: qualitative case study directly documenting how a specific PPP institutional intervention's marketization strategy and resident counter-mobilization shape water-access outcomes in an informal settlement.",
    source_document="Gopakumar 2014, IJURR (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established water-PPP/informal-settlement inclusion precedent (Nizkorodov S906): qualitative case study directly documenting how a specific PPP institutional intervention shapes water access in an informal settlement. NOT effect_sizes eligible: single-case qualitative study, no regression-based estimate. Extracted for record_id R934020F5D9E0.",
    )

# S916 - Toure, Kane, Noel, Turmine, Nedeff & Lazar - Mbour Senegal water-poverty GIS
add("S916",
    citation="Toure NM, Kane A, Noel JF, Turmine V, Nedeff V, Lazar G (2012). Water-poverty relationships in the coastal town of Mbour (Senegal): Relevance of GIS for decision support. International Journal of Applied Earth Observation and Geoinformation.",
    doi="10.1016/j.jag.2011.08.001",
    publication_year="2012",
    country="Senegal",
    subnational_unit="Mbour",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="Senegalese Waters (Sénégalaise Des Eaux, SDE), a private operator under the 1995 Senegalese water-sector reform",
    regulatory_model="GIS-based spatial household survey (120 households, grid-based sampling) examining the relationship between economic poverty and water access/affordability in Mbour, a coastal Senegalese town, tracing low and uneven household connection rates to the SDE piped network to what the authors describe as 'the perverse effect of the reform of the Senegalese water sector in 1995', mapping water-poverty (defined per the Global Water Partnership as water costs exceeding 5% of monthly income) against income poverty and finding they do not fully overlap spatially",
    population="households in Mbour, Senegal (approximately 1,000+ persons across 120 sampled households)",
    sample_size="120 households (99.19% response rate), spatial grid sampling",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", fees="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE",
    effect_measure="GIS-based household survey with spatial water-poverty index analysis",
    effect_estimate="Only 48.7% of Mbour households are connected to the SDE piped water distribution network, with the remainder relying on wells (38.6%) or expensive standpipes; standpipe water costs 1,750 CFA francs per cubic meter versus the 191 CFA franc social (subsidized) rate through formal connections -- a roughly 9-fold price differential; the study finds this persistently low and unequal connection coverage traces to the 1995 Senegalese water-sector reform's institutional design, and documents that water poverty (defined as water costs exceeding 5% of household income) affects 52.4% of water-paying families and does not spatially coincide entirely with general income poverty, meaning some non-poor neighborhoods still suffer poor water access as a direct legacy of the institutional reform.",
    study_design="GIS-based household survey with spatial water-poverty index analysis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: original 120-household GIS-based survey directly linking a specific national water-sector reform (Senegal, 1995) to quantified, spatially-mapped household water-connection and affordability outcomes.",
    source_document="Toure, Kane, Noel, Turmine, Nedeff & Lazar 2012, International Journal of Applied Earth Observation and Geoinformation (retrieved via Google Drive)",
    section="Results and discussion",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established national-reform/household-survey inclusion precedent (Larrain Chile): original household survey directly linking a national water-sector legal reform (Senegal 1995) to quantified household connection/affordability outcomes. NOT effect_sizes eligible: descriptive GIS/survey spatial analysis, no regression-based estimate isolating the mechanism. Extracted for record_id R8FA24A9DD2C8.",
    )

# S917 - Crane - Jakarta water market deregulation
add("S917",
    citation="Crane R (1994). Water Markets, Market Reform and the Urban Poor: Results from Jakarta, Indonesia. World Development.",
    doi="10.1016/0305-750X(94)90169-4",
    publication_year="1994",
    country="Indonesia",
    subnational_unit="Jakarta",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="Perusahaan Air Minum Jaya, the Jakarta municipal water enterprise",
    regulatory_model="Household survey and market-impact analysis of the April 1990 deregulation measure by Jakarta's municipal water enterprise, which permitted households with metered water connections to legally resell municipal water to non-connected neighbors -- a specific administrative/regulatory reform intended to expand effective water access to the roughly 80% of Jakarta's population lacking direct in-house connections, examining the deregulation's impact on money savings, consumption, and market structure for former vendor and standpipe customers",
    population="Jakarta households without direct municipal water connections, particularly former street-vendor and standpipe customers",
    sample_size="household survey (municipal water enterprise collaboration, questionnaire-based)",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", fees="TRUE", eligibility="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE",
    effect_measure="household survey with market-impact (preliminary evidence) analysis",
    effect_estimate="The April 1990 deregulation measure permitting Jakarta households with metered connections to legally resell municipal water produced primary social benefits in the form of money savings and increased water consumption for former street-vendor and standpipe customers; the aggregate market effect was found to be roughly equivalent to a costless expansion of the standpipe system, with the key distributional difference being significant income transfers from professional vendors and standpipe operators to household resellers, demonstrating that a specific administrative deregulation mechanism directly expanded effective water access and affordability for the urban poor without requiring new infrastructure investment.",
    study_design="household survey with market-impact (preliminary evidence) analysis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: household survey combined with market-impact analysis directly documenting a specific administrative deregulation mechanism's effect on water affordability and consumption for the urban poor.",
    source_document="Crane 1994, World Development (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established administrative-deregulation/water-access inclusion precedent: household survey directly documenting a specific 1990 regulatory reform's effect on water affordability/consumption for the urban poor. NOT effect_sizes eligible: preliminary descriptive market-impact analysis, no regression-based estimate isolating the mechanism. Extracted for record_id R984395E64462.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
