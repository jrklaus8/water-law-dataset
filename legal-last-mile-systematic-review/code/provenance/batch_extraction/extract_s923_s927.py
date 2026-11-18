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

# S923 - Reynaud - France PSP, regulation and social policies in water supply
add("S923",
    citation="Reynaud A (2010). Private Sector Participation, Regulation and Social Policies in Water Supply in France. Oxford Development Studies.",
    doi="10.1080/13600811003753362",
    publication_year="2010",
    country="France",
    subnational_unit="nationwide (municipal-level water service delegation)",
    legal_system="civil law",
    urban_rural="both",
    service_provider="municipal water services, directly managed or delegated to private companies (management, lease, or concession contracts), under France's 1992 RMI law recognizing access to water/energy as a right and the 2000 public-private social water fund",
    regulatory_model="Instrumental-variable econometric analysis (2001 INSEE Family Budget and Income Survey) of the determinants of a Water Affordability Index (WAI, share of gross household income spent on water charges), instrumenting private-sector-participation (PSP) status by technical water-service characteristics to correct for endogeneity of municipal delegation choice, examining how PSP, delegation-contract type, and social/regulatory measures affect household water affordability",
    population="French households nationwide (2001 INSEE Family Budget and Income Survey)",
    sample_size="national household income/expenditure survey sample",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", fees="TRUE", institutional_fragmentation="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE",
    effect_measure="instrumental-variable regression of Water Affordability Index on PSP status and delegation-contract characteristics",
    effect_estimate="4.31% of French households (about 1.16 million) spent more than 3% of income on water charges in 2001; single-parent families (especially female-headed) and large low-income families were most vulnerable to water poverty (14.15% of female-headed single-adult families were water-poor versus 4.31% overall; 11.53% where the household head was unemployed); the instrumented econometric analysis found that private-sector participation in water-service delegation did not improve, and if anything worsened, affordability for poor households relative to public management, and that the specific type of delegation contract (management, lease, or concession, and whether signed under the post-Sapin-Law transparent bidding regime) significantly affected the size of this affordability gap.",
    table="Table 1 (affordability by income decile); Table 2 (WAI regression, non-instrumented and IV models)",
    study_design="instrumental-variable econometric analysis of national household survey data",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: instrumental-variable regression directly isolating the effect of private-sector-participation and delegation-contract-type on household water affordability, correcting for endogeneity of the municipal delegation decision.",
    source_document="Reynaud 2010, Oxford Development Studies (retrieved via Google Drive)",
    section="Sections 3-4",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: rigorous institutional/econometric analysis of a specific legal/regulatory framework (1992 RMI law, delegation-contract type, Sapin Law bidding transparency) and its effect on household water access/affordability. NOT effect_sizes eligible: outcome is water charges/affordability (Water Affordability Index), which does not map to Family A/B/C's connection/access-probability/quantity/reliability framework, consistent with the established Whittington S897 (Batch 178) and Alzahrani S908 (Batch 180) precedent that clean regressions on pricing/affordability outcomes are excluded from effect_sizes pooling. Extracted for record_id R8821F07922AB.",
    )

# S924 - Furlong - Good water governance without good urban governance? (Ontario, Canada)
add("S924",
    citation="Furlong K (2012). Good water governance without good urban governance? Regulation, service delivery models, and local government. Environment and Planning A.",
    doi="10.1068/a44616",
    publication_year="2012",
    country="Canada",
    subnational_unit="Ontario (province-wide, with municipal case detail)",
    legal_system="common law",
    urban_rural="both",
    service_provider="Ontario municipal water utilities, operating under provincial Municipal Acts and post-Walkerton drinking-water regulatory reforms (Safe Drinking Water Act 2002, Clean Water Act 2006), with alternative service delivery (ASD) organizational reform as a recurring policy prescription",
    regulatory_model="Documentary/policy case-study analysis of 30+ years of Ontario water-sector institutional reform, tracing 1980s deregulation and organizational reform (alternative service delivery, arm's-length utilities), the 2000 Walkerton E. coli contamination crisis and subsequent province-level regulatory reassertion, and continued municipal governance/budgetary constraints, arguing that regulatory reform at higher scales cannot resolve water-supply challenges rooted in underlying municipal governance and budget capacity",
    population="Ontario municipalities and their water-service customers",
    sample_size="province-wide documentary/policy case study with municipal examples",
    household_level="FALSE", community_level="TRUE",
    legal_status="TRUE", institutional_fragmentation="TRUE", enforcement="TRUE", discretion="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_quality="TRUE", service_reliability="TRUE",
    effect_measure="documentary/policy case-study analysis of regulatory and organizational reform outcomes",
    effect_estimate="The 2000 Walkerton E. coli outbreak (7 deaths, 2,300 illnesses), attributed by the Walkerton Inquiry to cuts in provincial environmental oversight, triggered a province-level 'reregulation' (Safe Drinking Water Act 2002, Clean Water Act 2006) that improved water-quality compliance oversight; however, the paper shows that organizational reforms (alternative service delivery, ASD) promoted alongside this regulatory reassertion, by treating municipal water utilities as independent business units rather than addressing chronic underlying municipal governance problems (restrictive province-municipal fiscal relationships, inconsistent funding, budget stress documented in a $3 billion province-wide municipal fiscal gap), fail to resolve persistent water-supply infrastructure and service problems, demonstrating that regulatory/organizational reform at higher institutional scales is limited in effectiveness without addressing underlying local government capacity and governance culture.",
    study_design="documentary/policy case-study analysis (province-wide, with the Walkerton case and subsequent municipal reforms as focal examples)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: documentary/policy case-study analysis directly linking specific provincial regulatory reforms (Safe Drinking Water Act 2002, Clean Water Act 2006) and organizational reform models (ASD) to water-supply governance and service outcomes over a 30-year period.",
    source_document="Furlong 2012, Environment and Planning A (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established institutional-governance/regulatory-reform inclusion precedent (Monstadt & Schramm, Nyarko, Tiwale): documentary/policy case-study analysis directly linking specific water-sector legal/regulatory reforms to service-delivery governance outcomes. NOT effect_sizes eligible: qualitative documentary/policy case-study analysis, no regression-based estimate isolating a single mechanism. Extracted for record_id R86051205DAED.",
    )

