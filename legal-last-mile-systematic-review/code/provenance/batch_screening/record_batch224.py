#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R11ECDBD13542": "Mafuta, Zuwarimwe & Mwale 2021 (Sustainability, MDPI), 'WASH Financial and Social Investment Dynamics in a Conflict-Arid District of Jariban in Somalia.' Empirical mixed-methods study (19 randomly selected villages, transect walks, 38 focus group discussions, desktop review) documenting near-zero state-government WASH investment attributable to Somalia's collapsed central-government/statistical system since 1991, with WASH infrastructure financed almost entirely by NGOs (54.3%), diaspora remittances (34.5%) and community contributions (11.2%). A rigorous institutional/governance-failure case study directly documenting how state fragility as an institutional mechanism produces a WASH infrastructure backlog and low sanitation/water access for a vulnerable rural population.",
    "R33EC8B53721E": "Faure, Faust & Kaminsky 2019 (Water, MDPI), 'Legitimization of the Inclusion of Cultural Practices in the Planning of Water and Sanitation Services for Displaced Persons.' Qualitative institutional-decision-making study (28 semi-structured interviews with government and aid-organization stakeholders) examining how the institutional response to the 2015-2016 refugee/asylum crisis in Germany (de)legitimized inclusion of cultural practices in WASH facility planning for asylum seekers. Finds the institutional response was predominantly reactive rather than proactive. A rigorous institutional/administrative-decision-making case study directly documenting how legitimacy-based institutional discretion shapes WASH service design for a legally distinct, administratively processed population (asylum seekers).",
    "R855E06BB5C3D": "Martinez Moscoso, Aguilar Feijo & Verdugo Silva 2018 (Resources, MDPI), 'The Vital Minimum Amount of Drinking Water Required in Ecuador.' Rigorous doctrinal/normative/economic empirical study of Ecuador's 2017 legislative minimum-vital-water-amount guarantee (200 L/capita/day, Ministerial Agreements 2017-1522/1523) and its quantified differential economic impact across three municipalities (Cuenca, Gualaceo, Suscal) using original formula-based calculations (TAC, RWE, IH) applied to National Survey of Employment/Underemployment data. Finds the legal cost-recovery mechanism for raw-water-excess disproportionately burdens households in smaller, less-efficient, more-indigenous municipalities (Suscal: 4.17% of extreme-poverty household income vs. Cuenca: 0.31%). A rigorous legal/institutional-mechanism case study directly documenting how a water-law cost-recovery provision produces quantified differential affordability outcomes for indigenous and low-income households.",
}

