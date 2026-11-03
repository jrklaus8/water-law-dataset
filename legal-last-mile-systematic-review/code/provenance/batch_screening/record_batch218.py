#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R2D9BCED515D0": "Etongo, Fagan, Kabonesa & Asaba 2018 (Water/MDPI) survey-based study (SDW + 642 households across 17 villages, Lwengo district, southern Uganda) of community-managed rural water supply systems, examining the role of Water User Committees (WUCs) in participation and capacity development. Finds 30% of households had a WUC member, 52% had never made financial contributions to a WUC, and chi-square tests found no significant difference between wealthier and poorer households' contributions, with NGO/project-driven training the dominant source of technical capacity. A genuine institutional/community-management mechanism study examining WUC financial-contribution requirements and participation as determinants of rural water-system functionality/access.",
    "R14C9B7372CC7": "Badri & Joshi 2018 (IEEE PuneCon) practitioner impact-assessment study of Shelter Associates' 'One Home-One Toilet' (OHOT) cost-sharing household sanitation delivery model in urban slums of Maharashtra, India (pre-post case-control impact study, 386-463 households across four cities: Kolhapur, Navi Mumbai, Pimpri-Chinchwad, Pune). Documents a specific institutional/administrative mechanism -- a triangular partnership between the NGO, Urban Local Bodies, and community members in which SA provides construction materials while beneficiaries bear labour costs -- and quantitative outcomes (93% toilet usage by all family members, reduced UTI symptoms, reduced use of community toilet blocks). A genuine institutional/administrative-assistance mechanism study directly enabling household sanitation access for the urban poor.",
    "R14D397826679": "Behera, Rahut & Sethi 2020 (Utilities Policy) quantitative multinomial logit regression study using three waves of the Nepal Living Standard Survey (1995-96, 2003-04, 2010-11) examining determinants of urban household access to drinking water, sanitation, and waste-disposal services. Finds education, household wealth, distance to markets, and ecological/development region are significant determinants of access to piped water, flush toilets, and proper waste disposal. A rigorous quantitative study of water/sanitation access determinants using broad socioeconomic/geographic circumstance variables (education, wealth, distance, region) rather than a specific legal/institutional eligibility or barrier mechanism.",
    "R13014C89A7C9": "Tigabu, Nicholson, Collick & Steenhuis (Water Policy) Tobit-regression study (survey of 160 households across 16 water supply systems, Achefer area, Amhara region, Ethiopia) of determinants of household cash and labour contributions to community-managed rural water supply system protection and maintenance. Finds household contributions are positively and significantly affected by participation in project design/implementation, advocacy intensity, and household income, with Water User Committees (WUCs) setting the tariff/contribution levels that determine system functionality. A genuine institutional/community-management mechanism study, though the regression outcome variable (contribution amount) is a financing-sustainability measure rather than a direct water-access outcome.",
    "R0E434D61F108": "Ranganathan 2014 (International Journal of Urban and Regional Research) mixed quantitative/ethnographic case study of the Greater Bangalore water project's market-oriented 'beneficiary capital contribution' cost-recovery policy for extending piped water to peripheral, informally-tenured 'revenue layout' settlements. Documents that as a direct result of resident welfare associations' political mobilization and lobbying, the water utility formally waived the requirement of proof of permanent land tenure for a water connection and meter, accepting proof of payment for the water pipes alone as sufficient to demonstrate residence -- i.e., formal tenure was successfully removed as an eligibility requirement for water-service delivery. A rigorous legal/institutional mechanism study documenting a specific, named change to a formal water-connection eligibility requirement (tenure proof replaced by payment proof) for informally-tenured urban peripheral households.",
    "R0F404B9CB634": "Chng 2012 (Regulation & Governance) fieldwork-based institutional/regulatory case study of 'regulatory mobilization' by NGOs and community groups around water access for the urban poor in the wake of Metro Manila's 1997 water-utility privatization. Documents the National Water Resources Board's (NWRB) Certificate of Public Convenience (CPC) licensing framework governing small-scale water providers (SSWPs) operating in the absence of a clear institutional/legal framework for their participation in service provision (only 223 CPCs issued by June 2000, with tariff-setting rate adjustments capped at 12% return on investment), and how informal-sector actors and NGOs mobilized around these regulatory rules to obtain and expand water access. A genuine institutional/regulatory mechanism study directly examining formal licensing/tariff-regulation barriers and mobilization strategies affecting urban-poor water access.",
}

EXCLUDES = {
    "R6A8E5F1C16DC": ("E03", "Khabo-Mmekoa & Momba 2019 (IJERPH) microbiological water-quality study assessing thermotolerant coliform and E. coli contamination in drinking water samples from rural and urban households in Ugu District Municipality, KwaZulu-Natal, South Africa, using social-disparity framing (housing, education, employment) as descriptive background rather than an institutional/legal access mechanism. A water-quality/contamination-exposure study; extends the established water-quality-only exclusion precedent (McDonald & Jones; Eggers et al. 2018, Batch 215). Wrong-exposure contamination-testing study."),
    "R0BE5FFDEDC88": ("E04", "Sperling, Romero-Lankao & Beig 2016 (unnamed journal, citizen-priorities survey) survey study of over 1,200 Mumbai citizens examining determinants of local infrastructure and environmental policy PRIORITY RANKINGS (air pollution, waste, water, heat) rather than water access itself; piped-water-on-premises status is used only as one of several independent/predictor variables (alongside asthma, electricity access, literacy) explaining variation in the dependent variable of priority ranking. Wrong-outcome study: the outcome measured is policy-priority preference, not a water-access outcome."),
    "R0F457D622245": ("E12", "Sommer, Ferron, Cavill & House 2014 (Environment and Urbanization) narrative literature review synthesizing 275 existing articles, case studies, reports and grey-literature documents on violence, gender and WASH, explicitly noting the reviewed evidence base is 'primarily anecdotal case studies' rather than original empirical data collected by the authors. A conceptual/synthesis review with no original empirical data collected by the authors; extends the established review-paper exclusion precedent (Aiyer 2007; Sternlieb & Laituri 2010, Batch 216). Also wrong-topic in substance (violence/safety risk in WASH access, not a legal/institutional eligibility mechanism)."),
    "R0A739DB3E994": ("E06", "Nauges & Strand 2007 (Resource and Energy Economics) econometric water-demand-elasticity estimation study (two-step demand-function estimation, El Salvador and Tegucigalpa, Honduras household survey data) finding non-tap water demand elasticities of -0.4 to -0.7 with respect to total water cost. A pure economic/engineering demand-estimation study with no legal or institutional mechanism content whatsoever; extends the established engineering/economics-only exclusion precedent (Alvarez/Prieto/Zofio 2014; Grafton/Chu/Kompas 2015, Batch 212)."),
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
    print(f"Batch 218 processed: {n_inc} includes, {n_exc} excludes.")
