#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "RA420CEEC7E34",  # Brown - Reforming the Urban Environment, Germany 1870-1910
    "R59329720D787",  # Mason - Household Resources and Water Security, Philippines
    "R55280045A6D7",  # Bukari, Authur & Zachary - Social Aspects of Groundwater, Wa West District, Ghana
    "RCA0676FFA182",  # Estache & Grifell-Tatje - Distribution of Impacts of Mali's Water Privatisation
]

EXCLUDES = {
    "RDD4F59E101DE": ("E06", "Torterotot, Rebelo, Werey & Craveiro (2005), 'Rehabilitation of water networks: analysis of the decision making processes.' A survey/case-study analysis of internal utility asset-management decision-making processes (budgeting, prioritization, organizational structure) for water-PIPE rehabilitation across 14 European water utilities; an infrastructure asset-management/decision-science study, not an empirical study of a household water-access-barrier mechanism -- consistent with the established E06 engineering/technical-process exclusion precedent."),
    "REB1290DC097C": ("E05", "Munasinghe (1991), 'Water Supply Policies and Issues in Developing Countries.' A broad World Bank policy-review essay compiling WHO/World Bank regional coverage statistics, tariff/cost-recovery theory, and institutional-reform recommendations at a global/regional level; a policy synthesis drawing on secondary statistics rather than original empirical research on a specific documented legal/institutional access-barrier mechanism -- consistent with the established E05 policy-review-essay exclusion precedent."),
    "R7F996950E419": ("E05", "Satterthwaite (2003), 'The Millennium Development Goals and Urban Poverty Reduction: Great Expectations and Nonsense Statistics.' A critical policy essay arguing that official MDG water/sanitation/poverty statistics are unreliable and discussing donor/government institutional structures in general terms; a statistical-methodology and policy critique essay, not an empirical study of a specific legal/institutional water-access mechanism."),
    "R52881817AE22": ("E06", "Syaukat & Fox (2004), 'Conjunctive Surface and Ground Water Management in the Jakarta Region, Indonesia.' A hydro-economic optimization study (nonlinear GAMS programming model) comparing hypothetical ground/surface-water pumping-quota policy scenarios for economic efficiency; a technical resource-optimization modeling exercise, not an empirical study of a legal/institutional mechanism's effect on household water access -- consistent with the established E06 engineering/optimization exclusion precedent."),
    "RC8B2DF4FAAB3": ("E06", "Urakami & Parker (2011), 'The Effects of Consolidation amongst Japanese Water Utilities: A Hedonic Cost Function Analysis.' A translog hedonic cost-function econometric study of the effect of utility-merger consolidation on operating cost efficiency; a technical cost-efficiency/scale-economics study, not an empirical study of a legal/institutional mechanism's effect on household water access -- consistent with the established E06 engineering/cost-efficiency exclusion precedent."),
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

print(f"Batch 175 recorded: {n_inc} includes, {n_exc} excludes.")
