#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R0A72E874D143": "Rahaman, Everett & Neu 2007 (Accounting, Auditing & Accountability Journal), 'Accounting and the move to privatize water services in Africa.' Governmentality/institutional-sociology study (Bourdieu/Foucault framing) of the Ghanaian water-privatization debate, based on archival documents (2,300+ pages) and 34 interviews with government officials, World Bank/IMF representatives, NGOs (CAPW), and consultants. Documents how accounting technologies, vocabularies and experts were enlisted by the World Bank and Ghanaian Government to justify a proposed public-private-partnership/lease privatization of urban water services (GWC), and how these were resisted by civil-society coalitions, directly tracing the institutional mechanics of a national water-service-provision reform debate. A rigorous institutional/policy-process case study directly documenting the accounting and institutional mechanisms shaping a market-based water-service reform.",
    "R10C784AFAE14": "Subramaniam 2014 (Current Sociology), 'Neoliberalism and water rights: The case of India.' Qualitative-methods study analyzing India's National Water Policies (1987, 2002) and Five-Year Plans (1985-2007) alongside an embedded case study of Tarun Bharat Sangh (TBS), an NGO-led informal institution (the Arvari Sansad/'water parliament') governing collective water-resource management in 70 villages of Rajasthan. Documents a specific institutional mechanism (community self-governance vs. state/private commodification, contested legal ownership of a revived river's water rights) and how differential participation and access are shaped by caste, class and gender within the collective-governance institution. A rigorous institutional/legal-mechanism case study of a documented water-governance institution with differential access implications for a specific rural population.",
    "R0CD725BAD368": "Manikutty 1997 (Development Policy Review), 'Community Participation: So What? Evidence from a Comparative Study of Two Rural Water Supply and Sanitation Projects in India.' Rigorous comparative case study of two otherwise-similar Kerala rural water/sanitation projects that differed specifically in whether an institutional community-participation mechanism (Ward Water Committees, transparent siting/eligibility procedures) was incorporated, with household survey data (n=80 each project) documenting statistically significant differences in tap-functioning rates (92% vs. 74%), switch-over to safe water, cost recovery (25% vs. <10%), and beneficiary satisfaction. A rigorous institutional-mechanism comparative study directly isolating the effect of a participatory-governance institution on documented water-access and service outcomes.",
    "R0CC979E7B4D9": "McFarlane & Desai 2015 (Environment and Urbanization), 'Sites of entitlement: claim, negotiation and struggle in Mumbai.' Nine-month ethnographic study of two Mumbai informal settlements (Rafinagar, a non-notified slum, and Khotwadi, a notified slum) documenting how legal/administrative status under the Maharashtra Slum Areas Act 1971 (notified vs. non-notified) and a pre-1995-residency eligibility cutoff produce starkly differential water and sanitation entitlements and access (e.g., legal water connections barred to post-1995 residents; municipal raids cutting both legal and illegal connections in the non-notified settlement). A rigorous institutional/legal-status case study directly documenting a codified eligibility mechanism's effect on differential water/sanitation access.",
    "R150C5FBFA557": "Das 2015 (Environment and Urbanization), 'The urban sanitation conundrum: what can community-managed programmes in India unravel?' Comparative case study (36 in-depth interviews, household survey n=422, 2007-2008 and 2011 fieldwork) of Community-Managed Sewerage Schemes in notified slums in two Madhya Pradesh cities (Gwalior, Indore), documenting how an institutional cost-recovery/user-committee governance model, and the 'notified slum' eligibility status required for programme access, produced sharply different sanitation-access outcomes (e.g., 63% vs. 21% open defecation in project settlements) depending on socioeconomic status and local-government responsiveness. A rigorous institutional-mechanism comparative case study directly documenting a formal eligibility/cost-recovery mechanism's differential effect on sanitation access.",
    "R13E85C59B4CA": "Wutich 2009 (Human Ecology), 'Water Scarcity and the Sustainability of a Common Pool Resource Institution in the Urban Andes.' Ethnographic and panel-survey study (72 randomly sampled households, 5 interview rounds) of a community-run tapstand water system in a Cochabamba, Bolivia squatter settlement, documenting a formal community-membership eligibility institution (landowner/proxy-member status vs. renter status) that determines legal access to the water system and participation in its governance (Neighborhood Council), with renters formally excluded from water rights despite being long-time residents. A rigorous institutional/legal-eligibility-mechanism case study with quantitative (ANOVA, t-test) documentation of differential water access by community-membership status across wet/dry seasons.",
}

