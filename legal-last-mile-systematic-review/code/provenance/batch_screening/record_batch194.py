#!/usr/bin/env python3
import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
LOG = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "claude_sonnet_5"
DATE = "2026-09-27"

INCLUDES = {
    "R420211B3E670": "Legal/institutional book chapter on Chile's water/sanitation privatization reforms: Law 382 (General Law of Sanitation Services), Law 70 (General Law of Tariffs), SISS regulator, tariff-setting process based on hypothetical efficient company, and Law 18,778 subsidy system for low-income households (14.8% of customers benefited with subsidies in 2015).",
    "R418BDADF8E47": "Household survey (102 households) examining domestic rainwater harvesting adoption in Kinondoni, Tanzania, under the Tanzania Water Resources Management Act 2009's water-permit exemption for domestic RWH and government bylaws mandating RWH inclusion in building permits for new construction.",
    "R410CAF95F628": "Legal/institutional analysis of foreign-aid-driven (World Bank/JBIC) institutional reform of Kerala Water Authority: shift from government-subsidized supply to community-based cost-recovery scheme (KRWSA), removal of public taps, tariff increases, with household survey data on access before/after (49.3% of beneficiaries previously without sustainable access now getting water through KRWSA).",
    "R43C575771C91": "Empirical fieldwork (55 interviews) examining property rights regimes and charitable institutional arrangements (sobol/waqf) governing water access in Egypt's Nile Delta, including the 1984 Irrigation and Drainage Law's unenforceable legal right to irrigation water and NGO institutional-legitimacy requirements for establishing communal water access.",
    "R3DCC4CCBD760": "Empirical interview study (35 individuals, 16 organizations) of Namibia's water tariff price-setting process within its legal framework (Water Resources Management Act 2004, proposed Water Regulatory Board), documenting affordability outcomes for the urban poor (32% barely afford, 22% unable to afford communal water/sanitation facilities).",
}

EXCLUDES = {
    "R41224AA84355": ("E01", "Photovoice study (8 women) applying ecosocial/political-ecology theory to water-health linkages in rural Kenya; institutional content (KIWASCO pro-poor delivery model, government neglect) is background context for a primarily health-geography/collective-action analysis, not the paper's core analytical focus."),
    "R440763E96236": ("E01", "Anthropological study of sociocultural, economic and chemical water values in a Ghanaian small-scale gold-mining community; government/institutional oversight (or its absence) is discussed as background context for a water-values and contamination analysis, not the paper's core analytical framework."),
    "R3FEE63DFDEC4": ("E06", "Technical/engineering and financial planning report on rural water supply infrastructure in Fayoum, Egypt: production capacity, water balance projections, billing efficiency and Unaccounted-For-Water percentages, not an empirical analysis of a legal/institutional mechanism's effect on access."),
    "R3F83B65D41C0": ("E01", "Ordinal logistic regression study of which of 14 social-marketing/behavior-change program-implementation factors (trigger meetings, follow-up visits, training) predict household adoption of urine-diverting dry toilets in rural China; a program-effectiveness/behavioral-uptake study, not a legal/institutional access mechanism."),
    "R3E6A10BB691A": ("E01", "SWOT-analysis qualitative study comparing three public ownership/governance models (municipal unit, municipal-owned enterprise, municipal-owned company) for Finnish waterworks on efficiency/business-orientation/transparency grounds; not focused on access inequality for any marginalized population."),
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
