#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "R84FCE5A47D09",  # Anand - Leaky States: Water Audits, Ignorance, and Politics of Infrastructure, Mumbai
    "R828C9773E407",  # Peda, Argento & Grossi - Mixed Public-Private Enterprise, Estonian water sector
    "RA7ECB9D783C3",  # Valencia & Ecuyer - Community Water Management in the Colombian Post-Conflict
    "R84FF08BBE70F",  # Scott, Moldogaziev & Greer - Drink what you can pay for, Houston special purpose water districts
]

EXCLUDES = {
    "RF104A3C9A7FE": ("E01", "Bolatova et al. (2021), 'Challenges of Access to WASH in Schools in Low- and Middle-Income Countries: Case Study from Rural Central Kazakhstan.' A school WASH infrastructure-condition survey (pupil survey, infrastructure observation, administrator interviews) across 3 rural Kazakh schools; a purely technical/public-health infrastructure-condition assessment with no institutional/legal water-access-mechanism analysis."),
    "R84A709AA9EB9": ("E01", "Byrnes (2013), 'A short institutional and regulatory history of the Australian urban water sector.' A detailed regulatory/institutional history of Sydney and Melbourne water utilities focused on aggregate utility financial/regulatory-structure performance and productivity comparison (National Competition Policy reform, DEA-style efficiency comparisons); no household-level eligibility/documentation/disconnection/tenure content distinguishing water-access-barrier mechanisms."),
    "RB955BA567B95": ("E06", "Berg & Mugisha (2010), 'Pro-poor water service strategies in developing countries: Promoting justice in Uganda's urban project.' A linear-programming technology-selection optimisation study comparing yard taps, public water points and pre-paid meters for a Kampala pro-poor connection project; the core empirical contribution is an engineering/economic optimisation model, not an empirical assessment of a legal/institutional mechanism's effect on water-access outcomes."),
    "R865D170681D0": ("E03", "Peres, Fernandes & Peres (2004), 'Inequality of water fluoridation in Southern Brazil - the inverse equity hypothesis revisited.' An ecological study of municipal-level water FLUORIDATION policy diffusion (presence/timing) and its association with socio-economic indicators; the outcome is a water-quality/public-health additive policy, not water access (connection, quantity, reliability)."),
    "R8699CF1378C6": ("E01", "Hunt, Staunton & Dunstan (2013), 'Equity tension and new public management policy development and implementation in the water industry.' A Queensland Australia case study of entity-level user-pays water pricing-mechanism adoption (63.7% of urban water entities) under a transaction-cost/NPM framework; a conceptual four-dimensional equity framework applied at the utility-entity level with no household-level access-barrier outcome data (no disconnection, affordability-crisis, or connection-eligibility findings)."),
    "R85C7CC7405FF": ("E01", "Hagan & Kaiser (2011), 'The displaced and dispossessed of Darfur: explaining the sources of a continuing state-led genocide.' Analyzes intentional state-led destruction of food and water sources as a mechanism of genocidal elimination in the Darfur conflict; concerns water destruction as a weapon of ethnic conflict, not a legal/institutional water-access-barrier mechanism in ordinary governance."),
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

print(f"Batch 166 recorded: {n_inc} includes, {n_exc} excludes.")
