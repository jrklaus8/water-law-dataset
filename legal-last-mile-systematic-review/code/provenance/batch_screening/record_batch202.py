#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "RBA33BDA14EAD": "Ruiz Rosado 2008 case study of water supply access in Bellavista, Trujillo, Peru. Documents SEDALIB (the municipal water enterprise)'s explicit institutional rationing policy restricting formal piped supply to three days per week, two hours per day, and the role of the neighborhood 'Comite de Agua' community water committee in mediating and delaying/accelerating households' formal network connections. Documents severe, directly measured price disparities produced by this institutional rationing: households without adequate access pay up to 16.6x the network tariff to tricycle water vendors and 5-8x through official retail resale, with only 17% of Bellavista households achieving 'optimal access' status. Extends the institutional-rationing/informal-market-price-disparity precedent (Matsinhe, Juizo, Macheve & dos Santos 2008 Maputo, S1005) and the community-committee-gatekeeping precedent.",
    "RB87EFA103B2F": "Ratner & Rivera Gutierrez 2004 (Human Organization) action-research case study of wastewater management institutional transition in Panajachel, Guatemala. Documents the historical erosion of traditional Mayan civic/religious institutions (alcaldia, cofradia) previously responsible for collective waterworks maintenance, replaced by municipal fee-based administration. Documents a specific legal/institutional eligibility mechanism directly governing household sewage-connection access: initial municipal rules required proof of legal property ownership and up-to-date tax payment to connect, which discouraged connections; these were subsequently relaxed to require only currency on water/trash-collection bills plus a Q75 connection fee. Documents a differentiated, progressively-structured fee schedule negotiated through a multi-stakeholder dialogue forum, and a neighborhood 'alley committee' collective-connection mechanism, with directly measured connection-rate outcomes (550 of ~1,400 households connected by April 2001; 185 additional households connected via alley-committee collective agreements by March 2002). Extends the institutional-eligibility-documentation-requirement precedent for service connection and the community-committee-mediated-connection precedent (Ruiz Rosado S1012, this batch).",
}

EXCLUDES = {
    "RB8507E5E888F": ("E01", "Yntiso 2008 (Eastern Africa Social Science Research Review) mixed-methods study of the socioeconomic impacts of forced urban resettlement on low-income households relocated from inner-city Addis Ababa to 14 outskirts resettlement sites. While the paper documents legal-eligibility categories (owner-occupiers vs. public tenants vs. subtenants vs. private tenants) determining differential compensation entitlements under the World Bank Involuntary Resettlement Policy, water access is one minor sub-finding (section 6.7 of 6 impact domains) within a much broader study whose core focus is general livelihood disruption -- income decline, education-access decline, health-service-access decline, housing, social-network erosion, and transportation costs. The paper's core research question and scope are general resettlement-policy impact, not a focused legal/institutional water-access mechanism study. Reapplies the broad multi-domain-impact-study E01 precedent (cf. Kapuria Delhi Quality of Life, this batch; Adams et al Ghana DHS socioeconomic predictors, Batch 200)."),
    "R1823F1155BA1": ("E01", "Patel et al 2010 qualitative interview study (26 stakeholders) of perceived and actual institutional barriers -- exclusive beverage contracts, USDA regulations, cost -- to providing free drinking water in schools within a large California school district. Wrong topic and population: a school beverage/nutrition-policy barriers study, not a household/domestic water-access administrative-law mechanism study within the review's scope."),
    "RBCDE0E7C6962": ("E05", "Ndesamburo, Flynn & French 2012 reflective NGO practitioner case study describing WaterAid Tanzania's application of an 'Equity and Inclusion Framework' in Bashnet, Tanzania. Documents institutional programmatic outcomes (tariff reduction via diesel-generator-cost analysis, free service provision to identified disadvantaged households, disabled-accessible infrastructure design changes) but the methodology is a narrative/reflective NGO programme case study rather than a rigorous original empirical analysis of a legal/institutional mechanism. Reapplies the established reflective/practitioner-narrative E05 precedent (Zakiya 2014 Ghana endogenous-development essay, Batch 201; Musembi, Batch 200)."),
    "R1FBB650F8BAC": ("E05", "Cleaver & Hamada (Franks & Cleaver 'Resources-Mechanisms-Outcomes-Actors' analytical framework paper) on 'good water governance and gender equity'. A theoretical/conceptual framework article illustrated entirely with secondary case examples drawn from other researchers' previously published or unpublished studies (Dikito-Wachtmeister Zimbabwe; Tod Pakistan MCO/WCO; Howarth & Nott Nepal; Tukai Tanzania; Joshi et al India; Sultana Bangladesh), with no original empirical data collection by the authors. Conceptual/synthesis framework paper with no original empirical methodology; reapplies the established opinion/conceptual-essay E05 precedent (Musembi, Batch 200; Zakiya, Batch 201)."),
    "RB96173BC7BEA": ("E01", "Kapuria 2013 (Social Indicators Research) fuzzy-sets-theory quality-of-life assessment comparing Delhi neighborhoods (resettlement colonies, unauthorised colonies, urbanised villages vs. Cantonment Board/NDMC/DDA-jurisdiction colonies) across seven basic-service domains, of which water is only one alongside transport, sanitation, health, education, electricity, and green space. A multi-service composite quality-of-life index study, not a focused water-access legal/institutional-mechanism study; reapplies the broad multi-domain-impact-study E01 precedent (cf. Yntiso Addis Ababa, this batch; Adams et al Ghana DHS, Batch 200)."),
    "R1E0A15AEB55A": ("E01", "Chang et al 2020 (Journal of Cleaner Production) application of the 'City Blueprint Approach' diagnostic/benchmarking tool (Trends and Pressures Framework, City Blueprint Framework, Governance Capacity Framework) combined with hierarchical cluster analysis to evaluate integrated water resources management performance across 32 major Chinese cities. A technical governance-capacity benchmarking/indicator-tool study, not an empirical analysis of documented household-level access inequality tied to a specific legal/institutional mechanism; directly reapplies the City Blueprint Approach E01 precedent (Okumura et al 2021 Rio de Janeiro, Batch 201)."),
    "R16AB75AC4334": ("E01", "Kolesar & Serio 2011 (Interfaces, INFORMS Franz Edelman Award) operations-research study of revising reservoir water-release policies for three New York City dams on the Delaware River headwaters, balancing drinking-water-supply reliability, flood risk, and river-habitat/fisheries quality. Basin-scale, interstate reservoir-operations engineering/operations-research study; no household-level legal/institutional water-access mechanism or differential access outcome is examined. Reapplies the established basin/catchment-scale water-resource-allocation E01 precedent."),
    "R140432031A46": ("E01", "Chaudhuri et al 2020 (International Journal of Rural Management) nationwide spatial-statistical appraisal (Gini coefficients, hierarchical cluster analysis, Bray-Curtis slip-back index) of state-level Rural Water Supply Services coverage performance in India (2013-2018) using aggregated National Rural Drinking Water Programme database statistics against 40/55 lpcd norms. A macro-level, state-aggregated statistical assessment of programme coverage performance; does not test a specific legal/institutional mechanism's effect on household-level water-access outcomes via regression or case-based causal analysis. Reapplies the broad programme-performance/statistical-assessment E01 precedent (cf. Okumura Rio de Janeiro City Blueprint, Batch 201; Adams et al Ghana DHS, Batch 200)."),
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
    print(f"Batch 202 processed: {n_inc} includes, {n_exc} excludes.")