# S925 - Zaato & Ohemeng - Ghana Water Company Limited organizational resilience
add("S925",
    citation="Zaato JJ, Ohemeng FLK (2015). Building Resilient Organizations for Effective Service Delivery in Developing Countries: The Experience of Ghana Water Company Limited. Forum for Development Studies.",
    doi="10.1080/08039410.2015.1036112",
    publication_year="2015",
    country="Ghana",
    subnational_unit="nationwide (Ghana Water Company Limited)",
    legal_system="common law",
    urban_rural="urban",
    service_provider="Ghana Water Company Limited (GWCL), a state-owned urban water utility undergoing organizational-resilience-focused reform after alternating prior public and private management arrangements",
    regulatory_model="Qualitative case study based on nine face-to-face narrative interviews (July-August 2013) with high-ranking officials from seven organizations (Ministry of Water Works and Housing, GWCL, international donors, NGOs, international financial institutions), applying an organizational-resilience theoretical framework to assess whether GWCL's current reform (increased board/management autonomy) will produce a resilient organization capable of improving urban water service delivery",
    population="Ghana urban water utility customers and water-sector institutional stakeholders",
    sample_size="9 semi-structured interviews with officials from 7 water-sector organizations",
    household_level="FALSE", community_level="TRUE",
    legal_status="TRUE", institutional_fragmentation="TRUE", discretion="TRUE", bureaucratic_assistance="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_reliability="TRUE",
    effect_measure="qualitative interview-based case study assessed against an organizational-resilience theoretical framework",
    effect_estimate="Despite Ghana's urban water sector having undergone repeated public-private management reforms and substantial spending, over 50% of urban-centre residents had no piped water connection and the remaining half had only inconsistent access at the time of study; interviews with key water-sector officials revealed that the current reform (granting GWCL's board and management greater autonomy) was viewed as a necessary but insufficient step toward organizational resilience, because it lacked the strong political commitment and critical resource allocation needed to withstand environmental/managerial turbulence, indicating that formal governance-autonomy reforms alone are unlikely to resolve persistent urban water-access and reliability problems without complementary political and financial institutional support.",
    study_design="qualitative case study with semi-structured elite interviews, assessed against an organizational-resilience theoretical framework",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: original semi-structured interviews with high-ranking water-sector officials directly assessing how a specific institutional reform (GWCL board/management autonomy) affects the utility's capacity to improve urban water access and service reliability.",
    source_document="Zaato & Ohemeng 2015, Forum for Development Studies (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established national-utility institutional case-study inclusion precedent (Larrain Chile, Saleth & Sastry Karnataka): original interview-based case study directly examining a specific water-utility governance reform's effect on urban water-access and service-reliability outcomes. NOT effect_sizes eligible: qualitative interview-based case study, no regression-based estimate. Extracted for record_id R83CC2CDECA38.",
    )

