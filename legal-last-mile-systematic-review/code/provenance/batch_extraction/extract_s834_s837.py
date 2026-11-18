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

# S834 - Anand - Leaky States, Mumbai water audits (companion to S826)
add("S834",
    citation="Anand N (2015). Leaky States: Water Audits, Ignorance, and the Politics of Infrastructure. Public Culture.",
    doi="10.1215/08992363-2841880",
    publication_year="2015",
    country="India",
    subnational_unit="Mumbai",
    legal_system="common law",
    urban_rural="urban",
    service_provider="Mumbai Municipal Corporation water department",
    regulatory_model="Ethnographic study of Mumbai's water-audit politics amid a failed 2000s privatization/leak-reduction initiative, examining the same politically-mediated formal water-connection eligibility rule documented in the author's companion piece (a January 1995 settlement cutoff date, excluding roughly a million settlers from legitimate water-connection applications) and how water audits (measuring 'non-revenue water'/leakage) become sites of political contestation over infrastructure ignorance, class-differentiated water quotas, and scheduled intermittent supply",
    population="Mumbai water-department engineers, World Bank/consultant officials, and settlers in informal settlements",
    sample_size="ethnographic fieldwork with water-department engineers and settlers, beginning 2007",
    household_level="TRUE", community_level="TRUE", tenure_status="TRUE",
    eligibility="TRUE", documentation="TRUE", discretion="TRUE",
    formal_connection="TRUE", water_access="TRUE", service_quantity="TRUE", service_reliability="TRUE",
    effect_measure="ethnographic case study (interviews, participant observation)",
    effect_estimate="Confirms and extends the author's documented 1995 settlement-eligibility cutoff excluding roughly a million Mumbai settlers from legitimate water-connection applications; shows how a failed World Bank-backed privatization/water-audit initiative (aimed at reducing 'non-revenue water' through 24-7 metered supply) foundered on the same politically-mediated, unevenly-enforced eligibility and quota rules, with settlers continuing to receive smaller, more intermittent water quotas than residents of planned buildings, illustrating how infrastructural 'ignorance' about water quantities is itself a product of, and cover for, the same discretionary access-barrier politics",
    study_design="ethnographic case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: ethnographic fieldwork with both water-department officials and settlers directly documenting the same formal eligibility cutoff and discretionary quota-allocation practices as the author's companion 2011 study, examined through the lens of a failed privatization/audit reform.",
    source_document="Anand 2015, Public Culture (retrieved via Google Drive)",
    section="Introduction; water-audit politics and privatization failure",
    exact_location="Opening Haresh interview and subsequent analysis",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: companion ethnographic study to already-included S826 (Anand 2011, 'PoliTechnics of Water Supply in Mumbai'), directly documenting the same 1995 settlement-eligibility-cutoff rule for water connections and its discretionary, unevenly-enforced application, here examined through a failed privatization/water-audit reform initiative. NOT effect_sizes eligible: ethnographic case study, no regression-based estimate. Extracted for record_id R84FCE5A47D09.",
    )

