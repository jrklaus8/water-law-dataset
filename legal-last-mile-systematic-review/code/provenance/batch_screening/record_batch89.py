import csv, os, tempfile

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
REVIEWER = "Claude-AI-fulltext-2026-09-21"

INCLUDES = {
    "RE48029A5D3C0": "Qualitative case study (48 semi-structured interviews plus field observations, 2018-2020) of hybrid formal/informal, public/private labor relations in the maintenance and repair of water supply infrastructure in two Accra, Ghana neighborhoods (Nima informal settlement; Dodowa peri-urban). Documents genuine household-level legal-institutional content: GWCL's regulatory framework under the Public Utilities Regulatory Commission (PURC) and Water Resource Commission (WRC); the legality/illegality distinction for private water connections (illegal networks common in Nima, self-repair to conceal them from GWCL officials) and repair of public networks by private plumbers; household responsibility for private-connection maintenance under national water-sector policy; and Ghana's decentralized Community Water and Sanitation Agency (CWSA)/Water and Sanitation Management Team (WSMT) framework governing peri-urban water-system maintenance. Extracted as S582.",
}

def main():
    with open(DB, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    by_id = {r["record_id"]: r for r in rows}

    for rid in INCLUDES:
        assert rid in by_id, f"record_id {rid} not found in DB"
        row = by_id[rid]
        assert row["full_text_decision"] == "", f"{rid} already has a decision: {row['full_text_decision']!r}"

    for rid, notes in INCLUDES.items():
        row = by_id[rid]
        row["full_text_decision"] = "include"
        row["final_decision"] = "include"
        row["full_text_status"] = "retrieved"
        row["reviewer_1"] = REVIEWER
        row["notes"] = notes

    fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(DB), suffix=".csv")
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp_path, DB)

    print(f"done, db changed {len(INCLUDES)}")

if __name__ == "__main__":
    main()
