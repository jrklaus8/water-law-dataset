#!/usr/bin/env python3
import csv
import tempfile
import os

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
LOG = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "claude_sonnet_5"
DATE = "2026-09-27"

INCLUDES = {
    "R2E4979185A18": "Institutional 'governance failure' analysis (household survey, archives, GIS mapping, interviews) directly documenting how utility governance norms, land-use policy, tariff-related connection-fee disincentives, and tenure/residency status jointly create disincentives for connecting poor households to networked water supply in Jakarta.",
    "RAF43F1049CAC": "Archival/interview-based analysis of colonial and postcolonial institutional 'governmentality' (citizenship classification, land-use rationalities) that produced and sustained persistent, unequal fragmentation of household water-supply access by class in Jakarta, including under private-sector management from 1998.",
    "R2E27CA42816D": "Quantitative spatial/regression study (negative binomial regression) of disparities in community water systems' compliance with the U.S. Safe Drinking Water Act, finding small and rural community water systems significantly less likely to comply with this legal/regulatory framework.",
    "RAE2EE524BC5B": "Comparative empirical study applying a Hohfeldian legal-rights framework and cross-country WHO-UNICEF JMP access data and governance indicators to test whether formal legal promulgation of a right to water improves water access, finding governance mechanisms matter more than the formal right's articulation.",
}

EXCLUDES = {
    "R2E89C4D0ECBE": ("E01", "Comparative case study of two Portuguese water-utility governance contracts (PPP vs. public-public partnership) examining contract-design quality and administrative procedures; focused on utility contracting practice, not differential household access outcomes."),
    "RAD91FA5DFF79": ("E01", "Household survey-based access-measurement study finding that geographic/socioeconomic factors (settlement age, income) rather than government policy explain differences in service access across Bangkok slum communities; general descriptive access-determinants study, not a legal/institutional mechanism analysis."),
    "R2E48DA87EEB4": ("E05", "Theoretical/doctrinal legal-discourse argument article on the UN human-right-to-water resolution advocating a shift from public-private to public-NGO partnerships; normative commentary piece without an empirical case study or access-outcome data."),
    "R2DBFA78BFB76": ("E01", "Urban-planning theory study of infrastructure-extension mechanisms (utility 'institutional creativity and bricolage') for water and electricity in unplanned settlements, Delhi and Lima; a planning-theory framework spanning multiple utility sectors, not a water-specific legal/institutional access-mechanism study."),
    "RB091A2B0357C": ("E01", "Historical/political-economy essay on the general infrastructure crisis (water, housing, mass transit) in Lagos across the colonial and post-colonial periods; a multi-sector historical essay, water is one of several services discussed."),
    "R2D7CBFF1D2B9": ("E12", "Self-labeled systematic review synthesizing evidence on top-down and bottom-up approaches to slum service provision; secondary synthesis, not primary research."),
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
