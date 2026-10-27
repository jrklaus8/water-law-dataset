#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R6F0D8847D6F7": "de Sardan 2011 (IDS Bulletin) anthropological fieldwork study (three urban sites, Niger, 2009) of the co-delivery of four public goods including water and sanitation, examining formal/informal institutional 'modes of governance' (bureaucratic, project-based, associational, municipal, chiefly, merchant). Documents specific institutional/legal mechanisms: development-project-imposed 'social counterpart'/quota contributions as a condition of infrastructure investment; and an eligibility-circumvention practice in which 'traders may be permitted to declare themselves mere hawkers in order to be able to make use of socially subsidised water sources.' A genuine institutional/governance mechanism study directly examining formal and informal eligibility, contribution, and coordination mechanisms affecting water-service co-delivery to the poor.",
    "R214868A2F9A8": "Adams & Zulu 2015 (Geoforum) mixed-methods case study (preliminary survey, key-informant interviews, focus groups, secondary data) of Water User Associations (WUAs) as a business-based community-based natural resource management (CBNRM) model supplying water to poor urban/peri-urban neighborhoods of Malawi's two major cities. Documents how insecure/uncertain land tenure, poor municipal capacity, and power relations between WUAs and residents produce tradeoffs between water-supply expansion and participatory/ownership goals. A genuine institutional/governance mechanism study directly examining community-public partnership models and land-tenure barriers affecting peri-urban water access for the poor.",
    "R236175EC76E5": "Sandoval-Minero 2019 (Springer book chapter) institutional/policy analysis of Mexican urban water utility financial sustainability, documenting that federal subsidies are allocated via centralized 'operating rules' without linkage to performance commitments, the absence of formal economic/tariff regulation for most municipal utilities, and that 'many new connections are financed by the users themselves directly through connection rights,' shifting infrastructure costs onto households. A genuine institutional/legal mechanism study directly examining subsidy-allocation and connection-cost-burden barriers to affordable formal water-service access in Mexico.",
}

EXCLUDES = {
    "R6C0CAA12E4E9": ("E06", "Agthe & Billings 1987 (American Journal of Economics and Sociology) econometric simultaneous-equation demand study estimating water-price elasticity by household income group under Tucson, Arizona's increasing block-rate tariff structure. A pure economic demand-elasticity estimation study of already-connected households' consumption behavior, not a water-access eligibility mechanism; extends the established engineering/economics-only exclusion precedent (Nauges & Strand 2007, Batch 218; Alvarez/Prieto/Zofio 2014, Batch 212)."),
    "R69F53378C8F2": ("E06", "Jiang & Zheng 2014 (Economic Development and Cultural Change) panel-regression study of private sector participation (PSP) and financial/operational performance (employment, profitability, managerial expenses) of urban water utilities in China. The one potentially access-relevant estimate (number of domestic water users) is explicitly described by the authors as 'statistically insignificant or marginally significant' and 'still pretty vague.' A utility financial-performance/efficiency study, not a study documenting a significant effect on water-access eligibility; extends the established utility-efficiency exclusion precedent (Alvarez/Prieto/Zofio 2014; Grafton/Chu/Kompas 2015, Batch 212)."),
    "R686809568A69": ("E01", "Plummer, Velaniskis, de Grosbois, Kreutzwiser & de Loe 2010 (Environmental Science & Policy) content-analysis study of source-water-protection policy development in Ontario, Canada following the 2000 Walkerton E. coli contamination crisis, examining land-use planning policy statements across three watershed case studies. A water-RESOURCE/water-QUALITY regulatory-policy study, not a household water-SERVICE access-eligibility mechanism study; extends the established water-resource-vs-water-service-access distinction and the water-quality-crisis regulatory-compliance exclusion precedent (Grigg 2017/Flint, Batch 219)."),
    "R6D2B3D34E44B": ("E01", "Closmann 2007 (Journal of Urban History) historical study of water pollution and economic upheaval in Hamburg, Germany, 1919-1923, examining how post-WWI inflation and economic chaos increased industrial/agricultural wastewater discharge into the Elbe river. A historical water-QUALITY/pollution study without any water-service access-eligibility mechanism content; extends the established water-quality-focus and historical-institutional-narrative-without-documented-access-outcome exclusion precedents."),
    "R6E9D96798462": ("E12", "Ivens 2008 (Development) synthesis/opinion essay reviewing existing case studies and literature (GWA/UNDP reports, prior country studies) on whether increased water access empowers women, concluding that impact is limited and calling for 'more impact studies' and an 'empowering participatory approach.' A conceptual synthesis essay with no original empirical data collected by the author; extends the established review-paper exclusion precedent (Aiyer 2007; Sternlieb & Laituri 2010, Batch 216; Sommer et al. 2014, Batch 218)."),
    "R20AFC5AD5970": ("E01", "Kansal & Cole 2019 (ASCE World Environmental and Water Resources Congress) survey-based (173 stakeholders) WASH Sustainability Index and Customer Satisfaction Index assessment for Kailahun District, Sierra Leone, covering financial, institutional, management, and technical indicator domains and their relationship to the Human Development Index. A broad WASH infrastructure-sustainability and customer-satisfaction assessment framework, not a study documenting a specific legal/institutional water-access eligibility or exclusion mechanism; extends the established broad-framework exclusion precedent (Sternlieb & Laituri 2010, WASH indicator frameworks, Batch 216)."),
    "R1EA55CF56B9D": ("E12", "Gero, Carrard, Murta & Willetts 2014 (Journal of Water, Sanitation and Hygiene for Development), explicitly labeled 'Review Paper,' systematic review of existing literature on private and social enterprise roles in WASH service delivery for the poor. A systematic literature review synthesizing others' findings with no original empirical data collected by the authors; extends the established review-paper exclusion precedent (Aiyer 2007; Sternlieb & Laituri 2010, Batch 216; Nelson & Murray 2008, Batch 219)."),
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
    print(f"Batch 220 processed: {n_inc} includes, {n_exc} excludes.")
