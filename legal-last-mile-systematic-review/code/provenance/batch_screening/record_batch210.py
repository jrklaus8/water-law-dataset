#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R3C1D63DD65AB": "Kvartiuk 2016 (Voluntas) quantitative survey study (rural Ukraine, 2012, multi-stakeholder survey of residents/mayors/CBO leaders across two regions) of the effect of non-electoral participation and community-based organizations (CBOs) on local public-goods outcomes. Using SUR and ordered Probit-with-instruments models, finds participation (town hall meeting attendance) and established CBOs are both significantly and positively associated with the quality of local water-supply systems -- a unit increase in town hall meeting participation associated with a 29% increase in probability of a good water-supply situation, and an established CBO associated with a ca. 25% increase -- motivating discussion of water-supply service cooperatives as a functional local-governance arrangement. A genuine regression-based estimate directly isolating an institutional/participatory mechanism's (CBO establishment, non-electoral participation) effect on a water-supply-quality outcome; qualifies for effect_sizes.csv under the Family A framework.",
    "R3F7FD1164835": "Hoogesteger 2012 (Human Organization) in-depth case study of the consolidation of the provincial water users federation Interjuntas-Chimborazo in the Ecuadorian Andes (fieldwork 2008-2010). Documents how the federation's Legal Advisory Office filed formal complaints of corruption, ethnic discrimination, and bribery against the provincial Water Agency (WA), and through sustained lobbying and an 18-day occupation of the WA office by 4,000+ water users (2005), secured the dismissal of the WA director and establishment of a transparent selection process; the resulting WA office is documented as now treating 'all water users... alike without regard to economic, social, regional, or ethnic differences,' with corruption eliminated and a Kichwa-speaking lawyer appointed to serve indigenous water users in their own language. A documented institutional/administrative-mechanism (Water Agency corruption/discriminatory practice) and grassroots-federation intervention directly producing a measured improvement in equitable treatment of marginalized indigenous water users' access to water-rights administration.",
    "R650BE63591AA": "Gonzalez-Gomez, Garcia-Rubio & Gonzalez-Martinez 2014 (Utilities Policy) critical analysis of Spain's urban water-privatization model, based on the authors' own fieldwork assessing the true extent of private-sector participation (addressing a gap in the AEAS survey data, which misses 40% of the population and 88% of municipalities) and market-structure concentration, finding a clear oligopolistically dominant private-sector position has formed. Documents (citing Martinez-Espineira et al.'s nationally representative database analysis) that municipalities with privatized water-service management have higher water prices at any level of consumption than publicly managed municipalities, and identifies specific institutional/regulatory deficiencies (absence of competition, regulatory gaps, lack of transparency, low citizen participation) underlying this affordability disparity, proposing institutional reforms. A genuine institutional-mechanism (privatization/ownership-structure) study documenting an affordability outcome disparity via the authors' own fieldwork and secondary-database synthesis.",
}

EXCLUDES = {
    "R3B2D2E5CD09B": ("E01", "Teodoro & Switzer 2016 (Public Administration Review) logistic regression study (n=8,962 U.S. municipal water utilities) of a resource-endowment theory of human capital and agency performance, using utility compliance with the Safe Drinking Water Act as the empirical subject. Finds labor-market human capital availability and organizational scale jointly predict regulatory compliance with high-complexity health requirements. An institutional-capacity/regulatory-compliance study; the outcome is utility compliance with federal drinking-water regulations, not household-level differential water-access, connection, or affordability outcomes tied to a specific legal/institutional eligibility or barrier mechanism. Wrong-topic institutional-capacity study."),
    "R39990BF4F869": ("E01", "Neri Serneri 2007 (Journal of Urban History) historical study of the construction of modern urban water-supply and sewerage networks in Italian cities, 1880-1920, examining the functional/technical drivers (population growth, industrialization, hygiene) of infrastructure modernization and the shift from private to municipal water-system control. A macro-level history of infrastructure and technology adoption across Italian cities; while it discusses the private-to-municipal ownership shift, it does not document a specific legal/institutional eligibility mechanism's differential effect on household-level water access. Wrong-topic infrastructure-development history."),
    "R401566C6D1F6": ("E01", "Price, Fielding & Leviston 2012 (Society & Natural Resources) qualitative focus-group study (Toowoomba, Australia) of the cultural values and psychological needs (cultural theory; motivated social cognition) underlying supporters' and opponents' voting behavior in a 2006 referendum on a proposed potable recycled-water scheme. A public-attitudes/cognition study of a specific technology referendum, not an empirical study of a legal/institutional eligibility or barrier mechanism's effect on water access. Wrong-topic public-attitudes study."),
    "R08D3F4577102": ("E01", "Hope, Foster, Money & Rouse 2012 (Global Policy) forward-looking policy-implications paper on mobile-payment and smart-metering technology innovations for water security in Africa (Kenya and Zambia case studies), synthesizing existing AICD/WHO-UNICEF statistics and expert-ranking survey data on the prospective benefits of mobile water payments. A technology-innovation/policy-prospects paper; while it references documented price disparities between unregulated vendors and formal utilities, its primary empirical contribution is a speculative benefit-ranking exercise about future mobile-payment adoption rather than a rigorous measurement of an existing legal/institutional access-eligibility mechanism's effect. Wrong-topic technology-innovation study."),
    "R406FC36CCAAF": ("E05", "Vidal de Llobatera 2003 (Capitalism Nature Socialism) short 'Resource Wars' opinion/advocacy column (approximately one page) on Spanish water-utility privatization protests and the National Water Plan, describing corporate concessions and mobilizations against neoliberal water policy in narrative/advocacy form. No methodology, no data collection, no empirical evidence base. No empirical evidence."),
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
    assert len(INCLUDES) + len(EXCLUDES) == 8
    decided, _ = process_db()
    assert len(decided) == 8
    append_exclusion_log(decided)
    n_inc = sum(1 for r in decided if r["final_decision"] == "include")
    n_exc = sum(1 for r in decided if r["final_decision"] == "exclude")
    print(f"Batch 210 processed: {n_inc} includes, {n_exc} excludes (2 wrong_file_retrieved handled separately).")
