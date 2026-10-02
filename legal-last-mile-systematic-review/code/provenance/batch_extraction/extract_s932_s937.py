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

# S932 - Guidi Gutierrez, Gonzalez Gomez & Guardiola - Sucre Bolivia governance deficit
add("S932",
    citation="Guidi Gutierrez E, Gonzalez Gomez F, Guardiola J (2013). Water access in Sucre, Bolivia: a case of governance deficit. International Journal of Water Resources Development.",
    doi="10.1080/07900627.2012.721677",
    publication_year="2013",
    country="Bolivia",
    subnational_unit="Sucre (capital city)",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="publicly-owned (non-privatized) water-services company in Sucre, operating under Bolivia's 1906 Public Domain and Water Use Act and subsequent post-2006 water-sector legal/institutional reforms (Ministry of Water, anti-privatization political shift)",
    regulatory_model="Case-study/documentary institutional analysis of Sucre's water-services governance framework, tracing Bolivia's national water-regulatory history (1906 Public Domain and Water Use Act, post-2006 Ministry of Water reforms following the Cochabamba and El Alto privatization conflicts) and diagnosing the absence of an appropriate decision-making governance framework -- rather than public/private ownership per se -- as the source of service-delivery inefficiencies and social conflict in Sucre",
    population="Sucre, Bolivia water-service customers (fourth-largest Bolivian city)",
    sample_size="single-city case study with national regulatory-history documentary analysis",
    household_level="FALSE", community_level="TRUE",
    legal_status="TRUE", institutional_fragmentation="TRUE", discretion="TRUE", enforcement="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_reliability="TRUE",
    effect_measure="documentary/institutional case-study analysis",
    effect_estimate="Despite Sucre's water service being publicly (not privately) managed -- unlike the earlier Cochabamba and El Alto conflicts, which were explicitly about privatization -- the city nonetheless faces serious social conflict and service-delivery inefficiency, demonstrating that the absence of an adequate water-governance decision-making framework, not ownership structure (public vs. private) per se, is the root cause of poor water-access outcomes in Bolivia; the study finds that Bolivia's fragmented and historically inconsistent regulatory framework (dating to the 1906 Public Domain and Water Use Act, later disrupted by the anti-privatization political shift after 2006) has left cities like Sucre without adequate institutional mechanisms for resolving water-management conflicts and improving access.",
    study_design="documentary/institutional case-study analysis with national regulatory-history review",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: documentary institutional case-study analysis directly linking a specific national water-governance regulatory framework's fragmentation and gaps to household water-access and service-conflict outcomes in a named city.",
    source_document="Guidi Gutierrez, Gonzalez Gomez & Guardiola 2013, International Journal of Water Resources Development (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established water-governance-deficit institutional case-study inclusion precedent (Golooba-Mutebi Rwanda/Uganda; Zaato & Ohemeng Ghana): documentary institutional case study directly linking a specific national/municipal water-governance regulatory framework to household water-access and service-conflict outcomes. NOT effect_sizes eligible: qualitative documentary case-study analysis, no regression-based estimate. Extracted for record_id R7B052D90C3BF.",
    )

# S933 - Smith - Citizens' Voice initiative, South Africa
add("S933",
    citation="Smith L (2011). The Limits to Public Participation in Strengthening Public Accountability: A Reflection on the 'Citizens' Voice' Initiative in South Africa. Journal of Asian and African Studies.",
    doi="10.1177/0021909611403708",
    publication_year="2011",
    country="South Africa",
    subnational_unit="two South African cities (urban water service delivery)",
    legal_system="common law",
    urban_rural="urban",
    service_provider="local municipal authorities providing urban water services under South Africa's post-1994 progressive legislative/rights framework",
    regulatory_model="Four-year implementation study of the 'Raising Citizens' Voice in the Regulation of Water Services' methodology in two South African cities, examining how internal fragmentation across spheres of government and between politicians and officials, combined with a lack of service-delivery recourse mechanisms, restrains citizens' ability to hold local authorities publicly accountable for water-service delivery despite a progressive legislative rights framework",
    population="urban water-service users in two South African cities",
    sample_size="four-year multi-city implementation/action-research study",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", institutional_fragmentation="TRUE", administrative_review="TRUE", complaint="TRUE", participation="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_quality="TRUE",
    effect_measure="four-year participatory implementation study with lessons-learned analysis",
    effect_estimate="Despite South Africa's progressive legislative rights framework for water services, citizens' ability to hold local authorities accountable for service-delivery failures is significantly restricted by internal fragmentation across spheres of government and between politicians and officials, compounded by a lack of formal recourse mechanisms in the service-delivery landscape; the four-year implementation of the 'Raising Citizens' Voice' methodology in two cities demonstrated that public-participation initiatives alone cannot overcome this structural institutional fragmentation to meaningfully strengthen public accountability for water-access outcomes.",
    study_design="four-year multi-city participatory action-research/implementation study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: original multi-year implementation research directly documenting how institutional fragmentation across government spheres constrains citizen accountability mechanisms for water-service delivery in two cities.",
    source_document="Smith 2011, Journal of Asian and African Studies (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established institutional-fragmentation/accountability inclusion precedent (Allison Cape Town; Roncoli-type participation studies): original multi-year implementation research directly documenting how government fragmentation constrains citizen accountability for water-access outcomes. NOT effect_sizes eligible: qualitative multi-city implementation study, no regression-based estimate. Extracted for record_id R7891B393A14B.",
    )