# S926 - Vijay & Ghosh - Sabar Shouchagar Project (Nadia District, India)
add("S926",
    citation="Vijay D, Ghosh D (2018). The Sabar Shouchagar Project (toilets for everyone): making Nadia District the first open-defecation-free district in India. Emerald Emerging Markets Case Studies.",
    doi="10.1108/EEMCS-01-2018-0009",
    publication_year="2018",
    country="India",
    subnational_unit="Nadia District, West Bengal",
    legal_system="common law",
    urban_rural="rural",
    service_provider="Nadia District administration and Gram Panchayats, implementing the Sabar Shouchagar (toilets for everyone) sanitation program by coordinating national legal/policy sanitation frameworks (Total Sanitation Campaign, Nirmal Bharat Abhiyan) with rural-employment and livelihoods programs (MGNREGA, National Rural Livelihoods Mission) and intensive community mobilization",
    regulatory_model="Documented institutional case study of Nadia District's district-wide sanitation-access program, coordinating multiple national legal/policy instruments (sanitation campaigns, employment-guarantee and livelihoods schemes) and local government bodies (Gram Panchayats) with community mobilization to eliminate open defecation and achieve district-wide toilet coverage and usage, quantifying before/after institutional-intervention outcomes",
    population="rural households of Nadia District, West Bengal",
    sample_size="district-wide program covering the full population of Nadia District",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", eligibility="TRUE", institutional_fragmentation="TRUE", bureaucratic_assistance="TRUE", participation="TRUE",
    formal_connection="TRUE", sanitation_access="TRUE", service_coverage="TRUE",
    effect_measure="before/after program-outcome documentation (district administrative and program monitoring data)",
    effect_estimate="Under the Sabar Shouchagar institutional program -- coordinating national sanitation legal/policy frameworks (Total Sanitation Campaign, Nirmal Bharat Abhiyan) with employment/livelihoods schemes (MGNREGA, NRLM) and Gram Panchayat-level implementation and community mobilization -- household toilet coverage in Nadia District rose from approximately 60% to 97%, and toilet usage rose from approximately 57% to 99.8%, making Nadia the first district in India certified as open-defecation-free, demonstrating that coordinated multi-program institutional intervention combined with local-government implementation and community mobilization can rapidly transform district-wide sanitation-access outcomes.",
    table="program before/after coverage and usage statistics",
    study_design="institutional/programmatic case study with before/after district-level coverage and usage data",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: documented before/after district-wide program-outcome data directly linking a specific coordinated legal/policy sanitation-program intervention to quantified household sanitation-access and usage outcomes.",
    source_document="Vijay & Ghosh 2018, Emerald Emerging Markets Case Studies (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established government sanitation/infrastructure-program inclusion precedent (Kundu JnNURM, Batch 179): teaching-case-study format with substantial original institutional/programmatic documentation and quantified before/after coverage outcomes, distinguished from a purely pedagogical exercise by its detailed institutional-coordination content. NOT effect_sizes eligible: descriptive before/after program case study, no regression-based estimate isolating a single mechanism. Extracted for record_id R8132FFEC58AA.",
    )

# S927 - Roth - Constructing community health and safety (Central Saanich, BC, Canada)
add("S927",
    citation="Roth WM (2008). Constructing community health and safety. Proceedings of the Institution of Civil Engineers - Municipal Engineer.",
    doi="10.1680/muen.2008.161.2.83",
    publication_year="2008",
    country="Canada",
    subnational_unit="Central Saanich, British Columbia (Vancouver Island)",
    legal_system="common law",
    urban_rural="rural",
    service_provider="Central Saanich municipal council and municipal engineers, deciding whether to extend the existing municipal watermain to service households currently reliant on contaminated private wells",
    regulatory_model="Ten-year anthropological/ethnographic study of municipal engineering and administrative decision-making over a proposal to extend Central Saanich's municipal watermain by 4 km to service 64 homes drawing water from wells with documented high biological and chemical contaminant levels, examining how municipal engineers navigated conflicting scientific, testimonial, political, and ethical knowledge claims in an acrimonious public conflict over extending municipal water access",
    population="64 households in a rural zoned area of Central Saanich relying on contaminated private wells",
    sample_size="single-municipality, ten-year longitudinal ethnographic case study",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", discretion="TRUE", service_area="TRUE", participation="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_quality="TRUE",
    effect_measure="ten-year ethnographic/anthropological case study of municipal decision-making",
    effect_estimate="Over a decade-long, often acrimonious conflict, municipal engineers in Central Saanich had to evaluate conflicting scientific, testimonial, political, and ethical knowledge claims from residents, environmental advocates, and technical experts in deciding whether to extend the municipal watermain 4 km to connect 64 households whose private wells showed high biological and chemical contamination; the study documents how municipal administrative and engineering decision-making processes -- not purely technical water-quality assessment -- determined the ultimate resolution of whether affected households gained formal access to safe municipal water, illustrating the centrality of local institutional/administrative discretion and conflict-resolution processes to household water-access outcomes even in a high-income-country municipal context.",
    study_design="ten-year longitudinal anthropological/ethnographic case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: original ten-year ethnographic study directly documenting how municipal administrative/engineering decision-making processes determined household access to municipal water for a specific, identified group of households.",
    source_document="Roth 2008, Proceedings of the Institution of Civil Engineers - Municipal Engineer (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established municipal-administrative-decision-making inclusion precedent (Biddle & Baehler NYC/Flint, Batch 182): original longitudinal ethnographic study directly documenting how municipal institutional/administrative decision-making processes determine household water-access outcomes, including in a high-income-country context. NOT effect_sizes eligible: qualitative ethnographic case study, no regression-based estimate. Extracted for record_id R8CC9DED5F88A.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
