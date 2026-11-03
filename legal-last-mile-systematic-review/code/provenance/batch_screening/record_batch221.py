#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R1E3F115E2D74": "Botton & de Gouvello 2008 (Geoforum) institutional/regulatory case study of water and sanitation service provision in the Buenos Aires metropolitan region (BAMR), documenting institutional fragmentation across numerous service providers resulting in differentiated access to services. Finds the two regional regulators (ETOSS for the AASA concession area, ORAB for the rest of the BAMR) apply divergent regulatory tolerance for alternative/informal water-access methods: ETOSS's concession agreement designated AASA as the sole authorized provider and required private wells to be blocked up during network expansion, while ORAB tolerates private wells, illegal connections, and 'desvinculados' informal collective networks, the latter later granted institutional recognition via provincial decree 878/2003. A rigorous institutional/regulatory-fragmentation mechanism study directly documenting how differing regulatory frameworks produce differentiated formal/informal water-access opportunities for non-connected users.",
    "R20599F7A50A1": "Whittington 2003 (Water Policy) policy-reform analysis proposing a package of water tariff and connection-policy reforms for South Asian cities, explicitly finding that current tariffs 'are not helping the majority of the poor households, many of whom are not connected to the piped distribution system,' and recommending specific pro-poor institutional/legal mechanisms: ensuring poor households can obtain a private water connection when they want it, subsidizing upfront connection costs rather than volumetric use, providing public taps as a source of last resort, legalizing water vending and selling by neighbors, and not granting private operators exclusive service-area rights. A rigorous institutional/legal-mechanism policy analysis directly targeting connection-eligibility and legal-status barriers to formal water access for the poor.",
    "R71410CC8C846": "Adubofour, Obiri-Danso & Quansah 2013 (Environment and Urbanization) quantitative household survey (331 households in Aboabo, 457 in Asawase, plus 33 key-informant interviews) of water and sanitation coverage in two urban slum Muslim communities in Kumasi, Ghana, whose settlements are 'classified as illegal by city authorities.' Documents that many residents using pipe-borne water 'were not legally connected to a private tap at the household level because of low income levels,' relying instead on illegal tap connections or purchasing water from neighbors at 10-11 times the official block-tariff rate (35.86 cents/m3 official vs. US$3.45-3.83/m3 informal purchase); also documents landlords preventing on-plot latrine construction and a 'pay-to-dump' solid-waste fee scheme low-income households avoid by illegal dumping. A rigorous quantitative survey directly documenting legal-status-based exclusion from formal water connections and specific fee/landlord barriers to sanitation access for the urban poor.",
    "R704B148C5117": "Willis, Pearce, McCarthy, Ryan & Wadham 2008 (Development) institutional case study of the application of Australia's National Water Initiative (NWI) policy framework -- specifically its full-cost-recovery tariff clause (Clause 66(v)) and Community Service Obligation provisions -- to Yarilena, a small Aboriginal homeland community in South Australia. Documents a tiered water-pricing structure (US$0.44/kL for the first 125kL, then $1.03/kL) applied to the community's single bulk water connection despite serving 15 separate households, and the community's internal cost-sharing and infrastructure-management response to comply with NWI requirements. A genuine institutional/legal mechanism study directly examining how a national water-policy tariff and cost-recovery framework applies to and burdens an Indigenous community's collective water access.",
}

EXCLUDES = {
    "R21E676633A38": ("E01", "Bel, Gonzalez-Gomez & Picazo-Tadeo 2013 (International Journal of Water Resources Development) comparative institutional study of water-service privatization and regulatory-agency development in two Spanish regions (Andalusia and Catalonia), documenting market concentration ratios and the institutional design/empowerment of regional water regulators (AAA/Water Observatory, ACA). A study of regulatory-agency institutional architecture and market structure with no documented household-level access-exclusion outcome for any specific population; extends the established institutional-case-study-without-documented-access-outcome exclusion precedent (Barraque 2007; Lee 2014, Batch 212)."),
    "R727E74956984": ("E01", "Sandhu (year not captured), 'Vulnerability Dimensions and Access to Affordable Housing: The Case of the Waste Picker Community in Amritsar City, India,' a study primarily examining affordable-housing access and vulnerability for a waste-picker community, with water supply and sanitation mentioned only as descriptive background living-condition indicators rather than as the subject of a specific legal/institutional access-eligibility mechanism. Wrong-topic housing-vulnerability study with water only tangential."),
    "R74287BEE0595": ("E01", "Kotze & Mathola 2012 (Urban Forum) survey-based (120 households) resident-satisfaction study of South Africa's Urban Renewal Programme in Alexandra, Johannesburg, covering housing, sanitation, water supply, electricity, health, education and recreational facilities together. A broad multi-service urban-renewal satisfaction survey without isolating a specific legal/institutional mechanism governing water/sanitation access-eligibility; extends the established broad-multi-service-survey exclusion precedent (Sperling, Romero-Lankao & Beig 2016, Batch 220)."),
    "R72919F1AC937": ("E03", "Caldwell, Caldwell, Mitra & Smith 2003 (Social Science & Medicine) national survey study of arsenic contamination in Bangladeshi rural tubewells, examining the tradeoff between arsenic-exposure risk and the convenience/hygiene benefits of household tubewell ownership. A water-quality/contamination-exposure study, not a legal/institutional water-access eligibility mechanism study; extends the established water-quality-focus exclusion precedent (Khabo-Mmekoa & Momba 2019, Batch 220; Eggers et al. 2018, Batch 215)."),
    "R72F429CD88E3": ("E12", "Wutich, Jepson, Stoler, Thomson, Kooy, Brewis, Staddon & Meehan 2021 (Journal of the American Water Resources Association) conceptual agenda-setting article proposing a Household Water Insecurity (HWISE) research approach covering measurement, monitoring and management, synthesizing prior scale-development and ICT-monitoring literature. A conceptual/agenda-setting synthesis article with no original empirical data collected by the authors; extends the established review-paper exclusion precedent (Aiyer 2007; Gero et al. 2014, Batch 220)."),
    "R5D43547CB77D": ("E05", "Mpanga 2016 (African Human Rights Law Journal), 'Interpreting the human right to water as a means to advance its enforcement in Uganda,' a purely doctrinal legal-academic analysis proposing that Ugandan courts adopt a teleological interpretive approach to read an enforceable constitutional right to water into the 1995 Constitution's National Objectives and Directive Principles. A legal-interpretive/doctrinal argument with no empirical case study, fieldwork, or documented access-outcome evidence -- the right to water 'has not yet been adjudicated upon by the courts' in Uganda. No empirical evidence; matches exclusion code E05."),
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
    print(f"Batch 221 processed: {n_inc} includes, {n_exc} excludes.")
