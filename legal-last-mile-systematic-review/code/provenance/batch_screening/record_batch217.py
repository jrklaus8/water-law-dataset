#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R653891430501": "Anand 2012 (Ethnography) two-year ethnographic study of Muslim settlers in a northern Mumbai suburb (Premnagar), documenting how residents are rendered 'abject' -- denied, rather than merely lacking, social and political entitlements -- through the deliberate inaction of city (BMC) engineers and technocrats who have left 40-year-old municipal pipes to rust and go dry without replacement, while state/federal legislators sponsor alternative bore-well construction (requiring ~$100 household connection fees plus monthly charges) rather than extending the actual municipal network. A genuine institutional/administrative-discrimination mechanism (deliberate municipal inaction, contentious infrastructural connections) study with documented differential water-access outcomes for a specific marginalized religious/ethnic community.",
    "R6633D02DAFEB": "Silvestre 2012 (Utilities Policy) empirical study using survey data from the Portuguese Water Sector Regulator (ERSAR), examining the relationship between water-service social performance (user prices, service quality) and the institutional arrangement providing the service (public-private partnership vs. corporate public-sector organization). Finds user prices are more strongly related to organizational costs than to ownership/property or management model, while service quality is more strongly related to ownership/property than to costs or management model -- contradicting New Public Management assumptions that PPP participation inevitably yields lower prices and higher quality. A genuine institutional-arrangement (PPP vs. corporate public ownership) comparative study with documented empirical price/quality outcomes directly relevant to water-service affordability and quality.",
    "R64FBAD6F3FDE": "Valerio 2024 (Lex Localis) multi-level institutional governance case study (Multi-Level Governance theory + Institutional Analysis and Development framework; documentary/policy analysis, 2018-2023 administrative/performance data) of urban water governance in Zamboanga City, Philippines, finding persistent institutional fragmentation (overlapping regulatory mandates across LWUA/NWRB/DOH/local government, tariff-approval delays exceeding 12 months, politicized water-district board appointments) produces stagnant service coverage (48% of households in 2022), with the remaining majority relying on wells, communal sources, or vendors -- arrangements that 'typically impose higher effective costs and greater quality risks on poorer households.' A genuine institutional/administrative-fragmentation mechanism study with documented differential water-access/affordability outcomes for the poor.",
    "R66E3FE3817F3": "Panda 2007 (Gender, Technology and Development) critical policy-analysis essay examining gender-mainstreaming rhetoric and practice in Indian water management, analyzing the 'Women, Water and Work' campaign by India's Self-Employed Women's Association (SEWA) and newly-instituted water-sector reforms (including privatization) that marginalize women in decision-making, arguing effective gender mainstreaming requires treating water as a human right rather than superficial inclusion. A critical institutional/policy analysis directly examining how specific water-sector reform mechanisms (privatization, gender-mainstreaming implementation) differentially affect women's water-management roles and access.",
    "R65BF964A8E4D": "Eguavoen 2008 (Development) detailed institutional/legal case study (fieldwork 2004-2006, Nankani settlement, Upper East Region, northern Ghana) of how Ghana's National Community Water and Sanitation Program (NCWSP) -- with its Community Water and Sanitation Agency (CWSA), formal registration/membership requirements, a 5% community-contribution capital-cost fee, and water-user committees -- restricted pre-existing customary equal-use water rights (traditionally open to all community members without formal exclusion). Documents specific exclusion mechanisms: non-resident farmers formally excluded from pump use despite customary rights; some households failing to qualify for years because they could not raise the required community contribution; a hierarchy of restricted use rights imposed on non-members. A rigorous legal/institutional mechanism study documenting how a formal community-based management policy directly restricted and formalized exclusion from water access that had previously been open under customary law.",
    "R67088B57E351": "Antunes & Martins 2020 (Utilities Policy) quantitative fixed-effects panel regression study (111 countries, 1991-2015) of determinants of access to improved water sources, framed around the 2010 UN-recognized human right to water. Finds statistically significant coefficients (Driscoll-Kraay corrected, p<0.01): gross capital formation/investment (positive), agricultural-sector value-added share (negative), vulnerable female employment share (negative, ~0.11 percentage-point decrease in water access per 1 percentage-point increase), primary-school enrollment (positive), and urban population share (positive). A rigorous cross-national panel-regression study of water-access determinants including labor-market and economic-structure variables.",
    "R680EE05D7AEB": "Crook & Ayee 2006 (Development Policy Review) empirical case study of 'street-level' Environmental Health Officers in Kumasi and Accra, Ghana, examining how privatization and contracting-out of environmental sanitation services imposed new client-oriented ways of working on regulatory officials, finding that 'politically protected privatisations' undermined officials' ability to enforce sanitary standards despite officers' otherwise positive organizational adaptation. A genuine institutional/administrative-enforcement mechanism study documenting how privatization reform undermined regulatory enforcement capacity for environmental sanitation.",
    "R123EABE57C5A": "Alam et al. 2020 (International Journal of Environmental Research and Public Health) qualitative assessment (9 key-informant interviews with DWASA and City Corporation officials, 23 focus-group discussions with landlords, tenants, and CBOs across 16 low-income communities) of strategies and barriers to connecting low-income communities to the proposed Dhaka Sanitation Improvement Project sewerage network, Bangladesh. Identifies institutional/infrastructural barriers to formal sewerage connection for low-income communities (inadequate toilet infrastructure, lack of road access, financing/fee-collection challenges) and stakeholder-recommended solutions (income-based or area-based subsidies, equal-division or per-household fee models). A genuine institutional/administrative-mechanism study directly examining barriers to formal sanitation-service connection for low-income urban communities.",
}

EXCLUDES = {
    "R66E21A3EF32C": ("E01", "Zawahri 2006 (Third World Quarterly) comparative international-relations study of transboundary river-basin water treaties, examining what Iraq's Euphrates/Tigris water-security situation can learn institutionally from the Indus Waters Treaty between India and Pakistan. A water-RESOURCE geopolitical/international-treaty study, not a household water-SERVICE access-eligibility mechanism study; extends the established water-resource-vs-water-service-access distinction. Wrong-topic transboundary-treaty-comparison study."),
    "R67A29BF1BE09": ("E01", "Gehrke 2016 (American Journal of Economics and Sociology) historical study of Joseph Chamberlain's 'municipal socialism' program in Birmingham, England (late 19th century), examining the political emergence of municipal ownership of water and gas utilities as part of a broader progressive municipal-reform agenda. A historical institutional-ownership-model narrative without documenting a specific differential-access-exclusion outcome for a marginalized subpopulation; extends the established historical-institution-without-documented-access-outcome exclusion precedent (Barraque, Lee, Boucheron). Wrong-topic municipal-ownership political history."),
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
    print(f"Batch 217 processed: {n_inc} includes, {n_exc} excludes.")
