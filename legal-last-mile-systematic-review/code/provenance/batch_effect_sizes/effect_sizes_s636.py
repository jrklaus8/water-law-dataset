#!/usr/bin/env python3
import csv, os, tempfile

DB = "05_analysis/effect_sizes/effect_sizes.csv"


def main():
    with open(DB, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    existing_ids = {r["study_id"] for r in rows}
    assert "S636" not in existing_ids, "S636 already exists"

    row = {
        "study_id": "S636",
        "outcome_family": "service_coverage",
        "synthesis_family": "",
        "exposure_definition": (
            "Participation in Indonesia's Water Hibah (WH) intergovernmental "
            "performance-grant program -- a fiscal/administrative mechanism "
            "under which a kabupaten/kota (local government) makes an equity "
            "investment in its PDAM (local water enterprise), which the PDAM "
            "uses to establish household water connections for the poor, "
            "triggering a Ministry of Finance transfer (Rp 2 million per "
            "connection for the first 1,000, Rp 3 million thereafter) once "
            "connections are verified operational."
        ),
        "comparator_definition": (
            "Matched control kabupaten/kota not participating in the Water "
            "Hibah program in 2010-2011, drawn via one-to-one nearest-neighbour "
            "propensity-score matching from a pool of 65 local governments "
            "subsequently added to the program in 2013."
        ),
        "effect_measure": (
            "Propensity-score-matched treatment/control OLS regression and "
            "hurdle-model regression (probit selection equation plus "
            "conditional linear regression, bootstrapped standard errors, "
            "endogenous-transfer instrumentation)"
        ),
        "effect_estimate": (
            "WH program participation increases per capita PDAM equity "
            "investment by Rp 739 in constant 2000 terms (Rp 2,141 in "
            "2010-11 terms), coefficient 739.1, z=3.20, p<0.05. WH-financed "
            "investment per capita is a significant positive determinant of "
            "new household water connections per 1,000 persons: coefficient "
            "0.0003 (t=6.16, investment treated as exogenous) / 0.0004 "
            "(t=1.71, investment treated as endogenous), both significant at "
            "conventional levels. Estimated marginal cost of a WH-financed "
            "connection is Rp 2.5-2.9 million versus Rp 6.9-8.2 million for a "
            "connection financed from other local-government revenue sources "
            "-- a statistically significant difference in cost-efficiency. "
            "The WH program-participation dummy itself is not significant "
            "once WH-financed investment is separately specified, indicating "
            "the grant's effect on connections operates through the financed-"
            "investment channel rather than participation per se."
        ),
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "",
        "sample_size": "35 treatment + 35 control kabupaten/kota (34 after common-support trimming); 105 pooled local-government-year observations, 2010-2011",
        "direction": "positive (Water Hibah program participation and grant-financed investment associated with HIGHER household water connections, relative to non-participating matched local governments)",
        "adjusted": (
            "adjusted (log of other revenues per capita, log population, "
            "percentage of population urban, percentage of population poor, "
            "lagged percentage of population with access to water, log gross "
            "regional domestic product per capita; propensity-score-matched "
            "treatment/control sample; on/off-Java and year instruments for "
            "the endogenous WH-transfer specification)"
        ),
        "evidence_status": "OBSERVED",
        "provenance_note": (
            "extraction_database.csv S636; source Lewis 2014, Bulletin of "
            "Indonesian Economic Studies 50(3):415-433, Tables 5-10. A clean "
            "fiscal/administrative-grant exposure (Water Hibah performance-"
            "grant program and grant-financed PDAM equity investment) tested "
            "by a well-identified quasi-experimental design (one-to-one "
            "nearest-neighbour propensity-score matching with documented "
            "bias-reduction statistics, endogenous-transfer instrumentation) "
            "against a directly measured household-level water-connection "
            "outcome, with statistically significant coefficients and an "
            "explicit cost-efficiency comparison."
        ),
        "included_in_pooled_estimate": "FALSE",
        "exclusion_from_pooling_reason": (
            "ANALYSIS_PLAN.md S2 -- single quantitative study using an "
            "Indonesia-specific intergovernmental fiscal-transfer/performance-"
            "grant exposure and a household water-connection outcome; the "
            "exposure (a fiscal grant conditioning PDAM equity investment) "
            "does not cleanly match PROJECT_SPEC.md S8's Family A (legal "
            "recognition/tenure/eligibility), Family B (bureaucratic "
            "assistance/procedural simplification), or Family C (legal/"
            "administrative barriers) definitions, and no other quantitative "
            "study in the corpus shares this specific fiscal-grant "
            "operationalization, so pooling is not yet possible or "
            "meaningful."
        ),
    }

    rows.append(row)

    fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmppath, DB)

    print("Appended effect_sizes row for S636. New total:", len(rows))


if __name__ == "__main__":
    main()