# S934 - Rama Mohan - Rural Water Supply in India, institutionalizing people's participation
add("S934",
    citation="Rama Mohan RV (2003). Rural Water Supply in India: Trends in Institutionalizing People's Participation. Water International.",
    doi="10.1080/02508060308691722",
    publication_year="2003",
    country="India",
    subnational_unit="nationwide, with two NGO-led micro-level case studies",
    legal_system="common law",
    urban_rural="rural",
    service_provider="state Rural Water Supply Departments (centralized, supply-driven institutional model) versus community-managed institutional models promoted by sector-reform pilot projects in 63 districts and two NGO case-study projects",
    regulatory_model="Documentary/policy analysis of three decades of institutional change in India's rural water-supply sector, tracing the shift from traditional community water-harvesting/ownership to centralized government supply-driven management, and evaluating the performance of sector-reform pilot projects (63 districts) promoting community participation and ownership, including two detailed NGO-led micro-level case studies as models for scale-up",
    population="rural Indian villages and households (587,226 villages nationwide)",
    sample_size="national policy/documentary analysis plus two NGO-led micro-level case studies",
    household_level="FALSE", community_level="TRUE",
    legal_status="TRUE", institutional_fragmentation="TRUE", participation="TRUE", bureaucratic_assistance="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_reliability="TRUE",
    effect_measure="documentary/policy analysis with case-study comparison",
    effect_estimate="India's shift from traditional community water-management to a centralized, supply-driven government institutional model (with full state-funded costs and no community cost-recovery) is identified as a key driver of poor service delivery, over-exploitation of groundwater, and re-emergence of water-scarce villages; sector-reform pilot projects promoting community participation and ownership in 63 districts showed unimpressive nationwide performance, but two NGO-led micro-level models demonstrated successful community-institutional structures, indicating that the institutional design of water-management ownership and participation directly determines rural water-supply sustainability and access outcomes, with success requiring a holistic approach combining community participation, appropriate institutional structures, and preserved micro-level diversity within macro-level reform uniformity.",
    table="two detailed NGO case-study comparisons of successful micro-level community-institutional models",
    study_design="documentary/policy analysis with comparative case studies",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="Moderate: documentary/policy analysis with case-study evidence directly linking institutional/governance model (centralized supply-driven vs. community-participatory) to rural water-supply sustainability and access outcomes, though without a quantified regression-based comparative estimate.",
    source_document="Rama Mohan 2003, Water International (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established rural-water institutional-participation inclusion precedent (Obeta Nigeria, this same segment; Crow/Swallow/Asamba Kenya): documentary/policy analysis directly linking institutional-ownership models to rural water-access sustainability outcomes, with supporting case-study evidence. NOT effect_sizes eligible: documentary/case-study analysis, no regression-based estimate. Extracted for record_id R756C4F77C0A7.",
    )

