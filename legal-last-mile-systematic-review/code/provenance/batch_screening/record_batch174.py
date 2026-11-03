#!/usr/bin/env python3
import csv, tempfile, os
from datetime import date

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
SCREEN = f"{BASE}/02_screening/full_text/full_text_screening_database.csv"
EXCLOG = f"{BASE}/02_screening/exclusion_log/exclusion_log.csv"

TODAY = date.today().isoformat()

INCLUDES = [
    "R131D9C683C29",  # Miller - Watering the Garden of Tangier: Colonial Contestations
    "R0F7C649E8E07",  # Spronk - Roots of Resistance to Urban Water Privatization in Bolivia
    "R4D81D56EA98B",  # Coville, Galiani, Gertler & Yoshida - Financing Municipal Water/Sanitation, Nairobi (RCT)
    "R063CE14907E2",  # Gero & Willetts - Securing a conducive environment for WASH markets
]

EXCLUDES = {
    "R3ADAE9AD6CD1": ("E01", "Kabogo, Anderson, Hyera & Kajanja (2017), 'Facilitating public participation in water resources management: reflections from Tanzania.' A reflective/documentary review of Tanzania's Water Resources Management Act and basin-scale Water Users' Associations (WUAs); the paper's focus and case studies (Pangani, Wami/Ruvu, Lake Victoria basins) concern basin-scale water-RESOURCE allocation governance (irrigation, ecosystem needs, industrial/agricultural users), with 'domestic users' appearing only once as one of several water-user categories -- consistent with the established E01 macro-scale/basin-level water-resource-governance exclusion precedent (Grafton et al.), not a household drinking-water-access study."),
    "R35523A7C027A": ("E05", "Olivera (2001), 'The Fight for Water and Democracy: An Interview with Oscar Olivera.' A published verbatim interview transcript with a single informant (a Cochabamba union leader) recounting the Bolivian Water War, republished from a magazine feature; despite containing specific factual detail (Law 2029, the Aguas de Tunari contract), it is not an independent empirical research study with its own methodology, sampling or analysis -- a journalistic/oral-history interview transcript, not original research."),
    "R2153D357CF74": ("E01", "Torras (2005), 'Income and Power Inequality as Determinants of Environmental and Health Outcomes.' A cross-national OLS regression testing broad socioeconomic power-inequality proxies (not a documented legal/institutional water-access mechanism) against aggregate national access-to-safe-water and health outcomes; the exposure is a generic societal power-inequality construct, consistent with the established exposure-side-mismatch/macro-determinants exclusion precedent, not a specific legal/institutional mechanism."),
    "R1C7EBDEC4818": ("E05", "Coles (2009), 'Domestic water provision and gender roles in drylands.' A reflective review essay on the historical evolution of gender considerations in water-sector development policy, drawing primarily on a book the author co-edited and general secondary/grey literature rather than the author's own original fieldwork or data collection; consistent with the established E05 reflective-essay-on-secondary-sources exclusion precedent."),
    "R1876AB3E9A52": ("E01", "Stokman (1995), 'Modeling Conflict and Exchange in Collective Decision Making.' A game-theoretic political-science methodology paper introducing two abstract models of collective decision-making, illustrated with a worked example concerning Dutch water-utility merger/restructuring policy (expert-elicited actor positions on industry-concentration options); the paper concerns corporate merger/industrial-organization policy modeling, not household water access, and is fundamentally a decision-making modeling methodology exercise."),
    "R0F076F861B72": ("E05", "Griesinger & Moody (2001), 'North, South & Central America and the Caribbean.' A conference rapporteur's summary report of a regional session (120 participants) at a World Water Council-affiliated water-vision conference, synthesizing presentations and discussion points; a conference-proceedings summary with no original data collection or empirical study design."),
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

print(f"Batch 174 recorded: {n_inc} includes, {n_exc} excludes.")
