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

# S972 - Ponder & Omstedt - Detroit water crisis, municipal debt violence
add("S972",
    citation="Ponder CS, Omstedt M (2019). The violence of municipal debt: From interest rate swaps to racialized harm in the Detroit water crisis. Geoforum.",
    doi="10.1016/j.geoforum.2019.07.009",
    publication_year="2019",
    country="United States",
    subnational_unit="Detroit, Michigan",
    legal_system="common law",
    urban_rural="urban",
    service_provider="Detroit Water and Sewerage Department (DWSD), under federal court oversight (1977-2013) and, following the 2013 municipal bankruptcy, a state-appointed emergency manager",
    regulatory_model="Documentary/archival analysis (bond prospectuses, court records, financial consulting memoranda, news reporting) of the institutional and financial-legal mechanisms producing the Detroit Water and Sewerage Department's insolvency and subsequent mass household water shutoffs, tracing predatory interest rate swap deals (1998-2006) authorized under federal Judge Feikens' 35-year oversight, LIBOR-rate manipulation by contracting banks, the 2013 state-appointed emergency-manager bankruptcy process, and the racialized public narrative blaming delinquent residential customers rather than the swap debt",
    population="Detroit, Michigan water utility customers, disproportionately Black and low-income residents",
    sample_size="documentary/archival case-study analysis of DWSD financial and legal records, 1977-2016",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", discretion_accommodation="TRUE", enforcement="TRUE", disconnection="TRUE", fees="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE",
    effect_measure="documentary/archival case-study analysis of municipal debt-instrument legal mechanisms and their household water-access consequences",
    effect_estimate="Toxic interest rate swap deals authorized under 35 years of federal court oversight (1977-2013) generated $561 million in swap-related debt and, combined with mandated asset write-offs, rendered DWSD financially insolvent despite its underlying assets otherwise remaining comfortably solvent (absent these instruments, net position would have exceeded $1 billion per independent financial consultant analysis); rather than address this predatory-finance-driven insolvency, the state-appointed emergency manager (installed under Michigan's emergency-management law) authorized aggressive pursuit of a comparatively small $91.7 million in residential bill delinquencies, resulting in mass water shutoffs: 33,000 households in 2014, 23,200 in 2015, and 27,552 in 2016, disproportionately affecting Detroit's majority-Black, low-income population; a separate public-health study (Plum et al. 2017, cited) found significant correlations between block-level shutoff addresses and diagnoses of water-associated illness. The study demonstrates that a specific legal/financial institutional mechanism (interest rate swap contracts, federal court oversight, and emergency-manager bankruptcy authority) -- not household nonpayment behavior -- was the primary driver of a mass household water-access denial event with racially disparate impact.",
    figure="Fig. 1 (DWSD bond official statement); Fig. 2 (DWSD net assets with/without swap debt, 2006-2014)",
    study_design="documentary/archival case-study analysis of municipal financial and legal records",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: rigorous documentary/archival analysis directly tracing a specific financial-legal institutional mechanism (interest rate swap contracts, federal court oversight, state emergency-manager authority) to a quantified, racially disparate mass household water-access denial event (33,000+ shutoffs).",
    source_document="Ponder & Omstedt 2019, Geoforum (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, strong match to Family C framework: rigorous documentary case study directly linking a specific legal/financial institutional mechanism to mass household water-access denial with quantified racial disparity. NOT effect_sizes eligible: documentary/archival case-study analysis, no regression-based estimate isolating the mechanism (the cited Plum et al. 2017 correlation is a separate study's estimate, not this paper's own). Extracted for record_id R4818B7F566CE.",
    )

