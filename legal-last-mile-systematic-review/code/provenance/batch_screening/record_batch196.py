#!/usr/bin/env python3
import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
LOG = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "claude_sonnet_5"
DATE = "2026-09-27"

INCLUDES = {
    "R375DC07A5C67": "Qualitative case study (44 interviews, Faridabad/Delhi/Mumbai) examining legal notification status (Maharashtra Slum Areas Act 1971, MCGM pre-2000 documentation cutoff) and Public Interest Litigation (Bombay High Court, Article 21 right-to-life claim) as legal/institutional mechanisms determining differential water-service access for informal settlers.",
    "R375CB03774D9": "Institutional/political-economy case study of Sicily's 2002 water crisis documenting how Mafia-linked institutional capture of public-works contracting and regional/national government dysfunction produced unfinished infrastructure and a documented household water-supply-interruption disparity (national average 6.6 days/year vs 36.1 days/year in the south), disproportionately affecting the poorest neighborhoods.",
    "R355ECFDBF14D": "Qualitative study (40 key-informant interviews/focus groups, 6 villages) of village-level water committee decision-making structures, roles and gender dynamics under Fiji's Water Authority statutory-body framework, directly examining institutional governance of water access and security.",
    "R35461F430753": "Uganda WASH program case study documenting a Learning Alliance-developed regulatory structure, public-private-partnership maintenance contracts, proposed new by-laws, and formal legal status for community water-management committees, implemented across 200+ communities to improve household water-access sustainability.",
    "R330A544EACCE": "Empirical mixed-methods study (120 households + 24 small-scale independent water providers, Lilongwe, Malawi) examining alternative/informal water-provider dynamics in low-income areas under Malawi's Water Works Act (1995) and National Water Policy (2005) institutional/regulatory framework, where the formal utility fails to reach informal settlements.",
    "R317C83144950": "Empirical study (48 expert interviews, 35 artisan interviews, 20 failed water schemes visited) diagnosing institutional and organizational incapability of local government as a primary determinant of rural water-supply service failures in Ethiopia, with policy implications for capacity building.",
}

EXCLUDES = {
    "R36A2B99DC8AD": ("E01", "Lived-experience narrative study of the psychological 'paradox of social resilience' -- coping-cost perception and emotional numbing -- among Kathmandu Valley water-insecure residents; a psychological/behavioral resilience study, not a legal/institutional access mechanism."),
    "R35E214EE7613": ("E01", "Cross-national statistical/geospatial modeling study correlating composite governance and economic indicators (social-institutional-capacity index, corruption perception, GDP, gender empowerment) with global sanitation coverage and water-stress outcomes of sanitation-technology choice; broad macro-level indicator regression, not a specific legal/institutional mechanism's effect on a defined population's access."),
    "R316CFC35EF4E": ("E05", "Conceptual/theoretical seminar essay on institutional and organizational obstacles to efficient water-project operation and maintenance in Latin America; no original empirical data collection (no survey, interviews, or case-study fieldwork)."),
    "RAAB22A572D27": ("E01", "Ethnography and economic-experiment (dictator/ultimatum games) study of how religiosity shapes prosocial water-sharing norms in a Bolivian squatter settlement; the municipal utility's institutional exclusion of the settlement is background context, while the paper's core analytical framework is religiosity's effect on economic behavior, not a legal/institutional access mechanism."),
}

assert len(INCLUDES) + len(EXCLUDES) == 10

def atomic_write(path, fieldnames, rows):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path))
    with os.fdopen(fd, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp, path)

def process_db():
    with open(DB, newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    ids_seen = set()
    for row in rows:
        rid = row["record_id"]
        if rid in INCLUDES:
            ids_seen.add(rid)
            row["full_text_status"] = "retrieved"
            row["full_text_decision"] = "include"
            row["reviewer_1"] = REVIEWER
            row["final_decision"] = "include"
            row["notes"] = (row.get("notes") or "").rstrip()
            if row["notes"]:
                row["notes"] += "; "
            row["notes"] += INCLUDES[rid]
        elif rid in EXCLUDES:
            ids_seen.add(rid)
            code, detail = EXCLUDES[rid]
            row["full_text_status"] = "retrieved"
            row["full_text_decision"] = "exclude"
            row["exclusion_reason"] = code
            row["exclusion_reason_detail"] = detail
            row["reviewer_1"] = REVIEWER
            row["final_decision"] = "exclude"
            row["notes"] = (row.get("notes") or "").rstrip()
            if row["notes"]:
                row["notes"] += "; "
            row["notes"] += detail

    assert ids_seen == set(INCLUDES) | set(EXCLUDES), ids_seen ^ (set(INCLUDES) | set(EXCLUDES))
    atomic_write(DB, fieldnames, rows)
    print(f"Screening DB updated: {len(ids_seen)} records decided.")
    return {row["record_id"]: row for row in rows if row["record_id"] in ids_seen}

def append_exclusion_log(decided):
    with open(LOG, newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    for rid, (code, detail) in EXCLUDES.items():
        row = decided[rid]
        rows.append({
            "record_id": rid,
            "title": row["title"],
            "authors": row["authors"],
            "year": row["year"],
            "stage": "full_text",
            "exclusion_code": code,
            "exclusion_reason_detail": detail,
            "reviewer": REVIEWER,
            "date": DATE,
        })

    atomic_write(LOG, fieldnames, rows)
    print(f"Exclusion log updated: {len(EXCLUDES)} rows appended ({len(rows)} total).")

if __name__ == "__main__":
    decided = process_db()
    append_exclusion_log(decided)
