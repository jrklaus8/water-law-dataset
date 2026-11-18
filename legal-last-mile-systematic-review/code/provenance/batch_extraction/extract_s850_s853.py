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

# S850 - Aiga & Umenai - Impact of water supply improvement, Manila (ZIP legalization)
add("S850",
    citation="Aiga H, Umenai T (2002). Impact of improvement of water supply on household economy in a squatter area of Manila. Social Science & Medicine.",
    doi="10.1016/S0277-9536(01)00192-7",
    publication_year="2002",
    country="Philippines",
    subnational_unit="Manila (Leveriza and Maestranza squatter communities)",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="National Housing Authority (NHA) Zonal Improvement Program (ZIP); Manila water utility",
    regulatory_model="Comparative household-survey study (201 structured interviews plus focus groups) between a former squatter community formalized and upgraded under the Philippines' Zonal Improvement Program (Leveriza, LE), which converts illegal settlers into legal residents without relocation and installs private water connections, and a comparable squatter community still relying on illegal/informal public water faucets (Maestranza, MA); multiple regression with adjusted household income per capita as dependent variable and type of water supply as a significant predictor",
    population="households in the Leveriza and Maestranza squatter communities of Manila",
    sample_size="201 structured household interviews plus focus group discussions (7 participants per group)",
    household_level="TRUE", community_level="TRUE", tenure_status="TRUE",
    legal_status="TRUE", documentation="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE", service_quantity="TRUE",
    effect_measure="comparative household survey with multiple regression (adjusted household income per capita as dependent variable)",
    effect_estimate="Under the Zonal Improvement Program, formerly illegal settlers become legal residents and gain access to private water connections; households in the ZIP-legalized community (LE) had significantly higher water consumption (p<0.01) and significantly lower water expenditure (p<0.01) than the informal public-faucet community (MA); type of water supply was a significant predictor (p<0.01) of adjusted household income per capita in multiple regression, and the proportion of LE households below the poverty threshold fell from 55.6% to 29.9% as 72.1% of households formerly responsible for water collection began working for additional income using time freed by the improved, legally-connected water supply",
    study_design="comparative household survey with multivariate regression",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: a structured 201-household comparative survey directly linking a specific national legal-recognition/tenure-regularization program (ZIP) and its resulting formal water connections to quantified household economic outcomes, with multivariate regression controlling for confounders.",
    source_document="Aiga & Umenai 2002, Social Science & Medicine (retrieved via Google Drive)",
    table="Table 3 (multiple regression results)",
    section="Methods; Results; Discussion",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: rigorous comparative household-survey study directly documenting a specific legal-recognition/tenure-regularization program (Zonal Improvement Program) converting illegal settlers to legal residents with formal water connections. NOT effect_sizes eligible per the strict Family A/B/C framework (PROJECT_SPEC.md Section 8): the regression's dependent variable is adjusted household income per capita (an economic outcome), with water-supply type as the independent/exposure variable rather than water access itself as the outcome -- paralleling the S794/S822/S837 precedent of regression outcomes falling outside Family A's outcome definition (formal connection, water/sanitation access, quantity, reliability). Extracted for record_id R916889165AD5.",
    )

