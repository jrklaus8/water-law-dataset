#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R0878C3037524": "Gulyani, Talukdar & Kariuki 2005 (Urban Studies), 'Universal (Non)service? Water Markets, Household Demand and the Poor in Urban Kenya.' Rigorous household-survey study (674 households, 3 Kenyan towns) directly testing the standard 'poor pay more, get less' narrative and the World Bank's demand-driven/water-markets prescription. Finds that unit costs and water-use behavior do not divide cleanly along poor/non-poor lines and that kiosk service is not always a good solution for the poor, challenging the sufficiency of pricing-and-markets institutional reforms alone. A rigorous empirical institutional-mechanism study directly documenting how the market-based water-service institutional model performs (or fails to perform) for poor urban households.",
    "R09476239ACAF": "Ballestero 2015 (American Ethnologist), 'The Ethics of a Formula: Calculating a Financial-Humanitarian Price for Water.' Ethnographic/legal-institutional study of Costa Rica's public service regulator (ARESEP) and the regulatory formula it uses to set water tariffs, tracing how the constitutionally recognized human right to water is translated into a price via a specific legal/technical mechanism (the 'R' development-yield variable) and public hearings on rate petitions. A rigorous institutional/legal-mechanism ethnography directly documenting how a water-rate regulatory formula operationalizes -- and constrains -- the legal human right to water for Costa Rican consumers.",
    "R0B7EE19A8A50": "Pastore 2015 (Environment and Urbanization), 'Reworking the relation between sanitation and the city in Dar es Salaam, Tanzania.' Case study analysis of three areas of Dar es Salaam documenting how the colonial-era 'piped paradigm' of centralized water/sanitation infrastructure was imported to serve only elite neighborhoods, leaving the majority of urban Africans (relying on decentralized on-site systems -- boreholes, wells, on-site latrines) outside the formal planning model, and how local-government/urban-planning institutional coordination (or its absence) continues to shape differential sanitation access by settlement type. A rigorous institutional/planning-history case study directly documenting colonial-legacy infrastructure institutional design as a mechanism of differential sanitation access.",
}

EXCLUDES = {
    "R03DD1BAD1AD0": ("E04", "McSpirit & Reid 2011 (Society & Natural Resources), 'Residents' Perceptions of Tap Water and Decisions to Purchase Bottled Water.' A regression study of consumer purchasing-behavior/perceptions (perceived tap-water quality, trust, saliency, income) driving bottled-water purchase decisions in an Appalachian coal-mining region. A consumer-behavior/perceptions study, not a legal/institutional water-access-eligibility mechanism; extends the established perceptions/attitudes wrong-outcome exclusion precedent (Baird et al. 2015, Batch 223; Sperling et al. 2016, Batch 218)."),
    "R05BD2228D528": ("E12", "Willetts, Carrard, Crawford, Rowland & Halcrow 2013 (Development in Practice), 'Working from strengths to assess changes in gender equality.' A methodological paper presenting a strengths-based/appreciative-inquiry approach for assessing gender-equality outcomes of WASH initiatives, focused on evaluation methodology rather than an institutional/legal access-eligibility mechanism. Extends the established methodological/evaluation-approach exclusion precedent (Sullivan & Meigh 2003, Batch 226)."),
    "R0714B62F6AF9": ("E01", "Kiunsi 2013 (Environment and Urbanization), 'The constraints on climate change adaptation in a city with a large development deficit: the case of Dar es Salaam.' A broad urban development-deficit and climate-change-adaptation-policy overview; water/sanitation infrastructure statistics are contextual background within a climate-adaptation-plan-absence analysis, not the paper's institutional-mechanism analytical target. Extends the established wrong-topic exclusion precedent for content outside the review's institutional-access-mechanism scope."),
    "R08A3A9C2AA0D": ("E04", "Imo State Evaluation Team 1989 (Health Policy and Planning), 'Evaluating water and sanitation projects: lessons from Imo State, Nigeria.' A quasi-experimental health-impact evaluation (dracunculiasis, diarrhoea, nutritional status as primary outcomes) of a rural water/sanitation pilot intervention. A public-health epidemiological evaluation, not a legal/institutional access-eligibility mechanism study; extends the established child/public-health-outcome wrong-outcome exclusion precedent (Huda et al. 2012, Batch 223)."),
    "R0AF5F2494B63": ("E01", "Stewart & Gray 2006 (Environmental Politics), 'The Authenticity of \"Type Two\" Multistakeholder Partnerships for Water and Sanitation in Africa: When is a Stakeholder a Partner?' A governance/network-theory analysis (32 interviews) of two international multistakeholder partnerships' internal stakeholder/partner power structure, without documenting differential water-access outcomes for any specific population. A governance-structure/stakeholder-theory analysis, not a documented institutional mechanism's effect on access; extends the established wrong-topic exclusion precedent for governance-theory content lacking concrete access-outcome documentation."),
    "R08ABAD98A481": ("E01", "Perez 2002 (Community Development Journal), 'Achieving Sustainable Livelihoods -- A Case Study of a Mexican Rural Community.' A sustainable-livelihoods-framework case study of a rainwater-harvesting development project (San Felipe, Mexico), centered on participatory-development and gender-inclusion critique of project governance rather than a legal/institutional water-access-eligibility mechanism. Extends the established broad-development-critique wrong-topic exclusion precedent."),
    "R0B1CE2205CB7": ("E01", "Leon 2014 (Peace Review), 'Why Is the World Bank Financing Forced Evictions?' A political-economy critique of World Bank-financed 'villagization' and forced evictions of pastoral farmers in Ethiopia, centered on land tenure, dispossession and the 'right to the city' framework; water/sanitation infrastructure is mentioned only in passing as one of several services funded by the broader Protection of Basic Services program, not the paper's analytical focus. Extends the established water-resource/land-tenure-vs-water-service-access distinction (Ioris 2007, Batch 222)."),
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
    print(f"Batch 227 processed: {n_inc} includes, {n_exc} excludes.")
