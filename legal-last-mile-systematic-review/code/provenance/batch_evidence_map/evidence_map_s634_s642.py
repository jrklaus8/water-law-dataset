#!/usr/bin/env python3
import csv, os, tempfile

DB = "05_analysis/descriptive/evidence_map.csv"


def main():
    with open(DB, newline="", encoding="utf-8") as f:
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
        "S634",
        "cross-sectional household survey with GIS spatial epidemiology",
        "moderate-high",
        "tenure-based connection refusal and illegal pan-latrine status barring formal water/sanitation access",
        "household water-source type, sanitation-facility access, cholera incidence",
        "FALSE",
        "TRUE",
        "Ghana: GWCL tenure-based connection-refusal policy; 2009 High Court pan-latrine ban",
        "Ghana Water Company Limited; Accra Metropolitan Assembly",
    )
    add(
        "S635",
        "qualitative single-case study",
        "moderate-high",
        "legally-institutionalized participatory co-production water-governance mechanism",
        "household water-delivery predictability and service quality",
        "FALSE",
        "TRUE",
        "Venezuela: 2006 Organic Law on Communal Councils, technical water committees (MTAs)",
        "Hidrocapital; community water councils (CCAs)",
    )
    add(
        "S636",
        "quasi-experimental propensity-score-matched impact evaluation",
        "high",
        "intergovernmental fiscal/administrative performance-grant mechanism",
        "household formal water connection",
        "TRUE",
        "TRUE",
        "Indonesia: Water Hibah intergovernmental performance grant (Ministry of Finance)",
        "PDAMs (local government water enterprises); kabupaten/kota local governments",
    )
    add(
        "S637",
        "qualitative case study (KIIs, FGDs, observation)",
        "moderate",
        "dual statutory/customary water governance and gender-based exclusion from statutory institutions",
        "household water access, conflict over quantity/reliability",
        "FALSE",
        "TRUE",
        "Kenya: Water Act 2002 statutory Water Management Committees",
        "customary chiefs/elders; statutory WMCs; peace committees",
    )
    add(
        "S638",
        "qualitative case study with intervention/control comparison",
        "moderate-high",
        "NGO-facilitated institutional workaround to a legal-tenure connection barrier",
        "household formal water connection",
        "FALSE",
        "TRUE",
        "Bangladesh: DWASA tenure-based connection-refusal policy",
        "DSK NGO-facilitated CBOs; DWASA",
    )
    add(
        "S639",
        "historical documentary/archival case study",
        "high",
        "municipal water-connection licensing system and its social-class distribution",
        "household/institutional water connection, spatial access inequality",
        "FALSE",
        "TRUE",
        "colonial Peru: Cabildo water-connection licensing ordinances, 1578-1700",
        "Lima Cabildo; Water Judge; pipeline commissioners",
    )
    add(
        "S640",
        "qualitative comparative case study",
        "moderate-high",
        "spatially-differentiated legal service-provision model and traditional-authority land governance",
        "household water/sanitation service type and coverage",
        "FALSE",
        "TRUE",
        "South Africa: Free Basic Water Policy; Urban Development Line; Ingonyama Trust land",
        "eThekwini Water and Sanitation Unit; traditional authority",
    )
    add(
        "S641",
        "cross-sectional quantitative study (regression)",
        "moderate",
        "water-committee administrative-governance characteristics",
        "water-scheme functionality/reliability",
        "FALSE",
        "TRUE",
        "Ethiopia: community water-committee bylaws/financial-audit governance",
        "rural community water committees",
    )
    add(
        "S642",
        "cross-sectional household survey with chi-square test",
        "moderate",
        "notified/non-notified slum legal status and ward-level political fragmentation/clientelism",
        "household water/sanitation/drainage access",
        "FALSE",
        "TRUE",
        "India: West Bengal Municipal Act 1993; notified/non-notified slum classification",
        "Kolkata Municipal Corporation; ward councillors",
    )

    fd, tmppath = tempfile.mkstemp(dir=os.path.dirname(DB))
    with os.fdopen(fd, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(tmppath, DB)

    print("Appended 9 evidence_map rows. New total:", len(rows))


if __name__ == "__main__":
    main()
