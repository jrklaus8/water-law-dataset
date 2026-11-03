#!/usr/bin/env python3
import csv, tempfile, os

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/effect_sizes/effect_sizes.csv"


def atomic_write(path, fieldnames, rows):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path))
    with os.fdopen(fd, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp, path)


with open(PATH, newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

existing_ids = {r["study_id"] for r in rows}

new_rows = [
    {
        "study_id": "S1143",
        "outcome_family": "service_coverage",
        "synthesis_family": "C",
        "exposure_definition": (
            "Detroit Sanitation Division's administrative service-delivery rules: the explicit "
            "'weight rule' (routes/resources allocated proportional to garbage tonnage "
            "generated per census tract) and its supplementary 'center-city' equity rule "
            "(additional resources allocated to the inner city beyond the weight rule alone)."
        ),
        "comparator_definition": "Census tracts differing in neighborhood social well-being (distance from CBD / housing age) and racial composition (percent black), holding garbage generated per person constant.",
        "effect_measure": "OLS regression / Pearson correlation coefficients",
        "effect_estimate": (
            "Weight-rule fidelity: resource allocation (routes-per-1000-persons) correlates "
            "r=.842 with garbage collected per person (man-hours-per-1000-persons: r=.699). "
            "Garbage generated per person is itself significantly higher in neighborhoods "
            "farther from the CBD (higher social well-being) and with higher white population "
            "share (Table 6). With weight-rule effect controlled (Table 7), distance from CBD "
            "is significantly negatively related to resource allocation -- more sanitation "
            "resources go to inner-city (less-well-off) tracts than the weight rule alone would "
            "produce -- while percent black is not independently significant, indicating the "
            "explicit equity supplement operates by geography/well-being rather than race per "
            "se, producing an overall U-shaped distributional curve by neighborhood well-being."
        ),
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "",
        "sample_size": "420 Detroit census tracts, July/October 1973",
        "direction": "mixed (weight rule alone favors better-off/lower-density neighborhoods; supplementary center-city equity rule reverses this for the innermost tracts, producing a U-shaped net distribution)",
        "adjusted": "TRUE",
        "evidence_status": "OBSERVED",
        "provenance_note": (
            "extraction_database.csv S1143; source Jones, Greenberg, Kaufman & Drew 1978, "
            "Journal of Politics, Tables 6 and 7. Family C (administrative/legal barriers and "
            "access inequality): OLS-regression estimates directly isolating explicit "
            "administrative service-delivery rules' effect on differential sanitation-resource "
            "distribution across neighborhoods."
        ),
        "included_in_pooled_estimate": "FALSE",
        "exclusion_from_pooling_reason": (
            "ANALYSIS_PLAN.md S2 decision tree -- single study defining this exact "
            "exposure-outcome pairing (Detroit sanitation service-delivery-rule resource "
            "allocation); no other Family C study yet shares this operationalization, so "
            "pooling is not yet possible or meaningful."
        ),
    },
    {
        "study_id": "S1144",
        "outcome_family": "sanitation_access",
        "synthesis_family": "B",
        "exposure_definition": (
            "Social-proximity trust in NGOs/CBOs (survey-measured trust indicator, factor-"
            "analyzed) among urban poor households in Kampala informal settlements, as a "
            "predictor of accessing NGO- or CBO-supplied sanitation services."
        ),
        "comparator_definition": "Households with lower social-proximity trust in the respective NGO/CBO, holding spatial-proximity, perception, and socio-economic covariates constant.",
        "effect_measure": "Logit regression, coefficients and marginal effects (robust standard errors)",
        "effect_estimate": (
            "NGO sanitation-access model (n=192): trust coefficient 7.014 (robust SE 1.352, "
            "p<0.01), marginal effect 1.010 -- the largest marginal effect of any included "
            "variable. CBO sanitation-access model (n=189): trust coefficient 9.029 (robust SE "
            "1.706, p<0.01), marginal effect 0.173, again the largest marginal effect among "
            "included variables. Model fit: NGO model pseudo R2=0.4381; CBO model pseudo "
            "R2=0.2631 (both Wald chi2 p<0.001)."
        ),
        "lower_CI": "",
        "upper_CI": "",
        "standard_error": "1.352 (NGO model); 1.706 (CBO model), robust standard errors",
        "sample_size": "192 households (NGO model), 189 households (CBO model), Kampala slums",
        "direction": "positive (higher social-proximity trust in NGO/CBO increases probability of accessing that organization's sanitation services)",
        "adjusted": "TRUE",
        "evidence_status": "OBSERVED",
        "provenance_note": (
            "extraction_database.csv S1144; source Tukahirwa 2011 (Wageningen thesis / "
            "Tukahirwa, Mol & Oosterveer 2011, Habitat International), Table 3.6. Family B "
            "(administrative assistance/access): logit-regression estimates with robust "
            "standard errors directly isolating a social-network/trust-based administrative-"
            "assistance mechanism's effect on differential urban-poor access to NGO/CBO-"
            "supplied sanitation services."
        ),
        "included_in_pooled_estimate": "FALSE",
        "exclusion_from_pooling_reason": (
            "ANALYSIS_PLAN.md S2 decision tree -- single study defining this exact "
            "exposure-outcome pairing (social-proximity trust and NGO/CBO sanitation-service "
            "access in Kampala); no other Family B study yet shares this operationalization, "
            "so pooling is not yet possible or meaningful."
        ),
    },
]

for nr in new_rows:
    assert nr["study_id"] not in existing_ids, nr["study_id"]

atomic_write(PATH, fieldnames, rows + new_rows)
print(f"effect_sizes.csv updated: {len(new_rows)} rows added ({len(rows)} -> {len(rows) + len(new_rows)}).")
