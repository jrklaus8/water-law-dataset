#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R1E724AC6317D": "Sarkar 2019 (Water Policy) mixed-methods study of shared standpipe water access in Mathare slum, Nairobi, Kenya. Documents that the institutional/legal framework established by the Water Act 2002 (Water Service Boards, Water Service Providers, tariff-licensing regime under the Water Services Regulatory Board), traced to the colonial-era Vagrancy Act 1902 racial-segregation legacy shaping present-day water infrastructure distribution, is undermined by weak tariff-regulation enforcement, illegal connections, water theft, and documented tribal-affiliation favouritism by standpipe managers -- directly producing measured price disparities (Ksh.2 to Ksh.15+ per jerry can) and service-access hardship for slum residents (household survey n=258, focus groups, key-informant interviews). Extends the colonial-legacy institutional precedent (Njoh & Akiwumi S969; Kooy & Bakker S1001) and the institutional-capture/corruption precedent (Giglioli & Swyngedouw Sicily S990).",
    "R1F7E051104F1": "Romano 2012 (Bulletin of Latin American Research) case study of Nicaragua's anti-water-privatisation social movement and its legislative outcomes: the General Water Law (Law 620, 2007) and the Special CAPS Law (Law 722, 2010), the latter granting formal legal status/recognition to Comites de Agua Potable y Saneamiento (CAPS) -- community water-user associations that had operated for decades without legal recognition despite providing water access to over 1 million rural Nicaraguans. Documents, via 40 semi-structured interviews and focus groups, how the absence and later grant of formal legal status for these community water-management institutions directly shaped their capacity to secure funding, technical support, and water-system investment. Extends the institutional-legal-recognition-of-community-water-governance precedent (Nelson et al Fiji statutory water-committee governance, Batch 196; Harvey Uganda WASH regulatory structure/committee legal status, Batch 196).",
}

EXCLUDES = {
    "R19E5408986F2": ("E01", "Almebo et al 2021 (Environmental Health Insights) cross-sectional logistic-regression study of household utilization of community-level fluoride-filtered water in Dugda Woreda, Ethiopia. Examines behavioral/public-health determinants (income, affordability of a small water-treatment fee, family fluorosis history, knowledge, religious taboos around bone-char filters) of adoption of a specific water-QUALITY treatment technology; no legal/institutional mechanism governing water access is tested. Wrong-topic technology-utilization/uptake determinants study."),
    "RB70EF69F5B32": ("E01", "Sharma 2009 (Studies in History) historical study of water reservoirs and tanks in pre-modern (16th-17th century) India, based on European travelers' accounts. Purely a historical water-culture/architecture study of pre-modern reservoir construction and ritual water practices; no administrative-law or legal/institutional-mechanism analysis of documented access inequality relevant to the review's scope."),
    "R1BB5C10692F8": ("E01", "Dobyns 1952 (Human Organization) historical/anthropological case study of U.S. Indian Bureau administrators introducing wells among the Tohono O'odham (Papago) people of Arizona, 1915-1940s, examining administrative decision-making and tribal leadership resistance/acceptance of well technology. Narrative/administrative-anthropology case study of technology diffusion and resistance; no documented differential access outcome by social group tied to a legal/institutional barrier -- institutional content is background context for a diffusion-of-innovation narrative, per the established anthropological/narrative E01 precedent."),
    "R2622E802C40F": ("E01", "Okumura et al 2021 (Journal of Cleaner Production) application of the 'City Blueprint Approach' diagnostic/benchmarking tool (Trends and Pressures Framework, City Blueprint Framework, Governance Capacity Framework) to assess Integrated Water Resource Management performance for Greater Rio de Janeiro, comparing current and 2040-projected sanitation indicator scores against a strategic urban development plan. A technical governance-capacity benchmarking/indicator-tool study, not an empirical analysis of documented household-level access-inequality tied to a specific legal/institutional mechanism; reapplies the general institutional-governance-assessment E01 precedent (Kohlitz et al Pacific island HRWS-monitoring policy analysis, Batch 200)."),
    "R19C83E32D0E1": ("E01", "Andajani-Sutjahjo, Chirawatkul & Saito 2015 (Journal of International Women's Studies) qualitative gender study of domestic water burden, control, and public-participation exclusion in a Northeast Thailand village, examining male-dominated national and local water governance bureaucracy. Institutional/governance content is discussed but the study's core empirical finding concerns intra-household gender division of labor and women's exclusion from local governance participation, not a documented legal/institutional mechanism producing differential water ACCESS (all village households had water access via rainwater tanks). Reapplies the gender/anthropological-narrative E01 precedent (Jewell & Wutich, Batch 196)."),
    "R1D3B70649AA6": ("E05", "Zakiya 2014 (Development in Practice) reflective practitioner essay combining a literature review of NGO 'neo-comprador' critique and philanthrocapitalism theory with a first-person narrative case study of introducing endogenous-development (ED) praxis into WaterAid Ghana's WASH programming. Conceptual/reflective essay by a practitioner-scholar with no rigorous original empirical methodology analyzing a legal/institutional mechanism's effect on documented water-access outcomes; reapplies the established opinion/conceptual-essay E05 precedent (Musembi, Batch 200; Gupta, Ahlers & Ahmed, Batch 198)."),
    "R25B42F41DEE8": ("E06", "Schories 2008 (Desalination) engineering conference paper describing the IWAPIL innovative membrane bioreactor wastewater-treatment system piloted at two European campsites (Spain, Italy), reporting purification-efficiency and economic-comparison results. Pure wastewater-treatment engineering study with no legal/institutional-mechanism or access-inequality content; reapplies the established engineering-only E06 precedent."),
    "R25A96282EB25": ("E01", "Vasquez & Adams 2019 (Science of the Total Environment) discrete-choice-experiment (DCE) stated-preference economics study estimating households' willingness to pay for standpipe water-service attributes (hours, quality, distance, waiting time, governance/management type) in Nima-Maamobi slum, Accra, Ghana. A consumer-demand/willingness-to-pay economics study using choice-experiment methodology; institutional-barrier content (lack of property titles preventing utility extension) is cited only as background rationale, not empirically analyzed as a mechanism producing documented differential access. Reapplies the economic/demand-analysis E01 precedent."),
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
    print(f"Batch 201 processed: {n_inc} includes, {n_exc} excludes.")
