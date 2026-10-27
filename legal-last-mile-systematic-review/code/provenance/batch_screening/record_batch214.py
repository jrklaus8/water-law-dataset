#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R527BCF310148": "Massey 2014 (Habitat International) governmentality/counter-conduct case study of two upgraded informal settlements (Makhaza and New Rest, Cape Town, South Africa), documenting that government housing/infrastructure-upgrading programs failed to meet residents' actual needs, prompting resident 'counter-conduct' -- most prevalently the establishment of illegal electricity and water connections alongside backyard-shack construction and informal home-based businesses -- as a response to the conflicting governmentalities between residents and the state's upgrading institutions. A genuine institutional/administrative mechanism (government upgrading-program design failing to meet needs) study with documented resident resort to illegal water-connection practices as an access outcome.",
    "R5209A3D2844E": "Acey 2010 (Gender & Development) mixed-methods study (783 household ethnographic surveys across 18 neighborhoods, plus semi-structured interviews) of women's and men's responses to urban water-supply problems in Lagos and Benin City, Nigeria, using Hirschman's exit-voice-loyalty framework. Finds women are largely excluded from decision-making in the water sector through voluntary associations (male-dominated neighbourhood/community-development associations facilitate 'exit' behavior rather than institutional engagement, while women's religious-association membership is linked to 'voice' use), and documents institutional/procedural barriers to complaint (e.g., water-utility complaints require property-ownership documentation that renters/women often lack). A genuine institutional/participatory mechanism study (gendered exclusion from water-governance voice channels) with documented differential water-access-improvement outcomes by gender.",
    "R553025EB9A0D": "Hoque & Hoque 1994 (Health Policy and Planning) evaluation study of a two-year multi-agency NGO partnership Water Supply and Sanitation project in rural Bangladesh (295 partner NGOs, ~100,000 people provided handpump access), based on interviews with 192 families, 32 caretakers, and 42 NGO trainers/field officers. Documents a stark gender disparity in community participation in the institutional site-selection process: male users participated in site selection at essentially all visited sites, while female users participated in only 5 of the visited sites (15%), with non-participating women reporting they were simply never asked. A genuine institutional/administrative-participation mechanism (NGO/government site-selection process) study with a documented gender-differentiated participation outcome directly shaping water/sanitation-facility siting decisions.",
    "R54F56C59F64A": "Marson & Savin 2015 (World Development) panel-data regression study (pooled OLS, fixed and random effects; 225 observations, 22 Sub-Saharan African countries, utility-level data spanning 1995-2009) of the relationship between water-utility operation-and-maintenance cost-recovery ratios (a financial/institutional-regulatory policy mechanism) and change in water-supply coverage. Finds a significant curvilinear (inverted-U) relationship: cost recovery is associated with positive and significant coefficients on coverage increases up to a threshold, but the squared cost-recovery term shows a significant negative coefficient, indicating that beyond that threshold, a narrow financial-sustainability focus diverts utility priorities away from expanding universal access -- a genuine regression-based estimate directly isolating a financial/regulatory institutional mechanism's effect on a water-access outcome (coverage change), significant across all tested model specifications; qualifies for effect_sizes.csv under the Family C framework.",
    "R535DF24F0A07": "van Koppen & Schreiner 2014 (Water Policy) legal/institutional analysis of statutory water-licence law in Sub-Saharan Africa generally and South Africa specifically (National Water Act 1998, National Water Resource Strategy-2 2013), identifying three specific forms of legal injustice for small-scale (typically poor, Black) water users: (1) reinforcement of historical colonial-era capture of water-resource ownership that undermined customary water law; (2) administrative discrimination arising from government licensing-capacity constraints disproportionately burdening large numbers of small-scale applicants; and (3) a 'second-class' water entitlement for the smallest-scale users who are exempted from the licence-application requirement altogether. Proposes a transformative legal reform (Priority General Authorisations) to equalize access. A rigorous statutory-law analysis directly documenting a legal/institutional licensing mechanism's differential water-access effects on poor and historically marginalized users.",
}

EXCLUDES = {
    "R4FF8291DD424": ("E01", "Godlewski 2010 (Journal of Muslim Minority Affairs) international-relations/conflict-studies essay applying Realist theory to Israeli water politics in the Occupied West Bank and Gaza, arguing Israeli control of over 80% of West Bank fresh water resources perpetuates the Israeli-Palestinian conflict and obstructs the peace process. A geopolitical/international water-resource-conflict analysis synthesizing existing literature (no original empirical fieldwork or data collection described), not an empirical study of a legal/institutional mechanism's effect on household water-SERVICE access; extends the established water-resource-vs-water-service-access distinction (cf. Abers & Keck, Batch 209; Wong, Batch 213). Wrong-topic geopolitical water-resource-conflict essay."),
    "R526DB7DFDBEF": ("E01", "Proskuryakova, Saritas & Sivaev 2018 (Journal of Cleaner Production) foresight/scenario-planning methodology study developing global water-sector trend analysis and future scenarios for sustainable development in Russia. A futures/scenario-planning study of water-sector trends, not an empirical study of a specific legal/institutional eligibility or access-barrier mechanism's effect on household water access. Wrong-topic scenario-planning/foresight study."),
    "R4FFEE7FE13E6": ("E01", "Kulkarni & Shankar 2014 (Local Environment) conceptual/theoretical analysis of groundwater as a common-pool resource in India, examining competition between domestic, agricultural, and industrial uses/users across different hydrogeological settings, and calling for governance institutions sensitive to this competition. A groundwater-RESOURCE governance and competition study (irrigation, industry, domestic uses collectively), not an empirical study of a specific legal/institutional mechanism's differential effect on household water-SERVICE access; extends the established water-resource-vs-water-service-access distinction. Wrong-topic water-resource-competition study."),
    "R52495F14FBEB": ("E01", "Kot, Gagnon & Castleden 2015 (Water Policy) qualitative interview study (7 small Canadian community drinking-water systems; water operators, consumers, decision-makers) examining the human, financial, governance, and technical factors shaping how small water systems respond to and align with drinking-water-quality regulatory compliance challenges. An institutional-capacity/regulatory-compliance study concerned with utilities' ability to meet water-quality regulations, not a legal/institutional mechanism's differential effect on household-level water-service access or eligibility; extends the Teodoro & Switzer (Batch 210) institutional-capacity/regulatory-compliance exclusion precedent. Wrong-topic regulatory-compliance-capacity study."),
    "R54542BFFD781": ("E01", "Reddy & Snehalatha 2011 (Indian Journal of Gender Studies) fieldwork-based study (two urban slums, Hyderabad, India) exploring what sanitation and personal hygiene mean to poor and vulnerable women, examining locally perceived notions of cleanliness, the gendered division of sanitation tasks, and cultural/psychological dimensions of sanitation practice. Primarily a socio-cultural/perceptions study of the meaning and gendered performance of sanitation and hygiene, not an empirical study centered on a specific legal/institutional eligibility or access-barrier mechanism's differential effect on sanitation-service access. Wrong-topic socio-cultural/perceptions study."),
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
    print(f"Batch 214 processed: {n_inc} includes, {n_exc} excludes.")
