#!/usr/bin/env python3
import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
LOG = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "claude_sonnet_5"
DATE = "2026-09-27"

INCLUDES = {
    "RA92812EC2661": "Ethnographic/survey study of failed water-supply and sanitation privatization in Belize City, documenting negative material consequences (tariff increases, disconnection rates) under the institutional shift from public to privatized Belize Water Supply Limited (BWSL).",
    "RA9D674E9C236": "Empirical study of household tenure security (de facto vs. de jure) as the institutional/legal mechanism determining household investment decisions in on-site urban sanitation, Dakar, Senegal.",
    "R2F782937787E": "Field-based policy study documenting how flexible, non-prescriptive community-engaged institutional approaches to O&M cost-recovery tariff-setting (vs. rigid 100%-collection mandates) improved rural water-supply service delivery sustainability and collection rates in Tamil Nadu, South India.",
    "RAD2F8C9FB199": "Legal/institutional analysis of Australia's 2004 National Water Initiative, the Native Title Act 1993, and the Roper River water-allocation plan's Strategic Indigenous Reserve, documenting stark inequity between indigenous land ownership (>20%) and indigenous-specific water entitlements (<0.01% of diversions).",
    "RABA8C62B263C": "Legal analysis of notified/non-notified slum status in Mumbai and the 2014 Bombay High Court Public Interest Litigation ruling (Pani Haq Samiti) grounding a right to water in Article 21 of the Indian Constitution, documenting a >40x water-price disparity and higher infant mortality for non-notified slum residents.",
}

EXCLUDES = {
    "RA9E2522BF679": ("E01", "Historical/environmental narrative of the collapse of Emfuleni Local Municipality's wastewater treatment infrastructure and resulting fish-kill/environmental disaster in the Vaal River Barrage, South Africa (2018-2021); primary focus is environmental/ecological harm and river-system governance, not household water-access outcomes."),
    "RAB5CF32C6D46": ("E01", "Broad composite multi-dimensional deprivation index study (India, 1992/93-2004/5) comparing consistency between two national survey datasets across many welfare dimensions (expenditure, drinking water, clean fuel, child stunting, maternal BMI); water access is one of several household-amenity covariates in a general poverty-index methodology paper, not a legal/institutional mechanism analysis."),
    "RAB3F0FD802CD": ("E04", "Quasi-experimental difference-in-difference regression study of a slum-upgrading PPP intervention (Ahmedabad, India) using micro-health-insurance claims data; the measured dependent variable is waterborne illness incidence (a health outcome), not a water-access or coverage outcome."),
    "RA9308E647DFC": ("E01", "Political-economy analysis of the design, implementation and underutilization of Ethiopia's National WASH Inventory data-collection/monitoring system; focus is on sector-monitoring data governance and donor-government dynamics, not a legal/institutional mechanism's effect on household water access."),
    "RAC15BC9785C8": ("E01", "Organizational/business-ethics theoretical case study applying Frederick's naturological (economizing vs. ecologizing) framework to a single California utility rate-regulation proceeding (General Rate Case); analyzes regulatory-process value tensions, not water-access inequality for a marginalized population."),
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
