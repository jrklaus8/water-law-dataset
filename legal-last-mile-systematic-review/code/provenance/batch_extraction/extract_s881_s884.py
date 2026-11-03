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

# S881 - Brown - Reforming the Urban Environment, Germany 1870-1910
add("S881",
    citation="Brown JC (1987). Reforming the Urban Environment: Sanitation, Housing, and Government Intervention in Germany, 1870-1910 (dissertation summary). The Journal of Economic History.",
    doi="",
    publication_year="1987",
    publication_type="dissertation summary",
    country="Germany",
    subnational_unit="Basel (Switzerland, comparative hedonic analysis) and Prussian cities more broadly",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="municipal governments and privately financed/franchised waterworks",
    regulatory_model="Historical econometric dissertation combining (a) hedonic analysis of a 600-apartment 1889 Basel housing census to test for rental-market segmentation by class, and (b) a median-voter model of municipal waterworks-investment decisions exploiting Prussia's wealth-weighted electoral franchise (post-1848 three-class voting system) to identify the political-economy determinants of the diffusion of sanitary infrastructure (waterworks) across Prussian cities from 1867 (post-cholera) onward",
    population="urban residents of Prussian/German cities and Basel, 1870-1910",
    sample_size="600-apartment hedonic housing sample (Basel, 1889); city-level waterworks-diffusion panel using Prussian electoral/tax records",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", fees="TRUE", formal_connection="TRUE",
    water_access="TRUE",
    effect_measure="historical econometric analysis (hedonic regression and median-voter model)",
    effect_estimate="A median-voter model exploiting Prussia's wealth-weighted three-class electoral franchise (which gave disproportionate political representation to the top 5-10% of the income distribution) found that the chief influences on municipal waterworks adoption even in the years just after the mid-century cholera epidemics were capacity costs, the income of the (wealth-weighted) median voter, and industrial-user demand; simulations suggested that rising inequality and this specific electoral-weighting legal framework together accounted for one- to two-thirds of the observed decline in city size at which waterworks were built over the period, demonstrating that a specific legal/institutional voting-rights structure directly shaped the political feasibility and timing of municipal water-infrastructure investment decisions",
    study_design="historical econometric case study (hedonic and median-voter models)",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: dissertation summary (not the full dissertation) describing a median-voter econometric model that directly exploits a specific documented electoral-franchise legal mechanism (Prussia's wealth-weighted three-class voting system) to explain municipal waterworks-investment decisions, though without full published coefficient tables in this summary format.",
    source_document="Brown 1987, Journal of Economic History, Summaries of Dissertations (retrieved via Google Drive)",
    section="Reforming the Urban Environment: Sanitation, Housing, and Government Intervention in Germany, 1870-1910",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established historical-institutional/political-economy inclusion precedent (S840 Grant, Nashville; S871 Ogle, 19th-c. American cities): historical econometric analysis directly documenting a specific electoral-franchise legal mechanism shaping municipal water-infrastructure investment decisions. NOT effect_sizes eligible: this is a dissertation SUMMARY without full published coefficient/SE tables, so precise regression estimates cannot be extracted; the qualitative description of the median-voter model's findings is extracted for narrative synthesis only. Extracted for record_id RA420CEEC7E34.",
    )

# S882 - Mason - Household Resources and Water Security, Philippines
add("S882",
    citation="Mason LR (2014). Examining Relationships between Household Resources and Water Security in an Urban Philippine Community. Journal of the Society for Social Work and Research.",
    doi="10.1086/678923",
    publication_year="2014",
    country="Philippines",
    subnational_unit="Pinget, Baguio City",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="Baguio Water District (BWD)",
    regulatory_model="Mixed-methods study (randomly sampled household survey, N=396, plus 18 purposively sampled in-depth interviews) using multiple regression analysis to examine the association between financial, physical and social household resources and four water-security outcomes (consumption, perceived cleanliness, perceived ease, affordability), with household-level formal connection status to the municipal water utility (BWD) -- none/shared/own household connection -- as a key explanatory variable, documenting the PHP 10,000-14,000 (US$234-327) upfront cost (connection fee plus installation) required to obtain a household BWD connection",
    population="households in Pinget, an urban community in Baguio City, Philippines",
    sample_size="N=396 households (random sample) for survey; n=18 for in-depth interviews",
    household_level="TRUE", community_level="TRUE",
    fees="TRUE", formal_connection="TRUE",
    water_access="TRUE", service_quantity="TRUE", service_quality="TRUE", affordability="TRUE",
    effect_measure="multiple regression analysis (linear and logistic models), household survey",
    effect_estimate="Compared to households with no BWD connection, those with their own household BWD (formal utility) connection reported a 27.2% increase in liters-per-capita-per-day water consumption, a 0.35-standard-deviation higher perceived-cleanliness score, 2.16 times greater odds of reporting extreme ease of water access, and 2.76 times greater odds of reporting affordable water expenses (all statistically significant, p<.05 or better); households with only a shared/other BWD connection showed a 20.8% decrease in consumption but 2.71 times greater odds of affordability relative to no connection; the household BWD metered connection was found to have the most consistent positive association with water security across all four outcome measures, while the qualitative data documented the PHP 10,000-14,000 upfront cost of obtaining a connection as a major barrier for low-income households",
    study_design="mixed-methods household survey with multiple regression analysis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: randomly sampled household survey (N=396) with multiple regression models directly isolating formal household utility-connection status (a documented institutional/fee-based access mechanism) and its effect on four separately measured water-security/access outcomes, corroborated by qualitative interview data on the cost barrier to obtaining a connection.",
    source_document="Mason 2014, Journal of the Society for Social Work and Research (retrieved via Google Drive)",
    table="Table 4/5 (multiple regression results by outcome, as described in text)",
    section="Results; Discussion of key associations across models",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md. EFFECT_SIZES ELIGIBLE (Family A: legal recognition/formal connection and access): randomly sampled household survey with regression models isolating a specific documented institutional mechanism (formal BWD utility connection status, requiring a PHP 10,000-14,000 upfront fee) with directly measured water-access outcomes (consumption, cleanliness, ease, affordability), all four showing statistically significant positive effects. Extracted for record_id R59329720D787.",
    )

# S883 - Bukari, Authur & Zachary - Social Aspects of Groundwater, Wa West District, Ghana
add("S883",
    citation="Bukari FIM, Authur DD, Zachary P (2024). Social Aspects of Groundwater Use and Management in the Wa West District. Ghana Journal of Geography.",
    doi="10.4314/gjg.v16i2.5",
    publication_year="2024",
    country="Ghana",
    subnational_unit="Wa West District, Upper West Region",
    legal_system="common law",
    urban_rural="rural",
    service_provider="community-level groundwater point-source infrastructure (boreholes with hand pumps, dug wells), various donor-funded stakeholder organizations",
    regulatory_model="Mixed-methods study assessing groundwater governance and management institutional frameworks in rural Ghanaian communities against Ghana's National Water Policy and SDG 6 targets, examining an implicit (rather than deliberately separated) stakeholder governance framework for groundwater, and documenting accessibility (distance/waiting time) and affordability (unmetered, no rigorous tariff payment structure for donor-funded point sources) outcomes",
    population="rural households in Wa West District, Upper West Region, Ghana",
    sample_size="mixed-methods household-level survey and qualitative fieldwork across rural communities",
    household_level="TRUE", community_level="TRUE",
    institutional_fragmentation="TRUE", documentation="TRUE", fees="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE",
    effect_measure="mixed-methods descriptive study with policy-institutional analysis",
    effect_estimate="Groundwater governance in Wa West District operates through an implicit, largely unrecognized stakeholder framework rather than a deliberate institutional structure separating groundwater from surface-water governance, in contrast to Ghana's National Water Policy and SDG 6 targets; accessibility and affordability of groundwater were found to be close to meeting policy/standard expectations on average (e.g., WHO's 30-minute walking-time and 20-liters-per-person-per-day standards), but actual quantity of groundwater use fell below acceptable levels, and affordability of donor-funded, unmetered rural point sources lacks the rigorous tariff-payment structure found in urban piped systems (where 60% of urban households can afford metered water tariffs compared to only 32% of rural households, per prior research by the same author), illustrating a policy-practice gap in groundwater governance institutionalization",
    study_design="mixed-methods descriptive study with institutional/policy analysis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: mixed-methods fieldwork directly documenting the gap between Ghana's formal National Water Policy/SDG 6 institutional framework and actual implicit groundwater governance arrangements, with quantified accessibility/affordability outcomes for rural households.",
    source_document="Bukari, Authur & Zachary 2024, Ghana Journal of Geography (retrieved via Google Drive)",
    section="Materials and Methods; Results and Discussion",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established descriptive institutional/policy-gap inclusion precedent: mixed-methods fieldwork directly documenting the gap between formal national water policy and actual rural groundwater governance institutions, with quantified accessibility/affordability outcomes. NOT effect_sizes eligible: descriptive mixed-methods study, no regression-based estimate isolating a specific mechanism. Extracted for record_id R55280045A6D7.",
    )

# S884 - Estache & Grifell-Tatje - Mali Water Privatisation
add("S884",
    citation="Estache A, Grifell-Tatje E (2013). How (Un)Even was the Distribution of the Impacts of Mali's Water Privatisation across Stakeholders? The Journal of Development Studies.",
    doi="10.1080/00220388.2012.729046",
    publication_year="2013",
    country="Mali",
    subnational_unit="national (Energie du Mali service area)",
    legal_system="civil law",
    urban_rural="both",
    service_provider="Energie du Mali (EDM), transferred to French operator SAUR under a 2001 20-year concession contract, returned to public management within 5 years",
    regulatory_model="Quantitative ex-post welfare-distribution analysis (indicator duality and production-theory methodology, generalizing Grifell-Tatje & Lovell 2008 to a multi-output setting) using detailed regulator accounting data to decompose the economic value created (or destroyed) by Mali's 2001-2005 water/electricity utility privatisation concession contract with SAUR, and to quantify how that value was distributed across stakeholder groups: urban/rural users, intermediate suppliers, investors, workers (local and foreign), and taxpayers",
    population="Malian water/electricity utility (EDM) stakeholders: urban and rural users, workers, investors, taxpayers",
    sample_size="detailed regulator-collected accounting/operational data, 2001-2005 (Mali's SAUR concession period)",
    household_level="FALSE", community_level="TRUE",
    legal_status="TRUE", fees="TRUE", enforcement="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE",
    effect_measure="quantitative welfare-distribution decomposition analysis (indicator duality/production theory)",
    effect_estimate="Mali's 2001-2005 water/electricity privatisation concession contract with SAUR generated positive economic value overall, and most urban users, intermediate suppliers, investors and workers benefited from it; however, poor rural users gained substantially less than other stakeholder groups, and taxpayers experienced a net welfare loss; foreign workers and investors captured disproportionately larger benefits than local Malian counterparts, and the firm's owners captured a large share of the value created, likely through transfer pricing given their control over cost data for key intermediate inputs -- providing the first robust ex-post quantitative distributional assessment of an African water-privatisation experiment, directly documenting how a specific concession-contract legal mechanism produced highly uneven welfare effects across stakeholder groups, disadvantaging poor rural water users specifically",
    study_design="quantitative welfare-distribution decomposition analysis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: detailed regulator accounting-data-based decomposition analysis directly isolating a specific documented legal/contractual mechanism (Mali's 2001 SAUR water/electricity concession contract) and quantifying its differentiated welfare effects across stakeholder groups, including a specific quantified finding that poor rural users benefited far less than other groups.",
    source_document="Estache & Grifell-Tatje 2013, Journal of Development Studies (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established water-privatization distributional-impact inclusion precedent: rigorous quantitative ex-post analysis directly documenting a specific concession-contract legal mechanism's uneven welfare effects, disadvantaging poor rural users. NOT effect_sizes eligible: the welfare-decomposition (indicator duality/production theory) methodology does not produce a standard regression coefficient/SE/CI in the Family A/B/C sense required for pooling, though the finding itself is highly relevant to qualitative synthesis. Extracted for record_id RCA0676FFA182.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