EXCLUDES = {
    "R0C4B74812D98": ("E12", "Yacoob 1990 (Health Policy and Planning), 'Community self-financing of water supply and sanitation: what are the promises and pitfalls?' A critical policy essay/literature review synthesizing existing studies on cost-recovery and willingness-to-pay methodology across the WS&S sector broadly, offering general policy recommendations rather than presenting original empirical data on a specific institutional mechanism in a specific location. A methodological/policy-critique paper without an institutional-mechanism case study; extends the established methodological/evaluation-approach exclusion precedent (Sullivan & Meigh 2003, Batch 226; Willetts et al. 2013, Batch 227)."),
    "R013E7C57E2C0": ("E06", "Medilanski, Chuan, Mosler, Schertenleib & Larsen 2006 (Environment and Urbanization), 'Wastewater management in Kunming, China: a stakeholder perspective on measures at the source.' A structured-interview study (34 expert stakeholders) evaluating technical, financial and social feasibility of two competing decentralized sanitation technologies (urine-diverting dry toilets vs. NoMix flush toilets) for wastewater/nutrient management. An engineering/technology-adoption feasibility study focused on infrastructure choice, not a legal/institutional water-access-eligibility mechanism; extends the established engineering/economic-optimization exclusion precedent (Ojha et al. 2018, Batch 226)."),
    "R12527DF38787": ("E04", "Arar 1998 (Human Organization), 'Cultural Responses to Water Shortage among Palestinians in Jordan: The Water Crisis and Its Impact on Child Health.' A biocultural epidemiological study (year-long morbidity surveys, water-sample microbial analysis, 72 households) with childhood diarrhea incidence as the primary outcome, examining cultural, household-structure and gender-ideology determinants of child health in two Amman refugee camps. A public-health/child-health-outcome study, not a legal/institutional water-access-eligibility mechanism; extends the established public-health-outcome wrong-outcome exclusion precedent (Imo State Evaluation Team 1989, Batch 227)."),
}

WRONG_FILE = {
    "R110B658A4045": "Target record per new_batch_pool.json / Drive filename: Fombe & Bih 2014, 'Surface Water Pollution and its Implication in the Kumba Municipality of Cameroon.' Delivered PDF content (verified via both extracted .title metadata and full first-page-through-references text) is an entirely different paper: Kimengsi & Fogwe 2017 (International Journal of Global Sustainability), 'Urban Green Development Planning Opportunities and Challenges in Sub-Saharan Africa: Lessons from Bamenda City, Cameroon' -- different authors, different title, different journal, different year, different topic (urban green-space planning, not water pollution). Flagged wrong_file_retrieved; not screened; Drive file not moved.",
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
        elif rid in WRONG_FILE:
            detail = WRONG_FILE[rid]
            row["full_text_status"] = "wrong_file_retrieved"
            row["reviewer_1"] = REVIEWER
            row["notes"] = (row.get("notes", "") + " " if row.get("notes") else "") + detail

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
    assert len(INCLUDES) + len(EXCLUDES) + len(WRONG_FILE) == 10
    decided, _ = process_db()
    assert len(decided) == 9
    append_exclusion_log(decided)
    n_inc = sum(1 for r in decided if r["final_decision"] == "include")
    n_exc = sum(1 for r in decided if r["final_decision"] == "exclude")
    print(f"Batch 228 processed: {n_inc} includes, {n_exc} excludes, {len(WRONG_FILE)} wrong_file_retrieved.")