# S835 - Peda, Argento & Grossi - Estonian mixed public-private water company
add("S835",
    citation="Peda P, Argento D, Grossi G (2013). Governance and Performance of a Mixed Public-Private Enterprise: An Assessment of a Company in the Estonian Water Sector. Public Organization Review.",
    doi="10.1007/s11115-013-0233-z",
    publication_year="2013",
    country="Estonia",
    subnational_unit="a large Estonian city (mixed public-private water company)",
    legal_system="civil law",
    urban_rural="urban",
    service_provider="a mixed public-private water/sewerage company, majority municipally owned",
    regulatory_model="Case study grounded in Estonia's Public Water Supply and Sewerage Act, examining the governance and performance of the country's largest water company under a partial 2001 privatization (mixed public-private ownership), structured through a detailed 15-year service contract (97 specific performance levels, a K-coefficient tariff formula, quarterly/annual reporting obligations to a municipal supervisory authority), based on document review and face-to-face interviews with the company CEO, deputy mayor, a supervisory board member, and municipal officials",
    population="households and businesses served by the company's water/sewerage network",
    sample_size="document review plus face-to-face interviews with company CEO, deputy mayor, supervisory board member, and municipal officials",
    household_level="TRUE", community_level="TRUE",
    service_area="TRUE", fees="TRUE", administrative_review="TRUE",
    formal_connection="TRUE", water_access="TRUE", sanitation_access="TRUE",
    service_coverage="TRUE", service_reliability="TRUE", service_quality="TRUE", affordability="TRUE",
    effect_measure="institutional case study (contract/document review, semi-structured interviews)",
    effect_estimate="Under the mixed public-private ownership structure and detailed 15-year service contract (97 performance levels, K-coefficient tariff formula, quarterly/annual reporting to a municipal supervisory authority), the company achieved 99.7% water/sewerage coverage by 2010, kept household water bills at only 1.2-1.3% of disposable income through cross-subsidization from commercial customers, and reached 99.6% drinking-water-quality-sample compliance, illustrating how a specific contractual/regulatory governance mechanism sustained high household-level access, affordability, and service-quality outcomes",
    study_design="institutional/regulatory case study",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="1",
    mechanism_certainty="High: detailed documentary review of a specific 15-year service contract and its performance/tariff/reporting mechanisms, combined with interviews of the company CEO, deputy mayor, and supervisory board member, directly linking contractual governance design to quantified household-level coverage and affordability outcomes.",
    source_document="Peda, Argento & Grossi 2013, Public Organization Review (retrieved via Google Drive)",
    table="Service contract performance-level and tariff tables",
    section="Case description; governance mechanisms; performance results",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md, consistent with the established descriptive/regulatory-performance national-case-study precedent (S805 Kosova, S819 Chile, S830 Sao Paulo): detailed statutory/contractual governance analysis with quantified household-level coverage/affordability outcomes drawn from a specific 15-year service contract, supported by original interviews. NOT effect_sizes eligible: institutional case study, no regression-based estimate. Extracted for record_id R828C9773E407.",
    )

# S836 - Valencia & Ecuyer - Colombian post-conflict community water management
add("S836",
    citation="Valencia G, Ecuyer B (2023). La gestion comunitaria del agua en el posconflicto con las Farc-ep en Colombia [Community Water Management in the Colombian Post-Conflict]. Lecturas de Economia.",
    doi="10.17533/udea.le.n96a351422",
    publication_year="2023",
    country="Colombia",
    subnational_unit="16 PDET-prioritized post-conflict subregions",
    legal_system="civil law",
    urban_rural="rural",
    service_provider="community-based water-management associations (acueductos comunitarios)",
    regulatory_model="Documentary/policy analysis of official government post-conflict development-program data (PDET Development Programs with a Territorial Focus, their 16 PATR Action Plans for Regional Transformation, and 170 PMTR Municipal Pacts for Regional Transformation) examining drinking-water access and community water management across 16 prioritized post-conflict subregions, analyzing Colombia's Law 142 of 1994 (public services decentralization/market reform, which nominally recognizes community water associations but imposes undifferentiated regulatory requirements), Decree 1898 of 2016 (which defines community water systems only as temporary 'differentiated schemes' rather than a recognized permanent management model), and the 2017 popular legislative initiative for a community water self-management law (Ley Propia)",
    population="rural residents of 16 PDET post-conflict subregions relying on community-managed water systems",
    sample_size="documentary analysis of 16 PATR and 170 PMTR government program documents",
    household_level="", community_level="TRUE", legal_status="TRUE",
    eligibility="TRUE", documentation="TRUE", fees="TRUE", institutional_fragmentation="TRUE",
    formal_connection="TRUE", water_access="TRUE",
    effect_measure="documentary/policy analysis of national post-conflict development-program data",
    effect_estimate="Despite Law 142/1994 nominally recognizing community water-management associations, the absence of specific constitutional/legal recognition (reconocimiento juridico) of the community-management model -- reinforced by Decree 1898/2016's classification of community water systems as merely temporary 'differentiated schemes' -- leaves associations unable to formalize and access tariff subsidies or municipal-agreement funding; the analysis identifies legal recognition, alongside financial resources for community management and use of PDET investment contributions, as the three central challenges facing rural drinking-water access and community water governance in Colombia's post-conflict development",
    study_design="documentary/policy analysis using national government program data",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="Moderate-high: systematic documentary analysis of official government post-conflict program data (PATR/PMTR) across 16 subregions, combined with detailed legal-text analysis (Law 142/1994, Decree 1898/2016, the 2017 Ley Propia initiative) directly identifying the absence of legal recognition as a structural barrier to formalizing community water-management associations and their access to subsidies/funding.",
    source_document="Valencia & Ecuyer 2023, Lecturas de Economia (retrieved via Google Drive)",
    section="II. Analisis de resultados; III. Discusion: problematica de la gestion comunitaria del agua",
    exact_location="Section III.A (Falta de reconocimiento juridico) and Conclusiones",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: documentary/legal-policy analysis of official government post-conflict program data directly identifying the lack of legal recognition of community water-management associations as a structural access barrier, consistent with the established descriptive-regulatory-analysis inclusion precedent (S805 Kosova, S819 Chile, S828 Brazil WatSan law, S830 Sao Paulo). NOT effect_sizes eligible: documentary/policy analysis, no regression-based estimate. Extracted for record_id RA7ECB9D783C3.",
    )