# S935 - Hellberg - Water, life and politics: eThekwini municipality governmentality
add("S935",
    citation="Hellberg S (2014). Water, life and politics: Exploring the contested case of eThekwini municipality through a governmentality lens. Geoforum.",
    doi="10.1016/j.geoforum.2014.02.004",
    publication_year="2014",
    country="South Africa",
    subnational_unit="eThekwini municipality (Durban)",
    legal_system="common law",
    urban_rural="both",
    service_provider="eThekwini municipality, which administers differentiated water-service delivery technologies (tariff and payment systems, prepaid meters, free-basic-water allocations, disconnection practices) across different populations under South Africa's right-to-basic-water legal framework",
    regulatory_model="Original narrative-interview fieldwork (conducted 2008/2009) with water users in eThekwini municipality, examining through a governmentality/biopolitics lens how the municipality's differentiated water-service-delivery technologies (targeted at different population groups) shape water users' agency, self-perception as citizens, and lived access to water, despite the municipality's international reputation for pro-poor water-service innovation",
    population="water users across differentiated service-delivery technology zones in eThekwini municipality, Durban",
    sample_size="original narrative-interview fieldwork, 2008/2009",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", fees="TRUE", discretion="TRUE", disconnection="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE",
    effect_measure="original narrative-interview fieldwork analysis",
    effect_estimate="Water users' own narratives reveal that eThekwini municipality's differentiated water-service-delivery technologies -- tariff and payment systems, prepaid meters, free-basic-water allocations, and aggressive disconnection practices for non-payment -- produce markedly different, differentiating effects on how water users experience access to water and perceive themselves as citizens of a democratic South Africa, consolidating rather than eliminating the disconnectedness between different lived experiences within Durban's communities, illustrating that the specific technological/institutional mechanisms through which the constitutional right to basic water is implemented can entrench, rather than resolve, distinctions in water access and citizenship among different population groups.",
    study_design="original narrative-interview ethnographic fieldwork",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: original narrative-interview fieldwork directly documenting how specific municipal water-service-delivery institutional technologies (tariffs, prepaid meters, free-basic-water allocations, disconnection practices) shape differentiated household water-access outcomes.",
    source_document="Hellberg 2014, Geoforum (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established constitutional-rights-framework/institutional-narrative inclusion precedent (Allison Cape Town; Dugard South Africa): original narrative-interview fieldwork directly documenting how specific municipal water-service-delivery institutional technologies shape differentiated household water-access outcomes under a constitutional right-to-water framework. NOT effect_sizes eligible: qualitative narrative-interview fieldwork, no regression-based estimate. Extracted for record_id R73872693EBDD.",
    )

# S936 - Blase, Green & Matson - Public Water Supply Districts impacts, Missouri
add("S936",
    citation="Blase MG, Green PR, Matson A (1973). Selected Impacts of Public Water Supply Districts on Firms, Households and Communities. Journal of the Community Development Society.",
    doi="10.1080/15575330.1973.10877512",
    publication_year="1973",
    country="United States",
    subnational_unit="Boone County and Barton County, Missouri",
    legal_system="common law",
    urban_rural="rural",
    service_provider="Public Water Supply Districts (PWSDs), a specific legal/institutional water-district structure enabled by 1935 Missouri legislation and financed via Farmers Home Administration federal loans beginning in 1961",
    regulatory_model="Mail-questionnaire survey (65% response rate) of members of two Missouri Public Water Supply Districts (Boone County PWSD No. 5, rural-urban fringe, and Barton County PWSD No. 1, agricultural) documenting before/after impacts of PWSD formation -- a specific legal/institutional water-district mechanism -- on population in-migration, land values, household water consumption, and household facility improvements, comparing outcomes across the two district types",
    population="households and firms in two Missouri Public Water Supply District service areas",
    sample_size="211 respondents (Boone County) and 448 respondents (Barton County) mail-questionnaire survey",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", service_area="TRUE", fees="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_quantity="TRUE",
    effect_measure="mail-questionnaire survey with before/after self-reported comparisons",
    effect_estimate="Formation of a Public Water Supply District -- a specific legal/institutional water-district mechanism -- was associated with substantial population in-migration (40% of Boone County respondents and 25% of Barton County respondents were new residents since district formation, with 13-21% explicitly citing water availability as an influence on their relocation decision), a shift away from hauled/well water toward public network connection (33% of Boone County and 40% of Barton County respondents previously hauled water, at higher per-unit cost than the new district price), a substantial increase in monthly household water consumption (Boone County: 2,218 to 3,031 gallons, +37%), land-value appreciation exceeding comparable non-district areas (Boone County: 77% increase vs. 23% statewide; Barton County: 21% increase vs. 13.1% statewide), and household facility investments (Boone County average $1,126; Barton County average $672) following connection to the district's public water network.",
    table="comparative impacts on population movement, land prices, and household facilities across two Public Water Supply Districts",
    study_design="mail-questionnaire survey with before/after self-reported comparison across two water districts",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="Moderate: original survey-based before/after comparison directly linking a specific legal/institutional water-district formation mechanism to household water-connection, consumption, and community-development outcomes, though based on self-reported retrospective data without a formal regression-based causal estimate.",
    source_document="Blase, Green & Matson 1973, Journal of the Community Development Society (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: original survey-based institutional case study directly linking a specific legal water-district-formation mechanism (Missouri PWSD enabling legislation) to household water-connection and consumption outcomes. NOT effect_sizes eligible: descriptive before/after survey comparison, no regression-based estimate isolating the mechanism with a formal comparator/control group. Extracted for record_id R82B3655E82D0.",
    )

