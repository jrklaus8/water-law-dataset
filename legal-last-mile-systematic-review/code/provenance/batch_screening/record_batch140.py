import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXLOG = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-23"
DATE = "2026-09-23"

with open(DB, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

by_id = {r["record_id"]: r for r in rows}

ids = [
    "R483391EAF0A4", "R124041F5DF16", "R3AEF33753AF3", "R5288473FC800",
    "R9741314656A3", "R53BDAFE46BDD", "R02C6DE366093", "R0C5D57C3EF0E",
    "RF3056823844E", "RF307BBEBB415", "R6884837E85A8", "R5DEFEB3CB256",
    "R761657E447C4", "RB6A1EB27E732", "R1F58000B5617", "R3C9D8DD0859C",
]
for rid in ids:
    assert by_id[rid]["full_text_decision"] == "", f"{rid} not open"
    assert by_id[rid]["final_decision"] == "", f"{rid} not open"

# ---- INCLUDES ----

# R483391EAF0A4 - Bakker 2005, Neoliberalizing Nature (England & Wales) - INCLUDE -> S686
r = by_id["R483391EAF0A4"]
r["full_text_status"] = "retrieved"
r["full_text_location"] = "Google Drive inbox (delivered PDF)"
r["full_text_decision"] = "include"
r["final_decision"] = "include"
r["reviewer_1"] = REVIEWER
r["notes"] = (
    "Legal/regulatory case study of England & Wales water privatization (1989) and subsequent "
    "reregulation, documenting real institutional/legal mechanisms directly affecting household "
    "access and affordability: the economic regulator (Ofwat)'s formal legal duty to protect "
    "consumers from discriminatory prices, a High Court ruling that prepayment water meters "
    "installed in low-income households were illegal, and new legislation enacted in response that "
    "increased legal protection against domestic disconnections. Ties specific legal/regulatory "
    "decisions to access/affordability outcomes for low-income consumers. Included per "
    "INCLUSION_EXCLUSION.md criteria 1-9. Extracted as S686."
)

# R9741314656A3 - Schusterman & Hardoy 1997, Barrio San Jorge, Buenos Aires - INCLUDE -> S687
r = by_id["R9741314656A3"]
r["full_text_status"] = "retrieved"
r["full_text_location"] = "Google Drive inbox (delivered PDF)"
r["full_text_decision"] = "include"
r["final_decision"] = "include"
r["reviewer_1"] = REVIEWER
r["notes"] = (
    "Ten-year longitudinal case study of an informal settlement (Barrio San Jorge, Buenos Aires) "
    "documenting a real institutional/legal transition: inhabitants acquiring legal land tenure, "
    "provision for water and sanitation moving from informal/self-organized arrangements to being "
    "formally managed by the official public utilities, achieved through the settlement's newly-"
    "formed representative community organization negotiating directly with government agencies "
    "and utilities. Extends the established Ofer 2009 Orcasitas (Madrid) precedent: illegal-"
    "settlement-to-legal-recognition-to-formal-utility-connection pathway. Included per "
    "INCLUSION_EXCLUSION.md criteria 1-9. Extracted as S687."
)

# R02C6DE366093 - Faisal & Kabir 2005, Gender-Water Nexus Bangladesh - INCLUDE -> S688
r = by_id["R02C6DE366093"]
r["full_text_status"] = "retrieved"
r["full_text_location"] = "Google Drive inbox (delivered PDF)"
r["full_text_decision"] = "include"
r["final_decision"] = "include"
r["reviewer_1"] = REVIEWER
r["notes"] = (
    "Primary field study (field survey, focus group discussions, key-informant interviews at seven "
    "study locations across Bangladesh) examining household and irrigation water access. Documents "
    "a real institutional/legal mechanism: the Government of Bangladesh's Guidelines for "
    "Participatory Water Management (Ministry of Water Resources, 2000) mandating that women, "
    "landless persons, sharecroppers and Project Affected Persons be included as members of Water "
    "Management Group/Association Executive Committees, contrasted with the field-documented reality "
    "of minimal actual women's participation in agricultural/irrigation water management institutions. "
    "Included per INCLUSION_EXCLUSION.md criteria 1-9. Extracted as S688."
)

# RF3056823844E - Allen, Davila & Hofmann 2006, peri-urban water poor - INCLUDE -> S689
r = by_id["RF3056823844E"]
r["full_text_status"] = "retrieved"
r["full_text_location"] = "Google Drive inbox (delivered PDF)"
r["full_text_decision"] = "include"
r["final_decision"] = "include"
r["reviewer_1"] = REVIEWER
r["notes"] = (
    "Comparative three-year primary research project (fieldwork, interviews, focus groups, transect "
    "walks, metropolitan-wide institutional analysis across five metropolitan areas: Mexico City, "
    "Caracas, Chennai, Dar es Salaam, Cairo) examining peri-urban poor residents' access to water and "
    "sanitation. Develops and applies a legal/institutional 'policy-driven' vs. 'needs-driven' "
    "framework (citizens with rights-based entitlements vs. consumers subject to market pricing), "
    "finding access is predominantly needs-driven/informal rather than governed by formal legal "
    "entitlement. Included per INCLUSION_EXCLUSION.md criteria 1-9. Extracted as S689."
)

# RF307BBEBB415 - Anand 2007, Semantics of Success (India/Chennai) - INCLUDE -> S690
r = by_id["RF307BBEBB415"]
r["full_text_status"] = "retrieved"
r["full_text_location"] = "Google Drive inbox (delivered PDF)"
r["full_text_decision"] = "include"
r["final_decision"] = "include"
r["reviewer_1"] = REVIEWER
r["notes"] = (
    "Institutional mapping and case study of drinking water supply in Chennai, India, combining "
    "national-level survey data (NSS 54th round, 1998) with a detailed institutional history: the "
    "Madras City Municipal Corporation Act 1919 assigning water/sanitation to local government, the "
    "1978 World-Bank-advised creation of a state water board (transferring the function away from "
    "elected local government), and a 1998 citizen's charter reform. Applies Sen's entitlements "
    "framework to household-level survey data on water endowment by income group, documenting large "
    "inequality (lowest-income households ~33 lpcd vs. highest-income ~152 lpcd) and worse outcomes "
    "in institutionally weak peri-urban areas. Included per INCLUSION_EXCLUSION.md criteria 1-9. "
    "Extracted as S690."
)

# R5DEFEB3CB256 - Jenson 2008, Sewers/sanitation & citizenship regimes (Britain) - INCLUDE -> S691
r = by_id["R5DEFEB3CB256"]
r["full_text_status"] = "retrieved"
r["full_text_location"] = "Google Drive inbox (delivered PDF)"
r["full_text_decision"] = "include"
r["final_decision"] = "include"
r["reviewer_1"] = REVIEWER
r["notes"] = (
    "Historical-institutional case study of nineteenth-century British public-health/sanitation law "
    "(Public Health Act 1848, Municipal Corporations Act 1835, New Poor Law 1834, Vaccination Act "
    "1853), documenting real differential sewer/water-connection outcomes: the 1848 Act left "
    "responsibility for water/sewer provision in the hands of private companies with few market "
    "incentives to connect the poor (who lacked ability to pay), so that 'except where the wealthier "
    "residents paid for it in their suburban villas, little effort... was devoted to connecting-up, "
    "en masse, individual homes' before the last quarter of the century (by 1846 only 10 of ~190 "
    "local authorities possessed their own waterworks); citizenship/poor-law status determined which "
    "populations were subject to compulsory state sanitary surveillance vs. left to market provision. "
    "Distinguished from the excluded Kucher 2005 precedent (pure doctrinal commentary with no "
    "access-outcome data): this study documents actual differential connection patterns by class/"
    "citizenship status tied to specific statutory mechanisms. Included per INCLUSION_EXCLUSION.md "
    "criteria 1-9. Extracted as S691."
)

# R1F58000B5617 - Kumara 2013, Bangalore metropolitan governance - INCLUDE -> S692
r = by_id["R1F58000B5617"]
r["full_text_status"] = "retrieved"
r["full_text_location"] = "Google Drive inbox (delivered PDF)"
r["full_text_decision"] = "include"
r["final_decision"] = "include"
r["reviewer_1"] = REVIEWER
r["notes"] = (
    "Comparative institutional performance study of water-supply service delivery across governance "
    "structures in the Bangalore Metropolitan Region: a single dedicated metropolitan water board "
    "(BWSSB) versus ten fragmented Urban Local Bodies (Town/City Municipal Councils served by "
    "KUWSDB), using empirical benchmarking data (Karnataka Urban Service Level Benchmarking reports) "
    "on coverage in general households AND slums, water availability, consumption, unaccounted-for "
    "water, and cost recovery, computed into a Service Delivery Index and Operational Efficiency "
    "Index per governance unit. Directly ties institutional/governance fragmentation to differential "
    "household- and slum-level water-access outcomes. Included per INCLUSION_EXCLUSION.md criteria "
    "1-9. Extracted as S692."
)

# R3C9D8DD0859C - Chathukulam & Devavrathan 2014, Gram Panchayats Kerala sanitation - INCLUDE -> S693
r = by_id["R3C9D8DD0859C"]
r["full_text_status"] = "retrieved"
r["full_text_location"] = "Google Drive inbox (delivered PDF)"
r["full_text_decision"] = "include"
r["final_decision"] = "include"
r["reviewer_1"] = REVIEWER
r["notes"] = (
    "Primary field study (field survey/verification, focus group discussions across 7 Gram "
    "Panchayats, 32 anganwadis, 28 schools and 496 households in Kozhikode district, Kerala) "
    "examining sanitation/toilet access and coverage under India's Total Sanitation Campaign (TSC), "
    "implemented via the constitutionally-mandated decentralized local-government institutions "
    "(Panchayati Raj Institutions) and the Nirmal Gram Puraskar fiscal-incentive scheme. Constructs "
    "an empirical Total Sanitation Index per Panchayat from field-verified household/school/anganwadi "
    "toilet-access data. Extends the established India rural water/sanitation "
    "institutional-governance precedent (cf. Singh 2006 PRI/ARWSP). Included per "
    "INCLUSION_EXCLUSION.md criteria 1-9. Extracted as S693."
)

# ---- EXCLUDES ----

exclusions = [
    dict(
        rid="R124041F5DF16",
        title="Social construction of hydropolitics: The geographical scales of water and security in the Indus Basin",
        authors="Mustafa, D",
        year="2007",
        code="E05",
        detail=(
            "Narrative literature review explicitly framed as identifying 'important themes and future "
            "research directions' for the Indus Basin; the Karachi water/sanitation access-inequality "
            "discussion and the Punjab irrigation-access discussion both rest on citations to other "
            "authors' published case studies (including the author's own earlier 1998-2002 "
            "publications) rather than original data collection or analysis conducted within this "
            "article. Extends the established narrative-synthesis exclusion precedent (cf. Crow & "
            "McPike 2009). Fails inclusion criterion 3."
        ),
    ),
    dict(
        rid="R3AEF33753AF3",
        title="Alternatives for safe water provision in urban and peri-urban slums",
        authors="Ali, SI",
        year="2010",
        code="E06",
        detail=(
            "Engineering/technology review comparing household-level vs. community-level decentralized "
            "water treatment systems for slums (point-of-use technologies, treatment train options, "
            "public-health rationale). No legal, administrative, institutional, regulatory or "
            "governance analysis anywhere in the paper (near-zero mentions of institution/governance/"
            "legal/law/policy/regulation across the full text). Fails inclusion criterion 2."
        ),
    ),
    dict(
        rid="R5288473FC800",
        title="A Multisectoral Approach to Primary Health Care in Fujian, China",
        authors="Yang H.; Yiheng M.; Qiu X.; Zhang H.; Lin Q.; Guan J.; Clayton S.",
        year="1991",
        code="E01",
        detail=(
            "Community primary-health-care program case study (Dahu, Fujian) covering school health "
            "education, home reconstruction, road construction, environmental sanitation, occupational "
            "health, and local ordinances; access to clean water is mentioned only as one brief outcome "
            "indicator ('access to clean water is almost universal') among many program outputs, not "
            "the paper's object of study. Extends the established Sandhu 2000 incidental-indicator "
            "precedent. Fails inclusion criteria 1-2."
        ),
    ),
    dict(
        rid="R53BDAFE46BDD",
        title="The right to water versus cost recovery: Participation, urban water supply and the poor in sub-Saharan Africa",
        authors="Jaglin S.",
        year="2002",
        code="E05",
        detail=(
            "Regional narrative review/synthesis explicitly framed as reviewing 'reforms that have "
            "directly and indirectly affected water services' across sub-Saharan Africa over two "
            "decades, drawing on secondary case studies cited from other authors' published work (no "
            "'field survey', 'interview', 'fieldwork', 'methodology' or 'sample' sections anywhere in "
            "the text). Extends the established narrative-synthesis exclusion precedent (cf. Crow & "
            "McPike 2009). Fails inclusion criterion 3."
        ),
    ),
    dict(
        rid="R0C5D57C3EF0E",
        title="Reforms for managing urban environmental infrastructure and services in asia",
        authors="Memon M.A. Mushtaq Ahmed; Imura H.; Shirakawa H.",
        year="2006",
        code="E01",
        detail=(
            "Macro-level regional review of decentralization/privatization/community-participation "
            "legal and policy reforms (statutory decentralization acts) across 14 Asian countries and "
            "three sectors (water supply/wastewater, solid waste, air quality); reports only generic, "
            "unquantified 'considerable improvements in quality and coverage' with no household-level "
            "or city-level access outcome data linked to specific reforms. Extends the established "
            "macro-governance-index/policy-review exclusion precedent (cf. Nkiaka/Schiel/Laitinen/"
            "Padowski, Banerjee 2001). Fails inclusion criteria 4-5."
        ),
    ),
    dict(
        rid="R6884837E85A8",
        title="The microbiological quality of seven large commercial private water supplies in the United Kingdom",
        authors="Kay D.; Watkins J.; Francis C.A.; Wyn-Jones A.P.; Stapleton C.M.; Fewtrell L.; Wyer M.D.; Drury D.",
        year="2007",
        code="E03",
        detail=(
            "Pure microbiological water-quality monitoring study (faecal indicator organisms, Giardia "
            "and Cryptosporidium spp. at the consumer tap across seven commercial private water "
            "supplies). No legal, administrative, institutional or governance analysis; examines "
            "treatment/monitoring design and rainfall-linked contamination episodes only. Fails "
            "inclusion criterion 2."
        ),
    ),
    dict(
        rid="R761657E447C4",
        title="A rights-based approach to accessing health determinants",
        authors="Perkins F.",
        year="2009",
        code="E05",
        detail=(
            "First-person 'Commentary' (the article's own designated type) describing a single site "
            "visit to an NGO drop-in centre in Cairo; water/sewerage/electricity access is mentioned in "
            "two sentences as an anecdotal outcome of unspecified court cases, with no case details, "
            "no systematic data collection, and no methodology - water is one of several outcomes "
            "discussed (marriage-rights litigation, birth certificates/school enrollment, HIV "
            "prevention services) rather than the paper's object of study. Fails inclusion criteria "
            "1 and 3."
        ),
    ),
    dict(
        rid="RB6A1EB27E732",
        title="Social inclusion in Mumbai: Economics matters too",
        authors="Buckley R.M.",
        year="2011",
        code="E05",
        detail=(
            "Theoretical/economic commentary responding to another author's article about an NGO "
            "(SPARC) in Mumbai; the paper explicitly self-describes as 'not a fine-grained empirical "
            "study' and relies on back-of-envelope economic calculations (DALYs, opportunity costs) "
            "rather than original data collection. Sanitation (community toilets) is discussed as one "
            "of several contested strategic choices (alongside land tenure and resettlement policy), "
            "not empirically measured for access outcomes. Fails inclusion criterion 3."
        ),
    ),
]

with open(EXLOG, newline="", encoding="utf-8") as f:
    ex_reader = csv.DictReader(f)
    ex_fieldnames = ex_reader.fieldnames
    ex_rows = list(ex_reader)

for ex in exclusions:
    r = by_id[ex["rid"]]
    r["full_text_status"] = "retrieved"
    r["full_text_location"] = "Google Drive inbox (delivered PDF)"
    r["full_text_decision"] = "exclude"
    r["final_decision"] = "exclude"
    r["exclusion_reason"] = ex["code"]
    r["exclusion_reason_detail"] = ex["detail"]
    r["reviewer_1"] = REVIEWER

    ex_rows.append({
        "record_id": ex["rid"],
        "title": ex["title"],
        "authors": ex["authors"],
        "year": ex["year"],
        "stage": "full_text",
        "exclusion_code": ex["code"],
        "exclusion_reason_detail": ex["detail"],
        "reviewer": REVIEWER,
        "date": DATE,
    })

fd, tmp = tempfile.mkstemp(dir="/home/user/water-law-dataset/legal-last-mile-systematic-review")
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)
os.replace(tmp, DB)

fd, tmp = tempfile.mkstemp(dir="/home/user/water-law-dataset/legal-last-mile-systematic-review")
with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=ex_fieldnames)
    w.writeheader()
    w.writerows(ex_rows)
os.replace(tmp, EXLOG)

print("Batch 140 recorded: 8 includes, 8 excludes.")
print(f"exclusion_log.csv new total: {len(ex_rows)}")
