#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R5514D2439F0C": "Walsh 2011 (Human Organization) ethnographic study (fieldwork 2004-2008) of the Junta de Agua y Drenaje (JAD, Water and Drainage Council) water utility's neoliberal demand-management/cost-recovery program in Matamoros, Tamaulipas, Mexico, documenting institutional/administrative mechanisms including water-meter installation (targeting wealthy neighborhoods first, then extended to the majority), debt-amnesty and payment-plan programs, and disconnection/fine enforcement for wasteful use -- all operating within a legal constraint that 'by law, cannot be denied the service' since water is recognized as more a civil right than a commodity in Mexico. Documents extension of water lines and communal taps to poor peripheral immigrant neighborhoods alongside enforcement targeting the wealthy first. A genuine institutional/administrative mechanism (cost-recovery/tariff enforcement, water-meter rollout sequencing) study with documented differential water-access/affordability dynamics for poor vs. wealthy neighborhoods.",
    "R5614863C8D6E": "Jemmali & Amara 2015 (Applied Research in Quality of Life) quantitative study applying the World Bank's Human Opportunity Index (HOI) methodology (logistic regressions on seven 'circumstance' variables not controllable by individuals, per Roemer's theory) to assess inequality in access to water, sanitation, and electricity across Tunisian regions. Finds large and statistically significant disparities in access to safe water and sanitation between eastern (littoral) and western (inland) regions, with residence area, household-head education level, and per capita household expenditure identified as the most important circumstances driving regional disparities. A quantitative disparity-documentation study of water/sanitation access inequality by region and socioeconomic circumstance, informing potential policy targeting.",
    "R555884F9D440": "Dawson 2010 (Citizenship Studies) case study of Soweto's 'water war,' South Africa, examining the Operation Gcin'amanzi prepaid water-meter program and its class-differentiated implementation, analyzing how citizenship and belonging are constructed through residents' differential relationships to formal (metered, paying) versus informal (illegal-connection, resisting) water access. A genuine legal/institutional mechanism (prepaid water metering, disconnection enforcement) study documenting class-based differential water-access outcomes and resident resistance strategies.",
    "R58C7B8CDD09C": "Schoeffel 1995 (Project Appraisal) detailed case study of a failed donor-funded rural water-supply project in a South Pacific island country ('Vaika'), documenting multiple compounding institutional/administrative failure mechanisms: local-government inability to collect water-user fees due to widespread 'no tax' political opposition; complete exclusion of women from water-user committees and technical training despite women bearing the water-collection burden; customary land-tenure disputes blocking headworks construction; and political-party-based allocation disputes over which villages received service. A rich institutional/administrative-mechanism case study with multiple documented access-barrier mechanisms (fee-collection failure, gender exclusion, land tenure, political discretion) directly producing project failure and denied water access.",
    "R595251DE2748": "Schur 2017 (Journal of Latin American Geography) comparative mixed-methods study (152-household survey, 60 semi-structured interviews, participant observation, 2016 fieldwork, with a 1996 baseline survey) of household water security in two adjacent binational communities (Palomas, Chihuahua and Columbus, New Mexico) sharing the contaminated transboundary Mimbres Basin Aquifer. Finds each local water utility adopted a distinct institutional approach to groundwater contamination -- structured by differing national and binational water policy and institutional parameters -- resulting in centralized filtration technology making water less affordable in Columbus, while decentralized filtration technology in Palomas did not resolve contamination. A genuine institutional/policy-mechanism comparative study directly documenting differential water-affordability and access outcomes shaped by binational institutional parameters.",
}

EXCLUDES = {
    "R5455E07BCDDA": ("E01", "Warner & Bel 2008 (Public Administration) comparative institutional study of local water and solid-waste service delivery arrangements (public monopoly, competitive contracting, hybrid public/private firms) in the US and Spain, concluding that 'managing monopoly may be more important than competition in local service delivery.' A comparative analysis of institutional/ownership-arrangement efficiency and market structure, not an empirical study documenting a specific differential household-access or affordability outcome for a marginalized population; extends the Barraque (Batch 212) and Lee (Batch 212) institutional-comparison-without-documented-access-outcome exclusion precedent. Wrong-topic institutional-efficiency-comparison study."),
    "R5622BFD5874F": ("E01", "Fedulova 2016 (Baltic Journal of Economic Studies) macroeconomic/theoretical study proposing a market-based 'capitalization' mechanism for water resources in Ukraine's regions (Dnipro river basin), addressing industrial and agricultural water-resource management, ecological degradation, and asset depreciation in the water-management complex. A water-RESOURCE-market economics study concerned with industrial/agricultural water use and capital formation, with no discussion of household water/sanitation service access; extends the established water-resource-vs-water-service-access distinction. Wrong-topic water-resource-market economics study."),
    "R592ACB0FBD22": ("E01", "Hu 2011 (Human Ecology) historical-anthropological case study of Ten Mile Inn, a North China village, examining how villagers' worship of the Ninth Dragon God (a water deity) and its varying political fortunes across a century of Nationalist and Communist-era 'anti-superstition' campaigns track village political-authority struggles over water governance. Primarily a religious-political anthropology study of deity worship as a strategy for political legitimacy amid water scarcity, not an empirical study centered on a specific legal/institutional eligibility or access-barrier mechanism. Wrong-topic religious-political anthropology study."),
    "R5C5F26FA769D": ("E01", "Lukasiewicz, Bowmer, Syme & Davidson 2013 (Society & Natural Resources) content-analysis study of eight Australian government water-reform policy documents (national water-resource-management reform, e.g., Murray-Darling Basin-type reforms), applying a distributive/procedural/interactive social-justice framework to assess government intentions in macro-level water-RESOURCE reform policy. Concerned with water-resource allocation and reform policy at a national scale, not household-level water/sanitation service access via a specific legal/institutional eligibility mechanism; extends the established water-resource-vs-water-service-access distinction. Wrong-topic water-resource-reform-policy study."),
    "R0260D66B3853": ("E03", "Eggers et al. 2018 (International Journal of Environmental Research and Public Health) community-engaged cumulative risk assessment of inorganic well-water contaminants (uranium, manganese, nitrate, zinc, arsenic) on the Crow Reservation, Montana, finding more than 39% of tested wells unsafe by Hazard Index calculation. An exposure-science/health-risk-assessment study of well-water quality/contamination, not an empirical study of a legal/institutional eligibility or access-barrier mechanism's effect on water-service access. Wrong exposure -- water-quality-only study."),
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
    print(f"Batch 215 processed: {n_inc} includes, {n_exc} excludes.")
