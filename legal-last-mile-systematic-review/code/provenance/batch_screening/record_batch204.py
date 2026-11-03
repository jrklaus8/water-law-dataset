#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R07A0E36456D4": "Mogomotsi, Mogomotsi & Matlhola 2018 (Physics and Chemistry of the Earth) new-institutional-economics review of formal water institutions in Botswana. Documents that Botswana's Constitution contains no justiciable right to water (unlike South Africa/Namibia), leaving water provision purely discretionary, and analyzes the landmark Mosetlhanyane and Others v Attorney General of Botswana case (and predecessor Sesana case), in which the government, exercising its Water Act 1968 Section 6 borehole-permission regime, refused indigenous Basarwa/San residents of the Central Kalahari Game Reserve permission to re-commission a borehole for domestic water use -- a documented coercive-relocation tool that directly deprived a specific indigenous population of water access. Extends the legal-eligibility-permission-denial-as-relocation-tool precedent, and the indigenous/colonial-legacy institutional-mechanism precedent.",
    "R53F48CC1C325": "Fischer 2021 (World Development) mixed-methods study of India's Mahatma Gandhi National Rural Employment Guarantee Act (MGNREGA) -- a statutory decentralized rural-employment/infrastructure-project mechanism administered through elected village panchayats -- and its effects on climate-related water access in Himachal Pradesh. Uses a primary dataset of 798 small-scale development projects across 35 villages, finding that a majority of water-related interventions (199 of 251, 79%) improved water access in the face of water stress, with documented benefits skewing towards poorer and historically marginalized social groups, attributed to long-term political-democratization processes shaping local decision-making. Extends the statutory-decentralized-institutional-mechanism precedent for documented differential water-access outcomes by social group.",
    "R21E208560E01": "Hope 2007 (World Development) propensity-score-matching (PSM) quasi-experimental evaluation of India's government watershed-development programme (administered by the Rajiv Gandhi Mission for Watershed Development) in Madhya Pradesh, separately estimating treatment effects on agricultural returns and on domestic water collection time (n=470 matched sample). Finds the watershed-development institutional intervention increased mean domestic water collection time by 17.37 minutes/day (SE 2.46) in the dry season, with significant heterogeneous effects by income quartile (bottom two quartiles: 12-18 additional minutes/day; top quartile: 31.03 additional minutes/day) and by prior water-collection burden (households with the lowest prior collection times saw the largest increases). A rare regression/matching-based estimate directly isolating a government institutional mechanism's measured effect on a domestic water-access outcome; qualifies for effect_sizes.csv under the strict Family A/B/C framework.",
    "RBF7A834386E5": "Zerah 2008 (Geoforum) historical-institutional analysis of water supply infrastructure governance in colonial and post-colonial Bombay/Mumbai. Documents how the 1888 Bombay Municipal Corporation Act and subsequent municipal institutions shaped differential water-network access from the outset (favoring colonial/European quarters over native quarters), how post-independence 'notified' vs. 'non-notified' slum status determines eligibility for municipal water-network expansion, and how 1970s World Bank-imposed institutional/financial restructuring conditionalities shaped the current supply model -- all tied to directly measured differential access outcomes (500 lpcd in richer areas vs. ~50 lpcd in suburbs by the 1960s; only 5% of slum inhabitants have individual water connections vs. 49% sharing standpipes; documented scheduled-tribe (58%) vs. non-scheduled-caste/tribe (72%) differential connection rates). Extends the legal-eligibility-classification-status precedent (notified/non-notified slum status, cf. Das 2016 India CMWSS notified-slum eligibility, S1009).",
}

EXCLUDES = {
    "R01577352961E": ("E01", "Bardosh 2015 (Geoforum) ethnographic study of Community-Led Total Sanitation (CLTS) implementation in Katete district, Eastern Zambia, examining the behavioral/participatory-development methodology's tensions between theory, policy, practice and local realities. Focus is on a behavioral-change/community-mobilization sanitation-promotion technique (shame-based 'triggering', participatory rural appraisal), not a specific administrative-law/institutional eligibility, permitting, or tariff mechanism governing water/sanitation access. Wrong-topic behavioral-program-evaluation study."),
    "R234022A8FD20": ("E01", "Romero Lankao 2010 (Environment and Urbanization) climate-change vulnerability/hazard-exposure study of flood, drought and other water-related climate risks facing Mexico City. Institutional/governance content (1989 Federal District Water Commission private concessions, fragmented federal/state/municipal jurisdiction) appears only as contextual background to a disaster-risk-reduction and climate-adaptive-capacity narrative; the paper's core focus is climate-hazard vulnerability, not a documented legal/institutional mechanism producing differential household water-access outcomes. Reapplies the established climate-hazard/vulnerability-assessment E01 precedent."),
    "RBC9BBD26946B": ("E01", "Ilahi & Grimard 2000 (Economic Development and Cultural Change) econometric (reduced-form time-allocation equations) study using 1991 Pakistan Integrated Household Survey data to estimate how public water-infrastructure quality affects rural women's time allocation between water collection, market work, and leisure. Examines general infrastructure-quality effects on time-use, not a specific legal/institutional (permitting, eligibility, tariff) mechanism; wrong-topic economic time-allocation/demand-analysis study, reapplying the established economic/infrastructure-quality E01 precedent."),
    "RBFBE0C8DD5C3": ("E01", "Nkwocha 2009 (Social Indicators Research) household-survey study (n=501, 13 villages) with logistic regression of water supply deficiency and its socioeconomic implications (agriculture, rural industrialization, education, health) in the Niger-Delta region of Nigeria. Documents general water-scarcity effects on rural livelihoods and development; no specific legal/institutional mechanism (permitting, eligibility, tariff, connection rule) is examined as producing the documented deficiency. Wrong-topic general water-scarcity-impact study."),
    "RC05659F81735": ("E01", "Poonia & Punia 2018 (Water Policy) district-level (n=626 districts) spatial-statistical analysis using Census of India data and analytic hierarchy process (AHP) weighting to construct a composite drinking-water-supply sustainability index across India. A macro-level spatial-index/benchmarking study of programme coverage performance; does not test a specific legal/institutional mechanism's effect on household-level water-access outcomes via regression or case-based causal analysis. Reapplies the broad macro-level index/benchmarking-study E01 precedent (cf. Chaudhuri et al Har Ghar Jal, Batch 202; Okumura Rio de Janeiro City Blueprint, Batch 201)."),
    "RC03DB0BC866E": ("E07", "Adegun 2015 (Environment and Urbanization) comparative case study of state-led versus community-initiated stormwater drainage interventions in two informal settlements in Johannesburg, South Africa. Examines flood-risk/stormwater-drainage infrastructure management, a distinct service from household water supply/access; wrong service per the review's scope."),
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
    print(f"Batch 204 processed: {n_inc} includes, {n_exc} excludes.")
