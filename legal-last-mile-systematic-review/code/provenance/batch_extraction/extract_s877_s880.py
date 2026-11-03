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

# S877 - Miller - Watering the Garden of Tangier
add("S877",
    citation="Miller SG (2000). Watering the garden of Tangier: colonial contestations in a Moroccan city. The Journal of North African Studies.",
    doi="10.1080/13629380008718410",
    publication_year="2000",
    country="Morocco",
    subnational_unit="Tangier (international zone)",
    legal_system="mixed (Moroccan makhzan administration, international Sanitary Council, European concession law)",
    urban_rural="urban",
    service_provider="traditional conduit system administered by local Moroccan authorities; later an international Sanitary Council and an English water concession",
    regulatory_model="Historical institutional case study using primary/archival sources (traveler accounts, chronicles, diplomatic correspondence) documenting late-nineteenth/early-twentieth-century contestation over control of Tangier's water supply between European colonial 'sanitary modernizer' ideology (municipal regulation introduced in the 1880s, an international Sanitary Council originally formed to impose quarantine, and a lucrative English water concession pursued amid diplomatic rivalry) and indigenous Islamic/Moroccan religious-cultural water practices and makhzan administration",
    population="residents of Tangier, Morocco, late 19th-early 20th century",
    sample_size="historical documentary case study (archival/primary sources)",
    household_level="FALSE", community_level="TRUE",
    legal_status="TRUE", institutional_fragmentation="TRUE", enforcement="TRUE",
    formal_connection="TRUE", water_access="TRUE",
    effect_measure="historical documentary institutional case study",
    effect_estimate="Control over Tangier's water supply became a specific object of colonial-era institutional contestation: European residents and reformers pushed for municipal sanitary regulation (introduced in the 1880s) and pursued an English concession for water-system development, provoking diplomatic rivalry among European powers, while an international Sanitary Council (initially formed to enforce quarantine against cholera) extended its institutional reach into water-supply oversight; makhzan (Moroccan state) officials did not respond to modernization pressure with the alacrity reformers sought, reflecting indigenous religious/cultural water practices (ritual purity requirements, running-water primacy) that shaped resistance to externally imposed institutional control, illustrating how colonial-era concession and sanitary-council institutions directly contested traditional authority over urban water access and distribution",
    study_design="historical institutional case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: detailed historical documentary analysis using primary/archival sources directly documenting specific colonial-era institutional mechanisms (municipal sanitary regulation, an English water concession, an international Sanitary Council) contesting traditional authority over urban water distribution.",
    source_document="Miller 2000, Journal of North African Studies (retrieved via Google Drive)",
    section="Water Sacred and Foul; A Source of Scarcity and Abundance",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established historical-institutional-case-study inclusion precedent (S840 Grant, Nashville; S863 Liu Haiyan, Tianjin; S871 Ogle, 19th-c. American cities): historical documentary case study directly documenting colonial-era concession/sanitary-council institutional mechanisms contesting traditional water-access authority. NOT effect_sizes eligible: historical documentary case study, no regression-based estimate. Extracted for record_id R131D9C683C29.",
    )

