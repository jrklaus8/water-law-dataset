#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = ["RDAAEB54CE4DE", "RDA2517B5D58E", "RD9F8791BF7D2", "RD8B9CAF4C5DA", "RD8AD4E521D45"]

EXCLUDES = {
    "RDCB899855EE9": ("E01", "Wafer (2012), 'Discourses of Infrastructure and Citizenship in Post-Apartheid Soweto.' Traces the discursive link between infrastructure and post-apartheid citizenship through electricity-disconnection protests (Operation Khanyisa) and, briefly, the Phiri prepaid-water-metre court case. The paper's analytical object is citizenship discourse and protest politics, centred overwhelmingly on electricity; water is mentioned only in passing and is not itself analyzed as a legal/institutional access-barrier mechanism."),
    "RDB768A284CCF": ("E01", "Lee (2014), 'The Changing Nature of Border, Scale and the Production of Hong Kong's Water Supply System since 1959.' Macro-scale political-geography/border-studies analysis of transboundary bulk water supply between China and Hong Kong. Concerns state-to-state infrastructure and sovereignty politics, not a legal/administrative mechanism affecting household- or community-level water access for the poor."),
    "RDA19C702AB54": ("E05", "Willoughby-Herard (2014), \"'The only one who was thought to know the pulse of the people': Black women's politics in the era of post-racial discourse.\" A literary/cultural-studies genealogy analyzing three works of fiction (Ncgobo, Magona, Ndebele) to theorize black women's politics and protest. No empirical data on water access or a legal/institutional mechanism is examined; the method is literary textual analysis, not empirical social science."),
    "RD9AA2E70843A": ("E01", "Choguill (1994), 'Implementing Urban Development Projects: A Search for Criteria for Success.' Generic public-administration/planning-implementation framework (six constraint factors) applied comparatively to a Bangladesh squatter-resettlement project and a Tegucigalpa, Honduras water/sanitation project. The water case is one of two illustrations of a general implementation-theory framework; no specific legal/administrative access-barrier mechanism for water is analyzed."),
    "RD897F797A040": ("E01", "Roth et al. (2004), 'Those Who Get Hurt Aren't Always Being Heard: Scientist-Resident Interactions over Community Water.' Science-and-technology-studies (STS) ethnography of 'boundary work' between scientific expertise and local knowledge in a Canadian town-council dispute over extending a water main to unconnected residents. Analytical lens is expertise/discourse boundary-work, not a legal/institutional access-barrier mechanism, despite the underlying dispute concerning a municipal connection decision."),
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

print(f"Batch 149 recorded: {n_inc} includes, {n_exc} excludes.")