# S851 - Post - Home Court Advantage, Argentina water sector
add("S851",
    citation="Post AE (2014). Home Court Advantage: Investor Type and Contractual Resilience in the Argentine Water Sector. Politics & Society.",
    doi="10.1177/0032329213512981",
    publication_year="2014",
    country="Argentina",
    subnational_unit="14 subnational water privatization concessions (including Corrientes province)",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="water privatization concessionaires (multinational and domestic investor consortia)",
    regulatory_model="Comparative institutional case study of 14 Argentine water privatization contracts, testing whether domestic investors (versus multinational investors) are better able to negotiate mutually beneficial informal adaptations to formal concession contracts with host governments due to cross-sector market embeddedness, examining in detail the Corrientes province concession's transition from a multinational-led (Sideco) to a domestically-owned (Chamas brothers) consortium",
    population="households served by the 14 water privatization concessions across Argentina",
    sample_size="14 water privatization contracts; detailed case study of the Corrientes concession 1991-2001",
    household_level="", community_level="TRUE",
    institutional_fragmentation="TRUE", enforcement="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE", service_coverage="TRUE",
    effect_measure="comparative institutional case study with quantified coverage statistics",
    effect_estimate="Under the multinational-led (Sideco) ownership of the Corrientes concession (1992-1995), investment averaged only 4% of revenues amid conflict with the provincial regulator; after the domestically-owned Chamas-brothers consortium took over (1996-2000) and developed a more workable relationship with the provincial administration (including permitting a household census to improve billing), investment rose to 13% of revenues and water coverage rose from 66% to 90% while sewerage coverage rose from 31% to 68% over 1991-2001, demonstrating that domestic investor embeddedness in host-country institutions is associated with contractual resilience and expanded household-level water/sanitation access",
    study_design="comparative institutional case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: detailed comparative analysis of 14 water privatization contracts with a specific documented case (Corrientes) directly linking a change in investor type/institutional embeddedness to quantified household-level water/sewerage coverage outcomes.",
    source_document="Post 2014, Politics & Society (retrieved via Google Drive)",
    section="The Corrientes case: from Sideco to the Chamas brothers",
    exact_location="pp. 120-122",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: comparative institutional case study of water privatization concession contracts directly documenting a specific investor-type/contractual-governance mechanism and its quantified effect on household-level water/sewerage coverage. NOT effect_sizes eligible: comparative case study across 14 contracts without a formal regression model, no p-values or coefficients reported. Extracted for record_id R8EF694ACCE60.",
    )

# S852 - Narsiah & Ahmed - Neoliberalization of Water and Energy Sectors, South Africa/India
add("S852",
    citation="Narsiah S, Ahmed W (2012). The Neoliberalization of the Water and Energy Sectors in South Africa and India. Journal of Asian and African Studies.",
    doi="10.1177/0021909611429922",
    publication_year="2012",
    country="South Africa; India",
    subnational_unit="Dolphin Coast, Nelspruit, Stutterheim, Fort Beaufort, Queenstown (South Africa municipalities); national (India electricity sector)",
    legal_system="common law (South Africa); common law (India)",
    urban_rural="urban",
    service_provider="private water-services providers under South African municipal contracts (SAUR, Biwater-Nuon, Suez-Lyonnaise)",
    regulatory_model="Comparative political-economy case study examining South Africa's Water Services Act 1997 and National Water Act 1998, specifically the statutory provision permitting water-services authorities to contract with private-sector providers, and documenting the resulting municipal water-privatization contracts (Dolphin Coast/SAUR 1998, Nelspruit/Biwater-Nuon, Stutterheim/Fort Beaufort/Queenstown/Suez-Lyonnaise) and their subsequent collapse, alongside a parallel analysis of India's Electricity Act 2003 and energy-sector neoliberalization (based partly on original interviews)",
    population="residents of South African municipalities engaging privatized water services",
    sample_size="documentary/legal-text case analysis of multiple municipal water-privatization contracts, supplemented by original interviews (India electricity sector)",
    household_level="", community_level="TRUE",
    legal_status="TRUE", fees="TRUE", institutional_fragmentation="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE",
    effect_measure="comparative institutional/legal-text case study",
    effect_estimate="South Africa's Water Services Act (1997) contains a specific statutory provision enabling municipal water-services authorities to contract with private-sector providers; several municipalities used this provision to privatize water services (Dolphin Coast with SAUR in 1998, Nelspruit with Biwater-Nuon, and Stutterheim/Fort Beaufort/Queenstown with Suez-Lyonnaise during the 1990s), but all of these privatization arrangements were 'beset with major difficulties' and subsequently collapsed, illustrating a state-market logic embedded directly in post-apartheid water legislation that has undermined the state's own goals of equitable water-services delivery to the poor",
    study_design="comparative institutional/legal-text case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: direct legal-text analysis of a specific statutory provision (Water Services Act 1997) enabling water privatization, combined with documentation of multiple named municipal case outcomes resulting from its use.",
    source_document="Narsiah & Ahmed 2012, Journal of Asian and African Studies (retrieved via Google Drive)",
    section="Neoliberalization of the Water Sector in South Africa",
    exact_location="pp. 682-684",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: comparative institutional/legal case study directly analyzing a specific South African statutory provision (Water Services Act 1997) enabling water privatization and its documented municipal-level outcomes. NOT effect_sizes eligible: legal-text/documentary case study, no regression-based estimate. Extracted for record_id R92E20B0729D7.",
    )

