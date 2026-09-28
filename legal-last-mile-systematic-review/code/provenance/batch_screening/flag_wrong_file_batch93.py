#!/usr/bin/env python3
"""Flag two wrong-file Antigravity deliveries -- do NOT screen the mismatched content."""
import csv
import os
import tempfile

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
FT_DB = os.path.join(BASE, "02_screening/full_text/full_text_screening_database.csv")

UPDATES = {
    "RF7F8D43984CE": (
        "wrong_file_retrieved",
        "Antigravity Drive-inbox delivery (2026-09-22) does not match this record: "
        "target is 'Municipal Socialism Then and Now: some lessons for the Global South' "
        "(Leopold, Ellen; McDonald, David A, 2012, doi 10.1080/01436597.2012.728321), but the "
        "PDF delivered was Jamie Peck (2009), 'Creative moments: working culture, through "
        "municipal socialism and neoliberal urbanism' (book chapter in McCann & Ward (eds), "
        "Urban/global: relationality and territoriality in the production of cities, University "
        "of Minnesota Press) -- confirmed via full-text search, neither 'Leopold' nor "
        "'McDonald' appears anywhere in the delivered PDF, and the whole document (a "
        "creative-class/creative-cities urban economic-development policy piece contrasting "
        "1980s GLC cultural-industries policy with 2000s Detroit branding) never mentions "
        "water or sanitation. Not screened. Needs re-retrieval of the correct Leopold & "
        "McDonald 2012 Third World Quarterly article.",
    ),
    "R60D4F5EF6DE5": (
        "wrong_file_retrieved",
        "Antigravity Drive-inbox delivery (2026-09-22) does not match this record: target is "
        "'Supporting local climate adaptation planning and implementation through local "
        "governance and decentralised finance provision' (Sharma, Virinder; Orindi, Victor; "
        "Hesse, Ced; Pattison, James; Anderson, Simon, 2014, Community Development Journal, "
        "doi 10.1080/09614524.2014.907240), but the PDF delivered was a 1-page UK-Aid-funded "
        "field 'Resilience Assessment Summary' for Kinna ward, Isiolo County, Kenya (May 2012), "
        "with no listed academic authors -- confirmed via full-text search, none of Sharma, "
        "Orindi, Hesse, Pattison, or Anderson appears anywhere in the delivered PDF. Likely a "
        "grey-literature program document related to the same Kenya County Climate Adaptation "
        "Fund initiative discussed in the target article, but not the article itself. Not "
        "screened. Needs re-retrieval of the correct Sharma et al. 2014 journal article.",
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
