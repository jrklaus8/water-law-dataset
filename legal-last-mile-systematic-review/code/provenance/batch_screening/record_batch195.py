#!/usr/bin/env python3
import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
LOG = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "claude_sonnet_5"
DATE = "2026-09-27"

INCLUDES = {
    "R3D9E303C9EB3": "Economic/institutional framework analyzing rent-extracting behavior by government officials, water utility staff, public-tap operators, and vendors in Jakarta's municipal water system; informal institutional actors' rent-seeking behavior directly determines household connection availability and vended-water prices (up to 50x municipal tariff for unconnected households).",
    "R3AE23244EFDE": "Empirical field study of Mozambique's National Rural Water Supply and Sanitation Program implementation examining how water-committee leadership/governance quality and village institutional support determine borehole sustainability and continued water access, with attention to equity of access to intervention benefits.",
    "R39C8535D837B": "Empirical study (12 villages, Odisha, India) comparing two institutional arrangements (local-government Gram Panchayat vs community-based Village Water and Sanitation Committee) implementing the Demand Responsive Approach reform, finding that DRA reinforced existing social inequality in access to rural drinking water.",
}

EXCLUDES = {
    "R422212E8D444": ("E01", "Ethnographic study of Peru's Water Law 29338 (2009) and prior 1969 agrarian-reform water law redistributing basin-scale irrigation water rights among farmer irrigation organizations (juntas de usuarios), mining, and urban users, Arequipa; basin-scale water-resource-allocation governance study, not household domestic-access outcome."),
    "RA75E798FACF3": ("E06", "Data envelopment analysis (DEA) technical-efficiency benchmarking study of 22 water/sewerage companies in England and Wales incorporating service-quality variables; technical optimization/benchmarking methodology, not a legal/institutional access mechanism."),
    "RA69778FDBAC5": ("E12", "Journal AWWA legal case-note column summarizing three unrelated utility-law court decisions (Florida CIAC ratemaking, Colorado meter-pit liability, Pennsylvania mine-permit water-replacement); a news/case-summary column, not primary empirical research."),
    "RA7D5ADA35BCD": ("E12", "Book review (Contemporary Sociology) of Troesken's 'Water, Race, and Disease'; not primary research."),
    "R3CBE6A1ACFA3": ("E12", "Self-labeled 'survey of different regimes and the existing literature' providing a cross-country taxonomy of water-utility-regime reform experiences; broad theoretical/comparative literature review, not primary empirical research."),
    "R3CB8FAE6ECDA": ("E01", "Study of human-resources capacity, staffing distribution, and gender balance in Ghana's WASH-sector workforce (public/private/NGO institutions, training-institution graduate supply); a workforce/capacity-building policy analysis, not a legal/institutional mechanism's effect on household water-access outcomes."),
    "R3C5881639608": ("E05", "World Bank Water and Sanitation Program-Africa proposed multi-country work-program/action-plan document outlining five pro-poor strategy entry points; a program proposal citing other studies' findings, with no original empirical data collection or analysis of its own."),
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
