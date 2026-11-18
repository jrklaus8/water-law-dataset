#!/usr/bin/env python3
import csv, os, tempfile

DB = "02_screening/full_text/full_text_screening_database.csv"
EXCLOG = "02_screening/exclusion_log/exclusion_log.csv"
REVIEWER = "Claude-AI-fulltext-2026-09-21"
TODAY = "2026-09-22"

DECISIONS = {
    "R27F9C76B923F": {
        "decision": "include",
        "notes": (
            "Oteng-Ababio 2014, GeoJournal, 520-household survey across 8 Accra, "
            "Ghana communities documenting Ghana Water Company's refusal to extend "
            "formal connections to settlements lacking secure tenure, and the "
            "post-court-judgment illegal status of pan latrines, against real "
            "household-level water-source/sanitation-facility/cholera-incidence "
            "data. Extracted as S634. Not effect_sizes eligible (descriptive "
            "survey/spatial-epidemiology study)."
        ),
    },
    "RFD53F5AA1272": {
        "decision": "include",
        "notes": (
            "McMillan, Spronk & Caswell 2014, Water International, qualitative "
            "case study (19 semi-structured interviews, 4 months participant "
            "observation) of Venezuela's legally-institutionalized technical "
            "water committees (mesas tecnicas de agua) under the Organic Law on "
            "Communal Councils, Antimano parish, Caracas, documenting a shift "
            "from unpredictable to scheduled water delivery. Extracted as S635. "
            "Not effect_sizes eligible (single-case qualitative study)."
        ),
    },
    "R2DA99A1B268E": {
        "decision": "include",
        "notes": (
            "Lewis 2014, Bulletin of Indonesian Economic Studies, propensity-"
            "score-matched quasi-experimental impact evaluation of Indonesia's "
            "Water Hibah intergovernmental performance-grant program, testing "
            "program participation and grant-financed local-government equity "
            "investment in PDAMs against household water connections per 1,000 "
            "persons. Extracted as S636. EFFECT_SIZES ELIGIBLE -- rigorous "
            "PSM+regression quasi-experimental design with a significant "
            "coefficient for grant-financed investment on household water "
            "connections; added to effect_sizes.csv."
        ),
    },
    "R561E9B9BB1CD": {
        "decision": "exclude",
        "exclusion_reason": "E05",
        "exclusion_reason_detail": (
            "McClanahan 2014 theoretical green/cultural-criminology essay on "
            "water-privatization resistance and greywater/rainwater-catchment "
            "criminalization, drawing entirely on secondary journalistic and "
            "published-book case examples (Cochabamba, Gary Harrington Oregon "
            "case, Colorado rain-barrel law); no original empirical data "
            "collection, same rationale as the Viljoen/Burdon doctrinal-"
            "commentary exclusion precedent."
        ),
    },
    "RA16A47881570": {
        "decision": "include",
        "notes": (
            "Yerian, Hennink, Greene, Kiptugen, Buri & Freeman 2014, "
            "Environmental Management, qualitative study (10 key-informant "
            "interviews, 16 focus groups, 5 structured observations) of "
            "statutory water management committees under Kenya's Water Act "
            "2002 versus parallel customary water-governance systems in "
            "Marsabit District, documenting gender/cultural barriers to "
            "women's participation in statutory water-conflict-resolution "
            "institutions. Extracted as S637. Not effect_sizes eligible "
            "(qualitative study)."
        ),
    },
    "R8A95684C4716": {
        "decision": "exclude",
        "exclusion_reason": "E01",
        "exclusion_reason_detail": (
            "Akinboade, Mokwena & Kinfack 2014, 1,000-respondent survey of "
            "citizen protest participation as a function of general municipal-"
            "service dissatisfaction across 9 bundled service categories "
            "(health, housing, water, electricity, solid waste, community "
            "services, roads, crime, jobs); core topic is civic-protest "
            "behavior/political voice, not a legal/administrative water-access "
            "mechanism, with water treated as one of several composite "
            "dissatisfaction variables -- same bundling rationale as the Mansur "
            "Belem flood-risk exclusion precedent."
        ),
    },
    "R127F98538C60": {
        "decision": "exclude",
        "exclusion_reason": "E01",
        "exclusion_reason_detail": (
            "Pandey 2015 book chapter on municipal-finance mobilization for "
            "inclusive habitat (BSUP programme, Bhopal and Hyderabad, India); "
            "water supply is one bullet point in a seven-point charter (land "
            "tenure, housing, water, sanitation, education, health, social "
            "security) with the core topic being municipal fiscal-resource "
            "convergence strategy, not water/sanitation access via a specific "
            "legal/administrative mechanism."
        ),
    },
    "RDC37E0771C28": {
        "decision": "exclude",
        "exclusion_reason": "E05",
        "exclusion_reason_detail": (
            "van Dijk & Blokland 2016 is the editorial introduction to a "
            "special journal issue, summarizing other contributed papers' "
            "pro-poor water/sanitation benchmarking research; presents no "
            "original empirical data collection of its own, same rationale as "
            "the systematic-review-of-secondary-literature exclusion precedent."
        ),
    },
    "R3C12B6E203E7": {
        "decision": "include",
        "notes": (
            "Hossain & Ahmed 2015, Urban Water Journal, case-study "
            "investigation (9 focus group discussions/109 participants, 18 "
            "structured interviews, 3 intervention vs. 3 control slums) of an "
            "NGO-facilitated non-conventional public-private partnership "
            "(DSK/DWASA) overcoming Dhaka slum dwellers' lack of legal tenure "
            "as a barrier to formal water-utility connection. Extracted as "
            "S638. Not effect_sizes eligible (qualitative intervention/control "
            "case-study comparison, no regression-based effect estimate)."
        ),
    },
    "R4C4BF3B533F6": {
        "decision": "include",
        "notes": (
            "Bell 2015, The Professional Geographer, historical political-"
            "ecology archival study (Libros de Cabildos de Lima municipal "
            "council minutes, 1578-1700) of colonial Lima's drinking-water "
            "connection-licensing system (Cabildo, Water Judge, pipeline "
            "commissioners), documenting 63 petitions/80 documented "
            "connections and the social-class distribution of licenses "
            "(disproportionately Cabildo members) producing spatial water-"
            "access inequality. Extracted as S639. Uses the Legal "
            "Institutional Evidence Appraisal Framework, following the "
            "Hallstrom 2005 (S583) historical-archival precedent. Not "
            "effect_sizes eligible."
        ),
    },
    "R5252E45E9BD7": {
        "decision": "include",
        "notes": (
            "Sutherland, Scott & Hordijk 2015, European Journal of "
            "Development Research, case study (126 interviews across 4 "
            "settlements with contrasting land-tenure/governance status -- "
            "Ingonyama Trust traditional-authority land vs. municipal urban "
            "land) of eThekwini Municipality's Free Basic Water Policy and "
            "Urban Development Line spatially-differentiated service-"
            "provision model, documenting real household-level service-type "
            "variation (ground tanks/VIP vs. full-pressure/flush) across "
            "settlements. Extracted as S640. Not effect_sizes eligible "
            "(qualitative case study)."
        ),
    },
    "R180FA98A1842": {
        "decision": "exclude",
        "exclusion_reason": "E01",
        "exclusion_reason_detail": (
            "Seward, Xu & Turton 2015 is a desk-based backcasting policy "
            "analysis of South Africa's national groundwater-resource "
            "governance (competing agricultural/commercial use), based on "
            "practitioner experience and secondary literature rather than "
            "original household-level empirical data; concerns resource-level "
            "governance rather than household water/sanitation service "
            "access, same macro-governance rationale as the Nkiaka/Schiel/"
            "Laitinen exclusion precedent."
        ),
    },
    "RC0A0303230CB": {
        "decision": "include",
        "notes": (
            "Alexander, Tesfaye, Dreibelbis, Abaire & Freeman 2015, "
            "International Journal of Public Health, quantitative study (89 "
            "rural Ethiopian community water schemes, direct observation plus "
            "water-committee interviews) testing water-committee governance "
            "characteristics (record-keeping, financial audits, fees, paid "
            "caretaker, repair capacity) via regression against a functionality "
            "score. Extracted as S641. Not effect_sizes eligible (univariate "
            "logistic-regression associations for operational status are not "
            "statistically significant given the small sample, n=82)."
        ),
    },
    "RD190F3A11A59": {
        "decision": "include",
        "notes": (
            "De & Nag 2016, International Journal of Social Economics, "
            "541-household survey across 23 Kolkata slums (notified vs. "
            "non-notified legal status) examining religious/caste identity, "
            "political fragmentation/clientelism, and notified-slum legal "
            "status as determinants of household water/sanitation/drainage "
            "access, with a significant chi-square association between "
            "political fragmentation/competition and physical water access. "
            "Extracted as S642. Not effect_sizes eligible (descriptive/"
            "comparative statistics, no regression coefficient table for the "
            "water-access outcome)."
        ),
    },
    "R8134515D9626": {
        "decision": "exclude",
        "exclusion_reason": "E01",
        "exclusion_reason_detail": (
            "Favaro et al. 2016 book chapter analyzes water as a municipal-"
            "level 'environmental service' (watershed-protection area "
            "coverage, native forest remnants, HDI) across 39 municipalities "
            "in the Metropolitan Region of Sao Paulo; no household-level "
            "water/sanitation access, connection, or affordability data -- "
            "same macro/municipal-level governance rationale as the Nkiaka/"
            "Schiel/Laitinen exclusion precedent."
        ),
    },
}