# S878 - Spronk - Roots of Resistance to Urban Water Privatization, Bolivia
add("S878",
    citation="Spronk S (2007). Roots of Resistance to Urban Water Privatization in Bolivia: The 'New Working Class,' the Crisis of Neoliberalism, and Public Services. International Labor and Working-Class History.",
    doi="",
    publication_year="2007",
    country="Bolivia",
    subnational_unit="Cochabamba and El Alto/La Paz",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="Aguas de Tunari (Cochabamba, privatized 1999); Aguas del Illimani (La Paz-El Alto, privatized 1997)",
    regulatory_model="Comparative case-study analysis (informed by fieldwork and secondary documentary sources) of Bolivia's 1985 New Economic Policy structural-adjustment programme and subsequent 'capitalization' legal framework that privatized the municipal water utilities of Cochabamba (1999, Aguas de Tunari/Bechtel-led consortium) and La Paz-El Alto (1997, Aguas del Illimani/Suez-led consortium), examining the class composition and internal tensions of the territorially-based coalitions (the Coordinadora in Cochabamba, the Federacion de Juntas Vecinales in El Alto) that organized resistance to these specific privatization contracts",
    population="urban residents of Cochabamba and El Alto/La Paz, Bolivia",
    sample_size="two comparative case studies of urban water-privatization resistance movements",
    household_level="FALSE", community_level="TRUE",
    legal_status="TRUE", fees="TRUE", enforcement="TRUE", participation="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE",
    effect_measure="comparative case-study analysis",
    effect_estimate="Bolivia's 1985-2005 neoliberal structural-adjustment/capitalization legal framework produced specific municipal water-utility privatization concession contracts in Cochabamba (1999) and La Paz-El Alto (1997) that provoked large-scale, territorially-based (rather than trade-union-based) resistance coalitions; the study finds that five years after the Cochabamba Water War, internal tensions emerged within the resistance coalition between consumer interests (lowering water prices/tariffs) and worker interests (wages and working conditions of utility employees), with the paper arguing that a narrow focus on consumption/access issues at the expense of labor conditions risks weakening the broader working-class coalition capable of sustaining institutional change in water-service governance",
    study_design="comparative case-study analysis",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: comparative case-study analysis directly documenting two specific municipal water-privatization concession contracts under a national capitalization legal framework and the class-based coalition dynamics of resistance to them.",
    source_document="Spronk 2007, International Labor and Working-Class History (retrieved via Google Drive)",
    section="From State Capitalism to Neoliberalism; case studies of Cochabamba and El Alto",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established water-privatization-resistance case-study inclusion precedent: comparative case-study analysis directly documenting specific national capitalization-law-based municipal water-privatization concession contracts and organized institutional resistance to them. NOT effect_sizes eligible: comparative case-study analysis, no regression-based estimate. Extracted for record_id R0F7C649E8E07.",
    )

# S879 - Coville, Galiani, Gertler & Yoshida - Financing Municipal Water, Nairobi
add("S879",
    citation="Coville A, Galiani S, Gertler P, Yoshida S (2025). Financing Municipal Water and Sanitation Services in Nairobi's Informal Settlements. Review of Economics and Statistics.",
    doi="10.1162/rest_a_01379",
    publication_year="2025",
    country="Kenya",
    subnational_unit="informal settlements, Nairobi",
    legal_system="common law",
    urban_rural="urban",
    service_provider="Nairobi City Water and Sewerage Company (NCWSC)",
    regulatory_model="Randomized controlled field experiment (AEARCTR-0003556) testing two interventions by Nairobi's water utility among property owners in informal settlements with last-mile piped-water/sanitation connection loans and significant payment arrears: (i) face-to-face engagement encouraging payment, and (ii) systematic contract enforcement (transparent, credible disconnection notices for nonpayment as specified in the property owners' connection-loan contract), using five years of daily administrative billing data plus household/property-owner survey data collected nine months post-intervention",
    population="property owners and tenants of compounds with utility-financed last-mile water/sanitation connections in Nairobi informal settlements",
    sample_size="randomized field experiment; engagement and enforcement arms with administrative billing panel data (2014-2018) and survey follow-up (96 disconnected compounds among the enforcement-treated group)",
    household_level="TRUE", community_level="TRUE",
    fees="TRUE", enforcement="TRUE", disconnection="TRUE", reconnection="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_continuity="TRUE", affordability="TRUE",
    effect_measure="randomized controlled trial, regression-based intent-to-treat estimates",
    effect_estimate="Contract enforcement (transparent disconnection notices for nonpayment) increased the likelihood of payment within one month by 30 percentage points from an 11-percentage-point control base (p<0.001) and increased total payments by US$8.80 from a US$5.02 base (p<0.001); face-to-face engagement had a precisely estimated null effect on payment. Nine months after enforcement, piped water and sanitation connection rates were statistically indistinguishable between treatment and control compounds (most of the 96 disconnected compounds were reconnected after a partial payment or payment plan); use of piped water as the main water source was 4.4 percentage points higher among treated households but not significant (p=0.243); water spending (Control US$6.62 vs. Treatment US$6.86, p=0.803) and time spent collecting water (Control 118 min vs. Treatment 100 min, p=0.388) showed no significant difference; no significant effects were found on perceptions of service fairness/quality, tenant-property-owner relationships, or tenant psychological well-being.",
    study_design="randomized controlled trial",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: a randomized field experiment with administrative billing panel data and follow-up survey directly isolating a specific contractual/legal enforcement mechanism (service disconnection for nonpayment) and its effect on payment behavior and directly measured household water-access outcomes.",
    source_document="Coville, Galiani, Gertler & Yoshida 2025, Review of Economics and Statistics; NBER Working Paper 27569 (retrieved via Google Drive)",
    table="Tables 4-7",
    section="Results; Water Access and Use",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md. EFFECT_SIZES ELIGIBLE (Family C: legal/administrative barriers and access inequality): randomized controlled trial isolating a specific contractual enforcement mechanism (transparent disconnection-for-nonpayment notices) with directly measured water-access outcomes (piped connection rates, main water source, water spending, collection time), finding a precisely estimated null effect on access nine months post-intervention despite a strong positive effect on payment compliance. Extracted for record_id R4D81D56EA98B.",
    )

