#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R835937265185": "Baijius & Patrick 2019 (Water, MDPI), 'We Don't Drink the Water Here: The Reproduction of Undrinkable Water for First Nations in Canada.' A political-ecology case study using multiple First Nation source-water-protection plans on the Canadian Prairie to critically assess 'what roles political structures and institutions have in the continued exclusion of Indigenous peoples from water governance.' Documents that boil-water advisories are 2.5x more frequent for First Nation than non-First Nation communities and waterborne infections are 26x the national average, tracing causation to colonial institutional arrangements (the Indian Act reservation system, federal fiduciary/constitutional responsibility) that structurally exclude First Nations from water governance and decision-making. A rigorous institutional/legal-mechanism case study directly documenting a jurisdictional/governance-exclusion mechanism's effect on water access and quality outcomes.",
    "R93D7F84D81B3": "Katomero & Georgiadou 2018 (ISPRS Int. J. Geo-Information), 'The Elephant in the Room: Informality in Tanzania's Rural Waterscape.' Using organization theory and institutional theory (Helmke & Levitsky typology), examines how formal water-sector institutions (Community Owned Water Supply Organizations under Tanzania's National Water Policy) interact with informal programs, communication channels and sanction/reward systems in two districts (Hai, Siha) achieving superior rural water access, directly tied to SDG Target 6.1 (universal and equitable drinking-water access). A rigorous institutional-arrangement case study documenting how formal/informal institutional complementarity shapes rural water-access outcomes.",
    "RB5257A44EC80": "Patrick, Grant & Bharadwaj 2019 (Water, MDPI), 'Reclaiming Indigenous Planning as a Pathway to Local Water Security.' Institutional/legal case study of Muskowekwan First Nation (Saskatchewan) documenting how the Indian Act's 1876 reservation system created lands administratively disconnected from provincial infrastructure planning, while the Constitution Act 1982 assigns water-resource responsibility to provinces but leaves First Nations reserves under federal jurisdiction -- a jurisdictional fragmentation producing, in Saskatchewan, only 74% on-reserve piped water service versus 21% truck delivery (prone to contamination) and the remainder private wells, alongside a national rate of 85 concurrent drinking/boil-water advisories on reserves. Documents a five-stage community-based source-water-protection planning framework developed as an institutional/self-governance response. A rigorous jurisdictional/institutional-mechanism case study directly documenting differential water-service-type access attributable to federal/provincial governance fragmentation under the Indian Act.",
    "R132A30EE97F5": "Jama & Mourad 2019 (Sustainability, MDPI), 'Water Services Sustainability: Institutional Arrangements and Shared Responsibilities' (Garowe, Puntland, Somalia). Interview-based institutional case study documenting overlapping, uncoordinated mandates between two governmental water agencies (PSAWEN, Ministry of Environment) and a public-private-partnership water utility (NUWACO) operating under a concession contract. Finds the PPP's untreated tap water is unaffordable for many low-income households (connection fee $180; water priced such that poor households spend up to 10% of income on drinking water) and that 'the private company made water an economic good rather than a right that every citizen should enjoy, which affected the poor people, especially the children.' A rigorous institutional-fragmentation/PPP-arrangement case study directly documenting how uncoordinated institutional mandates and a concession-based pricing structure produce differential water-affordability/access outcomes for the poor.",
}

