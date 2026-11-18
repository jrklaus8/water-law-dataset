#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R3537F9598B47": "Granados & Sanchez 2014 (World Development) difference-in-difference panel study of the impact of Colombia's Law 142 of 1994 (household public utilities regime, enabling specialized public/private/mixed water and sewerage providers to replace direct municipal provision) on water/sewerage service coverage and child mortality, 550 municipalities, 1990-2005. Finds municipalities that reformed exhibited a slower reduction in child mortality and, for larger reformed municipalities, a smaller increase in water coverage than unreformed municipalities (though a larger increase in sewerage coverage). A genuine legal-reform (Law 142/1994) institutional-mechanism study directly measuring water/sewerage access-coverage outcomes via a difference-in-difference panel design (Table 5).",
    "R33F5730F8C31": "Makwara & Tavuyanago 2012 (European Journal of Sustainable Development) mixed-methods study (structured/semi-structured interviews with policymakers and residents, six urban councils, 2008-2012) of Zimbabwe's urban water-supply crisis. Documents an institutional/legal barrier mechanism -- municipal councils lack autonomy to set their own water tariffs and must obtain central-government permission, a bureaucratic approval process that delays maintenance/infrastructure investment and is compounded by shortage of foreign currency (also centrally controlled) -- contributing to documented water-access collapse (rationing, multi-month interruptions) and the 2008-2009 cholera epidemic.",
    "R30F0552CD829": "Francois, Kakeu & Kouame 2021 (Contemporary Economic Policy) dynamic panel (system GMM) study of institutional quality and access to improved sanitation across 44 sub-Saharan African countries, 2002-2015. Finds control of corruption, regulatory quality, and voice and accountability significantly and positively broaden sanitation access; documents a rural/urban dichotomy in which corruption control, rule of law, and government effectiveness matter for rural access while only voice and accountability matters in urban areas. A genuine institutional-quality panel-regression study of a sanitation-access outcome (sanitation explicitly within scope per INCLUSION_EXCLUSION.md).",
    "R351FB6562A87": "Leite 2010 (Gender & Development) qualitative case-study article documenting two Brazilian community water-management projects -- the 'Water Women' project in Sao Joao D'Alianca (Gender and Water Alliance/University of Brasilia/Union of Rural Workers, from 2001) and the Rural Women Workers Network (MMTR-SC) river-revitalization project in Santa Cruz da Baixa Verde, Pernambuco -- in which women's leadership within community water-management institutions is documented as directly improving local water conditions and community water-resource governance, contrasted with the absence of gender-sensitive water policy at the national level. Qualitative socio-legal case study of a gender-inclusive institutional-management-model mechanism and its access-relevant outcomes (per INCLUSION_EXCLUSION.md, qualitative socio-legal studies are not excluded for lacking a quantitative effect size).",
    "R350FA2E35538": "Bruggink 1985 (American Journal of Economics and Sociology) econometric study (95 U.S. municipally-owned water utilities, 1965 AWWA survey data) of monopoly welfare loss (excess residential water pricing above long-run marginal cost) and the effect of state versus local economic regulation on that welfare loss. Finds locally-regulated utilities exhibit significantly higher welfare loss (9.6-10.4% of the residential customer's annual bill) than state-regulated utilities (5.2-6.15%), a statistically significant difference (t=-4.58, p<0.01, Model 1; t=-2.71, p<0.01, Model 2). A genuine regression-based estimate directly isolating a regulatory/institutional mechanism's (state vs. local economic regulation) effect on a water-affordability outcome; qualifies for effect_sizes.csv under the Family C framework.",
}

EXCLUDES = {
    "R35003BF36393": ("E01", "McEvoy & Wilder 2012 (Global Environmental Change) critical risk analysis of a proposed Arizona-Sonora binational desalination plant as a climate-change adaptation response, examining discourse construction and unintended risks (energy demands, urban growth, brine discharge, geopolitical shifts, pricing effects) using cultural-risk and 'risk society' theory. A discourse/risk-analysis study of a proposed desalination technology and its speculative future impacts, not an empirical study of a legal/institutional mechanism's documented effect on household water access. Wrong-topic technology-risk-discourse study."),
    "R35DB956E02BF": ("E01", "Gorostiza, March & Sauri 2015 (Antipode) historical political-ecology case study of the Madrid water company Canales del Lozoya and its workers during the Spanish Civil War (1936-1939), documenting how worker/managerial knowledge of the urban water-supply infrastructure sustained service continuity under siege and was even weaponized (selective water-cutoffs to besieging troops). A historical account of wartime infrastructure resilience and labor geography, not a study of a legal/institutional mechanism producing differential household water-access outcomes in the sense of the project's access-inequality framework. Wrong-topic historical infrastructure-resilience study."),
    "R3665AA462296": ("E01", "Moglia, Perez & Burn 2008 (Development) conceptual/methodological discussion of three archetypal water-development participation processes (techno-centric, micro-credit, companion modelling) with an applied case study (AtollGame experiment, Tarawa, Kiribati), finding the participatory 'companion modelling' process undermined by the water utility's failure to take ownership of negotiated outcomes and political conflict between traditional and administrative authority. A process-design/methodology paper without a reported water-access, coverage, or affordability outcome tied to a specific legal/institutional mechanism. Wrong-topic participatory-process-design study."),
    "R3832EE69700F": ("E01", "Mbuvi, De Witte & Perelman 2012 (Utilities Policy) double-bootstrap DEA study of technical efficiency and effectiveness ('benefit of the doubt' analysis) of 51 African urban water utilities (WOP-Africa dataset, 2006), decomposing inefficiency from ineffectiveness and examining GDP, regulation type, and network density as determinants. A utility operational-efficiency/effectiveness benchmarking study measuring input-output production performance, not household-level differential water-access outcomes tied to a specific legal/institutional eligibility or barrier mechanism. Reapplies the established utility-operational-efficiency-benchmarking E01 precedent (Ferro, Romero & Covelli, Batch 207)."),
    "R366F94E9259F": ("E01", "Norman, Dunn, Bakker, Allen & Cavalcanti de Albuquerque 2013 (Water Resources Management) development and pilot application of the Water Security Status Indicators (WSSI) assessment method, a multivariate participatory governance-indicator tool integrating water quality/quantity for aquatic-ecosystem/human-health, applied to the Township of Langley, British Columbia. A governance-assessment-tool development/application study, not an empirical study of a legal/institutional mechanism's documented effect on differential household water access. Reapplies the established governance-benchmarking-tool-application E01 precedent (Moretto Venezuela, Batch 207; Chang et al China, Batch 202)."),
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
    print(f"Batch 208 processed: {n_inc} includes, {n_exc} excludes.")