EXCLUDES = {
    "R78B2DCE9ED20": ("E12", "Betera, Nyamandi & Nunu 2025 (INQUIRY), 'Exploring Water, Sanitation, and Hygiene Status and Health Outcomes in Zimbabwe: A Scoping Review of Literature.' An explicit, protocol-registered scoping review (655 records screened, 30 included) of existing literature on WASH status and health outcomes in Zimbabwe. A literature-review/synthesis article with no original empirical data collected by these authors; extends the established review-paper exclusion precedent (Aiyer 2007; Gero et al. 2014, Batch 220; Subramaniam & Williford 2012, Batch 222)."),
    "RA9801F141888": ("E12", "Turley, Saith, Bhan, Rehfuess & Carter 2013, 'Slum upgrading strategies involving physical environment and infrastructure interventions and their effects on health and socio-economic outcomes' (Cochrane Database of Systematic Reviews). A Cochrane intervention systematic review/meta-analysis of published trials, not original primary research; matches the established Cochrane systematic-review exclusion precedent (Danso-Appiah et al. 2008, Batch 219; Sinclair et al. 2011, Batch 223)."),
    "R365803888D74": ("E12", "Pories, Fonseca & Delmon 2019 (Water, MDPI), 'Mobilising Finance for WASH: Getting the Foundations Right.' A multi-organization (Water.org, IRC WASH, World Bank) synthesis/framework paper deriving '10 foundational issues' for WASH sector finance from a broad literature review, JMP/GLAAS/OECD datasets, and 20+ expert interviews spanning 40+ countries via a 'method of successive exclusion.' A framework-building synthesis exercise, not a bounded original empirical case study of a specific institutional mechanism's access-eligibility effect on a specific population; extends the established synthesis/framework-paper exclusion precedent (Jiménez et al. 2019, this batch; Kooy, Furlong & Lamb, Batch 222)."),
    "R363EC91C7699": ("E01", "Li, Cohen, Li & Zhang 2019 (Sustainability, MDPI), 'The Impacts of Socioeconomic Development on Rural Drinking Water Safety in China: A Provincial-Level Comparative Analysis.' A Canonical Correlation Analysis of broad province-level socioeconomic indicators (GDP per capita, urbanization rate, population density, water consumption) against a composite rural-drinking-water-safety index. Examines broad socioeconomic determinants of water infrastructure/quality, with no documented legal/institutional eligibility mechanism (tenure, fees, connection requirements, disconnection, discretion); extends the established broad-socioeconomic-circumstance-regression exclusion precedent (Antunes & Martins 2020, Batch 217)."),
    "R3A1EB80FA37D": ("E04", "Patel, Chandran, Hampton, Hecht, Grumbach, Kimura, Braff-Guajardo & Brindis 2012 (Preventing Chronic Disease, CDC), 'Observations of Drinking Water Access in School Food Service Areas Before Implementation of Federal and State School Water Policy, California, 2011.' A baseline observational study (24 California schools) of student water-drinking behavior/intake in food service areas before implementation of a school drinking-water mandate (SB 1413). The outcome measured is child water-consumption behavior for obesity prevention, not an access-eligibility mechanism excluding a marginalized population; extends the established child-health/consumption-behavior wrong-outcome exclusion precedent (Huda et al. 2012, Batch 223)."),
    "R2ABF896EA8EB": ("E12", "Jimenez, LeDeunff, Gine, Sjodin, Cronk, Murad, Takane & Bartram 2019 (Water, MDPI), 'The Enabling Environment for Participation in Water and Sanitation: A Conceptual Framework.' Explicitly states 'Based on an in-depth literature review, we analyze the forms of participation...' and proposes a conceptual framework integrating contextual factors and procedural elements. A literature-review-based conceptual-framework article with no original empirical data collection by these authors; extends the established review/conceptual-framework exclusion precedent (Aiyer 2007; Kooy, Furlong & Lamb, Batch 222)."),
    "R014D93A818B8": ("E05", "Bellaubi & Bustamante 2018 (Geosciences, MDPI), 'Towards a New Paradigm in Water Management: Cochabamba's Water Agenda from an Ethical Approach.' A theoretical/philosophical (geoethics, axiology, Kuhnian-paradigm) analysis of the values underlying Bolivia's Cochabamba Water Agenda, explicitly grounded in literature synthesis rather than original data collection (no interviews, surveys, or fieldwork reported). A doctrinal/values-based paradigm analysis with no independent empirical research methodology; matches the established doctrinal-analysis-no-empirical-evidence exclusion precedent (Mpanga 2016, Batch 221; Ioris 2007, Batch 222)."),
}


def atomic_write(path, fieldnames, rows):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path))
    with os.fdopen(fd, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp, path)


def process_db():
    with open(PATH, newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    decided = []

    for row in rows:
        rid = row["record_id"]
        if rid in INCLUDES:
            detail = INCLUDES[rid]
            row["full_text_status"] = "retrieved"
            row["full_text_decision"] = "include"
            row["reviewer_1"] = REVIEWER
            row["final_decision"] = "include"
            row["notes"] = (row.get("notes", "") + " " if row.get("notes") else "") + detail
            decided.append(row)
        elif rid in EXCLUDES:
            code, detail = EXCLUDES[rid]
            row["full_text_status"] = "retrieved"
            row["full_text_decision"] = "exclude"
            row["exclusion_reason"] = code
            row["exclusion_reason_detail"] = detail
            row["reviewer_1"] = REVIEWER
            row["final_decision"] = "exclude"
            row["notes"] = (row.get("notes", "") + " " if row.get("notes") else "") + detail
            decided.append(row)

    atomic_write(PATH, fieldnames, rows)
    return decided, fieldnames


def append_exclusion_log(decided):
    with open(EXCLOG_PATH, newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    for row in decided:
        if row["final_decision"] != "exclude":
            continue
        rows.append({
            "record_id": row["record_id"],
            "title": row["title"],
            "authors": row["authors"],
            "year": row["year"],
            "stage": "full_text",
            "exclusion_code": row["exclusion_reason"],
            "exclusion_reason_detail": row["exclusion_reason_detail"],
            "reviewer": REVIEWER,
            "date": DATE,
        })

    atomic_write(EXCLOG_PATH, fieldnames, rows)


if __name__ == "__main__":
    assert len(INCLUDES) + len(EXCLUDES) == 10
    decided, _ = process_db()
    assert len(decided) == 10
    append_exclusion_log(decided)
    n_inc = sum(1 for r in decided if r["final_decision"] == "include")
    n_exc = sum(1 for r in decided if r["final_decision"] == "exclude")
    print(f"Batch 224 processed: {n_inc} includes, {n_exc} excludes.")