# S853 - Gomez, Perdiguero & Sanz - Socioeconomic factors affecting rural water access
add("S853",
    citation="Gomez M, Perdiguero J, Sanz A (2019). Socioeconomic Factors Affecting Water Access in Rural Areas of Low and Middle Income Countries. Water.",
    doi="10.3390/w11020202",
    publication_year="2019",
    country="multiple (low, lower-middle, and upper-middle income countries, global panel)",
    subnational_unit="national (rural areas)",
    legal_system="mixed (multi-country panel)",
    urban_rural="rural",
    service_provider="not applicable (cross-national panel study of national governance/institutional capacity)",
    regulatory_model="Cross-national panel regression analysis using World Bank Worldwide Governance Indicators (rule of law, voice and accountability, political stability, control of corruption, government effectiveness, regulatory quality, converted to categorical 'weak'/'very weak' governance dummy variables) alongside socioeconomic factors (GNI, female primary completion, agriculture share of GDP, rural population growth, development aid) as predictors of rural water access (total improved, piped on premises, other improved sources), with robust standard errors for autocorrelation/heteroskedasticity",
    population="rural populations of low, lower-middle, and upper-middle income countries globally",
    sample_size="cross-national panel data, N=1691 (total improved model), N=1076 (piped on premises model), N=1573 (other improved sources model)",
    household_level="", community_level="TRUE",
    institutional_fragmentation="TRUE", enforcement="TRUE",
    water_access="TRUE", service_quality="TRUE",
    effect_measure="panel regression with robust standard errors, coefficients reported by governance-indicator category",
    effect_estimate="Weak regulatory quality is associated with significantly lower rural piped-water-on-premises access (coefficient -2.252, p<0.01) relative to strong regulatory quality; weak rule of law (-1.296, p<0.1), very weak rule of law (-3.932, p<0.05), weak voice/accountability (-2.429, p<0.01), very weak voice/accountability (-3.397, p<0.05), and very weak government effectiveness (-9.874, p<0.01) are also significantly associated with reduced piped-on-premises access, indicating that multiple dimensions of governance/institutional capacity are significant, largely independent predictors of rural piped-water access even controlling for GNI, agriculture, female education, and rural population growth",
    study_design="cross-national panel regression study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="2", outcome_measurement_quality="1",
    mechanism_certainty="Moderate-high: a large cross-national panel regression with robust standard errors directly isolating multiple institutional/governance-quality dimensions (rule of law, regulatory quality, voice/accountability, corruption control) as significant predictors of a clean water-access outcome (piped water on premises), though the governance indicators are broad, perception-based composite indices rather than a single documented legal/institutional mechanism (specific law, eligibility rule, or connection policy).",
    source_document="Gomez, Perdiguero & Sanz 2019, Water (retrieved via Google Drive)",
    table="Table 3 (piped water sources regression results)",
    section="3. Results",
    exact_location="Table 3",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: rigorous cross-national panel regression directly isolating institutional/governance-quality indicators as significant predictors of piped-water-on-premises access, a clean Family A-aligned outcome. NOT effect_sizes eligible per the strict Family A/B/C framework (PROJECT_SPEC.md Section 8): the exposure (World Bank Worldwide Governance Indicators) is a broad, perception-based composite governance index rather than a specific documented legal/institutional mechanism (legal recognition, tenure, documentation, or administrative barrier) as Family A/B/C require -- paralleling this batch-cycle's S841 (Ghana institutional trust) precedent of an exposure-side mismatch despite outcome-side eligibility. Extracted for record_id R6EA0A0277A0E.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
