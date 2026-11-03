#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = ["RFE7846A23C22", "RFE6F4BE0CCF1", "RF816C47AF660"]

EXCLUDES = {
    "RFE11AB2AFE89": ("E01", "O'Leary (2018), 'Pluralizing Science for Inclusive Water Governance: An Engaged Ethnographic Approach to WaSH Data Collection in Delhi, India.' The paper's own contribution is a citizen-science/participatory data-collection methodology (adapting an H2S water-quality test for community self-sampling), not primarily an empirical study of a legal/institutional water-access-barrier mechanism -- matches established precedent excluding data-collection-methodology papers (cf. Post, Agnihotri & Hyun 2018)."),
    "RFDABF84847E7": ("E06", "Almandoz, Cabrera, Arregui, Cabrera Jr. & Cobacho (2005), 'Leakage Assessment through Water Distribution Network Simulation.' Pure hydraulic-engineering methodology paper (EPANET simulation, water-balance calculation) for estimating physical/apparent leakage components in a distribution network. No legal/administrative access-barrier mechanism analyzed."),
    "RFD27AC6C215B": ("E01", "Bischoff-Mattson, Maree, Vogel, Lynch, Olivier & Terblanche (2020), 'Shape of a water crisis: Practitioner perspectives on urban water scarcity and 'Day Zero' in South Africa.' Q-methodology study clustering water-management practitioners' discourse perspectives (corruption/politics, supply/demand, social justice, pragmatic optimism) on the Cape Town water crisis. Analytical object is practitioner perception-clustering via Q-method, not a legal/institutional mechanism's measured effect on water access."),
    "RFA83F1BCC6A9": ("E01", "Das, Laishram & Jawed (2019), 'Public participation in urban water supply projects - The case of South-West Guwahati, India.' Develops and validates a stakeholder-engagement/public-participation framework (critical success factors, six-level participation ladder) for water-infrastructure PROJECT planning, using expert validation. A project-management/framework-development methodology study, not an empirical analysis of a legal/institutional water-access-barrier mechanism."),
    "RF84BAA4E54CD": ("E06", "Xu, VanBriesen, Small & Fischbeck (2009), 'Decision making under information constraints.' Pure engineering/operations-research paper on sensor-placement optimization models (graph-theory, deterministic/stochastic/robust optimization) for water-quality contamination detection in distribution networks. No legal/administrative access-barrier mechanism analyzed."),
    "RF7BB1B57C0B3": ("E06", "Arlosoroff, Roche & Wright (1989), 'Economic Considerations for Low-Cost, Groundwater-Based Rural Water Supply.' Engineering cost-benefit analytical tool for comparing pumping-technology options (handpump/solar/diesel/electric) in rural water supply, based on collection-time savings. Engineering/technology-selection economics, no legal/institutional access-barrier mechanism analyzed."),
    "RF6EFC712D0D7": ("E06", "Mitchell, Whiteside & Jones (2009), 'Water main rehabilitation and replacement: Developing and using a dynamic prioritization tool.' Pure asset-management engineering paper describing a GIS/Microsoft Access-based prioritization model for a US utility's capital water-main replacement budget, based on pipe age, material, breaks/leaks, and hydraulic performance. No legal/administrative access-barrier mechanism analyzed."),
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

print(f"Batch 153 recorded: {n_inc} includes, {n_exc} excludes.")
