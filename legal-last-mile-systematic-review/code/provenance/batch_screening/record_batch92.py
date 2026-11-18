#!/usr/bin/env python3
"""Eighty-seventh (unnumbered mixed) full-text screening batch: 8 excludes, 5 includes."""
import csv
import os
import tempfile

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
FT_DB = os.path.join(BASE, "02_screening/full_text/full_text_screening_database.csv")
EXCL_LOG = os.path.join(BASE, "02_screening/exclusion_log/exclusion_log.csv")

REVIEWER = "Claude-AI-fulltext-2026-09-21"

EXCLUDES = {
    "R7562AB7A89D4": {
        "code": "E04",
        "detail": "Swiss survey of water-sector professionals' stated organizational-form preferences (public/private/inter-municipal) using conjoint-analysis choice experiments; the measured outcome is expressed preference/attitude, not an actual access/connection/affordability/reliability outcome.",
        "note": "Wrong outcome; stated-preference/attitude survey of organizational-form preferences, not an access outcome.",
    },
    "R88B242AA77A8": {
        "code": "E05",
        "detail": "Desk-based development of policy-relevant SDG6 indicators for Austria via literature/dataset review and expert consultation on indicator selection criteria; no original empirical data collection on household or community water/sanitation access.",
        "note": "No original empirical data collection; indicator-selection/desk-review paper.",
    },
    "RCE880579857E": {
        "code": "E01",
        "detail": "Macro/national-level comparative-politics process-tracing study of the constitutionalization of the right to water in Kenya and Slovenia (domestic political drivers, opportunity structures, transnational norm diffusion); no household/applicant-level enforcement or access outcome examined.",
        "note": "Wrong topic/unit of analysis; macro constitutional-politics process study, no household-level enforcement outcome.",
    },
    "R8C306200E800": {
        "code": "E05",
        "detail": "Desk-based legal/policy review of Ecuador's water-management legal-authorization and quality-parameter framework; Methods section confirms a literature/document review with no original data collection.",
        "note": "No original empirical data collection; desk-based legal/policy literature review.",
    },
    "R5977B1A524C5": {
        "code": "E01",
        "detail": "Methodological/framework-development paper presenting a transdisciplinary systems-mapping architecture for the water-energy-sanitation nexus in Brazil; demonstrates a mapping method rather than empirically examining a household/community-level legal-institutional access mechanism or outcome.",
        "note": "Wrong topic/unit of analysis; methodological systems-mapping framework paper, not an empirical access study.",
    },
    "R0E0F6D8C3330": {
        "code": "E04",
        "detail": "Nominal Group Technique survey of 88 mostly national/state-level professionals and researchers (only n=7 from local communities) ranking 30 literature-derived success factors for rural water supply services in Brazil; the measured outcome is expert-perceived importance/ranking of factors, not an empirical access/connection/affordability/reliability outcome.",
        "note": "Wrong outcome; expert-opinion ranking/perception survey, not an empirical access outcome.",
    },
    "R3D4E9479ACD7": {
        "code": "E01",
        "detail": "Institutional-coordination-structure study assessing the functioning, legitimacy, and capacity of Zimbabwe's National Action Committee WASH sector-coordination mechanism via a questionnaire survey (43 organizations) and focus-group/key-informant interviews with sector institutions; measures institutional coordination effectiveness, not household-level water/sanitation access outcomes.",
        "note": "Wrong topic/unit of analysis; institutional-coordination-mechanism study, no household-level access outcome.",
    },
    "R7220865B32E6": {
        "code": "E06",
        "detail": "Technical climate-resilience assessment of 10 piped water supply schemes in Nepal using the HTIW engineering/infrastructure-resilience scoring framework (Likert-scale domain scores for infrastructure, catchment, management, supply chain, etc.); measures scheme-level technical resilience, not a legal-institutional household/community access outcome.",
        "note": "Engineering-only study; technical infrastructure-resilience scoring framework, no legal-institutional access examination.",
    },
}

