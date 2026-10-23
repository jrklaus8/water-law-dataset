#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = ["RFBA3CE02FD4E", "RFB5E22BF9BB7", "RF8DC8ABACFBA", "RF7AB8DA9173B"]

EXCLUDES = {
    "RFC696CEFD0F1": ("E01", "Organizational-communication-theory analysis (Weick's sensemaking framework, Foucauldian discourse) of the Walkerton, Ontario 2000 E. coli water contamination crisis. Analytical focus is crisis sensemaking/media representation, not the legal/regulatory mechanism (privatized water testing, cost-cutting) that caused the crisis; no household-level access/exclusion outcome examined."),
    "RFB41BA4B400D": ("E01", "Gender/livelihoods study of intra-household water allocation for domestic vs. productive uses (livestock, agriculture) in North Gujarat villages, comparing source vs. no-source villages. No legal/institutional access-barrier mechanism identified (no statute, eligibility, tenure, or documentation framework); inequity documented is informal/social (elite capture of tanker water) rather than tied to a specific legal/regulatory mechanism."),
    "RFA18A400F778": ("E01", "Australian public-administration/social-network-analysis case study of a voluntary NFP-private water company partnership addressing customer financial hardship via referral pathways. Outcome measured is partnership network quality/collaboration structure, not a water-access outcome; no statute, disconnection-prevention law, or eligibility framework for the hardship program is discussed."),
    "RF94808EAE557": ("E01", "Econometric estimation of urban residential water demand price elasticity in Zaragoza, Spain, using dynamic panel data. Pure demand-economics study of already-connected households; no access/exclusion mechanism examined. Extends the Mansur & Olmstead 2012 welfare-economics precedent under E01."),
    "RF8BD93786D82": ("E01", "Choice-experiment/willingness-to-pay economics study of household-tap preferences among urban poor residents in Nima, Accra, Ghana. Examines demand-side service-attribute preferences (connection fees, service hours, provider trust); no legal/institutional access-barrier mechanism (eligibility, tenure, documentation) examined. Extends the Mansur & Olmstead 2012 precedent under E01."),
    "RF81354379727": ("E01", "Foucauldian discourse/genealogy analysis of the urban poverty debate applied to infrastructure investment, using a World Bank-funded Zambia project as illustration. Focus is on development-policy discourse and donor institutional design (aid/NGO community-organization models), not a specific government legal/administrative access-barrier mechanism; no statute, eligibility, or tenure framework analyzed."),
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

print(f"Batch 144 recorded: {n_inc} includes, {n_exc} excludes.")
