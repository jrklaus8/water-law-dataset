#!/usr/bin/env python3
import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
LOG = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "claude_sonnet_5"
DATE = "2026-09-27"

INCLUDES = {
    "R44B35D130A49": "Household-level legal-status/institutional analysis: domestic rainwater harvesting held to be illegal by strict application of South Africa's National Water Act (Act 36 of 1998) and Water Services Act (Act 108 of 1997); DWAF Pilot Programme government financial assistance mechanism examined.",
    "R4443C2EFEEE0": "Empirical mixed-methods study (429 household questionnaires, Ramotswa/Tlokweng, Botswana): Major Village Infrastructure Programme cost-recovery-only-for-O&M institutional design and household income as primary barrier to waterborne-sewerage connection uptake (23-39% connected after 7 years availability).",
    "R4288E0B980A6": "Empirical mixed-methods case study (225 household questionnaires + 15 in-depth interviews, Upper West Region, Ghana): National Community Water and Sanitation Programme institutional structure (WSMTs/WATSANs/WMBs); potable water access rose 38%->97% post community-management introduction, with tariff-setting failures and absent Water Management Board threatening sustainability.",
    "R45641CF1C6FA": "Legal analysis of Palestinian Water Law No. 3 (2002), Oslo II jurisdictional fragmentation (Areas A/B/C), and occupying-power obligations under the Hague Regulations/Fourth Geneva Convention/ICESCR constraining the Palestinian Water Authority's ability to progressively realise the right to water and sanitation.",
    "R45B892C461F4": "Empirical household survey + key informant interviews (Wa municipality, Ghana) with regression analysis of in-house toilet facility provision; explicitly analyzes institutional/urban-planning-regime distortions (limited monitoring systems, inadequate logistics/personnel) alongside socio-economic and cultural factors as barriers to household sanitation access.",
}

EXCLUDES = {
    "R437473ADF773": ("E05", "WIREs Water article explicitly labeled 'OPINION' in its header; argumentative synthesis of the author's prior published work and broader literature, no original empirical data collection in this paper."),
    "R48132E069769": ("E01", "Primary analytical focus is the HIV/AIDS-water scarcity health/caregiving dialectic and stigma-driven social exclusion from communal water points; Zimbabwe Water Act 1998/Catchment Council institutional content is contextual background for community-wide scarcity, not the paper's analytical vehicle for differential access."),
    "R420DE16EB90E": ("E12", "Self-labeled systematic literature review of Water Safety Plan outcomes across 53 source documents; not primary research, and WSP risk-management content is a water-quality/engineering topic distinct from legal/institutional water-access mechanisms."),
    "R4459FC42FAAC": ("E01", "General institutional-reform argument/overview of Mumbai's urban water sector (supply, demand management, tariff efficiency); not focused on household-level access inequality or a specific legal/institutional mechanism's effect on an access outcome."),
    "RA542DE926650": ("E01", "Catchment/watershed conservation study: community attitudes toward upstream land degradation management and reservoir sustainability, Barekese, Ghana; not about household water access."),
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
