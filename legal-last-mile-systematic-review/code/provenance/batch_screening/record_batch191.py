#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "R4D48C6031F04",  # Nakyagaba et al - Power, politics and a poo pump, gulper sanitation technology, Kampala
    "R4D32E3F3E2E3",  # Jimenez, Mtango & Cairncross - What role for local government in sanitation promotion, Tanzania
    "RA32AC23D7C25",  # Balazs & Lubell - Social learning, environmental justice, integrated regional water management, California
    "RA0E245C18B33",  # Lea - Housing for Health in Indigenous Australia
    "RA1C04D0EBE47",  # Njoh & Akiwumi - Impact of colonization on access to improved water/sanitation, African cities
    "RA361E2E22F9C",  # Terhorst, Olivera & Dwinell - Social Movements, Left Governments, Water Sector Reform, Latin America
    "RA1626402A233",  # Spaling, Brouwer & Njoka - Factors affecting sustainability of community water supply project, Kenya
]

EXCLUDES = {
    "RA312FCCFFA53": ("E06", "Lin & Berg (2008), 'Incorporating Service Quality into Yardstick Regulation: An Application to the Peru Water Sector.' Technical benchmarking study using data envelopment analysis (DEA) and a quality-incorporated Malmquist productivity index to measure firm-level efficiency/productivity/quality change among 38 Peruvian water utilities; an econometric performance-measurement methodology study, not an institutional/legal access-mechanism study, with utility productivity (not household access) as the outcome."),
    "R9F7FE0255880": ("E01", "Aubin (2011), 'Non-owners' success: confrontations of rules in rivalries between water users in Belgium and Switzerland.' Theoretical/comparative case-study typology of property-rights-versus-public-policy rule confrontations in general water-resource rivalries (industrial water, hydro-power, flood control, environmental flow, one drinking-water-quality dispute among four cases); the object of study is resolution of water-resource-allocation rivalries generally, not household water/sanitation access, consistent with the established basin/resource-scale governance exclusion precedent (Tapela, Mancilla Garcia & Bodin)."),
    "RA13FEA76F392": ("E01", "Kubler & Schwab (2007), 'New regionalism in five Swiss metropolitan areas: An assessment of inclusiveness, deliberation and democratic accountability.' Comparative case study of metropolitan governance across four policy sectors (water supply, public transport, drug services, cultural amenities) with water as only one of four co-equal sectors; the outcome variables are inclusiveness, deliberation and democratic accountability of governance schemes, not water/sanitation access, consistent with the established precedent excluding studies where water is one of several indicators (Bazoglu; Lawanson & Fadare)."),
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

print(f"Batch 191 recorded: {n_inc} includes, {n_exc} excludes.")