def main():
    with open(DB, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    by_id = {r["record_id"]: r for r in rows}
    for rid in DECISIONS:
        assert rid in by_id, f"{rid} not found"
        r = by_id[rid]
        assert not r["full_text_decision"] and not r["final_decision"], f"{rid} already decided"

    excl_rows = []
    for rid, d in DECISIONS.items():
        r = by_id[rid]
        r["full_text_decision"] = d["decision"]
        r["final_decision"] = d["decision"]
        r["full_text_status"] = "retrieved"
        r["reviewer_1"] = REVIEWER
        if d["decision"] == "include":
            r["notes"] = d["notes"]
        else:
            r["exclusion_reason"] = d["exclusion_reason"]
            r["exclusion_reason_detail"] = d["exclusion_reason_detail"]
            excl_rows.append({
                "record_id": rid,
                "title": r["title"],
                "authors": r["authors"],
                "year": r["year"],
                "stage": "full_text",
                "exclusion_code": d["exclusion_reason"],
                "exclusion_reason_detail": d["exclusion_reason_detail"],
                "reviewer": REVIEWER,
                "date": TODAY,
            })

    fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmppath, DB)

    if excl_rows:
        with open(EXCLOG, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            exc_fieldnames = reader.fieldnames
            exc_existing = list(reader)
        exc_existing.extend(excl_rows)
        fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(EXCLOG))
        with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=exc_fieldnames)
            writer.writeheader()
            writer.writerows(exc_existing)
        os.replace(tmppath, EXCLOG)

    print("Batch 113 decisions recorded:", {k: v["decision"] for k, v in DECISIONS.items()})
    print("exclusion_log.csv new rows:", len(excl_rows))


if __name__ == "__main__":
    main()
