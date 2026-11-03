import csv, os, tempfile

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/descriptive/evidence_map.csv"

def main():
    with open(DB, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    existing_ids = {r["study_id"] for r in rows}
    for sid in ("S590", "S591", "S592"):
        assert sid not in existing_ids

    new_rows = [
        {
            "study_id": "S590",
            "study_design_class": "quasi_experimental",
            "evidence_level": "Historical quasi-experimental logit analysis (244 Prussian cities, 1880-1887) exploiting cross-province variation in municipal franchise/voting-rights law (the tax-weighted Three Class System vs. more equal franchise in Hannover/Holstein) to estimate its association with the probability a city invested in waterworks infrastructure, with instrumented cost and full covariate adjustment plus counterfactual province-swap simulations; provisional confidence: high -- one of the strongest causal-identification designs in the corpus for a legal-institutional exposure and a water-infrastructure-coverage outcome.",
            "mechanism_family": "franchise_voting_power_infrastructure_investment",
            "outcome_family": "primary_connection",
            "quantitative_synthesis_eligible": "TRUE",
            "qualitative_synthesis_eligible": "TRUE",
            "legal_context": "municipal_franchise_voting_rights_structure",
            "institutional_context": "Prussian municipal franchise law varied sharply across provinces: the Three Class System (Rhineland, Westphalia) weighted votes by progressive tax payment, concentrating political power among the wealthiest 1-2% of taxpayers, while Hannover and Holstein granted a more equal, tax-based franchise. Cities under the Three Class System were significantly more likely to invest in waterworks, holding cost, wealth, public-health crisis indicators, and industrial demand constant, consistent with a hypothesis that concentrating net economic benefits of sanitary reform among the enfranchised elite accelerated infrastructure adoption. Legal constraints on municipal bonding authority also shaped which cities could act on this demand.",
        },
        {
            "study_id": "S591",
            "study_design_class": "mixed_methods",
            "evidence_level": "Institutional/fiscal-reform case study (national Chinese statistics plus an in-depth Shanghai case study, 1990-1996) documenting a socialist-era employment/housing-linked water-access mechanism and fiscal-decentralization reforms expanding municipal infrastructure-financing autonomy; provisional confidence: moderate -- tap-water coverage is tracked as an explicit outcome variable, but water/sanitation is one of several infrastructure sectors covered and the data are descriptive national aggregates rather than a regression or natural experiment.",
            "mechanism_family": "employment_housing_linked_utility_access_fiscal_decentralization",
            "outcome_family": "effective_access",
            "quantitative_synthesis_eligible": "FALSE",
            "qualitative_synthesis_eligible": "TRUE",
            "legal_context": "state_employer_housing_linked_utility_access_fiscal_decentralization",
            "institutional_context": "Prior to and through the mid-1990s, state-sector employees automatically gained access to household utilities (water, electricity, sewerage) upon receiving employer-provided housing, a mechanism that persisted for over half of urban employment. Post-1979 fiscal decentralization progressively expanded municipal governments' extra-budgetary financing autonomy for infrastructure, including nationally-endorsed infrastructure connection fees (from 1986) and, in Shanghai specifically, the 1988-92 creation of an independent Urban Construction Investment and Development Company that separated infrastructure financing authority from the Finance Bureau, coinciding with tap-water access rising to 100% in Shanghai and 94.9% nationally by 1996.",
        },
        {
            "study_id": "S592",
            "study_design_class": "qualitative",
            "evidence_level": "Qualitative case study (interviews with utility, municipal, FIS, central-government, and consumer-association stakeholders) of water-utility privatization and network-extension governance in Cochabamba, Bolivia, with household connection-rate data disaggregated by neighborhood income level; provisional confidence: high -- primary stakeholder interviews and concrete connection-rate/pricing data directly document the legal-institutional mechanisms shaping household access.",
            "mechanism_family": "utility_privatization_governance_connection_target_community_comanagement",
            "outcome_family": "primary_connection",
            "quantitative_synthesis_eligible": "FALSE",
            "qualitative_synthesis_eligible": "TRUE",
            "legal_context": "utility_privatization_concession_bidding_connection_targets",
            "institutional_context": "SEMAPA (Cochabamba's municipal water/sanitation utility) was converted to a separate legal entity in 1986 and, ahead of a planned 1996-97 privatization, had its governing board restructured by the central government to reduce local political control and its legal service-area boundary extended by a new legal framework (9,500 to 13,500 hectares). The privatization concession explicitly conditions the bid award on a target of connecting at least 90% of the population within 5 years. A World-Bank-funded community co-management and training program (FIS) trained squatter-community members in network construction, billing, and maintenance to extend formal connections, while connection rates remained starkly unequal by neighborhood income (99% in affluent Casco Viejo vs. under 4% inside-house connection in some suburban districts).",
        },
    ]

    for row in new_rows:
        extra = set(row.keys()) - set(fieldnames)
        assert not extra, f"unexpected fields in {row['study_id']}: {extra}"
        missing = set(fieldnames) - set(row.keys())
        assert not missing, f"missing fields in {row['study_id']}: {missing}"

    rows.extend(new_rows)

    fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(DB), suffix=".csv")
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmp_path, DB)

    print(f"done, evidence_map rows now {len(rows)}")

if __name__ == "__main__":
    main()