# S973 - Danesi, Passarelli & Peruzzi - Italy Galli Law water reform
add("S973",
    citation="Danesi L, Passarelli M, Peruzzi P (2007). Water services reform in Italy: its impacts on regulation, investment and affordability. Water Policy.",
    doi="10.2166/wp.2006.059",
    publication_year="2007",
    country="Italy",
    subnational_unit="national, 52 Optimal Territorial Areas (ATOs) covering 61% of the population",
    legal_system="civil law",
    urban_rural="both",
    service_provider="municipally owned enterprises (82.6% of operators) transitioning to aggregated Optimal Territorial Area (ATO) utilities under the 1994 Galli Law (Law 36/1994), with a marginal but growing role for joint-stock companies",
    regulatory_model="Policy/institutional analysis of the Galli Law's 1994 water-sector reform, which mandated aggregation of thousands of fragmented municipal water utilities into 91 Optimal Territorial Areas (ATOs) governed by revenue-cap regulation, tracing the reform's implementation status, its effects on investment levels in aging water/sewerage infrastructure (average infrastructure age 22-32 years, 42% network leakage), and the resulting tension between required capital investment and tariff affordability",
    population="Italian water and sewerage service customers, national and regional (North/Middle/South-Islands) comparison",
    sample_size="52 completed ATOs (35 million inhabitants, 61% of Italian population), 2002 national infrastructure and economic statistics",
    household_level="FALSE", community_level="TRUE",
    eligibility="TRUE", legal_status="TRUE", institutional_fragmentation="TRUE", fees="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE",
    effect_measure="policy/institutional impact analysis with national and regional infrastructure/tariff statistics",
    effect_estimate="A decade after the Galli Law's 1994 reform mandating aggregation of Italy's fragmented municipal water utilities into ATOs, population coverage for water supply reached 96% and for sewerage 84%, but wastewater treatment coverage remained only 73%, with substantial regional disparities (water/sewerage expenditure per capita far higher in the North than South/Islands) and aging infrastructure (network leakage of 42%, average infrastructure age 22-32 years); the reform's revenue-cap regulatory model, designed to fund a 20-30-year capital investment program to modernize this infrastructure, created a direct institutional tension between required investment levels and tariff affordability for households, with the study documenting an active political/regulatory debate over how much of the investment burden could be passed to consumers without compromising affordability. The study demonstrates that the specific legal/regulatory design of the Galli Law reform (revenue-cap tariff-setting, ATO aggregation) directly shapes both investment adequacy and the affordability of household water/sewerage access.",
    table="Table 1 (water systems indicators); Table 2 (sewerage systems indicators); Table 3 (wastewater plants indicators); Table 4 (regional expenditure); Table 6 (forms of water services management)",
    study_design="policy/institutional impact analysis with national infrastructure and economic statistics",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: original policy/institutional analysis directly tracing the Galli Law's regulatory reform design (revenue-cap tariff regulation, utility aggregation) to national and regional water-service coverage and affordability outcomes, using comprehensive infrastructure and economic statistics.",
    source_document="Danesi, Passarelli & Peruzzi 2007, Water Policy (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: original policy/institutional analysis directly linking a specific national water-sector legal reform (Galli Law 1994) to water/sewerage service coverage, investment, and affordability outcomes. NOT effect_sizes eligible: descriptive policy/institutional analysis with infrastructure statistics, no regression-based estimate isolating a single mechanism. Extracted for record_id R460B9BC74FA4.",
    )

# S974 - Kacker & Joshi - In the pipeline, Delhi informal settlement water governance
add("S974",
    citation="Kacker SD, Joshi A (2016). In the pipeline: the governance of water supply to urban informal settlements. International Development Planning Review.",
    doi="10.3828/idpr.2016.15",
    publication_year="2016",
    country="India",
    subnational_unit="Sangam Vihar, an unauthorised settlement, New Delhi",
    legal_system="common law",
    urban_rural="urban",
    service_provider="informal small-scale private bore-well operators (Phase I), then resident-association-managed distribution from Delhi Jal Board (DJB) public tube wells (Phase II), with a proposed transition to DJB-contracted, regulated small-scale operators (Phase III)",
    regulatory_model="Exploratory field research (semi-structured interviews with 8 resident households and 4 private providers, 2007-2008, updated through 2015) tracing three phases in the evolving governance of water provision to Sangam Vihar, an unauthorised (illegal) settlement of 0.4-0.6 million residents at Delhi's periphery: an initial 'vicious cycle' of unregulated, profit-maximizing private bore-well operators exploiting captive customers; a 'claim-making' phase in which resident welfare associations leveraged electoral competition to secure DJB-built public tube wells and self-managed distribution networks; and an emerging 'virtuous cycle' phase of DJB-regulated contractual water provision",
    population="0.4-0.6 million residents of Sangam Vihar, an unauthorised settlement, New Delhi",
    sample_size="8 household interviews, 4 private-provider interviews, plus resident welfare association informants, 2007-2008 fieldwork updated through 2015",
    household_level="TRUE", community_level="TRUE",
    legal_status="TRUE", discretion_accommodation="TRUE", institutional_fragmentation="TRUE", participation="TRUE", fees="TRUE", procedural_steps="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE", service_reliability="TRUE",
    effect_measure="qualitative case-study analysis of institutional/political transitions in informal-settlement water-service governance",
    effect_estimate="Under the initial unregulated private-provider regime, service quality deteriorated over time as operators, facing detection risk and profit-maximization incentives, reduced supply duration from several hours to as little as 15-20 minutes per household daily while raising monthly charges to INR 250-300; following sustained collective claim-making by resident welfare associations leveraging local electoral competition (culminating in a 2003 assembly-election upset attributed to a water-access campaign), the Delhi Jal Board (DJB) established public tube wells and residents self-organized a community-managed distribution system, reducing user charges to INR 50/month with established, predictable supply schedules (versus the prior unregulated system's poor, variable predictability) -- see Table 1 comparison. The study demonstrates that shifts in the underlying legal/political-institutional status of water provision (from unregulated informal, to quasi-legal community-managed, toward formally regulated DJB-contracted provision) directly and measurably improved household water-access quality, predictability and affordability for a legally unauthorised settlement's residents.",
    table="Table 1 (comparison between private and community provision and management)",
    figure="Fig. 1 (the vicious circle); Fig. 2 (transition phase); Fig. 3 (the virtuous cycle)",
    study_design="exploratory qualitative case study with semi-structured interviews",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: original qualitative case study directly tracing the evolving legal/institutional status of water provision (unregulated informal -> quasi-legal community-managed -> DJB-regulated) to quantified improvements in household water-access predictability, quality, and affordability for a legally unauthorised settlement.",
    source_document="Kacker & Joshi 2016, International Development Planning Review (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Table 1, p. 265",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, strong match to Family A/B framework, consistent with the established informal-settlement governance-transition inclusion precedent: original qualitative case study directly linking institutional/legal-status transitions in water provision to quantified household access, cost, and reliability outcomes. NOT effect_sizes eligible: qualitative case study with descriptive before/after comparison, no regression-based estimate. Extracted for record_id R45FB2A780DA8.",
    )