EXCLUDES = {
    "R7B4238C0F691": ("E04", "Baird, Plummer, Dupont & Carter 2015 (Nature and Culture), 'Perceptions of Water Quality in First Nations Communities Exploring the Role of Context.' A multiple case-study survey (Likert-scale/multiple-choice questionnaires, n=100 per community) of resident PERCEPTIONS of water quality, cultural importance and governance satisfaction across three Ontario First Nations communities. While it references institutional/regulatory-gap facts as background (e.g., reliance on guidelines/funding arrangements rather than binding law), the study's actual method and results are a perceptions/attitudes survey, not an analysis of a documented institutional access-eligibility mechanism. Matches the established attitudes/perceptions wrong-outcome exclusion precedent (Sperling et al. 2016, Batch 218; Kotze & Mathola 2012, Batch 221)."),
    "R7A1EB1512BE4": ("E04", "Huda, Unicomb, Johnston, Halder, Sharker & Luby 2012 (Social Science & Medicine), interim evaluation of the SHEWA-B program's effect on childhood diarrhea and respiratory illness in rural Bangladesh via a large-scale handwashing/hygiene behavior-change intervention (500 intervention / 500 control households). A child-health-outcome behavior-change RCT-style evaluation with no legal/institutional water-access-eligibility mechanism; matches the established wrong-outcome (child health/behavior) exclusion precedent."),
    "R9ABC6050547A": ("E04", "Jackson, Hatton MacDonald & Bark 2019 (Water Resources Research), 'Public Attitudes to Inequality in Water Distribution: Insights From Preferences for Water Reallocation From Irrigators to Aboriginal Australians.' A contingent-valuation survey of the general (predominantly non-Indigenous) Murray-Darling Basin public's willingness-to-pay for water reallocation to Aboriginal communities. Measures public opinion/willingness-to-pay, not a documented institutional mechanism's effect on Aboriginal communities' actual water access; extends the established public-attitudes/priority-ranking wrong-outcome exclusion precedent (Sperling et al. 2016, Batch 218)."),
    "RAB0CE1247452": ("E06", "Yulistyorini, Camargo-Valero, Sukarni, Suryoputro, Mujiyono, Santoso & Rahayu 2019 (Processes, MDPI), 'Performance of Anaerobic Baffled Reactor for Decentralized Wastewater Treatment in Urban Malang, Indonesia.' A purely engineering/water-quality-treatment-performance study of SANIMAS ABR units (BOD/TSS/TKN/TP removal efficiencies against Indonesian regulatory design criteria). Brief mentions of illegal settlements and connection-cost barriers are incidental background, not the study's focus or quantitative content; extends the established engineering-performance exclusion precedent (Nauges & Strand 2007, Batch 218; Agthe & Billings 1987 and Jiang & Zheng 2014, Batch 220)."),
    "RE4B8992DC140": ("E06", "Snyder, Prentice-Mott, Boera, Mwaki, Alexander & Freeman 2020 (Int. J. Environ. Res. Public Health), 'The Sustainability and Scalability of Private Sector Sanitation Delivery in Urban Informal Settlement Schools: A Mixed Methods Follow Up of a Randomized Trial in Nairobi, Kenya.' A randomized-controlled-trial follow-up comparing facility maintenance/functionality outcomes between private-sector sanitation delivery (Sanergy Fresh Life Toilets) and government-standard delivery in 20 informal-settlement schools. Measures which service-delivery model keeps toilets functional/clean over time -- an infrastructure-performance/service-delivery-model comparison, not a legal/institutional access-eligibility mechanism determining who is excluded from service; extends the established engineering/service-performance exclusion precedent (Yulistyorini et al. 2019, this batch; Jiang & Zheng 2014, Batch 220)."),
    "R6C0638AC2F78": ("E01", "Sinclair, Abba, Zaman, Qadri & Graves 2011 (Cochrane Database of Systematic Reviews), 'Oral vaccines for preventing cholera.' A clinical/medical Cochrane systematic review of oral cholera vaccine efficacy (randomized controlled trials of whole-cell and other vaccine formulations vs. placebo). Wrong topic -- a vaccine-efficacy clinical review unrelated to legal/institutional water-access-eligibility mechanisms; matches the established Cochrane medical-review wrong-topic exclusion precedent (Danso-Appiah et al. 2008, Batch 219)."),
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
    print(f"Batch 223 processed: {n_inc} includes, {n_exc} excludes.")
