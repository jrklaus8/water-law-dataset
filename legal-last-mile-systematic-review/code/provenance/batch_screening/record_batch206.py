#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R2281173EAC98": "White, Murphy & Spence 2012 (International Indigenous Policy Journal) policy-analysis study of drinking-water safety on Canadian First Nations reserves. Documents the legal/jurisdictional mechanism whereby reserve lands fall under federal (not provincial/territorial) responsibility, with three federal departments (AANDC, Health Canada, Environment Canada) sharing fragmented responsibility and a funding model requiring First Nations to cover 20% of operating/maintenance costs. Documents, via Auditor General reports and Health Canada data, that despite over $2.5 billion in federal spending since 1996, 119 of over 600 First Nations communities remained under water advisories as of August 2012, with the Auditor General finding reserves 'years away' from parity with off-reserve water protection. Extends the indigenous/legal-jurisdiction-mechanism precedent (Mogomotsi et al Botswana, S1018).",
    "R25C72141A46C": "Snider 2004 (Social & Legal Studies) case study of the May 2000 E. coli contamination of Walkerton, Ontario's drinking water supply, which killed seven people and sickened 2,300. Documents that a formal Public Inquiry (the O'Connor Report, following 114 witnesses over nine months) directly attributed the disaster to specific institutional/regulatory policy choices under Ontario's neo-liberal 'Common Sense Revolution' government -- the decimation of the Ministry of the Environment and the redefinition of regulation as mere 'communication with stakeholders' -- and forced government re-regulation and re-staffing. A rigorously documented legal/institutional deregulation mechanism directly and measurably producing a severe water-safety/access-quality outcome, evidenced by a formal judicial inquiry.",
    "R2965A86006E5": "Zaki & Amin 2009 (Urban Studies) household-level empirical study of Thailand's first water-supply privatisation scheme, implemented in Pathumthani province (Bangkok Metropolitan Region) in 1998. Uses household-level survey data for poor communities (defined by community and income status) to document that privatisation was associated with a significant improvement in piped-water access despite increased connection costs and monthly charges, alongside improved water quality/service and prospects for improved tenure status among informal-settlement residents. A genuine household-level empirical study directly examining a specific institutional/legal mechanism's (privatisation) measured effect on water-access outcomes for the urban poor.",
    "R2B590CAA2B94": "Graham, Desai & McFarlane 2013 (Public Culture) nine-month ethnographic study of water politics in Mumbai informal settlements (Rafinagar and other sites). Documents new legal sanctions criminalizing 'water theft' by slum dwellers (prosecution under the nonbailable Prevention of Damages to Public Property Act, backed by police raids and arrests), and documents the Brihanmumbai Municipal Corporation's (BMC) differentiated, institutionally codified water-allocation policy explicitly providing informal-settlement connections only 45 litres/person/day versus 135 litres/person/day for formal residential areas -- a threefold documented institutional disparity. Extends the criminalization-of-informal-water-access and differentiated-institutional-allocation-quota precedents.",
}

EXCLUDES = {
    "RC2AB966A3236": ("E01", "Chappells & Medd 2012 (Society & Natural Resources) qualitative case study (22 householder interviews) of the concept of 'resilience' in UK water management policy discourse during the 2006 southeast England drought. Examines sociopolitical framings of drought-management resilience across water companies, regulators, and households; not a legal/institutional eligibility, permitting, or tariff mechanism producing documented differential household water-access outcomes. Wrong-topic drought-resilience-policy-discourse study."),
    "RC60181B6DCC6": ("E01", "Sharan 2011 (Indian Economic and Social History Review) colonial urban-environmental history of water in Delhi, 1868-1956, focused explicitly on narratives of water (im)purity, pollution, and technologies of purification rather than on the extent or legal/institutional determinants of water-supply access. Wrong-topic historical water-quality/pollution-discourse study, not a legal/institutional access-mechanism study."),
    "R5D1990E27D97": ("E12", "Mugagga & Nabaasa 2016 (International Soil and Water Conservation Research), a self-labeled 'Review Paper' thematically synthesizing existing literature on water resources' contribution to Sustainable Development Goal achievement across multiple African economic sectors (agriculture, energy, tourism, health, fisheries, trade). Literature-review/synthesis article with no original empirical data collection; wrong study design."),
    "RC7AC4804264A": ("E04", "Guardiola, Garcia-Rubio & Guidi-Gutierrez 2014 (Applied Research in Quality of Life) econometric study (535 households, Sucre, Bolivia) relating residential water-access variables (water cuts, water quality, access quality) to subjective well-being (life satisfaction, water-domain satisfaction) as the outcome. Water access is the exposure/predictor variable, not a legal/institutional mechanism, and the outcome measured is subjective well-being rather than water access itself. Wrong outcome per the review's scope."),
    "R2512F210717D": ("E12", "Perez Prado 2006 (American Anthropologist) is a book review of the edited volume 'Globalization, Water, and Health: Resource Management in Times of Scarcity' (Whiteford & Whiteford, eds.), summarizing the volume's twelve chapters. A book review, not an original empirical study; wrong study design."),
    "R26BC497EB17E": ("E01", "Hardy 2014 (Journal of the History of Medicine and Allied Sciences) historical epidemiology study comparing scientific and public-health strategies for typhoid fever control in America and England, c. 1910-50 (bacteriology, immunization, carrier management, milk pasteurization). A disease-control public-health history study; no legal/institutional water-access-eligibility mechanism is examined. Wrong-topic historical disease-control study."),
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
    print(f"Batch 206 processed: {n_inc} includes, {n_exc} excludes.")
