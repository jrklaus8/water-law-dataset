#!/usr/bin/env python3
"""Flag two wrong-file deliveries in Batch 210 -- do NOT screen the mismatched content."""
import csv
import os
import tempfile

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
FT_DB = os.path.join(BASE, "02_screening/full_text/full_text_screening_database.csv")

UPDATES = {
    "R3B415FA79D4C": (
        "wrong_file_retrieved",
        "Google Drive delivery (2026-09-27) does not match this record: target is "
        "'Gender, Class, and Access to Water: Three Cases in a Poor and Crowded Delta' "
        "(Crow, Ben; Sultana, Farhana, 2002, Society & Natural Resources), but the PDF "
        "delivered was Sneddon, Harris, Dimitrov & Ozesmi (2002), 'Contested Waters: "
        "Conflict, Scale, and Sustainability in Aquatic Socioecological Systems' -- the "
        "introductory essay to the SAME special issue (Society & Natural Resources 15:8), "
        "confirmed via full-text read: the delivered content's own title, authors, and "
        "abstract match the Sneddon et al. introduction verbatim, and the introduction "
        "itself cites 'Crow and Sultana, this issue' as a separate article on Bangladesh "
        "gender/water dynamics -- confirming the target article is a distinct piece within "
        "the same issue that was not the one delivered. Not screened. Needs re-retrieval of "
        "the correct Crow & Sultana 2002 article.",
    ),
    "R3DA90E060AD7": (
        "wrong_file_retrieved",
        "Google Drive delivery (2026-09-27) does not match this record: target is "
        "'Community Water Governance for Sustainable Local Development in Northern Ghana' "
        "(Bazaanah, Prosper, 2021), but the PDF delivered was Pranab Bardhan (2002), "
        "'Decentralization of Governance and Development,' Journal of Economic "
        "Perspectives 16(4):185-205 -- confirmed via full-text read of the delivered PDF's "
        "title page and running header. Wrong journal, wrong year, wrong author, wrong "
        "country focus (general cross-national decentralization theory, not Ghana). Not "
        "screened. Needs re-retrieval of the correct Bazaanah 2021 article.",
    ),
}


def main():
    with open(FT_DB, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    by_id = {row["record_id"]: row for row in rows}

    for rid, (status, note) in UPDATES.items():
        assert rid in by_id, f"record_id {rid} not found"
        row = by_id[rid]
        assert not row["full_text_decision"], f"{rid} already has full_text_decision={row['full_text_decision']!r}"
        assert not row["final_decision"], f"{rid} already has final_decision={row['final_decision']!r}"
        row["full_text_status"] = status
        row["notes"] = note

    fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(FT_DB), suffix=".csv")
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    os.replace(tmp_path, FT_DB)

    print(f"done, {len(UPDATES)} records flagged wrong_file_retrieved")


if __name__ == "__main__":
    main()
