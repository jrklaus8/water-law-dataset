#!/usr/bin/env python3
import csv
import os
import tempfile

REPO = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
DB = os.path.join(REPO, "02_screening/full_text/full_text_screening_database.csv")
EXLOG = os.path.join(REPO, "02_screening/exclusion_log/exclusion_log.csv")

REVIEWER = "Claude-AI-fulltext-2026-09-21"
DATE = "2026-09-22"

INCLUDES = {
    "R2621601881E4": "Genuine institutional/legal water-governance study explicitly examining "
        "\"legal provision for O&M\" under the Urban Councils Act Chapter 29:15, Water Policy 2012, "
        "and ZINWA Act Chapter 20:25 as a core parameter, with primary mixed-methods data collection "
        "across 11 local authorities in urban Zimbabwe tied to real WSS-status outcomes. "
        "Extracted for record_id R2621601881E4.",
    "R8D85A846848A": "Primary qualitative study (structured interviews + FGDs with 104 purposively "
        "sampled women with disabilities, plus 7 key-informant interviews) documenting institutional/"
        "policy-implementation gaps in Zimbabwe's National Disability Policy and constitutional "
        "provisions for equitable WASH access, tied to real household/individual-level WASH-access "
        "discrimination and harassment outcomes at community boreholes. "
        "Extracted for record_id R8D85A846848A.",
    "R4FB843E4946A": "Comparative institutional/legal analysis of public-private partnership models "
        "for water supply across Sub-Saharan Africa (Ivory Coast SODECI concession, Kenya kiosks, "
        "Senegal/Benin/Nigeria vendor markets) with real population-level coverage data (Table 1) and "
        "a primary household-level water-vendor consumption/pricing survey (Table 2, Zaroff & Okun "
        "1984) tied to institutional/regulatory arrangements (concession, affermage, licensing). "
        "Extracted for record_id R4FB843E4946A.",
    "R8D44D087F7A0": "Comparative institutional/legal analysis of water-sector ownership structures "
        "across four countries (England/Wales, Argentina, Cote d'Ivoire, Israel) with real household-"
        "level connection/coverage data (e.g. Buenos Aires 70%->83% connected) explicitly tied to "
        "legal/regulatory frameworks (1959 Israeli water law, concession contracts, independent "
        "regulatory agencies). Extracted for record_id R8D44D087F7A0.",
    "RC8B757CEFEBF": "Institutional/legal analysis of Sri Lankan urban water governance (Municipal "
        "Councils, NWSDB, Irrigation Department established by legislation) with real household-level "
        "connection/coverage/tariff data (76% urban connected, 40% standpost, income-tiered subsidy "
        "components) and explicit discussion of water rights and regulatory-body needs. "
        "Extracted for record_id RC8B757CEFEBF.",
    "R3A1A4F6F0CF5": "Institutional/legal analysis of Ghana's water-sector reforms under named Acts "
        "of Parliament (GWSC Act 310/1965, WRC Act 522/1996, PURC Act 538/1997) with real longitudinal "
        "coverage and tariff data (urban 76%->70%, rural 46%->30%) and explicit consumer-protection/"
        "vulnerable-group access provisions. Extracted for record_id R3A1A4F6F0CF5.",
}

EXCLUDES = {
    "RCFD40D935BC2": ("E01", "Institutional-governance-process case study of municipal sanitation "
        "(waste-collection) service-delivery-mode organizational change (NPM/PPP transitions) analyzed "
        "through public-administration theory; no household-level water/sanitation access outcome "
        "measured, extending the established service-delivery-mode E01 sub-pattern."),
    "RB22F274A2711": ("E01", "Primarily a qualitative study of kitchen social practices, diet, and "
        "cooking under a WEF-nexus-in-the-kitchen analytical lens; household water-sourcing/rationing/"
        "connection-cost content is one descriptive paragraph of background data with no legal or "
        "institutional analysis of water governance, following the Green & Blinkhorn incidental-topic "
        "precedent."),
    "RADD54B6C65E2": ("E05", "Opinion editorial (explicitly labeled 'OPINION EDITORIAL') presenting "
        "an ethical framework for managed retreat from centralized water systems; no original empirical "
        "data collection or analysis of its own, drawing only on the authors' prior published work and "
        "anecdote, following the established policy-commentary-essay E05 precedent."),
    "R85301EA43953": ("E01", "Qualitative descriptive gerontology/social-work study of internally "
        "displaced older adults' overall crisis experience during Ethiopia's armed conflict (food, "
        "shelter, sanitation supplies, health services, family disintegration, psychological stress); "
        "water/sanitation is one incidental hardship among many in a broader humanitarian-crisis study "
        "with no legal/institutional water-governance analysis."),
    "RC14288578517": ("E01", "UNICEF-sponsored National Sanitation Week program evaluation using "
        "social-mobilization/behavior-change methodology (IEC materials, mass media, village-level "
        "mobilization); a public-health promotion program report with no legal/institutional analysis "
        "of water/sanitation access barriers or governance frameworks."),
    "R9477DF8E814D": ("E01", "Framing paper for a special issue on postsocialist agrarian and "
        "environmental commons governance in Central/Eastern Europe (property-rights reform, common-"
        "pool resources including water AND landscape/agricultural resources); primary topic is general "
        "agrarian/environmental commons governance, not household water/sanitation access."),
    "R7A0CEC6E8A80": ("E01", "Study of gender dimensions of grassroots participation in Village "
        "Development Associations across diverse community-infrastructure projects (bridges, roads, "
        "school buildings, water supply, health centres) in Northwest Cameroon; water supply is one of "
        "several infrastructure types with no dedicated legal/institutional water-governance analysis."),
}

