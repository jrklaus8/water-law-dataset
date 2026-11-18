import csv, os, tempfile

EM = "/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/descriptive/evidence_map.csv"

def main():
    with open(EM, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    existing_ids = {r["study_id"] for r in rows}
    new_rows = []

    def add(sid, design_class, evidence_level, mech_family, outcome_family, quant, qual, legal_ctx, inst_ctx):
        assert sid not in existing_ids
        new_rows.append({
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
        "S599",
        "mixed_methods",
        ("Mixed-methods cross-sectional study (129-household survey + 6 FGDs + 18 KIIs, 3 villages) "
         "comparing water access/satisfaction by presence/absence of a registered Community Based "
         "Water Supply Organisation (COBWSO) in rural Tanzania; provisional confidence: moderate-high "
         "-- clean 3-village natural comparison with large, consistent disparities, though observational "
         "rather than a formal regression."),
        "community_water_institution_presence_access",
        "primary_connection",
        "FALSE",
        "TRUE",
        "tanzania_cobwso_water_institution_formal_informal",
        ("Tanzania's Water Resources Management Act 2009 and Rural Water Supply and Sanitation Act "
         "2019 establish a framework of formal (basin/catchment committees, national policy) and "
         "informal (customary, village by-law) institutions for water governance; the presence of a "
         "functioning, registered Community Based Water Supply Organisation (COBWSO) in one of 3 "
         "surveyed villages (Kibaoni) corresponds to 58% improved-water-source access and 72% "
         "satisfaction, versus under 3% improved access and over 80% dissatisfaction in the 2 villages "
         "without a registered COBWSO."),
    )

    add(
        "S600",
        "quantitative_observational",
        ("Book-length household survey (n=3,714) across 4 major Indian cities examining domestic "
         "water access/expenditure plus a one-way ANOVA comparing utility efficiency/effectiveness/"
         "customer-satisfaction scores by institutional-arrangement type; provisional confidence: "
         "moderate -- study design and scope confirmed from preface/TOC/introduction, but the full "
         "Chapters 5-9 body text was not completely read, so specific numeric findings are provisional."),
        "institutional_arrangement_type_utility_performance",
        "affordability",
        "TRUE",
        "TRUE",
        "india_municipal_water_utility_institutional_arrangement",
        ("Four Indian cities' water utilities operate under different institutional-arrangement types "
         "(departmental, parastatal board, corporatized utility); the book's Chapter 8 reports a "
         "significant one-way ANOVA difference in water-supply efficiency, effectiveness, and customer-"
         "satisfaction scores across these institutional types, alongside a 3,714-household survey "
         "documenting income- and education-stratified disparities in water-connection cost and monthly "
         "expenditure (Chapter 6) and unequal water-collection burden by class and gender (Chapter 7)."),
    )

    add(
        "S601",
        "quasi_experimental",
        ("Jurimetric case-law analysis of 4 South African judicial decisions (Nokotyana 2010, Beja "
         "2011, Kenton 2017, Msunduzi/Mshengu 2019) on municipal legal accountability for sanitation-"
         "delivery failures, each involving a specific, real, named community; provisional confidence: "
         "high -- concrete, verifiable judicial-record outcomes (toilet counts, enclosure orders, "
         "contempt findings) for each case, showing an escalating remedial pattern (from deference to "
         "enforced structural interdicts) across the 4 cases in chronological sequence."),
        "structural_interdict_judicial_enforcement_sanitation",
        "service_quality",
        "FALSE",
        "TRUE",
        "south_african_constitutional_sanitation_duty_structural_interdict",
        ("South Africa's Constitution ss 152-153, the Municipal Systems Act, and the Water Services Act "
         "s 3 impose a legal duty on municipalities to deliver basic sanitation services; across 4 "
         "decided cases from 2010-2019, courts progressed from budgetary-constraint deference "
         "(Nokotyana) to dignity-based enforcement ordering enclosure of 1,316 toilets (Beja), to "
         "contempt-of-court findings against a Municipal Manager for sewage-pump-maintenance failure "
         "(Kenton), to a comprehensive court-supervised structural interdict ordering VIP-toilet "
         "construction for every farm-occupier household regardless of private-landowner objection "
         "(Msunduzi), establishing the structural interdict as the primary emerging remedy for "
         "sanitation-delivery legal accountability."),
    )

    add(
        "S602",
        "qualitative",
        ("Narrative (non-systematic) literature/documentary review applying an 'urban water security "
         "territory' framework to Cartagena, Colombia's 1991-2019 water governance history; provisional "
         "confidence: moderate-high -- documented, verifiable coverage-rate discrepancies and a clear "
         "institutional mechanism (an un-updated land-use zoning law), though based on documentary "
         "analysis rather than primary household data collection."),
        "land_use_zoning_political_instability_service_exclusion",
        "service_coverage",
        "FALSE",
        "TRUE",
        "cartagena_pot_land_use_law_political_instability",
        ("Cartagena's 2001 Plan de Ordenamiento Territorial (POT, adopted under Colombia's Law 388 of "
         "1997) defined service-coverage 'urban zones' that systematically excluded long-standing "
         "informal settlements; the POT was never formally updated from 2001-2019 due to political "
         "instability (11 different mayors in 9 years), leaving official coverage indicators (up to "
         "99.91% aqueduct) to mask an estimated 25,898-70,000 unserviced residents in excluded zones, "
         "with a locally recalculated coverage rate (96.35%/86.32%) revealing the gap obscured by the "
         "official POT-zone-bounded metric."),
    )

    add(
        "S603",
        "mixed_methods",
        ("Mixed-methods case study (292-household survey + 45 water-operator interviews, 3 peri-urban "
         "settlements) of self-governed off-utility-grid water provision in Dar es Salaam, examining an "
         "unenforced statutory groundwater-extraction permit regime; provisional confidence: moderate -- "
         "income-stratified price/reliability/health disparities are clearly documented via survey data, "
         "but the legal mechanism is observed mainly through its non-enforcement rather than through "
         "variation in its application."),
        "unenforced_extraction_permit_market_self_governance",
        "affordability",
        "FALSE",
        "TRUE",
        "tanzania_water_resources_act_groundwater_permit_nonenforcement",
        ("Tanzania's Water Resources Management Act 2009 s 11(3) exempts legal landowners/occupiers "
         "from needing a permit for domestic-use shallow wells, while requiring a permit for commercial "
         "groundwater extraction; in 3 peri-urban Dar es Salaam settlements without utility service, "
         "commercial market-oriented water operators (tanker trucks, kiosks) extract and sell "
         "groundwater largely without the required permit, and the resulting unregulated water market "
         "is linked to substantial income-stratified disparities in price (100-500 TZS/20L depending on "
         "source), water-budget share (66% of low-income vs. 11% of high-income households spend over "
         "5% of disposable income on water), and self-reported typhoid (48.7%) and diarrhoea (21.3%) "
         "prevalence attributed by the Ward Health Officer to unregulated groundwater quality."),
    )

    add(
        "S604",
        "mixed_methods",
        ("Rapid (non-systematic) review combined with documentary/institutional analysis and the "
         "author's own participant observation as a national sanitation-verification-team facilitator, "
         "examining Ghana's decentralized sanitation-service-delivery legal framework; provisional "
         "confidence: moderate -- a directly tracked national outcome trend and a concrete GAMA project "
         "completion count are documented, but review methodology and some unquantified participant-"
         "observation claims limit causal specificity."),
        "decentralization_institutional_fragmentation_bylaw_nonenforcement",
        "service_coverage",
        "FALSE",
        "TRUE",
        "ghana_local_governance_act_ministerial_fragmentation_bylaw_gazetting",
        ("Ghana's Local Governance Act 2016 (Act 936) decentralizes the sanitation-delivery mandate to "
         "Metropolitan/Municipal/District Assemblies (MMDAs), but overlapping responsibility between the "
         "Ministry of Sanitation and Water Resources (policy) and the Ministry of Local Government and "
         "Rural Development (implementing-staff oversight) creates an 'institutional dilemma' that "
         "undermines policy follow-through; an estimated 80% of MMDA sanitation by-laws remain "
         "ungazetted and therefore unenforceable. National improved-sanitation access rose only "
         "marginally from 6% (1990) to 18% (2017) despite three decades of decentralization, while a "
         "World-Bank-funded GAMA project completed 21,091 household toilets across 12 MMDAs, exceeding "
         "its target ahead of schedule, illustrating that donor-funded, project-based interventions can "
         "outperform the routine decentralized institutional framework."),
    )

    fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(EM) or ".")
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows + new_rows)
    os.replace(tmppath, EM)

    print(f"Appended {len(new_rows)} evidence_map rows: {[r['study_id'] for r in new_rows]}")

if __name__ == "__main__":
    main()
