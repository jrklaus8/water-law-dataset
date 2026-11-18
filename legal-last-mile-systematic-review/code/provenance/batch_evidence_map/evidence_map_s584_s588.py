import csv, os, tempfile

DB = "/home/user/water-law-dataset/legal-last-mile-systematic-review/05_analysis/descriptive/evidence_map.csv"

def main():
    with open(DB, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    existing_ids = {r["study_id"] for r in rows}
    for sid in ("S584", "S585", "S586", "S587", "S588"):
        assert sid not in existing_ids

    new_rows = [
        {
            "study_id": "S584",
            "study_design_class": "qualitative",
            "evidence_level": "Comparative doctrinal/case-law documentary study (3 national constitutions, 12 laws, 5 regulatory rules, 21 constitutional bills, 2 constitutional-court rulings, plus secondary literature on case-law trends) of the constitutionalization of the right to water in Brazil, Colombia, and Peru. Documents Colombia's Constitutional Court tutela jurisprudence granting household reconnection to low-income petitioners unable to pay who show imminent risk to health/life, and Peru's amparo action and 2017 constitutional right-to-water amendment; provisional confidence: moderate -- directly analogous to the previously-included S517 Morgan household reconnection/disconnection precedent, though the study's method is comparative doctrinal/case-law documentary analysis rather than primary household-level fieldwork.",
            "mechanism_family": "judicial_enforcement_reconnection",
            "outcome_family": "water_access",
            "quantitative_synthesis_eligible": "FALSE",
            "qualitative_synthesis_eligible": "TRUE",
            "legal_context": "constitutional_right_to_water_tutela_amparo",
            "institutional_context": "Colombia's Constitutional Court has recognized access to water as a human right connected to life, health, and a clean environment, and has ordered household reconnection for low-income petitioners unable to pay who show imminent risk; Peru's 2017 constitutional amendment established a right to water and the amparo constitutional writ provides (limited, slow) judicial protection; Brazil lacks a Supreme Court-recognized right to water but courts and the Ministerio Publico intervene to warn public administrators/suppliers of their water/sanitation obligations. Legal opportunity structures for enforcing socio-economic rights are found to be stronger in Colombia and Brazil, weaker in Peru.",
        },
        {
            "study_id": "S585",
            "study_design_class": "qualitative",
            "evidence_level": "Ethnographic case study (participant observation, field recording, in-depth interviews with community leadership 2013-2015) of the Acueducto II inter-basin water-transfer project's impacts on the Maconi agrarian community, Queretaro/Hidalgo, Mexico. Documents the state government's broken public-private-partnership-financed restitution promises (hydraulic network, bridge, sanitary drainage) made after tunnel-blasting construction destroyed five natural springs; provisional confidence: moderate-high -- primary interview testimony directly confirms infrastructure was only partially built and water was never delivered, though the analysis is a single-case ethnography rather than a controlled exposure-comparator design.",
            "mechanism_family": "broken_ppp_compensation_promise",
            "outcome_family": "water_access",
            "quantitative_synthesis_eligible": "FALSE",
            "qualitative_synthesis_eligible": "TRUE",
            "legal_context": "public_private_partnership_infrastructure_compensation",
            "institutional_context": "The Acueducto II water-transfer project was financed and constructed under a public-private-partnership (Union Temporal de Empresas/SAQSA consortium) model. The Queretaro state government promised the Maconi agrarian community a hydraulic network extension, a bridge, and sanitary drainage as restitution for five natural springs destroyed by tunnel-blasting; only partial infrastructure (empty pipes, storage tanks) was built and water was never delivered, forcing the community into informal inter-community water-sharing arrangements with no government involvement.",
        },
        {
            "study_id": "S586",
            "study_design_class": "qualitative",
            "evidence_level": "Ethnographic case study of everyday infrastructure practices ('sociotechnical tinkering') in a piped water supply network in Moamba, Mozambique, focused on the Block Q11 (Quarteirao 11) self-installed pipe-extension case. Documents the water utility's discretionary toleration of a technically 'unauthorized' community-installed pipe extension and the neighborhood chief's creation of a community-internal payment/exclusion rule; provisional confidence: high -- directly observed ethnographic fieldwork documents the specific fee amounts, the exclusion of non-paying households, and the utility's tacit accommodation.",
            "mechanism_family": "informal_community_exclusion_rule_utility_discretion",
            "outcome_family": "water_access",
            "quantitative_synthesis_eligible": "FALSE",
            "qualitative_synthesis_eligible": "TRUE",
            "legal_context": "informal_community_governance_utility_toleration",
            "institutional_context": "Residents of Block Q11, Bairro Central, Moamba self-installed a pipe extension using recycled materials after the water utility said it lacked budget for the extension; the utility sent a technician to connect it to the main network without complaining about the 'unauthorized works.' The Block Q11 neighborhood chief collected a 50 MT per-household contribution fee, creating a new exclusionary entitlement rule: non-contributing/refusing households are barred from connecting (or must later pay a 500 MT premium) and must buy water from connected neighbors instead.",
        },
        {
            "study_id": "S587",
            "study_design_class": "qualitative",
            "evidence_level": "Ethnographic study (12 days participant observation with 4 tanker-driver associations plus 15 interviews with policy makers, 2015 and 2017) of urban water governance through tanker water supply practices in Accra, Ghana. Documents Ghana's water law's exclusive legal recognition of GWCL as urban water provider (leaving tanker/vendor supply unregulated) and the land-tenure barrier excluding Old Fadama informal-settlement residents from legal piped connections; provisional confidence: high -- direct ethnographic fieldwork and interviews with regulators/policy makers document the formal governance framework and its practical exclusionary effects.",
            "mechanism_family": "legal_non_recognition_land_tenure_exclusion",
            "outcome_family": "water_access",
            "quantitative_synthesis_eligible": "FALSE",
            "qualitative_synthesis_eligible": "TRUE",
            "legal_context": "informal_provider_non_recognition_land_tenure",
            "institutional_context": "Ghana Water Company Limited (GWCL) is the only legally recognized urban water provider; tanker and vendor water supply -- despite supplying roughly half of Accra's population in some form -- is absent from water laws/policies and outside the Public Utility Regulatory Commission's oversight. Residents of the Old Fadama informal settlement lack the legal land tenure required for a direct GWCL connection (fewer than 2% have their own tap) and depend on tanker-supplied private vendors, who are documented to collude with tanker drivers to create shortages and raise prices.",
        },
        {
            "study_id": "S588",
            "study_design_class": "mixed_methods",
            "evidence_level": "Mixed-methods case study (ACTogether community-level survey data across 57 informal settlements plus semi-structured interviews) of drivers of household water-access vulnerability in Kampala, Uganda. Documents how Kampala's overlapping land-tenure system and stand-pipe connection-fee requirements determine legal eligibility for piped-water access; provisional confidence: moderate-high -- a normalized community-level vulnerability index is calculated across all 57 settlements and corroborated by interview testimony, though the tenure/access relationship is documented narratively rather than through a directly modeled quantitative association.",
            "mechanism_family": "land_tenure_connection_fee_exclusion",
            "outcome_family": "water_access",
            "quantitative_synthesis_eligible": "FALSE",
            "qualitative_synthesis_eligible": "TRUE",
            "legal_context": "land_tenure_connection_fee_eligibility",
            "institutional_context": "Kampala has five overlapping land-tenure systems, and access to a legal piped-water connection depends on land ownership and the ability to pay a stand-pipe connection fee; since most slum residents do not own land, piped water is generally untenable for them unless they pay a stand-pipe manager for access. Kampala Capital City Authority (KCCA) upgrading efforts favor top-down 'clearing' over participatory upgrading undertaken by the NGO ACTogether, which is associated with better-maintained sanitation infrastructure and greater community uptake. 48 of 57 slum communities scored below the water-access-vulnerability threshold.",
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
