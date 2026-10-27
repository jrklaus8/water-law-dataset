#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "RABD874ECDC9D",  # Larrain - Human Rights and Market Rules in Chile's Water Conflicts
    "RAF5FDD222D54",  # Avidar - Half-hearted Devolution, Kenya's water governance, Siaya County
    "RAAA3E8CD5A17",  # Allison - Balancing responsibility for sanitation, Cape Town CBOs
    "RA88CE2AB8E94",  # Wahby - Urban informality and the state, Cairo Gehood Zateya
    "RA78F7A82EE77",  # Akumuntu et al - Enabling sustainable FSM service delivery chain, Kigali
]

EXCLUDES = {
    "RAF1193CDC9AF": ("E01", "Bond (2000), 'Economic Growth, Ecological Modernization or Environmental Justice? Conflicting Discourses in Post-Apartheid South Africa.' Broad political-economy/environmental-discourse essay examining three illustrative case studies (basic-needs infrastructure financing including water/sanitation, an industrial zinc-smelter zone, and the Lesotho-Johannesburg water transfer scheme); water/sanitation is one of three illustrative topics within a much broader macro-political-economy discourse analysis, not a dedicated water-access institutional-mechanism study -- consistent with the established 'water as minor topic' exclusion precedent (Presbey Detroit)."),
    "RA8A5580EBB31": ("E01", "Frenoux & Tsitsikalis (2015), 'Domestic private fecal sludge emptying services in Cambodia: between market efficiency and regulation needs for sustainable management.' Field survey of Cambodia's private fecal-sludge-extraction-and-transportation-operator (ETO) market, framed around market efficiency and profitability of private operators; supply-side market-economics analysis, not a legal/institutional water/sanitation-access-barrier study -- consistent with the established sanitation-business-economics exclusion precedent (Nimoh et al., Batch 178)."),
    "RAEF4F8AC8D31": ("E05", "Ranganathan (2016), 'Thinking with Flint: Racial Liberalism and the Roots of an American Water Tragedy.' Confirmed via full-text read to be explicitly self-framed as 'this essay' applying a critical-race-theory/political-theory framework ('racial liberalism') to interpret the Flint water crisis; an argumentative/interpretive theoretical essay drawing on secondary historical sources, with no described original data collection (no interviews, surveys, or original archival research methodology) -- consistent with the established conceptual-essay E05 exclusion precedent (Loftus, Coles)."),
    "RA3D65AC0E1D7": ("E01", "Vivekanandan (2009), 'Nano Applications, Mega Challenges: The Case of the Health Sector in India.' Confirmed via full-text read that this article concerns nanotechnology governance in India's health/pharmaceutical sector; water is mentioned only in passing (a single sentence on nanomembrane water-filter commercialization and a South African pilot project cited as an aside) with no substantive water-access content -- a title/abstract-corpus-inclusion error, not wrong_file_retrieved (title/author match the delivered PDF exactly)."),
    "RA3683AE3534F": ("E06", "Hoko & Hertle (2006), 'An evaluation of the sustainability of a rural water rehabilitation project in Zimbabwe.' Technical monitoring-and-evaluation study of an NGO-implemented borehole rehabilitation project, assessing pump functionality, breakdown rates, headworks condition and community-management performance as project-sustainability indicators; a technical/engineering project-performance evaluation, not a study of a legal/institutional water-access mechanism."),
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

print(f"Batch 179 recorded: {n_inc} includes, {n_exc} excludes.")
