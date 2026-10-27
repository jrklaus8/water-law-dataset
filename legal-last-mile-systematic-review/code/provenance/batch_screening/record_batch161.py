#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "RC8E4D27449CF",  # Koelble & LiPuma - institutional obstacles, South Africa
    "RC3F88BC83E64",  # Hirvi & Whitfield - clientelist political settlements, Ghana
    "RC2F103D94FC7",  # Kelly-Richards & Banister - Nogales Sonora, land tenure/water access
    "RC2ADB3C483ED",  # Devas - Cambodia Battambang, local government/water enterprise
    "RC00FA37AB2F9",  # Jimu - Nkolokoti water kiosks, Malawi
]

EXCLUDES = {
    "RC4001C6C73B3": ("E01", "Akosa, Franceys, Barker & Weyman-Jones, 'Efficiency of Water-Supply and Sanitation Projects in Ghana.' A data envelopment analysis (DEA) methodology paper measuring technical efficiency scores for 10 water/sanitation projects; 'institutional' appears only as one generic DEA input-category label, not an analyzed legal/institutional access-barrier mechanism -- matches the Guppy (2014) Water Poverty Index methodology-development precedent."),
    "RC0750E198B8C": ("E01", "Peter & Nkambule (2012), 'Factors affecting sustainability of rural water schemes in Swaziland.' A Multi-Criteria Analysis of technical, social, financial, environmental, and internal community-management (institutional) factors correlated with rural water-scheme functionality; the 'institutional' factor concerns internal community user-committee/leader coordination, not a formal legal/institutional government access-barrier mechanism -- matches the general WASH-sustainability-factors methodology exclusion precedent."),
    "RC0409B5F0BE0": ("E03", "Petelet-Giraud et al. (2017), 'Multi-layered water resources, management, and uses under the impacts of global changes... Recife, NE Brazil.' A hydrogeological/environmental-science field study (isotope/water-chemistry sampling by a geological-survey research team) on aquifer overexploitation and salinization; Brazilian water law and governance are discussed narratively but with no primary institutional data collection (no interviews or household survey) -- institutional context is background only, matching the Rowles et al. (2020) precedent."),
    "RC02292A9D406": ("E01", "Furlong (2015), 'Water and the entrepreneurial city: The territorial expansion of public utility companies from Colombia and the Netherlands.' An analytical/theoretical paper on municipal water corporations' international commercial expansion strategy (EPM Medellin, WMD Netherlands); concerns corporate strategy in new international markets, not a domestic household water-access-barrier mechanism."),
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
    # RBEDB6556B711 (Olmstead, Thirsty Colonias) left untouched: correct file
    # delivered (title/author/journal/pages all confirmed matching), but the
    # underlying PDF appears to be a scanned/image JSTOR reprint whose text
    # extraction returned only the repeated JSTOR cover-page/footer boilerplate,
    # not the article body -- no usable content to screen against. Left open,
    # not flagged wrong_file_retrieved (file identity is correct), pending a
    # future extraction retry.

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

print(f"Batch 161 recorded: {n_inc} includes, {n_exc} excludes, 1 left undecided (RBEDB6556B711, unreadable scanned PDF).")