# S837 - Scott, Moldogaziev & Greer - Houston special purpose water districts
add("S837",
    citation="Scott TA, Moldogaziev T, Greer RA (2018). Drink what you can pay for: Financing infrastructure in a fragmented water system. Urban Studies.",
    doi="10.1177/0042098017729092",
    publication_year="2018",
    country="United States",
    subnational_unit="Houston, Texas metropolitan statistical area",
    legal_system="common law",
    urban_rural="urban",
    service_provider="more than 500 special purpose water supply districts (Municipal Utility Districts, Water Control and Improvement Districts, Fresh Water Supply Districts)",
    regulatory_model="Quantitative panel study of institutional fragmentation, analyzing how local fiscal capacity (lagged revenues, fund balance) and area wealth (median home value) condition special purpose water districts' capital-investment/debt-issuance response to regulatory (Safe Drinking Water Act) violations, using hierarchical Bayesian regression models on district-level administrative/financial data (Texas Water District Database, Texas Bond Review Board, Safe Drinking Water Information System, American Community Survey)",
    population="households served by special purpose water districts in the fragmented Houston metro area",
    sample_size="panel data on 500+ special purpose water districts in the Houston metropolitan statistical area",
    household_level="", community_level="TRUE",
    institutional_fragmentation="TRUE", enforcement="TRUE",
    service_reliability="TRUE", service_quality="TRUE",
    effect_measure="hierarchical Bayesian regression (log-odds of debt issuance; additive log-dollar amount of capital financing), 95% credible intervals",
    effect_estimate="Institutional fragmentation among Houston's 500+ special purpose water districts does not impede capital-infrastructure investment in relatively affluent districts following regulatory violations, but districts in relatively less-affluent areas have significantly limited fiscal capacity to respond to service-delivery problems and violations with new capital investment/debt issuance, demonstrating that fragmented special-district governance structurally channels infrastructure-investment capacity toward wealthier areas",
    study_design="quantitative panel study with hierarchical Bayesian regression",
    risk_of_bias_tool="Legal Institutional Evidence Appraisal Framework",
    legal_measurement_quality="1", outcome_measurement_quality="2",
    mechanism_certainty="High: large administrative panel dataset (500+ districts) with a formal Bayesian regression model directly isolating how institutional fragmentation interacts with local fiscal/economic capacity to shape capital-investment responses to regulatory violations, though the outcome (capital investment/debt issuance) is a proxy for, rather than a direct measure of, household water-access/quality outcomes.",
    source_document="Scott, Moldogaziev & Greer 2018, Urban Studies (retrieved via Google Drive)",
    table="Table 1 descriptive statistics; Figure 1 credible-interval model results",
    section="Results: hierarchical Bayesian regression models",
    exact_location="Throughout",
    extraction_note="INCLUDE per INCLUSION_EXCLUSION.md: rigorous quantitative institutional-fragmentation study directly isolating how special-purpose-district governance and local fiscal capacity shape water-infrastructure capital investment following regulatory violations. NOT effect_sizes eligible per the strict Family A/B/C framework (PROJECT_SPEC.md Section 8): the regression outcome is capital investment/debt issuance (a fiscal-response proxy), not a water-access outcome (formal connection, water/sanitation access, quantity, reliability) isolated per PROJECT_SPEC.md's Family A definition -- paralleling the established S794 Vasquez and S822 Nolan/Bloom/Subbaraman precedents for outcome measures too far removed from or too composite relative to water access itself. Extracted for record_id R84FF08BBE70F.",
    )

fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EXTR))
with os.fdopen(fd, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in rows:
        w.writerow(row)
os.replace(tmp, EXTR)

print(f"New total: {len(rows)}")
