import csv, os, tempfile

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
LOG = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-21"
DATE = "2026-09-22"

# includes: record_id -> notes
INCLUDES = {
    "R7D3F1DFC2F82": "Andes indigenous community-professional negotiation study with genuine legal-institutional content: legal status/land titles for indigenous communities, a judicial workshop, and formation of a new legal 'consortium' structure for water/resource governance; qualitative case-study with original empirical fieldwork. Extracted as S580.",
    "R1F5F1AA03B4D": "22-city American Southwest study of water-supply policy transitions; qualitative institutional-logics analysis of political conflicts (development, preservation, environmental, consumer logics) over supply-increase and demand-reduction water policy, plus quantitative regression/random-forest modeling of political predictors of water conservation policy adoption (VWCIb index built from public documents/ordinances). Municipal/regulatory unit of analysis; genuine original empirical data (document review + media conflict coding + quantitative modeling). Extracted as S581.",
}

# excludes: record_id -> (code, detail)
EXCLUDES = {
    "RF7AFEEC69292": ("E01", "Governance-process/participation discourse study (civil society in development discourse); macro/institutional unit of analysis, not household-level water/sanitation access."),
    "RCBAA22BF401E": ("E05", "Documentary/case-study sociolegal analysis of the Kashechewan water crisis using secondary sources and case law; no original empirical data collection by the author."),
    "RADD32264AC64": ("E01", "Political-economy study of bottled water commodification and corporate resource-extraction contestation; not a household-level legal-administrative water/sanitation access study."),
    "R7863774753EC": ("E01", "Institutional healthcare-facility WASH study in Kenya; institutional (non-household) unit of analysis, analogous to prior healthcare-facility WASH exclusion precedent."),
    "RE41EC0C4C23A": ("E01", "Workplace menstrual-health intervention pilot study; workplace-based unit of analysis, not household water/sanitation access."),
    "R720E1DE4E7C8": ("E01", "Dengue epidemiology/public-health surveillance study using Lahore's fractured water infrastructure as disease-transmission context; primary outcome is epidemiological (mosquito breeding/disease risk), not a water access/connection/affordability outcome."),
    "R49DDEAB1849F": ("E01", "WaterAid Nigeria LGA-INGO partnership/participatory-development case study; governance-process/participation study at institutional (LGA) level, not household-unit legal-administrative water access."),
}

def main():
    with open(DB, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    by_id = {r["record_id"]: r for r in rows}

    all_ids = set(INCLUDES) | set(EXCLUDES)
    for rid in all_ids:
        assert rid in by_id, f"record_id {rid} not found in DB"
        row = by_id[rid]
        assert row["full_text_decision"] == "", f"{rid} already has a decision: {row['full_text_decision']!r}"

    log_rows = []

    for rid, notes in INCLUDES.items():
        row = by_id[rid]
        row["full_text_decision"] = "include"
        row["final_decision"] = "include"
        row["full_text_status"] = "retrieved"
        row["reviewer_1"] = REVIEWER
        row["notes"] = notes

    for rid, (code, detail) in EXCLUDES.items():
        row = by_id[rid]
        row["full_text_decision"] = "exclude"
        row["final_decision"] = "exclude"
        row["full_text_status"] = "retrieved"
        row["reviewer_1"] = REVIEWER
        row["exclusion_reason"] = code
        row["exclusion_reason_detail"] = detail
        log_rows.append({
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

    fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(DB), suffix=".csv")
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp_path, DB)

    with open(LOG, newline="", encoding="utf-8") as f:
        log_reader = csv.DictReader(f)
        log_fieldnames = log_reader.fieldnames
        existing_log = list(log_reader)

    existing_log.extend(log_rows)

    fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(LOG), suffix=".csv")
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=log_fieldnames)
        writer.writeheader()
        writer.writerows(existing_log)
    os.replace(tmp_path, LOG)

    print(f"done, db changed {len(all_ids)}, log rows now {len(existing_log)}")

if __name__ == "__main__":
    main()
