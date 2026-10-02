#!/usr/bin/env python3
import csv, os, tempfile

EM = "05_analysis/descriptive/evidence_map.csv"


def main():
    with open(EM, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    existing_ids = {r["study_id"] for r in rows}

    def add(sid, design_class, evidence_level, mech_family, outcome_family, quant, qual, legal_ctx, inst_ctx):
        assert sid not in existing_ids, f"{sid} already exists"
        rows.append({
            "study_id": sid,
            "study_design_class": design_class,
            "evidence_level": evidence_level,
            "mechanism_family": mech_family,
            "outcome_family": outcome_family,
            "quantitative_synthesis_eligible": quant,
            "qualitative_synthesis_eligible": qual,
            "legal_context": legal_ctx,
            "institutional_context": inst_ctx,
        })

    add(
        "S612",
        "qualitative",
        "Qualitative ethnographic study (32 in-depth interviews drawn from a 304-participant base sample) of women's household water access in Gressier, Haiti; provisional confidence: moderate -- rich lived-experience data on informal institutional dynamics, corroborated by a cited 40% service-restriction statistic, but a qualitative synthesis rather than a statistically tested exposure-outcome relationship.",
        "informal_unregulated_pipe_networks_household_access",
        "service_reliability",
        "FALSE",
        "TRUE",
        "haiti_informal_water_infrastructure_governance_vacuum",
        "Water infrastructure in Gressier, Haiti operates almost entirely outside formal government documentation or oversight (no accessible records of existing infrastructure; DINEPA and international NGOs/relief agencies are the nominal but largely absent regulatory presence), resulting in informal neighbor-to-neighbor pipe networks with unregulated payment schemes -- an estimated 40% of households with piped access have services restricted monthly for non-payment, and households have paid up to US$100 for pipe installations that never functioned.",
    )

    add(
        "S613",
        "mixed_methods",
        "Mixed-methods case study (293-household survey across 4 Jalisco municipalities plus official/stakeholder interviews) of drinking-water quality/access regulation in Western Mexico; provisional confidence: moderate-high -- concrete survey-measured intermittency/cost data corroborated by official CONAGUA inspection-rate statistics, but reported descriptively rather than through a regression linking the legal exposure to the outcome.",
        "weak_water_regulation_enforcement_household_intermittency_affordability",
        "service_reliability",
        "FALSE",
        "TRUE",
        "mexico_1992_national_waters_law_conagua_concession_enforcement_nom127",
        "Mexico's 1992 National Waters Law concession system and CONAGUA's near-nonexistent enforcement capacity (269 inspections/year across 41,116 Jalisco concessions) combine with a weak NOM-127-SSA1-1994 drinking-water standard (second-worst of 6 countries against WHO guidelines) to produce documented household-level water intermittency (34.1% receive water daily, 27.3% twice a week or less, household survey n=293) and affordability burdens (48% resorted to tanker-truck water at 358% higher cost).",
    )

    fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(EM))
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmppath, EM)

    print("Appended", 2, "evidence_map rows: ['S612', 'S613']")


if __name__ == "__main__":
    main()
