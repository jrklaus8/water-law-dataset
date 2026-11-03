#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "R014D81805085": "Hanak 2008 (Land Economics), 'Is Water Policy Limiting Residential Growth? Evidence from California.' Fixed-effects/random-effects panel regression (289 jurisdictions, 1994-2003, original statewide land-use survey data) finding that adoption of local water-adequacy screening policies (an administrative-review growth-control mechanism under SB 901/610/221) significantly slowed new residential permitting by 16%-41% depending on specification, while price-based water connection impact fees showed no significant effect. A rigorous regression-based study directly isolating a specific administrative/legal institutional mechanism's (water-adequacy screening review) effect on new housing/water-connection access.",
    "R0327EF4BAA21": "Dos Santos & LeGrand 2013 (Urban Studies), 'Is the Tap Locked? An Event History Analysis of Piped Water Access in Ouagadougou, Burkina Faso.' Cox proportional-hazards regression on residential life-history data finding that residence in a non-zoned (spontaneous/informal) settlement area produces a hazard ratio of 0.14 (zoned periphery reference) for gaining piped water access -- formal connection is 'not possible in non-zoned areas' -- with interaction terms showing renting in a non-zoned periphery area produces a hazard ratio of 0.00 (statistically indistinguishable from impossible). A rigorous regression-based study directly isolating a legal/administrative zoning-status mechanism's effect on piped water access.",
    "R0282D73BD533": "Mukhija & Mason 2013 (Urban Studies), 'Reluctant Cities, Colonias and Municipal Underbounding in the US: Can Cities Be Convinced to Annex Poor Enclaves?' Case study of municipal underbounding (the unwillingness of California cities to annex poor unincorporated colonias lacking potable water and sewer systems), documenting a counter-intuitive case where adjacent cities were convinced to annex poor neighborhoods, with federal infrastructure funding identified as a key enabling institutional mechanism. A rigorous institutional/legal-mechanism case study of municipal boundary/annexation law as a determinant of water/sewer infrastructure access for poor unincorporated communities.",
    "R0400EAA17741": "Smiley 2016 (Journal of Development Studies), 'Water Availability and Reliability in Dar es Salaam, Tanzania.' Household-survey/interview-based empirical study documenting that new piped-water connections require upfront payment for meter, pipes, labor, connection fee and three months' estimated consumption -- expenses 'beyond the scope of affordability for many of Dar es Salaam's poorest residents' -- alongside fragmented, unevenly distributed water-service provision by income area. A rigorous empirical case study directly documenting connection-fee and service-fragmentation institutional mechanisms producing differential water-access outcomes by income.",
    "R01EF154CA5CB": "Fiki, Amupitan, Dabi & Nyong 2007 (Journal of Community Practice), 'From Disciplinary to Interdisciplinary Community Development: The Jos-McMaster Drought and Rural Water Use Project in Nigeria.' Case study documenting the failure of Nigeria's centralized state-directed rural water program (DFRRI) -- water provision 'became politicized,' corrupted, and boreholes were sited on old cemeteries without community consultation -- and the subsequent shift to a community-centered 'nodal governance' model under an interdisciplinary university-community partnership. A rigorous institutional/governance-failure case study directly documenting how a centralized state water-provision mechanism produced access failures for rural communities, and an institutional alternative's response.",
    "RFD5A081230C5": "Ojha, Neupane, Pandey, Singh, Bajracharya & Dahal 2020 (Water, MDPI), 'Scarcity amidst plenty: Lower Himalayan cities struggling for water security.' Multi-city field-research study (5 Himalayan cities, Nepal and India, 2014-2018) finding that 4 of 5 towns lack well-performing local water-governance institutions and none has a coordinated water planning/governance system, resulting in a fragmented mix of government, community and private water-supply systems. A rigorous multi-city institutional case study directly documenting local water-governance capacity gaps as a mechanism shaping urban water security and equity.",
}

EXCLUDES = {
    "R0320961C9ED4": ("E01", "Arku & Arku 2010 (Gender & Development), 'I cannot drink water on an empty stomach: a gender perspective on living with drought.' Ethnographic focus-group study of gendered time-use and workload during drought periods in the Volta Rural Water Supply Project area, Ghana, centered on the absence of irrigation (a water-RESOURCE, agricultural-production issue) rather than a household water-SERVICE access-eligibility mechanism. Extends the established water-resource-vs-water-service distinction (Ioris 2007, Batch 222; Postel & Thompson 2005, Batch 220)."),
    "R03A03D4DBFB6": ("E12", "Sullivan & Meigh 2003 (Water Policy), 'Considering the Water Poverty Index in the context of poverty alleviation.' A methodological/implementation-focused paper on how to apply the Water Poverty Index (WPI) composite indicator in practice (census procedures, school-based data collection), not an empirical case study of a specific institutional/legal access-eligibility mechanism. Extends the established methodological/index-development-paper exclusion precedent."),
    "RA6188251C726": ("E06", "Ojha, Thapa, Shrestha, Shindo, Ishidaira & Kazama 2018 (Water, MDPI), 'Water Price Optimization after the Melamchi Water Supply Project.' A technical/economic optimization study (simulation modeling of expenditure ratio and utility working ratio across water-use scenarios) to identify an economically optimal water tariff for Kathmandu Valley, Nepal. An engineering/economic-optimization exercise, not documentation of an institutional/legal mechanism's differential effect on access; extends the established engineering/economic-optimization exclusion precedent (Jiang & Zheng 2014, Batch 220)."),
}

# Wrong-file-retrieved case: content delivered does not match the target record's title/authors.
WRONG_FILE = {
    "R0D5C4BC1354D": (
        "Target record per new_batch_pool.json is Nallathiga 2009, 'Private Sector "
        "Participation in the Provision of Urban Water Supply: Examining the Options "
        "and Scope in Mumbai.' The delivered PDF (Drive fileId "
        "1awwh8qsHeO0El78U-lgTXbF6tecMDB19) is instead Karen Bakker 2008 (Water "
        "Alternatives), 'The Ambiguity of Community: Debating Alternatives to "
        "Private-Sector Provision of Urban Water Supply' -- a different author, "
        "title, journal, and year, confirmed by both the extracted title metadata "
        "and the full article text (Cochabamba Water War case study, no mention of "
        "Mumbai or Nallathiga). Flagged wrong_file_retrieved; NOT screened; file NOT "
        "moved to Processed; left untouched pending correct retrieval."
    ),
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
        elif rid in WRONG_FILE:
            detail = WRONG_FILE[rid]
            row["full_text_status"] = "wrong_file_retrieved"
            row["reviewer_1"] = REVIEWER
            row["notes"] = (row.get("notes", "") + " " if row.get("notes") else "") + detail

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
    assert len(INCLUDES) + len(EXCLUDES) + len(WRONG_FILE) == 10
    decided, _ = process_db()
    assert len(decided) == 9
    append_exclusion_log(decided)
    n_inc = sum(1 for r in decided if r["final_decision"] == "include")
    n_exc = sum(1 for r in decided if r["final_decision"] == "exclude")
    print(f"Batch 226 processed: {n_inc} includes, {n_exc} excludes, {len(WRONG_FILE)} wrong_file_retrieved.")