# S937 - de Carvalho, Costa, Marques & Netto - household connection to wastewater, Brazil RIA
add("S937",
    citation="de Carvalho BE, Costa SAB, Marques RC, Netto OC (2019). The impact of household connection to public network wastewater systems: regulatory impact assessment. Water Science and Technology.",
    doi="10.2166/wst.2019.102",
    publication_year="2019",
    country="Brazil",
    subnational_unit="Belo Horizonte, Betim, Contagem and Ribeirao das Neves (BBCR), Minas Gerais state",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="COPASA/COPANOR and local water/wastewater companies, regulated by the Water and Wastewater Regulatory Agency of Minas Gerais (ARSAE) under Brazil's national Federal Law 11445/2007 and Minas Gerais State Law 13317/1999 mandating household connection to available public wastewater networks",
    regulatory_model="Ex-ante regulatory impact assessment (RIA) using multiple criteria decision analysis (MCDA, MACBETH method) with a stakeholder focus group (ARSAE, academics, local government) to evaluate four regulatory policy options -- strong (100%), advanced (75%), intermediate (50%) infrastructure diffusion, and 'do nothing' (0%) -- for reducing the gap of non-connected households to the public wastewater network across four Brazilian municipalities, weighing social (health), economic (tariff revenue/investment), and environmental (sludge diversion) criteria",
    population="365,000+ non-connected residents across four Minas Gerais municipalities (BBCR)",
    sample_size="4-municipality regulatory impact assessment, ~3.85 million people under ARSAE jurisdiction with wastewater coverage",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", enforcement="TRUE", fees="TRUE", discretion="TRUE",
    formal_connection="TRUE", sanitation_access="TRUE", service_coverage="TRUE",
    effect_measure="multiple criteria decision analysis (MACBETH), sensitivity/robustness/cost-benefit analysis of regulatory policy scenarios",
    effect_estimate="Despite Brazil's national (Federal Law 11445/2007) and Minas Gerais state (Law 13317/1999) legal mandates requiring household connection to available public wastewater networks, these legal requirements have not been effectively enforced, leaving a persistent household-connection gap (up to 42% of the urban population without wastewater-network access in the Belo Horizonte metropolitan region); the regulatory impact assessment identifies 'advanced infrastructure diffusion' (a 75% reduction in non-connected households, achievable by 2023 at a cost of BRL 33 million and generating an estimated BRL 42 million surplus in tariff revenue) as the optimal regulatory policy option, projected to reduce sludge disposed of in watercourses by 17,414 tons annually and improve waterborne-disease avoidance by 12.5%, demonstrating that specific regulatory-enforcement policy design directly determines the scale of achievable household wastewater-connection gains under an existing but under-enforced legal mandate.",
    table="Table 1 (aspects of all policy alternatives, 2017-2026); Figures 3-5 (value functions, overall policy-option scores, cost-benefit analysis)",
    study_design="ex-ante regulatory impact assessment (multiple criteria decision analysis, MACBETH method) with stakeholder focus group",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="Moderate: prospective regulatory-scenario modeling directly linking a specific national/state legal household-connection mandate and its regulatory-enforcement policy options to projected household wastewater-connection and associated health/environmental outcomes, though based on ex-ante MCDA scenario projections rather than an observed causal estimate.",
    source_document="de Carvalho, Costa, Marques & Netto 2019, Water Science and Technology (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established regulatory-impact-assessment/institutional-design inclusion precedent (Reynaud France; Nyarko Ghana PPP): original MCDA regulatory impact assessment directly linking a specific national/state legal household-connection mandate and its enforcement-policy design to projected household wastewater-access outcomes. NOT effect_sizes eligible: ex-ante scenario-modeling/MCDA analysis, not an observed regression-based causal estimate. Extracted for record_id R721DC414A085.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