TITLES = {
    "R2621601881E4": ("Analysis of operation and maintenance arrangements for water supply in urban areas in Zimbabwe", "Hoko, Mapenzauswa, Toto, Kerith and Nhapi", "2024"),
    "RCFD40D935BC2": ("The rise and fall of an NPM-style reform in China: a longitudinal case study of sanitation service delivery in Guangzhou", "Chen, Chen and Mitchell", "2024"),
    "RB22F274A2711": ("Urban water-energy-food nexus in the kitchen and social practices of diet and cooking: implications for household sustainability", "Ahmed", "2025"),
    "RADD54B6C65E2": ("Ethical challenges of managed retreat from centralized water systems", "Wutich, Brewis, Thomson, Beresford, White and the Arizona Water for All Consortium", "2025"),
    "R8D85A846848A": ("Access to water, sanitation and hygiene facilities by women with disabilities in Zimbabwe's Harare Metropolitan Province during COVID-19", "Muridzo, Hungwe and Chadambuka", "2025"),
    "R85301EA43953": ('"Everything is Awful:" Experiences of Internally Displaced Older Adults During the Armed Conflict in Ethiopia', "Gebeyaw, Gashaw, Kasseye and Adamek", "2026"),
    "R4FB843E4946A": ("Public-private partnership in water supply and sanitation in sub-saharan Africa", "Lewis and Miller", "1987"),
    "R8D44D087F7A0": ("Changing ownership structures in the water supply and sanitation sector", "Chenoweth", "2004"),
    "RC8B757CEFEBF": ("Challenges to urban water management in Sri Lanka", "Seneviratne", "2000"),
    "R3A1A4F6F0CF5": ("Water Pricing and Water Sector Reforms Information Study in Ghana", "Gyau-Boakye and Ampomah", "2003"),
    "RC14288578517": ("Myanmar experiences in sanitation and hygiene promotion: Lessons learned and future directions", "Bajracharya", "2003"),
    "R9477DF8E814D": ("The commons in transition: Agrarian and environmental change in Central and Eastern Europe", "Sikor", "2004"),
    "R7A0CEC6E8A80": ("Grassroots participation for infrastructural provisioning in Northwest Cameroon: Are Village Development Associations the Panacea?", "Fonchingong and Ngwa", "2005"),
}

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

by_id = {r["record_id"]: r for r in rows}

for rid in list(INCLUDES) + list(EXCLUDES):
    assert rid in by_id, f"record_id {rid} not found"
    r = by_id[rid]
    assert not r["full_text_decision"] and not r["final_decision"], f"{rid} already decided"

for rid, note in INCLUDES.items():
    r = by_id[rid]
    r["full_text_decision"] = "include"
    r["final_decision"] = "include"
    r["full_text_status"] = "retrieved"
    r["reviewer_1"] = REVIEWER
    r["notes"] = note

for rid, (code, detail) in EXCLUDES.items():
    r = by_id[rid]
    r["full_text_decision"] = "exclude"
    r["final_decision"] = "exclude"
    r["full_text_status"] = "retrieved"
    r["reviewer_1"] = REVIEWER
    r["exclusion_reason"] = code
    r["exclusion_reason_detail"] = detail

fd, tmppath = tempfile.mkstemp(dir=REPO)
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmppath, DB)

# Append to exclusion_log.csv
with open(EXLOG, newline="", encoding="utf-8") as f:
    ex_reader = csv.DictReader(f)
    ex_fieldnames = ex_reader.fieldnames
    ex_rows = list(ex_reader)

for rid, (code, detail) in EXCLUDES.items():
    title, authors, year = TITLES[rid]
    ex_rows.append({
        "record_id": rid,
        "title": title,
        "authors": authors,
        "year": year,
        "stage": "full_text",
        "exclusion_code": code,
        "exclusion_reason_detail": detail,
        "reviewer": REVIEWER,
        "date": DATE,
    })

fd, tmppath = tempfile.mkstemp(dir=REPO)
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=ex_fieldnames)
    writer.writeheader()
    writer.writerows(ex_rows)
os.replace(tmppath, EXLOG)

print(f"Batch 124 recorded: {len(INCLUDES)} includes, {len(EXCLUDES)} excludes.")
print(f"exclusion_log.csv new total: {len(ex_rows)}")