INCLUDES = {
    "RF0D065E4A163": "Comparative constitutional-law and case-study analysis of the right to water in Brazil, Colombia, and Peru, documenting court-enforced household water reconnection/disconnection cases (including tutela actions) under constitutional/statutory right-to-water frameworks, directly analogous to the previously-included S517 Morgan 'Turning off the tap' precedent. record_id RF0D065E4A163.",
    "RC89A2B1CEA16": "Case study of the Queretaro Aqueduct II water-transfer project in Mexico documenting broken public-private-partnership compensation promises to rural communities affected by the transfer works, including empirical evidence of unmet contractual/legal commitments and resulting social inequality in water access. record_id RC89A2B1CEA16.",
    "RA84EFD886B54": "Ethnographic study of the Moamba, Mozambique water infrastructure system documenting informal community-set payment and exclusion rules and utility discretionary refusal to formally recognize/maintain an 'unauthorized' community-built pipe extension, evidencing the interplay of formal and informal institutional authority over household water access. record_id RA84EFD886B54.",
    "R684F94E229C3": "Ethnographic/interview-based study (participant observation with tanker drivers, 15 interviews with policy makers) of Accra, Ghana's tanker water-supply governance, documenting the formal regulatory framework's non-recognition of tanker/vendor water providers, illegal versus legal water-filling-point status, and land-tenure-based exclusion of informal-settlement residents (Old Fadama) from legal piped connections. record_id R684F94E229C3.",
    "R2E8B036BE02F": "Mixed-methods study (ACTogether community survey data across 57 informal settlements plus interviews) in Kampala, Uganda documenting how Kampala's complicated land-tenure system and connection-fee requirements determine household access to piped water, with land ownership status directly gating legal water-access vulnerability across slum communities. record_id R2E8B036BE02F.",
}


def main():
    with open(FT_DB, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    by_id = {row["record_id"]: row for row in rows}

    all_ids = list(EXCLUDES.keys()) + list(INCLUDES.keys())
    for rid in all_ids:
        assert rid in by_id, f"record_id {rid} not found in full-text DB"
        row = by_id[rid]
        assert not row["full_text_decision"], f"{rid} already has full_text_decision={row['full_text_decision']!r}"
        assert not row["final_decision"], f"{rid} already has final_decision={row['final_decision']!r}"

    exclusion_rows_to_append = []

    for rid, info in EXCLUDES.items():
        row = by_id[rid]
        row["full_text_decision"] = "exclude"
        row["final_decision"] = "exclude"
        row["full_text_status"] = "retrieved"
        row["exclusion_reason"] = info["code"]
        row["exclusion_reason_detail"] = info["detail"]
        row["reviewer_1"] = REVIEWER
        row["notes"] = info["note"]
        exclusion_rows_to_append.append({
            "record_id": rid,
            "title": row["title"],
            "authors": row.get("authors", ""),
            "year": row.get("year", ""),
            "exclusion_code": info["code"],
            "exclusion_reason_detail": info["detail"],
            "stage": "full_text",
            "reviewer": REVIEWER,
            "date": "2026-09-22",
        })

    for rid, note in INCLUDES.items():
        row = by_id[rid]
        row["full_text_decision"] = "include"
        row["final_decision"] = "include"
        row["full_text_status"] = "retrieved"
        row["reviewer_1"] = REVIEWER
        row["notes"] = note

    fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(FT_DB), suffix=".csv")
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    os.replace(tmp_path, FT_DB)

    with open(EXCL_LOG, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        log_fieldnames = reader.fieldnames
        log_rows = list(reader)

    for entry in exclusion_rows_to_append:
        log_row = {k: entry.get(k, "") for k in log_fieldnames}
        log_rows.append(log_row)

    fd2, tmp_path2 = tempfile.mkstemp(dir=os.path.dirname(EXCL_LOG), suffix=".csv")
    with os.fdopen(fd2, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=log_fieldnames)
        writer.writeheader()
        for row in log_rows:
            writer.writerow(row)
    os.replace(tmp_path2, EXCL_LOG)

    print(f"done, db changed {len(all_ids)}, log rows now {len(log_rows)}")


if __name__ == "__main__":
    main()
