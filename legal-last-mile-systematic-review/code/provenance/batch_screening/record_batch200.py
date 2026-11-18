#!/usr/bin/env python3
import csv
import tempfile
import os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/full_text/full_text_screening_database.csv"
EXCLOG_PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/02_screening/exclusion_log/exclusion_log.csv"

REVIEWER = "Claude-AI-fulltext-2026-09-27"
DATE = "2026-09-27"

INCLUDES = {
    "RB67EF412F779": "Gomes & Hermans 2018 (Land Use Policy) institutional-change case study of drinking-water access in peri-urban Khulna, Bangladesh (Matumdanga and Phultala). Documents how formal legal/institutional mechanisms -- the WATSAN committee tube-well licensing quota system (Matumdanga's repeated licence-application failures since 1996) versus Phultala's successful constitutional/statutory legal challenge (Bangladesh Constitution Arts. 32/40/42, Environmental Conservation Act 1995, Groundwater Management Ordinance 1985) against a KCC groundwater-abstraction project -- directly determine differential drinking-water access outcomes for the two communities. Extends the institutional-discretion/legal-mechanism precedent line (e.g. Behailu et al Ethiopia local-government incapability, Batch 196).",
    "RB26ACD9EDC54": "Morales & Zambrano 2018 (Poblacion y Salud en Mesoamerica) mixed social/technical/institutional survey study of sanitation management in the informal settlement Bajo Los Anonos, San Jose, Costa Rica. Documents that informal land tenure ('precario', 43% of surveyed households) and fear of eviction directly discourage household investment in sanitation infrastructure improvements, combined with documented municipal institutional non-response despite awareness of the problem; wastewater DBO5 sampling and household survey data (82% cite poor wastewater management as the main problem) link this institutional/tenure mechanism to measured sanitation-access/quality outcomes. Extends the Scott, Cotton & Khan Dakar tenure-security-and-investment precedent (S996, Batch 197).",
    "R26D33D07A9AC": "Das 2016 (Environment and Planning A) cross-case institutional analysis of the Community Managed Water Supply Scheme (CMWSS) in three Indian cities (Gwalior, Indore, Jabalpur), examining how decentralization under the 74th Constitutional Amendment Act (1992), notified-slum status, and Community Water and Sanitation Committee (CWASC) governance arrangements with municipal corporations produced starkly different water-connection and cost-recovery outcomes across the three cities (household survey n=322, interviews, focus groups). A strong institutional/legal-mechanism study directly documenting differential water-access outcomes tied to municipal governance and decentralization-law design.",
}

