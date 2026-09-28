#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R5C1AE58C70FF": "Bond 2012 (Third World Quarterly) political history of South African community-based social movements since the mid-1980s, with extensive documentation of water-specific institutional mechanisms and struggles: Johannesburg Water's prepaid water-meter rollout beginning in Orange Farm (prompting the Orange Farm Crisis Water Committee); the 'Free Basic Water' policy (nominally 6,000 litres/household/month) whose sharply convex second-tier tariff block disproportionately burdened poor households using more than 6,000 litres/month while wealthier flat-rate high-volume users faced minimal increases; and mass water disconnections (officially 1.5 million people/year) triggering township protests, a 1998 legal/regulatory campaign against Lesotho Highlands Water Project cost-driven pricing, and a documented infant death directly linked to a water cutoff. A genuine legal/institutional mechanism (Free Basic Water tariff design, prepaid metering, disconnection enforcement) study with extensively documented differential water-access/affordability outcomes for the poor.",
    "R5C0FB7C8A56E": "Ducrot & Bourblanc 2017 (Natural Resources Forum) case study examining the equity considerations of a rural water and sanitation programme in a district of semi-arid Mozambique, analyzing contradictions between the pro-poor equity strategy embedded in the programme's design, planning and implementation, and its actual delivered outcomes. Finds that even an explicitly pro-poor programme strategy can fall short of delivering genuine equity, and that overlooking local perceptions of equity directly undermines communities' capacity/willingness to maintain their water points. A genuine institutional/administrative-design mechanism study directly examining a rural water-access program's equity outcomes.",
    "R61589A3544B4": "Galaz 2004 (Environmental Politics) game-theoretic and empirical study of Chile's tradable water-rights market -- a legal institution promoted by the World Bank and other international organizations as a model solution to water scarcity -- finding that the introduction of this water market has created 'an obvious incentive to violate the water rights of underprivileged users,' contradicting official claims that negative social consequences of the Chilean water market have been limited. A genuine legal/institutional mechanism (tradable water-rights market) study directly documenting differential water-access/rights-security risk for poor water users under a market-based legal reform.",
    "R5FAEF4C373E7": "Shandra, Shandra & London 2012 (Journal of Poverty) cross-national two-way fixed-effects regression study (30 Sub-Saharan African nations, 1990-2005) testing whether International Monetary Fund structural adjustment adversely affects infant mortality, finding higher levels of IMF structural adjustment correspond with higher infant mortality, operating indirectly through several mediating pathways including access to an improved water and sanitation source (alongside HIV prevalence, female educational attainment, debt service, foreign investment, international trade, and GNP per capita). An institutional/economic-policy mechanism (IMF structural adjustment conditionality) study documenting water/sanitation access as one of several confirmed mediating pathways to a health outcome.",
    "R60EF6EE70FE0": "Birkenholtz 2010 (Environment and Planning A) political-ecological study (2007 household survey of six Jaipur, India neighborhoods stratified by class; follow-up household interviews 2007 and 2009; interviews with public water-supply managers and private water-tanker vendors) of the transformation of Jaipur's centralized urban water-supply network into a 'full-cost-recovery' system. Finds that spatially uneven network expansion and intermittent flow, combined with historical axes of political-economic difference, produce uneven adaptive responses (waiting on water, private tubewell construction, private tanker purchases) that are exacerbating disparities in access to drinking water, while the cost-recovery reform has left the public utility unable to actually recover costs. A genuine institutional/administrative-mechanism (full-cost-recovery tariff reform) study with documented class-differentiated water-access outcomes.",
}

EXCLUDES = {
    "R5AC1E717B5D7": ("E01", "Taylor 2014 (International Journal of Regional and Local History) historical case study of the lengthy, contested political process by which the town of Sevenoaks, Kent solved its sewage/sanitary problem (1871-1882), focusing on the institutional platform provided by the Local Board and the leadership skills of local politician Major James German. A historical narrative of institutional/political leadership dynamics in achieving sanitary reform, without documenting a specific differential-access-exclusion outcome for a marginalized subpopulation; extends the established historical-institution-without-documented-access-outcome exclusion precedent (Barraque, Lee, Batch 212). Wrong-topic institutional-political history."),
    "R5CF5ED5FBF8F": ("E01", "Hoag 2006 (Peace Review) historical/ethnographic essay on gender and water-resource development in Africa (dam construction, wetland/fisheries conservation), centered on the Rufiji Delta, Tanzania case, documenting women's historical exclusion from and gradual inclusion in participatory natural-resource-management decision-making (REMP project). Primarily a water-RESOURCE development/conservation participation study (dams, wetlands, fisheries), not a household water-SERVICE access-eligibility mechanism study; extends the established water-resource-vs-water-service-access distinction. Wrong-topic water-resource-development gender-participation study."),
    "R5B9459402927": ("E01", "Moore 2014 (Environmental Politics) political-science study of China's South-North Water Transfer Project (SNWTP), evaluating Ecological Modernisation and Authoritarian Environmentalism theories against this technocratic mega-infrastructure project's high social, economic and environmental costs. A water-RESOURCE mega-infrastructure and authoritarian-environmental-politics study, not a household water-service access-eligibility mechanism study; extends the established water-resource-vs-water-service-access distinction. Wrong-topic water-resource-infrastructure-politics study."),
    "R63A9A75133CE": ("E01", "Boucheron 2001 (Urban History) detailed medieval institutional/legal history of water governance in Milan, c.1200-1500, examining juridical distinctions of public/private water, the creation of a specialized water-management magistracy, and princely arbitration of disputes among elite commercial/agricultural water users (millers, merchants, irrigators). Explicitly notes Milan never needed public fountains or a centralized drinking-water-service institution because private well-digging was accessible to all; the article's institutional/legal analysis concerns elite economic-use water-resource allocation, not household water-SERVICE access. Extends the established historical-institution-without-documented-household-access-outcome exclusion precedent. Wrong-topic medieval water-resource-governance history."),
    "R649B644170D9": ("E12", "Sternlieb & Laituri 2010 (Journal of Contemporary Water Research & Education) conceptual/methodological review of environmental indicator frameworks (Pressure-State-Response, DPSIR, Water Poverty Index, Environmental Sustainability Index) used to evaluate 'hydrophilanthropy' (NGO/foreign-aid funding quality) for water, sanitation and hygiene programs. A conceptual review and critique of indicator-framework methodology; no original empirical data collection or analysis of a specific legal/institutional access-eligibility mechanism. Conceptual/methodological review, no original empirical data."),
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
    print(f"Batch 216 processed: {n_inc} includes, {n_exc} excludes.")
