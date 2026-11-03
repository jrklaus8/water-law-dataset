#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R23FC463CA51F": "Drew 2008 (Development) case study of civil-society groundwater-rights activism in Mehdiganj, India. Documents India's 73rd/74th Constitutional Amendments, which empower panchayats (local governing bodies) to regulate natural-resource use, upheld by a Joint Parliamentary Committee report as authorizing panchayats to restrict commercial groundwater extraction. Documents the Plachimada, Kerala precedent in which the Perumatty Panchayat used this legal authority to support community opposition to a Coca-Cola bottling plant's groundwater mining, leading to a Public Interest Litigation and a court-ordered plant closure in 2004 -- a directly measured legal/institutional-mechanism outcome protecting community water access. Extends the legal-recognition-of-local-governing-body-authority-over-water precedent.",
    "RC1FEB7393384": "Loftus 2007 (International Journal of Urban and Regional Research) study, combining political-ecology/feminist-standpoint theory with 20 semi-structured interviews across three areas of Durban, South Africa. Documents eThekwini Water Services' differentiated institutional/technical connection mechanism (a low-pressure 'ground tank' system for informal areas vs. full-pressure domestic connections) and a tiered tariff table cross-subsidizing free basic water by consumption volume and connection type, tied to documented differential outcomes: 100,000 new households connected since apartheid's end, but rural residents recently connected via the ground-tank system 'have not encountered the same difficulties with payments as those in townships and informal settlements.' Extends the tariff/connection-type-differentiation-mechanism precedent for South African water institutions (cf. Gowlland-Gualtieri S1014, Muller S1016).",
    "RC377927F144E": "Driessen 2008 (Development) case study of the 'Social Control' participatory-governance model institutionalized in SEMAPA, Cochabamba's public water utility, following Bolivia's 2000 Water War. Documents the legal/institutional creation of elected Citizen Directors (4 of 9 SEMAPA Directory seats) and Basic Services Committees, institutional capture/corruption by municipal elites undermining service equity, and a documented infrastructure-expansion Plan targeting the poorest, least-connected Southern Zone of Cochabamba, alongside the marginalization of civil-society groups (e.g., ASICA-Sur) from decision-making. Extends the institutional-capture/participatory-governance-model precedent (Giglioli & Swyngedouw Sicily, S990).",
    "RC1D14599F0AE": "Tardanico 2008 (Journal of Development Studies) regression-based study (heterogeneous choice ordinal models; World Bank household survey, N=1,243 sub-sample of N=1,426) of post-civil-war San Salvador, El Salvador, examining household macro-structural and socio-institutional assets -- including formal vs. informal dwelling-title ownership and reported community/government intervention establishing household municipal water service -- as predictors of municipal service-coverage deficits (9% of the sub-sample reports a water deficit) and hazard vulnerability. A genuine regression-based analysis directly incorporating legal/institutional tenure and service-establishment variables as predictors of water-service-coverage outcomes.",
    "RC331942401C8": "Anand 2004 (International Journal of Technology Management and Sustainable Development) case study of water-access entitlements in Chennai, India. Documents the Chennai Metropolitan Water Supply and Sewerage Board (Metro Water Board)'s institutional accountability structure -- a principal-agent arrangement in which the Board, though supplying only Chennai City, is legally accountable to the state legislature (representing all of Tamil Nadu) rather than to Chennai's own population, given the absence (unlike Mumbai, Kolkata, or Bangalore) of an elected Chennai local government during the relevant period. Documents, via household income/water-endowment data (Tables 2-3), that while official statistics report over 90% water-supply access in Chennai, approximately 31% of households lack secure water entitlements, with inequality closely tied to income and land ownership. Extends the institutional-accountability-structure/documented-entitlement-inequality precedent.",
}

EXCLUDES = {
    "RBFD1D75DFEC0": ("E01", "Alston & Mason 2008 (Rural Society) study of the gender composition of water-decision-making bodies (National Water Commission, Catchment Management Authorities, Murray-Darling Basin Authority) in Australia's Murray-Darling Basin. Examines agricultural/environmental water-allocation governance and gender representation on decision-making boards, not documented differential household water-ACCESS outcomes. Reapplies the established gender/governance-representation E01 precedent."),
    "RC0A0716E4072": ("E01", "Rahaman, Everett & Neu 2013 (Business and Society Review) qualitative case study (21 interviews) of the business ethics, trust, and morality dimensions of water-services privatization deliberations in Ghana, analyzed through feminist ethics-of-care, Rawlsian justice, and virtue-ethics frameworks. Core focus is stakeholder trust/ethical-perspective analysis of privatization negotiations, not a documented legal/institutional mechanism's measured effect on differential water-access outcomes. Wrong-focus business-ethics/trust-analysis study."),
    "RC165BC72115E": ("E01", "Douglas 2016 (Commonwealth & Comparative Politics) comparative study of Public Value Management practices across 16 mixed public utilities (airport, seaport, bus transportation, drinking water, electricity, gasoline, household waste) in three Caribbean territories (Aruba, Curacao, St Kitts). A general public-management-theory application study across multiple non-water-specific utility types; water-access outcomes are not isolated or analyzed separately. Wrong-topic general public-management-effectiveness study."),
    "R24B92E5B8F42": ("E01", "Gondhalekar et al 2013 (Ecological Health: Society, Ecology and Health) mixed-methods study (200-household survey, 70-hotel survey, GIS mapping, interviews) of water scarcity and health (diarrhoeal disease) issues linked to tourism-driven urban growth in Leh Town, Ladakh, India. Focus is on water scarcity/pollution and its health consequences within an urban-planning framework, not a legal/institutional mechanism producing documented differential household water-access outcomes. Wrong-topic water-scarcity/environmental-health study."),
    "RC3824F034384": ("E01", "Meinzen-Dick & Bakker 1999 (Agriculture and Human Values) case study of the Kirindi Oya irrigation system, Sri Lanka, as a multiple-use common-pool resource. Core focus is agricultural/irrigation water management and the institutional structure of Farmers' Organizations; domestic water supply is one minor use category among several (field crops, livestock, fisheries, domestic, other enterprises). Reapplies the established agricultural/irrigation-system multiple-use-commons E01 precedent."),
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
    print(f"Batch 205 processed: {n_inc} includes, {n_exc} excludes.")