EXCLUDES = {
    "R29678D9CBF7A": ("E01", "Zekri 2008 (Agricultural Water Management) economic-incentives/regulation study of groundwater over-abstraction and seawater intrusion in the Batinah agricultural region of Oman -- examines irrigation water quotas, energy quotas, and subsidy/tax instruments for agricultural groundwater management. Basin-scale agricultural water-RESOURCE-allocation study (93% of groundwater used for irrigation), not a household domestic water-access study; reapplies the established basin/catchment-scale E01 precedent (Andersen 2016 Peru, Batch 195; Kumasi et al Barekese, Batch 193)."),
    "RB5516429E2DC": ("E01", "Mkondiwa, Jumbe & Wiyo 2013 (African Development Review) Canonical Correlation Analysis of the statistical association between household poverty (income/expenditure) and lack of access to safe water in rural Malawi (n=1,651 households). Purely a socioeconomic-determinants correlation study with no legal/institutional mechanism tested; reapplies the established socioeconomic-determinants E01 precedent (Daniere & Takahashi Bangkok, Batch 198)."),
    "RB57130FC082E": ("E01", "Massarutto & Ermano 2013 (Utilities Policy) national-level regulatory-design critique of Italy's 1994 water and sanitation sector reform (concession-contract regulation, full-cost-recovery, territorial integration) -- argues underperformance stems from poor regulatory design rather than ownership structure. General institutional-reform/regulatory-design analysis of aggregate service quality, investment, and pricing outcomes with no documented differential household-level access-inequality mechanism (confirmed via full-text search: no discussion of poor/low-income/tenant households, affordability disparities, or social tariffs). Reapplies the general institutional-reform E01 precedent (Clark & Mondello France, Batch 199; Pinto/Da Cruz/Marques Portugal PPP, Batch 198)."),
    "RB67D8330DA11": ("E01", "Adams, Boateng & Amoyaw 2015 (Social Indicators Research) generalized-linear-model regression of socio-economic and demographic predictors (wealth, education, household size, marital status, gender of household head, region, urban/rural residence) of potable water and sanitation access using the 2008 Ghana Demographic and Health Survey. Purely socioeconomic-determinants regression with no legal/institutional/regulatory variable tested; reapplies the established Daniere & Takahashi Bangkok E01 precedent (Batch 198)."),
    "RB407CBC6296A": ("E01", "McKay & Bjornlund 2001 (Social Justice Research) broad review of Australia's COAG water-sector reform legal instruments (Trade Practices Act, Competition Policy Reform Act, water-entitlement legislation) across both rural irrigation water markets and urban water pricing, synthesizing others' survey findings on social-justice/equity implications. Predominantly a basin-scale rural irrigation-water-market allocation review (E01 precedent, Andersen 2016/Derman & Ferguson Zimbabwe Batch 199) with a general urban-pricing-equity literature synthesis rather than an original documented access-inequality mechanism analysis of household water access; reapplies the general institutional-reform-review E01 precedent (Nallathiga Mumbai, Batch 193)."),
    "R27F9A4C5890B": ("E05", "Musembi 2014 (Waterlines) normative/doctrinal argument article elaborating 'active, free, and meaningful' participation as a human right in water and sanitation governance, drawing on international human-rights instruments (Aarhus Convention, Berlin Rules, UN Declaration on the Right to Development) and illustrative secondary examples. Conceptual/theoretical piece with no original empirical data collection on documented access-inequality outcomes; reapplies the established opinion/conceptual-essay E05 precedent (Gupta, Ahlers & Ahmed, Batch 198; Planas, Batch 196)."),
    "R276F53A7E8D1": ("E01", "Kohlitz, Chong & Willetts 2016 (Water Policy) qualitative document-analysis study coding 19 national water/sanitation policies across 13 Pacific island countries for how they envision MONITORING the human rights to water and sanitation (governance roles/responsibilities, information flows, service-delivery-dimension coverage). The study's subject is the design quality of national monitoring policy documents themselves, not documented household water-access outcomes or a legal/institutional mechanism's effect on access; reapplies the established WASH-monitoring-governance E01 precedent (Welle et al, Batch 197)."),
}


def atomic_write(path, fieldnames, rows):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path))
    with os.fdopen(fd, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp, path)


def process_db():
    with open(PATH, newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    decided = []

    for row in rows:
        rid = row["record_id"]
        if rid in INCLUDES:
            detail = INCLUDES[rid]
            row["full_text_status"] = "retrieved"
            row["full_text_decision"] = "include"
            row["reviewer_1"] = REVIEWER
            row["final_decision"] = "include"
            row["notes"] = (row.get("notes", "") + " " if row.get("notes") else "") + detail
            decided.append(row)
        elif rid in EXCLUDES:
            code, detail = EXCLUDES[rid]
            row["full_text_status"] = "retrieved"
            row["full_text_decision"] = "exclude"
            row["exclusion_reason"] = code
            row["exclusion_reason_detail"] = detail
            row["reviewer_1"] = REVIEWER
            row["final_decision"] = "exclude"
            row["notes"] = (row.get("notes", "") + " " if row.get("notes") else "") + detail
            decided.append(row)

    atomic_write(PATH, fieldnames, rows)
    return decided, fieldnames


def append_exclusion_log(decided):
    with open(EXCLOG_PATH, newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    for row in decided:
        if row["final_decision"] != "exclude":
            continue
        rows.append({
            "record_id": row["record_id"],
            "title": row["title"],
            "authors": row["authors"],
            "year": row["year"],
            "stage": "full_text",
            "exclusion_code": row["exclusion_reason"],
            "exclusion_reason_detail": row["exclusion_reason_detail"],
            "reviewer": REVIEWER,
            "date": DATE,
        })

    atomic_write(EXCLOG_PATH, fieldnames, rows)


if __name__ == "__main__":
    assert len(INCLUDES) + len(EXCLUDES) == 10
    decided, _ = process_db()
    assert len(decided) == 10
    append_exclusion_log(decided)
    n_inc = sum(1 for r in decided if r["final_decision"] == "include")
    n_exc = sum(1 for r in decided if r["final_decision"] == "exclude")
    print(f"Batch 200 processed: {n_inc} includes, {n_exc} excludes.")
