#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "RB96E8D94B2BD",  # Aleixo, Rezende, Pena, Zapata & Heller - Inequalities in Access to Water, Brazilian Northeast
    "RB70B7542FFB9",  # Bellaubi & Boehm - Management practices and corruption risks in water service delivery, Kenya and Ghana
    "RB709D82B9922",  # Truelove - Negotiating states of water: bureaucratic arbitrariness, Delhi
    "RB6BFA3BE24E5",  # Jocoy - Who gets clean water? Aid allocation to small water systems in Pennsylvania
    "RB7D025C8BB6D",  # Anzera, Belotti, Bousselmi & Rabi - Hydropolitical challenges of domestic water conservation, Palestine and Tunisia
]

EXCLUDES = {
    "RBD91806D4AF5": ("E05", "Satterthwaite (2016), 'Missing the Millennium Development Goal targets for water and sanitation in urban areas.' A review of MDG progress drawing on UN statistical data, focused on documenting deficiencies and definitional inadequacies in global water/sanitation monitoring statistics rather than an empirical study of a specific legal/institutional access mechanism -- consistent with the established Satterthwaite E05 statistical-methodology-critique exclusion precedent (Batch 175, same author)."),
    "RB9A117B7E3E9": ("E01", "Kundu (2000), 'Urban poverty in India: Issues and perspectives in development.' A broad analysis of rural/urban poverty trends and interstate variations in India; water supply is examined together with toilets and electricity as one of several 'basic amenities' within a much broader poverty/governance-reform analysis, not a dedicated water-access institutional-mechanism study."),
    "RB5444B329650": ("E12", "Dos Santos, Adams, Neville, Wada, de Sherbinin, Mullin Bernhardt & Adamo (2017), 'Urban growth and water access in sub-Saharan Africa: Progress, challenges, and emerging research directions.' Explicitly labeled 'Review' in Science of the Total Environment; a secondary literature review synthesizing existing empirical research on urban water access in SSA and proposing future research directions, not an original empirical study -- consistent with the established E12 secondary-review exclusion precedent."),
    "RB4ABDB221CD3": ("E01", "Boardman (2010), 'Mexico at the vanguard: A new era in medicines of biotechnological origin.' Confirmed via full-text read that this article concerns Mexican pharmaceutical regulation of biocomparable/biosimilar biotechnology drugs (an amendment to Article 222 Bis of the General Health Law); the content has no connection whatsoever to water access or water law, indicating a title/abstract-screening corpus-inclusion error rather than a wrong_file_retrieved case (title/author match the delivered PDF exactly)."),
    "RB2086E7D7795": ("E01", "Li, Wang, Malhi, Li, Gao & Tian (2009), 'Chapter 7 Nutrient and Water Management Effects on Crop Production, and Nutrient and Water Use Efficiency in Dryland Areas of China.' Confirmed via full-text read that this is a purely agronomic book chapter (Advances in Agronomy) on soil nutrient/water interactions for crop yield in dryland farming; agricultural agronomy with no water-access institutional/legal content, indicating a corpus-inclusion error."),
}

def atomic_write(path, fieldnames, rows):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path))
    with os.fdopen(fd, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for row in rows:
            w.writerow(row)
    os.replace(tmp, path)

with open(SCREEN, newline="") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    rows = list(r)

n_inc = n_exc = 0
for row in rows:
    rid = row["record_id"]
    if rid in INCLUDES:
        row["full_text_status"] = "included"
        row["full_text_decision"] = "include"
        row["final_decision"] = "include"
        row["reviewer_1"] = "Claude"
        n_inc += 1
    elif rid in EXCLUDES:
        code, detail = EXCLUDES[rid]
        row["full_text_status"] = "excluded"
        row["full_text_decision"] = "exclude"
        row["final_decision"] = "exclude"
        row["exclusion_reason"] = code
        row["exclusion_reason_detail"] = detail
        row["reviewer_1"] = "Claude"
        n_exc += 1

assert n_inc == len(INCLUDES), f"expected {len(INCLUDES)} includes, matched {n_inc}"
assert n_exc == len(EXCLUDES), f"expected {len(EXCLUDES)} excludes, matched {n_exc}"

atomic_write(SCREEN, fieldnames, rows)

meta = {}
with open(SCREEN, newline="") as f:
    r = csv.DictReader(f)
    for row in r:
        meta[row["record_id"]] = row

with open(EXCLOG, newline="") as f:
    r = csv.DictReader(f)
    ex_fieldnames = r.fieldnames
    ex_rows = list(r)

for rid, (code, detail) in EXCLUDES.items():
    m = meta[rid]
    ex_rows.append({
        "record_id": rid,
        "title": m["title"],
        "authors": m["authors"],
        "year": m["year"],
        "stage": "full_text",
        "exclusion_code": code,
        "exclusion_reason_detail": detail,
        "reviewer": "Claude",
        "date": TODAY,
    })

atomic_write(EXCLOG, ex_fieldnames, ex_rows)

print(f"Batch 177 recorded: {n_inc} includes, {n_exc} excludes.")