# S975 - March & Sauri - Barcelona ecological modernization/debt water-cycle privatization
add("S975",
    citation="March H, Sauri D (2013). The unintended consequences of ecological modernization: debt-induced reconfiguration of the water cycle in Barcelona. Environment and Planning A.",
    doi="10.1068/a45380",
    publication_year="2013",
    country="Spain",
    subnational_unit="Metropolitan Barcelona, Catalonia",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="Agencia Catalana de l'Aigua (ACA, regional water-resource authority), Aigues Ter-Llobregat (ATLL, public bulk-water-supply company being leased to private consortia), Aigues de Barcelona (AGBAR/Suez Environnement, private retail water utility)",
    regulatory_model="Documentary/policy analysis (annual budgets of ACA, ATLL policy reports, official Catalan/Spanish legislation and budget laws, newspaper archives) tracing how EU environmental directives (Urban Wastewater Treatment Directive, Drinking Water Directive, Water Framework Directive) combined with EU budget-deficit rules and an inadequate water-tax-only financing model drove the Catalan Water Agency into EUR 1.5 billion debt, used as the discursive and legal justification for a 50-year private lease of the public bulk-water-supply company ATLL and for steep water-tax/tariff increases (9.5% in 2011, with a proposed path toward EUR 3.5/m3 full-cost recovery) shifting the cost burden onto households",
    population="4.5 million residents of Metropolitan Barcelona, Catalonia, Spain",
    sample_size="documentary/policy analysis of institutional annual budgets, legislation, and news archives, 2000-2012",
    household_level="FALSE", community_level="TRUE",
    legal_status="TRUE", discretion_accommodation="TRUE", fees="TRUE", institutional_fragmentation="TRUE", political_coordination="TRUE",
    formal_connection="TRUE", water_access="TRUE", affordability="TRUE",
    effect_measure="documentary/policy analysis of EU/national/regional legal-financial mechanisms and their tariff/affordability and governance consequences",
    effect_estimate="EU environmental directives required an estimated EUR 9.5 billion in Catalan water-cycle investment for 2010-2015, but the Catalan Water Agency's water-tax-only financing model covered only about half of expenditures on average, forcing reliance on short-maturity debt (five-year loans financing 25-30-year infrastructure) that by 2011 consumed 70% of water-tax revenue for debt service alone; this 'manufactured' debt crisis (EUR 1.5 billion ACA debt, EUR 679 million ATLL debt) was used to justify both a 50-year private lease of the public bulk-water-supply company ATLL (EUR 995.5 million) and a 9.5% 2011 water-tax increase with a proposed path toward full EUR 3.5/m3 cost recovery, while simultaneously restricting stakeholder participation in river-basin planning back to 'traditional' water users (excluding environmental, community, and consumer groups); the study demonstrates that a specific combination of EU legal mandates and an inadequate regional water-financing institutional design directly produced both increased household water-cost burden and reduced public-sector control over water-cycle governance and public participation.",
    table="Table 1 (investments in the water cycle for 2010-15)",
    figure="Fig. 3 (ACA long-term debt evolution); Fig. 6-7 (water-tax coverage of expenditures and debt repayment); Fig. 8 (price evolution 2000-10)",
    study_design="documentary/policy analysis of institutional budgets, legislation, and archival news sources",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: rigorous documentary/policy analysis directly tracing EU legal directives and Catalan water-financing institutional design to quantified household water-tariff increases and reduced public participation in water governance.",
    source_document="March & Sauri 2013, Environment and Planning A (retrieved via Google Drive)",
    section="Throughout",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established PSP/tariff-affordability institutional inclusion precedent (Reynaud France PSP/water affordability, Batch 183): rigorous documentary analysis directly linking EU legal mandates and regional water-financing institutional design to household tariff/affordability and governance-participation outcomes. NOT effect_sizes eligible: documentary/policy analysis with descriptive budget/tariff statistics, no regression-based estimate isolating a single mechanism. Extracted for record_id RA580E8237E5A.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