# S880 - Gero & Willetts - WASH markets, local government
add("S880",
    citation="Gero A, Willetts J (2020). Securing a conducive environment for WASH markets: The role of local government. Waterlines.",
    doi="10.3362/1756-3488.18-00026",
    publication_year="2020",
    country="Vietnam; Cambodia; Indonesia",
    subnational_unit="multiple provincial/district local governments",
    legal_system="civil law",
    urban_rural="both",
    service_provider="small-scale private/social WASH enterprises operating under local-government licensing, regulation and subsidy arrangements",
    regulatory_model="Qualitative political-economy study combining semi-structured interviews with rural water-supply enterprises, sanitation entrepreneurs, NGOs and local government officials across Vietnam, Cambodia and Indonesia, examining the institutional/regulatory roles local governments play in facilitating (or constraining) small-scale WASH markets -- including licensing and registration requirements, quality-standards monitoring/accreditation, targeted subsidies to facilitate access for the poor and disadvantaged, and the state's Human Right to Water and Sanitation (HRTWS) obligations even where service delivery is delegated to private enterprises",
    population="small-scale WASH enterprises, local government officials and NGOs in Vietnam, Cambodia and Indonesia",
    sample_size="semi-structured interviews with enterprises, NGOs and government officials across three countries",
    household_level="FALSE", community_level="TRUE",
    documentation="TRUE", fees="TRUE", enforcement="TRUE", discretion="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE", affordability="TRUE",
    effect_measure="qualitative interview-based political-economy study",
    effect_estimate="Local governments were found to play critical but under-recognised institutional roles in enabling small-scale WASH markets -- including training/business-development support, linking demand and supply, supporting entrepreneur associations, providing targeted subsidies/financing to facilitate access for the poor and disadvantaged, and setting/monitoring quality standards and accreditation -- but faced constraints including lack of role clarity, inadequate skills/capacity, and a widespread perception (among both government and enterprises) that WASH market systems should arise spontaneously without government involvement, resulting in gaps between the state's formal Human Right to Water and Sanitation obligations and actual local regulatory practice",
    study_design="qualitative interview-based political-economy study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: multi-country semi-structured interview study directly documenting specific local-government regulatory/institutional mechanisms (licensing, subsidies, quality standards, HRTWS obligations) affecting small-scale WASH-market access outcomes.",
    source_document="Gero & Willetts 2020, Waterlines (retrieved via Google Drive)",
    section="Local government roles in facilitating markets; Results",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established institutional/regulatory-mechanism inclusion precedent: multi-country semi-structured interview study directly documenting specific local-government regulatory mechanisms (licensing, subsidies, quality standards) affecting WASH-market access. NOT effect_sizes eligible: qualitative interview study, no regression-based estimate. Extracted for record_id R063CE14907E2.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
