#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "R7EE9044E5204",  # Golooba-Mutebi - public/private/community water provision Rwanda & Uganda
    "R7EE2F2CC79B7",  # Obeta - Rural water supply in Nigeria: policy gaps and future directions
    "R7DF2A5059A76",  # Diaz-Cayeros, Magaloni & Ruiz-Euler - traditional governance, Oaxaca Mexico
    "R7C16D234F08C",  # Mallick - Amplifying community voices for drinking water access, Bangladesh
]

EXCLUDES = {
    "R80F6DB4B063B": ("E05", "Brocklehurst (2014), 'The 2014 Sanitation and Water for All High Level Meeting: what does it tell us about how developing countries are tackling inequalities?' Descriptive coding/analysis of 307 stated political commitments (pledges) tabled by 43 developing countries at a global partnership meeting; documents the CONTENT of commitments and cites JMP/GLAAS background statistics, but presents no empirical evidence of institutional mechanisms' actual effects on water-access outcomes -- a monitoring/advocacy report of stated intentions, not an empirical institutional-mechanism study."),
    "R800C51E60CEC": ("E01", "Scodanibbio & Manez (2005), 'The World Commission on Dams: A fundamental step towards integrated water resources management and poverty reduction? A pilot case in the Lower Zambezi, Mozambique.' Basin-scale dam-operation/water-resources governance study examining Cahora Bassa dam's effects on downstream agricultural, fishing, and prawn-industry livelihoods and IWRM/WCD governance recommendations; not a household water/sanitation access study, consistent with the basin-scale exclusion precedent (Tapela, this same pool)."),
    "R8BF0E540D98E": ("E12", "Huby (1995), 'Water Poverty and Social Policy: A review of issues for research.' Self-labeled as 'a review of issues for research' in its own title; synthesizes existing UK OFWAT/DSS reports, consultations, and prior studies on water affordability/disconnection without original empirical data collection of its own."),
    "R8AEFC6F889E8": ("E01", "Parsa, Nakendo, McCluskey & Page (2011), 'Impact of formalisation of property rights in informal settlements: Evidence from Dar es Salaam city.' Study of land-tenure formalization and access to credit/collateral in informal settlements; water/sanitation is mentioned only briefly (5-7 times in a 70,000-character paper) as background motivation, not the empirical focus, which is property-rights registration and financial-sector credit access."),
    "R7D749313D4F4": ("E01", "Kefeni & Yallew (2018), 'Communal latrine utilization and associated factors in Addis Ababa, Ethiopia: a community-based cross-sectional study.' Cross-sectional survey and logistic regression of behavioral/environmental determinants of latrine USE among households with existing physical access (age, family size, distance, cleaning frequency, latrine design); not an institutional/legal access-mechanism study, consistent with the behavioral/engineering-adjacent exclusion precedent."),
    "R7C2124844CF8": ("E04", "Salman, Al-Karablieh & Haddadin (2008), 'Limits of pricing policy in curtailing household water consumption under scarcity conditions.' Econometric household water-demand-function analysis (price and income elasticity of consumption quantity among already-connected households in Jordan); the outcome is consumption/demand quantity given existing connection, not connection/access probability or an institutional access-mechanism outcome."),
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
        assert row["full_text_decision"] in ("", None), f"{rid} already decided"
        row["full_text_status"] = "included"
        row["full_text_decision"] = "include"
        row["final_decision"] = "include"
        row["reviewer_1"] = "Claude"
        n_inc += 1
    elif rid in EXCLUDES:
        assert row["full_text_decision"] in ("", None), f"{rid} already decided"
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

print(f"Batch 184 recorded: {n_inc} includes, {n_exc} excludes.")
