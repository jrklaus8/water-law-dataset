#!/usr/bin/env python3
"""Evidence map rows for the 5 includes in the eighty-first full-text screening batch (S571-S575)."""
import csv
import os
import tempfile

BASE = "/home/user/water-law-dataset/legal-last-mile-systematic-review"
EM_FILE = os.path.join(BASE, "05_analysis/descriptive/evidence_map.csv")

ROWS = [
    {
        "study_id": "S571",
        "study_design_class": "mixed-methods",
        "evidence_level": (
            "Mixed-methods study (647 water-point WSSI quantitative assessments + 103 semi-structured "
            "qualitative committee interviews) of rural water security in Mvila Division, Cameroon. "
            "Documents committee-level institutional and economic failures against Cameroon's General "
            "Code of Decentralized Territorial Collectivities (Law No. 2019/024) and proposes an "
            "intermunicipal syndicate legal structure for professional maintenance; provisional "
            "confidence: moderate -- a large water-point sample combined with committee interviews, "
            "though the legal/institutional analysis is largely descriptive rather than a measured "
            "exposure-comparator effect."
        ),
        "mechanism_family": "institutional_governance",
        "outcome_family": "service_reliability",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "decentralized_territorial_collectivities_code",
        "institutional_context": (
            "Cameroon's General Code of Decentralized Territorial Collectivities (Law No. 2019/024 of "
            "24 December 2019) provides the legal framework under which water-point committees (CGPE) "
            "manage rural water points; the study documents institutional, governance, and economic "
            "dimensions of committee failures across 647 water points and proposes a legally grounded "
            "intermunicipal syndicate structure to professionalize maintenance."
        ),
    },
    {
        "study_id": "S572",
        "study_design_class": "mixed-methods",
        "evidence_level": (
            "Mixed-methods study (152 house-unit toilet mapping with GPS + natural group discussions + "
            "2 focus group discussions, total population 2,743) of shared-sanitation access and "
            "exclusion in Fante New Town, Kumasi, Ghana. Documents a landlord-permission exclusion "
            "mechanism (49% non-permittance, 84% attributed to landlord-exclusive toilet use) with "
            "detailed case studies; provisional confidence: moderate-high -- systematic house-unit-level "
            "mapping triangulated with focus groups, though the regulatory/legal dimension (legal "
            "abolition of bucket latrines; proposed landlord-provision instruments) is a secondary "
            "discussion-section finding."
        ),
        "mechanism_family": "landlord_tenant_exclusion",
        "outcome_family": "sanitation_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "bucket_latrine_prohibition",
        "institutional_context": (
            "Ghana's legal abolition of bucket ('pan') latrines shapes house-unit sanitation provision "
            "in Kumasi; the study documents landlords' de facto control over shared toilet access "
            "within multi-household compound units (case studies of exclusive landlord use) and "
            "proposes legal/social-economic instruments -- building-regulation enforcement and "
            "financial incentives -- to require landlords to provide adequate tenant sanitation."
        ),
    },
    {
        "study_id": "S573",
        "study_design_class": "qualitative",
        "evidence_level": (
            "Qualitative study (243 interviews + 39 focus group discussions across 18 communities in "
            "Ghana, Kenya, and Zambia) of community participation in INGO-supported rural "
            "water-committee governance. Documents tariff-setting decision-making, "
            "transparency/accountability rights (Rio Declaration Principle 10 framing), and "
            "power-dynamics exclusion case examples; provisional confidence: moderate-high -- a large, "
            "cross-country qualitative sample with a structured community-participation typology "
            "(Bowen et al. transactional/transitional/transformational), though the sample was drawn "
            "from 'successful' community-management sites rather than being representative."
        ),
        "mechanism_family": "MULTIPLE",
        "outcome_family": "community_participation",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "community_management_national_water_policies",
        "institutional_context": (
            "National water policies in Ghana (2007), Zambia (2010), and Kenya (2013) write community "
            "management into rural water governance; the study documents water-committee tariff-setting "
            "decision-making processes, community members' rights to transparency and accountability "
            "(information, voicing concerns, remedies), and concrete exclusion/power-imbalance examples "
            "including a headman locking a community borehole without committee permission."
        ),
    },
    {
        "study_id": "S574",
        "study_design_class": "mixed-methods",
        "evidence_level": (
            "Mixed-methods study (299 respondents across 30 rural water points; 8 FGDs; 12 KIIs) of "
            "community governance and water-point functionality in Traditional Authority Mankhambira, "
            "Nkhata Bay District, Malawi. Documents Water Point Committee governance quality "
            "(committee-trained vs functional correlation r=0.61, p<0.01), traditional-authority "
            "by-law enforcement, and informal contribution-based exclusionary access rules with "
            "explicit recommendations to codify inter-village access rights; provisional confidence: "
            "moderate -- combines a 299-respondent structured survey with FGD/KII triangulation, though "
            "purposive (non-random) sampling limits generalizability."
        ),
        "mechanism_family": "institutional_governance",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "informal_by_laws_traditional_authority",
        "institutional_context": (
            "Water Point Committees, traditional-authority chiefs, and district government jointly "
            "govern rural water access in TA Mankhambira; the study documents informal, unwritten "
            "contribution-based membership rules that exclude non-contributing households/villages "
            "from borehole access (treating water access as a private rather than communal right) and "
            "recommends codifying inter-village by-laws defining access rights, responsibilities, and "
            "penalties for misuse."
        ),
    },
    {
        "study_id": "S575",
        "study_design_class": "qualitative",
        "evidence_level": (
            "Qualitative study (98 participants: in-depth interviews and focus group discussions) of "
            "household-level water, sanitation, and hygiene access in Jenikura, Central Gonja District, "
            "Ghana, and Mpukunyoni, Mtubatuba Municipality, South Africa. Documents corruption and "
            "favouritism in water-service distribution against named statutory frameworks (South "
            "Africa's Water Services Act, Free Basic Water policy, Municipal Systems Act; Ghana's CWSA "
            "Act, Local Government Act, Public Health Act); provisional confidence: moderate-high -- "
            "cross-country qualitative comparison with detailed named legislative analysis and quoted "
            "participant testimony on distributional inequity, though evidence remains "
            "perception-based rather than independently verified."
        ),
        "mechanism_family": "corruption_favouritism_distribution",
        "outcome_family": "water_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "MULTIPLE",
        "institutional_context": (
            "South Africa's Water Services Act (1997), National Water Act (1998), Free Basic Water "
            "policy (2001), and Municipal Systems Act (2000) govern household water-service delivery in "
            "Mtubatuba; Ghana's CWSA Act (1998), Local Government Act (1993), and Public Health Act "
            "(2012) govern delivery in Central Gonja District. The study documents participant "
            "testimony on corruption/favouritism (preferential water-tanker deliveries to "
            "socially-connected households) and a public-private-partnership water-treatment model "
            "(Novubu-Mtubatuba Municipality) as a potential replication template."
        ),
    },
]


def main():
    with open(EM_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    existing_ids = {row["study_id"] for row in rows}
    for row in ROWS:
        assert row["study_id"] not in existing_ids, f"{row['study_id']} already exists"
        assert set(row.keys()) == set(fieldnames), f"field mismatch for {row['study_id']}"

    rows.extend(ROWS)

    fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(EM_FILE), suffix=".csv")
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    os.replace(tmp_path, EM_FILE)

    print(f"done, evidence_map rows now {len(rows)}")


if __name__ == "__main__":
    main()
