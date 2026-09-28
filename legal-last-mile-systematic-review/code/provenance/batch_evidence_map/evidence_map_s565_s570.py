import csv, tempfile, os

path = "05_analysis/descriptive/evidence_map.csv"

with open(path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

new_rows = [
    {
        "study_id": "S565",
        "study_design_class": "mixed_methods",
        "evidence_level": "Mixed-methods case study (150-household survey, environmental spot measurements, policy document review) developing and applying the Greywater Service Innovation Ladder (GSIL) governance-maturity framework for decentralised greywater services in Southlea Park, Harare, Zimbabwe. Documents concrete legal-institutional mechanisms (RDC/ward-committee gate-decision authority, Equity Safeguard Ratio affordability threshold, statutory greywater-policy vacuum) with a household survey and composite governance-index computation; provisional confidence: moderate -- a single-settlement case study with a reasonably sized household sample (n=150) but no comparator settlement.",
        "mechanism_family": "MULTIPLE",
        "outcome_family": "effective_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "common law",
        "institutional_context": "Zimbabwe's National Water Policy Review (2021) makes only limited reference to greywater management, leaving peri-urban settlements to manage wastewater informally; the proposed Greywater Service Innovation Ladder (GSIL) assigns Gate 1 (household-to-community) decision authority to Rural District Council (RDC)/ward committees and Gate 2 (community-to-micro-utility) authority jointly to RDC and a regulator; the Equity Safeguard Ratio (ESR) benchmarks household affordability against a 3-5% income threshold; and rollback/pause mechanisms are triggered if health or equity thresholds deteriorate below required levels.",
    },
    {
        "study_id": "S566",
        "study_design_class": "qualitative",
        "evidence_level": "Qualitative participatory photovoice study (10 teachers, 10 students, 6 facilitated group discussions, 75-participant advocacy event) of school WASH governance gaps in two urban primary schools in Jimma Town, Ethiopia. Documents concrete institutional-governance mechanisms (weak monitoring/supervision, unclear inter-agency responsibility, absence of facility-deterioration reporting channels) with direct participant testimony and a structured advocacy-event bridging mechanism; provisional confidence: moderate -- a two-school qualitative case study with a modest but methodologically rich participant base (20 core participants plus 75 advocacy-event attendees).",
        "mechanism_family": "MULTIPLE",
        "outcome_family": "effective_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "civil law",
        "institutional_context": "Participants documented an institutional-governance gap in school WASH management: unclear division of responsibility among school administrations, health workers, and local authorities for facility maintenance and reporting; absence of formal mechanisms for reporting deteriorated or full sanitation facilities; and a bureaucratic hierarchy in which accountability flows upward from schools to higher officials with no institutional channel for students/teachers to present concerns directly -- a gap the study's advocacy-event methodology was designed to bridge by convening students, teachers, and local officials for direct dialogue.",
    },
    {
        "study_id": "S567",
        "study_design_class": "mixed_methods",
        "evidence_level": "Mixed-methods cross-sectional study (400-household survey across 120 water points, technician/engineer/committee key-informant interviews) of rural water-scheme functionality and sustainability governance in Gursum District, Eastern Ethiopia. Documents concrete legal-institutional mechanisms (WASHCO tariff/fee authority, government-dominated technology selection despite nominal community ownership, District Water Office institutional support) with a large representative household sample and weighted composite sustainability scoring; provisional confidence: high -- large randomly sampled household survey (n=400) across a proportionally sampled set of 120 water points with a validated multi-subindicator sustainability instrument.",
        "mechanism_family": "MULTIPLE",
        "outcome_family": "effective_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "civil law",
        "institutional_context": "Rural water schemes are nominally community-owned (73.3%) and WASHCO-managed (tariff-setting, fee collection, O&M financial management), but technology selection is overwhelmingly government-determined (85.8%) rather than community-determined (3.0%); District Water and Energy Resources Development Office (WWRDO) and NGOs (UNICEF, PSNP) provide external technical/financial support (67.8% of schemes); and national nonfunctionality-reduction targets (10% by 2012, 7% for Oromia by 2015) remain unmet, with the overall sustainability score at only 32.9% and 91% of WASHCOs providing no timely financial reporting to their communities.",
    },
    {
        "study_id": "S568",
        "study_design_class": "mixed_methods",
        "evidence_level": "Participatory mixed-methods concept-mapping study (22 stakeholders including policymakers, NGO representatives, water/education-sector officials, disability-advocacy leaders, and students with physical disabilities) of strategies for inclusive school WASH access in the Upper West Region, Ghana. Documents concrete legal-institutional mechanisms (CRPD normative baseline, unimplemented Inclusive Education Policy, proposed accountability/sanction roadmap) via structured brainstorming/sorting/rating and multidimensional-scaling cluster analysis; provisional confidence: moderate -- a methodologically structured concept-mapping process with a modest, purposively selected but multi-sector stakeholder sample (n=22 core participants, 35 at consultative workshop).",
        "mechanism_family": "MULTIPLE",
        "outcome_family": "effective_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "common law",
        "institutional_context": "The UN Convention on the Rights of Persons with Disabilities (CRPD) provides the normative baseline for equitable WASH-service access; Ghana's national Inclusive Education Policy exists formally but, per stakeholder testimony, lacks the financial and human resources for implementation; and stakeholders proposed a roadmap of punitive/accountability measures to sanction supervisors or authorities who deliberately deny students with physical disabilities access to WASH facilities, alongside local-government intervention mechanisms including resource mobilization, monitoring, and WASH database/reporting requirements.",
    },
    {
        "study_id": "S569",
        "study_design_class": "mixed_methods",
        "evidence_level": "Mixed-methods case study (150-household survey, 7 key-informant interviews, 4 focus group discussions) applying shit flow diagram (SFD), city service delivery assessment (CSDA), and SWOT analysis to citywide sanitation governance in Noakhali Pourashava, Bangladesh. Documents concrete legal-institutional mechanisms (National Strategy for Water Supply and Sanitation's silence on fecal sludge management, CSDA-scored institutional/regulatory gaps by sanitation domain) with a household survey and named-institutional-actor key-informant triangulation; provisional confidence: moderate -- a single-municipality case study with a modest household sample (n=150) and structured multi-tool institutional assessment.",
        "mechanism_family": "MULTIPLE",
        "outcome_family": "effective_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "common law",
        "institutional_context": "Bangladesh's National Strategy for Water Supply and Sanitation (2014) establishes the policy goal of open-defecation-free status via sanitary toilets and sewage-network coverage but makes no reference to fecal sludge management (FSM); CSDA institutional-domain scoring documents that off-site sanitation policy/legislation and treatment/reuse regulation score 'poor' across enabling, developing, and sustaining governance stages, while on-site sanitation policy scores comparatively better on enabling but 'poor' on funding/capacity; and named institutional actors (WASA, DPHE, Noakhali Pourashava, UNDP) were interviewed on statutory and regulatory responsibility gaps, with only 3% of excreta safely reaching treatment.",
    },
    {
        "study_id": "S570",
        "study_design_class": "qualitative",
        "evidence_level": "Qualitative multi-case study (documentary review, 31 combined key-informant interviews across three countries, three participatory cross-case analysis workshops) of sub-national government sanitation-leadership mechanisms in Siaya County (Kenya), Nyamagabe District (Rwanda), and Moyo District (Uganda). Documents concrete legal-institutional mechanisms (constitutional/statutory decentralisation architecture, a governor's signed financial-commitment letter, mandatory livelihood-benefit/toilet-use conditionality) using a participatory Most Significant Change/outcome-harvesting methodology; provisional confidence: moderate-high -- a structured three-country comparative case-study design with named-official interviews and cross-case collective-analysis workshops, though case selection favored settings with demonstrated positive change.",
        "mechanism_family": "MULTIPLE",
        "outcome_family": "effective_access",
        "quantitative_synthesis_eligible": "FALSE",
        "qualitative_synthesis_eligible": "TRUE",
        "legal_context": "MULTIPLE",
        "institutional_context": "Kenya's 2010 constitutional reform (implemented 2013) devolved sanitation-provision responsibility to 47 elected county governments; Uganda's 1980s decentralisation devolved sanitation responsibility to 135 Districts, though district decisions remain financially/politically dependent on central government per cited scholarship; Rwanda's 2000 decentralisation reforms assign implementation to 30 district councils under centrally-set five-year targets; and the study documents concrete sub-national commitment mechanisms including Siaya County's governor's signed financial-commitment letter binding sanitation budget allocation, Moyo District's mandatory toilet-ownership condition for livelihood-programme benefits, and Rwanda's Human Security Issue Taskforce and WASH investment-plan institutionalisation into district development strategy.",
    },
]

rows.extend(new_rows)

fd, tmp = tempfile.mkstemp(dir="05_analysis/descriptive")
with os.fdopen(fd, "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
os.replace(tmp, path)

print("done, evidence_map rows now", len(rows))
