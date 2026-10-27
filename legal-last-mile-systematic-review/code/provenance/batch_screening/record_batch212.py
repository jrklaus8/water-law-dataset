#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R46937097B958": "Heller 2007 (Journal of Comparative Social Welfare) analysis of Brazilian basic sanitation (BS) sector examining the political, institutional and legal aspects of access, tracing the PLANASA concession model (1970s, municipalities granting concessions to state-owned utilities), documented social asymmetries in coverage by income (households earning over 20 minimum wages vs. under 1), region (North/Northeast lower coverage), and institutional arrangement (state vs. municipal utilities), and the 2007 National Sanitation Law (Law No. 11,445) establishing new universalization/equity-oriented institutional framework. A genuine legal/institutional mechanism (concession model, state-vs-municipal utility structure, national sanitation law) study with documented differential water/sanitation access outcomes by income and region.",
    "R4556D8990F42": "Murungi & van Dijk 2014 (Habitat International) empirical study (semi-structured interviews, observation, secondary data) of feacal sludge emptying, transportation and disposal in Kampala, Uganda informal settlements, identifying institutional fragmentation between the public KCCA and private cesspool operators, complete absence of price regulation, and documenting how high, unregulated emptying prices act as a bottleneck excluding poor slum dwellers from formal sanitation-emptying services, pushing them toward illegal manual emptiers who dump sludge in the environment. An institutional/administrative-barrier (lack of price regulation, institutional fragmentation) mechanism study with a documented sanitation-service-affordability/access outcome for informal-settlement residents.",
    "R462B01EA2916": "Gerlach & Franceys 2010 (World Development) comparative case-study analysis of economic regulation's introduction into the water sector across 11 metropolitan areas in Africa and Asia, examining the challenge of reaching all urban consumers, particularly the poor, finding pro-poor regulatory outcomes constrained by inadequate framework conditions and limited understanding of alternative (informal) providers, with regulatory governance itself often vulnerable. A genuine institutional/legal mechanism (economic regulation design) study directly examining its differential effect on access to water services for the urban poor across multiple developing-country cities.",
    "R4624B0F84E67": "van Dijk, Etajak, Mwalwega & Ssempebwa 2014 (Habitat International) empirical study (household surveys and stakeholder interviews in one slum each in Kampala and Dar es Salaam) of sanitation financing and governance structures (households, shared/CBO-managed, government/private toilets), documenting how the ownership/governance-structure of a facility (private household, informally-shared, CBO-managed community toilet, or publicly-approved shared facility) determines fee levels and eligibility/access conditions (e.g., CBO-managed toilets open only to contributing community members). An institutional/administrative-mechanism (governance-structure-dependent eligibility and fee) study with documented differential sanitation-access conditions across facility-governance types in informal settlements.",
    "R497171E0A98B": "Kurup 1991 (Social Indicators Research) case-study account of Kerala's Socio-Economic Units (SEU) programme (Netherlands/Denmark-funded, in partnership with the Kerala Water Authority), documenting how the pre-SEU public-standpost site-selection process (opaque, panchayat-driven, criteria 'not convincing or known') resulted in standposts not located in the areas that most needed them, and how the introduction of a participatory process -- involving Ward Water Committees explicitly identifying and mapping 'deserving areas' (concentrations of below-poverty-line households) -- shifted site-selection to better target poor households for public-standpost water access. An institutional/participatory-mechanism study with a documented before/after improvement in the targeting of water-access provision to the poor.",
}

EXCLUDES = {
    "R482CFD536DF0": ("E01", "Barraque 2007 (Journal of Comparative Social Welfare) in-depth historical institutional analysis of French water-service governance (centralization vs. decentralization, delegation to private companies, joint boards, Conseil d'Etat regulatory oversight of concession contracts) from the 19th century to the present. While a genuine institutional/legal history, the article documents the historical evolution toward near-universal coverage in Western Europe without identifying or measuring a specific institutional/legal eligibility or barrier mechanism's differential access effect on an excluded subpopulation. Extends the Neri Serneri (Batch 210) and McFarlane (Batch 211) macro-institutional-history exclusion precedent. Wrong-topic institutional history without a documented differential-access outcome."),
    "R46CB7FA17E82": ("E06", "Alvarez, Prieto & Zofio 2014 (European Planning Studies) stochastic frontier analysis methodology paper studying cost-efficiency levels and technological characteristics of public infrastructure provision in relation to urban patterns and population density. A purely technical/econometric cost-efficiency methodology study; no legal/institutional eligibility or access-barrier mechanism is examined. Engineering/technical-efficiency-only study."),
    "R4914200BD97B": ("E06", "Grafton, Chu & Kompas 2015 (Journal of Utilities Policy) dynamic economic model deriving an optimal 'golden rule' for the timing of water-supply infrastructure augmentation (e.g., desalination plant commissioning) under cost-of-service tariff regulation, calibrated to Sydney, Australia. A technical/economic optimization exercise concerned with market-wide tariff-setting efficiency and infrastructure-timing, not with a legal/institutional mechanism's differential effect on household-level water access. Engineering-economics optimization study."),
    "R4CCD45F0ECA6": ("E01", "Lee 2014 (Urban History) historical/archival study of piped water supplies managed by civic bodies in medieval English towns (to c. 1550), examining the origins, technologies, finance, management and oversight of civic conduits and their relationship to charitable provision. A genuine institutional history of water-supply governance, but the article documents the general growth of civic/charitable piped-water provision without isolating or measuring a specific legal/institutional eligibility or barrier mechanism's differential access effect on an excluded subpopulation. Wrong-topic institutional history without a documented differential-access outcome."),
    "R4BBE5A2D92EE": ("E01", "Zaato 2015 (Journal of Asian and African Studies) case study of a management contract (MC) used to reform urban water services in Ghana, examining whether contractualism is a suitable public-sector-reform tool and under what conditions contracting can promote efficiency, concluding contractualism is 'a defective tool' for the politically sensitive water sector absent adequate context, task specificity, and creative adaptation. A public-administration/contract-theory case study concerned with organizational efficiency and reform-tool suitability, not with a legal/institutional mechanism's differential effect on household-level water access. Institutional-efficiency/contract-theory study, not an access-outcome study."),
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
    print(f"Batch 212 processed: {n_inc} includes, {n_exc} excludes.")
