# Changelog

All notable methodological and structural decisions for this project are
logged here, per `REPRODUCIBILITY.md` §8 and `PROTOCOL.md` §12 (protocol
amendments in particular must be logged here with rationale).

## 2026-09-22 (latest) — Ninety-seventh full-text screening batch (2 Drive-retrieved PDFs: 1 include S616, 1 exclude)

Two PDFs surfaced in the Google Drive retrieval inbox. Both target
record_ids confirmed open with no prior `wrong_file_retrieved` history;
titles and authors verified against delivered PDFs before screening.

- **R7DF720007123** (Reniko & Kolawole 2020, *South African Geographical
  Journal*, "'They don't read metres, they only bring bills': Issues
  surrounding the installation of prepaid water metres in Karoi town,
  Zimbabwe"). **INCLUDE.** Qualitative case study: 35 resident interviews/
  FGDs across 5 high-density residential areas, plus KTC/ZINWA official
  interviews, examining a proposed prepaid water meter (PWM) policy
  framed by residents and officials as violating the Zimbabwean
  Constitution's right to water via automatic disconnection, against
  household-level access/affordability/disconnection-risk outcomes and
  real revenue-collection data (only 8.2% of possible monthly revenue
  collected under the existing post-paid system, 2018). Extracted as
  **S616**. Not effect_sizes eligible (PWMs not yet implemented at time
  of study, no exposure-comparator outcome regression).
- **R77FE93587FBF** (Grigg 2020, *Water International*, "Smart water
  management: can it improve accessibility and affordability of water
  for everyone?"). **EXCLUDE (E05, no empirical evidence).** A
  conceptual/theoretical discussion paper examining how smart-water-
  management technologies could hypothetically improve utility access
  and affordability; the paper's own central demonstration is explicitly
  conceptual/illustrative, not an original empirical study with real
  data collection.

`extraction_database.csv`/`evidence_map.csv` updated (S616, 613 → 614
rows each). `effect_sizes.csv` unchanged (31 rows; no new candidates).
`exclusion_log.csv` updated (610 rows total; E05 67 → 68).
`full_text_retrieval_queue.csv` regenerated (2,435 open records).
Duplicate audit clean (no DOI or record_id duplicates).
`validate_schemas.py` confirms all 13 tracked files OK.

Running totals: 1,224/3,659 screened (614 include/610 exclude), 2,435
open, 614 extracted studies, 31 effect_sizes rows.

## 2026-09-22 — Ninety-sixth full-text screening batch (3 Drive-retrieved PDFs: 2 includes S614-S615, 1 exclude)

Three PDFs surfaced in the Google Drive retrieval inbox. All 3 target
record_ids confirmed open with no prior `wrong_file_retrieved` history;
titles and authors verified against delivered PDFs before screening.

- **R7CD58D2E7BE3** (Agbemor & Smiley 2021, *The Journal of Development
  Studies*, "Tensions between Formal and Informal Water Providers:
  Receptivity toward Mechanised Boreholes in the Sunyani West District,
  Ghana"). **INCLUDE.** Case-study census of 98 mechanised boreholes plus
  2,439 water-user interviews, documenting privately managed informal
  boreholes operating in explicit, unenforced violation of Ghana's Water
  Resources Commission groundwater-abstraction permitting, against
  household-level water access, reliability, quantity, and affordability
  outcomes (91/93 boreholes functional >=347 days/year; >=25 L/capita/day).
  Extracted as **S614**. Not effect_sizes eligible (descriptive census
  statistics, no regression).
- **R77355A6C9E10** (Tantoh & McKay 2020, *GeoJournal*, "Rural
  self-empowerment: the case of small water supply management in
  Northwest, Cameroon"). **INCLUDE.** Household survey (108 households,
  6 villages) of community-based water management under Cameroon's 1998
  water law, documenting Water Management Committee eligibility/fee
  requirements against household water access and consumption (34%
  private connection at 35.6 L/capita/day vs 66% communal tap at 24.7
  L/capita/day; 71/108 households unable to afford connection fees).
  Extracted as **S615**. Not effect_sizes eligible (descriptive per-village
  means, no significance test, small samples).
- **R96A74867D7C2** (Sandoval & Sarmiento 2020, *Disaster Prevention and
  Management*, "A neglected issue: informal settlements, urban
  development, and disaster risk reduction in Latin America and the
  Caribbean"). **EXCLUDE (E01, wrong topic).** Macro/national-level
  comparative content analysis of 17 Habitat III National Reports
  examining urban informal-settlement prevalence and risk-governance/
  disaster-resilience discourse; water/sewerage access appears only as an
  aggregate national statistic, not tested against any specific
  legal/administrative mechanism -- same macro cross-national governance-
  index rationale as the Nkiaka/Shadabi & Ward/Laitinen/Schiel exclusions.

`extraction_database.csv`/`evidence_map.csv` updated (S614-S615, 611 →
613 rows each). `effect_sizes.csv` unchanged (31 rows; no new
candidates). `exclusion_log.csv` updated (609 rows total; E01 201 → 202).
`full_text_retrieval_queue.csv` regenerated (2,437 open records).
Duplicate audit clean (no DOI or record_id duplicates).
`validate_schemas.py` confirms all 13 tracked files OK.

Running totals: 1,222/3,659 screened (613 include/609 exclude), 2,437
open, 613 extracted studies, 31 effect_sizes rows.

## 2026-09-22 — Ninety-fifth full-text screening batch (2 Drive-retrieved PDFs: 2 includes S612-S613, 0 excludes)

Two PDFs surfaced in the Google Drive retrieval inbox. Both target
record_ids confirmed open with no prior `wrong_file_retrieved` history;
titles and authors verified against delivered PDFs before screening.

- **RB27F53708057** (Chapman, Merceron, Myers & Wood 2020, *Water
  International*, "Women's lived-experiences of water infrastructure in
  Gressier, Haiti"). **INCLUDE.** Qualitative ethnographic study: 32
  in-depth interviews (from a 304-participant base sample) with women in
  Gressier, Haiti, documenting informal, unregulated neighbor-to-neighbor
  water-pipe networks operating with no accessible government
  documentation or oversight (DINEPA nominally but largely absent),
  informal payment/non-payment/service-restriction dynamics (~40% of
  households with piped access restricted monthly for non-payment), and
  informal source-management disputes, against household water
  access/reliability/affordability outcomes. Extracted as **S612**. Not
  effect_sizes eligible (qualitative interview-based study, no
  regression).
- **R70C06383A22C** (McCulligh, Arellano-Garcia & Casas-Beltran 2020,
  *Local Environment*, "Unsafe waters: the hydrosocial cycle of drinking
  water in Western Mexico"). **INCLUDE.** Mixed-methods case study:
  293-household survey across 4 Jalisco municipalities plus
  official/stakeholder interviews, documenting Mexico's 1992 National
  Waters Law concession system, CONAGUA's near-nonexistent enforcement
  (269 inspections/year across 41,116 concessions), and the weak
  NOM-127-SSA1-1994 drinking-water standard, against household-level
  water-service intermittency (only 34.1% of surveyed households receive
  water daily) and affordability (48% resorted to tanker-truck water at
  358% higher cost) outcomes. Extracted as **S613**. Not effect_sizes
  eligible (descriptive survey statistics within a qualitative
  case-study narrative, no regression).

`extraction_database.csv`/`evidence_map.csv` updated (S612-S613, 609 →
611 rows each). `effect_sizes.csv` unchanged (31 rows; no new
candidates). `exclusion_log.csv` unchanged (608 rows; no new exclusions
this batch). `full_text_retrieval_queue.csv` regenerated (2,440 open
records). Duplicate audit clean (no DOI or record_id duplicates).
`validate_schemas.py` confirms all 13 tracked files OK.

Running totals: 1,219/3,659 screened (611 include/608 exclude), 2,440
open, 611 extracted studies, 31 effect_sizes rows.

## 2026-09-22 — Ninety-fourth full-text screening batch (4 Drive-retrieved PDFs: 3 includes S609-S611, 1 exclude)

Four PDFs surfaced in the Google Drive retrieval inbox. All 4 target
record_ids confirmed open with no prior `wrong_file_retrieved` history;
titles and authors verified against delivered PDFs before screening.

- **RE081EB767D08** (Jana, Sarkar, Thomas, Krishna Priya, Bandyopadhyay,
  Crosbie, Abi Ghanem, Waller, Pillai & Newbury-Birch 2021, *Clean
  Technologies and Environmental Policy*, "Rethinking water policy in
  India with the scope of metering towards sustainable water future").
  **INCLUDE.** Documentary/institutional policy analysis of 12 Indian
  national water supply policies (1949-2012), chronologically assessed
  against 20 SDG-6 sustainability indicators, with real government
  service-level benchmark data (household piped-water coverage, cost
  recovery, metering extent across 6 cities), tariff/subsidy structures,
  and willingness-to-pay case studies. Genuine legal/institutional
  exposure (National Water Policy 1987/2002/2012, tariff/metering
  regulatory gaps) against household water-access/affordability outcomes.
  Included via the Legal Institutional Evidence Appraisal Framework,
  consistent with the Rout & Kattumuri India book and Theodory Tanzania
  precedent. Extracted as **S609**. Not effect_sizes eligible (narrative
  indicator-based policy review, no regression-based effect estimate).
- **R4D207458780C** (Sohns, Ford, Adamowski & Robinson 2021, *Environmental
  Management*, "Participatory Modeling of Water Vulnerability in Remote
  Alaskan Households Using Causal Loop Diagrams"). **INCLUDE.** Qualitative
  participatory-modeling study: 14 water-policy stakeholders individually
  interviewed to construct causal loop diagrams of household water
  vulnerability in rural Alaska, merged into a validated collective model.
  Genuine legal/institutional exposure (water quality regulations, water
  rights permits, operations-and-maintenance funding policy) directly
  examined against household water access/availability/affordability,
  corroborated by real rate/consumption/hospitalization data. Extracted
  as **S610**. Not effect_sizes eligible (qualitative causal-loop-diagram
  synthesis, no quantitative exposure-comparator regression).
- **RAFE7B383AF05** (Gordon & Byron 2021, *Cultural Studies*, "Sweeping
  the city: infrastructure, informality, and the politics of
  maintenance"). **EXCLUDE (E01, wrong topic).** A cultural-studies/
  urban-theory essay on homeless-encampment "sweeps" and infrastructure-
  maintenance politics in Toronto and San Francisco. Though it references
  "the right to sanitation" and a UN report on water/sanitation rights in
  passing, the actual empirical focus and outcome measured (encampment
  removal/dispossession) is homelessness/housing policing, not
  water/sanitation service access.
- **R0F2F1A4CDE94** (Gonzalez Rivas 2023, *International Planning
  Studies*, "Addressing the impossible triad -- high inequality,
  decentralized policy and low local capacity -- challenges for drinking
  water policy in Mexico"). **INCLUDE.** Mixed-methods institutional
  analysis combining 2,450-municipality Mexican census data
  (1950-2010) with 15 official interviews (2011-2013) and document
  analysis of the 1972 centralized Federal Waters Law vs. the
  1976-1980s decentralization reform and CONAGUA/PROII funding-programme
  permit requirements. Genuine legal/institutional exposure
  (decentralization, 17-requirement municipal funding-proposal process)
  cross-tabulated against household water-connection outcomes by
  municipality. Included via the Legal Institutional Evidence Appraisal
  Framework. Extracted as **S611**. Not effect_sizes eligible (author
  explicitly disclaims a causal-driver interpretation of the descriptive
  cross-tabulation).

`extraction_database.csv`/`evidence_map.csv` updated (S609-S611, 606 →
609 rows each). `effect_sizes.csv` unchanged (31 rows; no new candidates
this batch). `exclusion_log.csv` updated (608 rows total; E01 200 → 201).
`full_text_retrieval_queue.csv` regenerated (2,442 open records).
Duplicate audit clean (no DOI or record_id duplicates).
`validate_schemas.py` confirms all 13 tracked files OK.

Running totals: 1,217/3,659 screened (609 include/608 exclude), 2,442
open, 609 extracted studies, 31 effect_sizes rows.

## 2026-09-22 — Ninety-third full-text screening batch (6 Drive-retrieved PDFs: 4 includes S605-S608, 2 excludes)

Six PDFs surfaced in the Google Drive retrieval inbox. All 6 target
record_ids confirmed open with no prior `wrong_file_retrieved` history;
title/authors verified against `full_text_screening_database.csv` before
reading.

- **R59468F0C4D5B** — Meredith T, MacDonald M, Kwach H, Waikuru E,
  Alabaster G (2021). "Partnerships for Successes in Slum Upgrading:
  Local Governance and Social Change in Kibera, Nairobi." Book chapter in
  *Land Issues for Urban Governance in Sub-Saharan Africa*, Springer, pp.
  237-255. doi 10.1007/978-3-030-52504-0_15. **INCLUDE.** Case study of
  the KENSUP Soweto East slum-upgrading project's Settlement Executive
  Committee (SEC), a formally constituted community institution that
  negotiated housing pricing across a political-administration change,
  prevailed in a 2-year civil court case, and secured legal property
  ownership plus K-WATSAN water/sanitation infrastructure for 822
  families. Extracted as **S605**.
- **RF8C06439B2CA** — Zhou S, Liang J (2021). "Migrant workers and
  environmental amenities and infrastructure in urban China: from the
  lens of environmental justice." *Journal of Environmental Policy &
  Planning* 23(6):781-795. doi 10.1080/1523908X.2021.1920379.
  **INCLUDE.** Panel fixed-effects regression (290 Chinese prefectural
  cities, 2008-2014) finding China's hukou household-registration status
  (a legal/administrative exclusion mechanism) significantly predicts
  lower per-capita wastewater and solid-waste treatment capacity
  (p<0.01) in cities with a higher share of unregistered temporary
  residents. Extracted as **S606**; also added to `effect_sizes.csv`
  (Family C) — a clean legal-exclusion exposure with consistent,
  robustness-checked significant coefficients (30 → 31 rows).
- **R4A2516BE7A0A** — Biswas R, Arya K, Fernandes V, Shah T (2020). "Find
  A Loo: an app for sanitation governance." *Information, Communication &
  Society* 24(11):1586-1602. doi 10.1080/1369118X.2020.1716038.
  **EXCLUDE (E01, wrong topic).** Mobile-app usability/design study (33
  evaluators, SUS/PCS Likert scales); the outcome is app usability score,
  not a population-level sanitation access outcome — a methodology paper,
  same rationale as prior crowd-sourced-data/GIS-modeling methodology
  exclusions.
- **RF92EF484E8E6** — Jeil EB, Abass K (2021). "A contextual analysis of
  public health implications of water choices and hygiene practices in
  Northern Ghana." *Local Environment* 26(5):542-556. doi
  10.1080/13549839.2021.1901269. **EXCLUDE (E01, wrong topic).**
  86-household risk-perception-theory study of water-source choice
  driven by taste, accessibility, and traditional beliefs; no legal/
  institutional exposure is examined in the empirical analysis.
- **R7D6CA19199B3** — Romano ST, Nelson-Nuñez J, LaVanchy GT (2021).
  "Rural water provision at the state-society interface in Latin
  America." *Water International* 46(6):802-820. doi
  10.1080/02508060.2021.1928973. **INCLUDE.** Comparative documentary
  review of community-based water management (CBWM) legal-recognition
  frameworks in Nicaragua (2010 Special CAPS Law), Honduras (2003 Water
  Framework Law), and Costa Rica (1939 Law of Associations/ASADAS), with
  registration-rate statistics for each country (e.g. only 30% of
  Nicaraguan CAPS registered within 5 years of the law). Extracted as
  **S607**.
- **R7F86482382FC** — Basu M, DasGupta R, Hashimoto S, Hoshino S (2020).
  "A multi-actor and bottom-up perspective on attaining rural water
  security: qualitative evidence from India." *Environment, Development
  and Sustainability* 23:1461-1484. doi 10.1007/s10668-020-00631-2.
  **INCLUDE.** Multi-actor qualitative study (282 community FGD
  participants + 33 Gram Panchayat heads + Block officials, 16 villages,
  West Bengal) documenting India's decentralized Panchayati Raj water-
  governance framework, including a directly quoted instance of caste-
  based exclusion from a community handpump and a discretionary new-
  construction-vs-maintenance funding-allocation pattern. Extracted as
  **S608**.

`extraction_database.csv`/`evidence_map.csv` updated (S605-S608, 602 →
606 rows each). `effect_sizes.csv` updated (30 → 31 rows, S606 added,
Family C). `exclusion_log.csv` updated (607 rows total; E01 198 → 200).
`full_text_retrieval_queue.csv` regenerated (2,446 open records).
Duplicate audit (DOI + record_id) and `validate_schemas.py` both clean.
Running totals: 1,213/3,659 screened (606 include/607 exclude), 2,446
open, 606 extracted studies, 31 effect_sizes rows.

## 2026-09-22 — Ninety-second full-text screening batch (8 Drive-retrieved PDFs: 6 includes S599-S604, 2 excludes)

Eight PDFs surfaced in the Google Drive retrieval inbox. All 8 target
record_ids confirmed open with no prior `wrong_file_retrieved` history;
title/authors verified against `full_text_screening_database.csv` before
reading.

- **RD6A4E2B98389** — Theodory TF (2022). "Emerging and persistent
  challenges in water resources governance in rural Tanzania: The Mgeta
  subcatchment of the Upper Ruvu Basin." *Norsk Geografisk Tidsskrift*
  76(2):110-124. doi 10.1080/00291951.2022.2048067. **INCLUDE.**
  Mixed-methods study (129-household survey + 6 FGDs + 18 KIIs, 3
  villages) comparing water access/satisfaction by presence vs. absence of
  a registered Community Based Water Supply Organisation (COBWSO) under
  Tanzania's Water Resources Management Act 2009/Rural Water Supply and
  Sanitation Act 2019 framework: 58% improved-access/72% satisfaction in
  the COBWSO village vs. under 3% improved-access/over 80% dissatisfaction
  in the 2 villages without one. Extracted as **S599**.
- **R68EEE02D1AF5** — Rout S, Kattumuri R (2022). *Urban Water Supply and
  Governance in India*. Springer. doi 10.1007/978-981-16-3819-0.
  **INCLUDE.** Book-length household survey (n=3,714) across Ahmedabad,
  Bengaluru, Hyderabad and Kochi examining domestic water access/
  expenditure plus a one-way ANOVA comparing utility efficiency/
  effectiveness/customer-satisfaction scores by institutional-arrangement
  type (departmental/parastatal/corporatized). Only the preface, table of
  contents, introduction and references were read in full given the
  book's length (~300 pages); Chapters 5-9's complete body text was not
  read, so specific numeric findings are flagged provisional pending a
  fuller read. Extracted as **S600**.
- **R805217DA7537** — Twani N, Soyapi CB (2022). "The legal accountability
  of local government in South Africa for the failure to deliver
  sanitation services." *South African Journal on Human Rights*
  38(1-2):92-111. doi 10.1080/02587203.2022.2115397. **INCLUDE.**
  Jurimetric case-law analysis of 4 decided South African cases
  (Nokotyana 2010, Beja 2011, Kenton 2017, Msunduzi/Mshengu 2019) showing
  an escalating judicial remedy pattern for municipal sanitation-delivery
  failures, from budgetary-constraint deference to enforced structural
  interdicts (e.g. Beja: court ordered enclosure of 1,316 toilets in
  Khayelitsha's Silvertown project). Extracted as **S601**.
- **R6103D8CFE42F** — Aluko OO, Esan OT, Agboola UA, Ajibade AA, John OM,
  Obadina OD, Afolabi OT (2022). "How secured and safe is the sanitation
  and hygiene services in a maximum-security correctional facility in
  Southwest Nigeria." *International Journal of Environmental Health
  Research* 32(10):2200-2217. doi 10.1080/09603123.2021.1949438.
  **EXCLUDE (E01, wrong topic).** Cross-sectional study of 420 prison
  inmates; institutional (non-household) unit of analysis, same rationale
  as prior WASH-in-healthcare-facility/WASH-in-school exclusions.
- **R97E03B20C00D** — Sullivan Lemaitre A, Stoler J (2023).
  "Socio-political barriers to sustainable urban water governance: the
  case of Cartagena, Colombia." *Water International* 48(6):783-803. doi
  10.1080/02508060.2023.2256643. **INCLUDE.** Narrative (non-systematic)
  review applying an urban water security territory framework to
  Cartagena's 1991-2019 water governance history, documenting how the
  2001 land-use zoning law (POT), never formally updated across 11 mayors
  in 9 years, systematically excludes informal settlements from official
  service-coverage zones, masking an estimated 25,898-70,000 unserviced
  residents behind official coverage rates up to 99.91%. Extracted as
  **S602**.
- **R4B1669E987E0** — Dakyaga F, Schramm S, Kyessi AG (2023). "Between
  self-help and emerging water markets: self-governance, everyday
  practices and the spatiality of water access in Dar es Salaam." *Urban
  Geography* 44(7):1369-1393. doi 10.1080/02723638.2022.2106054.
  **INCLUDE.** Mixed-methods case study (292-household survey + 45
  water-operator interviews, 3 peri-urban settlements) examining Section
  11(3) of Tanzania's Water Resources Management Act 2009 (permit-free
  domestic-well exemption vs. unenforced commercial-extraction permit
  requirement), linked to sharp income-stratified disparities in water
  price, reliability, and self-reported typhoid (48.7%)/diarrhoea (21.3%)
  prevalence. Extracted as **S603**.
- **RF0B06784A547** — Wang Y, Man C, Xu A, Shi Q (2022). "Spatial
  transformation and Chinese environmental governance innovation from an
  urban political ecology perspective: An analysis of Shenzhen's evolving
  waterscape." *Progress in Geography* 41(9):1755-1769 (Chinese-language;
  read and evaluated in the original Chinese, per
  `INCLUSION_EXCLUSION.md` criterion 10). **EXCLUDE (E01, wrong topic).**
  Urban-political-ecology documentary analysis of Shenzhen's city-scale
  water-resource commodification/governance evolution; outcomes examined
  are aggregate city-level water-consumption/wastewater-discharge/
  river-water-quality statistics, a macro/city-level water-resources
  outcome, not a household or population-level water-service-access
  outcome — same rationale as prior Nkiaka/Nigeria-OECD macro-governance
  exclusions.
- **R7E87780D0891** — Mariwah S (2022). "Decentralization and Resource
  Capacity for Sustainable Sanitation Services Delivery in Ghana." In:
  Adjei POW, Adu-Gyamfi S (eds) *Democratic Decentralization, Local
  Governance and Sustainable Development*, Springer, pp. 193-208. doi
  10.1007/978-3-031-12378-8_11. **INCLUDE.** Rapid review plus the
  author's own facilitator/verification-team observations, documenting
  Ghana's 'institutional dilemma' (overlapping MSWR/MLGRD ministerial
  responsibility) and an estimated 80% of MMDA sanitation by-laws
  remaining ungazetted/unenforceable, alongside real tracked outcome data
  (national access rose only 6%→18%, 1990-2017; a World-Bank-funded GAMA
  project completed 21,091 household toilets across 12 MMDAs ahead of
  schedule). Extracted as **S604**.

`extraction_database.csv`/`evidence_map.csv` updated (S599-S604, 596 →
602 rows each). `effect_sizes.csv` unchanged (30 rows; no new study in
this batch had a clean exposure-comparator design meeting the strict
eligibility bar). `exclusion_log.csv` updated (605 rows total; E01 196 →
198). `full_text_retrieval_queue.csv` regenerated (2,452 open records).
Duplicate audit (DOI + record_id) and `validate_schemas.py` both clean.
Running totals: 1,207/3,659 screened (602 include/605 exclude), 2,452
open, 602 extracted studies, 30 effect_sizes rows (unchanged).

## 2026-09-22 — Ninety-first full-text screening batch (7 Drive-retrieved PDFs: 6 includes S593-S598, 1 exclude)

Seven PDFs surfaced in the Google Drive retrieval inbox. All 7 target
record_ids confirmed open with no prior `wrong_file_retrieved` history;
title/authors verified against `full_text_screening_database.csv` before
reading (per the batch-88 lesson of checking authors, not just titles).

- **R7A9FA4B1B749** — Ko H (2024). "A study on the equity and influencing
  factors of local water supply services in Korea." *Journal of Korea
  Water Resources Association* 57(6):393-407. doi
  10.3741/JKWRA.2024.57.6.393. **INCLUDE.** Tobit regression (152 South
  Korean local governments, 2010/2016/2021) of Coulter distributional-
  inequity coefficients for 6 water-service-equity variables against
  administrative-district classification (si/gun), municipal fiscal
  autonomy, and local tax burden. Administrative si classification and
  local tax burden significantly improve equity (p<0.01-0.05 across all
  3 years); fiscal autonomy (financial independence) significantly
  worsens it (p<0.01, all years, all 6 variables). Extracted as **S593**;
  also added to `effect_sizes.csv` (Family C) — a clean institutional/
  fiscal-governance exposure with consistent, replicated Tobit
  coefficients (29 → 30 rows).
- **RB0165DA1B47D** — Linn C, Robbins-Panko J, Perry TE, Seibel A (2023).
  "Living with Lead: Older Adults' Experiences of Necropolitical Water
  Governance in Flint, Michigan." *Human Organization* 82(4):335-346.
  **INCLUDE.** Ethnographic interviews (46 older-adult residents,
  2016-2018) documenting Michigan's Emergency Manager law suspending
  local democratic control (enabling the 2014 water-source switch),
  state/federal water-safety emergency declarations, and a court-ordered
  consent-decree lead-service-line-replacement deadline as legal/
  institutional mechanisms shaping household water insecurity. Extracted
  as **S594**.
- **RF563E44C5B3E** — Mokoena A (2023). "Questioning Day Zero: Rights,
  Provision, and Water Inequality in Khayelitsha, Cape Town." *Human
  Organization* 82(4):324-334. **INCLUDE.** Qualitative fieldwork (10
  households + 3 officials) during the 2017-2018 Day Zero crisis
  documenting the South African constitutional water right, the Free
  Basic Water policy quantum litigated in *Mazibuko v. City of
  Johannesburg*, disproportionate installation of prepaid Water
  Management Devices in low-income/informal areas, and formal/informal
  settlement classification determining connection eligibility.
  Extracted as **S595**.
- **R238F15C4814B** — Kashem S, Tahsin N, Subah Z, Murshed SB, Nowreen S,
  Mondal MS (2023). "Assessing the right to water of the urban poor in
  Dhaka city." *GeoJournal* 88:3183-3204. doi 10.1007/s10708-022-10804-3.
  **INCLUDE.** Mixed-methods comparison (150-household survey + 9
  FGDs/12 IDIs/3 KIIs) of 3 Dhaka slums, 2 legally DWASA-connected and 1
  illegally connected. DWASA's connection requirement (conditioned on
  land title/approved building plan) excludes tenure-insecure, frequently
  -evicted residents; the illegally-connected slum pays 17x the water
  price, spends 8% of income on water (vs. 0.5-2.0%), and has the
  highest (worst) Water Security Index of the 3 slums. Extracted as
  **S596**.
- **R6022ED0189EC** — Kouassi HAA, Andrianisa HA, Traoré MB, Sossou SK,
  Nguematio RM, Djambou MD (2023). "Factors influencing community-led
  total sanitation (CLTS) implementation abandonment before achieving
  open defecation-free (ODF) status: case study of the Central-Western
  region of Burkina Faso." *Environmental Science and Pollution
  Research* 30:125628-125645. doi 10.1007/s11356-023-31142-y.
  **INCLUDE.** Content analysis (257 interviewees, 4 villages) of
  national CLTS sanitation-program abandonment; governance/institutional
  factors (subsidy-policy ambiguity applied inconsistently across
  adjoining villages, agent transfers, inter-agency coordination
  failure) account for 26.28% of abandonment cases (787 of 3,546
  triggered villages nationally). Sissili province, the only province
  using a single actor and the original unsubsidized approach, achieved
  100% ODF certification with zero abandonments. Extracted as **S597**.
- **R8D6F4AD1EAA6** — Aluko OO, Oloruntoba EO, Ana GREE, Afolabi OT, Okon
  AJ (2023). "The dynamics of household water security and treatment
  practices: a population-based, cross-sectional study in Osun State,
  Southwest Nigeria." *Environmental Monitoring and Assessment* 195:138.
  doi 10.1007/s10661-022-10682-9. **INCLUDE.** Cross-sectional study
  (548 households) directly testing an EU/African-Development-Bank-
  funded WASH institutional and governance reform program as an exposure
  against household water security via binary logistic regression; the
  study concludes the reform program did not significantly influence
  water security, while wealth and improved household toilet facilities
  were significant predictors (OR=1.667, 95% CI 1.058-2.628, p=0.028).
  Extracted as **S598**.
- **RADF284366C3F** — Hamdan OHC, Libânio M, Costa VAF (2023). "Proposal
  of a regulatory index of quality of water supply services—RIQS."
  *Environmental Science and Pollution Research* 30:93564-93581. doi
  10.1007/s11356-023-28880-4. **EXCLUDE (E06, engineering only).** A
  methodological/engineering paper proposing and validating an AHP-
  weighted regulatory index for triaging on-site inspections across 591
  Minas Gerais, Brazil municipalities. The unit of analysis is the
  municipality/utility, not a household or population; the outcome is
  an engineering/operational index score used for inspection
  prioritization, not a population-level legal-institutional-factor
  vs. access-outcome test.

`extraction_database.csv`/`evidence_map.csv` updated (S593-S598, 590 →
596 rows each). `effect_sizes.csv` updated (29 → 30 rows, S593 added,
Family C). `exclusion_log.csv` updated (603 rows total; E06 45 → 46).
`full_text_retrieval_queue.csv` regenerated (2,460 open records).
Duplicate audit (DOI + record_id) and `validate_schemas.py` both clean.
Running totals: 1,199/3,659 screened (596 include/603 exclude), 2,460
open, 596 extracted studies, 30 effect_sizes rows.

## 2026-09-22 — Ninetieth full-text screening batch (1 Drive-retrieved PDF: 1 exclude)

One PDF surfaced in the Google Drive retrieval inbox. Open with no prior
`wrong_file_retrieved` history, title/authors matched:

- **R2F0303FF9A77** — Willis MD, Buonocore JJ (2023). "Fossil Fuel
  Racism: The Ongoing Burden of Oil and Gas Development in the Shadows of
  Regulatory Inaction." *American Journal of Public Health*
  113(11):1176-1178. **EXCLUDE (E01, wrong topic).** A short editorial
  commenting on two other studies' findings about oil and gas extraction
  siting near persistently marginalized/redlined communities in Los
  Angeles County, and reviewing the regulatory timeline (setback-distance
  rules, fracking moratoria/bans) for oil and gas development in
  California and New York. "Community water supply contamination" is
  mentioned once in passing as a health-hazard pathway addressed by a
  different cited study, not examined empirically here — the paper's
  subject is oil/gas extraction environmental-justice regulation, not
  water/sanitation service access.

`exclusion_log.csv` updated (602 rows total). `full_text_retrieval_queue.csv`
regenerated (2,467 open records). Duplicate audit (DOI + record_id) and
`validate_schemas.py` both clean (no extraction/evidence_map/effect_sizes
changes this batch — pure exclude). Running totals: 1,192/3,659 screened
(590 include/602 exclude), 2,467 open, 590 extracted studies, 29
effect_sizes rows (unchanged).

## 2026-09-22 — Eighty-ninth full-text screening batch (5 Drive-retrieved PDFs, all Antigravity-delivered: 2 excludes, 3 new includes S590-S592)

Five PDFs surfaced in the Google Drive retrieval inbox in one check, all
pre-matched with `record_id` in the filename and all genuine matches (no
`wrong_file_retrieved` issues this time — every delivered PDF's content
was cross-checked against the target title/authors before screening, per
the lesson from the previous batch):

- **R4F2E31188545** — Mundonde J, Makoni PL (2024). "Framework Model for
  Financing Sustainable Water and Sanitation Infrastructure in Zimbabwe."
  *Water* 16(12):1691. **EXCLUDE (E04, wrong outcome).** National-level
  Tobit econometric analysis (1996-2021 annual time series, 25
  observations) of macroeconomic, financial-market, and governance
  determinants of the aggregate USD investment value of water/sanitation
  PPP transactions reaching financial closure; the outcome is aggregate
  investment financing value, not any household/community-level access,
  connection, coverage, affordability, or reliability outcome.
- **R052039CCB61E** — Brown JC (1989). "Public Reform for Private Gain?
  The Case of Investments in Sanitary Infrastructure: Germany,
  1880-1887." *Urban Studies* 26:2-12. **INCLUDE.** Historical
  quasi-experimental logit analysis of 244 Prussian cities exploiting
  cross-province variation in municipal franchise/voting-rights law (the
  tax-weighted "Three Class System" vs. more equal franchise in
  Hannover/Holstein) to estimate its association with the probability a
  city invested in waterworks infrastructure — instrumented cost, full
  covariate adjustment, counterfactual province-swap simulations
  (likelihood-ratio test statistic -30.0, 3 df). One of the strongest
  causal-identification designs for a legal-institutional exposure in the
  corpus. Extracted as **S590**; also added to `effect_sizes.csv`
  (Family C) — the second quantitative addition to that table this
  session (28 → 29 rows).
- **RDA48A50740DB** — Tomalty R, Skaburskis A (1997). "Negotiating
  Development Charges in Ontario: Average Cost versus Marginal Cost
  Pricing of Services." *Urban Studies* 34(12):1987-2002. **EXCLUDE
  (E01, wrong topic/unit of analysis).** Qualitative case study (27
  interviews plus OMB case-law analysis) of municipal development-charge
  calculation methodology across 8 Greater Toronto Area municipalities;
  water/sewer is mentioned only generically as one of many bundled "hard
  services" (alongside roads, parks, libraries, fire/police, land,
  buildings, even furniture) with no water-specific data or access
  outcome reported anywhere in the paper.
- **R2B84D3F84A28** — Wu W (1999). "Reforming China's Institutional
  Environment for Urban Infrastructure Provision." *Urban Studies*
  36(13):2263-2282. **INCLUDE.** Institutional/fiscal-reform case study
  (national statistics plus a Shanghai case study) documenting a
  socialist-era legal-institutional household-access mechanism
  (state-employer-provided housing automatically conferring
  water/electricity/sewerage access, persisting for over half of urban
  employment through the mid-1990s) alongside fiscal-decentralization and
  infrastructure-connection-fee reforms, with tap-water coverage tracked
  as an explicit outcome variable (81.0% → 94.9% nationally 1990-1996;
  100% in Shanghai both years). Extracted as **S591**.
- **R639910BFA05F** — Marvin S, Laurie N (1999). "An Emerging Logic of
  Urban Water Management, Cochabamba, Bolivia." *Urban Studies*
  36(2):341-357. **INCLUDE.** Qualitative case study (interviews with
  SEMAPA, municipal, FIS, central-government, and consumer-association
  stakeholders) documenting SEMAPA's legal restructuring and
  privatization-driven governance changes, a privatization bid structure
  tying utility ownership to a specific connection-rate target (90%
  within 5 years), a World-Bank-funded community co-management/training
  program (FIS) extending formal connections to squatter communities, and
  household connection-rate disparities by neighborhood income (99% in
  affluent Casco Viejo vs. under 4% inside-house connection in some
  suburban districts). Extracted as **S592**.

`evidence_map.csv` updated for S590-S592. `exclusion_log.csv` updated
(601 rows total). `full_text_retrieval_queue.csv` regenerated (2,468
open records). Duplicate audit (DOI + record_id) and
`validate_schemas.py` both clean. Running totals: 1,191/3,659 screened
(590 include/601 exclude), 2,468 open, 590 extracted studies, 29
effect_sizes rows.

## 2026-09-22 — Eighty-eighth full-text screening batch (3 Drive-retrieved PDFs: 2 wrong-file deliveries flagged, 1 new include S589)

Three PDFs surfaced in the Google Drive retrieval inbox, the first delivery
from an Antigravity retrieval session working from an exported copy of the
open-records queue (see `COWORK_RETRIEVAL_INSTRUCTIONS.md`-style handoff).
All three target record_ids were open with no prior `wrong_file_retrieved`
history, but this batch is a reminder of why the "verify delivered
PDF title/content matches the target record" pipeline step exists as a
separate check from "confirm the record_id is open": **two of the three
titles matched closely enough on the surface that a title-only check would
have passed them through, but the actual delivered content was a different
paper entirely** — caught only by cross-checking the delivered PDF's
author names against the `authors` field already on file in
`full_text_screening_database.csv`.

- **RF7F8D43984CE** — target is Leopold, Ellen & McDonald, David A (2012),
  "Municipal Socialism Then and Now: some lessons for the Global South,"
  *Third World Quarterly*, doi 10.1080/01436597.2012.728321. The PDF
  delivered was a different paper sharing only the phrase "municipal
  socialism" in its title/theme: Jamie Peck (2009), "Creative moments:
  working culture, through municipal socialism and neoliberal urbanism"
  (book chapter contrasting 1980s GLC cultural-industries policy with
  2000s Detroit "creative cities" branding) — confirmed via full-text
  search that neither "Leopold" nor "McDonald" appears anywhere in the
  delivered PDF, and the whole ~1,600-line document never once mentions
  water or sanitation. **Not screened.** `full_text_status` set to
  `wrong_file_retrieved`; record remains open pending correct retrieval.
- **R60D4F5EF6DE5** — target is Sharma, Virinder; Orindi, Victor; Hesse,
  Ced; Pattison, James; Anderson, Simon (2014), "Supporting local climate
  adaptation planning and implementation through local governance and
  decentralised finance provision," *Community Development Journal*, doi
  10.1080/09614524.2014.907240. The PDF delivered was a 1-page UK-Aid-
  funded field "Resilience Assessment Summary" for Kinna ward, Isiolo
  County, Kenya (May 2012) — grey-literature program documentation
  related to the same Kenya County Climate Adaptation Fund initiative,
  but not the target journal article itself; none of the five target
  authors' names appear in the delivered PDF. **Not screened.**
  `full_text_status` set to `wrong_file_retrieved`; record remains open.
- **R98669D9A19CA** — World Bank/Inter-American Development Bank (2004),
  *Ecuador: Creating Fiscal Space for Poverty Reduction — A Fiscal
  Management and Public Expenditure Review*, Volume I, Report No.
  28911-EC. This one is a genuine match (the delivered "Vol. 1 of 2" PDF
  corresponds exactly to the two-volume structure the document itself
  describes). **INCLUDE.** Water/sanitation is a minor sub-topic within
  this much larger multi-sector national fiscal report (electricity,
  telecom, education, health, pensions, oil are all also covered), but
  within its ~3-page water subsection the report presents an original
  World-Bank-staff quantile-based subsidy-incidence estimate specific to
  water (poorest quintile captures 7.9% of water subsidies vs. 41.3% to
  the richest) and a household-level case illustration (Box 3.2, Machala,
  El Oro): connected households pay ~US$1.20/month for ~15 m3 (0.4% of
  monthly income) versus unconnected households, served by tankers,
  paying ~US$29.00/month for only 4-5 m3 (9.0% of monthly income) — a
  roughly 22-24x higher effective per-unit cost for the unconnected poor.
  Tied to decentralized, under-resourced municipal water governance
  (MIDUVI transfers for municipal investment cut from US$52M to US$5M,
  2001-2002; no integrated national water-resource-management system).
  Extracted as **S589** (observational). Also added to
  `effect_sizes.csv` (Family A, economic_access) as a descriptive,
  unadjusted case comparison — the first change to that table all
  session (27 → 28 rows); not eligible for pooling (no sample size, CI,
  or significance test reported in the source, and it is an illustrative
  city-level case rather than a study-level regression/RCT estimate).

`evidence_map.csv` updated for S589. `exclusion_log.csv` unchanged (no
excludes this batch). `full_text_retrieval_queue.csv` regenerated (2,473
open records — the two wrong-file-flagged records remain open pending
correct retrieval, not counted as decided). Duplicate audit (DOI +
record_id) and `validate_schemas.py` both clean. Running totals:
1,186/3,659 screened (587 include/599 exclude), 2,473 open, 587
extracted studies, 28 effect_sizes rows.

## 2026-09-22 — Eighty-seventh full-text screening batch (14 Drive-retrieved PDFs: 1 duplicate deferred, 8 excludes, 5 new includes S584-S588)

Fourteen PDFs surfaced in the Google Drive retrieval inbox in one check (6
pre-matched with record_id in the filename, 8 labeled `UNMATCHED__` and
title-matched by content against the full-text screening database). One
(**R897B0E5CB3C7**, Li/McManus/Cronk Liberia water-point-functionality
paper) is a duplicate of an already-`include`-decided record (matching
study S388 from an earlier session) — moved to the Processed folder without
re-screening, per the standing duplicate-defer rule. The remaining 13 open
with no prior `wrong_file_retrieved` history:

- **R7562AB7A89D4** — Lieberherr E, Ingold K. "Public, Private, or
  Inter-Municipal Organizations: Actors' Preferences in the Swiss Water
  Sector." **EXCLUDE (E04, wrong outcome).** Stated-preference/
  choice-experiment survey of water-sector professionals' organizational-
  form preferences; the measured outcome is expressed preference, not an
  access/connection/affordability/reliability outcome.
- **R88B242AA77A8** — Germann V, Langergraber G. "Going Beyond Global
  Indicators — Policy Relevant Indicators for SDG 6 Targets in the Context
  of Austria." **EXCLUDE (E05, no empirical evidence).** Desk-based
  indicator-selection/expert-consultation paper; no original data
  collection on household/community access.
- **RCE880579857E** — Løvbrand E/Gloppen S (Kenya/Slovenia right-to-water
  constitutionalization). **EXCLUDE (E01, wrong topic/unit of analysis).**
  Macro comparative-politics process-tracing study of constitutional
  right-to-water adoption; no household-level enforcement outcome.
- **RF0D065E4A163** — Côrtes L, Gianella C, Páez AM, Vallejo Piedrahíta C
  (2021). "Comparing Experiences of Constitutional Reforms to Enshrine the
  Right to Water in Brazil, Colombia, and Peru: Opportunities and
  Limitations." *Water* 13(24):3519. doi 10.3390/w13243519. **INCLUDE.**
  Comparative constitutional-law/case-law documentary study documenting
  Colombia's Constitutional Court tutela jurisprudence enforcing household
  reconnection for low-income petitioners unable to pay who show imminent
  risk to health/life, and Peru's amparo action/2017 constitutional
  amendment — directly analogous to the previously-included S517 Morgan
  "Turning off the tap" household reconnection/disconnection precedent.
  Extracted as **S584** (qualitative).
- **R8C306200E800** — Wingfield et al. "Challenges to Water Management in
  Ecuador: Legal Authorization, Quality Parameters, and Socio-Political
  Responses." **EXCLUDE (E05, no empirical evidence).** Desk-based legal/
  policy literature review; Methods section confirms no original data
  collection.
- **R5977B1A524C5** — de Castro MAS et al. "An Experiment in
  Transdisciplinary Systems Mapping: Architecture and the Water-Energy-
  Sanitation Nexus in Brazil." **EXCLUDE (E01, wrong topic/unit of
  analysis).** Methodological systems-mapping-framework paper; matches the
  established Porse et al. 2022 methodological-paper precedent.
- **RC89A2B1CEA16** — Granados-Muñoz LE (2022). "El acueducto II de
  Querétaro: obras de trasvase y escenarios de desigualdad social."
  *Letras Verdes* 32:129-146. doi 10.17141/letrasverdes.32.2022.5273.
  **INCLUDE.** Spanish-language ethnographic case study documenting the
  Querétaro state government's broken public-private-partnership-financed
  restitution promises (hydraulic network, bridge, sanitary drainage) made
  to the Maconí agrarian community after aqueduct-tunnel blasting destroyed
  five natural springs; primary interview testimony confirms water was
  never delivered. Extracted as **S585** (qualitative).
- **RA84EFD886B54** — Silva-Novoa Sanchez LM, Kemerink-Seyoum JS,
  Zwarteveen M (2019). "Water Infrastructure Always In-the-Making:
  Distributing Water and Authority through the Water Supply Network in
  Moamba, Mozambique." *Water* 11(9):1926. doi 10.3390/w11091926.
  **INCLUDE.** Ethnographic case study of a self-installed household pipe
  extension (Block Q11) that the water utility tacitly tolerated as
  "unauthorized" while providing technical connection assistance; the
  neighborhood chief's 50 MT per-household contribution fee created a new
  exclusionary entitlement rule barring non-paying households.
  Extracted as **S586** (qualitative).
- **R684F94E229C3** — Alba R, Bruns A, Bartels LE, Kooy M (2019). "Water
  Brokers: Exploring Urban Water Governance through the Practices of
  Tanker Water Supply in Accra." *Water* 11(9):1919. doi
  10.3390/w11091919. **INCLUDE.** Ethnographic study (12 days participant
  observation, 15 policy-maker interviews) documenting Ghana's water law's
  exclusive legal recognition of GWCL as urban water provider (leaving
  tanker/vendor supply unregulated) and the land-tenure barrier excluding
  Old Fadama informal-settlement residents from legal piped connections.
  Extracted as **S587** (qualitative).
- **R2E8B036BE02F** — Richmond A, Myers I, Namuli H (2018). "Urban
  Informality and Vulnerability: A Case Study in Kampala, Uganda." *Urban
  Science* 2(1):22. doi 10.3390/urbansci2010022. **INCLUDE.** Mixed-methods
  study (ACTogether community survey data across 57 informal settlements
  plus interviews) documenting how Kampala's overlapping land-tenure
  system and stand-pipe connection-fee requirements determine household
  eligibility for legal piped-water access. Extracted as **S588** (mixed
  methods).
- **R0E0F6D8C3330** — Machado AVM, dos Santos JAN, Quindeler NdS, Alves LMC
  (2019). "Critical Factors for the Success of Rural Water Supply Services
  in Brazil." *Water* 11(10):2180. **EXCLUDE (E04, wrong outcome).**
  Nominal Group Technique survey of 88 mostly national/state-level
  professionals (only n=7 from local communities) ranking 30 literature-
  derived success factors; measured outcome is expert-perceived importance,
  not an empirical access outcome.
- **R3D4E9479ACD7** — Dhoba L (2022). "Strengthening water, sanitation and
  hygiene governance: a critical review of Zimbabwe's WASH sector
  institutional arrangements." *H2Open Journal* 5(2):248. **EXCLUDE (E01,
  wrong topic/unit of analysis).** Institutional-coordination-mechanism
  study (questionnaire survey of 43 sector organizations plus FGDs/KIIs)
  assessing the functioning/legitimacy of Zimbabwe's National Action
  Committee WASH coordination structure; no household-level access
  outcome — matches the established SusWASH institutional-coordination
  precedent.
- **R7220865B32E6** — Poudel M et al. (2024). "Effectiveness of climate
  resilient water safety plans in Nepal." *AQUA — Water Infrastructure,
  Ecosystems and Society* 73(7):1437. **EXCLUDE (E06, engineering only).**
  Technical climate-resilience assessment of 10 piped water supply schemes
  using the HTIW engineering/infrastructure-resilience scoring framework
  (Likert-scale domain scores); measures scheme-level technical resilience,
  not a legal-institutional household access outcome.

`evidence_map.csv` updated for S584-S588. `exclusion_log.csv` updated (599
rows total). `full_text_retrieval_queue.csv` regenerated (2,474 open
records). Duplicate audit (DOI + record_id) and `validate_schemas.py`
both clean. Running totals: 1,185/3,659 screened (586 include/599
exclude), 2,474 open, 586 extracted studies, 27 effect_sizes rows
(unchanged — none of S584-S588 report a quantitative comparator effect
estimate).

## 2026-09-22 — Eighty-sixth full-text screening batch (2 Drive-retrieved PDFs: 1 exclude, 1 new include S583)

Two further PDFs surfaced in the Google Drive retrieval inbox on the next
recurring 10-minute inbox check. Both open with no prior
`wrong_file_retrieved` history, no duplicates to defer:

- **R546EB2436B96** — Hallström J (2005). "Technology, social space and
  environmental justice in Swedish cities: water distribution to
  suburban Norrköping and Linköping, 1860-90." *Urban History*
  32(3):413-433. doi 10.1017/S0963926805003214. **INCLUDE.** A historical
  case-comparative study using primary archival sources (City
  Council/Waterworks Board/Water Company minutes, contemporary newspaper
  accounts) of whether working-class suburbs received municipal
  piped-water connections. Documents genuine household/property-level
  legal-institutional content: the "planned area"/rural-district
  administrative boundary determining applicability of national
  building, fire, and public-health codes; discretionary municipal
  decisions on extension requests (Norrköping's contested 1886 approval
  vs. Linköping's Ladugårdsbacke request, denied until 1921); the "10
  percent rule" extension-financing criterion; and fee-based connection
  charges. Extracted as **S583** (qualitative). Notably, `read_file_content`
  returned an empty `fileContent` for the companion PDF surfaced the
  same check (R6E292C80B16D) despite it being a valid, non-empty PDF —
  the established `download_file_content` + base64-decode fallback
  recovered the full text.
- **R6E292C80B16D** — Jiménez A, Pérez-Foguet A (2010). "Water Point
  Mapping for the Analysis of Rural Water Supply Plans: Case Study from
  Tanzania." *Journal of Infrastructure Systems*. **EXCLUDE (E06,
  engineering only).** A GIS/water-point-mapping technical analysis of
  5,921 rural water points across 15 Tanzanian districts, evaluating
  coverage-estimation methodology and technology-type functionality
  decay over time against the Rural Water Supply and Sanitation
  Program's design assumptions; no legal-administrative access mechanism
  examined — matches the established infrastructure/technical-methodology
  precedent (e.g., the Delhi hydrological IDW-interpolation study).

`evidence_map.csv` updated for S583. `exclusion_log.csv` updated (591
rows total). `full_text_retrieval_queue.csv` regenerated (2,487 open
records). Duplicate audit (DOI + record_id) and `validate_schemas.py`
both clean. Running totals: 1,172/3,659 screened (581 include/591
exclude), 2,487 open, 581 extracted studies, 27 effect_sizes rows
(unchanged — S583 is qualitative with no quantitative effect estimate).

## 2026-09-22 — Eighty-fifth full-text screening batch (2 Drive-retrieved PDFs: 2 excludes)

Two further PDFs surfaced in the Google Drive retrieval inbox on the next
recurring 10-minute inbox check. Both open with no prior
`wrong_file_retrieved` history, no duplicates to defer:

- **RFE07661F24F1** — Hushie M (2018). "State-civil society partnerships
  for improving safe water and sanitation coverage in the Northern
  region of Ghana: An exploratory qualitative study." *Cogent Social
  Sciences* 4(1):1508626. doi 10.1080/23311886.2018.1508626. **EXCLUDE
  (E01, wrong topic).** A qualitative study (24 interviews, 16 CSO-
  District Assembly collaborations) of state-civil-society partnership
  dynamics for W&S service delivery; the studied outcome is partnership
  drivers/nature/successes/challenges at the institutional level, not a
  household-level legal-administrative access mechanism — matches the
  established governance-process/partnership-dynamics precedent.
- **R46ADCD34A830** — Soublière J-F, Cloutier C (2015). "Explaining
  Levels of Local Government Involvement in Service Delivery: The
  Dynamics of Cross-Sector Partnerships in Malawi." *Public
  Administration and Development* 35:192-205. doi 10.1002/pad.1715.
  **EXCLUDE (E01, wrong topic).** A qualitative ethnographic study of
  power/control dynamics between Malawian District Councils and
  development partners in rural water supply; the studied outcome is the
  level of local-government involvement in service delivery, an
  institutional governance-process outcome, not household-level water
  access — same rationale as the Hushie exclusion.

`exclusion_log.csv` updated (590 rows total). `full_text_retrieval_queue.csv`
regenerated (2,489 open records). Duplicate audit (DOI + record_id) and
`validate_schemas.py` both clean. Running totals: 1,170/3,659 screened
(580 include/590 exclude), 2,489 open, 580 extracted studies, 27
effect_sizes rows (unchanged).

## 2026-09-22 — Eighty-fourth full-text screening batch (1 Drive-retrieved PDF: 1 new include S582)

One further PDF surfaced in the Google Drive retrieval inbox on the
immediately following inbox check (a recurring 10-minute inbox check was
scheduled per researcher request). Open with no prior
`wrong_file_retrieved` history, no duplicate to defer:

- **RE48029A5D3C0** — Jambadu L, Pilo' F, Monstadt J (2024). "Co-producing
  maintenance and repair: hybrid labor relations in water supply in
  Accra, Ghana." *Urban Research & Practice* 17(2):280-302. doi
  10.1080/17535069.2023.2180325. **INCLUDE.** A qualitative comparative
  case study (48 semi-structured interviews plus field observations,
  2018-2020) across Nima (informal settlement) and Dodowa (peri-urban),
  Accra. Documents genuine household-level legal-institutional content:
  GWCL's PURC/WRC-regulated maintenance mandate; the legality/illegality
  distinction for private and illegal water connections and informal
  self-repair (residents hiring private plumbers to repair public-network
  leaks, GWCL employees moonlighting as private plumbers); household
  maintenance obligations under national water-sector policy; and Ghana's
  decentralized CWSA/Water and Sanitation Management Team framework for
  peri-urban community water-system maintenance. Extracted as **S582**
  (qualitative).

`evidence_map.csv` updated for S582. `full_text_retrieval_queue.csv`
regenerated (2,491 open records). Duplicate audit (DOI + record_id) and
`validate_schemas.py` both clean. Running totals: 1,168/3,659 screened
(580 include/588 exclude), 2,491 open, 580 extracted studies, 27
effect_sizes rows (unchanged — S582 is qualitative with no quantitative
effect estimate).

## 2026-09-22 — Eighty-third full-text screening batch (9 Drive-retrieved PDFs: 7 excludes, 2 new includes S580-S581)

Nine further PDFs surfaced in the Google Drive retrieval inbox on the
immediately following inbox check. All nine were open with no prior
`wrong_file_retrieved` history and no duplicates to defer:

- **R7D3F1DFC2F82** — Craps M, Dewulf A, Mancero M, Santos E, Bouwen R
  (2004). "Constructing Common Ground and Re-Creating Differences Between
  Professional and Indigenous Communities in the Andes." *Journal of
  Community & Applied Social Psychology* 14(5):378-393. doi
  10.1002/casp.796. **INCLUDE.** A qualitative case study of a negotiation
  process between indigenous highland communities and development
  professionals in the Chambo river subbasin, Ecuador. Documents genuine
  legal-institutional content: indigenous communities' legal land titles,
  a judicial workshop process, and formation of a new interinstitutional
  legal consortium governing subbasin water/resource issues. Extracted as
  **S580** (qualitative).
- **R1F5F1AA03B4D** — Hess DJ, Wold CA, Hunter E, Nay J, Worland S,
  Gilligan J, Hornberger GM (2016). "Drought, Risk, and Institutional
  Politics in the American Southwest." *Sociological Forum* 31(S1):807-827.
  doi 10.1111/socf.12274. **INCLUDE.** A mixed-methods study of 22 American
  Southwest metropolitan statistical areas combining qualitative
  institutional-logics conflict coding of water-supply-policy disputes
  (development, preservation, environmental, consumer logics — e.g.
  Choctaw/Chickasaw Nations litigation over Sardis Lake, San Antonio's
  Vista Ridge ratepayer opposition, Tucson pricing/mandate conflicts) with
  a quantitative decision-tree/random-forest model identifying a city's
  Partisan Voting Index as the dominant predictor of municipal
  water-conservation-policy adoption (VWCIb index, 117 metrics).
  Extracted as **S581** (mixed methods). Not added to `effect_sizes.csv`:
  the decision-tree/random-forest variable-importance analysis (%
  increase in prediction error) is not a coefficient-plus-standard-error
  effect estimate comparable to the studies already in that file.
- **RF7AFEEC69292** — Suleiman L (2011). "Civil society: a revived mantra
  in the development discourse." *Water Policy* 13(1):87-101. doi
  10.2166/wp.2010.087. **EXCLUDE (E01, wrong topic).** A governance-
  process/participation discourse study at a macro/institutional unit of
  analysis, not household-level water/sanitation access — matches the
  established governance-process/participation precedent.
- **RCBAA22BF401E** — Murdocca C (2010). "'There Is Something in That
  Water': Race, Nationalism, and Legal Violence." *Law & Social Inquiry*
  35(2):369-402. doi 10.1111/j.1747-4469.2010.01189.x. **EXCLUDE (E05, no
  empirical evidence).** A documentary/case-study sociolegal analysis of
  the Kashechewan water crisis using secondary sources and case law, with
  no original empirical data collection by the author.
- **RADD32264AC64** — Jaffee D, Newman S (2013). "A More Perfect
  Commodity: Bottled Water, Global Accumulation, and Local Contestation."
  *Rural Sociology* 78(1):1-28. doi 10.1111/j.1549-0831.2012.00095.x.
  **EXCLUDE (E01, wrong topic).** A political-economy study of bottled-
  water commodification and corporate resource-extraction contestation,
  not a household-level legal-administrative water/sanitation access
  study.
- **R7863774753EC** — Abu TZ, Elliott SJ, Karanja D (2021). "'When you
  preach water and you drink wine': WASH in healthcare facilities in
  Kenya." *Journal of Water, Sanitation and Hygiene for Development*
  11(4):558-569. doi 10.2166/washdev.2021.238. **EXCLUDE (E01, wrong
  topic).** An institutional healthcare-facility WASH study — institutional
  (non-household) unit of analysis, matching the established
  institutional-WASH exclusion precedent.
- **RE41EC0C4C23A** — Krishna A, Eliatamby DM, Fry MW, et al. (2024).
  "Workplace menstrual health in the private sector: Results from a pilot
  study in Kenya and Nepal." *Journal of Water, Sanitation and Hygiene for
  Development* 14(7):473-485. doi 10.2166/washdev.2024.026. **EXCLUDE
  (E01, wrong topic).** A workplace-based menstrual-health intervention
  pilot study, not household water/sanitation access.
- **R720E1DE4E7C8** — Rehman N (2022). "Epidemic Infrastructures and the
  Politics of Responsibility in Lahore." *Antipode* 54(5):1451-1475. doi
  10.1111/anti.12826. **EXCLUDE (E01, wrong topic).** A dengue
  epidemiology/public-health surveillance study using Lahore's fractured
  water infrastructure as disease-transmission context; the primary
  reported outcome is epidemiological (mosquito breeding/disease risk),
  not a water access/connection/affordability outcome.
- **R49DDEAB1849F** — Yusuf TS, Murray A, Okereke C (2022). "Working with
  local governments to increase access to WASH services: a case of
  WaterAid's participatory approaches in Nigeria." *H2Open Journal*
  5(3):424-437. doi 10.2166/h2oj.2022.061. **EXCLUDE (E01, wrong topic).**
  A WaterAid Nigeria LGA-INGO partnership/participatory-development case
  study — a governance-process/participation study at institutional (LGA)
  level, not household-unit legal-administrative water access.

`evidence_map.csv` updated for S580-S581. `exclusion_log.csv` updated for
the 7 new excludes (588 rows). `full_text_retrieval_queue.csv`
regenerated (2,492 open records). Duplicate audit (DOI + record_id) and
`validate_schemas.py` both clean. Running totals: 1,167/3,659 screened
(579 include/588 exclude), 2,492 open, 579 extracted studies, 27
effect_sizes rows (unchanged — S580 is qualitative with no quantitative
effect estimate; S581's decision-tree/random-forest political-predictor
analysis does not yield a coefficient-plus-standard-error effect
estimate comparable to the studies already in `effect_sizes.csv`).

## 2026-09-22 — Eighty-second full-text screening batch (6 Drive-retrieved PDFs: 2 excludes, 4 new includes S576-S579)

Six further PDFs surfaced in the Google Drive retrieval inbox on the
immediately following inbox check. All six were open with no prior
`wrong_file_retrieved` history and no duplicates to defer:

- **R70028D9094A5** — Mallory A, Omoga L, Kiogora D, Riungu J, Kagendi D,
  Parker A (2021). "Understanding the role of informal pit emptiers in
  sanitation in Nairobi through case studies in Mukuru and Kibera
  settlements." *Journal of Water, Sanitation and Hygiene for
  Development* 11(1):51-59. doi 10.2166/washdev.2020.193. **INCLUDE.** A
  qualitative study (53 semi-structured interviews with pit emptiers,
  residents, entrepreneurs, and officials). Documents genuine
  household/informal-worker-level legal-institutional content: Kenya's
  Water Act 2016 devolving sanitation to counties; the absence of
  licencing or legal recognition for informal pit emptiers; NEMA-backed
  enforcement threats; cartel violence; and Sanergy's private
  transfer-station formalisation model. Extracted as **S576**
  (qualitative).
- **R6EE7062C2464** — de Menezes Fraga CI, de Maria Albuquerque Alves C
  (2025). "Subsidies and affordability: a social approach to water supply
  tariffs." *Journal of Water, Sanitation and Hygiene for Development*
  15(1):75-83. doi 10.2166/washdev.2024.253. **INCLUDE.** A quantitative
  study (tariff/consumption microdata across 35 Federal District, Brazil
  service areas, plus a binary logistic regression) identifying
  demographic predictors of water-poverty risk (female household head
  OR=2.78; brown race OR=2.84; children OR=1.49) against Brazil's 2020 New
  Legal Framework for Basic Sanitation (Law 14,026/2020). Extracted as
  **S577** (quantitative).
- **R5BAA92844EB0** — Maiello A, de Paiva Britto ALN, Quintslr S (2021).
  "The spotted zebra: Cohabitation between informal solutions and
  public-owned infrastructures for water supply in the Rio de Janeiro
  Metropolitan Region." *Water Policy* 23(1):187-204. doi
  10.2166/wp.2020.115. **INCLUDE.** A mixed-methods case study (90-
  respondent survey + 9 semi-structured interviews) in Queimados, Rio de
  Janeiro Metropolitan Region. Documents genuine legal-institutional
  content: CEDAE's 30-year water-supply concession contract; clientelist-
  politics dynamics shaping infrastructure siting; and complete
  institutional non-recognition of grassroots natural-spring sources.
  Extracted as **S578** (mixed methods).
- **R0A9549D920CD** — Fallon Grasham C, Neville G (2021). "Socio-political
  processes must be emphasised alongside climate change and urbanisation
  as key drivers of urban water insecurity." *Water Policy* 23(1):36-57.
  doi 10.2166/wp.2020.333. **INCLUDE.** A mixed-methods comparative case
  study (household surveys n=95/96; interviews n=90+90+19) across three
  Ethiopian cities. Documents genuine household-level legal-institutional
  content: Ethiopia's WASH Implementation Framework/One WASH National
  Programme; a nationally illegal informal water-vending sector; a formal
  Addis Ababa rationing policy; and the 2013 National Guideline for Urban
  Water Utilities Tariff Setting, with quantified financial-burden ratios
  (informal water up to 20x, bottled water up to 76x the formal tariff).
  Extracted as **S579** (mixed methods).
- **R4BFAEC61E31D** — Armah MK, Rodrigues MAV (2026). "The determinants of
  performance in water service delivery: an analysis of municipalities in
  Ghana." *Water Practice & Technology* 21(2):467-486. doi
  10.2166/wpt.2026.189. **EXCLUDE (E04, wrong outcome).** A data
  envelopment analysis (DEA) of 23 Ghanaian water utilities measuring
  technical/scale efficiency and revenue/OPEX slack from utility-level
  financial data — matches the established utility/company-performance
  outcome precedent (Gidion et al. and related DEA studies).
- **R90EB686B9582** — Porse E, Kerner M, Shinneman J, Kaplan J, Stone S,
  Cadenasso ML (2022). "Stormwater utility fees and household
  affordability of urban water services." *Water Policy* 24(6):998-1013.
  doi 10.2166/wp.2022.024. **EXCLUDE (E01, wrong topic).** A GIS/parcel-
  level methodological/simulation paper presenting a generalizable
  approach to estimate stormwater-fee affordability impacts, not an
  empirical examination of a legal-administrative access mechanism —
  matches the established methodological-contribution sub-precedent.

`evidence_map.csv` updated for S576-S579. `exclusion_log.csv` updated for
the 2 new excludes (581 rows). `full_text_retrieval_queue.csv`
regenerated (2,501 open records). Duplicate audit (DOI + record_id) and
`validate_schemas.py` both clean. Running totals: 1,158/3,659 screened
(577 include/581 exclude), 2,501 open, 577 extracted studies, 27
effect_sizes rows (unchanged — none of the new includes has a genuine
exposure-vs-comparator quantitative contrast; S577's logistic-regression
odds ratios are demographic predictors of water-poverty risk, not a
legal-institutional exposure-vs-comparator effect).

## 2026-09-22 — Eighty-first full-text screening batch (15 Drive-retrieved PDFs: 10 excludes, 5 new includes S571-S575)

Fifteen further PDFs surfaced in the Google Drive retrieval inbox (3
already-decided duplicates from the same inbox check — RD864629E91F7,
R0482B6E724C6, R2C5270DE77D8 — were moved to Processed without
re-screening per the duplicate-detection/defer rule). One record
(R22849E39FE23) carried prior `wrong_file_retrieved` history; its
title/content was re-verified against the target record before screening
and confirmed to match this time:

- **R17BBF0A9B354** — "Strengthening rural water security through
  professional maintenance: lessons from Mvila Division, Cameroon."
  **INCLUDE.** A mixed-methods study (647 water-point WSSI quantitative
  assessments, 103 semi-structured committee interviews). Documents
  genuine legal-institutional content: Cameroon's General Code of
  Decentralized Territorial Collectivities (Law No. 2019/024 of 24
  December 2019); institutional/governance/economic analysis of
  water-point committee failures; and a proposed intermunicipal syndicate
  legal structure. Extracted as **S571** (mixed methods).
- **R0A361F399C81** — Foggitt E, Cawood S, Evans B, Acheampong P (2019).
  "Experiences of shared sanitation — towards a better understanding of
  access, exclusion and 'toilet mobility' in low-income urban areas."
  *Journal of Water, Sanitation and Hygiene for Development* 9(3):581-590.
  doi 10.2166/washdev.2019.025. **INCLUDE.** A mixed-methods study (152
  house-unit toilet mapping with GPS, natural group discussions, 2 focus
  groups; 2,743-person study population) in Fante New Town, Kumasi,
  Ghana. Documents genuine household-level legal-institutional content: a
  landlord-permission exclusion mechanism (49% non-permittance, 84%
  attributed to landlord-exclusive toilet use); the legal abolition of
  bucket latrines; and proposed legal/social-economic instruments
  requiring landlords to provide adequate tenant sanitation. Extracted as
  **S572** (mixed methods).
- **R25C5F4851EB7** — Shields KF et al. (2021). "Community management does
  not equate to participation: fostering community participation in
  rural water supplies." *Journal of Water, Sanitation and Hygiene for
  Development* 11(6):937-947. doi 10.2166/washdev.2021.089. **INCLUDE.**
  A qualitative study (243 interviews + 39 focus group discussions across
  18 communities in Ghana, Kenya, and Zambia). Documents genuine
  institutional-governance content: water-committee tariff-setting
  decision-making; community participation typology
  (transactional/transitional/transformational); and
  transparency/accountability rights framed under Rio Declaration
  Principle 10. Extracted as **S573** (qualitative).
- **R22849E39FE23** — Chimphero LM, Tembo M, Gadama R (2026). "Community
  engagement and capacity building as determinants of rural water supply
  functionality: a case of traditional authority Mankhambira in Nkhata
  Bay District, Malawi." *Journal of Water, Sanitation and Hygiene for
  Development* 16(1):22-35. doi 10.2166/washdev.2025.149. **INCLUDE.** A
  mixed-methods study (299 respondents across 30 water points, 8 FGDs, 12
  KIIs). Title/content re-verified against prior `wrong_file_retrieved`
  history and confirmed matching on this delivery. Documents genuine
  household/village-level legal-institutional content: Water Point
  Committee governance; traditional-authority by-law enforcement; and
  informal contribution-based exclusionary access rules with explicit
  recommendations to codify inter-village access rights. Extracted as
  **S574** (mixed methods).
- **R44ED9C065C16** — Bazaanah P, Buthelezi SJ, Oppong DAK (2024).
  "Qualitative study of drinking water, sanitation, and hygiene access:
  perspectives from the Central Gonja District, Ghana, and Mtubatuba
  Municipality, South Africa." *Journal of Water, Sanitation and Hygiene
  for Development* 14(11):1043-1065. doi 10.2166/washdev.2024.021.
  **INCLUDE.** A qualitative study (98 participants: interviews and
  FGDs). Documents genuine household-level legal-institutional content:
  South Africa's Water Services Act, Free Basic Water policy, and
  Municipal Systems Act; Ghana's CWSA Act and Local Government Act; and
  testimony on corruption/favouritism in water distribution plus a
  public-private-partnership water-treatment model. Extracted as **S575**
  (qualitative).
- **R7BC30D37A001** — "Water quality status and challenges in India and
  Nepal" (book chapter). **EXCLUDE (E05, no original empirical
  evidence).** A pure literature-review/synthesis chapter relying
  exclusively on secondary sources; no original data collection.
- **R2DDCC2FC03E7** — "Water policy reform in the Nigeria water governance
  system: assessment" (OECD governance principles/toxicological-index
  study). **EXCLUDE (E01, wrong topic).** A macro/basin-level analysis
  with no household/applicant-level legal-administrative access
  examination — matches the Nkiaka/Laitinen precedent.
- **RF16C02EE1F2F** — "Water inequality and the constitutional right to
  water: evaluating the [Free Basic Water policy]" (South Africa).
  **EXCLUDE (E05, no original empirical evidence).** Explicitly
  self-described "doctrinal legal research methodology"; Ethics Statement
  confirms no human participants, reliance exclusively on secondary/
  documentary sources.
- **RC28E7E20373D** — "Use of group maturity index to measure growth,
  performance, and sustainability" (Zimbabwe community health clubs).
  **EXCLUDE (E01, wrong topic).** A hygiene-promotion program
  organizational-monitoring-tool validation study; does not examine any
  water/sanitation legal-administrative access mechanism.
- **R178AF8716D6A** — "Urban Water System of the National Capital
  Territory (NCT) of Delhi" (hydrological/engineering study). **EXCLUDE
  (E06, engineering only).** IDW spatial interpolation on secondary DJB/
  CGWB/CPCB datasets; no household-level empirical data collection.
- **RDC76C62702D0** — Pierce G, Lai L (2019). "Toward a comprehensive
  explanatory model of reliance on alternatives to the tap: evidence
  from California's retail water stores." *Journal of Water and Health*
  17(3). doi 10.2166/wh.2019.289. **EXCLUDE (E01, wrong topic).** A
  zero-inflated negative binomial regression modeling retail water store
  locations across California census tracts as a proxy for tap-water-
  alternative reliance; examines market-substitution behavior, not any
  legal-administrative access mechanism.
- **RD5DE21EB6425** — Hlongwa N, Nkomo SL, Desai SA. "Barriers to water,
  sanitation, and hygiene in Sub-Saharan Africa: a mini review."
  **EXCLUDE (E05, no original empirical evidence).** An explicit
  PRISMA-style systematic literature review of 76 secondary sources; no
  original data collection.
- **R7E702A70F8C6** — Kimbugwe C et al. (2022). "Practical system
  approaches to realise the human rights to water and sanitation: results
  and lessons from Uganda and Cambodia." *H2Open Journal* 5(1):69-83.
  **EXCLUDE (E01, wrong topic).** A WaterAid programmatic process-review
  paper (Likert-scale stakeholder perception surveys of institutional
  "building blocks"); not an empirical examination of household-level
  legal-administrative water access.
- **R3B73F903D49F** — Chatterley C et al. (2018). "Institutional WASH in
  the SDGs: data gaps and opportunities for national monitoring."
  *Journal of Water, Sanitation and Hygiene for Development* 8(4):
  595-606. **EXCLUDE (E01, wrong topic).** A review of national WASH
  monitoring-data systems (EMIS/HMIS) for schools and health care
  facilities — explicitly non-household settings.
- **R345D7E2BCAC6** — Schiel RE, Wilson BM, Langford M, Faulkner CM
  (2023). "Democracy and public goods revisited: Local institutions,
  development, and access to water." *The British Journal of Politics and
  International Relations* 25(2):237-259. **EXCLUDE (E01, wrong
  topic).** A cross-national regression analysis (140 states,
  2000–2015) using aggregate World Bank/V-Dem/REIGN datasets; a macro
  governance-index study with no household/applicant-level
  legal-administrative access examination.

`evidence_map.csv` updated for S571-S575. `exclusion_log.csv` updated for
the 10 new excludes (579 rows). `full_text_retrieval_queue.csv`
regenerated (2,507 open records). Duplicate audit (DOI + record_id) and
`validate_schemas.py` both clean. Running totals: 1,152/3,659 screened
(573 include/579 exclude), 2,507 open, 573 extracted studies, 27
effect_sizes rows (unchanged — none of the new includes has a genuine
exposure-vs-comparator quantitative contrast).

## 2026-09-21 — Eightieth full-text screening batch (10 Drive-retrieved PDFs: 4 excludes, 6 new includes S565-S570)

Ten further PDFs surfaced in the Google Drive retrieval inbox, all
title/content-verified against their target records prior to screening
(no wrong-file deliveries this batch):

- **R3B336474D5A8** — Mbiza H et al. (2026). "Service innovation and
  governance models for decentralised greywater systems in pro-poor
  urban settlements: evidence from Southlea Park, Zimbabwe." *Water
  Policy* 28(3):520-539. doi 10.2166/wp.2026.168. **INCLUDE.** A
  mixed-methods case study (150-household survey, environmental spot
  measurements, policy document review) developing and applying the
  Greywater Service Innovation Ladder (GSIL) governance-maturity
  framework. Documents genuine legal-institutional content: Zimbabwe's
  National Water Policy greywater-governance vacuum; RDC/ward-committee
  gate-decision authority over service-progression thresholds; and the
  Equity Safeguard Ratio affordability-threshold mechanism. Extracted as
  **S565** (MMAT, mixed methods).
- **RA1815DB6A8FD** — Abawari MJ et al. (2026). "Seeing sanitation: using
  photovoice for research and advocacy on WASH challenges in two
  Ethiopian urban primary schools." *Journal of Water, Sanitation and
  Hygiene for Development* 16(5):409-425. doi 10.2166/washdev.2026.250.
  **INCLUDE.** A qualitative participatory photovoice study (10 teachers,
  10 students, 6 facilitated group discussions, 75-participant advocacy
  event). Documents genuine institutional-governance content: weak
  monitoring/supervision and unclear inter-agency responsibility for
  school WASH maintenance; absence of facility-deterioration reporting
  channels; and the advocacy event's role in bridging vertical
  bureaucratic-accountability gaps between school communities and local
  officials. Extracted as **S566** (CASP, qualitative).
- **R19F2163297EB** — Gashaw Y et al. (2025). "Rural community water
  supply schemes: functionality status, sustainability, and associated
  factors in eastern Ethiopia: a mixed-methods study." *Journal of Water,
  Sanitation and Hygiene for Development* 15(8):683-696. doi
  10.2166/washdev.2025.053. **INCLUDE.** A mixed-methods cross-sectional
  study (400-household survey across 120 water points, technician/
  engineer/committee interviews). Documents genuine legal-institutional
  content: WASHCO tariff-setting and fee-collection authority;
  government-dominated technology selection (85.8%) despite nominal
  community ownership (73.3%); and District Water Office/NGO
  institutional-support structures. Extracted as **S567** (MMAT, mixed
  methods).
- **R2A9D36D4B43E** — Azupogo UW, Dassah E, Bisung E (2023). "Promoting
  safe and inclusive water and sanitation services for students with
  physical disabilities in primary schools: a concept mapping study in
  Ghana." *Journal of Water, Sanitation and Hygiene for Development*
  13(6):453-463. doi 10.2166/washdev.2023.029. **INCLUDE.** A
  participatory mixed-methods concept-mapping study (22 stakeholders
  across policy, NGO, water, education, disability-advocacy, and student
  sectors). Documents genuine legal-institutional content: the UN CRPD
  normative baseline; Ghana's Inclusive Education Policy implementation-
  resource gap per stakeholder testimony; and a proposed accountability/
  sanction roadmap for authorities denying disability access to WASH
  facilities. Extracted as **S568** (MMAT, mixed methods).
- **RF35F2E5A319B** — Karim F et al. (2024). "Holistic citywide sanitation
  for an urban area in the Global South: A case study of the Noakhali
  Pourashava of Bangladesh." *Journal of Water, Sanitation and Hygiene
  for Development* 14(7):572-582. doi 10.2166/washdev.2024.169.
  **INCLUDE.** A mixed-methods case study (150-household survey, 7
  key-informant interviews, 4 focus group discussions) applying shit flow
  diagram (SFD), city service delivery assessment (CSDA), and SWOT
  analysis. Documents genuine legal-institutional content: Bangladesh's
  National Strategy for Water Supply and Sanitation's silence on fecal
  sludge management; CSDA-scored institutional/regulatory gaps by
  sanitation domain; and named institutional actors' (WASA, DPHE,
  Pourashava, UNDP) statutory responsibility gaps. Extracted as **S569**
  (MMAT, mixed methods).
- **R78F5B66C5C9F** — Coultas M et al. (2022). "Galvanising and fostering
  sub-national government leadership for area-wide sanitation
  programming." *H2Open Journal* 5(1):1-10. doi 10.2166/h2oj.2022.022.
  **INCLUDE.** A qualitative multi-case study (documentary review, 31
  combined key-informant interviews across Kenya, Rwanda, and Uganda,
  three participatory cross-case analysis workshops). Documents genuine
  legal-institutional content: each country's constitutional/statutory
  decentralisation architecture assigning sanitation mandates to
  sub-national tiers; a governor's signed financial-commitment letter
  binding budget allocation to sanitation; and mandatory livelihood-
  benefit/toilet-use conditionality. Extracted as **S570** (CASP,
  qualitative).
- **R65E0D0F26A0A** — Celume, Donoso et al. "Reform of the Chilean water
  code in 2022: shift from a neoliberal model to a more public interest
  model." **EXCLUDE (E05, no original empirical evidence).** A
  PRISMA-style systematic review of 63 existing secondary legal-critique
  studies plus comparative legal-text analysis of Law No. 21,435 versus
  the 1981 Water Code. No original household-level empirical data
  collection — matches the Viljoen/Burdon doctrinal-commentary precedent,
  extended to systematic reviews of secondary legal literature.
- **R73C7494E55DD** — Gidion. "Ranking water utilities in a competitive
  scenario using two years of information and data envelopment
  analysis." *Water Practice & Technology* 20(2):436-448. **EXCLUDE (E04,
  wrong outcome).** A network-DEA efficiency-benchmarking study of 40
  Tanzanian urban water utilities on inputs (non-revenue water, personnel
  expenditure, staffing) versus outputs (population served, hours of
  service, metered customers). Utility-level performance ranking, not
  household/applicant-level access — matches the established DEA-exclusion
  precedent from R8821B3A63A95, REA26B447CC9E, RC47ECBF4C9AF,
  R23EE2449CF6B.
- **R96593F742647** — Satpathy S, Jha R. "Intermittent water supply in
  Indian cities: considering the intermittency beyond demand and
  supply." *AQUA — Water Infrastructure, Ecosystems and Society*
  71(12):1395-1407. **EXCLUDE (E05, no original empirical evidence).**
  Explicitly self-described by the authors as relying "mostly... on the
  review of literature," using only existing government/utility
  statistics with no original household-level data collection.
- **R3BF9C93DC6A9** — Saadi S, Johns C. "Governing smart water cities for
  urban water resilience: international lessons and a Canadian policy
  framework." *Water Policy* (2026). **EXCLUDE (E05, no original
  empirical evidence).** Explicitly self-described as a "policy-oriented
  scoping review" synthesizing 51 secondary academic and policy sources
  across five international and five Canadian case examples; no original
  empirical data collection.

`evidence_map.csv` updated for S565-S570. `exclusion_log.csv` updated for
the 4 new excludes (569 rows). `full_text_retrieval_queue.csv`
regenerated (2,522 open records). Duplicate audit (DOI + record_id) and
`validate_schemas.py` both clean. Running totals: 1,137/3,659 screened
(568 include/569 exclude), 2,522 open, 568 extracted studies, 27
effect_sizes rows (unchanged — none of the new includes has a genuine
exposure-vs-comparator quantitative contrast).

## 2026-09-21 — Seventy-ninth full-text screening batch (7 Drive-retrieved PDFs: 1 exclude, 4 new includes S561-S564, 2 wrong-file-retrieved left open)

Seven further PDFs surfaced in the Google Drive retrieval inbox:

- **R9FA1C1004C69** — Dwipayanti NMU et al. (2022). "Inclusive WASH and
  sustainable tourism in Labuan Bajo, Indonesia: needs and opportunities."
  *Journal of Water, Sanitation and Hygiene for Development* 12(5):417-431.
  doi 10.2166/washdev.2022.222. **INCLUDE.** A qualitative case study (20
  semi-structured interviews, 6 focus groups, 2020 fieldwork) of Inclusive
  WASH access in a "super-premium" tourism destination. Documents genuine
  legal-institutional content: the municipal utility PDAM's intermittent
  (twice-weekly) supply amid a 10 L/s deficit; Indonesia's Ministry of
  Public Works minimum water-requirement service standard; a tiered
  hotel/household tariff structure with documented preferential-delivery
  effects; and the POKJA AMPL multi-stakeholder governance working group.
  Extracted as **S561** (CASP, qualitative).
- **R07131CF3EAEE** — Akpabio EM, Ozoh SI (2026). "Household access to
  water, sanitation, and hygiene services in Cross River State, Nigeria:
  patterns, challenges, and community participation." *Water Policy*
  28(4):651-674. doi 10.2166/wp.2026.005. **INCLUDE.** A mixed-methods
  cross-sectional study (800-household survey, 751 retrieved/93.9%
  response rate, plus key-informant interviews) across three ecological
  zones. Documents genuine legal-institutional content: Cross River
  State's new 2025 Water Supply and Sanitation Law establishing a
  statutory WaSH-access guarantee; a newly inaugurated WaSH regulatory
  department; the 2025 WaSH Policy's financing/accountability-dashboard
  mechanisms; and institutionalized community task groups. Extracted as
  **S562** (MMAT, mixed methods).
- **RC1E784D9D197** — Nkolola BN, Phiri A (2024). "From fetchers to
  decision-makers: exploring the gender dynamics of water access and
  governance in resource-poor communities of Mbala, Zambia." *Journal of
  Water, Sanitation and Hygiene for Development* 14(12):1291-1304. doi
  10.2166/washdev.2024.214. **INCLUDE.** A mixed-methods study (122
  mWater-tool interviews, Empowerment in WASH Index survey, 2023-2024
  fieldwork) of Water Point Committee (WPC) governance. Documents genuine
  legal-institutional content: WPCs as the community water-governance
  institution with formal membership eligibility criteria and election
  cycles, but lacking enforceable financial-contribution mechanisms;
  EWI-quantified finding that gendered exclusion is not the primary
  sustainability barrier (women scored higher on the index than men),
  contribution-enforcement failure is. Extracted as **S563** (MMAT, mixed
  methods).
- **R8FFC351CC113** — Mandara CG, Butijn C, Niehof A (2013). "Community
  management and sustainability of rural water facilities in Tanzania."
  *Water Policy* 15(S2):79-100. doi 10.2166/wp.2013.014. **INCLUDE.** A
  mixed-methods study (221-household survey, 6 FGDs, official interviews,
  2 detailed village case studies, national-policy document review,
  2011-2012 fieldwork). Documents extensive genuine legal-institutional
  content: Tanzania's 2002 NAWAPO and 2008 NWSDS national water-policy
  frameworks and their failure to define Village Water Committee (VWC)
  roles; the subsidiarity-principle cost-recovery devolution to user fees;
  District Water Department staffing deficits (41-50% below required);
  private-operator tender processes without district legal-unit
  oversight; and VWC gender-parity composition requirements. Extracted as
  **S564** (MMAT, mixed methods).
- **RC1CB10DA729E** — Schiedek L et al. (2021). "Assessing national WaSH
  targets through a water governance lens: a case study of the Sanitation
  and Water for All partnership commitments." *Journal of Water,
  Sanitation and Hygiene for Development* 11(5):805-813. doi
  10.2166/washdev.2021.049. **EXCLUDE (E01, wrong topic).** A deductive
  content analysis of 291 voluntary policy-commitment texts submitted to a
  global partnership's online database, coded against a governance-framework
  taxonomy. No original household/community-level data collection and no
  examination of any specific country's legal-administrative water-access
  mechanisms — the unit of analysis is international-partnership
  commitment-text quality, not a primary empirical study of household-level
  legal-administrative access, the same macro/cross-national rationale
  applied to the earlier Nkiaka, Shadabi & Ward, and Laitinen exclusions.
- **RDA537B7BBB17** and **R22849E39FE23** — both **remain open**, fourth
  and first-time wrong-file deliveries respectively. RDA537B7BBB17's
  target is "Fecal sludge management (FSM): Analytical tools for
  assessing FSM in cities," but the file delivered was Agbo, Jeffrey &
  Sule (2025), a systematic review of urban WSS failings in Sub-Saharan
  Africa (doi 10.2166/washdev.2025.267) — a different paper entirely.
  R22849E39FE23's target is "Community engagement and capacity building
  as determinants of rural water supply functionality... Malawi," but the
  file delivered was Suleiman (2011), "Civil society: a revived mantra in
  the development discourse" (Accra water-utility privatisation
  governance, doi 10.2166/wp.2010.087). Both records' `full_text_status`
  updated to `wrong_file_retrieved` with notes documenting the mismatch;
  both left open pending correct retrieval.

`evidence_map.csv` updated for S561-S564. `exclusion_log.csv` updated for
the 1 new exclude (565 rows, unchanged net since the R81549C4709FC
correction two batches prior). `full_text_retrieval_queue.csv`
regenerated (2,532 open records). Duplicate audit (DOI + record_id) and
`validate_schemas.py` both clean. Running totals: 1,127/3,659 screened
(562 include/565 exclude), 2,532 open, 562 extracted studies, 27
effect_sizes rows (unchanged -- none of the new includes has a genuine
exposure-vs-comparator quantitative contrast).

## 2026-09-21 (latest) — Seventy-eighth full-text screening batch (5 Drive-retrieved PDFs: 2 excludes, 2 new includes S559-S560, 1 wrong-file-retrieved left open)

Five further PDFs surfaced in the Google Drive retrieval inbox after the
seventy-seventh batch below:

- **RBEBE0BACCD18** — Wagaba et al., study of small NGOs' access to
  geological/hydrogeological data for water-point siting and planning
  purposes in eastern Africa. **EXCLUDE (E01, wrong topic).** The unit of
  analysis is a practitioner/NGO organization's access to technical
  scientific data (borehole records, aquifer maps), an entirely different
  exposure and population than this review's target of household- or
  applicant-level legal-administrative access to water services.
- **RE8D979932979** — Blanchon, analysis of South Africa's 1998 National
  Water Act "Reserve" mechanism (statutory environmental-flow allocation),
  with an Orange River case study. **EXCLUDE (E01, wrong topic).** A
  policy/hydrological-geography analysis of environmental-flow and
  river-basin allocation law, drawn from government reports and secondary
  sources with no original empirical data collection on households; the
  exposure examined is a different unit of analysis than household-level
  legal-administrative water access.
- **R81549C4709FC** — target record is "Building Political Capabilities
  through Participation for Environmental Justice in Informal Housing in
  Kathmandu" (Singh S., Singh B. 2024, doi 10.4324/9781003371175-24), but
  this is a **fourth consecutive wrong-file delivery** (`full_text_status`
  was already `wrong_file_retrieved` from three prior attempts, documented
  in this record's `notes`) — the PDF actually delivered was again chs.
  19-20 of the same edited volume (Sherpa; Awale, on Nepal climate-change
  adaptation and Indigenous Environmental Justice), confirmed via full-text
  read. **A first pass this session mistakenly recorded this record as
  EXCLUDE (E01) based on the wrongly-delivered file's content, without
  first checking the record's prior `full_text_status`/`notes` history.**
  This was caught and reverted the same session: `full_text_decision`,
  `final_decision`, `reviewer_1`, `exclusion_reason`, and
  `exclusion_reason_detail` were all cleared back to blank, the erroneous
  row was removed from `exclusion_log.csv`, and `notes` was updated to
  record the fourth wrong-file attempt. The record **remains open**
  pending correct retrieval of the Singh & Singh chapter; the wrongly
  delivered Drive file was still moved to the Processed folder (consistent
  with how the three prior wrong-file deliveries for this record were
  handled) so it does not keep re-surfacing in the inbox.
- **RD1E30397691A** — Boucher-Hedenström J, Rutherford D (2010).
  "Services d'eau et d'assainissement et dispersion « urbaine » dans le
  comté de Stockholm." *Flux* 2010/1-2 (n°79-80):54-68. doi
  10.3917/flux.079.0054. **INCLUDE.** A qualitative case study (interviews
  with named municipal/regional officials, combined with regulatory
  analysis) of water/sanitation service configuration amid urban sprawl in
  Stockholm County, Sweden, with a Norrtälje case study. Documents genuine
  legal-institutional content: Sweden's 2007 Water Services Act municipal
  responsibility and cost-price tariff principle; four service-
  configuration types A-D; ~90,000 households on alternative
  (non-municipal) solutions; municipal permit/connection requirements and
  enforcement authority over substandard individual installations; and a
  mini-network (samfällighet) unanimous-consent connection model.
  Extracted as **S559** (CASP, qualitative).
- **R1197785426F6** — Baron C, Bonnassieux A (2013). "Gouvernance hybride,
  participation et accès à l'eau potable: Le cas des associations
  d'usagers de l'eau (AUE) au Burkina Faso." *Annales de géographie*
  2013/5 (n°693):525-548. doi 10.3917/ag.693.0525. **INCLUDE.** A
  qualitative case study (field studies conducted 2011-2014 under the ANR
  Sud II APPI research project) of hybrid water governance and the
  legal-institutional role of Water Users' Associations (AUE) in rural/
  semi-urban Burkina Faso. Documents genuine legal-institutional content:
  the 2001 Water Law right to water; the 2009 decentralization decree
  transferring infrastructure competence to communes; AUE legal
  homologation/licensing criteria (30-80 members, gender parity, youth
  quotas, elected 6-member bureau); AUE's formal role fixing water
  tariffs, controlling point-of-service operators, and mediating
  conflicts; delegation of AEPS management to private or associative
  operators via affermage contracts; and documented gendered exclusion
  within this formal participatory governance structure. Extracted as
  **S560** (CASP, qualitative).

`evidence_map.csv` updated for S559-S560. `exclusion_log.csv` updated for
the 2 new excludes, net (564 rows: 3 added then 1 removed on correction).
`full_text_retrieval_queue.csv` regenerated (2,537 open records, including
R81549C4709FC restored to open). Duplicate audit (DOI + record_id) and
`validate_schemas.py` both clean. Running totals: 1,122/3,659 screened
(558 include/564 exclude), 2,537 open, 558 extracted studies, 27
effect_sizes rows (unchanged -- neither new include has a genuine
exposure-vs-comparator quantitative contrast).

## 2026-09-21 — Seventy-seventh full-text screening batch (2 Drive-retrieved PDFs: 2 new includes S557-S558)

Two further PDFs surfaced in the Google Drive retrieval inbox after the
seventy-sixth batch below:

- **RE7ECD35103C3** — Kim E (2014). "Conceptual practice of 'rural
  wellbeing' in Uzbekistan: Contradictions and implications for gender
  equality." *Rural Society* 23(3):243-256. doi
  10.1080/10371656.2014.11082068. **INCLUDE.** A qualitative institutional
  ethnographic case study (40 in-depth interviews with women peasant
  farmers plus 65 additional stakeholder interviews, participant
  observation, and ~400-document institutional text analysis, 2011
  fieldwork) of a foreign-funded participatory Water User Association
  (WUA) project in rural Uzbekistan. Documents genuine legal-institutional
  content: the Uzbek government's institutionalization of WUAs to organize
  village-level water management after decollectivization; 1994
  formalization of individual household peasant-farm land rights; private
  farmers' long-term state lease contracts with cotton/wheat quotas and
  fines for shortfall; and "community mobiliser" selection criteria that
  discursively and structurally excluded women -- the majority of
  household farmers -- from the project despite their extensive
  unrecognized water-access labor and self-organized (but never
  institutionally recognized) water-user groups. Extracted as **S557**
  (CASP, qualitative).
- **RC61ECDAD14A5** — Selfa T, Bain C, Moreno R (2014). "Depoliticizing
  land and water 'grabs' in Colombia: the limits of Bonsucro certification
  for enhancing sustainable biofuel practices." *Agriculture and Human
  Values* 31:455-468. doi 10.1007/s10460-014-9509-3. **INCLUDE.** A
  qualitative case study (14 in-depth exploratory interviews with
  sugarcane/ethanol industry stakeholders plus additional interviews with
  an agricultural researcher and displaced rural residents, June-August
  2012) of land and water access under Bonsucro biofuel certification in
  the Valle del Cauca, Colombia. Documents genuine legal-institutional
  content: Colombia's water-concession regulatory regime (Decree 1541/78,
  Agreement 042/2010) administered by the Cauca Valley Corporation,
  described by interviewees as captured by the sugar industry; the sugar
  industry holding 64%/88% of surface/underground water concessions
  versus 26%/2% for household use; industry lobbying to reclassify
  potable groundwater as non-potable to free it for irrigation; and
  Bonsucro's "obey the law" certification standard legitimizing this
  disproportionate access without addressing underlying inequitable
  distribution or historical dispossession. Extracted as **S558** (CASP,
  qualitative).

`evidence_map.csv` updated for S557-S558. `full_text_retrieval_queue.csv`
regenerated (2,541 open records). Duplicate audit (DOI + record_id) and
`validate_schemas.py` both clean. Running totals: 1,118/3,659 screened
(556 include/562 exclude), 2,541 open, 556 extracted studies, 27
effect_sizes rows (unchanged -- neither new include has a genuine
exposure-vs-comparator quantitative contrast).

## 2026-09-21 — Seventy-sixth full-text screening batch (6 Drive-retrieved PDFs: 3 excludes, 3 new includes S554-S556)

Six further PDFs surfaced in the Google Drive retrieval inbox after the
seventy-fifth batch below:

- **RB51DE5CBDEE4** — Cole S, Browne M (2015). "Tourism and Water Inequity
  in Bali: A Social-Ecological Systems Analysis." *Human Ecology*
  43:439-450. doi 10.1007/s10745-015-9739-z. **INCLUDE.** A mixed-methods
  case study (39 interviews, 2 focus groups, 110 tourist surveys, 2010
  fieldwork) of tourism-driven water inequity in Canggu, Bali, using
  Ostrom's SES framework. Documents genuine legal-institutional content:
  11 fragmented, poorly coordinated government departments sharing water
  responsibility; Bali's 1999 regency-level decentralization producing
  inter-Regency competition; the traditional subak irrigation-governance
  system; widespread non-enforcement of building-coverage and
  water-metering/tariff regulations against the tourism industry (which
  consumes 65% of water); and up to 5,000 households in Denpasar on a
  waitlist for a public connection, paying unlicensed private-vendor water
  at prices up to Rp50,000 (~US$5.80)/gallon. Extracted as **S554** (MMAT).
- **RF78C62C99387** — Palta M, du Bray MV, Stotts R, Wolf A, Wutich A
  (2016). "Ecosystem Services and Disservices for a Vulnerable Population:
  Findings from Urban Waterways and Wetlands in an American Desert City."
  *Human Ecology* 44:463-478. doi 10.1007/s10745-016-9843-8. **INCLUDE.**
  A mixed-methods ethnographic study (155 participant-observation site
  visits, 10 informal interviews, 7 semi-structured interviews,
  water-quality monitoring at 5 sites, 2012-2013) of ecosystem services and
  disservices accessed by people experiencing homelessness via informal
  urban waterways along the Salt River in Phoenix, Arizona. Documents
  genuine legal-institutional content: Phoenix's 2004 anti-camping
  ordinances criminalizing public water access; public water
  fountains/bathrooms locked at night; the Phoenix Heat Relief Network's
  insufficient capacity; and the illegality of accessing state/federal
  wetlands, exposing users to Park Ranger enforcement and threatened
  arrest -- an extra-legal informal water-access strategy for a legally
  excluded vulnerable population, alongside a serious documented
  health-risk trade-off (E. coli exceeding EPA drinking standards in
  21-100% of measurements). Extracted as **S555** (MMAT).
- **R3D2D360577A3** — Ghertner DA (2017). "When Is the State? Topology,
  Temporality, and the Navigation of Everyday State Space in Delhi."
  *Annals of the American Association of Geographers* 107(3):731-750. doi
  10.1080/24694452.2016.1261680. **INCLUDE.** A qualitative ethnographic
  case study (24 months of fieldwork, 2006-2014) of everyday negotiation of
  water, electricity, and building-permission access in Delhi's informal
  slum settlements and unauthorized colonies. Documents genuine
  legal-institutional content directly on point for the review's "legal
  last mile" framework: illegal electricity/water reconnection via direct
  personal negotiation with low-level bureaucrats; unauthorized colonies
  (20%+ of Delhi's population) categorically barred from official
  municipal water/sewerage connections despite valid property-transaction
  documentation; Delhi Jal Board officials operating at least 15
  unregistered borewells in direct violation of a 2010 state drilling ban,
  financed via an MLA's discretionary fund rather than official channels;
  and Resident Welfare Associations as state-recognized but formally
  non-state intermediaries controlling informal water-delivery and
  construction-approval access. Extracted as **S556** (CASP, qualitative).
- **RA1EBB350D5D3** — a doctrinal/legal-theoretical analysis of Australian
  water law and Indigenous water rights (Burdon, Drew, Stubbs, Webster &
  Barber, *Settler Colonial Studies* 2015), drawing on historical records,
  case law, and existing scholarship with no original empirical data
  collection. **EXCLUDE (E05, no empirical evidence)**, the same rationale
  applied to the earlier Viljoen doctrinal-commentary exclusion.
- **RBE33CDE5272C** — a discrete-choice-experiment survey-methodology paper
  (Lanz & Provins, *Journal of Regulatory Economics* 2015) examining
  whether "status quo" choices in willingness-to-pay surveys reflect
  genuine consumer preferences for a regulated English water utility's
  investment planning. **EXCLUDE (E01, wrong topic)** -- the paper's actual
  contribution is survey-methodology validity, not a primary empirical
  study of legal-administrative water access.
- **R23EE2449CF6B** — a theoretical incomplete-contracts economic model of
  public-private-partnership water-utility contract design (Nakhla,
  *European Journal of Law and Economics* 2016), illustrated with secondary
  published performance statistics from Senegalese and Burkinabe water
  utilities. **EXCLUDE (E04, wrong outcome)** -- the outcome variables
  (network yield, connection counts, staff productivity) are
  utility/company-level performance metrics, not household-level access,
  the same rationale applied to the prior DEA, PDAM, and Thai FSM
  exclusions.

`evidence_map.csv` updated for S554-S556. `full_text_retrieval_queue.csv`
regenerated (2,543 open records). Duplicate audit (DOI + record_id) and
`validate_schemas.py` both clean. Running totals: 1,116/3,659 screened
(554 include/562 exclude), 2,543 open, 554 extracted studies, 27
effect_sizes rows (unchanged -- none of the three new includes has a
genuine exposure-vs-comparator quantitative contrast).

## 2026-09-21 — Seventy-fifth full-text screening batch (5 Drive-retrieved PDFs: 2 excludes, 3 new includes S551-S553)

Five further PDFs surfaced in the Google Drive retrieval inbox after the
seventy-fourth batch below:

- **R5AB0C14E4E11** — Harris LM, Kooy M, Rusca M, et al. (2017). "Gendered
  lives, gendered waters: the differentiated access, uses, knowledges, and
  governance of water in urban Ghana and South Africa." **INCLUDE.** A
  mixed-methods statistical study (487-household survey across four
  underserved settlements: Ashaiman and Teshie in Accra, Ghana; Khayelitsha
  and Philippi in Cape Town, South Africa) of gender-differentiated water
  access, uses, knowledges, governance, and experiences. Documents genuine
  legal-institutional content: Ghana's GWCL urban piped-supply mandate and
  the AVRL private-consortium management period (2006-2011); South
  Africa's Constitutional right to water and sanitation, the Free Basic
  Water policy (6kl/household/month regardless of household size), and
  apartheid-era racial/class-differentiated water infrastructure still
  shaping access via the ongoing RDP housing-formalization process.
  Extracted as **S551** (JBI Analytical Cross Sectional Studies).
- **R169602E7BE36** — Romano ST (2017). "Democratic Decentralization and
  Community-Based Water Governance: The Case of Nicaragua's Water
  Committees (CAPS)." **INCLUDE.** A qualitative case study (18
  semi-structured interviews with rural water committees plus NGO/
  multilateral/government staff interviews, 12 months of fieldwork
  2007-2010, plus 2014 follow-up) of the "organic empowerment" of
  Nicaragua's community-based water committees. Documents genuine
  legal-institutional content: the Special Law of Potable Water and
  Sanitation Committees (Law 722, 2010) that formally recognized over
  5,000 previously unrecognized CAPS serving more than 1 million rural
  residents; the prior General Water Law (Law 620, 2007) that excluded
  CAPS; CAPS' lack of personeria juridica (legal personality) preventing
  legal receipt of constructed water systems; user-fee collection
  ($0.23-$2.85/household/month) with informally negotiated non-enforcement
  of shutoff rules for seasonal-labor households; and legal-gray-area
  negotiation of land/water-source access with private landowners.
  Extracted as **S552** (CASP Qualitative Studies Checklist).
- **R17B052404210** — Forster T, Downsborough L, Chomba MJ (2017).
  "Improving Accountability and Governance: The Establishment of a Water
  User Association in the Groot Marico Catchment, South Africa."
  **INCLUDE.** A qualitative case study (48 semi-structured and
  focus-group interviews with commercial farmers, emerging farmers, and
  local community members, plus document analysis, fieldwork 2011 and
  2015) of power asymmetries in the establishment of a Water User
  Association (WUA). Documents genuine legal-institutional content: the
  National Water Act 1998's definition and establishment guidelines for
  WUAs as the local collaborative-governance vehicle for redressing
  apartheid-era water-access inequality; the "existing lawful use"
  provision tying commercial-farmer water entitlements to land ownership
  from the 1996-1998 baseline period, continuing to advantage the white
  minority of commercial irrigation farmers despite the NWA's stated
  intent to separate water rights from land ownership; and a documented
  WUA-establishment meeting from which black rural community members and
  emerging farmers were functionally excluded via short notice, an
  inaccessible venue, and English-only proceedings, resulting in
  commercial farmers dominating the vote on WUA leadership and a
  pre-drafted constitution. Extracted as **S553** (CASP Qualitative
  Studies Checklist).
- **R8A34FFD0A52F** — a "Defining Moments" reflective essay (*Health
  Communication* journal's personal-narrative/vignette section) about
  lived experience of water access in southeastern Ohio. **EXCLUDE (E12,
  wrong study design).** Built around unstructured focus-group anecdotes,
  analyzed through communication/narrative theory (liminality, otherness)
  rather than legal-institutional mechanism analysis, with no described
  sample size, sampling method, or systematic coding protocol -- the piece
  does not meet the review's standard for an appraisable empirical study
  design.
- **RC47ECBF4C9AF** — a quantitative study (multiple regression analysis of
  data from 160 Thai municipalities) of technical, financial, social, and
  institutional factors influencing faecal sludge management (FSM) service
  performance. **EXCLUDE (E04, wrong outcome).** The outcome variables
  (operational efficiency, service performance/complaint-rate, and
  treatment feasibility indicators) are municipality-level
  service-performance metrics, not household- or applicant-level access,
  connection, affordability, or reliability outcomes -- the same
  institutional/organizational-performance exclusion rationale applied to
  the prior DEA and PDAM-performance studies (R8821B3A63A95,
  REA26B447CC9E). Also concerns fecal sludge/septic management rather than
  water supply access.

`evidence_map.csv` updated for S551-S553. `full_text_retrieval_queue.csv`
regenerated (2,549 open records). Duplicate audit (DOI + record_id) and
`validate_schemas.py` both clean. Running totals: 1,110/3,659 screened
(551 include/559 exclude), 2,549 open, 551 extracted studies, 27
effect_sizes rows (unchanged -- none of the three new includes has a
genuine exposure-vs-comparator quantitative contrast).

## 2026-09-21 — Seventy-fourth full-text screening batch (2 Drive-retrieved PDFs: 1 exclude, 1 new include S550)

Two further PDFs surfaced in the Google Drive retrieval inbox after the
seventy-third batch below:

- **R9BAE8BE9ADB8** — Nastar M, Abbas S, Aponte Rivero C, Jenkins S, Kooy M
  (2018). "The emancipatory promise of participatory water governance for
  the urban poor: Reflections on the transition management approach in the
  cities of Dodowa, Ghana and Arusha, Tanzania." *African Studies*
  77(4):504-525. doi 10.1080/00020184.2018.1459287. **INCLUDE.** A
  mixed-methods comparative case study (104 household interviews in
  Dodowa, 56 household interviews plus 120 water-point interviews in
  Arusha) of power dynamics in participatory groundwater governance.
  Documents genuine legal-administrative content across two countries:
  Ghana's Community Water and Sanitation Agency Act/WATSAN committee
  structure and GWCL connection process, alongside a roughly 10x informal
  resale-price markup for tank-resold water versus the regulated GWCL
  tariff; Tanzania's Water Resource Management Act assigning the Pangani
  Basin Water Board groundwater-permitting authority, undermined by an
  unfunded monitoring capacity leaving many boreholes unregistered, and
  Arusha City Council land permits issued in designated groundwater
  recharge areas confirmed by a National Environment Management Council
  official to be illegal under the Act; and household-level exclusion from
  community water governance in both cities tied to tenure status
  (renters), kinship ties, and land ownership. Extracted as **S550**
  (MMAT).
- **REA26B447CC9E** — Nohong M (2018). "The moderating effect of efficiency
  and non-market capability in relationship between government involvement
  and resources to performance of water supply companies (PDAM) in
  Sulawesi, Indonesia." *International Journal of Law and Management*
  60(2):402-412. doi 10.1108/IJLMA-11-2016-0117. **EXCLUDE (E04, wrong
  outcome).** An explanatory PLS-SEM survey study (60 PDAM managing
  directors) of company-level "Performance" as a function of government
  involvement, resources, efficiency, and non-market capability -- the
  same technical/organizational-efficiency exclusion rationale applied to
  the prior DEA study (R8821B3A63A95); no household- or applicant-level
  access outcome is examined.

`evidence_map.csv` updated for S550. `full_text_retrieval_queue.csv`
regenerated (2,554 open records). Duplicate audit (DOI + record_id) and
`validate_schemas.py` both clean. Running totals: 1,105/3,659 screened
(548 include/557 exclude), 2,554 open, 548 extracted studies, 27
effect_sizes rows (unchanged -- the new include has no genuine
exposure-vs-comparator quantitative contrast).

## 2026-09-21 — Seventy-third full-text screening batch (4 Drive-retrieved PDFs: 2 excludes, 2 new includes S548-S549)

Four further PDFs surfaced in the Google Drive retrieval inbox after the
seventy-second batch below:

- **RACFFE4F7F72C** — Nyamwanza AM (2018). "Local institutional adaptation
  for sustainable water management under increasing climatic variability and
  change: A case in the mid-Zambezi Valley, Zimbabwe." *International
  Journal of Climate Change Strategies and Management* 10(3):453-471. doi
  10.1108/IJCCSM-03-2017-0078. **INCLUDE.** A qualitative case study (34
  semi-structured interviews, 3 community workshops, key informant
  interviews, documentary review) of local water-related institutional
  adaptation in Mbire District. Documents genuine legal-institutional
  content under Zimbabwe's Water Act 1998, ZINWA Act 1998, Environmental
  Management Act 2002, and Rural District Councils Act 1996: the
  statutorily mandated Catchment/Sub-Catchment Councils and ZINWA are
  functionally absent in this rural district (over 90% of residents had no
  knowledge of them), leaving the RDC, EMA, traditional authorities, and
  community Borehole Water Committees as the institutions actually
  governing access; RDC enforcement of a national streambank-cultivation
  by-law produced sustained conflict with EMA and residents, resolved via a
  locally negotiated accommodation not fully accepted inter-institutionally;
  and borehole access is severely strained, with most wards far exceeding
  the government's recommended 250-persons-per-borehole maximum (up to
  2,000 in the worst-affected ward) after the post-2000 collapse of
  donor-funded drilling/maintenance support. Extracted as **S548** (CASP
  Qualitative Studies Checklist).
- **RCC0D2A422FD2** — Bartels LE, Bruns A, Alba R (2018). "The production of
  uneven access to land and water in peri-urban spaces: de facto
  privatisation in greater Accra." *Local Environment* 23(12):1172-1189.
  doi 10.1080/13549839.2018.1533932. **INCLUDE.** A mixed-methods case
  study (62 semi-structured household interviews, transect walks, photo
  diaries, expert/stakeholder interviews) of de facto privatisation and
  uneven access to land and water in peri-urban Greater Accra. Documents
  genuine legal-administrative access mechanisms under Ghana's Water
  Resources Commission Act 1996 and Water Use Regulations 2001: unlicensed,
  unregistered de facto private control of groundwater by landowners
  despite the legal permit requirement; private water-vendor pricing 3-20x
  the official GWCL rate, stratified by income between bulk-tanker and
  neighbourhood-vendor purchase; customary allodial-title land tenure
  exploited via an unresolved 20-year chieftaincy dispute enabling multiple
  sale of the same plots; formal land-title registration under the Title
  Registration Act 1986 functionally inaccessible to most residents; and an
  extra-legal "digging fee"/asafo-money payment required before
  construction can begin. Extracted as **S549** (MMAT).
- **R8AD13170998A** — Post AE, Agnihotri A, Hyun C (2018). "Using
  Crowd-Sourced Data to Study Public Services: Lessons from Urban India."
  *Studies in Comparative International Development* 53:324-342. doi
  10.1007/s12116-018-9271-4. **EXCLUDE (E01, wrong topic).** A methods
  paper on using crowd-sourced data in political science research (the
  authors' NextDrop water-intermittency project in Bangalore is one
  illustration among several suggested applications -- protest politics,
  corruption, public opinion, law and order). The paper's actual
  contribution is methodological (groundtruthing, selection-bias
  correction, cluster-randomization causal inference, research
  partnerships), not a primary empirical study of legal-administrative
  water-access mechanisms.
- **RFAED90B6DD97** — Silva Rodríguez de San Miguel JA (2018). "Gender and
  water management in Mexico." *Management of Environmental Quality*
  29(5):842-858. doi 10.1108/MEQ-10-2017-0112. **EXCLUDE (E05, no empirical
  evidence).** Explicitly self-labeled "Paper type: General review" -- a
  narrative literature survey (JSTOR/EBSCOhost database search, hand-coded
  themes) with no original empirical data collection of its own; the author
  states future research will add the case studies and fieldwork
  observations this review lacks.

`evidence_map.csv` updated for S548-S549. `full_text_retrieval_queue.csv`
regenerated (2,556 open records). Duplicate audit (DOI + record_id) and
`validate_schemas.py` both clean. Running totals: 1,103/3,659 screened
(547 include/556 exclude), 2,556 open, 547 extracted studies, 27
effect_sizes rows (unchanged -- neither new include has a genuine
exposure-vs-comparator quantitative contrast).

## 2026-09-21 — Seventy-second full-text screening batch (3 Drive-retrieved PDFs: 1 exclude, 2 new includes S546-S547)

Three further PDFs surfaced in the Google Drive retrieval inbox after the
seventy-first batch below:

- **RC6B24320D282** — Morena Y et al. (2019). "The analysis of health
  aspects in housing type 45, Panorama Indah residence, Pekanbaru." *MATEC
  Web of Conferences* 276:06032. doi 10.1051/matecconf/201927606032.
  **EXCLUDE (E06, engineering only).** A single-house (N=1) building-code
  compliance survey assessed against the Indonesian Directorate General of
  Human Settlements 1986 housing-health standard, with water supply one of
  six inspected physical criteria (lighting, ventilation, water supply,
  wastewater disposal, humidity, air pollution). A single-dwelling
  engineering/health-code inspection, not a legal-administrative
  water-access mechanism study.
- **R55F012C376B7** — Singh S, Shrestha K, Hamal M, Prakash A (2020).
  "Perform or wither: role of water users' associations in municipalities
  of Nepal." *Water Policy* 22(S1):90-106. doi 10.2166/wp.2019.051.
  **INCLUDE.** A mixed-methods study (350-household survey across Damauli
  and Tansen municipalities, plus focus group discussions) of Water
  Users' Associations (WUAs) under Nepal's Water Resource Act 1992,
  Water Resource Regulation 1993, and Drinking Water Regulation 1998.
  Documents concrete household-level access/burden mechanisms: new tap
  connections costing NPR 50,000 (~USD 440) with waits up to 11 years,
  a two-tier informal-payment mechanism (NPR 100,000 for faster
  connection), WUA-committee/private-repair-agency collusion and
  political capture, gendered exclusion (taps registered only to male
  household heads despite women bearing 6-7 hrs/day of water-collection
  burden), tanker-water costs (~Rs 357/1,000L), and inequitable WUA
  spring-water pricing (NPR 20 to 80 per 6,000L). Extracted as **S546**
  (MMAT).
- **REB0B1F68FC00** — Sarrazin C, Gautier E, Hollé A, Grancher D, de
  Bélizal E, Hadmoko DS (2019). "Resilience of socio-ecological systems
  in volcano risk-prone areas, but how much longer? Assessment of
  adaptive water governance in Merapi volcano, Central Java, Indonesia."
  *GeoJournal* 84:183-213. doi 10.1007/s10708-018-9856-5. **INCLUDE.** A
  mixed-methods case study (73 stakeholder interviews, including 42
  household-level, across 7 villages/dusun; 1-month 2013 fieldwork) of
  adaptive water governance on Merapi's southern slopes. Documents
  genuine Indonesian legal-institutional content: the 1987 irrigation
  reforms and 1998/1999 decentralization framework's "Turnover Program"
  transferring irrigation governance from customary Ulu-Ulu
  rights-holders to formal Water Users Associations (WUA) and WUA
  Federations; institutional pluralism across the Ministry of Public
  Works, Ministry of Agriculture & Environment, regional water agencies,
  the Irrigation Committee, and residual informal Ulu-Ulu authority,
  producing an undelivered 2013 government subvention payment owed to
  WUAs; and post-2010-eruption lahar damage to sabo-dams/irrigation
  canals causing drinking- and irrigation-water crises, met by unequal
  government emergency water-tank distribution and informal Gotong
  Royong mutual-aid canal repair. Extracted as **S547** (MMAT).

`evidence_map.csv` updated for S546-S547. `full_text_retrieval_queue.csv`
regenerated (2,560 open records). Duplicate audit (DOI + record_id) and
`validate_schemas.py` both clean. Running totals: 1,099/3,659 screened
(545 include/554 exclude), 2,560 open, 545 extracted studies, 27
effect_sizes rows (unchanged -- neither new include has a genuine
exposure-vs-comparator quantitative contrast).

## 2026-09-21 — Seventy-first full-text screening batch (1 Drive-retrieved PDF, new include S545)

One further PDF surfaced in the Google Drive retrieval inbox after the
seventieth batch below:

- **RC85926098F35** — Dobbin KB (2020). "'Good Luck Fixing the
  Problem': Small Low-Income Community Participation in Collaborative
  Groundwater Governance and Implications for Drinking Water Source
  Protection." *Society & Natural Resources* 33(12):1468-1485. doi
  10.1080/08941920.2020.1772925. **INCLUDE.** A qualitative case study
  (27 semi-structured interviews with 35 individuals across 23 small
  low-income communities in California's San Joaquin Valley) documenting
  a genuine legal-administrative participation regime under California's
  Sustainable Groundwater Management Act (SGMA, 2014). SGMA statutorily
  lists Disadvantaged Communities and domestic well owners among 11
  mandatory beneficial-user categories that local Groundwater
  Sustainability Agencies (GSAs) must involve, but leaves the specific
  form of representation to GSA discretion; in this study, privately
  owned water systems and domestic-well communities never achieved
  formal voting representation, while formal voting seats typically
  required a financial contribution (one community saved $8,000 by
  choosing non-voting status). Interviewees with advisory/stakeholder
  positions repeatedly described having "voice but not vote";
  transparency failures were common (non-Brown-Act-compliant meetings,
  one community first notified about SGMA three years after it took
  effect); and drinking-water/water-quality considerations were reported
  as largely absent from resulting Groundwater Sustainability Plans, with
  25% of interviewees explicitly expecting SGMA's net effect on their
  community to be negative. Extracted as **S545** (CASP Qualitative
  Studies Checklist).

`evidence_map.csv` updated for S545. `full_text_retrieval_queue.csv`
regenerated (2,563 open records). Duplicate audit (DOI + record_id) and
`validate_schemas.py` both clean. Running totals: 1,096/3,659 screened
(543 include/553 exclude), 2,563 open, 543 extracted studies, 27
effect_sizes rows (unchanged -- qualitative case study with no
exposure-vs-comparator quantitative contrast).

## 2026-09-21 — Seventieth full-text screening batch (1 Drive-retrieved PDF, new include S544)

One further PDF surfaced in the Google Drive retrieval inbox after the
sixty-ninth batch below:

- **R05E6A40917AB** — Turley B, Caretta MA (2020). "Household Water
  Security: An Analysis of Water Affect in the Context of Hydraulic
  Fracturing in West Virginia, Appalachia." *Water* 12(1):147. doi
  10.3390/w12010147. **INCLUDE.** A qualitative case study (30
  semi-structured in-depth interviews with mineral owners, surface
  owners, and concerned citizens across 8 northwestern West Virginia
  counties) documenting a genuine legal-administrative regime governing
  household groundwater security around hydraulic fracturing. WV code
  22-6A-18's "presumed liability" statute (2013 Natural Gas Horizontal
  Well Control Act) conditions legal protection for well-water
  contamination on a 1500-foot distance and 6-month time threshold from
  drilling, both set by government/industry compromise rather than
  public-health science; the mandated baseline and post-drill water
  testing is conducted by contractors hired by the oil and gas companies
  themselves (not an independent regulator), producing delayed and
  contested results -- one resident learned via a FOIA request, after
  drinking the water unknowingly for six months, that a test had already
  found E. coli contamination; oil and gas wastewater is exempt from the
  federal Safe Drinking Water Act ("the Halliburton Loophole"); and a
  Natural Resources Defense Council report found the WV Department of
  Environmental Protection failed to enforce Underground Injection
  Control requirements (wastewater injected under expired permits, over
  half of wells abandoned unplugged). Non-disclosure agreements
  accompanying company buyouts/remediation suppress residents' ability
  to discuss confirmed contamination, and loss of usable water can
  render a home unsellable. Extracted as **S544** (CASP Qualitative
  Studies Checklist).

`evidence_map.csv` updated for S544. `full_text_retrieval_queue.csv`
regenerated (2,564 open records). Duplicate audit (DOI + record_id) and
`validate_schemas.py` both clean. Running totals: 1,095/3,659 screened
(542 include/553 exclude), 2,564 open, 542 extracted studies, 27
effect_sizes rows (unchanged -- qualitative case study with no
exposure-vs-comparator quantitative contrast).

## 2026-09-21 — Sixty-ninth full-text screening batch (2 Drive-retrieved PDFs, both new includes S542-S543)

Two further PDFs surfaced in the Google Drive retrieval inbox after the
sixty-eighth batch below:

- **RB432D9F6004C** — Singh S, Hassan SMT, Hassan M, Bharti N (2020).
  "Urbanisation and water insecurity in the Hindu Kush Himalaya: Insights
  from Bangladesh, India, Nepal and Pakistan." *Water Policy*
  22(S1):9-32. doi 10.2166/wp.2019.215. **INCLUDE.** A companion paper
  to S541 in the same special issue, covering Bangladesh, India, Nepal
  and Pakistan with its own quantitative supply/demand data table
  (Table 9, 13 cities: e.g. Kathmandu Valley KUKL service area faces a
  178 MLD deficit, Quetta 64 MLD, Rawalpindi 59 MLD) and distinct
  legal-administrative content: despite clear departmental mandates,
  the forest department in Darjeeling could not extend its mandate to
  artificial recharge outside protected areas, blocking spring
  rejuvenation; a water-augmentation project (lifting water from the
  Balasun river) stalled and its cost escalated from INR 400 million to
  INR 560 million due to irreconcilable design/implementation
  disagreements between the municipality, hill council and World Bank;
  and private-tanker pricing that varies by distance documented as
  restricting the water quantity purchased by poorer households.
  Extracted as **S542** using the Legal Institutional Evidence
  Appraisal Framework (not a systematic review -- no described search
  protocol).
- **R0312B751BEAE** — Twum KO, Abubakari M (2020). "Drops in the city:
  the puzzle of water privatization and consumption deficiencies in
  urban Ghana." *Water Policy* 22(3):417-434. doi
  10.2166/wp.2020.175. **INCLUDE.** A mixed-methods study (26
  semi-structured interviews across Accra, Kumasi, Sekondi-Takoradi and
  Tamale, plus secondary data and GIS spatial mapping) documenting a
  genuine legal-administrative access mechanism: the informal nature of
  living arrangements in low-income neighborhoods prevents residents
  from acquiring the legal documentation required for household pipe
  connections, categorically barring them from formal Ghana Water
  Company Ltd (GWCL) service and forcing reliance on private/informal
  vendors at markedly higher prices ($0.10/bucket from private wells,
  $0.18/gallon from tankers, $10-20 for untreated hand-dug-well water in
  poor neighborhoods) in a weak/unregulated private-vendor market. GWCL
  itself supplies only 41% of the urban population, with only 30% of
  urban Ghanaians having piped-water access. Extracted as **S543**
  (MMAT, mixed methods).

`evidence_map.csv` updated for S542 and S543. `full_text_retrieval_queue.csv`
regenerated (2,565 open records). Duplicate audit (DOI + record_id) and
`validate_schemas.py` both clean. Running totals: 1,094/3,659 screened
(541 include/553 exclude), 2,565 open, 541 extracted studies, 27
effect_sizes rows (unchanged -- no defined exposure-vs-comparator
contrast with a locatable effect estimate in either narrative
synthesis).

## 2026-09-21 — Sixty-eighth full-text screening batch (1 Drive-retrieved PDF, new include S541)

One further PDF surfaced in the Google Drive retrieval inbox after the
sixty-seventh batch below:

- **R08C74B34D928** — Singh V, Pandey A (2020). "Urban water resilience
  in Hindu Kush Himalaya: issues, challenges and way forward." *Water
  Policy* 22(S1):33-45. doi 10.2166/wp.2019.329. **INCLUDE.** A
  narrative policy synthesis (not a systematic review -- no described
  search protocol) across 8 named cities in the Hindu Kush Himalaya
  region (Kabul, Quetta, Shimla, Mussoorie, Nainital, Kathmandu, Xining,
  Thimphu) spanning Afghanistan, Pakistan, India, Nepal, China and
  Bhutan, combining a quantitative supply/demand data table (Table 1)
  with field observations from the HI-AWARE research consortium.
  Documents genuine legal-administrative access mechanisms: groundwater
  abstraction bye-laws exist in multiple towns (Quetta, Kabul, Dehradun,
  Haldwani) but are "seldom followed," attributed partly to the
  political clout of informal water-tanker operators ("tanker mafia");
  absence of water metering and differential pricing across most towns;
  institutional fragmentation across multiple water-supply
  departments/agencies operating in silos; and inequitable "zero day"
  water cutoffs disproportionately affecting socio-economically weaker
  areas even where aggregate scarcity is not severe, with unaffordable
  tanker-water pricing (Kabul residents pay $0.36/unit) as the de facto
  supply mechanism where formal municipal supply is deficient (Kabul
  supplies only ~20% of its population; Kathmandu Valley faces a ~70%
  shortfall). Extracted as **S541** using the project's own Legal
  Institutional Evidence Appraisal Framework.

`evidence_map.csv` updated for S541. `full_text_retrieval_queue.csv`
regenerated (2,567 open records). Duplicate audit (DOI + record_id) and
`validate_schemas.py` both clean. Running totals: 1,092/3,659 screened
(539 include/553 exclude), 2,567 open, 539 extracted studies, 27
effect_sizes rows (unchanged -- no defined exposure-vs-comparator
contrast in a narrative multi-city synthesis).

## 2026-09-21 — Sixty-seventh full-text screening batch (1 Drive-retrieved PDF, exclude)

One further PDF surfaced in the Google Drive retrieval inbox after the
sixty-sixth batch below:

- **R8821B3A63A95** — Nithammer CM, Mahabir J, Dikgang J (2022).
  "Efficiency of South African water utilities: a double bootstrap DEA
  analysis." *Applied Economics* 54(26):3055-3073. doi
  10.1080/00036846.2021.2002802. **EXCLUDE E04.** A rigorous
  double-bootstrap data envelopment analysis (DEA) benchmarking the
  technical/operational efficiency of 144 South African Water Services
  Authorities (77-utility panel, 2010-2014), with institutional
  determinants tested in a second-stage truncated regression (WSA
  status, water-board use, outsourcing to a private provider, political
  competition/majority-vote-share, urban vs. rural location, municipal
  election-cycle effects). However, the outcome variable throughout is a
  DEA efficiency/inefficiency score -- utility-level input-output
  productivity (inputs: operating cost, length of mains; outputs:
  authorized consumption, water quality) -- not a household/applicant
  access, connection, affordability, or service-reliability outcome as
  defined by this review's scope. No household- or applicant-level
  legal-administrative access mechanism is examined.

`full_text_retrieval_queue.csv` regenerated (2,568 open records).
Duplicate audit (DOI + record_id) and `validate_schemas.py` both clean.
Running totals: 1,091/3,659 screened (538 include/553 exclude), 2,568
open, 538 extracted studies (unchanged -- exclude only), 27
effect_sizes rows (unchanged).

## 2026-09-21 — Sixty-sixth full-text screening batch (4 Drive-retrieved PDFs, 1 new include S540 + 3 excludes)

Four further PDFs surfaced in the Google Drive retrieval inbox after the
sixty-fifth batch below:

- **R9FFEBB4E1EFA** — Silva-Novoa Sanchez LM, Bossenbroek L, Schilling J,
  Berger C (2022). "Governance and Sustainability Challenges in the
  Water Policy of Morocco 1995-2020." *Water* 14(18):2932. doi
  10.3390/w14182932. **INCLUDE.** Content analysis of Moroccan water
  policy (Law 10-95 and its 2016 successor, Law 36-15) combined with 37
  semi-structured interviews with farmers, local officials, and water
  administrators in the Middle Draa Valley (MDV), Zagora province, south
  Morocco. Documents genuine legal-administrative access mechanisms:
  well-digging permits reportedly requiring informal payments/bribery to
  obtain; a circular institutional bind where drip-irrigation subsidies
  require an existing well (officials do not check for a digging permit)
  while some tribes require farmers to first work the land -- which
  requires water/a well -- before granting the land-use certificate that
  a digging permit itself requires; institutional fragmentation across
  the Ministries of Agriculture (subsidies), Water/River Basin Agency
  (well-digging permits), and Interior/caidat (tribal land
  certification); unequal Kharouba/1-8/1-4 water-rights share allocation
  among farmers inside oases; and unconnected/intermittent rural
  drinking-water households. Extracted as **S540** (CASP Qualitative
  Studies Checklist).
- **R397656949E83** — Viljoen S (Water Wheel / South African water-law
  journal). A doctrinal commentary on South African water-law property
  paradigms. **EXCLUDE E05.** Pure doctrinal/theoretical discussion of
  property-law frameworks with no empirical access-outcome evidence —
  distinguished from doctrinal includes (e.g. S538 Dallasheh, S533
  Ghertner) which document a concrete, operating legal-administrative
  access mechanism rather than abstract legal theory.
- **R98A0DCEA5699** — Mamokhere J et al. A paper on municipal service
  partnerships/PPP governance. **EXCLUDE E07.** Self-described
  non-empirical conceptual paper synthesizing secondary literature, no
  primary data collection; generic multi-service municipal governance
  topic, not water-specific.
- **R1BF978DC83F1** — Shadabi L, Ward FA. "Predictors of safe drinking
  water access." **EXCLUDE E01.** A rigorous macro cross-national
  econometric study of national-level governance-quality composite
  indices (GDP, Gini, corruption-avoidance index, government-
  effectiveness index, civil-liberties index) as predictors of
  aggregate national safe-drinking-water access rates — the wrong unit
  of analysis for this review's household/applicant-level
  legal-administrative access scope, the same rationale applied to the
  earlier Nkiaka exclusion (sixty-fourth batch above).

`evidence_map.csv` updated for S540. `full_text_retrieval_queue.csv`
regenerated (2,569 open records). Duplicate audit (DOI + record_id) and
`validate_schemas.py` both clean. Running totals: 1,090/3,659 screened
(538 include/552 exclude), 2,569 open, 538 extracted studies, 27
effect_sizes rows (unchanged this batch — none of the 4 records met the
strict effect_sizes eligibility bar).

## 2026-09-21 — Sixty-fifth full-text screening batch (2 Drive-retrieved PDFs, 1 already-decided duplicate + 1 new include S539)

Two further PDFs surfaced in the Google Drive retrieval inbox after the
sixty-fourth batch below:

- **R844EAC3AEE12** — a correctly-relabeled re-upload of the Dewi,
  Kusumoarto & Rejoni (2026) slum-participation study already excluded
  E01 in the sixty-first batch (2026-09-21 earlier). Per the project's
  standing duplicate-defer rule, an already-decided record_id is never
  re-litigated on a fresh upload; the existing exclude decision stands
  unchanged, and the file was moved straight to the Drive `Processed/`
  folder without further screening.
- **RA0FB2C52085F** — Zhang X, Gonzalez Rivas M, Grant M, Warner ME
  (2022). "Water pricing and affordability in the US: public vs.
  private ownership." *Water Policy* 24(3):500-516. doi
  10.2166/wp.2022.283. **INCLUDE.** OLS regression across the 500
  largest US community water systems (321 government-owned, 121
  cooperative, 58 investor-owned). Private ownership is associated with
  a $144.04 higher annual water bill (std. coeff 0.35, p<0.01) and a
  1.55-percentage-point higher share of lowest-quintile household
  income spent on water (std. coeff 0.26, p<0.01), controlling for
  regulation, water supply, infrastructure age, and community
  demographics. Separately, state regulation favorable to private
  providers -- New Jersey and Pennsylvania's "fair value" legislation
  (enabling private acquisition of municipal systems at inflated
  valuations recoverable through rates) and Distribution System
  Improvement Charge (DSIC) surcharges (passing capital costs to
  ratepayers between formal rate cases) -- is associated with a further
  $88.64 higher annual bill (p<0.01). Real legal-administrative
  mechanisms (state Public Utility Commission rate regulation,
  fair-value legislation, DSIC surcharges) with a genuine,
  non-fabricated exposure-vs-comparator contrast and clean effect
  estimates. Extracted as **S539** (JBI Critical Appraisal Checklist
  for Analytical Cross Sectional Studies) and added to
  `effect_sizes.csv` -- the review's second ownership/regulation
  pricing-effect study, alongside S526 (Switzer & Teodoro 2025).

`evidence_map.csv` updated for S539. `full_text_retrieval_queue.csv`
regenerated (2,573 open records). Duplicate audit (DOI + record_id) and
`validate_schemas.py` both clean. Running totals: 1,086/3,659 screened
(537 include/549 exclude), 2,573 open, 537 extracted studies, 27
effect_sizes rows.

## 2026-09-21 — Sixty-fourth full-text screening batch (2 Drive-retrieved PDFs, both excludes E01)

Two further PDFs surfaced in the Google Drive retrieval inbox after the
sixty-third batch below — both genuinely new, still-open screening
records, both excluded:

- **RD864629E91F7** — Nkiaka E (2022). "Exploring the socioeconomic
  determinants of water security in developing regions." *Water Policy*
  24(4):608-625. doi 10.2166/wp.2022.149. **EXCLUDE E01.** A macro
  cross-national econometric study across 117 countries (Africa,
  Asia-Pacific, Latin America and the Caribbean) developing a composite
  Water Security Index (biophysical + socioeconomic sub-indices) and
  regressing it against GDP per capita, the Government Effectiveness
  Index (a cross-national governance-quality composite, not a specific
  administrative-law mechanism), ODA-WSS, female primary-school
  completion, and urban population share. No household- or
  applicant-level legal-administrative access mechanism (eligibility,
  documentation, fees, connection procedure, enforcement) is examined;
  wrong unit of analysis (country) and wrong topic (macro development
  econometrics) for this review's scope.
- **R2C5270DE77D8** — Laitinen J, Katko TS, Hukka JJ, Juuti P, Juuti R
  (2022). "Governance and Practices for Achieving Sustainable and
  Resilient Urban Water Services." *Water* 14(13):2009. doi
  10.3390/w14132009. **EXCLUDE E01.** A sequential PESTEL/SWOT
  strategic-planning synthesis of Finnish urban water utility
  governance, infrastructure investment, and institutional framework,
  built from prior literature and expert-workshop notes on a country
  with near-universal water access. No specific access-exclusion
  mechanism at household or applicant level is examined — this is a
  generic utility-governance/sustainability-planning discussion, not
  empirical access-mechanism evidence.

`full_text_retrieval_queue.csv` regenerated (2,574 open records).
Duplicate audit (DOI + record_id) and `validate_schemas.py` both clean.
Running totals: 1,085/3,659 screened (536 include/549 exclude), 2,574
open, 536 extracted studies, 26 effect_sizes rows. E01 exclusion count:
168 -> 170.

## 2026-09-21 — Sixty-third full-text screening batch (1 Drive-retrieved PDF, new include S538)

One further PDF surfaced in the Google Drive retrieval inbox after the
sixty-second batch below — a genuinely new, still-open screening record:

- **R0482B6E724C6** — Dallasheh L (2022). "Would the United States Come
  to Nazareth's Aid? Local and International Contests over the City's
  Water." *Journal of Palestine Studies* 51(4):24-44. doi
  10.1080/0377919X.2022.2131458. **INCLUDE.** A rigorous archival
  historical case study (primary sources: Israeli State Archives,
  Nazareth Municipal Archives, US National Archives, Knesset records,
  contemporary press), not doctrinal commentary — satisfies
  `INCLUSION_EXCLUSION.md` on strong legal-administrative grounds.
  Nazareth's elected municipal council formally held water-infrastructure
  decision authority under the Mandate-era Municipal Corporations
  Ordinance of 1934, but every step (funding, equipment import,
  foreign-currency access) required Israeli military-government
  authorization throughout 1948-1966 martial law. Mekorot, the national
  quasi-official water utility, ultimately secured control of the
  municipality-owned well as a precondition of connecting the city to
  the national grid (1955), and in 1966 cut off Nazareth's entire water
  supply over an unpaid municipal debt, explicitly wielded as political
  leverage to force the resignation of an elected mayor. Extracted as
  **S538** using the Legal Institutional Evidence Appraisal Framework —
  the convention already established for doctrinal/archival
  legal-institutional case studies (S356, S364, S504, S507, S513, S517,
  S518, S533), resolved by hand as `doctrinal` in `evidence_map.csv`.

No genuine single-study statistical contrast meeting `effect_sizes.csv`'s
strict eligibility bar, so not added there (an archival historical
narrative, like the project's other doctrinal/jurimetric studies, is not
eligible for that file). `evidence_map.csv` updated.
`full_text_retrieval_queue.csv` regenerated (2,576 open records).
Duplicate audit (DOI + record_id) and `validate_schemas.py` both clean.
Running totals: 1,083/3,659 screened (536 include/547 exclude), 2,576
open, 536 extracted studies, 26 effect_sizes rows.

## 2026-09-21 — Sixty-second full-text screening batch (2 Drive-retrieved PDFs, both new includes S536-S537)

Two further PDFs surfaced in the Google Drive retrieval inbox after the
sixty-first batch below — both genuinely new, still-open screening
records, not mislabeled duplicates:

- **R0206140E81E4** — Abrams, Carden, Teta & Wagsaether (2021). "Water,
  Sanitation, and Hygiene Vulnerability among Rural Areas and Small
  Towns in South Africa: Exploring the Role of Climate Change,
  Marginalization, and Inequality." *Water* 13(20):2810. doi
  10.3390/w13202810. **INCLUDE.** Qualitative climate-risk-and-
  vulnerability case-study comparison (transdisciplinary CRVA) of WASH
  access in rural HaSinari (Limpopo) and small-town Prince Albert
  (Western Cape), South Africa. Genuine legal-administrative content:
  Prince Albert's "leiwater" irrigation-furrow water allocation, managed
  by the Kweekvallei Irrigation Board, is restricted to residents
  holding allocation rights recorded in historical (Apartheid-era) title
  deeds, structurally excluding North-End (predominantly Colored)
  residents while South-End (historically white-favored) residents
  retain access; in HaSinari the formal municipal water department has
  effectively ceased functioning and been replaced by elected,
  fee-funded community Water Committees that collect monthly household
  contributions to fund diesel for borehole pumps. Extracted as **S536**
  (CASP).
- **REA101C40B5BB** — Alam, Rahat, Nawaz, Neeher, Tabassum, Upoma, Kamal,
  Evans & Hutchings (2025). "Behaviour change interventions to promote
  household connectivity to sewer: a scoping review." *Global Health
  Action* 18(1):2476335. doi 10.1080/16549716.2025.2476335. **INCLUDE.**
  PRISMA-ScR scoping review synthesizing 11 sewer-connection
  behaviour-change-intervention case studies across 8 countries
  (Ecuador, Colombia, Bolivia, Brazil, Kenya, Morocco, India, Pakistan).
  Directly synthesizes legal-administrative mechanisms: mandatory-
  connection legal provisions (Tamil Nadu's regulatory 100-meter
  connection mandate, Sao Paulo's 2002 municipal connection law,
  Salvador's Law 7307/1998), indirect financial subsidies (free
  connections), fees, and penalty/legal-action provisions for
  non-connection or illegal discharge. Finds programmes combining free
  connection with community engagement (Colombia 75%, Morocco 80%,
  Kenya 76%, Bolivia 81%) substantially outperform legal-mandate
  messaging or promotion alone without a financial subsidy (Tamil Nadu
  40%; Sao Paulo 19% despite free connection, attributed to a
  concurrent water crisis). Extracted as **S537**
  (`systematic_review_secondary`, AMSTAR 2).

Both included studies satisfy `INCLUSION_EXCLUSION.md` criteria 1-2
(water/sanitation access examined alongside a legal/administrative/
governance factor) on genuine, non-trivial institutional grounds, not a
generic development-studies framing. Neither contains a fabricated or
genuine single-study exposure-vs-comparator statistical contrast meeting
`effect_sizes.csv`'s strict eligibility bar (S537's pre/post connection-
rate percentages are programme-level scoping-review syntheses without a
defined comparator group, consistent with how other included systematic
reviews, e.g. S319, have been excluded from `effect_sizes.csv`), so
neither was added there. `evidence_map.csv` updated for both.
`full_text_retrieval_queue.csv` regenerated (2,577 open records).
Duplicate audit (DOI + record_id) and `validate_schemas.py` both clean.
Running totals: 1,082/3,659 screened (535 include/547 exclude), 2,577
open, 535 extracted studies, 26 effect_sizes rows.

## 2026-09-21 — Sixty-first full-text screening batch (8 Drive-retrieved PDFs, 4 excludes + 4 new includes S532-S535) + self-caught screening/extraction mismatch fix

A further batch of 8 PDFs surfaced in the Google Drive retrieval inbox.
Four excludes:

- **R33EDCF0902FE** — Arctic community wastewater-treatment engineering
  study. **EXCLUDE E01.** No legal-administrative access dimension;
  purely a treatment-technology engineering study.
- **RD1D7FB8C4689** — children's-participation urban-planning study.
  **EXCLUDE E01.** General participatory-planning literature, no
  water-access mechanism examined.
- **RE6A753BADE5C** — Nigeria conflict/cholera commentary piece.
  **EXCLUDE E01.** Commentary, not empirical evidence of a
  legal-administrative access mechanism.
- **R844EAC3AEE12** — Dewi et al., slum-participation study. **EXCLUDE
  E01.** General participatory-planning discussion of informal
  settlements; no specific connection/eligibility/enforcement mechanism
  analyzed. (Note: this file arrived in the inbox mislabeled with
  record_id `RB8BD27638F17` — see retrieval-script bug note below — and
  was correctly re-matched by title against
  `full_text_screening_database.csv` before being screened under its
  true record_id, R844EAC3AEE12.)

Four new includes:

- **RB8BD27638F17** — Murray, Meyer & Fourie (2023). "Workshopping Water
  Justice: linking struggles from the Cape Flats to the rest of the
  Continent." *Globalisation, Societies and Education* 21(5):705-719.
  doi 10.1080/14767724.2023.2165478. **INCLUDE.** Extracted as **S532**
  (CASP).
- **R589F244C9832** — Ghertner (2023). "Infrastructures of Overlordship:
  Law, Labor Camps, and the Material Geographies of Servitude." *Annals
  of the American Association of Geographers* 113(6):1483-1500. doi
  10.1080/24694452.2023.2187340. **INCLUDE.** Extracted as **S533**
  (Legal Institutional Evidence Appraisal Framework, per the convention
  used for doctrinal/jurimetric legal-case-analysis studies).
- **RE955C8795F4F** — Saha & Chakma (2026). "Co-producing household
  water insecurity: environmental constraints, socio-economic
  inequalities, and local water governance in rural Puruliya, Eastern
  India." *SN Social Sciences* 6:371. doi 10.1007/s43545-026-01660-w.
  **INCLUDE.** Extracted as **S534** (MMAT).
- **R3858447F3CCC** — Grisaffi, Leinster, Sipuma, Owako & Parker (2026).
  "New definitions for good practice: Regulators as activists for urban
  road-transported sanitation in eastern and southern Africa." *PLOS
  Water* 5(1):e0000385. doi 10.1371/journal.pwat.0000385. **INCLUDE.**
  Extracted as **S535** (CASP).

**Self-caught process error (for the audit trail):** the four S532-S535
extraction rows were initially added to `extraction_database.csv`
without recording the corresponding `full_text_decision`/
`final_decision` = "include" in `full_text_screening_database.csv` in
the same step. This produced a transient mismatch (529 include vs. 533
extracted rows), caught immediately by the routine
include-count-vs-extraction-row-count cross-check run before finalizing
this batch's documentation. Fixed by explicitly recording the four
missing include decisions, each individually verified as still-open
before being set. No decision was revisited or re-litigated — this was
purely a missed bookkeeping step, corrected before commit.

**Retrieval-script mislabeling — recurrence noted.** The Dewi et al.
PDF (true record_id R844EAC3AEE12, excluded E01 above) arrived in the
inbox labeled with record_id `RB8BD27638F17`, which actually belongs to
a separate, correctly-labeled file already in the inbox ("Workshopping
Water Justice," extracted as S532 above). This is a new instance of the
same DOI-mislabeling bug class the researcher's local session reported
fixing on 2026-09-21 (see the sixtieth-batch entry below) — either that
fix is incomplete or this file predates/postdates the local session's
18-PDF re-test sample. Flagged for the researcher/local session; the
file was screened correctly under its true record_id via title-match
against the screening database before any decision was recorded.

`evidence_map.csv` updated for S532-S535. `full_text_retrieval_queue.csv`
regenerated (2,579 open records). Duplicate audit (DOI + record_id) and
`validate_schemas.py` both clean after the mismatch fix. Running
totals: 1,080/3,659 screened (533 include/547 exclude), 2,579 open, 533
extracted studies, 26 effect_sizes rows.

## 2026-09-21 — Sixtieth full-text screening batch (3 Drive-retrieved PDFs, 1 new include S531) + S469 data-gap fix

A further batch of PDFs surfaced in the Google Drive retrieval inbox
(beyond the 7 already handled in the enrichment pass below). Three were
genuinely new, still-open screening records (the other apparent "new"
files in the inbox turned out to be duplicate copies of already-decided
records, mislabeled by a since-fixed bug in the researcher's local
retrieval script — see note below):

- **R0B87CA1C5270** — Fonta, Gordon & Toumpakari (2025). "A
  cross-comparative analysis of child poverty across sub-Saharan Africa:
  the case of Francophone and Anglophone African states." *International
  Journal of Health Governance* 30(1):44-58. **EXCLUDE E01.** Cross-national
  DHS-survey (945,487 children, 22 countries) ANOVA/risk-ratio comparison
  of multidimensional child-poverty outcomes between Francophone and
  Anglophone colonial-legacy groupings; the water-poverty dimension itself
  shows no significant colonial-origin difference (RR=1.00). A macro
  cross-national comparative epidemiology study, not an analysis of a
  specific household-level legal-administrative access mechanism.
- **R6C87B9274F13** — Aigbavboa, Addo, Ebekozien, Thwala & Arthur-Aidoo
  (2025). "Appraising institutional management of urban water supply in
  Ghana: the role of the stakeholders." *Journal of Facilities Management*
  23(2):269-288. **INCLUDE.** Sequential exploratory mixed-methods study
  (19 KIIs + 521-respondent survey, Greater Accra) documenting a real
  household water-connection procedure: submit a site plan (affidavit
  required "in some situations"), write to the district manager, GWCL
  survey/cost estimate (~2 weeks), payment before connection; individual
  applicants are first redirected to the district assembly for a permit.
  Extracted as **S531** (MMAT).
- **R8D17337BEC6A** — Luyaba, Mbhele, Moyo, Nsubuga & Mafunda (2025).
  "Benchmarking efficiency to support a transition to financial
  sustainability in the South African municipal water sector." *Water
  Policy* 27(11):1270-1290. **EXCLUDE E01.** DEA-based infrastructure-
  management-efficiency and creditworthiness benchmarking across 144
  South African water-services-authority municipalities; a utility-level
  financial/infrastructure-efficiency study, no household-level
  connection-access mechanism examined.

**Data-integrity fix, S469** (Alam et al. 2025, "Barriers to sewer
connection in urban Dhaka," extracted 2026-09-18): `effect_measure` and
`effect_estimate` were found blank despite all other 88 fields being
populated — an extraction oversight, not an abstract-only gap. Fixed using
the now-retrieved full-text PDF: 384 matched connected/not-connected
households, with cost (33%), lack of space (16%), legal issues (9%) and
lack of awareness (8%, p=0.002) cited as connection barriers, plus
significant duration-of-settlement, water/sewer-bill, and
years-connected differences between groups (full detail in
`extraction_database.csv`).

**Local retrieval-script bug (now fixed by the researcher's local
session):** the local watcher's DOI matcher pulled DOIs from anywhere in
a PDF's body text (including its own reference list), so a PDF could be
mislabeled with a record it merely cited. This affected 4 inbox files
this round (R0206140E81E4, R6103D8CFE42F, R7220865B32E6, RF78C62C99387),
each a duplicate copy of a PDF already correctly present in the inbox
under its true record_id. The researcher's local session fixed the
matcher (metadata-only DOI extraction, falling back to title matching)
and deleted the 4 mislabelled duplicates after checksum-confirming each
had an identical correctly-labelled copy; R0206140E81E4 (a genuine,
still-open, never-actually-retrieved record — Abrams et al. 2021, South
African WASH vulnerability) was returned to the retrieval queue for real.

`evidence_map.csv` updated for S531. `full_text_retrieval_queue.csv`
regenerated (2,587 open records). Duplicate audit (DOI + record_id) and
`validate_schemas.py` both clean. Running totals: 1,072/3,659 screened
(529 include/543 exclude), 2,587 open, 529 extracted studies, 26
effect_sizes rows.

## 2026-09-21 — Full-text enrichment pass: 7 previously abstract-only extractions upgraded

Via the new Google Drive retrieval pipeline (local watcher script depositing
retrieved PDFs into a shared Drive inbox folder for this session to read),
actual full-text PDFs were retrieved for 7 studies that had been extracted
from abstract-only content on 2026-09-17 pending full text: **S430**
(Ogunbode, Nigeria SDG 6 review), **S431** (Tantoh, Kamerounay, McKay &
Leonard, Bambili Cameroon rural water governance), **S433** (Kadiri, Toxic
waters, Hyderabad informal settlement), **S452** (Mazingisa, Wiysonge &
Kgware, eThekwini school WASH), **S455** (Yanquiling, Dressler & Smith,
colonial cholera/water infrastructure Philippines), **S458** (Dhaundiyal,
Indian Himalayan Region heritage water architecture policy), and **S467**
(Opdyke et al., post-conflict Marawi displacement/WASH).

This is an **enrichment pass, not a new-include batch** — all 7 studies were
already counted in prior running totals (528 include / 541 exclude, 528
extracted studies); no include/exclude decisions were revisited, per the
project's standing duplicate-defer rule. Each study's full text was read in
full and cross-checked against its existing extraction row:

- **S430, S455, S458** — full text confirmed the existing abstract-based
  extraction was already substantively accurate and complete; no field
  changes beyond an `extraction_note` verification stamp.
- **S433** — added `eligibility=TRUE` and `documentation=TRUE`; the full
  text reveals a concrete documentation-based service-qualification barrier
  (Aadhaar cards, residency certificates) that formally disqualifies many
  households in Film Nagar Basti's 18 informally settled colonies from
  municipal water regardless of need, plus markedly uneven municipal
  responsiveness by settlement-recognition status. `regulatory_model` and
  `effect_estimate` enriched accordingly.
- **S431** — added `fees=TRUE`; the full text reveals a direct conflict of
  interest (4 of 7 private mini-water schemes are owned by Bambili Water
  Authority Board of Directors members who approved their own schemes and
  can charge non-participating households for connection) plus specific
  household cash/in-kind contribution and O&M fee schedules. `effect_estimate`
  enriched accordingly.
- **S452, S467** — `citation` fields (previously generic placeholders
  pending full-text bibliographic detail) and `doi` fields completed:
  S452 → *Sustainability* 18(11):5333, doi 10.3390/su18115333; S467 →
  *International Journal of Disaster Resilience in the Built Environment*
  17(2):297-313, doi 10.1108/IJDRBE-06-2025-0069.

`evidence_map.csv` judgment-call fields (mechanism_family, outcome_family,
study_design_class) reviewed against full text for all 7 studies and found
already accurate; no changes required. No new `effect_sizes.csv` rows added
this pass — candidate quantitative contrasts in S452 (gender-differentiated
Hygiene Access Index, p=0.008) and S467 (housing-damage/satisfaction
correlations) were considered but not added, as neither is a direct
legal-administrative connection-access mechanism within this review's
strict effect-size eligibility criteria.

Duplicate audit (DOI + record_id-in-extraction_note) re-run after these
edits: no duplicates introduced. `validate_schemas.py` confirms all 13
tracked files still match their documented/generated schema. Totals
unchanged: 1,069/3,659 screened (528 include/541 exclude), 2,590 open,
528 extracted studies, 26 effect_sizes rows.

## 2026-09-21 — Fifty-ninth full-text screening batch: 4 researcher-supplied PDFs, 0 new includes

The researcher uploaded 4 more PDFs. All four were excluded, all E01
(wrong topic):

- **R2042942EE2E9** — Gbekley, E.H. et al. (2023). "Urban Governance
  and Sanitation in the Peri-Urban Commune of Agoe-Nyve 6 in Togo:
  Diagnosis of the Sanitation System in Adetikope." *Water* 15(18):3306.
  Cross-sectional descriptive KAP survey (5256 households) of household
  wastewater/excreta management practices (latrine types/condition,
  discharge points, TDE-utility satisfaction); no eligibility,
  documentation, fee, discretion, or enforcement mechanism content.
- **R178B38D4B00E** — Tangworachai, S.; Wong, W.-K.; Lo, F.-Y. (2023).
  "Determinants of water consumption in Thailand: sustainable
  development of water resources." *Studies in Economics and Finance*
  40(5):950-970. ARDL econometric time-series analysis of aggregate
  regional water-consumption determinants (price, income, climate) at
  the MWA/PWA utility level; no household-level access mechanism.
- **R713FCE4485F0** — Adeoti, O.S.; Kandasamy, J.; Vigneswaran, S.
  (2023). "Water infrastructure sustainability in Nigeria: a systematic
  review of challenges and sustainable solutions." *Water Policy*
  25(11):1094. PRISMA systematic review (15 studies) of technical,
  financial, environmental, social, political, and institutional
  factors in Nigerian water-infrastructure failure; broad infrastructure
  sustainability, not household-level service-connection mechanisms.
- **R52422EAFB872** — Hellberg, S. (2023). "What constitutes the social
  in (social) sustainability? Community, society and equity in South
  African water governance." *Local Environment* 28(4):459-475.
  Governmentality-theory study (18 expert interviews plus policy-
  document analysis) theorizing "the social" in social sustainability;
  a theoretical/conceptual study, not an empirical analysis of a
  specific legal-administrative access mechanism's effect on household
  outcomes.

No new extractions, evidence_map, or effect_sizes changes this batch.
`full_text_retrieval_queue.csv` regenerated (2,590 open records).
`validate_schemas.py` confirms all 13 tracked files still match their
documented/generated schema.

## 2026-09-21 — Fifty-eighth full-text screening batch: 3 researcher-supplied PDFs, 2 new includes (S529-S530)

The researcher uploaded 3 more PDFs. One new exclude, two new includes:

- **R30DF179C3488** — Martín Velasco, M.J.; Calderón, G.; Lima, M.L.;
  Matencón, C.L.; Massone, H.E. (2023). "Water governance challenges at
  a local level: implementation of the OECD Water Governance Indicator
  Framework in the General Pueyrredon Municipality, Buenos Aires
  Province, Argentina." *Water Policy* 25(7):623-638. **EXCLUDE E01.**
  Qualitative governance-assessment study (OECD traffic-light
  framework, expert panel plus OSSE/ADA official interviews) evaluating
  water-resources governance broadly across 12 principles (capacity,
  financing, regulatory frameworks, stakeholder engagement, basin
  coordination). A brief social-rate/affordability mention appears
  under Principle 11, but the paper's core focus is a general
  water-resources governance-capacity diagnostic, not household-level
  service-connection mechanisms.
- **R9E6D4A706EE3** — Wagle, P. (2024). "Water access disparity in
  Mumbai, India: Using spatial and structural attributes as formal
  conditionalities." *Journal of Urban Affairs* 46(4):831-844.
  **INCLUDE.** Qualitative document/interview study (64 interviews with
  municipal engineers, experts, and activists) documenting MCGM's
  two-tier water-connection entitlement system: a shared standpost
  connection (45 LPCD) for "slum" dwellings vs. an individual
  house-service connection (135 LPCD) for "other-than-slum" dwellings,
  with the full entitlement contingent on spatial/structural
  documentation conditionalities (Commencement Certificate, No-
  Objection-Certificate, Occupation/Building-Completion Certificate,
  Hydraulic Engineer Remarks) that render informal dwellings formally
  ineligible. Extracted as **S529** (CASP).
- **RFFE87AAC2802** — Hofstetter, M.; Bolding, A.; Boelens, R. (2023).
  "Rooted Water Collectives in a Modernist and Neoliberal Imaginary:
  Threats and Perspectives for Rural Water Commons." *Water*
  15(21):3736. **INCLUDE.** Qualitative comparative case study
  (100+ interviews across extended action-research engagement) of
  three rural user-owned water collectives (two in South Africa, one
  in Switzerland), documenting how South Africa's Water Services Act
  1997 and Municipal Systems Act 2000 rendered most community-based
  water schemes "technically illegal" as unlicensed service providers,
  leaving their formal status contingent on municipal discretion in a
  legal grey zone, and how Swiss subsidy conditions pressured a
  60-year-old cooperative toward forced merger. Extracted as **S530**
  (CASP).

Neither new include was added to `effect_sizes.csv` (qualitative case
studies, no locatable inferential exposure-comparator effect estimate).
A corpus-wide duplicate audit (exact-DOI + record_id-in-extraction_note
methods) came back clean against the resulting 528-study corpus.
`full_text_retrieval_queue.csv` regenerated (2,594 open records).
`validate_schemas.py` confirms all 13 tracked files still match their
documented/generated schema.

## 2026-09-21 — Fifty-seventh full-text screening batch: 2 researcher-supplied PDFs, 0 new includes

The researcher uploaded 2 more PDFs. Both were excluded:

- **R4F91395D4663** — Walling, D. (2024). "Governing infrastructure,
  development and inequality around deindustrialized US cities."
  *Territory, Politics, Governance* 12(6):725-745. **EXCLUDE E01.**
  Comparative case study (Scranton, PA vs. Providence, RI) using social
  network analysis of institutional governance relationships across
  economic-development and drinking-water infrastructure systems,
  examining rate-setting authority location (state Public Utility
  Commission oversight of Scranton's privately-owned water utility vs.
  city-controlled Providence Water). Unit of analysis is institutional/
  organizational networks and regional economic-development governance
  structure, not households; no household-level eligibility,
  documentation, connection, or access/affordability outcome data.
- **R98DAA4FFBC8B** — Hosseini, S.; Yadav, P. (2024). "The Significance
  of Traditional Legal Framework in Regulating Groundwater Rights in
  Iran." *LEAD Journal* 20(1):1-15. **EXCLUDE E05.** Doctrinal/
  historical legal analysis (literature review of historical,
  religious, and legal texts from the Sassanid Empire, 224 CE, to the
  1906 Iranian Constitution) of traditional Iranian groundwater
  property-rights doctrine using Schlager & Ostrom's common-pool-
  resource framework. No primary data collection or defined empirical
  study design -- pure doctrinal commentary without empirical access
  evidence.

No new extractions, evidence_map, or effect_sizes changes this batch.
`full_text_retrieval_queue.csv` regenerated (2,597 open records).
`validate_schemas.py` confirms all 13 tracked files still match their
documented/generated schema.

## 2026-09-21 — Fifty-sixth full-text screening batch: 3 researcher-supplied PDFs, 0 new includes

The researcher uploaded 3 more PDFs. All three were excluded:

- **R1E7614BBAC9B** — Rivera-Nunez, I.M.; Luque Agraz, D.; Murphy, A.D.;
  Jones, E.C.; Flores-Cuamea, M.A. (2024). "The Types of Water Conflicts
  in an Irrigation System in Northern Mexico: Conflict as a Negative
  Link in Social Network Analysis." *Social Sciences* 13(6):312.
  **EXCLUDE E07.** Social network analysis (118 structured interviews +
  6 key-informant interviews + ethnography) of conflicts among users
  and institutional actors in the Rio Mayo Irrigation District, Sonora.
  The paper's core focus, title, and majority of empirical content
  (Conflict Types 1-2, ~31 of 45 non-structural-remnant users) concern
  irrigation-water resource governance among farmers (agrotitanes,
  land-rental blocks, irrigation-module hydrocracy). Conflict Type 3
  (14 users) touches genuine domestic/household water content (OOMAPAS
  utility poor service/high fees driving self-managed community/
  artisanal wells), but this is a secondary sub-theme within a study
  whose dominant focus is irrigation-water resource governance --
  wrong service.
- **RA86420433D1C** — Milligan, R.; Adams, E.A.; Wheeler, C.;
  Raulerson, S.; Vermillion, N. (2024). "The hydro-racial fix in
  infrastructural regions: Atlanta's situation in a regional water
  governance conflict." *Territory, Politics, Governance* 12(6):866-883.
  **EXCLUDE E07.** Qualitative study (10 years participant observation +
  20 semi-structured interviews) applying racial-capitalism theory to
  the interstate Apalachicola-Chattahoochee-Flint water dispute between
  Georgia, Florida and Alabama over regional water-resource allocation.
  Core empirical focus is interstate/regional water-RESOURCE allocation
  governance, not household-level service-connection mechanisms.
- **R683C9C404D89** — Eduful, M. (2024). "Toward good governance in
  water resources management in Ghana." *Natural Resources Forum*
  48(3):485-507. **EXCLUDE E01.** Qualitative study (31 semi-structured
  interviews) examining Ghana's IWRM institutional framework (Water
  Resources Commission, Densu River Basin Management Board) and
  regulatory mechanisms (water-use permits/charges, environmental
  permitting, buffer-zone policy). A broad water-RESOURCES governance-
  institution study, not focused on household-level drinking-water/
  sanitation SERVICE connection-access mechanisms.

No new extractions, evidence_map, or effect_sizes changes this batch.
`full_text_retrieval_queue.csv` regenerated (2,599 open records).
`validate_schemas.py` confirms all 13 tracked files still match their
documented/generated schema.

## 2026-09-19 — Fifty-fifth full-text screening batch: 3 researcher-supplied PDFs, 1 new include (S528)

The researcher uploaded 3 more PDFs. Two new excludes, one new include:

- **R2C4C322911D6** — Sibley, M.; Peach, K.; Leon-Corwin, M.; Selvakumar,
  P.P.; Diodosio, K.; Fox, A.; Spurlock, C.; Olofsson, K. (2024).
  "Exploring risk-scapes in Oklahoma: institutional trust, environmental
  justice, climate change, and infrastructure." *Safer Communities*
  23(2):152-170. **EXCLUDE E04.** Nested regression models (n=2,687
  Oklahoma adults, M-SISNet survey) predicting institutional trust,
  environmental-justice perceptions, and climate-change risk
  perceptions, with "concern for water infrastructure" (a subjective
  3-item perception/attitude index) as an outcome. The outcome measured
  is subjective concern, not an objective water-service access,
  connection, or exclusion outcome; no legal/administrative mechanism
  content.
- **R4FCD4A37638A** — Rodrigues, P.M.; Goncalves, J.; Marques, R.C.
  (2024). "Public policies on human rights to water in informal
  settlements: a bibliometric analysis." *Water Policy* 26(7):718.
  **EXCLUDE E05.** Bibliometric/scientometric meta-analysis (citation-
  network, keyword co-occurrence, thematic mapping of 1,702
  publications, 1978-2023). Contains no primary or synthesized
  empirical findings about actual household/community water-access
  outcomes -- studies publication metadata, not water access itself.
- **R91862C6D9F43** — Santos, J.G.; Ioris, A.A.R. (2024). "Water
  Conflicts and Socioterritorial Dynamics: The Hydrosocial Cycle After
  the Sao Francisco River Transposition Project in the Northeast of
  Brazil." *Land* 13(12):2032. **INCLUDE.** Ethnographic study (48
  interviews in 2019 + 12 follow-up interviews in 2024 with resettled
  rural families, plus federal institutional-actor interviews) of
  Brazil's largest water-infrastructure project (PISF), finding that
  845 directly-affected families resettled across 18 rural villages
  are not guaranteed access to or use of the transposed water despite
  living in its immediate surroundings, and that popular participation
  is excluded from the project's formal governance Management Board
  (only formal institutional actors participate). Extracted as **S528**
  (CASP).

Not added to `effect_sizes.csv` (ethnographic case study, no locatable
inferential exposure-comparator effect estimate). A corpus-wide
duplicate audit (exact-DOI + record_id-in-extraction_note methods) came
back clean against the resulting 526-study corpus.
`full_text_retrieval_queue.csv` regenerated (2,602 open records).
`validate_schemas.py` confirms all 13 tracked files still match their
documented/generated schema.

## 2026-09-19 — Fifty-fourth full-text screening batch: 2 researcher-supplied PDFs, 1 new include (S527)

The researcher uploaded 2 more PDFs. One new exclude, one new include:

- **R53BA195BE952** — Suyeno, S.; Sumartono, S.; Haryono, B.S.; Amin, F.
  (2024). "Water governance puzzle in Riau Province: uncovering key
  actors and interactions." *Water Policy* 26(1):60. **EXCLUDE E01.**
  Textual Network Analysis (TNA) of government policy/regulatory
  documents mapping actor networks (central/provincial/local government
  agencies) in Durolis regional water-supply-system governance across
  three Riau Province regencies, Indonesia. A governance-network/
  stakeholder-mapping study using document text-mining; no household-
  level eligibility, documentation, fee, discretion, or enforcement
  mechanism content, and no household/community population or access/
  connection/affordability outcome examined.
- **R73F67667C714** — Khadam, N.; Bukhtawer, N.; Iqbal, Z.; Qayyum, H.;
  Khan, Z.F.; Razzaq, M.; Idrees, F. (2024). "Gender inequality, water
  rights and policy implications: learning from the experience of
  experts working in water sector." *Cogent Social Sciences*
  10(1):2334109. **INCLUDE.** Qualitative expert-panel study (6
  water-sector experts, six-stage Braun & Clarke thematic analysis)
  documenting that formal, documented water connections in Pakistan are
  legally tied to property ownership (departing from the Easement Act
  1882 only with Punjab's 2019 Water Act), automatically excluding
  landless households -- disproportionately headed/represented by
  women, since only 36 of 1000 women in Punjab own land -- from formal
  supply. Also reviews Sindh's 2018 Water Management Ordinance
  amendment introducing a gender quota for water-governance bodies and
  the Local Government Ordinance 2001's women's council-seat
  reservations (15-33% by province), only ~19.6% of which were actually
  filled in the 2013/2015 elections. Extracted as **S527** (CASP).

Not added to `effect_sizes.csv` (qualitative expert-panel study, no
locatable inferential exposure-comparator effect estimate). A
corpus-wide duplicate audit (exact-DOI + record_id-in-extraction_note
methods) came back clean against the resulting 525-study corpus.
`full_text_retrieval_queue.csv` regenerated (2,605 open records).
`validate_schemas.py` confirms all 13 tracked files still match their
documented/generated schema.

## 2026-09-19 — Fifty-third full-text screening batch: 2 researcher-supplied PDFs, 2 new includes (S525-S526), first effect_sizes.csv addition since 2026-09-17

The researcher uploaded 2 more PDFs. Both were newly-decided records
(no duplicates this round):

- **RC2CB18536B31** — Kachenje, Y.E. (2025). "Institutional Coordination
  Challenges in Service Delivery the Case of Water Supply in Dar Es
  Salaam, Tanzania." *International Journal of Research and Innovation
  in Social Science* 8(12):2087-2103. **INCLUDE.** Qualitative case
  study (key informant interviews, focus group discussions, household
  interviews, document analysis) comparing one public (DAWASA), one
  private, and one community-based water-supply scheme in Dar es
  Salaam. Table 1 reports processing time for new water-connection
  applications: a maximum of 30 days (public) vs. 3 days (private) vs.
  6 days (community-based), involving 5, 2, and 3 key actors
  respectively. Most private providers are found to be unregistered as
  formal service providers, recognized only informally by residents,
  reflecting weak enforcement of the Water Supply and Sanitation Act
  2019, the EWURA Act, and the Water Resources Management Act.
  Extracted as **S525** (CASP).
- **R09A594443F58** — Switzer, D.; Teodoro, M.P. (2025). "Public
  enterprise pricing as redistributive policy." *Policy Studies
  Journal* 53(2):365-387. **INCLUDE.** Cross-sectional OLS regression
  (n=1,183-1,189 US water utilities serving 40,000+ residents, 2019
  rate data + 2017 ACS income data) testing whether local income
  inequality (mean-to-median income ratio) predicts water-rate
  progressivity (unit price ratio), and whether the relationship
  differs between local-government-owned utilities (rates set by
  elected officials) and investor-owned utilities (rates set by state
  Public Utilities Commissions). Finds income inequality correlates
  positively and significantly with price progressivity (coefficient
  0.310, p=0.005), while private/investor-owned ownership
  independently predicts more regressive pricing (coefficient -0.167,
  p<0.001); the Private x Inequality interaction term was in the
  expected (weaker-for-private) direction but not statistically
  significant (-0.209, p=0.387). Extracted as **S526** (JBI Critical
  Appraisal Checklist for Analytical Cross Sectional Studies).

S526's ownership-type effect estimate was added to
`05_analysis/effect_sizes/effect_sizes.csv` as a genuine, non-fabricated
exposure-comparator regression result (Family C — administrative/legal
barriers and access inequality, per `PROJECT_SPEC.md` §8), bringing the
tracked-studies-with-a-real-effect-estimate total to 26. S525 was not
added (qualitative case study; the processing-time figures reported are
single-case descriptive comparisons, not a locatable inferential
exposure-comparator estimate). A corpus-wide duplicate audit (exact-DOI
+ record_id-in-extraction_note methods) came back clean against the
resulting 524-study corpus. `full_text_retrieval_queue.csv` regenerated
(2,607 open records). `validate_schemas.py` confirms all 13 tracked
files still match their documented/generated schema.

## 2026-09-18 — Fifty-second full-text screening batch: 6 researcher-supplied PDFs, 2 duplicates skipped, 3 new includes (S522-S524)

The researcher uploaded 6 more PDFs. Two were duplicate re-uploads of
already-decided records, both deferred to without reprocessing:

- **R5104D5ACF77A** (Fono et al. 2025, "Aboriginal and Torres Strait
  Islander Perspectives in Drinking Water Policy: A Realist Review"):
  already included as **S521**.
- **R30B01FDAF470** (Shoko 2025, "Structural Determinants of Conflicts
  and Cooperation in Rural Water Management"): already excluded
  **E05**.

One new exclude:

- **R5C25784E85C8** — Bae, J.; Kang, S.; Lynch, M.J. (2025). "Drinking
  Water Injustice: Racial Disparity in Regulatory Enforcement of Safe
  Drinking Water Act Violations." *Race and Justice* 15(3):335-355.
  **EXCLUDE E04.** OLS regression (n=1,860 community water systems,
  EPA SDWIS data, robust SEs) finding that SDWA noncompliance-duration
  length is longer for water systems in counties with higher Black/
  Hispanic populations and shorter for counties with higher White
  populations; poverty/income were not statistically significant. The
  outcome is state/federal regulatory-enforcement duration for water-
  QUALITY violations at the utility/system level, not household-level
  legal-administrative eligibility/burden/discretion/enforcement
  mechanisms governing service CONNECTION or exclusion — the same
  category as prior E03/E04 exclusions for SDWA-compliance studies
  (Dobbin & Fencl 2021; Anica 2022).

Three new includes:

- **RAD821298C663** — Aizannon, G.S.; Akueson, G.H.A.; Moumouni-Moussa,
  I. (2025). "Does the Emergence of Private Actors in the Potable
  Water Market Reduce Inequalities and Improve Access? A Critical
  Analysis Based on a Case Study in Selected Municipalities of Benin."
  *International Journal of Research and Innovation in Social
  Science* 8(12):2620-2636. **INCLUDE.** Mixed-methods case study
  (2023 interviews with local producers/consumers plus a descriptive
  survey across four Beninese communes) finding 63.10% of surveyed
  consumers rely on private operators, 52% of surveyed producers lack
  a formal water safety plan, and rural coverage (~60%) trails urban
  coverage (~85%), amid an acknowledged absence of a robust regulatory
  framework governing private operators. Extracted as **S522**
  (MMAT).
- **RC61AA453D176** — Rempel, J.L.; Dobbin, K.B. (2025). "When
  'symbolic' policy is anything but: Policy design and feedbacks from
  California's human right to water law." *Policy Studies Journal*
  53(3):701-722. **INCLUDE.** Qualitative case study (23 interviews
  plus archival/document analysis) of California's AB 685 (2012)
  human-right-to-water law, tracing a decade of indirect resource
  effects: the SB-200 SAFER program (up to $1.4 billion for low-income
  drinking-water needs), a COVID-19 shutoff moratorium followed by
  over $1 billion in household water-debt credit relief, and SB-88's
  state-mandated consolidation of local water systems persistently
  failing low-income populations. Extracted as **S523** (CASP).
- **R6A776E9F321E** — Hernando-Arrese, M.; Ibarra, M.I. (2025).
  "Waters of resistance: decolonising perspectives on women's
  territorial r-existence in southern Chile." *Gender & Development*
  33(1):189-213. **INCLUDE.** Ethnographic case study (8 interviews
  plus a 14-person focus group) of gendered water-rights and
  connection-access disparities among Rural Drinking Water Committees/
  Cooperatives (APRs) in the Toltén hydrosocial territory, Chile,
  documenting that 47.2% of the rural population lacks formal potable-
  water access and that APRs/Indigenous communities hold only 3.7% of
  regionally granted water rights versus 23% for 16 individuals/private
  companies. Extracted as **S524** (CASP).

None of the three new includes was added to `effect_sizes.csv`
(descriptive mixed-methods percentages and qualitative case studies,
no locatable inferential exposure-comparator effect estimate). A
corpus-wide duplicate audit (exact-DOI + record_id-in-extraction_note
methods) came back clean against the resulting 522-study corpus.
`full_text_retrieval_queue.csv` regenerated (2,609 open records).
`validate_schemas.py` confirms all 13 tracked files still match their
documented/generated schema.

## 2026-09-18 — Fifty-first full-text screening batch: 7 researcher-supplied PDFs across two uploads, 2 new includes (S520-S521)

The researcher uploaded 7 more PDFs across two chat messages (arriving
mid-turn while documentation for the previous batch was still being
updated). All 7 were newly-decided records (no duplicates this round).

Five new excludes:

- **R278169A3D0E0** — Mungekar, N.; Holscher, K.; Janssen, A.; Loorbach,
  D. (2025). "Repairing urban water governance through informality:
  comparing governance capacities for reparation in Indian cities."
  *Water Policy* 27(4):521. **EXCLUDE E01.** Comparative ethnographic
  case study (64 semi-structured interviews plus observation notes
  across Bhuj and Bhopal, India) of "consolidative" and "jugaadu"
  informal-governance capacities for reparative water-sensitive urban
  governance. Documents real informal institutions (Ward/Mohalla
  Samitis, councillor-mediated intermediation, NGO cost-sharing funding,
  standalone-tank/RWH interventions), but the analytic focus and
  reported outcome are the governance-capacity/reparation theoretical
  framework itself, not a specific household-level access mechanism
  tied to a measured connection/service outcome.
- **R83113184DA6F** — Hoang, P.D.; Tran, N.T. (2025). "Applying
  nontraditional security management to address critical local water
  challenges: the case of Hanoi, Vietnam." *Water Policy* 27(4):400.
  **EXCLUDE E01.** Qualitative assessment rating Hanoi's water-security
  management effectiveness across coarse city-wide dimensions
  (technical, policy/legislation, social, economic, awareness) using a
  3-level scale; a broad city-wide governance-effectiveness framework,
  not household-level legal-administrative mechanism analysis.
- **R228B6D79BA63** — KC, S. et al. (2025). "Nexus governance in
  practice: a stakeholder-driven framework for groundwater
  sustainability in Barahathawa Municipality, Madhesh Province."
  *Sustainability Nexus Forum* 33:20. **EXCLUDE E01.** A 32-indicator
  Groundwater Governance Index (technical, legal/institutional,
  cross-sector, operational dimensions) assessed via expert/community
  surveys for a groundwater resource used predominantly for irrigation
  (85%), with domestic hand-pump supply a minor secondary use; a broad
  water-RESOURCE governance-index study, not household drinking-water/
  sanitation SERVICE access focused.
- **RC88A6B7A249D** — Thommandru, A.; Turdialiev, M.A.; Mone, V. (2025).
  "Hydro-hegemony in the Anthropocene: Neoliberal Paradigms and Global
  South Marginalization in Water Scarcity Governance." *Journal of
  Developing Societies* 41(3):383-405. **EXCLUDE E05.** Conceptual/
  narrative essay on hydro-hegemony and neoliberalism illustrated with
  secondary-source case vignettes (Nile/Jordan River disputes,
  Cochabamba, Mumbai "Water for All", Indian watershed-restoration
  examples); no defined empirical study design or original data
  collection.
- **REC9732CB9945** — Vignesh, K. (2025). "Water Pricing, Tariff, and
  Conflicts: The Dynamics of Political Economy, Fairness, and Cost
  Recovery." *Peace Review* 37(4):670-692. **EXCLUDE E05.**
  Self-described "qualitative and integrative" case-based narrative
  synthesis with conceptual theorization, drawing on the Pacific
  Institute's Water Conflict Chronology and news archives for
  illustrative case vignettes (Cochabamba, Ireland, Johannesburg/Durban,
  Detroit, Manila, Jakarta); no defined case-selection methodology or
  systematic-review search protocol.

Two new includes:

- **RE68DB735F2D8** — Kharmylliem, B.; Kipgen, N. (2025). "Village
  councils, social capital and sustainability: a study of urban water
  management of Shillong in Meghalaya, India." *Water Policy*
  27(3):301. **INCLUDE.** Qualitative case study (semi-structured
  interviews) of clan-based property control over springs/borewells and
  village-council (*dorbar shnong*) governance of household water
  distribution in Shillong, contrasting commercialized and communal
  distribution models and documenting locality-based disparities in
  connection access and scarcity. Extracted as **S520**.
- **R5104D5ACF77A** — Fono, M.A. et al. (2025). "Aboriginal and Torres
  Strait Islander Perspectives in Drinking Water Policy: A Realist
  Review." *Australian Journal of Social Issues* 60:602-620.
  **INCLUDE.** PRISMA-documented realist systematic review (5
  peer-reviewed studies + 33 grey-literature sources, JBI critical
  appraisal, context-mechanism-outcome analysis) of Aboriginal and
  Torres Strait Islander peoples' engagement in Australian drinking-
  water policy at macro/meso/micro system levels, finding fragmented
  and inconsistent engagement and 400+ remote/regional communities
  lacking safe drinking-water access. Extracted as **S521** (flagged
  `study_design_class = systematic_review_secondary`, AMSTAR 2).

Neither new include was added to `effect_sizes.csv` (qualitative case
study and realist review; no locatable quantitative effect estimate). A
corpus-wide duplicate audit (exact-DOI + record_id-in-extraction_note
methods) came back clean against the resulting 519-study corpus.
`full_text_retrieval_queue.csv` regenerated (2,613 open records).
`validate_schemas.py` confirms all 13 tracked files still match their
documented/generated schema.

## 2026-09-18 — Fiftieth full-text screening batch: 9 researcher-supplied PDFs across two uploads, 3 duplicates skipped, 1 new include (S519)

The researcher uploaded 9 more PDFs across two chat messages (one arriving
mid-turn while the first batch was still being analyzed). Three were
duplicate re-uploads of already-decided records, all deferred to without
reprocessing:

- **REA305644CBB3** (Chambolle 1999, "De l'eau pour tous?"): already
  excluded **E05**.
- **R4266AA2DF8F3** (Busari 2002, "Millennial Policies... Southern African
  Example"): already excluded **E05** (note: `full_text_screening_database.csv`
  records this as E05, not E01 as a prior summary stated — the exclusion
  detail text reads "no identifiable empirical study design", i.e. E05's
  code, matching its own `exclusion_reason_detail`).
- **RF5EE990F4D41** (Lee & Floris 2003, *Natural Resources Forum*):
  already included as **S518**.

Six records were screened fresh:

- **R50E028EACDD8** — Birkinshaw M. (2026). "Smart water? Corporate
  experiments and hybrid hydraulics in India." *Urban Geography*
  47(5):1027-1048. **INCLUDE.** A 21-month embedded ethnographic study
  (2012-2025 fieldwork; 30+30 interviews plus 12 months living in an
  urban village and 9 months in an unauthorized colony) of the Malviya
  Nagar Water Services (MNWS) "smart water" PPP in Delhi (Suez + SPML
  Infra). Documents how Delhi's 8 legally differentiated settlement-type
  categories (jhuggi-jhompri hut clusters, recognized slums, resettlement
  colonies, planning-exempt rural/urban villages, unauthorized colonies,
  regularized unauthorized colonies, planned colonies — after Bhan 2013)
  structure settlement-type-dependent access to metered connections and
  24/7 supply pilots: recognized slums and 3 wealthy planned colonies got
  good service, while urban villages and unauthorized colonies were left
  with contaminated "hybrid hydraulic" supply and self-built connections
  treated as illegal under Water Board engineering norms despite being
  built out of necessity. Extracted as **S519**. Not added to
  `effect_sizes.csv` (ethnographic qualitative study, no locatable
  quantitative effect estimate).
- **R4DE47C45D5E7** — Mia, Md. Sakib; Parvin, Mehnaz; Islam, Md Jahidul
  (2026). "Unplanned urbanisation and drinking water insecurity in
  Faridpur City, Bangladesh." *Development in Practice* 36(2):295-310.
  **EXCLUDE E01.** Interpretative Phenomenological Analysis (20
  semi-structured interviews) of water scarcity, time burden, unsafe
  storage, harassment/safety risk during collection, domestic conflict,
  and social humiliation tied to private tube-well ownership disputes;
  Socio-Ecological Systems framework. A social/gender/psychological
  water-insecurity study; governance-failure language appears only in
  passing with no concrete eligibility/documentation/fee/enforcement
  mechanism content.
- **RAB6AA06D8E9D** — Carranza, L.A.; Verdura, N.C.; Gargallo, J.R.
  (2025). "Socioeconomic impacts derived from the effects of climate
  change on water quality in Catalonia (Spain)..." Conference abstract
  ckaf180.144, *European Journal of Public Health* 35(Suppl 6). **EXCLUDE
  E09.** Conference-abstract-only record (8 semi-structured stakeholder
  interviews, QUEEN project); insufficient methodological detail to
  assess design, sample, or extractable outcomes.
- **R981381DE4EDB** — Mueller, A.B.; Bosch, H.J.; Gupta, J.; Karg, A.
  (2026). "Mapping water property rights through water use permits and
  the implications for water (re)allocation: a global south overview."
  *Water Policy* 28(7):927-947. **EXCLUDE E07.** Comparative legal
  analysis of water-use-permit quasi-property-rights systems (duration,
  renewal, transfer, compensation, dispute settlement, suspension/
  revocation) across 110 Global South countries. Rich legal-institutional
  mechanism content, but the unit of analysis is water-RESOURCE
  allocation permits (irrigation, industrial, agricultural, groundwater/
  surface abstraction), not household/community drinking-water or
  sanitation SERVICE connection access — wrong service, consistent with
  prior E07 precedent for water-rights/permit-market studies.
- **RA2ACB8D17124** — Stiegler, M.H. (2004). "Requiring Water Supply
  Connection Is Within Town's Police Power" (plus a companion case note),
  *Journal AWWA* 96(10):36. **EXCLUDE E05.** Brief "law & water"
  practitioner case-note column summarizing two US appellate decisions
  (a Nebraska water-appropriation nonuse cancellation; a Rhode Island
  case on a town's police power to require public-water-system
  connection for a building permit). No defined empirical study design;
  the Rhode Island case concerns a real-estate developer's zoning
  entitlement, not household/low-income service-access exclusion.
- **R20286B7A363F** — Kamga, M.A.; Tsayo Kenzo, S.; Toussoumna, E.;
  Nodem Fomene, R.; Letah Nzouebet, W.A.; Suya, R.G. (2026). "Spatial
  analysis of socio-collective infrastructure and territorial
  inequalities in a rural context: evidence from Fokoué Subdivision
  (West Cameroon)." *GeoJournal* 91:101. **EXCLUDE E06.** GIS-based
  spatial-accessibility and technical-standards-compliance assessment of
  water, health, and education infrastructure (distance-to-standpipe,
  population-per-tap, slope, flood-exposure compliance against WHO/
  MINEDUB thresholds). Pure spatial/technical infrastructure-siting and
  standards-compliance study; no eligibility, documentation, fee,
  discretion, or enforcement mechanism analysis.

A corpus-wide duplicate audit (exact-DOI + record_id-in-extraction_note
methods) came back clean against the resulting 517-study corpus.
`full_text_retrieval_queue.csv` regenerated (2,620 open records).
`validate_schemas.py` confirms all 13 tracked files still match their
documented/generated schema.

## 2026-09-18 — Forty-ninth full-text screening batch: 3 researcher-supplied PDFs, 2 duplicates skipped, 1 new include (S518)

The researcher uploaded three more PDFs directly via chat. Two were
duplicate re-uploads of already-decided records, both deferred to
despite the fresh reads, per the project's standing rule against
re-litigating already-decided records:

- **R4266AA2DF8F3** (Busari 2002, *Canadian Water Resources Journal*,
  "Millennial Policies and Strategies for Promoting Household Water
  Security: A Southern African Example"): already excluded **E01** — a
  Swaziland rural water-sector policy/institutional-capacity review
  (planning/coordination, financial, technical, social issues), not
  focused on household-level legal-administrative access mechanisms.
  This independent re-read reached the same conclusion.
- **REA305644CBB3** (Chambolle 1999, *La Houille Blanche*, "De l'eau
  pour tous?"): already excluded **E05** — a Suez Lyonnaise des Eaux
  corporate research synthesis (1997 internal project) on serving
  underprivileged districts across multiple concession contracts
  (Argentina, La Paz, Manila, Jakarta, Casablanca), documenting
  authorities' reluctance to "legalize" informal settlements and
  thereby avoid conferring official recognition, and Durban's
  three-tier alternative service-delivery system. This fresh read
  leaned toward inclusion given its rich institutional-exclusion
  content, but the existing E05 rationale (no defined empirical study
  design, sample, or data-collection methodology) is a defensible call
  on a genuinely different axis (methodological rigor rather than
  topical relevance) and was not re-litigated.

**Include:**

- **RF5EE990F4D41** (Lee & Floris 2003, *Natural Resources Forum*,
  "Universal access to water and sanitation: Why the private sector
  must participate"): a four-country comparative policy analysis
  (Argentina, Chile, Bolivia, Peru) of private-sector water-utility
  participation. Documents Buenos Aires's contract renegotiation
  obliging service extension to suburban shanty towns and a universal
  service and environmental improvement fee (SUMA) cross-subsidizing
  new-connection costs; La Paz/El Alto's connection-fee tiers reduced
  for households supplying labour (Table 3) and a proof-of-land-title
  requirement for new connections that the utility considered waiving
  but which was "reinstated at the insistence of the municipality";
  and a welfare-loss counterfactual analysis estimating Lima's failure
  to privatize SEDAPAL cost US$557.80 million in domestic benefits
  (1995-2004 NPV) while leaving over 1.7 million people unconnected.
  Extracted as **S518** (`risk_of_bias_tool = Legal Institutional
  Evidence Appraisal Framework`, `study_design_class` resolved by hand
  as `jurimetric`, `mechanism_family = MULTIPLE` — `eligibility`,
  `burden`, `discretion_accommodation`, `outcome_family =
  primary_connection`).

Not added to `effect_sizes.csv` (comparative case-study/scenario-model
figures, no inferential exposure-comparator estimate). Duplicate audit
(exact-DOI and record_id-in-extraction_note methods) came back clean.
`full_text_retrieval_queue.csv` regenerated (2,626 open records).
`validate_schemas.py` reports all 13 checked files match their
documented/generated schema.

## 2026-09-18 — Forty-eighth full-text screening batch: 4 researcher-supplied PDFs, 2 duplicates skipped, 2 new excludes

The researcher uploaded four more PDFs directly via chat. Two were
duplicate re-uploads of already-decided records and were skipped
without reprocessing: Morgan (2006, "Turning off the tap"), already
extracted as **S517** in the immediately preceding batch; and Acero,
Safarpour, Faust, Lin, Albertson, Stephens & Spearing (2026, *Environ.
Res. Commun.*, "Cross-sector lifecycle challenges impacting Alaska's
critical infrastructure systems"), already excluded E01.

**New excludes (both E01, wrong topic):**

- **R4B98C5717E00** (Karmaksh & Kumar 2026, *Water Policy*, "Urban
  development and water bodies in Indian cities: a systematic review of
  reciprocal relationships"): a 62-paper PRISMA-style systematic review
  synthesizing broad thematic literature on urban water in Indian
  cities (supply/efficiency reforms, peri-urban/informal water systems,
  wastewater reuse, governance/equity/resilience, sustainable
  practices, water insecurities) spanning hydrology, urban planning,
  GIS, and governance generally, not focused on household-level
  legal-administrative eligibility/burden/discretion/enforcement
  mechanisms.
- **REDD845E73CF8** (Levin, Epstein, Ford, Harrington, Olson & Reichard
  2002, *Environmental Health Perspectives*, "U.S. Drinking Water
  Challenges in the Twenty-First Century"): a broad review of US public
  drinking-water infrastructure challenges (pricing, utility
  consolidation, public/private ownership, climate change, waterborne
  disease, land use, groundwater/surface water, SDWA regulatory
  history) focused on technical/public-health infrastructure and
  water-quality regulation for the already-connected population, not
  household-level legal-administrative access-barrier mechanisms.

No new includes this batch. Duplicate audit (exact-DOI and
record_id-in-extraction_note methods) came back clean.
`full_text_retrieval_queue.csv` regenerated (2,627 open records).
`validate_schemas.py` reports all 13 checked files match their
documented/generated schema.

## 2026-09-18 — Single-record screening: 1 new include (S517), flagged HIGH PRIORITY by the researcher

★ **The researcher explicitly flagged this record as a key, high-priority
reference for the dissertation** — this is noted here, in `S517`'s
`extraction_note`/`regulatory_model` field in `extraction_database.csv`,
and in `evidence_level` in `evidence_map.csv`, so it stays visible to
anyone reviewing the corpus. There is no dedicated "priority" field in
`CODEBOOK.md`'s fixed 92-field schema, so the flag is carried as a
prominent, clearly-marked prefix in the relevant free-text fields rather
than as a new column.

**Include:**

- **R73C643F91689** (Morgan 2006, *European Journal of International
  Law*, "Turning off the tap: Urban water service delivery and the
  social construction of global administrative law"): a comparative
  doctrinal/qualitative case study of Argentina and South Africa (part
  of a six-country research project) analyzing the Vivendi/Aguas del
  Aconquija v. Argentina ICSID investment-arbitration dispute arising
  from the Tucuman water concession — including the provincial
  Ombudsman's dispute-resolution interventions and five consecutive
  judges' refusal of jurisdiction over a collective non-payment
  lawsuit — and South Africa's shift from a "political" to a
  "transactional" water-tariff/disconnection regulatory model, alongside
  constitutional case law on disconnection due process (*Residents of
  Bon Vista Mansions v Southern Metropolitan Local Council*; *Manqele v
  Durban Transitional Metropolitan Council*) and cross-subsidy equality
  (*Pretoria City Council v Walker*, decided 5-4). The paper's central
  analytical finding: "global administrative law" in urban water
  service delivery is constituted through iterative interaction between
  formal legal processes and informal political modes (protest,
  negotiation, media), with end-users and foreign water-service
  providers holding sharply asymmetric capacity to switch between
  domestic and international levels of governance. Extracted as **S517**
  (`risk_of_bias_tool = CASP`, `mechanism_family = MULTIPLE` — `burden`,
  `discretion_accommodation`, `enforcement`, `outcome_family =
  administrative_outcome`).

Not added to `effect_sizes.csv` (doctrinal/qualitative case study, no
inferential exposure-comparator estimate). Duplicate audit (exact-DOI
and record_id-in-extraction_note methods) came back clean.
`full_text_retrieval_queue.csv` regenerated (2,629 open records).
`validate_schemas.py` reports all 13 checked files match their
documented/generated schema.

## 2026-09-18 — Forty-seventh full-text screening batch: 5 researcher-supplied PDFs, 1 duplicate skipped, 2 excludes + 2 new includes (S515-S516)

The researcher uploaded five more PDFs directly via chat. One was a
duplicate re-upload of an already-decided record: Milton, Hore, Hossain
& Rahman (2012, *Emerging Health Threats Journal*, "Bangladesh arsenic
mitigation programs: lessons from the past," already excluded E03) and
was skipped without reprocessing.

**Excludes (both E01, wrong topic):**

- **RB45F57F659FC** (Babah, Deida, Blake & Froelich 2012, *Procedia
  Engineering*, "Fresh water distribution problematic in Nouakchott"): a
  215-household survey and physico-chemical/bacteriological water-
  quality study of Nouakchott, Mauritania's informal terminal-fountain
  distribution system, with no legal-administrative mechanism content.
- **R4DC2A9DD9226** (Iribarnegaray & Seghezzo 2012, *Sustainability*,
  "Governance, Sustainability and Decision Making in Water and
  Sanitation Management Systems"): develops and applies a Sustainable
  Water Governance Index (SWGI) methodology to Salta, Argentina — a
  governance-index framework paper, not an empirical legal-administrative
  mechanism study.

**Includes:**

- **RF464DBEDC353** (Ioris 2012, *Geoforum*, "The geography of multiple
  scarcities: Urban development and water problems in Lima, Peru"): a
  54-interview political-ecology case study (a distinct companion paper
  to the already-included S304, Ioris 2012 in *Singapore Journal of
  Tropical Geography*, on the same broader Lima fieldwork) documenting
  the 1961 law that defined the legal status of Lima's barriadas and
  provided a legal framework for their integration into the city, and
  SEDAPAL's rejected low-cost condominial connection system, perceived
  by residents as "a second-class solution... intrinsically
  discriminatory as it was only adopted in the periphery of the city."
  Extracted as **S515** (`risk_of_bias_tool = CASP`, `mechanism_family =
  MULTIPLE` — `eligibility`, `burden`, `discretion_accommodation`,
  `outcome_family = primary_connection`).
- **RD49DE850A4CE** (Subbaraman, O'Brien, Shitole, Shitole, Sawant,
  Bloom & Patil-Deshmukh 2012, *Environment and Urbanization*, "Off the
  map: the health and social implications of being a non-notified slum
  in India"): a four-year mixed-methods PUKAR-Harvard-NYU research
  collaboration in Kaula Bandar, Mumbai (a distinct companion paper to
  the already-included S084, Lubeck-Schricker et al. 2023, on the same
  broader non-notified-slum research programme) documenting a 1995
  addendum to the Maharashtra Slum Areas Act 1971 conditioning basic-
  amenity entitlement on pre-1995 residency proof, a No Objection
  Certificate mechanism by which the central-government land-owning
  agency (Mumbai Port Trust) blocks state service extension, routine
  police fines for informal water-tanker use and open defecation, and a
  disaster-compensation payout 37 times smaller per household than a
  comparable notified slum received after an equivalent fire. Extracted
  as **S516** (`risk_of_bias_tool = MMAT`, `mechanism_family = MULTIPLE`
  — `eligibility`, `burden`, `enforcement`, `outcome_family =
  primary_connection`).

Neither new include was added to `effect_sizes.csv` (qualitative
case study and descriptive comparative statistics respectively, no
inferential exposure-comparator estimate). Duplicate audit (exact-DOI
and record_id-in-extraction_note methods) came back clean.
`full_text_retrieval_queue.csv` regenerated (2,630 open records).
`validate_schemas.py` reports all 13 checked files match their
documented/generated schema.

## 2026-09-18 — Forty-sixth full-text screening batch: 4 researcher-supplied PDFs, 2 duplicates skipped, 2 new excludes

The researcher uploaded four more PDFs directly via chat. Two were
duplicate re-uploads of already-decided records, both independently
re-confirmed against fresh reads before being skipped without
reprocessing:

- **R86610BDFBD5E** (Roy 2013, *Urban Water Journal*, "Negotiating
  marginalities: right to water in Delhi"): already extracted as
  **S416** (Kathputli Colony legally-notified-slum case study).
- **R1A33C22EDA73** (Baird, Summers & Plummer 2013, *Canadian Water
  Resources Journal*, "Cisterns and safe drinking water in Canada"):
  already excluded **E03** — a fragmented, province-by-province
  regulatory-gap review of private-cistern drinking-water-quality risk
  (legal responsibility resting with the private owner/user), not a
  formal-connection eligibility/burden/discretion/enforcement study.

**New excludes (both E01, wrong topic):**

- **R87DEE5B78284** (Johnston, Hug, Inauen, Khan, Mosler & Yang 2014,
  *Science of the Total Environment*, "Enhancing arsenic mitigation in
  Bangladesh: Findings from institutional, psychological, and technical
  investigations"): a synthesis of institutional-stakeholder preference
  surveys, RANAS-model psychological drivers of arsenic-safe
  water-technology adoption, and technical/geochemical evaluation of
  deep-tubewell water quality — a technology-preference/behavior-change
  and technical-geochemistry study with no household-level
  legal-administrative mechanism content.
- **RE5DB6996E04E** (Okeola & Sule 2012, *Journal of King Saud
  University – Engineering Sciences*, "Evaluation of management
  alternatives for urban water supply system using Multicriteria
  Decision Analysis"): an Analytic Hierarchy Process (AHP) exercise
  selecting among hypothetical public/private ownership-operation
  models for Offa, Nigeria's urban water works, based on a
  questionnaire-elicited hypothetical Decision Making Group — an
  abstract institutional-ownership decision-methodology paper with no
  empirical household-level legal-administrative mechanism content.

No new includes this batch. Duplicate audit (exact-DOI and
record_id-in-extraction_note methods) came back clean.
`full_text_retrieval_queue.csv` regenerated (2,634 open records).
`validate_schemas.py` reports all 13 checked files match their
documented/generated schema.

## 2026-09-18 — Forty-fifth full-text screening batch: 5 researcher-supplied PDFs, 1 duplicate skipped, 1 exclude + 3 new includes (S512-S514)

The researcher uploaded five more PDFs directly via chat. One was a
duplicate re-upload of an already-decided, already-extracted record:
Majuru, Suhrcke & Hunter (2016, *IJERPH*, "How Do Households Respond to
Unreliable Water Supplies? A Systematic Review," a systematic review of
28 studies on household coping strategies — storing, drilling wells,
purchasing water, treating water — for unreliable water, already
extracted as **S438**) and was skipped without reprocessing.

**Exclude (E01, wrong topic):**

- **RFB194B660A78** (Ferro & Mercadier 2016, *Utilities Policy*,
  "Technical efficiency in Chile's water and sanitation providers"): a
  stochastic-frontier-analysis (SFA) econometric study estimating the
  comparative technical efficiency of 18 Chilean water/sewerage
  providers (2005-2013), focused on Non-Revenue Water reduction and
  X-Factor/K-Factor tariff-regulation design — a utility technical/
  economic efficiency benchmarking study with no household-level
  legal-administrative mechanism content.

**Includes:**

- **RA617D33E8893** (Dobbin & Sarathy 2015, *Society & Natural
  Resources*, "Solving Rural Water Exclusion: Challenges and Limits to
  Co-Management in Costa Rica"): a mixed-methods 3-ASADA comparative
  case study finding that despite an identical formal ICAA delegation
  agreement and regulatory framework across all three community water
  associations, the low-performing ASADA (Hatillo) operated in "blatant
  disregard" of ICAA regulations (no water meters, below-recommended
  tariffs, unchlorinated water averaging 218.25 E. coli/100ml) despite
  its board president being the most knowledgeable of all three about
  ICAA law — and that violations led to no official sanctions in any of
  the three communities, exposing incapacities in the state-oversight
  framework for both high- and low-performing co-management alike.
  Extracted as **S512** (`risk_of_bias_tool = MMAT`, `mechanism_family =
  MULTIPLE` — `burden`, `discretion_accommodation`, `enforcement`,
  `outcome_family = effective_access`).
- **RA0D30B3E8C1C** (McGranahan 2015, *World Development*, "Realizing
  the Right to Sanitation in Deprived Urban Communities: Meeting the
  Challenges of Collective Action, Coproduction, Affordability, and
  Housing Tenure"): a conceptual/narrative synthesis (illustrated by the
  Orangi Pilot Project, Karachi, and the Alliance in Mumbai/Pune)
  documenting that utilities "may not be allowed" to serve settlements
  "until the settlement has been recognized by the government," and
  that tenure insecurity can cut either way on landlords'/tenants'
  incentive to invest in sanitation improvements. Extracted as **S513**
  (`risk_of_bias_tool = Legal Institutional Evidence Appraisal
  Framework`, `study_design_class` resolved by hand as `doctrinal`,
  `mechanism_family = MULTIPLE` — `eligibility`, `burden`,
  `discretion_accommodation`, `outcome_family = primary_connection`).
- **RCE4DA02A6859** (Chowns 2015, *Public Administration and
  Development*, "Is Community Management an Efficient and Effective
  Model of Public Service Delivery? Lessons from the Rural Water Supply
  Sector in Malawi"): a mixed-methods study (679 water points, 276
  users/managers, 26 key-informant interviews, ~50,000-case national
  database) finding Water Point Committee Maintenance Fund savings
  averaged just 2% of the amount they should hold, against a national
  water-sector budget marginalized to 1-3% of government spending
  (versus 16% each for education and health) and a water ministry
  downgraded out of ministerial status — concluding community management
  persists because it "works" for the state and donors as a means of
  offloading responsibility, not because it delivers the promised
  technical/financial benefits. Extracted as **S514**
  (`risk_of_bias_tool = MMAT`, `mechanism_family = MULTIPLE` — `burden`,
  `outcome_family = effective_access`).

None of the three new includes was added to `effect_sizes.csv`
(descriptive multi-case comparison, conceptual synthesis, and
descriptive mixed-methods statistics respectively — no inferential
exposure-comparator estimate in any). Duplicate audit (exact-DOI and
record_id-in-extraction_note methods) came back clean.
`full_text_retrieval_queue.csv` regenerated (2,636 open records).
`validate_schemas.py` reports all 13 checked files match their
documented/generated schema.

## 2026-09-18 — Forty-fourth full-text screening batch: 5 researcher-supplied PDFs, 2 duplicates skipped, 3 excludes

The researcher uploaded five more PDFs directly via chat. Two were
duplicate re-uploads of already-decided, already-extracted records and
were skipped without reprocessing: Muia Mutua, Agwata & Anyango (2017,
Mavoko Municipality, Machakos County, Kenya sanitation-policy-instrument
effectiveness study), already extracted as **S423**; and Saraswat, Mishra
& Kumar (2017, Kathmandu Valley WEAP integrated urban water management
scenario modeling), already excluded E06 — both re-reads independently
confirmed the same decisions already on record (include and exclude E06
respectively) before being skipped.

**Excludes (all E01, wrong topic):**

- **REB85F9212C3F** (Schramm & Wright-Contreras 2017, *Geoforum*, "Beyond
  passive consumption: Dis/ordering water supply and sanitation at
  Hanoi's urban edge"): an urban-infrastructure-studies/STS analysis of
  periurban and new-urban-area residents' socio-technical practices for
  accessing water/sanitation beyond centralized networks (private wells,
  housing cooperatives), focused on infrastructure planning history and
  financing/corporatization dynamics rather than household-level legal-
  administrative eligibility/burden/discretion/enforcement mechanisms.
- **R35688D83A3FB** (Hutchings, Parker & Jeffrey 2016, *Journal of Rural
  Studies*, "The political risks of technological determinism in rural
  water supply: A case study from Bihar, India"): a discourse-analysis
  study contrasting India's National Water Policy with a traditionalist
  grassroots movement's storylines about handpump vs. open-well
  technology, examining technological-determinism discourse and policy
  framing rather than legal-administrative access-barrier mechanisms.
- **R27783A9D443D** (Aadnesgaard & Willows 2016, *Corporate Ownership &
  Control*, "Audit outcomes and the level of service delivery within
  local government municipalities in South Africa"): a 52-municipality
  correlational study of financial audit outcomes versus a composite
  service-delivery score-card, using aggregate municipal-level statistics
  with no household-level legal-administrative mechanism content.

Duplicate audit (exact-DOI and record_id-in-extraction_note methods) came
back clean. `full_text_retrieval_queue.csv` regenerated (2,640 open
records). `validate_schemas.py` reports all 13 checked files match their
documented/generated schema.

## 2026-09-18 — Forty-third full-text screening batch: 5 researcher-supplied PDFs, 4 excludes + 1 new include (S511)

The researcher uploaded five more PDFs directly via chat.

**Excludes (all E01, wrong topic):**

- **RF4D94533DCB2** (Arimah 2017, *Procedia Engineering*, "Infrastructure
  as a Catalyst for the Prosperity of African Cities"): a UN-Habitat
  Expert Opinion Survey study of water supply, road network, and
  telecommunications infrastructure's aggregate, city-level contribution
  to "urban prosperity" across 14 African cities; no household-level
  legal-administrative eligibility/burden/discretion/enforcement content.
- **R3945222BBF31** (Garn, Sclar, Freeman, Penakalapati, Alexander,
  Brooks, Rehfuess, Boisson, Medlicott & Clasen 2017, *International
  Journal of Hygiene and Environmental Health*, "The impact of
  sanitation interventions on latrine coverage and latrine use: A
  systematic review and meta-analysis"): a WHO-commissioned systematic
  review/meta-analysis (64 studies) of sanitation intervention-type
  effectiveness (CLTS, subsidy/provision, education, sewerage, Total
  Sanitation Campaign) on latrine coverage and use — a technical
  public-health intervention-effectiveness review, not a legal-
  administrative mechanism study.
- **R60BD629D7DFF** (Manda & Wanda 2017, *Environment and Urbanization*,
  "Understanding the nature and scale of risks in Karonga, Malawi"): a
  380-household survey and hospital-records study of disaster and
  everyday risks (flooding, earthquakes, droughts, traffic accidents,
  political violence, disease, unsafe water/sanitation) in a
  disaster-risk-reduction framework; water/sanitation is only one of
  several everyday-risk categories, with no legal-administrative
  eligibility/burden/discretion/enforcement analysis.
- **R812164425DA7** (Whaley & Cleaver 2017, *Water Resources and Rural
  Development*, "Can 'functionality' save the community management
  model of rural water supply?"): a literature review of the
  Community-Based Management (CBM) and water point committee (WPC)
  "functionality" literature for rural handpump water supply in
  Sub-Saharan Africa, engaging with committee governance and
  socio-technical functionality theory rather than the review's
  legal-administrative mechanism framework.

**Include:**

- **R7477260689CE** (Poupeau & Hardy 2017, *Water International*, "The
  social conditions of self-organized utilities: water cooperatives in
  La Paz and El Alto, Bolivia"): a mixed-methods study (GIS mapping,
  550-household questionnaire, interviews, and a monographic case study
  of the Las Nieves cooperative) documenting Bolivia's legal requirement
  that Alternative Service Delivery (ASD) water cooperatives register
  with the Ministry for Water and Environment (rarely done "due to the
  complicated and costly bureaucratic steps required"), the formal
  utility EPSAS's legal exclusion of "non-constructible" (natural-hazard)
  zones from its service area, the La Paz municipal government's
  largely absent formal recognition of cooperatives, and detailed
  comparative tariff/connection-fee data (EPSAS BOB 1.9-2.6/m3; ASD
  average BOB 10/month per World Bank survey; Las Nieves cooperative BOB
  5/month plus a BOB 500 connection fee). Extracted as **S511**
  (`risk_of_bias_tool = MMAT`, `mechanism_family = MULTIPLE` —
  `eligibility`, `burden`, `discretion_accommodation`,
  `outcome_family = formal_connection`).

S511 was not added to `effect_sizes.csv` (descriptive case-study/survey
tariff comparison, no inferential exposure-comparator estimate).
Duplicate audit (exact-DOI and record_id-in-extraction_note methods)
came back clean. `full_text_retrieval_queue.csv` regenerated (2,643 open
records). `validate_schemas.py` reports all 13 checked files match
their documented/generated schema.

## 2026-09-18 — Forty-second full-text screening batch: 5 researcher-supplied PDFs, 2 new includes (S509-S510)

The researcher uploaded five more PDFs directly via chat. Three were
duplicate re-uploads of already-decided, already-extracted records
(Zaunda et al. 2018 disability-friendly school WASH facilities, already
S403; Monney & Antwi-Agyei 2018 Ghana MDG water-target review, just
excluded E01 earlier this same batch; Wang & Li 2018 rural China
infrastructure governance/finance study, already S439) and were skipped.

**Includes:**

- **R7142E0CB4FAE** (Akwataghibe, Wegelin, Postma, Fajemisin, Banda, Khan,
  Jurji & Toonen 2018, *Journal of Water, Sanitation and Hygiene for
  Development*, "Exploring equity focus of the SHAWN WASH programme in
  Nigeria"): a mixed-methods programme evaluation (2,105-household
  survey, 294-household disability sub-survey, 62 IDIs, 60 FGDs)
  documenting needs/commitment-based LGA selection scoring, hardship-
  based eligibility criteria for latrine-construction support (lack or
  disability of a male household head), WASHCOM gender-quota selection
  discretion, and political interference in water-point siting producing
  skewed distribution. Extracted as **S509** (`risk_of_bias_tool = MMAT`,
  `mechanism_family = MULTIPLE` — `eligibility`, `burden`,
  `discretion_accommodation`, `outcome_family = economic_access`).
- **R546A1803D994** (Adams & Smiley 2018, *Natural Resources Forum*,
  "Urban-rural water access inequalities in Malawi: implications for
  monitoring the Sustainable Development Goals"): a mixed-methods
  comparative household-survey study (645 peri-urban, 139 rural
  households) documenting Malawi's 1995 Water Works Act establishing the
  legal basis for parastatal water boards, Water User Association
  partnerships extending service to underserved peri-urban areas, and
  detailed comparative connection-cost/payment data across urban/rural
  contexts (household tap connection ~US$56 vs. private rural well
  construction ~US$1,200). Extracted as **S510** (`risk_of_bias_tool =
  MMAT`, `mechanism_family = MULTIPLE` — `burden`,
  `discretion_accommodation`, `outcome_family = economic_access`).

Neither new include was added to `effect_sizes.csv` (descriptive
household-survey statistics, no inferential exposure-comparator
estimate). Duplicate audit (exact-DOI and record_id-in-extraction_note
methods) came back clean. `full_text_retrieval_queue.csv` regenerated
(2,648 open records). `validate_schemas.py` reports all 13 checked files
match their documented/generated schema.

## 2026-09-18 — Forty-first full-text screening batch: 5 researcher-supplied PDFs, 2 excludes + 1 new include (S508)

The researcher uploaded five more PDFs directly via chat. Two were
duplicate re-uploads of already-decided, already-extracted records
(Zaunda, Holm, Itimu-Phiri, Malota & White 2018, disability-friendly
school WASH facilities in Rumphi, Malawi, already included as S403;
Wang & Li 2018, rural China community/social-development infrastructure
governance/finance study, already included as S439) and were skipped.

**Excludes (both E01, wrong topic):**

- **RA397C02E9861** (van Welie & Romijn 2018, *Environmental Science &
  Policy*, "NGOs fostering transitions towards sustainable urban
  sanitation in low-income countries"): a Transition Management-framework
  case study of a Dutch NGO's sanitation-chain project in Kisumu, Kenya.
  Core analytical focus is NGO coalition-building/capacity-building
  processes; legal/regulatory gaps appear only incidentally.
- **R20B75DEA6614** (Monney & Antwi-Agyei 2018, *Journal of Water,
  Sanitation and Hygiene for Development*, "Beyond the MDG water target to
  universal water coverage in Ghana"): a broad national policy review of
  Ghana's water-sector institutional framework, financing, and
  environmental/climate issues, with tariff-regulation content appearing
  only secondarily within a much broader review.

**Include:**

- **RAE45D86D7434** (Domínguez Serrano & Castillo Pérez 2018, *Estudios
  Demográficos y Urbanos*, "Las organizaciones comunitarias del agua en el
  estado de Veracruz"): a qualitative case study of Veracruz, Mexico
  community water organizations (patronatos) documenting the absence of
  formal legal recognition for community water organizations in Mexico —
  unlike Chile, Ecuador, and several Central American countries — and the
  "municipal exclusivity" legal argument used to deny recognition, annual
  renewal instability for rural water committees, and CAEV's direct
  administration of rural systems where municipal institutional capacity
  is absent. Extracted as **S508** (`risk_of_bias_tool = CASP`,
  `mechanism_family = MULTIPLE` — `eligibility`, `discretion_accommodation`,
  `enforcement`, `outcome_family = administrative_outcome`). Not added to
  `effect_sizes.csv` (qualitative case study, no inferential
  exposure-comparator estimate).

Duplicate audit (exact-DOI and record_id-in-extraction_note methods) came
back clean. `full_text_retrieval_queue.csv` regenerated (2,650 open
records). `validate_schemas.py` reports all 13 checked files match their
documented/generated schema.

## 2026-09-18 — Fortieth full-text screening batch: 5 researcher-supplied PDFs, 3 excludes + 2 new includes (S506-S507) — 1,006 records screened

The researcher uploaded five more PDFs directly via chat. This batch
resolves a long-standing `wrong_file_retrieved` flag: the DuChanois et
al. 2019 record (`R5725BF04FB9F`) had twice received only a 2-page
erratum notice on prior delivery attempts; this delivery finally
contained the actual 9-page substantive article, allowing a real
screening decision.

**Excludes:**

- **R5725BF04FB9F** (DuChanois, Liddle, Fenner, Jeuland, Evans, Cumming,
  Zaman, Mujica-Pereira, Ross, Gribble & Brown 2019, *Environmental
  Science & Technology*, "Factors Associated with Water Service Continuity
  for the Rural Populations of Bangladesh, Pakistan, Ethiopia, and
  Mozambique"), **E01 wrong topic**: a 4,786-household multi-country
  fractional-logistic-regression study of technical/financial predictors
  of water service continuity (a reliability outcome), not household-level
  legal-administrative eligibility/burden/discretion/enforcement
  mechanisms.
- **R84CEA3C0917E** (Lazaro, Kapute & Holm 2019, *Food Science &
  Nutrition*, "Food safety policies and practices in public spaces...
  Mzuzu, Malawi"), **E01 wrong topic**: a food-safety microbiological
  study (E. coli/Salmonella testing on fish) with regulatory gaps as
  secondary content; core exposure/outcome is foodborne-disease risk, not
  household water/sanitation access.
- **RD2FC36DF2664** (Grasham, Korzenevica & Charles 2019, *WIREs Water*,
  "On considering climate resilience in urban water security... urban
  poor in sub-Saharan Africa"), **E01 wrong topic**: a systematic review
  of urban-poor climate-shock vulnerability (floods, droughts, cholera),
  with colonial-legacy/permit-eligibility content appearing only as
  secondary supporting evidence within a much broader climate-resilience
  review.

**Includes:**

- **R7DE9B0E11BE0** (Hoque, Hope, Arif, Akhter, Naz & Salehin 2019,
  *Science of the Total Environment*, "A social-ecological analysis of
  drinking water risks in coastal Bangladesh"): a 2,103-household
  mixed-methods study with a complete 2,805-tubewell infrastructure audit
  documenting elite-influenced allocation of public tubewells, a failed
  formal water-vending tariff system undermined by political promises of
  "free water for all," absence of regulation for the now-dominant
  private self-supply market (78% of tubewells), and cross-jurisdictional
  boundary effects excluding one union from government arrangements.
  Extracted as **S506** (`risk_of_bias_tool = MMAT`, `mechanism_family =
  MULTIPLE` — `burden`, `discretion_accommodation`, `enforcement`,
  `outcome_family = effective_access`).
- **R6C5C0454C690** (Appiah-Effah, Duku, Azangbego, Aduafo Aggrey,
  Gyapong-Korsah & Nyarko 2019, *Journal of Water, Sanitation and Hygiene
  for Development*, "Ghana's post-MDGs sanitation situation: an
  overview"): a policy review documenting the Local Government Act's
  MMDA sanitation mandate, the National Environmental Sanitation Policy's
  shift of financing responsibility onto households (improved facilities
  costing up to 66% of annual income for the poorest quintiles), and a
  novel 10% property-tax sanitation surcharge piloted in Ga West
  Municipal Assembly. Extracted as **S507** (`risk_of_bias_tool = Legal
  Institutional Evidence Appraisal Framework`, `study_design_class =
  doctrinal`, `mechanism_family = MULTIPLE` — `burden`,
  `discretion_accommodation`, `enforcement`, `outcome_family =
  administrative_outcome`).

Neither new include was added to `effect_sizes.csv` (descriptive
statistics and narrative policy review, no inferential exposure-
comparator estimate). Duplicate audit (exact-DOI and
record_id-in-extraction_note methods) came back clean.
`full_text_retrieval_queue.csv` regenerated (2,653 open records).
`validate_schemas.py` reports all 13 checked files match their
documented/generated schema.

## 2026-09-18 — Thirty-ninth full-text screening batch: 5 researcher-supplied PDFs, 2 excludes + 2 new includes (S504-S505) — 1,001 records screened

The researcher uploaded five more PDFs directly via chat. This batch's
first decision (Enqvist & Ziervogel, S504) brings full-text screening
past **1,001 of 3,659 records decided** for the first time. One item was
a duplicate re-upload of an already-decided, already-extracted record
(Wright-Contreras 2019, "A Transnational Urban Political Ecology of Water
Infrastructures... Hanoi," already included as S441, 2026-09-17) and was
skipped.

**Excludes:**

- **R2A746B07BB89** (Wescoat, Shah, Singh & Murty 2019, *Journal of
  Water, Sanitation and Hygiene for Development*, "Habitations, villages,
  and gram panchayats: local drinking water planning in rural India with
  a Pune district case study"), **E01 wrong topic**: a technical GIS/
  data-integration methodology paper on coordinating administrative
  planning-data levels for rural water planning in India, not focused on
  household-level legal-administrative eligibility/burden/discretion/
  enforcement mechanisms.
- **REA69A46FD418** (Kang 2019, *Water Policy*, "Challenges for water
  infrastructure asset management in South Korea"), **E06 engineering
  only**: an infrastructure engineering/asset-management study of aging
  water/sewage/dam infrastructure deterioration rates and maintenance
  budgets in a near-universally-connected system (98.9% access), no
  household-level access/exclusion mechanism content.

**Includes:**

- **R4C0AB373567F** (Enqvist & Ziervogel 2019, *WIREs Water*, "Water
  governance and justice in Cape Town: An overview"): a narrative
  overview/literature-synthesis of Cape Town's water governance across
  the 2015-2018 drought, documenting the Free Basic Water indigent-
  registration policy, Water Management Devices installed without free/
  prior/informed consent from some residents (with bypassing described as
  "breaking a legal agreement"), regressive block tariffs, and the City's
  three-phase Critical Water Shortages Disaster Plan. Extracted as
  **S504** (`risk_of_bias_tool = Legal Institutional Evidence Appraisal
  Framework`, `study_design_class = doctrinal`, `mechanism_family =
  MULTIPLE` — `eligibility`, `burden`, `discretion_accommodation`,
  `enforcement`, `outcome_family = effective_access`). Complements the
  Cape Town "Day Zero" papers already in the corpus (S492 Millington &
  Scheba; R79DCFD4D36F2 Dugard).
- **R90A7B7F95F14** (Adank, Godfrey, Butterworth & Defere 2019, *Water
  Policy*, "Small town water services sustainability checks: development
  and application in Ethiopia"): a mixed-methods diagnostic sustainability
  assessment of 7 Ethiopian small towns finding all 7 Town Water Utilities
  scored below benchmark (25/100) on "urban poor get affordable water,"
  with 6 of 7 utilities making no provision for shared yard connections
  allowing compound-housing residents to jointly apply for service, and
  Ethiopia scoring 0/100 on having any urban water regulatory agency.
  Extracted as **S505** (`risk_of_bias_tool = MMAT`, `mechanism_family =
  MULTIPLE` — `eligibility`, `burden`, `discretion_accommodation`,
  `enforcement`, `outcome_family = economic_access`).

Neither new include was added to `effect_sizes.csv` (narrative review and
descriptive diagnostic indicator scores, no inferential exposure-
comparator estimate). Duplicate audit (exact-DOI and
record_id-in-extraction_note methods) came back clean.
`full_text_retrieval_queue.csv` regenerated (2,658 open records).
`validate_schemas.py` reports all 13 checked files match their
documented/generated schema.

## 2026-09-18 — Thirty-eighth full-text screening batch: 4 researcher-supplied PDFs, 2 excludes + 1 new include (S503)

The researcher uploaded four more PDFs directly via chat. One was a
duplicate re-upload of an already-decided record (Scruggs, Pratesi &
Fleck 2020, "Direct potable water reuse in five arid inland communities,"
already excluded E01, 2026-09-17) and was skipped.

**Excludes (both E01, wrong topic):**

- **R2F5B70B881D1** (Bayu, Kim & Oki 2020, *Water Resources Research*,
  "Water Governance Contribution to Water and Sanitation Access Equality
  in Developing Countries"): a macro cross-country PCA/regression analysis
  (82 countries) correlating aggregate national governance indicators
  (World Bank WGI, UN-Water GLAAS) with GINI-based access-inequality
  indices. An aggregate governance-index correlational study, not focused
  on household-level legal-administrative mechanisms.
- **R9F1B737223A9** (Robina-Ramírez, Sañudo-Fontaneda & McCallum 2020,
  *Transactions of the Royal Society of South Africa*, "Human dignity as
  a mediator effect for the rights and duties of accessing water and
  sanitation"): a structural equation modeling (SEM-PLS) survey study of
  483 informal Doornkop (Soweto) dwellers measuring psychological/ethical
  constructs (human dignity, governance principles) as predictors of a
  2-item access-perception scale. A psychometric attitudes study, not
  empirical documentation of actual legal-administrative mechanisms.

**Include:**

- **R41F032E11DB1** (Fischer, Hope, Manandhar, Hoque, Foster, Hakim, Islam
  & Bradley 2020, *Global Environmental Change*, "Risky responsibilities
  for rural drinking water institutions: The case of unregulated
  self-supply in Bangladesh"): a mixed-methods infrastructure-audit study
  (blanket water-point inventories, Bayesian growth modeling, secondary
  DPHE cost-archive analysis) documenting the historical DPHE group-
  application eligibility requirement (ten-or-more-household applications,
  formal tender, water-quality testing) for publicly funded tubewells, and
  the complete regulatory vacuum (no drilling permits, registration, or
  quality testing) now governing the private self-supply market that
  installs forty-five tubewells for every one publicly funded tubewell.
  Extracted as **S503** (`risk_of_bias_tool = MMAT`, `mechanism_family =
  MULTIPLE` — `eligibility`, `burden`, `discretion_accommodation`,
  `enforcement`, `outcome_family = effective_access`). Not added to
  `effect_sizes.csv` (growth-trend modeling, no individual exposure-
  comparator estimate meeting the strict bar).

Duplicate audit (exact-DOI and record_id-in-extraction_note methods) came
back clean. `full_text_retrieval_queue.csv` regenerated (2,662 open
records). `validate_schemas.py` reports all 13 checked files match their
documented/generated schema.

## 2026-09-18 — Thirty-seventh full-text screening batch: 5 researcher-supplied PDFs, 1 exclude + 4 new includes (S499-S502) — 500 studies extracted

The researcher uploaded five more PDFs directly via chat. This batch's
fourth include (Chidambaram 2020, S502) brings full extraction to
**500 studies**.

**Exclude:**

- **R76F882DBFBC5** (Díaz-Caravantes, Zuniga-Teran, Martín, Bernabeu,
  Stoker & Scott 2020, *Environment & Urbanization*, "Urban water
  security: a comparative study of cities in the arid Americas"), **E01
  wrong topic**: a comparative secondary-literature study (SETEG
  framework) of three arid-region cities focused on aquifer
  overexploitation, riparian-ecosystem health, and agricultural-vs-urban
  water competition. No household-level legal-administrative
  eligibility/burden/discretion/enforcement content.

**Includes:**

- **R00DA63CC6F36** (Ekane, Kjellén, Westlund, Ntakarutimana & Mwesige
  2020, *Development Policy Review*, "Linking sanitation policy to
  service delivery in Rwanda and Uganda: From words to action"): a
  17-interview qualitative comparative study documenting Rwanda's Organic
  Law (2005) open-defecation/waste-dumping penalties and Uganda's Public
  Health Act (1964/2000) provision that dwellings without proper
  sanitation facilities may be "closed down and or its owner prosecuted,"
  set against weak enforcement capacity and institutional fragmentation
  in both countries. Extracted as **S499** (`risk_of_bias_tool = CASP`,
  `mechanism_family = MULTIPLE` — `burden`, `discretion_accommodation`,
  `enforcement`, `outcome_family = administrative_outcome`).
- **R0B762667B98F** (Mitlin & Walnycki 2020, *The Journal of Development
  Studies*, "Informality as Experimentation: Water Utilities' Strategies
  for Cost Recovery and their Consequences for Universal Access"): a
  mixed-methods study across four sub-Saharan African cities (Blantyre,
  Dar es Salaam, Harare, Windhoek) drawing on large SDI-affiliate
  household surveys, finding six-person households can face water costs
  up to 112% of income (Blantyre) and that 30% of Blantyre's piped
  connections had been disconnected at least once for unpaid bills in the
  prior 5 years, alongside Windhoek's "development levels" legal
  framework for low-income migrant access to communal water points.
  Extracted as **S500** (`risk_of_bias_tool = MMAT`, `mechanism_family =
  MULTIPLE` — `eligibility`, `burden`, `discretion_accommodation`,
  `enforcement`, `outcome_family = economic_access`).
- **R7180E92CAB54** (Sharma, Namchu, Nyima, Luitel, Singh & Goodrich 2020,
  *Water Policy*, "Water management systems of two towns in the Eastern
  Himalaya: case studies of Singtam in Sikkim and Kalimpong in West Bengal
  states of India"): a mixed-methods comparative case study documenting a
  PHED connection-eligibility rule barring hotels/restaurants from
  household water connections, unequal multi-connection allocation to
  elite households, and fragmented GTA/state-government governance in
  Kalimpong versus more coordinated governance in Singtam. Extracted as
  **S501** (`risk_of_bias_tool = MMAT`, `mechanism_family = MULTIPLE` —
  `eligibility`, `burden`, `discretion_accommodation`, `enforcement`,
  `outcome_family = effective_access`).
- **R96B6919F9E31** (Chidambaram 2020, *World Development*, "How do
  institutions and infrastructure affect mobilization around public
  toilets vs. piped water? Examining intra-slum patterns of collective
  action in Delhi, India"): a qualitative ethnographic study of four Delhi
  Jhuggi Jhopri Clusters documenting India's notified/non-notified slum
  legal classification (only notified slums are officially entitled to
  individual household piped-water connections), informal "quasi-legal"
  negotiated DJB pipe connections, and the enforcement risk of "illegal
  construction" destruction for unauthorized private toilet connections
  amid DUSIB/DJB/land-owning-agency jurisdictional fragmentation.
  Extracted as **S502** (`risk_of_bias_tool = CASP`, `mechanism_family =
  MULTIPLE` — `eligibility`, `burden`, `discretion_accommodation`,
  `enforcement`, `outcome_family = formal_connection`).

None of the four new includes was added to `effect_sizes.csv`
(descriptive household-survey percentages or qualitative case studies,
no regression-based exposure-comparator estimate meeting the strict
bar). Duplicate audit (exact-DOI and record_id-in-extraction_note
methods) came back clean. `full_text_retrieval_queue.csv` regenerated
(2,665 open records). `validate_schemas.py` reports all 13 checked files
match their documented/generated schema.

## 2026-09-18 — Thirty-sixth full-text screening batch: 5 researcher-supplied PDFs, 3 new includes (S496-S498)

The researcher uploaded five more PDFs directly via chat. Two were duplicate
re-uploads of already-decided, already-extracted records and were skipped
without reprocessing: Venkataramanan et al. 2020 ("Coping strategies for
individual and household-level water insecurity," already excluded E01
earlier this same day) and Zvobgo & Do 2020 ("COVID-19 and the call for
'Safe Hands'... Chitungwiza municipality, Zimbabwe," already included as
S461, 2026-09-17).

**Includes:**

- **RCB86A4946CD4** (Komakech, Kwezi & Ali 2020, *Water Policy*, "Why
  prepaid technologies are not a panacea for inclusive and sustainable
  rural water services in Tanzania?"): a mixed-methods multi-case study
  (1,785-household survey, 101 interviews, 3 districts) documenting
  cost-based exclusion from prepaid water tags/cards ("the current mode of
  exclusion arises from the cost of buying the water tags"), CBWSO
  discretion in identifying "vulnerable households" eligible for free
  water credit, and tariff-setting political struggles under Tanzania's
  2019 Water and Sanitation Act. Extracted as **S496**
  (`risk_of_bias_tool = MMAT`, `mechanism_family = MULTIPLE` —
  `eligibility`, `burden`, `discretion_accommodation`, `outcome_family =
  economic_access`). Not added to `effect_sizes.csv` (descriptive
  household-survey percentages, no regression-based exposure-comparator
  estimate).
- **RAA1E9DFFD38D** (Shah & Badiger 2020, *Water Policy*, "Conundrum or
  paradox: deconstructing the spurious case of water scarcity in the
  Himalayan Region through an institutional economics narrative"): a
  qualitative institutional case study of Darjeeling, India, documenting a
  formal water-connection process requiring three legal land/residency
  documents (Khatian, land registration, municipal mutation document) plus
  a tiered connection fee (USD250-520), municipal discretion over
  approving informal community requests for public standpipes, and
  political/institutional fragmentation across 5 government bodies.
  Extracted as **S497** (`risk_of_bias_tool = CASP`, `mechanism_family =
  MULTIPLE` — `eligibility`, `burden`, `discretion_accommodation`,
  `outcome_family = formal_connection`). Not added to `effect_sizes.csv`
  (qualitative case study, no inferential exposure-comparator estimate).
- **R1DE5B8602164** (Shrestha, Joshi & Roth 2020, *Contemporary South
  Asia*, "The hydro-social dynamics of exclusion and water insecurity of
  Dalits in peri-urban Kathmandu Valley, Nepal"): a 74-interview
  qualitative case study documenting caste-based exclusion of Dalit
  households from a formally registered water-user committee (denied
  membership despite prior-use rights, later required to "pay the same
  rate as new migrants"), Community Forest User Group membership
  requirements tied to land ownership for spring access, and merely
  symbolic Dalit representation on governance committees despite Nepal's
  mandatory-representation policy. Extracted as **S498**
  (`risk_of_bias_tool = CASP`, `mechanism_family = MULTIPLE` —
  `eligibility`, `burden`, `discretion_accommodation`, `enforcement`,
  `outcome_family = effective_access`). Not added to `effect_sizes.csv`
  (qualitative case study, no inferential exposure-comparator estimate).

Duplicate audit (exact-DOI and record_id-in-extraction_note methods) came
back clean. `full_text_retrieval_queue.csv` regenerated (2,670 open
records). `validate_schemas.py` reports all 13 checked files match their
documented/generated schema.

## 2026-09-18 — Thirty-fifth full-text screening batch: 5 researcher-supplied PDFs, 2 excludes + 1 new include (S495)

The researcher uploaded five more PDFs directly via chat. Two were duplicate
re-uploads of already-decided, already-extracted records and were skipped
without reprocessing: Cooper et al. 2021 ("Environmental health conditions
in the transitional stage of forcible displacement," already included as
S427, 2026-09-17) and Schramm & Ibrahim 2021 ("Hacking the pipes:
Hydro-political currents in a Nairobi housing estate," already included as
S460, 2026-09-17).

**Excludes (both E01, wrong topic):**

- **R1EF0C58DFF30** (Bisung & Dickin 2021, *Journal of Water, Sanitation
  and Hygiene for Development*, "Who does what and why? Examining
  intra-household water and sanitation decision-making and autonomy in
  Asutifi North, Ghana"): a 600-respondent intra-household gender
  decision-making autonomy survey (Relative Autonomy Index/self-
  determination theory). Focused on gendered household decision-making
  psychology, not legal-administrative connection/access mechanisms.
- **R0EE420F57BE6** (Venkataramanan et al. 2020, *WIREs Water*, "Coping
  strategies for individual and household-level water insecurity: A
  systematic review"): a systematic review of 173 studies on informal
  household coping behaviors (diversifying sources, storage, purchasing,
  treatment, relocation) for water insecurity. No legal-administrative
  eligibility/burden/discretion/enforcement mechanism content.

**Include:**

- **R71F4B6CD0DF4** (Samuel, Agbola & Olojede 2021, *Local Economy*,
  "Local governance and the crisis of water and sanitation provision in
  medium-sized urban centres: Evidence from three cities in Nigeria"): a
  mixed-methods case study (secondary National Urban Water Sector Reform
  Project data plus 6 official interviews) documenting institutional
  fragmentation across federal/state/local/NGO/donor water-point
  providers (45.8% of 606 facilities non-functional), unregulated private
  water vendors, absence of a dedicated local WSS department, and local
  government fiscal-autonomy constraints under Nigeria's federal system.
  Extracted as **S495** (`risk_of_bias_tool = MMAT`, `mechanism_family =
  MULTIPLE` — `discretion_accommodation`, `enforcement`, `outcome_family =
  administrative_outcome`). Not added to `effect_sizes.csv` (descriptive
  secondary data and qualitative interviews, no inferential
  exposure-comparator estimate).

Duplicate audit (exact-DOI and record_id-in-extraction_note methods) came
back clean. `full_text_retrieval_queue.csv` regenerated (2,673 open
records). `validate_schemas.py` reports all 13 checked files match their
documented/generated schema.

## 2026-09-18 — Thirty-fourth full-text screening batch: 4 researcher-supplied PDFs, 1 exclude + 3 new includes (S492-S494)

The researcher uploaded four more PDFs directly via chat.

**Exclude:**

- **RC062A42C92E7** (Dobbin & Fencl 2021, *Utilities Policy*, "Institutional
  diversity and safe drinking water provision in the United States"), **E03
  wrong exposure/water-quality-only**: a Bayesian mixed-effects regression
  study of 2,867 California community water systems examining Safe
  Drinking Water Act health-based violation counts (a water quality
  compliance outcome) by institutional/governance type. No content on
  household-level legal-administrative eligibility, burden, discretion, or
  enforcement mechanisms governing service connection/access.

**Includes:**

- **R2BEEDB854704** (Millington & Scheba 2020, *International Journal of
  Urban and Regional Research*, "Day Zero and The Infrastructures of
  Climate Change: Water Governance, Inequality, and Infrastructural
  Politics in Cape Town's Water Crisis"): a qualitative political-ecology
  case study (4 official interviews plus civil-society respondents,
  participant observation, discourse analysis) of Cape Town's 2015-2018
  water crisis. Documents the withdrawal of universal Free Basic Water
  (FBW) provision, an arduous indigent-registration eligibility process
  ("almost impossible" for informal-economy workers), Water Management
  Device (WMD/prepaid meter) installation that automatically cuts supply
  once the FBW allocation is exhausted (declared legal following the
  Constitutional Court's Mazibuko ruling), and revised stepped tariff
  structures. Extracted as **S492** (`risk_of_bias_tool = CASP`,
  `mechanism_family = MULTIPLE` — `eligibility`, `burden`,
  `discretion_accommodation`, `enforcement`, `outcome_family =
  effective_access`). Not added to `effect_sizes.csv` (qualitative case
  study, no inferential exposure-comparator estimate).
- **R8228B92EF766** (Giner & Pavon 2021, *Environmental Challenges*, "A
  retrospective analysis of program outcomes and lessons learned on
  implementing first-time wastewater infrastructure in underserved
  communities in Texas from 1995 through 2017"): a mixed-methods
  retrospective program evaluation (GWR spatial regression on $626 million
  in funding across 31 Texas border counties plus 100+ interviews) of
  first-time wastewater service to colonias. Documents the pre-1989
  absence of county land-use enforcement that enabled colonia formation
  without infrastructure, subsequent Model Subdivision Rules legislation
  requiring counties to adopt land-use regulation, household-connection-
  cost subsidy design within grants, and onsite-system permit/biennial-
  inspection requirements. Wastewater coverage grew from under 20% (1995)
  to 77% (2018). Extracted as **S493** (`risk_of_bias_tool = MMAT`,
  `mechanism_family = MULTIPLE` — `eligibility`, `burden`,
  `discretion_accommodation`, `enforcement`, `outcome_family =
  primary_connection`). Not added to `effect_sizes.csv` (county-level GWR
  standardized residuals, not an individual exposure-comparator estimate
  meeting the strict effect-size bar).
- **RF3C4D16222DD** (Rahmasary, Koop & van Leeuwen 2021, *Integrated
  Environmental Assessment and Management*, "Assessing Bandung's
  Governance Challenges of Water, Waste, and Climate Change: Lessons from
  Urban Indonesia"): a City Blueprint Approach diagnostic governance-
  capacity assessment of Bandung, Indonesia, including discussion of the
  city's slum-area legalization policy providing informal-settlement
  residents legal tenure security and access to basic infrastructure, and
  governance-capacity gaps in wastewater statutory compliance/enforcement.
  Included for consistency with the same research group's companion City
  Blueprint paper already in the corpus (S172, Rahmasary et al. 2019, 11
  Asian cities). Extracted as **S494** (`risk_of_bias_tool = MMAT`,
  `mechanism_family = MULTIPLE` — `discretion_accommodation`,
  `enforcement`, `outcome_family = administrative_outcome`,
  `mechanism_certainty = 1`). Not added to `effect_sizes.csv` (standardized
  diagnostic indicator scores, not an inferential exposure-comparator
  estimate).

Duplicate audit (exact-DOI and record_id-in-extraction_note methods) came
back clean. `full_text_retrieval_queue.csv` regenerated (2,676 open
records). `validate_schemas.py` reports all 13 checked files match their
documented/generated schema.

## 2026-09-18 — Thirty-third full-text screening batch: 5 researcher-supplied PDFs, 4 excludes + 1 new include (S491)

The researcher uploaded five more PDFs directly via chat.

**Excludes:**

- **R033F9B44E40D** (Nkiaka, Bryant, Okumah & Gomo 2021, *WIREs Water*,
  "Water security in sub-Saharan Africa: Understanding the status of
  sustainable development goal 6"), **E01 wrong topic**: a 167-article
  systematic review assessing the status of ALL SDG6 targets (water
  quality, water stress, IWRM/transboundary management, ecosystems,
  climate change, conflict/migration, urbanization) across all 48 SSA
  countries; household-level water/sanitation access (§3.1) is only one of
  many sections, and the paper is not focused on the review's
  household-level legal-administrative connection/access mechanisms.
- **R5FC9426CBC4C** (Amayi 2021, *Environmental Challenges*, "Flower
  growing firms' contribution to community water use management in
  Naivasha Sub County, Kenya"), **E01 wrong topic**: a corporate
  social-responsibility/water-use-management study examining flower-firm
  water abstraction, waste-water disposal, and CSR frameworks relative to
  resident communities; no household-level legal-administrative
  service-connection mechanism content.
- **R4E01960E4669** (Sutomo, Sagala, Sutomo, Wrinarti & Sanjaya 2021,
  *Kesmas*, "Accelerating the provision of safe water supply in urban and
  rural areas of Indonesia"), **E05 no empirical evidence**: a narrative
  synthesis of Indonesia's historical water-coverage statistics and a
  "good water management" framework (content/institutional/communication
  layers), including slow-sand-filter engineering technology
  recommendations; no defined empirical study design, sample, or
  data-collection methodology.
- **R93A5FB34B8B7** (Koseoglu, Ellis & Biswas 2021, *Journal of Water,
  Sanitation and Hygiene for Development*, "Scenario-based life-cycle cost
  assessment to support sustainable investment in rural communal
  sanitation facilities: application to a school-based sanitation
  facility"), **E06 engineering only**: a scenario-based life-cycle cost
  assessment (LCCA) methodology paper modeling material/labour/energy
  costs for a school sanitation facility in rural India across
  valuation-capacity-external-support scenarios; an infrastructure
  cost-engineering methodology, not household-level legal-administrative
  eligibility/burden/discretion/enforcement mechanisms.

**Include:**

- **R2EE333D81F87** (Sempewo, Kisaakye, Mushomi, Tumutungire & Ekyalimpa
  2021, *Social Sciences & Humanities Open*, "Assessing willingness to pay
  for water during the COVID-19 crisis in Ugandan households"): a
  1,639-household binary logistic regression survey (40 small towns, 4
  regions of Uganda) set against Uganda's March 2020 presidential
  directive suspending all water disconnections for non-payment during the
  COVID-19 lockdown. 67% of households were not willing to pay for water
  during the lockdown; households without an existing formal
  payment relationship with the utility had roughly double the odds of
  unwillingness to pay (OR=2.125, 95% CI 1.581-2.857, p<0.001), with
  region, water-source location, and handwashing frequency as further
  significant predictors. Extracted as **S491** (`risk_of_bias_tool =
  JBI`, `mechanism_family = MULTIPLE` — `burden`,
  `discretion_accommodation`, `enforcement`, `outcome_family =
  economic_access`). **Added to `effect_sizes.csv`**: a genuine
  exposure-comparator (formal payment relationship vs. none) with OR, CI,
  p-value and N, tied directly to the disconnection-moratorium enforcement
  mechanism — meets the strict effect-size bar.

Duplicate audit (exact-DOI and record_id-in-extraction_note methods) came
back clean. `full_text_retrieval_queue.csv` regenerated (2,680 open
records). `validate_schemas.py` reports all 13 checked files match their
documented/generated schema.

## 2026-09-18 — Thirty-second full-text screening batch: 5 researcher-supplied PDFs, 2 excludes + 2 new includes (S489-S490)

The researcher uploaded five more PDFs directly via chat. One was a
duplicate re-upload of an already-decided record (Hove et al. 2022,
"Lessons from community participation in primary health care and water
resource governance in South Africa: a narrative review" — already excluded
E04, 2026-09-17) and was skipped without reprocessing.

**Excludes (both E01, wrong topic):**

- **R234D49848D7B** (Cai, Zhao & Varis 2021, *Journal of Cleaner
  Production*, "Match words with deeds: Curbing water risk with the
  Sustainable Development Goal 6 index"): a global composite SDG6 index
  constructed across 232 countries/territories using secondary aggregate
  national statistics. A macro cross-country index-construction/
  benchmarking exercise, no household-level legal-administrative mechanism
  content.
- **R7B70065EDFE6** (Dery, Bisung, Dickin & Atengdem 2021, *H2Open
  Journal*, "'They will listen to women who speak but it ends there':
  examining empowerment in the context of water and sanitation
  interventions in Ghana"): a 15-KII qualitative study of gender
  empowerment in WASH using Kabeer's empowerment framework. Focused on
  gender/social-norms dynamics; a single participant quote on rich-vs-poor
  connection disparity is incidental, not the paper's own focal
  contribution.

**Includes:**

- **R77DEA3810C24** (Koehler, Thomson, Goodall, Katuva & Hope 2021, *World
  Development*, "Institutional pluralism and water user behavior in rural
  Africa"): a 1,215-household/254-waterpoint multivariate logistic
  regression study (Kwale County, Kenya) finding households who consider
  their existing water supply costly have roughly half the odds of
  intending to contract a professional maintenance service provider
  (OR=0.532, SE=0.138, p=0.015), with regular payment systems, drinking
  use, and distance to the next handpump as further significant
  predictors. Extracted as **S489** (`risk_of_bias_tool = JBI`,
  `mechanism_family = MULTIPLE` — `burden`, `discretion_accommodation`,
  `outcome_family = economic_access`). **Added to `effect_sizes.csv`**: a
  genuine exposure-comparator (cost-concern) with OR, SE, p-value and N —
  meets the strict effect-size bar.
- **R3A151FC152B0** (Aliyev 2021, in *Resilience of Water Supply in
  Practice*, Ch. 9, "Economic resilience in water supply service in rural
  Tajikistan: A case study from Oxfam"): a practitioner case study
  documenting Tajikistan's Law on Drinking Water and Wastewater (N1633,
  2019), a blurred MEWR/SUE KMK regulatory boundary, cost-recovery
  tariff-setting through the Anti-Monopoly Agency, over 50 detected
  illegal connections, 74-349% operational-cost increases (2016-2020)
  across 3 Water User Associations, and unofficial district-government
  dismissal of WUA chairmen. Extracted as **S490**
  (`risk_of_bias_tool = MMAT`, `mechanism_family = MULTIPLE` — `burden`,
  `discretion_accommodation`, `enforcement`, `outcome_family =
  effective_access`). Not added to `effect_sizes.csv` (descriptive
  programme-monitoring KPI trends, no inferential exposure-comparator
  estimate).

Duplicate audit (exact-DOI groups, `record_id`-in-`extraction_note`
groups): clean, no duplicates found. Retrieval queue regenerated (2,685
open records). `validate_schemas.py`: all 13 checked files match their
documented/generated schema. Running totals updated in `README.md`,
`PRISMA_WORKFLOW.md`, `06_outputs/prisma/prisma_flow.md`, and
`06_outputs/supplementary/preliminary_results.md`: 974/3,659 full-text
screened (488 include / 486 exclude), 2,685 open, 488 studies fully
extracted (S001-S490, S227/S399 documented gaps), 186 quantitative- / 403
qualitative-synthesis-eligible in `evidence_map.csv`, 24 rows in
`effect_sizes.csv`.

## 2026-09-18 — Thirty-first full-text screening batch: 5 researcher-supplied PDFs, 3 excludes + 2 new includes (S487-S488)

The researcher uploaded five more PDFs directly via chat, all matching open
records by exact title:

**Excludes (all E01, wrong topic):**

- **R07C7E4C10649** (Bruns, Meisch, Ahmed, Meissner & Romero-Lankao 2022,
  *Geoforum*, "Nexus disrupted: Lived realities and the water-energy-food
  nexus from an infrastructure perspective"): a theoretical Political
  Ecology paper introducing a "heterogeneous infrastructure configuration"
  framework for the WEF-nexus, illustrated with 3 Sub-Saharan African
  vignettes spanning water+energy+food broadly; water/sanitation
  service-access legal-administrative content is incidental, not focal.
- **R9B3445F82EB1** (Pugel, Javernick-Will, Peabody et al. 2022, *Science
  of the Total Environment*, "Pathways for collaboratively strengthening
  water and sanitation systems"): an fsQCA of 11 donor/NGO/government
  collaborative WASH-program cases in Eastern Africa, identifying
  institutional/organizational conditions for program progress. A
  meta-level collaborative-governance program-design study, not a
  household-level legal-administrative connection-mechanism study.
- **RBADD83B9D09A** (Joshua, Tompkins, Schreckenberg, Ngongondo, Gondwe &
  Chiotha 2022, *Physics and Chemistry of the Earth*, "Water policy and
  resilience of potable water infrastructure to climate risks in rural
  Malawi"): a climate-resilience/infrastructure-vulnerability and
  rainfall-trend-analysis study evaluating water-policy effectiveness
  against flood/drought disaster preparedness; a single incidental
  borehole-fee/non-payment mention is not the paper's own focal
  legal-administrative-mechanism contribution.

**Includes:**

- **R9532479BE24C** (Kusi-Appiah & Mkandawire 2022, *Wellbeing, Space and
  Society*, "Political ecology of household water security among the
  urban poor in Malawi"): a 52-participant qualitative study (Mzuzu)
  finding exorbitant NRWB tariffs exclude/tenuously connect most poor
  residents, documenting service disconnection for late/non-payment,
  per-container fees at community water points, and government
  non-recognition of informal settlements as a structural connection-
  eligibility barrier, forcing reliance on exclusionary kinship/church
  networks for substitute access. Extracted as **S487**
  (`risk_of_bias_tool = CASP`, `mechanism_family = MULTIPLE` — `eligibility`,
  `burden`, `enforcement`, `outcome_family = economic_access`). Not added
  to `effect_sizes.csv` (qualitative thematic analysis with descriptive
  percentages only, no inferential exposure-comparator estimate).
- **R25608A5994D3** (Ahabwe, Batega, Ssewaya & Niwagaba 2022, *Journal of
  Water and Climate Change*, "Governance conundrum in pursuit of the
  human right to water and sanitation: tracking the progress of the
  leave-no-one-behind principle in Uganda"): a cross-sectional qualitative
  governance study (multi-category key-informant interviews plus
  structured legal/policy review) documenting Uganda's Constitution,
  Water Act Cap 152, Penal Code Act and NWSC pro-poor pre-paid-meter
  tariff structure against persistent implementation gaps — unregulated,
  "exorbitantly high" faecal-sludge fees outside Kampala, only 15% of key
  informants confirming poverty-based subsidies, and an unimplemented
  2015 World Bank tariff-overhaul recommendation. Extracted as **S488**
  (`risk_of_bias_tool = CASP`, `mechanism_family = MULTIPLE` —
  `eligibility`, `burden`, `discretion_accommodation`, `enforcement`,
  `outcome_family = effective_access`). Not added to `effect_sizes.csv`
  (qualitative content analysis and policy review, no inferential
  exposure-comparator estimate).

Duplicate audit (exact-DOI groups, `record_id`-in-`extraction_note`
groups): clean, no duplicates found. Retrieval queue regenerated (2,689
open records). `validate_schemas.py`: all 13 checked files match their
documented/generated schema. Running totals updated in `README.md`,
`PRISMA_WORKFLOW.md`, `06_outputs/prisma/prisma_flow.md`, and
`06_outputs/supplementary/preliminary_results.md`: 970/3,659 full-text
screened (486 include / 484 exclude), 2,689 open, 486 studies fully
extracted (S001-S488, S227/S399 documented gaps), 184 quantitative- / 402
qualitative-synthesis-eligible in `evidence_map.csv`, 23 rows in
`effect_sizes.csv` (unchanged this batch).

## 2026-09-18 — Thirtieth full-text screening batch: 5 researcher-supplied PDFs, 2 excludes + 3 new includes (S484-S486)

The researcher uploaded five more PDFs directly via chat, all matching open
records by exact title:

**Excludes (both E01, wrong topic):**

- **R00625C11FB19** (Munene & Hall 2022, *Environmental Health Insights*,
  "Proximity of Water Wells to Public Water Testing Facilities in Alberta
  Using Drive Times"): a GIS drive-time service-area analysis of 5,872
  private wells and 107 voluntary public water-quality testing facilities.
  Concerns access to a voluntary testing service, not water/sanitation
  service connection; does not satisfy inclusion criterion 1.
- **RECC0531CE044** (Mukwarami & Fakoya 2022, *Journal of Governance and
  Regulation*, "Causality relationship between sustainability factors and
  water management"): a Granger-causality panel study (8 South African
  metropolitan municipalities) of social/environmental/governance/economic
  determinants of municipal water investment. Macro municipal financial/
  governance econometrics, not a household-level legal-mechanism study.

**Includes:**

- **R570145F5F20F** (Monyai, Chivanga, Monyai & Ndlovu 2022, *Journal of
  Governance and Regulation*, "The Role of Communities in Innovative Water
  Management: Sustainability Governance in the Emerging Country"): a
  117-participant qualitative study (Mbizana and Ngwathe municipalities,
  South Africa) documenting weak enforcement of municipal by-laws against
  illegal water connections due to political complicity, nominal/top-down
  participation processes, and uncompensated pipeline-easement land
  disputes. Extracted as **S484** (`risk_of_bias_tool = CASP`,
  `mechanism_family = MULTIPLE` — `burden`, `discretion_accommodation`,
  `enforcement`, `outcome_family = effective_access`).
- **R394E198B902C** (Dektar, McConnell & Kasekende 2022, *Water Policy*,
  "Exploratory assessment of challenges and issues with private water
  operators in rural water supply and service delivery: a case study of
  the Karamoja region, Uganda"): a qualitative case study across 4 rural
  schemes documenting weak enforcement of tariff/regulatory policy,
  bureaucratic tariff-approval delays, and risky payment-in-kind/loan
  tariff arrangements. Extracted as **S485** (`risk_of_bias_tool = CASP`,
  `mechanism_family = MULTIPLE` — `burden`, `enforcement`, `outcome_family
  = effective_access`).
- **R9860C906C24C** (Calderón-Villarreal et al. 2022, *Social Science &
  Medicine*, "Deported, homeless, and into the canal: Environmental
  structural violence in the binational Tijuana River"): a binational
  mixed-methods study (85-respondent survey, ethnography, water testing)
  of deported/homeless residents of the Tijuana River canal, documenting
  ID/documentation-based hospital-eligibility barriers, fee-conditioned
  private sanitation access, and police raids forcing contact with
  contaminated water. Extracted as **S486** (`risk_of_bias_tool = MMAT`,
  `mechanism_family = MULTIPLE` — `eligibility`, `burden`, `enforcement`,
  `outcome_family = effective_access`).

Neither S484, S485 nor S486 was added to `effect_sizes.csv`: S484 and S485
are qualitative case studies with no inferential exposure-comparator
estimate; S486 reports a real OR (skin infection ~ river-water contact,
OR=2.3, 95% CI 1.2-5.3) but this is a health-outcome epidemiological
finding, not an estimate tied to a legal/administrative access mechanism,
so it falls outside this review's effect-size scope.

Duplicate audit (exact-DOI groups, `record_id`-in-`extraction_note`
groups): clean, no duplicates found. Retrieval queue regenerated (2,694
open records). `validate_schemas.py`: all 13 checked files match their
documented/generated schema. Running totals updated in `README.md`,
`PRISMA_WORKFLOW.md`, `06_outputs/prisma/prisma_flow.md`, and
`06_outputs/supplementary/preliminary_results.md`: 965/3,659 full-text
screened (484 include / 481 exclude), 2,694 open, 484 studies fully
extracted (S001-S486, S227/S399 documented gaps), 184 quantitative- / 400
qualitative-synthesis-eligible in `evidence_map.csv`, 23 rows in
`effect_sizes.csv` (unchanged this batch).

## 2026-09-18 — Twenty-ninth full-text screening batch: 8 researcher-supplied PDFs, 5 excludes + 2 new includes (S482-S483)

The researcher uploaded eight more PDFs directly via chat. One was a
duplicate re-upload of an already-decided record (Beyene, Adam & Minale
2023, "Examining the practice of urban governance using UN-Habitat urban
governance index in Gondar city, North West Ethiopia" — already S401,
extracted 2026-09-17) and was skipped without reprocessing.

**Excludes (all E01, wrong topic):**

- **RCDD2A6F242AA** (Nlunda, Matumona, Numbi, Kapenga & Mbela 2023, *J.
  Water, Sanitation and Hygiene for Development*, "Peri-urban schools of
  Kinshasa before and during COVID-19"): a school WASH-infrastructure/
  hand-hygiene-behavior evaluation among adolescent girls, no legal/
  administrative connection-mechanism content.
- **R0AFD77B3C677** (Cassivi, Covey, Rodriguez & Guilherme 2023,
  *International Journal of Hygiene and Environmental Health*, "Domestic
  water security in the Arctic: A scoping review"): the review's own
  PRISMA-ScR eligibility criteria explicitly exclude "studies addressing
  water-related issues from a governance, law or policy perspective" —
  precisely this review's target content.
- **RF37B79776186** (Bankole, James, Odjegba, Bankole, Emmanuel, Fiore, Pu
  & Moruzzi 2023, *Water Policy*, "Factors affecting sanitation coverage in
  three income levels and potential toward achieving SDG 6.2"): a
  cross-country Sanitation Coverage Index benchmarking study; Nigeria's
  funding/institutional-responsibility narrative is background context, not
  the paper's own empirical household-level finding.
- **R924147005E03** (Mukwarami & van der Poll 2023, *J. Governance and
  Regulation*, "Analysis of the relationship between social factors and
  water services delivery in the public sector"): a 20-municipality panel
  econometric study of social/political determinants of aggregate water
  investment/access rate in South Africa.
- **R48E6D809E739** (Jaren, Leya & Mondal 2022, *Water*, "Investigation of
  Gender-Differentiated Impacts of Water Poverty on Different Livelihood
  Groups in Peri-Urban Areas around Dhaka, Bangladesh"): a gender-
  differentiated Water Poverty Index study focused on socioeconomic/
  physical/gender barriers (distance, time burden, capacity), not a
  specific legal/administrative connection-eligibility, burden, discretion
  or enforcement mechanism.

**Includes:**

- **R97CEDDF99259** (Meehan, Beresford, Amador Cid, Avelar Portillo, Marin,
  Odetola & Pacheco-Vega 2023, *WIREs Water*, "Homelessness and water
  insecurity in the Global North: Trapped in the dwelling paradox"): a
  conceptual synthesis on how private-home-based water/sanitation
  provision structurally excludes unhoused people, citing named UK
  anti-homeless statutes (Anti-Social Behaviour, Crime and Policing Act
  2014; Police, Crime, Sentencing and Courts Act 2022) criminalizing the
  resulting public urination/defecation and encampments. Extracted as
  **S482** (`risk_of_bias_tool = AMSTAR2`, `mechanism_family = MULTIPLE` —
  `eligibility`, `discretion_accommodation`, `enforcement`, `outcome_family
  = effective_access`). Not added to `effect_sizes.csv` (conceptual
  synthesis, no quantitative exposure-comparator estimate).
- **R8FA145CC6D69** (Mutono, Wright, Mutembei & Thumbi 2022, *Habitat
  International*, "Spatio-temporal patterns of domestic water distribution,
  consumption and sufficiency: Neighbourhood inequalities in Nairobi,
  Kenya"): an 11-year utility panel study (2,380 water-distribution
  itineraries) finding residents of high-income Nairobi areas six times more
  likely to receive sufficient water than low-income residents (rate ratio
  5.78, 95% CI 5.34-6.25, p<0.001), tied to connection-type disparities
  (inhouse piped vs. shared taps/water kiosks) and a tenure-security gap
  (85% vs. 58%). Extracted as **S483** (`risk_of_bias_tool = ROBINS-I`,
  `mechanism_family = MULTIPLE` — `eligibility`, `burden`, `outcome_family
  = effective_access`). **Added to `effect_sizes.csv`**: a genuine
  exposure-comparator (residential income category) with rate ratios, 95%
  CIs, p-values and N — meets the strict effect-size bar.

Duplicate audit (exact-DOI groups, `record_id`-in-`extraction_note`
groups): clean, no duplicates found. Retrieval queue regenerated (2,699
open records). `validate_schemas.py`: all 13 checked files match their
documented/generated schema. Running totals updated in `README.md`,
`PRISMA_WORKFLOW.md`, `06_outputs/prisma/prisma_flow.md`, and
`06_outputs/supplementary/preliminary_results.md`: 960/3,659 full-text
screened (481 include / 479 exclude), 2,699 open, 481 studies fully
extracted (S001-S483, S227/S399 documented gaps), 183 quantitative- / 397
qualitative-synthesis-eligible in `evidence_map.csv`, 23 rows in
`effect_sizes.csv`.

## 2026-09-18 — Twenty-eighth full-text screening batch: 10 researcher-supplied PDFs, 7 excludes + 2 new includes (S480-S481)

The researcher uploaded ten more PDFs directly via chat. One was a duplicate
re-upload of an already-decided record (Brown et al. 2023, *Lancet Global
Health*, "The effects of racism, social exclusion, and discrimination on
achieving universal safe water and sanitation in high-income countries" —
already S418, extracted 2026-09-17) and was skipped without reprocessing.

**Excludes (all E01, wrong topic):**

- **RF88313EC8B9F** (Gandidzanwa, Togo & Mawonde 2024, *Water Supply*,
  "Water–energy network provisioning services in Harare, Zimbabwe"): a
  314-household WEF-nexus reliability/governance-perception survey framed
  through collective-action theory, no legal/administrative connection-
  mechanism content.
- **REF486158BFC4** (Masiya, Hall, Murray, Etter-Phoya, Hannah & O'Hare
  2024, *Sustainable Development*, "Tax expenditures and progress to the
  Sustainable Development Goals"): a 97-country macro fiscal-policy
  simulation, no household-level or institutional legal-mechanism analysis.
- **RDD3426650476** (Mabadahanye, Dalu, Munyai, Dondofema & Dalu 2024,
  *Sustainability*, "Institutional Arrangements and Roles within Water and
  Wastewater Treatments in the Vhembe District, South Africa"): a
  plant-worker/utility-operations institutional-capacity study.
- **RFD88555FDAE3** (Hopkins & Sowby 2024, *Water*, "A Qualitative
  Definition of Reliable Water Supply for Public Water Systems"): a
  utility-level water-supply-reliability planning-definition study.
- **R9426D15C50ED** (Cabrera Barbecho & Sarmiento 2023, *Sustainability*,
  "Exploring Technical Efficiency in Water Supply Evidence from Ecuador"):
  a DEA double-bootstrap utility technical-efficiency benchmarking study.
- **R9625C2C2538C** (Zarepour Moshizi, Yousefi, Amini & Shojaei 2023,
  *GeoJournal*, "Rural vulnerability to water scarcity in Iran"): an
  agricultural/irrigation water-scarcity vulnerability study, not household
  drinking-water/sanitation service access.
- **R96D0E77D69DF** (Narzetti, Pinto, Narzetti & Cetrulo 2023, *Water*,
  "Reaching Universal Coverage of Water and Sanitation Services: Is
  Regionalization a Sustainable Path for Developing Countries?"): a WSS
  utility-regionalization financial-feasibility study (Santa Catarina,
  Brazil); household affordability appears only as a top-down financial-
  model projection metric, not an empirical household-level finding.

**Includes:**

- **R95B9BD41525A** (Maxcy-Brown, Wilson, Chai, McCaskill, Bakchan,
  Christian, Barnett, Elliott & White 2024, *J. Sustainable Water in the
  Built Environment*, "The Past, Present, and Future of Wastewater
  Management in Alabama's Black Belt"): NPDES compliance-data analysis
  across 59 facilities (37.3% average noncompliance) combined with a legal/
  policy review of homeowner OWTS-permitting responsibility, regulatory
  enforcement history (consent decrees, court actions), and federal
  funding programs structurally favoring utilities over individual
  households. Extracted as **S480** (`risk_of_bias_tool = AMSTAR2`,
  `mechanism_family = MULTIPLE` — `eligibility`, `burden`, `enforcement`,
  `outcome_family = effective_access`). Not added to `effect_sizes.csv`
  (descriptive compliance-rate analysis, no inferential exposure-comparator
  estimate).
- **R86567443C17D** (Machado, Oliveira, Matos & Santos 2023, *Water*,
  "Strategies for Achieving Sustainability of Water Supply Systems in Rural
  Environments with Community Management in Brazil"): an 11-specialist
  Delphi-style expert-panel evaluation of legal/institutional strategies
  for rural community-managed water supply, covering national legal
  frameworks (Laws 11.445 and 14.026), municipal-community legal
  instruments, and payment-capacity-based tariffs with default-driven
  service cuts. Extracted as **S481** (`risk_of_bias_tool = MMAT`,
  `mechanism_family = MULTIPLE` — `eligibility`, `burden`, `discretion_
  accommodation`, `enforcement`, `outcome_family = effective_access`). Not
  added to `effect_sizes.csv` (descriptive expert-panel voting counts, no
  inferential exposure-comparator estimate).

Duplicate audit (exact-DOI groups, `record_id`-in-`extraction_note`
groups): clean, no duplicates found. Retrieval queue regenerated (2,706
open records). `validate_schemas.py`: all 13 checked files match their
documented/generated schema. Running totals updated in `README.md`,
`PRISMA_WORKFLOW.md`, `06_outputs/prisma/prisma_flow.md`, and
`06_outputs/supplementary/preliminary_results.md`: 953/3,659 full-text
screened (479 include / 474 exclude), 2,706 open, 479 studies fully
extracted (S001-S481, S227/S399 documented gaps), 182 quantitative- / 396
qualitative-synthesis-eligible in `evidence_map.csv`, 22 rows in
`effect_sizes.csv` (unchanged this batch).

## 2026-09-18 — Twenty-seventh full-text screening batch: 7 researcher-supplied PDFs, 2 excludes + 2 new includes (S478-S479)

The researcher uploaded seven more PDFs directly via chat. Three were
duplicate re-uploads or wrong-file retrievals of already-decided records
and were skipped without reprocessing: D'Odorico, Dell'Angelo & Rulli's
"Appropriation pathways of water grabbing" (already excluded E01,
2026-09-17), Sisay, Gari & Ambelu's Addis Ababa fecal-sludge/sanitation-
safety study (already S463, 2026-09-17), and a third delivery of the wrong
chapter for record R81549C4709FC (Singh & Singh, ch.18, "Building
Political Capabilities... Kathmandu") — confirmed via full-text read as the
same Sherpa/Awale chapters already documented in that record's
`wrong_file_retrieved` note; still open pending correct retrieval.

**Excludes:**

- **R3E54D7DA6A1A** (Wiechman, Alonso Vicario, Anderies, Garcia, Azizi &
  Hornberger 2024, *Water Resources Research*, "Institutional Dynamics
  Impact the Response of Urban Socio-Hydrologic Systems to Supply
  Challenges"): a conceptual dynamical-systems model (UWIIM) of utility-
  level investment/rate-setting/curtailment institutional friction in
  three stylized Phoenix Metro cities, explicitly not intended to predict
  real-city outcomes. Excluded **E01 (wrong topic)**.
- **R6F531D59E896** (Jaffee 2024, *WIREs Water*, "Unequal trust: Bottled
  water consumption, distrust in tap water, and economic and racial
  inequality in the United States"): a focus-article review of bottled-
  water consumption/trust patterns by race and income. Excluded **E04
  (wrong outcome)**: the article's own focal contribution is bottled-water
  consumption/trust perception, not formal connection/effective access/
  economic access/administrative outcomes; its Box 1 on water-affordability
  and shutoffs is a boxed aside summarizing other cited studies, not this
  paper's own empirical content.

**Includes:**

- **RCA5D7CE8A750** (Albright, Coleman Flowers, Kramer & Weinthal 2024,
  *Local Environment*, "Failing septic systems in Lowndes County, Alabama:
  citizen participation, science, and community knowledge"): a 294-
  household survey documenting legal enforcement (fines/arrests under
  Alabama's sanitation code since 2002 for failing septic systems in a
  county with impermeable clay soils), prohibitive installation costs
  ($6,000-$30,000), and a 2023 US DOJ/HHS interim environmental-justice
  agreement requiring sanitation access regardless of ability to pay and
  suspending punitive enforcement. Extracted as **S478**
  (`risk_of_bias_tool = JBI`, `mechanism_family = MULTIPLE` — `burden`,
  `discretion_accommodation`, `enforcement`, `outcome_family =
  effective_access`). Not added to `effect_sizes.csv`: a descriptive survey
  and legal/institutional case narrative, no inferential exposure-
  comparator estimate.
- **R0B3058C4EC24** (Dobbin, Hernandez, Bostic, Harrison, Singhal, Barnett,
  Vasquez-Rodriguez, Pierce & Sawyer 2024, *WIREs Water*, "Making a vicious
  cycle virtuous: A research and policy agenda for advancing the water
  security of unregulated users in the Southwestern U.S."): a narrative
  review of the regulatory/assistance-program landscape for ~2.5 million
  federally unregulated water users (domestic wells, very small systems,
  hauled water) across 7 Southwestern US jurisdictions, documenting
  inconsistent statutory definitions, a USDA owner-occupancy eligibility
  rule excluding renters, and Navajo Nation watering-point fees suspended
  under IHS CARES Act funding. Extracted as **S479**
  (`risk_of_bias_tool = AMSTAR2`, `mechanism_family = MULTIPLE` —
  `eligibility`, `burden`, `outcome_family = effective_access`). Not added
  to `effect_sizes.csv`: a narrative policy-landscape review, no single
  quantitative exposure-comparator estimate.

Duplicate audit (exact-DOI groups, `record_id`-in-`extraction_note`
groups): clean, no duplicates found. Retrieval queue regenerated (2,715
open records). `validate_schemas.py`: all 13 checked files match their
documented/generated schema. Running totals updated in `README.md`,
`PRISMA_WORKFLOW.md`, `06_outputs/prisma/prisma_flow.md`, and
`06_outputs/supplementary/preliminary_results.md`: 944/3,659 full-text
screened (477 include / 467 exclude), 2,715 open, 477 studies fully
extracted (S001-S479, S227/S399 documented gaps), 182 quantitative- / 394
qualitative-synthesis-eligible in `evidence_map.csv`, 22 rows in
`effect_sizes.csv` (unchanged this batch).

## 2026-09-18 — Twenty-sixth full-text screening batch: 9 researcher-supplied items, 7 excludes + 2 new includes (S476-S477)

The researcher uploaded nine more items directly via chat (eight PDFs plus
one Google Drive-shared PDF), all matching open records by exact title
(two were duplicate re-uploads of already-decided/extracted records —
Beker & Kansal 2023 Ethiopia UDWS, already S449, and Araújo et al. 2024
Federal District of Brazil water-equity study, already S462 — both
verified by title/DOI match and skipped without reprocessing):

**Excludes:**

- **RA87C32E58A64** (Ijioma, Ijioma & Herd 2025, *Water Practice &
  Technology*, "Assessment of quality and health risks in drinking water
  sources in Aba, Nigeria"): Water Safety Plan chemical/bacteriological
  risk assessment. Excluded **E03 (wrong exposure)**: water-quality/health-
  risk focus, no household-level legal-administrative connection mechanism
  content despite a general discussion of environmental-law enforcement.
- **RA9D46FF2372C** (Ati, Satpathy & Saxena 2024, *Water Policy*,
  "Perceived public service performance, trust in the government, and
  citizens' willingness to participate: Evidence from water governance in
  Visakhapatnam, India"): household survey on trust/participation among
  already-connected households. Excluded **E01 (wrong topic)**: a
  political-trust/civic-participation study, not focused on legal/
  administrative connection eligibility, burden, discretion or enforcement.
- **RAEA95650888A** (Zhalil & Duishebaeva 2024, *BIO Web of Conferences*,
  "Strengthening the human resource potential as a basis for the
  development of the potable water supply and disposal sector of the
  Kyrgyz Republic"): a vocational-training program proposal for utility
  workers. Excluded **E01 (wrong topic)**: no household-level empirical
  legal-administrative access-mechanism content.
- **RD59389822173** (Nono, Mvongo & Defo 2024, *Water Supply*, "Assessment
  of non-revenue water in the urban water distribution system network in
  Cameroon"): IWA-methodology water-loss/leak-detection engineering
  assessment. Excluded **E06 (engineering only)**.
- **R0C221D09D4AD** (García-López, Cuadrado-Quesada & Montano 2024,
  *Sustainable Development*, "Untangling the vicious cycle around water and
  poverty"): cross-country 2SLS econometric analysis of water access, GDP
  and human capital using aggregate JMP/FAO/World Bank statistics. Excluded
  **E01 (wrong topic)**: macro development-economics study, no household-
  level or institutional legal-mechanism analysis.
- **R561806D16CAB** (Zambrano-Alvarado & Uyaguari-Diaz 2024, *PeerJ*,
  "Insights into water insecurity in Indigenous communities in Canada:
  assessing microbial risks and innovative solutions, a multifaceted
  review"): a microbiology/water-treatment technology review. Excluded
  **E03 (wrong exposure)**: the authors explicitly restrict their own
  review's scope to "technical and microbiological issues," acknowledging
  but excluding legal/governance analysis.
- **R6D780116D575** (Grant & Willetts 2024, *Water*, "Locally Led
  Opportunities for Water, Sanitation and Hygiene, Climate Change and
  Gender Equality Partnerships in the Blue Pacific"): a systematic scoping
  review of WASH/climate/gender civil-society coalitions and localism
  discourse. Excluded **E01 (wrong topic)**: no legal/administrative
  connection-mechanism content.

**Includes:**

- **RBB6F3EAC4B2C** (Khan & Fenner 2024, *Water*, "Socio-Demographic
  Factors Driving the Choice of Alternative Safe Water Sources and Their
  Implications for Public Health: Lessons from Goalmari, Bangladesh"): a
  220/415-household baseline/endline survey finding that Veolia's 5,000 BDT
  upfront internal-connection fee, combined with the shutdown of nearby
  community tap points to consolidate demand, drove low-income households
  toward unsafe alternative water sources (ANOVA p=0.0004057). Extracted as
  **S476** (`risk_of_bias_tool = JBI`, `mechanism_family = BURDEN`,
  `outcome_family = economic_access`). Not added to `effect_sizes.csv`: the
  reported statistic is a bare ANOVA p-value with no coefficient/OR/
  correlation magnitude or CI, below the strict effect-size bar.
- **R63EA69FC6367** (Di Giovanni & Bercovich, eds., 2025, *Legal
  Empowerment in Informal Settlements: Grassroots Experiences in the Global
  South*, Routledge, retrieved via Google Drive share): a 12-chapter,
  10-country edited volume of grassroots legal-empowerment case studies.
  Extraction centers on Chapter 5 (Ouma, Njoroge & Weru, "Innovating
  participation to expand water and sanitation access under a special
  planning area in Mukuru informal settlements, Nairobi"), the volume's
  most directly on-topic and quantified case: Mukuru's 2017 declaration as
  a Special Planning Area under Kenya's Physical Planning Act, a documented
  "poverty penalty" (172% more per m³ for water than formal Nairobi
  estates), and co-produced simplified-sewer/prepaid-water-dispenser
  infrastructure reaching ~12,000 households, with a KES 5,000 connection
  fee found prohibitive and requiring a micro-loan facility. Extracted as
  **S477** (`risk_of_bias_tool = CASP`, `mechanism_family = MULTIPLE` —
  `burden` and `discretion_accommodation`, `outcome_family =
  effective_access`). Not added to `effect_sizes.csv`: a qualitative case
  study with descriptive settlement-level counts, no inferential
  exposure-comparator estimate. Other chapters of the volume (housing/
  tenure/eviction case studies in Delhi, Accra, Rio, Buenos Aires,
  Karachi, Dhaka, Manila and South Africa) were not separately extracted,
  as noted in the `extraction_note`.

Duplicate audit (exact-DOI groups, `record_id`-in-`extraction_note`
groups): clean, no duplicates found. Retrieval queue regenerated (2,719
open records). `validate_schemas.py`: all 13 checked files match their
documented/generated schema. Running totals updated in `README.md`,
`PRISMA_WORKFLOW.md`, `06_outputs/prisma/prisma_flow.md`, and
`06_outputs/supplementary/preliminary_results.md`: 940/3,659 full-text
screened (475 include / 465 exclude), 2,719 open, 475 studies fully
extracted (S001-S477, S227/S399 documented gaps), 182 quantitative- / 392
qualitative-synthesis-eligible in `evidence_map.csv`, 22 rows in
`effect_sizes.csv` (unchanged this batch).

## 2026-09-18 — Twenty-fifth full-text screening batch: 1 researcher-supplied PDF, 1 new include (S475)

The researcher uploaded one more PDF directly via chat, matching an open
record by exact title, read in full (35 pages):

- **RA6A88199324A** (Murebwayire, Nilsson, Nhapi & Wali 2025, *Sustainability*
  17(17):7588, "A Systematic Review of Households' Fecal Sludge Management
  Situation to Identify Gaps and Improve Services: A Case of Kigali City,
  Rwanda"): **Included.** A PRISMA 2020 systematic review of 73 publications
  (36 scientific studies + 32 government/policy documents) on household-level
  fecal sludge management in Kigali, organized around four themes (access to
  sanitation, FSM services, public health, sanitation governance). Directly
  reviews 23 government publications (laws, national strategies, regulations,
  policies, standards, guidelines) and documents institutional fragmentation
  across overlapping mandates (national ministries, WASAC, City of
  Kigali/district authorities, private FSM operators), regulatory/building-law
  approval requirements for on-site sanitation that are seldom enforced in
  practice, authorities prioritizing sanctions over supportive regulatory
  mechanisms, and recurring tenant-landlord disputes over pit-latrine
  construction/maintenance responsibility, against a documented USD 316
  million annual WASH-sector funding gap (only ~7% of budget to sanitation).
  Extracted as **S475**, `risk_of_bias_tool = AMSTAR2` (systematic review,
  design-matched per `RISK_OF_BIAS.md` §1; `study_design_class` mechanically
  derives to `systematic_review_secondary`), `mechanism_family = MULTIPLE`
  (`burden`, `discretion_accommodation`, `enforcement` all TRUE),
  `outcome_family = effective_access`. Not added to `effect_sizes.csv`: a
  thematic/narrative secondary synthesis across 73 heterogeneous sources, not
  a single exposure-vs-comparator quantitative estimate.

Duplicate audit (exact-DOI groups, `record_id`-in-`extraction_note` groups):
clean, no duplicates found. Retrieval queue regenerated (2,728 open records).
`validate_schemas.py`: all 13 checked files match their documented/generated
schema. Running totals updated in `README.md`, `PRISMA_WORKFLOW.md`,
`06_outputs/prisma/prisma_flow.md`, and
`06_outputs/supplementary/preliminary_results.md`: 931/3,659 full-text
screened (473 include / 458 exclude), 2,728 open, 473 studies fully
extracted (S001-S475, S227/S399 documented gaps), 181 quantitative- /
390 qualitative-synthesis-eligible in `evidence_map.csv`, 22 rows in
`effect_sizes.csv` (unchanged this batch).

## 2026-09-18 — Twenty-fourth full-text screening batch: 4 researcher-supplied PDFs, 2 excludes + 2 new includes (S473-S474)

The researcher uploaded four more PDFs directly via chat, all matching
existing open records by exact title, all read in full:

**Excludes:**

- **R647969B935A4** (Bolatova, Sharapatova, Kanagat, Kabiyev, Berndtsson &
  Tussupova 2025, *Sustainability*, "Household Satisfaction and Drinking
  Water Quality in Rural Areas: A Comparison with Official Access Data"):
  multinomial logistic regression (n=1,361, 86 villages, Atyrau Region,
  Kazakhstan) identifying predictors of household satisfaction with
  drinking water QUALITY (turbidity, taste, odor, supply interruptions),
  also comparing official vs. field-reported connection statistics.
  Excluded **E03 (wrong exposure)**: core outcome is water-quality
  satisfaction/perception, not the legal/administrative mechanisms of
  connection eligibility, burden, discretion, or enforcement this review
  targets — no discussion of land tenure, connection fees, eligibility
  criteria, or service-provider governance barriers.
- **R0FD21DF7787A** (Omalanga & Onyari 2025, *Limnol. Rev.*, "Management of
  Water Resources in South Africa: A Systematic Review"): a systematic
  review of 60 articles (2011-2025) spanning agricultural/industrial water
  allocation, climate change, urbanization, funding, water quality/
  biostability, and technological innovation. Excluded **E01 (wrong
  topic)**: a general water-RESOURCE-management review, not focused on the
  legal/administrative mechanisms of household/community water-SERVICE
  access this review targets.

**New includes:**

- **S473** (`R262744119C0D`, Nyambwe, Kulimushi Matabaro, Mulengezi
  Mushegerha, Kashinzwe Kibekenge, Bukenya & Nzukizi Mudumbi 2025, *Urban
  Science*, "Urban Sprawl and Drinking Water Services in an African City:
  The Case of Bukavu in DR Congo"): 655-household survey plus diachronic
  GIS analysis (1984-2024) finding distance from city center significantly
  negatively correlates with drinking-water coverage (r=-0.42, p<0.05) and
  very strongly correlates with collection time (r=0.963); land tenure
  insecurity (29.74% of households lack formal titles) concentrates poor
  REGIDESO connection in informal peripheral neighborhoods (74% title-less
  vs. 68% citywide periphery), with tenants reporting disconnection
  disputes over unpaid water bills. Not added to `effect_sizes.csv` — the
  correlational findings are geographic/spatial (distance-based) rather
  than a clean legal/institutional exposure-comparator contrast.
- **S474** (`R8750FBD0FA97`, Kehinde, Schuster-Wallace, Fowler & Bharadwaj
  2025, *J. Water Health*, "Weaving knowledge systems to eradicate drinking
  water crises in First Nations across Canada"): mixed-methods study of
  Canada's federal Long-Term Drinking Water Advisory (LTDWA) response —
  CA$598 million invested across 149 infrastructure projects (2016-2022,
  55% concentrated in Ontario alone), yet 38 LTDWAs remained in 30 First
  Nations as of July 2025 (some over two decades old). Finds the federal
  risk-based funding formula (CFMP) prioritizes infrastructure technology
  while allocating under 0.1% combined to operator training and
  source-water protection, and qualitative interviews document
  jurisdictional fragmentation, inconsistent operator-certification access
  across provinces, and exclusion of First Nations water principles and
  self-determination from the funding design. Not added to
  `effect_sizes.csv` — descriptive government-expenditure data with no
  inferential statistical test or exposure-comparator contrast.

Full-text screening now stands at 930/3,659 (472 include / 458 exclude),
2,729 open in the regenerated retrieval queue. `extraction_database.csv`
and `evidence_map.csv` both grew to 472 rows; `effect_sizes.csv` unchanged
at 22 rows. Duplicate audit (exact DOI, record_id-in-extraction_note) came
back clean. `validate_schemas.py` passes all 13 checked files.

## 2026-09-18 — Twenty-third full-text screening batch: 3 researcher-supplied PDFs, 1 duplicate re-upload, 1 exclude, 1 new include (S472)

The researcher uploaded three more PDFs directly via chat. One
(Frempong et al. 2025, mining activities and water security in Ghana) was a
redundant re-upload of a record already screened, included, and extracted
as S434 in an earlier batch (verified by title/authors match against
`full_text_screening_database.csv` and `extraction_database.csv` before
taking any action) — no reprocessing needed. The other two matched open
records and were read in full:

- **R3A98EF381592** (Vij & Narain 2025, *WIREs Water*, "Neglected Spaces or
  Potential Grounds? Water (In)security and Climate Adaptation in
  Peri-Urban Asia and Africa"): a systematic literature review (57
  articles) of peri-urban climate-change adaptation and water (in)security,
  thematically organized around vulnerability of peri-urban agriculture,
  barriers/enablers to adaptation planning, and disaster/climate justice.
  Excluded **E01 (wrong topic)**: a water-resource/climate-security review
  unrelated to household or community water/sanitation SERVICE
  connection, eligibility, or access (`INCLUSION_EXCLUSION.md` exclusion
  criterion 7) — the review's scope is climate vulnerability and adaptation
  broadly (agriculture, land, disaster governance), not the legal/
  administrative mechanisms of service access this review targets.
- **R01D34FC853D2** (Lopez, Ofori, Mdee & Llaxacondor 2025, *J. Water
  Sanitation Hyg. Dev.*, "Does container-based sanitation align with
  sanitation sectoral planning in Lima?"): **included as S472.** Qualitative
  case study (26 interviews) of container-based sanitation (CBS) in
  Pamplona Alta, an informal settlement complex in Lima, Peru, where 92% of
  ~12,300 households lack a sewer connection. Finds that Lima's fragmented
  sanitation sectoral regime (SEDAPAL, SUNASS, municipalities, MVCS) and a
  legal prohibition (Legislative Decree No. 1280) barring ecological-
  sanitation organizations from providing sewerage, wastewater treatment,
  or sanitary disposal services obstructs scaling CBS despite high social
  acceptability among ~7,000 users; state service delivery is formally
  conditioned on legal title deeds, structurally excluding informal
  residents; CBS is treated by all parties as a temporary stopgap pending
  conventional sewerage that may never arrive. Not eligible for
  `effect_sizes.csv` (qualitative design, no statistical effect estimate).

Full-text screening now stands at 926/3,659 (470 include / 456 exclude),
2,733 open in the regenerated retrieval queue. `extraction_database.csv`
and `evidence_map.csv` both grew to 470 rows; `effect_sizes.csv` unchanged
at 22 rows. Duplicate audit (exact DOI, record_id-in-extraction_note) came
back clean. `validate_schemas.py` passes all 13 checked files.

## 2026-09-18 — Twenty-second full-text screening batch: 4 researcher-supplied PDFs, 2 excludes + 2 new includes (S470-S471)

The researcher uploaded four PDFs directly via chat over the course of this
batch. All four matched existing open records in
`full_text_screening_database.csv` by exact title, all four were read in
full; two were excluded and two were included and extracted.

**Excludes:**

- **R4590CBC940E4** (Garrett, Mok, Brown, Schaider, Powers, Fitzstevens,
  Amico, Osimo, Cordner & Carignan 2025, *J. Environ. Stud. Sci.*,
  "REACHing for PFAS solutions: how two communities responded to drinking
  water contamination"): qualitative CBPR case-study comparison of two US
  communities (Hyannis, MA and Pease Tradeport, Portsmouth, NH) discovering
  PFAS drinking-water contamination, covering community activism, blood
  testing, and government/legal response (state and federal MCL adoption,
  a 3M-v.-NH-DES lawsuit, DoD immunity claims in PFAS litigation,
  insurance-coverage legislation). Excluded **E03 (wrong exposure)**: the
  paper's focus is water-quality contamination discovery and response, not
  the legal/administrative mechanisms of household connection, eligibility,
  or service access this review targets — a water-quality-only study,
  consistent with the project's established E03 pattern.
- **R4DB61161A41A** (Kwame, Siiba, Apatinga & Owusu 2025, *Nurs. Rep.*,
  "Water (In)Accessibility, Healthcare Delivery, and Patients' Health
  Outcomes in Ghana: Perspectives from the Yendi Hospital"): ethnographic
  qualitative study (43 interviews + participant observation + 1 focus
  group) of how intermittent institutional water supply at one Ghanaian
  hospital affects missed medical reviews, admission refusal, and
  nurse-patient-caregiver relationship quality. Excluded **E02 (wrong
  population)**: the population/setting is institutional healthcare-facility
  water provision (patients, caregivers, and nurses within a single
  hospital), not household/community water or sanitation service access —
  directly analogous to the prior E02 exclusion of Ayalew et al. 2025
  ("Beyond access: assessing WASH service delivery models in healthcare
  facilities...", `RF2AF386D1E6D`).

**New includes:**

- **S470** (`RE42F8D320487`, Amorim, Resende, Miranda & Freistadt 2025,
  *Water Policy* 27(11):1153-1174, "The effect of the regulation and
  regulatory enforcement on the implementation of the social tariff in the
  water sector: empirical evidence from Brazil"): panel-data study of 572
  Minas Gerais municipalities (Copasa-MG service area) testing whether a
  2021 regulatory norm and periodic inspections by the state economic
  regulator (Arsae-MG) increased implementation of an income-eligibility
  social tariff, measured via a Degree of Implementation of the Social
  Tariff (DIST) Index. Random-effects panel regression finds a ~19
  percentage-point increase in implementation associated with regulatory
  enforcement (p<0.01, all 3 model specifications), corroborated by
  Wilcoxon signed-rank tests significant in all 11 macro-regions; a
  robustness-check panel extended back to 2018 finds a smaller but still
  significant ~13 percentage-point effect. A genuine quasi-experimental
  before/after estimate (no counterfactual group exists, since the
  regulatory change was statewide) — added to `effect_sizes.csv`.
- **S471** (`R90BA49D542B6`, Hughes, Kirchhoff, Lee & Switzer 2025, *AWWA
  Water Science* 7(1):e70014, "Understanding the Cost of Basic Drinking
  Water Services in the United States: A National Assessment"): national
  cross-sectional OLS study (2,119 US municipalities, state fixed effects)
  of the fiscal, community, organizational, and environmental drivers of
  the household cost of 6,000 gallons/month of municipal drinking water.
  Mayor-led (vs. manager/council-led) municipal government form is
  associated with $1.58/month lower cost in the organizational-structure
  model (p<0.05), attenuating to a non-significant $1.03 once other
  covariates are added; utilities that purchase water wholesale charge
  $2.86/month more (p<0.05). Added to `effect_sizes.csv` (form-of-government
  coefficient recorded as the primary institutional/governance effect per
  CODEBOOK.md §12's one-effect-per-study default).

Full-text screening now stands at 924/3,659 (469 include / 455 exclude),
2,735 open in the regenerated retrieval queue. `extraction_database.csv`
and `evidence_map.csv` both grew to 469 rows; `effect_sizes.csv` grew from
20 to 22 rows. Duplicate audit (exact DOI, record_id-in-extraction_note)
came back clean. `validate_schemas.py` passes all 13 checked files.

## 2026-09-18 — Twenty-first full-text screening batch: Google Drive Zotero-storage re-sync (batch 5), 2 new includes (S468-S469)

The researcher shared a new Google Drive folder that turned out to be a
fresh full re-sync of his Zotero attachment-storage library, not a small
delta: 111 storage-key subfolders were enumerated (matching the batches-1-3
pattern of many recurring keys, e.g. `35R6JBMX`, `XD2GTAMW`, `ZA6F5UCY`,
`577RP5MF`, `883TJUZ7`), containing 110 real attachments (PDFs and
Google-Doc web snapshots; the 111th folder held only the researcher's own
Zotero-master-spreadsheet export, not a screening target) plus 8
`.zotero-ft-cache` files (ignored, as always).

**Matching method**: token-overlap (Jaccard) scoring of normalized,
stopword-stripped titles against all 3,659 `full_text_screening_database.csv`
titles, top-3 candidates inspected by eye rather than trusting the top score
blindly. 100 of 110 items matched confidently and unambiguously on the
first pass. A further 8 had meaningless Zotero-assigned filenames (`pad`
×2, `wp.2025`, `ws.2025`, `home`, `anti`, `discovery`, bare DOI-suffix
strings like `25741292.2025`, `07352166.2026`, `S0957178726001657`) and
required downloading and reading the actual content before they could be
matched at all.

**Result of matching**: 108 of the 110 real attachments resolved to
already-decided `record_id`s (skipped, not re-processed — most were
literal duplicate copies of PDFs/web-snapshots already screened in this
session's earlier batches 1-3, now living under a second, different
Zotero storage key in the re-synced folder). 2 resolved to already-flagged
`wrong_file_retrieved` records (`R81549C4709FC`, `R5725BF04FB9F`) — both
re-downloaded and re-read in full to confirm the mismatch still holds on
this third retrieval attempt (same wrong book chapter; same 2-page erratum
notice, respectively); the flags remain in place, both records still open.
Genuinely open and newly matched: **2 records, both included**.

**S468** (Santos, Ferreira, Lanzinha & Collado 2025, *Urban Science*):
qualitative phenomenological case study (6 semi-structured interviews, 3
institutional actors + 3 community leaders) of WASH-service sustainability
in Beira, Mozambique, finding persistent institutional fragmentation
across four overlapping agencies (SASB, AdRC, AIAS, CMB), an informally
tolerated community-self-managed standpipe system in one neighbourhood
(Ponta Gêa) contrasted with no such recognition elsewhere, and a
social-tariff mechanism that does not cover operating costs.

**S469** (Alam, Rahat, Neeher, Tabassum, Nawaz, Evans & Hutchings 2025,
*J. Water Sanitation Hyg. Dev.*): 384-household matched-pair mixed-methods
study of barriers to sewer connection in Dhaka, Bangladesh — a
$84-342 USD connection fee against a ~$270 USD average monthly salary,
multi-year delay despite full compliance, and DWASA's undocumented
discretionary inaction on completed applications, which two of ten IDI
respondents responded to by self-connecting without authorization and
being fined by police for unauthorised road-cutting.

Neither new include had a genuine, non-fabricated single exposure-
comparator effect estimate with a locatable confidence interval (Alam et
al.'s statistical tests treat sewer-connection status as the *outcome*
being compared across groups on various barrier/belief variables, not as
an outcome produced by a defined legal-mechanism exposure), so
`effect_sizes.csv` is unchanged at 20 rows.

A corpus-wide duplicate audit re-run afterwards (4 independent methods:
exact DOI, exact normalized title, fuzzy title ratio>0.85, duplicate
record_id in `extraction_note`) came back clean (0 groups) against the
resulting 467-study corpus. Schema validation
(`code/analysis/validate_schemas.py`) passes on all 13 checked files.

Updated figures: 920/3,659 full-text records decided (467 include / 453
exclude), 2,739 open (`full_text_retrieval_queue.csv` regenerated to
match). `extraction_database.csv` and `evidence_map.csv` now at 467 rows
(178 quantitative-synthesis-eligible, 387 qualitative-synthesis-eligible);
`effect_sizes.csv` unchanged at 20 rows.

## 2026-09-17 — Twentieth full-text screening batch: Google Drive Zotero-storage batch 3, 45 new includes (S423-S467)

Continuation of the Google Drive Zotero attachment-storage retrieval effort
(51 confirmed record_id <-> Drive-fileId matches, plus content-based
identification of 15 additional ambiguous-filename Google Docs). **45
included, 4 excluded, 2 flagged `wrong_file_retrieved`** (left open).

**Retrieval notes**: 44 items downloaded as PDF via `download_file_content`
(base64); 2 items (`RA18CACA8BA7C`, a >10MB PDF that failed direct download,
and `RA1089E59F308`, whose PDF download consistently hit a transient MCP
session-expiry error) were instead retrieved as natural-language text via
Drive's `read_file_content`. One record (`R4B40A3139B39`, a 156MB PDF,
Medeiros et al., Brazilian rural-school WASH) could not be downloaded
directly and `read_file_content` returned empty content for it — but the
*same study's* full text was independently located, in Portuguese, among
the 15 ambiguous-filename Google Docs (Zotero-assigned filename
`dTC6gXGV9Ymz8xYpNLHgMvD`, SciELO/Cadernos de Saude Publica DOI
10.1590/0102-311XPT128025, a trilingual PT/EN/ES companion snapshot of the
same paper) and used as the retrieval source instead, avoiding an
`oversized_file_undeliverable` outcome.

**15 ambiguous-filename Google Docs**: all 15 were downloaded and content-
identified. 13 turned out to be duplicate Zotero web-snapshots of records
already among the 51 confirmed matches (e.g. two independent "pad" and two
independent "wp.2025" snapshots of the same two underlying papers) and
required no separate action; 1 (`25741292.2025`) was a blank/unusable
snapshot ("Reader environment loading", the page had not finished loading
when Zotero saved it); 1 (`dTC6gXGV9Ymz8xYpNLHgMvD`) supplied genuine
substitute full-text content for the oversized `R4B40A3139B39` PDF, as
above. None resolved to a genuinely new, previously-unmatched open record.

**`wrong_file_retrieved` (2, left open)**:
- `R5725BF04FB9F`: the delivered PDF is only a 2-page ACS "Addition/
  Correction" erratum notice (DOI 10.1021/acs.est.9b03482) for DuChanois et
  al. 2019's water-service-continuity article — no methods/results content,
  the substantive article itself was not retrieved.
- `R81549C4709FC`: this record was already flagged `wrong_file_retrieved`
  in an earlier batch. The new retrieval attempt again delivered the wrong
  file — a 12-page book chapter, "Climate Change in Nepal through an
  Indigenous Environmental Justice Lens" (Sherpa), confirmed via full-text
  search to contain no mention of "Singh" or "Political Capabilities"
  anywhere — so the flag remains in place rather than being cleared.

**4 excluded** (all E03 wrong-exposure except one E01 wrong-topic):
Alzahrani & Tawfik (Saudi urban water *consumption* drivers — "institutional
factors" reduced to a single narrow desalinated-water-access variable, not
a legal/administrative exposure); Choque-Quispe et al. (Peru, a water-
*quality* deterministic/probabilistic health-risk study, governance only
incidental background); Nunbogu, Harter & Mosler (Ghana latrine completion
via the RANAS *behavioural* model, not a legal/institutional exposure);
and D'Odorico, Dell'Angelo & Rulli ("Appropriation pathways of water
grabbing" — zero mentions of "household"/"drinking water"/"domestic water",
examines macro-level agricultural/mining/hydropower water-resource
appropriation, not household/community service access; E01).

**45 includes** span sanitation-policy compliance (Kenya, Mexico), legal
pluralism/decentralisation (Uganda), slum legal-notification status
(Ludhiana, India), correctional-facility menstrual hygiene, water-board
electoral accountability (California — IRR=1.23, p<0.001 for jurisdictional
fragmentation predicting uncontested elections; uncontested elections
associated with bill-assistance-adoption probability falling from 0.31 to
0.12), intermunicipal cooperation and WWS performance (Brazil, panel fixed-
effects), Human Right to Water/Sanitation affordability and disconnections
(Portugal, Nairobi), heritage water infrastructure policy (Indian
Himalayan Region), and a national school-census logistic-regression study
of WASH-in-schools funding-formula disadvantage (Brazil, ORs up to 6.40,
p<0.001) — full list and mechanism coding in `extraction_database.csv`
(study_id S423-S467).

4 of the includes had a clean, locatable, non-fabricated single exposure-
comparator effect estimate and were added to `effect_sizes.csv` (S434 mining
proximity/water security; S435 uncontested elections/bill-assistance
adoption; S445 regional funding-formula disadvantage/water-absence odds
ratios; S448 intermunicipal cooperation/financial performance) — all
recorded without a synthesis-family assignment and without pooling, each
being the only study yet sharing its specific exposure-comparator
operationalization, per `ANALYSIS_PLAN.md` §2's decision tree.

A corpus-wide duplicate audit re-run afterwards (4 independent methods:
exact DOI, exact normalized title, fuzzy title ratio>0.85, duplicate
record_id in `extraction_note`) came back clean (0 groups) against the
resulting 465-study corpus.

Updated figures: 918/3,659 full-text records decided (465 include / 453
exclude), 2,741 open (`full_text_retrieval_queue.csv` regenerated to
match). `extraction_database.csv` and `evidence_map.csv` now at 465 rows
(177 quantitative-synthesis-eligible, 385 qualitative-synthesis-eligible);
`effect_sizes.csv` now at 20 rows (+4).

## 2026-09-17 — Nineteenth full-text screening batch: 5 researcher-supplied PDFs, 4 new includes (S419-S422)

Researcher supplied 5 more PDFs directly via chat upload. **4 included, 1
excluded**:

- **Excluded**: Haapala & White 2018 (E04, wrong outcome — institutional-
  bricolage study of rural water project implementation *staff* in Nepal;
  population and outcome are staff motivation/authority, not household
  access).
- **S419** (Kobes 2016, eastern Slovakia): qualitative ethnographic case
  study (1999-2014) of a Roma settlement denied extension of the standard
  municipal water network on the grounds of disputed/unclear land tenure,
  instead connected to a lower-quality parallel system and billed a fixed
  quarterly fee despite no meters being installed.
- **S420** (Helgegren 2020, Bolivia PhD thesis, Chalmers University):
  multi-paper thesis on the Kanata metropolitan region's co-existing
  municipal/community/individual water-sanitation regimes. **Duplicate-
  overlap handling**: this thesis's Paper II reports the same findings
  already captured as study S410 (Helgegren, McConville, Landaeta & Rauch
  2020, a separately-published journal article extracted in yesterday's
  batch) — Paper II's content was deliberately *not* re-extracted here to
  avoid double-counting; S420 captures only the genuinely additional
  regime-analysis findings (Paper I, real population/service-coverage data
  by regime and municipality) plus a summary of Papers III/IV.
- **S421** (Agade, Anderson, Lugusa & Awino 2022, Kenya): mixed-methods
  study of Water Resource Users' Associations (WRUAs, Kenya's Water Act
  2002/2016) alongside indigenous Maasai institutions (Olosho councils,
  Laibon) in the Narok County rangelands — WRUA corruption/elite capture
  and enforcement gaps ("who one knows" determines irrigation access)
  documented via 80 interviews plus a full 12-month police-occurrence-book
  conflict log (14 documented incidents) and the independent ACLED
  database.
- **S422** (OECD 2021, *Water Governance in Asia-Pacific*): cross-national
  survey of 48 Asia-Pacific countries' water governance frameworks
  (regulatory-body mandates, abstraction/pollution charges, monitoring),
  with a dedicated section empirically cross-tabulating governance-
  mechanism adoption against the Asian Development Bank's household/urban
  water-security index scores.

A corpus-wide duplicate audit re-run afterwards (4 independent methods)
came back clean against the resulting 420-study corpus — confirming the
S410/S420 overlap was correctly handled by selective extraction rather than
needing a full duplicate-merge (the two records capture genuinely different,
non-overlapping content from the same underlying PhD research programme).

Updated figures: 869/3,659 full-text records decided (420 include / 449
exclude), 2,790 open. `extraction_database.csv` and `evidence_map.csv` now
at 420 rows (156 quantitative-synthesis-eligible, 354 qualitative-
synthesis-eligible); `effect_sizes.csv` unchanged at 16 rows (none of this
batch's 4 includes had a clean single exposure-comparator effect estimate
with a locatable confidence interval).

## 2026-09-17 — Second Antigravity Drive batch: 34 PDFs, 18 new includes (S401-S418), 1 retrieval mismatch flagged

Antigravity (Gemini) delivered a second batch of 34 open-access PDFs to
the shared Google Drive folder, named by `record_id` per the retrieval
prompt. All 34 were confirmed genuinely open in
`full_text_screening_database.csv` before screening (no re-screened
records). Full-text screened against `INCLUSION_EXCLUSION.md`: **18
included (S401-S418), 15 excluded, 1 flagged as a retrieval mismatch and
left open** (not screened).

**Retrieval mismatch caught before screening**: `R81549C4709FC`'s actual
target record is "Building Political Capabilities through Participation
for Environmental Justice in Informal Housing in Kathmandu" (Singh &
Singh, ch.18 of a Handbook of Climate Justice, DOI
10.4324/9781003371175-24), but the PDF delivered contains chapters 19-20
of the same edited volume instead (Sherpa's Nepal climate-policy chapter;
Awale's Kavre women/water chapter) — a wrong-chapter retrieval, not a
content match. This was identified by cross-checking the PDF's visible
title/chapter numbers against the record's title in the screening
database before making a screening judgment, per the project's "never
fabricate data" discipline. The record's `full_text_status` was set to
`wrong_file_retrieved` with a note describing the mismatch; it remains
open, awaiting a correct re-retrieval of chapter 18, not screened as
include or exclude.

**18 new includes (S401-S418)** span a strong cluster of studies directly
on the review's core administrative/legal-mechanism framework:
- **Eligibility mechanisms**: S404 (Mwaura et al. 2021, Kenya) — WRUA
  legal membership under the Water Act 2002/2016 reducing water poverty
  by 14-32% (ATT, three independent quasi-experimental estimators:
  endogenous switching probit, propensity score matching, inverse
  probability weighting) — added to `effect_sizes.csv` (Family A); S412
  (Ranganathan & Balazs 2015) — Tooleville (California) and Bommanahalli
  (Bangalore) both excluded from municipal water networks by
  unincorporated/peri-urban jurisdictional status rather than physical
  distance, a direct empirical instance of the review's core thesis; S416
  (Roy 2013) — Delhi's Kathputli Colony, where the Slum Areas Act 1956
  notification status and a 2002 Supreme Court Article 21 ruling leave
  slum residents' water access as an exceptional grant rather than an
  enforceable right ("claims of the poor... never become rights").
- **Discretion/accommodation and enforcement**: S415 (Ward et al. 2026) —
  37 interviews across 11 US water utilities documenting "street-level
  discretion" (bending rules, expediting CAP enrollments, waiving fees)
  and a three-camp typology (Traditionalist/Balancer/Benevolence-Led)
  explaining why most utilities' customer-assistance programs lack
  recognition-justice design; S403 (Zaunda et al. 2018, Malawi) — disabled
  children's primary-school WASH access undermined because Malawi's
  Disability Act does not make inclusive WASH provision legally binding,
  with zero of 10 surveyed schools having accessible facilities; S402
  (Sakaya et al. 2025, Uganda) — overlapping/fragmented legal mandates
  across three ministries explaining a 65%-vs-40% safely-managed-access
  gap between two towns.
- **Systematic review**: S418 (Brown et al. 2023, *Lancet Global Health*)
  — a documented-search-strategy review of racism/exclusion mechanisms in
  high-income-country water/sanitation access, including a North Carolina
  case (Irongate Drive) excluded from municipal service for decades by
  racial municipal underbounding, only annexed and connected in 2020;
  flagged `study_design_class = systematic_review_secondary`,
  `risk_of_bias_tool = AMSTAR 2`.
- Also included: S401 (Gondar, Ethiopia UGI governance study), S405
  (Soweto Free Basic Water implementation), S406 and S408 (Cameroon and
  Senegal rural water-governance-transfer case studies, both flagged
  `study_design_class = jurimetric`), S407 (Archibong 2018, Nigeria
  historical federal/local service-inequality panel study), S409
  (Ethiopia Wolaita Zone water-point coverage/governance study), S410
  (Cochabamba, Bolivia community-managed systems and legal-entity
  status), S411 (Oosterwold, Netherlands wastewater self-organization
  legal mismatch, `study_design_class = jurimetric`), S413 (Minas Gerais,
  Brazil COPASA privatization/coverage study), S414 (Waterberg, South
  Africa private-water regulatory-exemption case study), and S417
  (Hacker et al. 2025, US unsheltered-individuals WASH-access study).

**15 exclusions**, all reasoned against `INCLUSION_EXCLUSION.md`: E01
wrong topic (public-acceptance-of-technology and financialization-theory
papers), E03 wrong exposure (hydrological/engineering modelling, water-
quality/arsenic-mitigation-technology and cistern-contamination-risk
studies), E04 wrong outcome (utility regulatory-compliance, infrastructure-
lifecycle-management, and willingness-to-pay/satisfaction studies whose
outcome is not access/connection/exclusion), E05 no empirical evidence
(corporate/policy essays and narrative commentary without a defined
study design) E06 engineering only. Full per-record rationale in
`02_screening/exclusion_log/exclusion_log.csv`.

A corpus-wide duplicate audit re-run afterwards (4 independent methods)
came back clean against the resulting 416-study corpus.

Updated figures: 864/3,659 full-text records decided (416 include / 448
exclude), 2,795 open. `extraction_database.csv` and `evidence_map.csv` now
at 416 rows (154 quantitative-synthesis-eligible, 351 qualitative-
synthesis-eligible); `effect_sizes.csv` now at 16 rows.

## 2026-09-16 — Single-record screening: Tsanga Tabi 2009, French water-disconnection/social-vulnerability case study (S400)

Researcher supplied 2 more PDFs directly. **1 excluded**: Carre &
Deroubaix 2009 (E04, Flux 76-77, domestic rainwater-harvesting practices
in Paris-suburb municipalities; real empirical interviews and LEMA-law
regulatory context, but the actual outcome studied is utility revenue-
model/tariff-sustainability tension under declining consumption and user
attitudes toward the service, not a household-level access/connection/
exclusion outcome — wrong outcome). **1 included** and fully extracted as
S400: Tsanga Tabi 2009 (Flux 76-77), a mixed-methods case study (Vannes
municipal utility and Loiret private-concession department, plus national
disconnection statistics) of France's water-disconnection legal framework
— LEMA (2006) article 1 prohibiting disconnection of FSL-aid recipients,
municipal anti-disconnection arretes (several annulled by administrative
tribunals on prefectoral referral for exceeding municipal competence),
and departmental "Solidarite Eau" partnership aid schemes, with real
administrative data (120,000 national disconnections in 2003; Loiret aid
take-up rates of 50.5%/47%, average aid EUR93-98/household).

`S399` remains a permanent gap in the study_id sequence (like `S227`): it
was assigned earlier the same day to a PDF that the duplicate-detection
audit found was the same article as the already-extracted S102, and was
merged into S102 rather than kept as its own row — see the
"Google Drive batch" entry below. S400 continues the sequence from S398,
not S399, to avoid reusing a number that was briefly live.

Regenerated `full_text_retrieval_queue.csv`, re-ran the duplicate audit
(clean against the resulting 398-study corpus), and validated all 13
tracked schemas. Net: 829 → 831 decided, 397 → 398 include, 432 → 433
exclude, 2830 → 2828 open. `evidence_map.csv` quantitative_synthesis_
eligible now 145/398 (was 144/397), qualitative_synthesis_eligible now
335/398 (was 334/397).

## 2026-09-16 — Google Drive batch: 19 PDFs (18 new + 1 duplicate) via Antigravity retrieval, 11 new includes (S389-S399), 1 genuine duplicate caught and merged

Researcher shared a new Google Drive folder of Antigravity-retrieved PDFs.
Downloaded all 19 files via the Google Drive MCP connector (base64,
decoded locally); 1 (`RB334FC53A1A9`, Glavanits & Fenyes 2026) duplicated a
record already screened and included as S387 earlier the same day and was
skipped without re-processing. The remaining 18 were screened.

**Process note, disclosed rather than papered over**: the first parallel
`Read` batch of 5 PDFs, and 4 PDFs from a second parallel batch of 5,
returned only extraction-confirmation text with no visible page images
(a request-limit truncation), meaning the resulting screening decisions
were initially made without actually seeing those 9 PDFs' content — a
direct violation of this project's "never fabricate data" rule. Caught
this before extraction began, and re-read all 9 individually (Wall 2004,
Barnes 2006, Whelan & Willis 2007, Goncalves 2014, Umunna 2010, Fracalanza
et al. 2013, Suharyanto et al. 2018, Nurbaiti & Bambang 2018, Minaverry
2017) against real page images. All 9 original decisions were confirmed
correct on re-verification, so no decisions changed, but this is recorded
here because the near-miss is itself worth disclosing.

**7 excluded**: Wall 2004 (E05, CSIR technical note/feasibility discussion,
no primary population/exposure/outcome data of its own); Barnes et al. 2006
(E01, an engineering-education curriculum-design paper, wrong topic);
Umunna 2010 (E05, a "Letter to the Editor" opinion piece citing secondary
WHO statistics, no primary methodology); Fracalanza, Jacob & Eca 2013 (E05,
a theoretical/conceptual essay on environmental-justice water governance,
no primary data collection); Nurbaiti & Bambang 2018 (E05, self-described
as a non-systematic "literature study," no primary data collection of its
own); Jauhari, Soesilo & Priadi 2021 (E06, a Life Cycle Cost
engineering-costing exercise, consistent with the Tseng et al. 2020
precedent); Leite, Carmo & Correia 2026 (E01, a corporate Balanced-Scorecard
management-tool case study, no household-level access analysis).

**11 included and fully extracted** (`extract_s389_s399.py`,
`build_evidence_map.py` + `fill_evidence_map_s389_s399.py`): Whelan &
Willis 2007 (rural Tasmania, statutory Public Health Act compliance burden
and disconnection-liability tensions, 12 interviews); Goncalves 2014
(Portugal, ERSAR social-tariff income-eligibility impact analysis, 278
municipalities); Suharyanto et al. 2018 (Salatiga, Indonesia,
Rapfish/MDS institutional-dimension sustainability scoring of 4 community
water-supply schemes); Minaverry 2017 (Argentina, jurimetric legal analysis
of 2 court cases prohibiting water disconnection for non-payment as a
human-right-to-water violation — appraised with the project's own Legal
Institutional Evidence Appraisal Framework); Curtis 2019 (BMJ Global
Health, 17 interviews on institutional behaviour change driving India's
Swachh Bharat sanitation-coverage transformation); Salom & Khumalo 2022
(Namibia, Ohangwena Region, a legal-framework transition gap undermining
rural water management); Lutfia et al. 2024 (Indonesia, Jambon Village
SPAMDes institutional-dimension characterization); Gouveia,
Formiga-Johnsson & Britto 2026 (Sao Goncalo, Brazil, "invisible"
hydrosocial scarcity among nominally-connected households); de Araujo,
de Morais & de Almeida 2025 (Brazil, 853-municipality panel study of
institutional-capacity determinants of legally-mandated sanitation-policy
adoption — flagged as a strong future `effect_sizes.csv` candidate pending
its full regression table); dos Santos Nascimento Sobrinho & da Mota
Silveira Neto 2025 (Recife, Brazil, a genuine quasi-experimental
difference-in-differences evaluation of the ZEIS zoning-law intervention,
with a real ~23-percentage-point effect on household sewage-network
access — **added to `effect_sizes.csv`**, Family A); and Alvaredo 2025
(Barreiro, Portugal, historical archival case study of a mandatory-
connection/minimum-tariff legal regime, 1930s-1980s).

**Genuine duplicate caught and resolved**: the corpus-wide duplicate audit
(re-run after extraction, as always) found Alvaredo 2025 already existed
in the corpus as S102 (`record_id` `R34A26DC79A8B`, extracted 2026-09-15
from abstract-only text) — a second copy of the same DOI
(10.15847/cct.36875) reached the pipeline this round under a differently-
formatted title that produced a distinct content-hash `record_id`
(`R21CAA5C1809C`), missing the earlier DOI-based dedup pass. Rather than
keep both, merged this round's fuller full-text extraction (archival
tariff tables, specific decree citations, year-by-year unpaid-bill
percentages) into S102's row, corrected `R21CAA5C1809C` from `include` to
`exclude`/E08 in `full_text_screening_database.csv`, logged it to
`exclusion_log.csv`, and updated S102's `evidence_map.csv` row (mechanism_
family MULTIPLE, `study_design_class` reclassified from `doctrinal` to
`jurimetric` given the fuller archival-empirical-data picture now
available). Net new studies from this round: 11 include, not 12.

Regenerated `full_text_retrieval_queue.csv`, re-ran the corpus-wide
duplicate-detection audit a second time after the S102/S399 fix (clean
against the resulting 397-study corpus), and validated all 13 tracked
schemas. Net: 811 → 829 decided, 387 → 397 include, 424 → 432 exclude,
2848 → 2830 open. `evidence_map.csv` quantitative_synthesis_eligible now
144/397 (was 140/387), qualitative_synthesis_eligible now 334/397 (was
328/387). `effect_sizes.csv` 14 → 15 rows.

## 2026-09-16 — Cowork Scopus retrieval status merged into full_text_screening_database.csv

Merged a researcher-supplied `full_text_status`/`full_text_location`/
`notes` update covering all 1,139 previously-open Scopus records (the CSV
sent to the researcher earlier the same day for the Cowork retrieval
prompt) into `full_text_screening_database.csv`. **This is a status/
triage update, not a completed retrieval round**: of the 1,139 records,
only 1 (`RB334FC53A1A9`, Glavanits & Fenyes 2026) was actually retrieved
as a PDF — and that one had already been separately supplied by the
researcher and screened as S387 earlier the same day, so no new screening
resulted from this merge. The remaining 1,138 break down as: 713
`not_retrievable` (paywalled, no OA copy per Unpaywall), 168
`oa_pdf_candidate` (a direct OA PDF URL was located but not yet
downloaded), 138 `no_oa_copy_found` (no DOI or no OA match), 105
`oa_page_candidate` (an OA landing page was located, no direct PDF link,
not yet downloaded), and 14 `pending` (DOI not indexed by Unpaywall, needs
manual/title search). The 168 + 105 = 273 `oa_pdf_candidate`/
`oa_page_candidate` records are genuine near-term retrieval opportunities
— Cowork has already identified a legitimate open-access location for
each, but the file itself still needs to be fetched and supplied. `final_
decision` was left untouched for every record (no full-text screening
occurred in this merge). Regenerated `full_text_retrieval_queue.csv`
(counts unchanged: 811 decided, 2,848 open, since no `final_decision`
changed) and validated all 13 tracked schemas.

## 2026-09-16 — Single-record screening: Li, McManus & Cronk 2025, Liberia water-point functionality (S388), extended into effect_sizes.csv

Researcher supplied one more PDF directly; identified via DOI/title match
as record `R897B0E5CB3C7`, confirmed genuinely open. **Included** and
fully extracted as S388: a large-sample (n=11,065 Afridev hand pumps)
quantitative study of Liberian water-point functionality, with a genuine
institutional/governance exposure (maintainer type — no management, local
authority, institutional organization, or WASH committee) and a real,
locatable adjusted-OR effect estimate (Local vs No Management: adjusted
OR=3.733, 95% CI 2.993–4.657, p<0.0001).

**Added to `effect_sizes.csv`** (14th row) — the strongest new candidate
since the last extension: a genuine institutional-management
exposure-vs-comparator contrast from a large administrative census, with a
real adjusted OR and CI, not a fabricated or forced fit. `synthesis_family`
left blank rather than assigned to Family A/B/C: the exposure (who is
institutionally responsible for a water point's maintenance) doesn't
cleanly match legal recognition/tenure (Family A), application-process
bureaucratic assistance (Family B), or an access-restricting barrier
(Family C) — a real judgment call flagged for the manuscript stage rather
than guessed, per `PROJECT_SPEC.md` §8.

Regenerated `full_text_retrieval_queue.csv`, re-ran the duplicate audit
(clean against the resulting 387-study corpus), and validated all 13
tracked schemas. Net: 810 → 811 decided, 386 → 387 include, 2849 → 2848
open; `effect_sizes.csv` 13 → 14 rows.

## 2026-09-16 — Single-record screening: Glavanits & Fenyes 2026, "Beyond Potty Parity" (S387)

Researcher supplied one more PDF directly (no `record_id` in the filename
this time), identified via DOI/title match against
`full_text_screening_database.csv` as record `RB334FC53A1A9`, confirmed
genuinely open. **Included** and fully extracted as S387: Glavanits &
Fenyes 2026 (Laws 15(3):55), a mixed-methods study (97-respondent
questionnaire, 56-user chronometric time-measurement observation, and
qualitative thematic coding) of gendered waiting-time disparities in
public-toilet access in Hungary, framed against EU Council Directive
2004/113/EC's indirect-discrimination standard and a comparative review of
public-toilet regulatory philosophies across 6 jurisdictions (a
"quantitative"/fixture-ratio model, US "potty parity," UK performance-based
BS 6465, and German qualitative-functional ASR/DIN standards). Not added
to `effect_sizes.csv`: the paper's real regression/ANOVA findings use
gender as the exposure variable, not an institutional/legal exposure with
a genuine comparator (e.g. different regulatory regimes with matched
outcome data), so per the S135 precedent this is recorded as
quantitative_synthesis_eligible = TRUE in `evidence_map.csv` without
forcing an effect_sizes.csv entry.

Regenerated `full_text_retrieval_queue.csv`, re-ran the duplicate audit
(clean against the resulting 386-study corpus), and validated all 13
tracked schemas. Net: 809 → 810 decided, 385 → 386 include, 2850 → 2849
open.

## 2026-09-16 — Seventeenth full-text screening batch: 15 records via researcher-supplied PDFs, 13 new includes (S374-S386)

Screened 15 more full-text PDFs supplied directly by the researcher (a
continuation of the same-day retrieval round; the first 13 PDFs of this
upload wave duplicated records already screened and pushed earlier the
same day — confirmed via record_id lookup against
`full_text_screening_database.csv` before any re-processing, so no
duplicate decisions were recorded). Recorded via `record_batch19.py`.

**2 excluded**: Meng et al. 2026 (E06, Hainan rural sewage-facility
GIS/spatial-statistics study, engineering/spatial-planning only, no
legal/institutional access-barrier analysis); Prieto 2016 (E07, Chilean
Atacameno water-RIGHTS-MARKET and indigenous-identity study, concerns
agricultural/mining/multi-use water-resource-rights transactions, not
household drinking-water/sanitation service access).

**13 included and fully extracted** (`extract_s374_s386.py`,
`build_evidence_map.py` + `fill_evidence_map_s374_s386.py`): Inha & Hukka
2019 (Seattle water-service institutional resilience); Farmer 2017 (16-
month Cairo ethnography of tariff/payment-system resistance in an informal
settlement); Martellet et al. 2024 (Rio Branco, Brazil, ACERTAR regulatory-
audit indicator evaluation of Brazil's Novo Marco Regulatorio — appraised
with the project's own Legal Institutional Evidence Appraisal Framework as
`jurimetric`, a real judgment call resolved by hand since
`build_evidence_map.py` cannot mechanically distinguish doctrinal from
jurimetric); Tamboura, Baron & Kabore 2024 (Ouagadougou bottom-up water
innovation in legally-unrecognized "non loti" neighborhoods); Shekhar &
Dwivedi 2021 (India, NFHS-4 wealth-index regression showing ~200x odds-
ratio inequality in sanitation-technology access, institutional-
fragmentation framing); Morales-Juarez & Mendez-Garcia 2021 (Oaxaca,
Mexico, independent community water systems unrecognized in national water
law); Baron & Maillefert 2011 (comparative institutionalist analysis of
drinking-water governance across francophone West Africa — abstract-only,
only 2 pages were retrievable from the supplied PDF); Bradshaw & Huby 2013
(England and Wales water-poverty trend analysis); Malima & Pindihama 2022
(Vhembe District, South Africa, rural potable-water-security household
survey); Aguirre-Osuna 2026 (Cabo San Lucas, Mexico, mixed-methods study of
unequal water access and concentrated national water-concession
ownership); Ayanlola et al. 2025 (South-West Nigeria, regression-identified
determinants of open defecation including weak sanitation-law enforcement,
beta=0.47, p=0.002); Rojas Rivera 2026 (Colombia, Hausman-Taylor panel-data
study of fiscal/political/administrative decentralization's effects on
municipal water/sewerage coverage — flagged as a strong future
`effect_sizes.csv` candidate once its full regression-results table, not
yet retrieved in this pass, is read); Esteban et al. 2025 (Las Vigas,
Guerrero, Mexico, mixed-methods study finding payment-conditioned water
distribution and fragmented institutional oversight driving unequal
access).

Regenerated `full_text_retrieval_queue.csv`, re-ran the corpus-wide
duplicate-detection audit (4 independent methods) against the resulting
385-study corpus (clean), and validated all 13 tracked schemas.

Net (across both batches processed today, 2026-09-16): 781 → 809 decided,
366 → 385 include, 415 → 424 exclude, 2878 → 2850 open.
`evidence_map.csv` quantitative_synthesis_eligible now 138/385 (was
130/366), qualitative_synthesis_eligible now 327/385 (was 316/366).
`effect_sizes.csv` unchanged at 13 rows (S385 flagged as a strong
candidate pending fuller-text retrieval, consistent with the discipline of
never forcing an entry without the full effect-estimate table in hand).

**`04_quality/risk_of_bias/2026-09-16_evidence_limitations.md` is now
stale by 19 studies (366→385, 5.2%)** — its percentage breakdowns still
reflect the 366-study corpus; not recomputed in this round for the same
reason given in the previous entry (small relative corpus change versus
the effort of a full re-derivation), flagged rather than silently left
inconsistent.

## [Unreleased]

Nothing yet — no phase past repository setup and source verification has
been reached.

## 2026-09-16 — Sixteenth full-text screening batch: 13 records via researcher-supplied PDFs, 6 new includes (S368-S373)

Screened 13 full-text PDFs supplied directly by the researcher (retrieved via
the "Antigravity" agent's Unpaywall-based retrieval pass, per the retrieval
prompt drafted earlier this session), all confirmed genuinely open
(`final_decision` blank) in `full_text_screening_database.csv` before
screening. Recorded via `record_batch18.py`.

**7 excluded**: Marques 2008 (E01, Portuguese utility TFP/efficiency study,
no legal/institutional access mechanism); de Wit et al. 2024 (E01, WASH-
sector historiography, meta-level not empirical); Félix-López et al. 2023
(E07, reclaimed-water market economics, wrong service); Kireitseva et al.
2025 (E03, Ukraine water-resource SWOT/index, access percentages are index
inputs not a legal/institutional exposure); Sinharoy et al. 2022 (E05, ARISE
scales protocol with no results yet reported); Weets & Katz 2024 (E04,
global WASH-AMR policy mapping, outcome is AMR risk not access); Tseng et
al. 2020 (E06, ingredients-based WASH-in-healthcare-facilities costing
study, engineering/cost-estimation only).

**6 included and fully extracted** (`extract_s368_s373.py`,
`build_evidence_map.py` + `fill_evidence_map_s368_s373.py`):

- **S368** — Makalela & Molepo 2025 (Lepelle-Nkumpi Municipality, South
  Africa; n=449 household survey; chi-square/correlation analysis of
  COVID-19 and municipal water/sanitation/electricity/refuse service-
  delivery adequacy). Note: the source paper's own Statement-B1-B4 item
  labels in its prose narrative do not consistently match its own Table 1
  row order — reported as the source itself narrates it, flagged in
  `extraction_note` rather than silently resolved by guessing.
- **S369** — Hove et al. 2019, "Water is life" (BMJ Global Health), a
  qualitative PAR/Photovoice study in 3 Agincourt HDSS villages, Mpumalanga,
  South Africa. **Companion paper to S357** (Hove et al. 2021, Global Health
  Action, same VAPAR programme and study area) under this review's
  established companion-paper precedent (distinct reported findings, not a
  duplicate) — and, because full text was read here (unlike S357's
  abstract-only extraction), the fuller of the pair.
- **S370** — Macura et al. 2023 (BMJ Global Health), a systematic mapping
  review of gender equality and social inclusion (GESI) in WASH
  interventions (463 studies/499 publications, 62 LMICs). Because full text
  was available, this study's `risk_of_bias_rating` could be **positively
  determined as Critically Low** (not "Not ratable") — the review authors
  themselves explicitly state no critical appraisal of individual included
  studies was conducted, a directly confirmed AMSTAR 2 item-9 critical
  weakness, distinguishing this from the earlier 17-study AMSTAR 2 batch
  where the limiting factor was insufficient extraction depth rather than a
  confirmed fact.
- **S371** — Nurmaningtyas, Hamzah & Aprianti 2026, a sequential mixed-
  methods SWOT-AHP study of Tobati Village, Jayapura, Indonesia — an
  indigenous coastal water-based settlement with institutional dualism
  between customary (Ondoafi/tribal-chief) and formal government authority.
- **S372** — Nelson et al. 2021 (BMJ Open), a realist review of how
  community participation shapes WASH availability, behaviour-change, and
  infrastructure-longevity outcomes across 73 primary studies (29 LMICs).
  Same confirmed-not-guessed **Critically Low** AMSTAR 2 rating logic as
  S370 applies here (authors explicitly state formal appraisal of
  individual included papers was not carried out, citing realist-review
  convention).
- **S373** — Burt, Ercümen, Billava & Ray 2018 (World Development), a
  genuine quasi-experimental matched-cohort study (genetic matching, 8
  continuous-water-supply pilot wards vs. 8 matched intermittent-supply
  control wards, Hubli-Dharwad, India) of a tariff/service-level reform's
  effects on household costs, time savings, and equity. Flagged in
  `extraction_note` as a strong future `effect_sizes.csv` candidate once the
  paper's full regression-output table (not yet read in this pass) is
  retrieved — not added this round because only headline point estimates
  from the results narrative, not the full coefficient/CI table, were
  available.

Re-ran the corpus-wide duplicate-detection audit (4 independent methods)
against the resulting 372-study corpus: clean, no new duplicates.

Net: 781 → 794 decided, 366 → 372 include, 415 → 422 exclude, 2878 → 2865
open. Extraction and evidence_map fully caught up (372/372, no gap beyond
the pre-existing S227). `evidence_map.csv` quantitative_synthesis_eligible
now 132/372 (was 130/366), qualitative_synthesis_eligible now 320/372 (was
316/366). `effect_sizes.csv` unchanged at 13 rows this round (S373 flagged
as a candidate, not added, per the discipline in `ANALYSIS_PLAN.md` §2 of
never forcing an entry without the full effect-estimate table in hand).

**Note on `04_quality/risk_of_bias/2026-09-16_evidence_limitations.md`**:
that narrative's design-mix/jurisdiction/mechanism-family percentage
breakdowns were computed against the 366-study corpus earlier the same day
and are now stale by these 6 studies (1.6% of the corpus) — flagged rather
than silently left inconsistent; a full recomputation is still owed as a
follow-up, not done in this round given the small magnitude of the change
relative to the effort of re-deriving every percentage in that document.

## 2026-09-16 — AMSTAR 2 appraisal batch: all 17 systematic-review-secondary studies, all "Not ratable"

Continued Phase 9 appraisal to the next tool group after the RoB 2/
ROBINS-I pilot: the 17 studies flagged `study_design_class =
systematic_review_secondary` (S015, S019, S027, S052, S079, S116,
S319–S329), for which `RISK_OF_BIAS.md` specifies AMSTAR 2.

Obtained AMSTAR 2's tool structure via WebSearch (`WebFetch` to amstar.ca
and every publisher domain tried again returned `EGRESS_BLOCKED`, same
environment limitation as the RoB 2/ROBINS-I batch) — but this time, unlike
that batch, the tool text itself came back reasonably complete: all 16
items with verbatim/near-verbatim wording, the 7 critical items (2, 4, 7,
9, 11, 13, 15), and the confidence-rating algorithm, cross-checked across
multiple independent search results.

**The blocker this time was different: study-extraction depth, not tool
completeness.** All 17 of these systematic reviews were extracted at
citation/DOI/one-sentence-summary level, not from their own full Methods
sections — several explicitly flagged "abstract/repository metadata only"
in their `extraction_note`. AMSTAR 2 appraises what a review's own report
describes; not knowing whether a review reports something (e.g. protocol
registration, duplicate screening) is different from confirming it does
not, so every item lacking extracted evidence was marked "Not assessable"
rather than scored "No" — a deliberately more conservative reading than
AMSTAR 2's own default convention. Result: **6 of 17 studies (S015, S019,
S027, S052, S079, S116) have at least one genuinely assessable item**
(mostly item 1, PICO-scope specificity, and item 8, description of
included studies, inferable from richer extraction notes); the other 11
(S319–S329) have none. **S015 is the only study with a confirmed answer on
any critical item**: its `extraction_note` states it is OSF-registered
(https://osf.io/w94yr/), a genuine "Yes" on critical item 2 (prospective
protocol). Every one of the 17 studies' overall rating is **"Not
ratable"** — AMSTAR 2's High/Moderate/Low/Critically-Low algorithm
requires a defensible answer to all 7 critical items, and at most 1 of 7 is
answered for any study here. 17 appraisal-form files added to
`04_quality/appraisal_forms/` (`<study_id>_AMSTAR2.md`).

This is itself a disclosed finding, not just a process note: **a real
AMSTAR 2 appraisal of these 17 systematic reviews is not possible without
first retrieving and extracting each one's full Methods section** — a
prerequisite this project has not yet met for any of them. `extraction_note`
on each of the 17 rows now records that the appraisal was attempted and
why it could not be completed. `code/analysis/validate_schemas.py`
confirms all 13 checked files still match their documented schema.

## 2026-09-16 — Cross-cutting evidence-limitations narrative recomputed against 366-study corpus

The preliminary RoB narrative written earlier the same day (`04_quality/
risk_of_bias/2026-09-16_evidence_limitations.md`) explicitly flagged that
its corpus-composition figures were computed against 350 studies, before
that day's Zotero-batch screening round brought the total to 366, and
that "a full recomputation is still owed." Recomputed every figure in the
file directly from `extraction_database.csv`/`evidence_map.csv` at 366
studies: design mix (qualitative 39%, mixed-methods 20%, quasi-
experimental/experimental only 4% combined), mechanism_certainty (7%
reach quasi-experimental/experimental levels 3-4), country/legal-system
coverage (Brazil/India/South Africa 29% of corpus; common law 41%/civil
law 39%/mixed 13%), abstract-only-extraction rate (rose from 57/350, 16%,
to 69/366, 19%, once both disclosure-sentence phrasings used across
different extraction batches were searched for), mechanism-family
coverage, and Legal Institutional Evidence Appraisal Framework usage (73
of 366, 20%, now also covering S356/S364's cross-country regulatory
syntheses). None of the underlying patterns shifted materially with the
16 additional studies, as anticipated, but every number in the file is
now a fresh computation rather than a carried-over stale figure. Also
folded in the AMSTAR-2/CASP tool-assignment fix's continued consistency
check and the 8-study record_id traceability gap found during the same-
day duplicate audit. "Overall confidence" remains deliberately blank
pending real Phase 9 ratings.

## 2026-09-16 — Duplicate audit re-run on 366-study corpus (clean); effect_sizes.csv extended with 2 more studies (S353, S358)

Two follow-up items after the Zotero-batch screening round, both requested
directly by the researcher.

**Duplicate-detection audit re-run** across the full 366-study corpus
using the same four methods as the earlier post-hoc audit (exact DOI
match, exact normalized-title match, fuzzy-title similarity via
`difflib.SequenceMatcher` ratio > 0.85 with a length-difference
pre-filter, and duplicate-`record_id` detection via regex over
`extraction_note`). **Result: clean — zero duplicates found** by any
method across all 366 studies. One incidental, non-duplicate finding:
8 early studies (S076–S083) have no `record_id` recorded in their
`extraction_note` at all — not a regex-matching failure (confirmed by
direct substring search), a genuine traceability gap from an early
extraction batch that predates the "record_id X." note convention. Flagged
for the researcher's awareness; not fixed in this pass since it does not
affect data correctness or introduce a duplication risk, only limits how
easily those 8 rows can be cross-referenced back to their screening
record.

**`effect_sizes.csv` extended from 11 to 13 rows**, reviewing the two
studies from the 2026-09-16 Zotero batch with real, calculable effect
estimates: **S353** (Marcillo, Krometis & Krometis 2021 — private vs.
public utility ownership, adjusted OR=1.899 [95% CI 1.455–2.478] for SDWA
monitoring/reporting violations) and **S358** (Williams et al. 2025 —
Tribal oversight/primacy regulatory jurisdiction vs. state-primacy,
adjusted OR=0.62, p<0.001, for groundwater-decline risk). Both were
checked against `ANALYSIS_PLAN.md` §2's decision tree the same way as the
original 11: S358's Tribal-oversight exposure is assigned Family A (legal/
jurisdictional recognition), flagged as a looser fit than S084/S085/S142
since it operates at the level of environmental-regulatory authority
rather than household tenure/eligibility. S353's ownership-type exposure
does not match any of Families A/B/C and is recorded without a family
assignment, same treatment as S149/S178/S312 in the original batch. Both
studies also report real race-based effects (e.g. S358's OR=2.01 for
higher-Black-population communities) that were deliberately **not** used
as the primary extracted effect, for the same reason S135 was excluded
from this file entirely in the original pass — population demographic
composition is not itself a legal/institutional exposure. Both new rows
have `included_in_pooled_estimate = FALSE` with a decision-tree-cited
reason, consistent with every other row in the file.

`code/analysis/validate_schemas.py` confirms all 13 checked files still
match their documented schema.

## 2026-09-16 — Fifteenth full-text screening batch: 25 records via Zotero-sourced Drive folder, 16 new includes (S352–S367)

Researcher shared a new Drive folder of PDFs retrieved via Zotero. Of 34
files in the folder, 9 duplicated already-screened records (Muller 2007,
Hailu Tesfaye et al. 2026, Andrews et al. 2025, Hanjabam 2018, Abdulhadi et
al. 2024, Mottelson & Venerandi 2020, Nastar et al. 2019 — all decided in
earlier batches this session) and were skipped after verifying their
`final_decision` was already set (per the corrected column-verification
methodology from the TEST-ZIP incident). The remaining 25 were matched by
title/author to their pre-seeded `record_id` in
`full_text_screening_database.csv` and screened.

**One file/title mismatch found, not screened, flagged for the
researcher:** the Drive file named "Singh S. and Singh B. — 2024 —
Building Political Capabilities through Participation for Environmental
Justice in Informal Housing" actually contains two chapters from an
unrelated book, *Environmental Justice in Nepal* (Sherpa and Awale, on
climate-change adaptation and a Kavre water-scarcity case study) — a
keyword search of the full downloaded text confirmed no trace of "Singh,"
"political capabilities," or "informal housing" anywhere in it. Record
`R81549C4709FC` (the pre-seeded queue entry for the real Singh & Singh
paper) is left unscreened rather than screening the wrong content under
the right title, or the right title under wrong content.

16 included (S352–S367): Wamuchiru 2017 (Dar es Salaam grassroots water
citizenship); Marcillo, Krometis & Krometis 2021 (Virginia SDWA violations
by ownership/demographics, adjusted ORs); Crow & Odaba 2010 (Nairobi slum
water access and institutional learning); Singh et al. 2022 (Kampala fecal
sludge business models); Trémolet & Smith 2026 (OECD economic-regulation
synthesis); Hove et al. 2021 (South African rural water stakeholder
participation); Williams et al. 2025 (Arizona groundwater decline/
contamination by race and Tribal oversight, adjusted ORs); Doyle et al.
2018 (Crow Reservation tribal water utility jurisdictional/regulatory
gaps); Galway 2016 (First Nations Ontario drinking-water advisories);
Atigaku et al. 2026 (Togo community water governance, connection-cost
data); Khangale, Madumo & Tshiyoyo 2023 (South African intergovernmental
water-service relations); Sofiyah, Aji et al. 2025 (Jakarta sanitation
participation); Sylvester, Hutchings & Mdee 2023 (England/Wales water-
poverty systematic documentary review); Kharmylliem & Kipgen 2021
(Shillong formal/informal water-governance institutions); Quattrochi et
al. 2021 (BMJ Global Health — companion infrastructure/access/governance
outcomes paper to the same DRC VEA cluster-RCT already in the corpus as
S294, which reports diarrhea/growth/institutions outcomes; included as a
distinct-outcomes companion paper, not a duplicate, per standard PRISMA
practice for multi-outcome trial publications); Atem et al. 2026 (Foumbot,
Cameroon water-resource-management barriers, chi-square test on
water-source distribution, p=0.0001388).

9 excluded: Ramachandraiah 2011 (E01, flood-disaster response, water/
sanitation a secondary topic); Howard et al. 2020 (E05, WaSH/COVID-19
narrative review, no study-specific empirical data); Jabari et al. 2020
(E06, water-security risk-index engineering methodology); Willetts et al.
2022 (E01, climate-adaptation planning process, not access barriers);
Mashingaidze 2013 (E07, Kariba Dam displacement — excluded resources are
fishery/tourism/hydropower/wildlife, not household water/sanitation
service); Nagheeby et al. 2026 (E05, conceptual "capitalist Black Hole"
research note, no identifiable study-level population/exposure/outcome);
Inam 2025 (E01, earthquake-zone women's psychosocial-health interviews,
hygiene a minor secondary topic); Gomes et al. 2018 (E04, simulation-
gaming capacity-building workshop evaluation, outcome is participant
learning, not access/connection/service).

While fixing 9 extraction-database rows' mismatched core mechanism
booleans against their own detailed sub-codes (e.g. `fees=TRUE` recorded
without the parent `burden=TRUE`, `discretion=TRUE` without
`discretion_accommodation=TRUE`) — an internal-consistency check run
before populating `evidence_map.csv`'s `mechanism_family` — 9 of the 16
new rows needed a core-boolean correction; none required data invention,
only aligning the core boolean with sub-codes already recorded in the same
row.

Net: 757 → 781 decided, 350 → 366 include, 407 → 415 exclude, 2902 → 2878
open. Extraction and evidence_map fully caught up (366/366, no gap beyond
the existing documented S227 gap). `code/analysis/validate_schemas.py`
confirms all 13 checked files match their documented schema.

## 2026-09-16 — First risk-of-bias appraisal pilot batch (12 studies): RoB 2 (3) and ROBINS-I (9), partial and explicitly flagged

Began item 4 of the user-approved work plan: per-study appraisal against the
official validated tools. Started with the two smallest `risk_of_bias_tool`
groups (RoB 2: S057, S085, S294; ROBINS-I: S037, S121, S142, S143, S169,
S189, S213, S219, S235) as a manageable pilot before the much larger CASP
(151 studies) and MMAT (68) groups.

**Real environment blocker hit and disclosed to the researcher:** `WebFetch`
returned `EGRESS_BLOCKED` for every domain tried that hosts the actual
official checklists — `unisa.edu.au`, `bristol.ac.uk`, `cochrane.de`,
`methods.cochrane.org`, `training.cochrane.org`, `riskofbias.info`,
`corates.org`, `arxiv.org`, `strataresearch.net`, `pmc.ncbi.nlm.nih.gov`,
`en.wikipedia.org` — an organization egress-policy restriction, not
something to route around. `WebSearch` still worked and returned real,
citable excerpts. The researcher was asked directly (`AskUserQuestion`) how
to proceed and chose to continue on WebSearch snippets alone.

**Second, more specific tension surfaced and also put to the researcher:**
`04_quality/appraisal_forms/APPRAISAL_FORM.md` (written earlier in this
project, anticipating this exact blocked-network scenario) explicitly says
not to reconstruct a checklist from memory or partial sources, precisely
because an incomplete or approximated tool "produces a rating that means
nothing." WebSearch recovered RoB 2's Domains 1/2/4 reasonably completely
but only the general purpose of Domains 3/5; for ROBINS-I it recovered
solid signalling-question detail only for the Confounding domain, and only
domain *names* for the other six. Asked again, the researcher chose to
proceed with what could be recovered, explicitly marking incomplete domains
"not assessable — incomplete tool text obtained in this environment"
rather than guessing, and disclosing the limitation prominently rather than
presenting a partial appraisal as equivalent to a full one.

**What was produced:** 12 appraisal-form files in
`04_quality/appraisal_forms/` (`<study_id>_RoB2.md` /
`<study_id>_ROBINS-I.md`), each with a domain-by-domain table, real
citations to the extracted study text backing every judgement actually
made, and an explicit "Source of tool structure" section naming exactly
what WebSearch did and did not recover. `extraction_database.csv`'s
`risk_of_bias_rating` for all 12 is written as a partial/lower-bound value
(e.g. "Some concerns (partial pilot appraisal...)" / "at least Serious
(...)") rather than a bare tool-scale label, so it cannot be mistaken for a
complete official-tool rating; `selection_bias`/`measurement_bias`/
`confounding`/`attrition`/`reporting_bias` were filled from genuine
extracted evidence where available (e.g. S085's real 61.5% endline-
recontact/balance-test and pre-registration/Benjamini-Hochberg detail) and
marked not-assessable otherwise.

**One more finding surfaced in passing:** S235 (Dondeynaz et al. 2012,
WatSan4Dev cross-national indicator-database/factor-analysis study) does
not fit ROBINS-I's intervention-effect framing at all — it develops a
governance/WASH indicator database via factor analysis, not an
intervention evaluation. Flagged in its appraisal form as a likely
`risk_of_bias_tool` mis-assignment from an earlier extraction pass, but
**not corrected unilaterally** here since the appropriate alternative
tool/`study_design_class` was not re-derived from the source text in this
pass.

`code/analysis/validate_schemas.py` confirms all 13 checked files still
match their documented schema after these 12 rows were filled.

## 2026-09-16 — Preliminary cross-cutting evidence-limitations narrative; fixed 11 studies' mis-assigned risk_of_bias_tool

Third item of the user-approved non-PDF-dependent work plan: wrote
`04_quality/risk_of_bias/2026-09-16_evidence_limitations.md`, following the
structure of `EVIDENCE_LIMITATIONS_TEMPLATE.md`. `RISK_OF_BIAS.md` §3
specifies this narrative should be written only once every included study
has an individual appraisal rating — which has not happened (Phase 9 has
not been applied to any study). The file is explicitly labeled
preliminary/pre-appraisal: it covers only what corpus-composition fields
already support without a rating (design-class mix, mechanism_certainty
distribution, country/legal-system coverage, mechanism-family coverage,
abstract-only-extraction rate, use of the non-validated Legal Institutional
Evidence Appraisal Framework) and leaves "Overall confidence in the body
of evidence" as an explicit placeholder pending real Phase 9 ratings.

Headline findings: only 12 of 350 studies (3%) use a quasi-experimental or
experimental design, and mechanism_certainty confirms only 26 of 350 (7%)
reach "quasi-experimental" or "experimental" evidence directly — the
evidence base overwhelmingly documents association, not causation. 16% of
studies (57/350) were abstract-only extractions. Brazil/India/South Africa
account for 30% of country coverage. Common law and civil law systems are
close to evenly represented (140 vs. 138 of 350), with 43 mixed/hybrid/
customary-overlay and 28 with a blank `legal_system` field (a real,
unaddressed extraction gap).

While compiling the narrative, found and fixed a real data bug: of the 17
studies flagged `study_design_class = systematic_review_secondary` (for
which `RISK_OF_BIAS.md` specifies AMSTAR 2 is the correct instrument),
11 (S319–S329, added in the 2026-09-16 E12-policy-amendment batch) had
been left with `risk_of_bias_tool = CASP` — an apparent carry-over default
from that batch's extraction script. Corrected all 11 to the same
AMSTAR-2 label used for the other 6 systematic-review studies
(S015, S019, S027, S052, S079, S116), with each row's `extraction_note`
recording the correction. `study_design_class` was already correct for
all 17 and did not need to change. `validate_schemas.py` confirms all 13
checked files still match their documented schema after this fix.

## 2026-09-16 — First population of `effect_sizes.csv`: 11 rows from the 124 quantitative-synthesis-eligible studies

With no new PDFs pending, worked through the user-approved plan's second
item: populating `05_analysis/effect_sizes/effect_sizes.csv` (previously
header-only). Per `DATA_DICTIONARY.md` and
`03_extraction/extraction_form/EXTRACTION_FORM.md`, this file is **not** a
mirror of every `evidence_map.csv` row flagged
`quantitative_synthesis_eligible = TRUE` — it records only effects that are
actually judged eligible for quantitative synthesis per
`ANALYSIS_PLAN.md` §2's decision tree (a clearly defined exposure, a
meaningful comparator, a clearly defined and in-scope outcome, and an
available or defensibly calculable effect estimate).

Reviewed all 124 quant-eligible studies' full extracted effect data
(`extraction_database.csv`'s `effect_measure`/`effect_estimate`/CI/SE/
`p_value`/`model_type`/`study_design` fields). The large majority are
single-group descriptive statistics with no defined comparator and were
correctly left out. Identified **11 studies** with a genuine,
non-fabricated exposure-vs-comparator contrast and a locatable numeric or
faithfully-summarized effect: **S037, S057, S084, S085, S104, S142, S149,
S174, S178, S294, S312**. Also re-checked three studies that looked
superficially promising and excluded them because the exposure or outcome
did not match a legal/institutional exposure or an access-outcome in
`PROJECT_SPEC.md` §8's scope: **S006** (real OR=18.12 but for a
"management-strategy effectiveness" outcome, not access), **S039** (no
defined legal/institutional exposure-comparator, purely descriptive), and
**S135** (racial composition, not a legal/administrative exposure, drives
the model). A follow-up keyword/CI sweep across the remaining 110
quant-eligible studies not in the original 14-study working list turned up
11 more regression-bearing candidates (S060, S062, S070, S075, S081, S143,
S189, S213, S219, S282, S348); each was checked and excluded for the same
reasons (before/after with no comparator, non-legal exposure, or no
locatable numeric effect) — none added.

Of the 11 rows added: **4 assigned to `PROJECT_SPEC.md` §8 Family A**
(legal recognition/eligibility → access: S037, S057, S084, S142; S104 also
tagged Family A but flagged with a caveat that its tenure exposure is one
covariate among several, not a dedicated test), **2 to Family B**
(administrative assistance → connection/formalization: S085, S294), **1 to
Family C** (institutional capacity as an administrative-barrier proxy:
S174), and **3 left with no family** (S149, S178, S312) because their
exposure or outcome does not match any of the three existing families'
definitions as written — per `DATA_DICTIONARY.md`'s allowance for "a newly
identified family," but a single study each does not justify formally
defining one yet. S312's case also surfaced a coding issue worth flagging
without unilaterally fixing it: `evidence_map.csv` codes its outcome as
`effective_access`, but the actual outcome is jurisdiction-level policy
adoption (a shutoff moratorium), not household access — noted in the new
row's `provenance_note` rather than silently pooled or silently corrected.

Every row has `included_in_pooled_estimate = FALSE`, since no actual
meta-analytic pooling has occurred in this project (still pre-Phase-12);
each `exclusion_from_pooling_reason` cites the specific
`ANALYSIS_PLAN.md` §2 decision-tree branch responsible (most commonly:
single study per exposure-comparator definition, or a numeric effect size
not locatable in the extracted abstract text without re-extracting the
full source PDF, which was not done rather than approximated, per
`PROJECT_SPEC.md` §14).

`code/analysis/validate_schemas.py` confirms `effect_sizes.csv` (17
fields) still matches its documented schema; all 13 checked project CSVs
pass. No other file changed.

## 2026-09-16 — Post-hoc duplicate-detection audit: one true duplicate found and removed (S227)

While waiting on further PDFs, ran a full duplicate audit across all 351
included studies: exact-DOI matching, exact-normalized-title matching,
fuzzy-title similarity (difflib ratio > 0.85), and duplicate-record_id
matching (all extraction_note "record_id" references, using a corrected
regex — the first attempt missed 8 early studies, S076–S083, whose notes
predate the standardized "record_id X." phrasing).

Found exactly one genuine duplicate: **S063 and S227** were independent
extractions of the same underlying paper (Pastrana-Miranda & Gonzalez-Caamal
2022, same DOI `10.12804/revistas.urosario.edu.co/territorios/a.9931`)
ingested into the search corpus under two different record_ids
(`RF043AAD78E8E` and `R7EECD84CD3AA`) that the original deduplication script
(`code/search/deduplicate.py`) failed to merge, and which were then
independently screened and extracted without either pass detecting the
overlap. S063 is the fuller extraction (documents specific 2015 INEGI
census statistics and both `DISCRETION_ACCOMMODATION`/institutional-
fragmentation mechanisms); S227 duplicated the same content at lower detail
and has been removed. `R7EECD84CD3AA`'s decision was changed from `include`
to `exclude` (E08, duplicate of `RF043AAD78E8E`), and its rows removed from
`extraction_database.csv` and `evidence_map.csv`. **`S227` is now a
permanent gap in the study_id sequence** (not renumbered, to avoid
disturbing every cross-reference to S228–S351 already committed across
prior batches) — this is intentional, not a data error.

No other duplicates (exact or fuzzy) were found across the remaining 350
studies.

Net: 351 → 350 includes, 406 → 407 excludes; decided count unchanged (757).

## 2026-09-16 — Fourteenth full-text screening batch: 7 records via direct chat upload, 4 new includes (S348–S351)

Seven PDFs supplied directly via chat upload (no record_id in filename this
round — matched to `full_text_screening_database.csv` by title instead).
Four included: Andrews, Beynon & Baafi (2025, Ghanaian local-government
infrastructure access and governance quality, S348); Hanjabam (2018,
community-managed 24x7 rural water supply model, Manipur, India, S349);
Abdulhadi, Bailey & Van Noorloos (2024, PRISMA scoping review of WASH/housing
access inequalities in LMIC slums, S350, reinstated per the E12
secondary-review policy); Nastar, Isoke, Kulabako & Silvestri (2019, politics
of land tenure and water access, Kampala, Uganda, S351). Three excluded: a
2007 conceptual/policy essay on macro-scale climate-adaptation financing with
no empirical last-mile data (E05); a mixed-methods study of sanitation
*workers'* occupational PPE use rather than household access (E02, wrong
population); and an urban-morphology/spatial-form study where water/sanitation
access was only a minor secondary household-survey variable (E01).

Net: 347 → 351 includes, 403 → 406 excludes, 750 → 757 decided.

## 2026-09-16 — Twelfth and thirteenth full-text screening batches: 26 records decided (18 new includes, S330–S347), from direct chat upload and a Drive "proxy_downloads" folder

Two records supplied directly via chat upload were screened first
(R3A70FDFC6D73, a Peru academic specialization thesis with real
mixed-methods primary data — 120 households plus institutional
interviews — diagnosing sanitation-coverage and institutional-coordination
determinants of child diarrheal-disease risk, included as S330 despite its
health-outcome framing, given the genuine institutional/access data;
R7FB99A985F04, a systematic review of climate-resilient infrastructure in
informal settlements broadly — flooding, drainage, green infrastructure,
energy systems — excluded E01 as out of this review's water/sanitation
access-governance scope even though water/sanitation appears as one of
several intervention types it covers).

The researcher then pointed to a new Drive folder ("proxy_downloads")
delivering 24 further PDFs, 2 of which duplicated the just-uploaded pair.
Before screening the remaining 22, every one of the 24 record_ids was
verified against `full_text_screening_database.csv`'s real
`full_text_status`/`final_decision` columns (the exact check that was
missing in the earlier TEST ZIP mistake) — confirming all 22 were
genuinely open, not decided elsewhere. Of the 22: 17 included (S331–S347)
and 5 excluded (E01×3, E04×1, E06×1).

Net effect: full-text decided count 724 → 750; includes 329 → 347;
excludes 395 → 403; extraction database 329 → 347 studies (S330–S347).

## 2026-09-15 — Eleventh full-text screening batch (107 records from an external OA-retrieval mission's Drive delivery), data-integrity correction, and E12 (secondary/systematic review) policy amendment

A researcher-run external tool ("Antigravity") independently executed an
Unpaywall/OpenAlex open-access retrieval mission against the review's full
record pool and pushed its tracking CSVs directly to this branch as commit
`bed36a4` (74 `full_text_retrieval_results_*.csv` files in
`02_screening/full_text/retrieval_results/` + one empty SSRN raw-export
file). Per this project's standing convention, the retrieved PDFs
themselves were deliberately kept out of the git repository (stored only
on the researcher's local machine); only the CSV tracking files were
committed. The commit was independently verified (`git fetch` + `git show
--stat`) before being merged — it was purely additive and touched no
existing tracked file.

Cross-referencing the 541 `retrieved` record_ids in those CSVs against
`full_text_screening_database.csv` found 322 corresponding to
still-open-queue records; of those, 107 were reachable to this AI session
via a Google Drive folder ("TEST ZIP") the researcher subsequently shared,
containing the actual retrieved PDFs for that subset. The remaining ~215
retrieved-but-unreachable PDFs stay on the researcher's local machine,
outside this session's access, pending the researcher supplying them via
chat or Drive in a future batch.

**Data-integrity bug and correction (disclosed for transparency and
reproducibility):** an initial cross-reference script used to classify the
107 "TEST ZIP" record_ids as open-vs-decided checked a non-existent
`screening_decision` column instead of `final_decision`, so it wrongly
reported all 107 as unscreened. On that false premise, all 107 were
re-screened, re-extracted (as S318–S372) and pushed into
`evidence_map.csv`. A direct count against the committed baseline exposed
the error (decided-record counts barely moved despite 107 "new" decisions
having ostensibly been recorded), and a full audit against the
pre-batch committed state found: **5** record_ids were genuinely new
(never previously decided); **48** were already-`include` duplicates
(already extracted under an earlier S-number — S318–S372 duplicated 48
existing studies); **41** were already-`exclude` duplicates; and **13**
had a re-judgment that *conflicted* with the original decision. All
duplicate/erroneous `full_text_screening_database.csv` rows,
`exclusion_log.csv` entries, `extraction_database.csv` rows and
`evidence_map.csv` rows were reverted to their pre-batch state; the 13
conflicts were surfaced to the researcher rather than resolved
unilaterally. Net legitimate result of the 107-file batch: **1 new
include** (S318, Shrestha et al. 2023, Nepal WASH status review) and 4 new
excludes (E01×1, E04×1, E06×1, E10×1) from the 5 genuinely-open records;
plus 21 records independently confirmed as E10 bot-block/placeholder
artifacts via the established byte-size cluster-sampling method.

**Root-cause lesson for all future batches:** before treating any record
as "open" for screening, cross-reference scripts must read the exact
existing column names (`full_text_status`, `full_text_decision`,
`final_decision`) from `full_text_screening_database.csv` — never assume a
column name without confirming it against the file's actual header first.

**E12 (wrong study design) policy amendment, applied retroactively
project-wide:** of the 13 conflicting re-judgments, the researcher
confirmed that 3 stemmed from E12 having been applied to secondary/
systematic literature reviews on the basis that they are "not primary
empirical research" — but `CODEBOOK.md` lists `systematic_review_secondary`
as a valid `study_design_class`, so review-type studies are legitimate
evidence for this review, not automatically out of scope. Searching the
full `exclusion_log.csv` for the same rationale found 11 records
project-wide (not just the 3 from this batch) excluded on that same
"secondary review, not primary research" basis; the researcher confirmed
the amendment should apply to all 11 for consistency. All 11 were flipped
to `include`, reinstated in `extraction_database.csv` (S319–S329) as
`study_design_class = systematic_review_secondary`, and their
`exclusion_log.csv` entries removed. Two other E12 exclusions with a
*different* rationale (a government white paper with no original
empirical data, and a multi-chapter edited volume not extractable as a
single study) were left excluded — the amendment applies specifically to
the "it's a review, not primary research" rationale, not to E12 generally.
The remaining 10 of the original 13 conflicts (abstract-only re-judgments
disagreeing with an earlier abstract-only decision, neither grounded in
verified full text) were left at their original decision per researcher
instruction, since nothing more authoritative than the original judgment
was established.

Net effect on the database from this whole batch: full-text decided count
719 → 724 (+5 genuinely new); includes 317 → 329 (+1 new TEST ZIP include,
+11 E12-policy reinstatements); excludes 402 → 395 (net -7, reflecting the
11 E12 reinstatements against +4 new TEST ZIP excludes); extraction
database 317 → 329 studies (S318–S329).

## 2026-09-15 — Tenth full-text screening batch: 213 records decided from a third Drive folder, 68 new includes (S250–S317), byte-size cluster-sampling methodology and repository-landing-page-abstract policy formalized

Processed all 213 files from a third Google Drive folder (folder id
`1JxeuCz3dm4HWtkdZ1zpeMXU4R4WDBwY8`).

**Screening methodology for this batch, disclosed for transparency:**
109 of the 213 files were under 20KB. Rather than reading each
individually, one fileId per exact-byte-size cluster was read to
verify the cluster's content, and the verified classification was then
applied to every other file sharing that exact byte size. This
identified 10 distinct patterns — empty files (14), a Radware/IOP Bot
Manager captcha block (6, all exactly 14,371 bytes), a UBC "sorry for
the inconvenience" block (2, 4,935 bytes), an Anubis bot-challenge page
across four size variants (9), a Project MUSE "verification required"
page (1), a listed-size-vs-actual-empty mismatch (1), a JavaScript-
required app shell (1), a "client challenge...JavaScript is disabled"
page (1), and a "Redirecting..." placeholder page spanning a ~2,680–
3,050-byte range verified via roughly ten independent spot-checks
across the cluster (73) — none of which are actual paper content, so
all 108 of these files (one further file in this size range, see next
paragraph, was excluded from the E10 bulk-classification) were recorded
as E10 without individual reads. The remaining 104 files (≥20KB) were
each read and screened individually against the project's E01–E12
criteria.

**Repository-landing-page-abstract policy (new, applies to all future
batches):** one of the byte-size-cluster files initially flagged as a
likely bot-block/placeholder turned out, on inspection, to be a
publisher/repository landing page carrying a genuine, correctly-
matched abstract but no full-text PDF body. Several more files in the
individually-screened 104 turned out to be the same kind of landing
page. Rather than continue treating "no full-text body retrieved" as
automatic E10, a policy is now in force: a landing page with a
genuine, identifiably-correct abstract is screened for inclusion like
any other abstract, and if included is extracted at abstract-level
granularity only (country, legal system, population, the four
mechanism booleans, a paraphrased effect estimate, and study
design/risk-of-bias tool where inferable from the abstract), with an
`extraction_note` explicitly disclosing "extracted from published
abstract/repository metadata only; full PDF text not retrieved via
fetch." E10 is now reserved strictly for bot-blocks, empty files,
placeholder/redirect-only pages, or content that is not identifiably
the correct paper. This reverses the ad hoc treatment used for a small
number of similar cases in earlier batches and was applied
retroactively within this batch once formalized (one file,
`schwartz_2023`, was provisionally bucketed into the size-cluster E10
sweep before the policy was finalized and was pulled out and given a
real INCLUDE judgment under the new policy).

**68 included and fully extracted** (S250–S317): studies span utility
managerial decision-making on prepaid water technology for low-income
areas (Kenya); village health/sanitation/nutrition committee
functioning and contextual barriers to participation (India);
century-long historical-institutional water/sewerage governance
regimes — state monopoly, private concession, re-nationalization
(Buenos Aires); environmental-health-literacy barriers to navigating
water-quality law on Tribal lands (USA); gram panchayat organisation-
development and local-government service delivery (Karnataka, India);
water-rationing politics during drought crisis (São Paulo, twice, plus
a third paper on the same crisis); customary/local water-rights
formalization and its double-edged effects on marginalized-group water
security (Peru, twice); school WASH facility management and gendered
maintenance burden (Ghana); water-access exclusion from formal
governance decision-making and maternal health (rural Malawi); climate-
resilience institutional gaps in small-town water utilities (Ethiopia);
national SDG 6 progress review (Nigeria); informal water-vendor market
structure and its linkages to formal utility revenue (Lodwar, Kenya);
historical water/sanitation policy stages and universalization
challenges (Argentina, two papers); comparative formal/informal water-
delivery configurations methodology (Peru and Ghana); water
re-allocation as distributive/recognitional/participatory justice
(India); sanitation-law regional coverage disparities (Brazil); rural
drinking-water tap-connection-coverage-vs-functionality gap (Satara,
India); governance failure, corruption, and "hydraulic apartheid"
(South Africa); geodemographic water-management-modality analysis
(Oaxaca, Mexico); WASH institutional-capacity gaps in a refugee-crisis
context (Cox's Bazar, Bangladesh); rural water/sanitation project-
management-model legal-compliance evaluation (Colombia); urban-poor
sanitation-programme mismatch across four cities; technocratic vs
participatory water-crisis governance (Brazil); a sanitation human-
vulnerability index (Paraíba, Brazil); IWRM operationalization and
inequitable access (Karnataka, India, two papers via different
frameworks); socio-spatial water-supply/consumption inequality
(Tijuana, Mexico); peri-urban/rural water-supply inefficiencies
(Colombia); legal-economic affordability of water-access rights
(Puerto Vallarta, Mexico); urban water-supply trend/change-point
dynamics vs stagnant household access (Gondar, Ethiopia); territorial
water-vulnerability indexing (Gran Valparaíso, Chile); handpump-payment
institutional models (rural Kenya); household water-source choice and
gendered collection-time burden (Madagascar); gender/social-inclusion
gaps in WASH institutional structures (Nepal); multilevel-governance
water-supply public-private partnerships (Indonesia); a stratified-
sampling methodology for measuring human-right-to-water access
disparities; informal-settlement infrastructure co-construction and
rights-claiming (Belo Horizonte, Brazil); sachet-water consumption
driven by municipal rationing (Accra, Ghana); unregulated urban sprawl
and public-service strain (Baghdad); comparative municipal public-
health-service governance (Chennai vs Delhi); informal privatisation of
community taps (rural Nepal); water-security/infrastructure-age gaps
(Guwahati, India); citizen-participation dilemmas in water governance
(Kumasi, Ghana); a cluster-RCT of a WASH intervention's null health
effect but positive local-institution effect (rural DR Congo); social-
tariff coverage/incidence variation in basic sanitation (Brazil);
citywide pit-emptying/transport sanitation-service tariff-setting
(Kenya and Zambia); a critical-institutionalism/political-economy
framework for rural water institutional change; colonial-to-post-
colonial water/sanitation service history (Mombasa); doctrinal legal
analysis of water-service consumer/user rights (Argentina) and of the
UN Special Rapporteur mandate on the human rights to water and
sanitation; indigenous water-rights struggle against an irrigation
project (Peru); rural water-policy design across Africa and Asia;
community water-quality perception over time (El Salvador); denial of
shelter/water/sanitation access to homeless Roma EU migrants (Sweden);
sanitation public-private partnership coverage gains (Esteio, Brazil);
customer-attrition mitigation in container-based sanitation
organizations; collective self-organization for informal water
distribution (Xochimilco, Mexico City); human-right-to-water rural
access monitoring methodology (Nicaragua); pro-poor rural water/
sanitation policy implementation under decentralization (Tanzania, two
papers); COVID-19-era water-shutoff-moratorium adoption predictors
(USA); school drinking-water-access compliance-audit gaps (Massachusetts,
USA); peri-urban waterscape planning-policy blind spots (Ghaziabad,
India); comparative drinking-water-quality governance (Brazil/Ecuador/
Malawi); and a global urban-water-tariff survey (308 cities, 102
countries).

**145 excluded**: E10 inaccessible/mismatched full text ×120 (108 via
the verified byte-size-cluster sweep described above, plus 12 further
individually-confirmed bot-blocks, empty-content responses, or
metadata-only landing pages lacking any abstract text among the 104
individually-screened files); E01 wrong topic ×17 (agricultural/
irrigation water-rights and water-grabbing studies, marine-protected-
area/fisheries management, tourist-facility infrastructure, broad
natural-resource-access frameworks bundling water with land/grazing/
forest, macro water-resource governance/coordination studies, a
development-cooperation/foreign-aid mapping study, and other papers
whose empirical focus lay outside last-mile household/community access
governance); E12 wrong study type ×2 (a narrative literature review and
a multi-chapter edited book, neither extractable as a single primary
study); E04 wrong outcome ×1 (access disparity used only as a COVID-19
epidemiological-risk covariate); E03 wrong exposure ×3 (water-quality/
environmental-health or groundwater-contamination studies where access
governance was not the analytic focus); E06 engineering only ×1
(wastewater-treatment-technology adoption survey); E08 duplicate ×1 (a
Portuguese-language SciELO republication of an already-included
English-language paper on colonial environmental racism in Brazilian
sanitation, S239/batch-nine).

Ran `code/analysis/build_evidence_map.py` to mechanically derive
`study_design_class` (13 studies using the project's Legal
Institutional Evidence Appraisal Framework tool required manual
`doctrinal`/`jurimetric` classification per `RISK_OF_BIAS.md` §2 — 11
doctrinal, 2 jurimetric) and `mechanism_family`; filled `outcome_family`,
`quantitative_synthesis_eligible`, and `qualitative_synthesis_eligible`
by hand for all 68 new studies. Regenerated
`full_text_retrieval_queue.csv` (2,940 open records) and reran
`validate_schemas.py` — all 13 checked files still match their
documented/generated schema. Updated `PRISMA_WORKFLOW.md`, `README.md`,
`06_outputs/prisma/prisma_flow.md`, and
`06_outputs/supplementary/preliminary_results.md` with the new totals,
derived programmatically from the CSVs rather than hand-computed.

## 2026-09-15 — Ninth full-text screening batch: 52 records decided from second Drive-folder ("folder 2"), 27 new includes (S223–S249), 3 independently-reverified content-mismatch findings

Processed all 52 files from a second Google Drive folder ("folder 2",
subfolder of `1Wouws6UtI2bMXwJVSHV5J3ILZ0OsEycV`, folder id
`14kIEZBIkeEyKnVr0NQs1nFDh7ncK5Vcl`).

**Data-integrity note on this batch's process:** the screening judgments
for this batch were first made in a conversation segment that was
summarized before the decisions were written to any script or CSV. On
resuming, the prior segment's conclusions existed only as an unpersisted
summary — no decision had actually reached durable storage. Rather than
transcribe the summary's claims from memory, every one of the 52 files
was re-read and re-screened from the source PDF content in this segment,
including an independent re-verification (a fresh, isolated re-read of
each fileId) of the three files the prior segment had flagged as
content-mismatched, before any exclusion decision was recorded.

**27 included and fully extracted** (S223–S249): studies on
cooperative/state water-and-sanitation provision and regulatory-subsidy
asymmetry (Santa Fe and Buenos Aires provinces, Argentina); urban-rural
drinking-water disparities and water justice (Lilongwe, Malawi);
wastewater-plant siting and "sacrifice zone" household access
(Zapopan, Mexico); water-distribution centralization and environmental
injustice (Valle de Mexico); community-based water management filling
gaps in formal supply (rural Mexico); informal-settlement water access
(Valparaiso, Chile); decentralized rural water-service governance
information flows (Uganda); water-access public-policy implementation
and socio-spatial segregation (Aguas-Lindas, Brazil); comparative
national drinking-water-coverage regulatory gaps (Panama vs. Costa
Rica); informal-settlement sanitation management (San Jose, Costa
Rica); peri-urban municipal-service-capacity lag (Makhado, South
Africa); cross-national water/governance/human-development indicator
analysis; differential urban-rural regulatory schemes for water supply
(Colombia); county-level water policy and devolved governance (Kitui,
Kenya); developmental local government and service-delivery obstacles
(South Africa); racialized/colonial continuum of sanitation deprivation
(Brazil); comparative First Nation vs. non-First Nation drinking-water
systems (Ontario, Canada); rural water-supply-sustainability
determinants (Quang Ninh, Vietnam); comparative water/sewage
concession-contract analysis (Brazil); community-based governance and
equitable access for the urban poor (India); institutional-capacity
gaps for rural sanitation (Eastern Cape, South Africa); national
water/sanitation regulatory-framework analysis (Malawi); a universal-
WSS-access governance-model project (Minas Gerais, Brazil);
institutional causes of insufficient water supply, incl. a legal
land-tenure eligibility gate on piped-water connection (Tegucigalpa,
Honduras); an unregulated joint community-corporate water-supply
partnership (Cameroon); and historical-institutionalist path-dependency
analysis of Brazil's national sanitation regulatory-regime formation.

**25 excluded**: E01 wrong topic ×9 (broad IWRM/water-resource-policy
reviews, ICT/technology-management studies, groundwater-banking supply-
side infrastructure, SDG macro-indicator tracking, network-alignment
methodology papers, environmental-services/watershed-conservation legal
instruments, and a broad urban-planning/social-class-conflict theory
paper mentioning sanitation only in passing); E03 wrong exposure ×1
(endocrine-disruptor chemical/regulatory screening); E05 no empirical
evidence ×2 (two GIS/triangulation policy-landscape review papers by
the same author pair, explicitly preliminary with "data...remains
sketchy"); E06 engineering only ×3 (anaerobic-baffled-reactor
wastewater-treatment review; surface-stream-water engineering
assessment; urban-design/GIS drought-vulnerability mapping); E12 wrong
study design ×2 (two secondary systematic reviews/meta-analyses); E10
inaccessible/mismatched full text ×8 — 5 genuine bot-block/empty-file
cases (Anubis and Incapsula challenge pages, one empty file) plus 3
content-mismatch cases, each independently re-verified by a fresh,
isolated re-read of the same fileId: a fileId expected to contain a
water-institutional paper instead contained an unrelated cross-sectional
survey on rural latrine use (Tamilarasan et al., Perambalur District,
India); a fileId expected to contain a journal article instead
contained the "New Jersey Water Supply Plan 2017-2022" (a 484-page
NJDEP planning document); and a fileId expected to contain a
water-institutional paper instead contained an unrelated microbiology
paper on lantibiotic production by *Bacillus licheniformis*. None of
the three mismatched contents self-identified as belonging to another
record tracked in this batch, so no secondary decision was fabricated
from any of them — each was recorded solely as an E10 exclusion of the
record it was expected to represent.

Ran `code/analysis/build_evidence_map.py` to mechanically derive
`study_design_class` (7 studies using the project's own Legal
Institutional Evidence Appraisal Framework tool required manual
`jurimetric` classification, since the tool name alone can't
distinguish doctrinal from jurimetric per `RISK_OF_BIAS.md` §2) and
`mechanism_family` (3 studies needed manual classification where only
non-core institutional-process fields, not the 4 core mechanism
booleans, had been set); filled `outcome_family`,
`quantitative_synthesis_eligible`, and `qualitative_synthesis_eligible`
by hand for all 27 new studies. Regenerated
`full_text_retrieval_queue.csv` (3,153 open records) and reran
`validate_schemas.py` — all 13 checked files still match their
documented/generated schema. Updated `PRISMA_WORKFLOW.md`, `README.md`,
`06_outputs/prisma/prisma_flow.md`, and
`06_outputs/supplementary/preliminary_results.md` with the new totals,
derived programmatically from the CSVs rather than hand-computed, and
opportunistically corrected several pre-existing stale figures in the
same files left over from before this batch (e.g. a stray "196
extracted studies" Phase 9/10 reference and a stray "222" reference
that predated this batch's renumbering).

## 2026-09-15 — Eighth full-text screening batch: 57 records decided from second Drive-folder sweep, 26 new includes (S197–S222)

Processed the remaining 57 not-yet-decided files in the first Google Drive
folder (`1q_H3SrhYEGwQR-04WZP7Nqxex7CtpyF1`, files 43-100 of its 100-file
listing; the other 43 were duplicates of records already decided in
earlier local-upload or Drive batches).

**26 included and fully extracted** (S197–S222): studies on state-NGO
service-delivery partnerships (Pakistan), human-rights/legal analyses of
sanitation and water-affordability protection (Alabama, Spain x2),
decentralized-sanitation regulatory-framework analysis (Brazil x3, one
covering the 2020 national WSS-sector reform), decentralized/self-supply
water-governance case studies (Namibia, South Africa x2), a feminist
political-ecology food/water-security study (Nicaragua), collaborative
water-governance network resilience (Ecuador), a cross-national
household-infrastructure-access index (Africa), Free Basic Sanitation
policy-implementation studies (South Africa, Malawi), a sanitation
Technological-Innovation-System case study (Nairobi), CLTS adoption among
tribal communities (India, Swachh Bharat Mission), a social-accountability
before/after water-governance evaluation (Uganda), a municipal
water-food-governance nexus household survey (Zimbabwe), municipal
water/sanitation institutional diagnostics (Senegal, Cameroon), unequal
socio-spatial drinking-water-infrastructure outcomes (rural Bihar, India),
a theoretical-plus-empirical study of political interference in
sanitation-tariff regulation (Brazil), an ethnographic study of urban
sanitation-governance deficits and "slumification" (Uganda), a
political-ecology comparison of water-contamination governance responses
(Ireland), and a qualitative study of sanitation-access barriers for
disabled individuals despite formal legal accommodation entitlements
(Uganda).

**31 excluded**: 17 as E10 (inaccessible full text) and 14 for
substantive reasons (E01 wrong topic ×4, E04 wrong outcome ×3, E06
engineering only ×3, E12 wrong study design ×2, E01/E12 mix as detailed
in `exclusion_log.csv`). The E10 group includes two newly-confirmed
Unpaywall-failure byte-size signatures beyond the ones already documented
in the sixth-batch entry below: 8 files at exactly 14,371 bytes all
independently verified (4 of 8 read directly, remaining 4 pattern-matched
on the identical byte count) as the same IOP Publishing "Radware Bot
Manager Captcha" page, and 2 files at exactly 751 bytes both verified as
a bare "DSpace" repository placeholder page; plus one genuinely 0-byte
file, four distinct bot-verification/access-block pages (Anubis "Making
sure you're not a bot!" ×2, a "High Load - Verifying Browser" holding
page, and a BunkerWeb block page), and two bare redirect/download-holding
stub pages ("Redirecting" and "Preparing to download...") with no
retrievable content.

Regenerated `full_text_retrieval_queue.csv` (3,205 open records),
re-ran `validate_schemas.py` (all 13 files pass), and updated
`PRISMA_WORKFLOW.md`, `README.md`, `06_outputs/prisma/prisma_flow.md`,
and `06_outputs/supplementary/preliminary_results.md` with the new
totals: 454 of 3,659 full-text records decided (222 include / 232
exclude); 222 studies fully extracted (S001–S222); 83 of 222 judged
eligible for quantitative synthesis, 197 for qualitative synthesis.

## 2026-09-15 — Seventh full-text screening batch: 16 more records decided, 10 new includes (S187–S196), first content-mismatch data-integrity finding

Continued through the same Google Drive folder (records 27-42 of the
first 100-file batch). **10 included and fully extracted** (S187–S196):
community-based rural water/sanitation management studies in Ghana
(Braimah et al.; Kumasi), a cluster-RCT-linked process evaluation of a
government sanitation campaign in Orissa, India showing an 8%-to-66%
latrine-coverage increase, a documentary analysis of Brazilian federal
sanitation-investment policy, a private social-enterprise water/health
service study in conflict-affected DRC showing fee-based affordability
as the dominant access barrier, a stratified community-leader survey on
land-regularisation and social-tariff barriers in irregular Brazilian
settlements, an institutional case study of groundwater-licence
allocation producing spatial access disparities in peri-urban Bangladesh,
a public-private sanitation-delegation programme evaluation in
Ouagadougou (6.1%→17% access increase), an ASPIRE-toolkit slum-upgrading
sustainability assessment in Dhaka, and a doctrinal case-docket analysis
of judicial enforcement (or non-enforcement) of Brazilian public civil
actions ordering sanitation provision.

**6 excluded** (E01 wrong topic ×2, E04 wrong outcome ×1, E10
inaccessible full text ×2, E12 wrong study design ×1). One exclusion (a
Roman-law legal-history article on ancient water rights) was judged E01
as outside the review's contemporary-service-access scope rather than
E11, since no jurisdiction match was even attempted.

**First content-mismatch data-integrity finding this session**: the file
stored under one record's expected filename (`R512107239D86_dapaah_2017.pdf`,
a tiny 4,935-byte file) did not actually contain that record's content —
reading it returned the full text of an entirely different, unrelated
article (which, by its own title/DOI, was independently verified against
`screening_database.csv` to be the paper belonging to a *different*
record already in this batch, `R65D5267860B3`, Pu et al.'s systematic
review). Rather than fabricate an extraction for the Dapaah record from
content that is not actually its own, `R512107239D86` was excluded E10
(full text genuinely inaccessible/misdirected in this environment) and
`R65D5267860B3` was independently excluded E12 on the strength of the
title/abstract/DOI evidence recovered from the misdirected file, cross-
referenced against the title/abstract screening database. This is most
likely an artifact of the researcher's Unpaywall bulk-fetch pipeline
(the fetch step resolving to the wrong PDF for one DOI), not something
introduced by this session's processing, and is flagged here rather than
silently worked around.

`full_text_screening_database.csv` now stands at 397 of 3,659 decided
(196 include / 201 exclude); `extraction_database.csv` and
`evidence_map.csv` both hold 196 fully-extracted studies (S001–S196),
with schema validation (`validate_schemas.py`) passing for all 13
tracked files and the retrieval queue regenerated (3,262 open records).

## 2026-09-15 — Sixth full-text screening batch: first Google Drive bulk retrieval, 24 records decided, 17 new includes (S170–S186)

The researcher, in response to the operational burden of chat-uploading PDFs
five at a time, switched to a bulk-retrieval workflow: after running the
open records through the Unpaywall API (confirming 282 of the 3,278
remaining records have an open-access PDF available, with the rest behind
hard publisher paywalls), the researcher shared a Google Drive folder
containing the successfully-retrieved PDFs for direct access via the
Drive connector, rather than continuing one-by-one chat uploads. This
first folder contains 100 files; 24 were screened this round (3 duplicated
records already decided in earlier batches were skipped; the remaining
~73 and a second, still-uploading folder are queued for the next round).

**17 included and fully extracted** (S170–S186), spanning groundwater and
urban water governance studies (Kenya, India, Hyderabad), institutional-
capacity/regulatory analyses of sanitation universalization (Brazil,
including a national multivariate regression on institutional capacity
and access indicators), a large adjusted logistic-regression study of WASH
access and Water Safety Plan programming in conflict-affected southern
Syria (mOR 24.16, 95% CI 5.93–98.5), qualitative institutional-governance
case studies (Uganda, Switzerland, South Africa, Costa Rica), a corruption
agent-based model of water service delivery (Kenya/Ghana), an fsQCA study
of water-committee governance conditions, and a documentary "infrastructural
violence" analysis of exclusionary water policy/legislation/planning in
Delhi.

**7 excluded** (E01 wrong topic ×2, E06 engineering only ×1, E05 no
empirical evidence ×1, E10 inaccessible full text ×3), full reasoning
logged per-record in `exclusion_log.csv`. The E10 code (inaccessible full
text) was used for the first time this session: three Unpaywall-sourced
files turned out, on inspection, to be a zero-byte PDF, an empty-content
extraction, and a bot-verification challenge page respectively, rather
than the actual article — a genuine Unpaywall/open-access retrieval
failure distinct from the researcher's own upload process. A cluster of
other files in the same folder shared suspiciously identical small byte
sizes (e.g., exactly 14,371 bytes across eight differently-named files);
these are queued for a similar accessibility check before being screened
as content.

`full_text_screening_database.csv` now stands at 381 of 3,659 decided (186
include / 195 exclude); `extraction_database.csv` and `evidence_map.csv`
both hold 186 fully-extracted studies (S001–S186), with schema validation
(`validate_schemas.py`) passing for all 13 tracked files and the retrieval
queue regenerated (3,278 open records).

## 2026-09-15 — Fifth full-text screening batch: 61 records decided, 29 new includes (S141–S169)

A fifth, much larger wave of 61 researcher-supplied full-text PDFs was
screened against `INCLUSION_EXCLUSION.md`. **29 included and fully
extracted** (S141–S169), spanning informal/hybrid governance mechanisms in
Nairobi and Cape Town informal settlements (S141, S147, S153, S154, S165),
municipal-incorporation and jurisdictional eligibility barriers to
infrastructure connection (S142), a quasi-experimental before/after Water
Safety Plan evaluation in Uganda (S143), regulatory/institutional analyses
of sanitation and water governance in South Africa, Indonesia, Brazil,
Chile, and Zambia (S144–S146, S159, S161), doctrinal legal-historical
studies of water-sector privatisation/remunicipalisation in Hungary and
France (S148, S162), a propensity-score-matched study of women's
participation in Village Water and Sanitation Committees in Odisha, India
(S149), caste-based exclusion from water/sanitation access for Harijan
communities in Bangladesh (S151), documentary/jurimetric policy analyses of
national water-financing and affordability schemes in India, Brazil, and
Mexico (S152, S156, S158, S164, S166), and several affordability/tariff-
fairness and institutional-capacity studies (S150, S160, S163, S167–S169).

**32 excluded** (E01 wrong topic ×11, E02 wrong population ×2, E04 wrong
outcome ×5, E05 no empirical evidence ×1, E06 engineering/technical ×4, E07
wrong service ×3, E12 wrong study design ×6), full reasoning logged
per-record in `exclusion_log.csv`. The E12 code (six systematic/narrative
reviews and one primary government policy document masquerading as a
study) was used for the first time this session; several water-resources-
management and multi-service "broad governance" papers (e.g., local-
government-autonomy and decentralization-efficiency studies naming water as
one of several services) were excluded E01 for lacking a dedicated
water/sanitation-service-access analytical focus, consistent with prior E07
precedent for water-*resources* (as opposed to water-*service*) governance
studies.

`full_text_screening_database.csv` now stands at 357 of 3,659 decided (169
include / 188 exclude); `extraction_database.csv` and `evidence_map.csv`
both hold 169 fully-extracted studies (S001–S169), with schema validation
(`validate_schemas.py`) passing for all 13 tracked files and the retrieval
queue regenerated (3,302 open records).

## 2026-09-15 — Fourth full-text screening batch: 15 records decided, 4 new includes (S137–S140)

A fourth wave of 15 researcher-supplied full-text PDFs was screened against
`INCLUSION_EXCLUSION.md`. **4 included and fully extracted:**

- S137 Mndzebele & Onatu 2026 (Lerato Park, Kimberley, South Africa) —
  qualitative case study of a ~3,500-household informal settlement's
  statutory exclusion from municipal planning instruments (IDP, SDF,
  MTREF) driving reliance on illegal water connections and severely
  inadequate shared bucket-toilet sanitation.
- S138 Ribeiro & Galizoni 2003 (Jequitinhonha Valley, Brazil) — ethnographic
  study (22 communities, 188 families, 1999–2002) documenting the absence
  of small/customary water consumers from the formation of Brazil's formal
  water-scarcity legislation and river-basin management agencies; a
  companion, non-duplicate study to S125 (cross-referenced).
- S139 Moss 2008 (Eastern Germany) — documentary case study of how
  post-reunification demographic decline produced chronic water/wastewater
  infrastructure overcapacity, driving utility governance responses
  ("splintering urbanism") that intensify spatial disparities in service
  quality and pricing.
- S140 Jacob & Kotzebue 2026 (Bamboo Settlement #3, Trinidad and Tobago) —
  mixed-methods household survey (n=31) evaluating a government land-title
  regularization/upgrading program against the UN's five SDG 11.1
  informal-settlement dimensions, including water and sanitation access.

**11 excluded** (E01 ×2, E05 ×4, E06 ×3, E07 ×2), full reasoning logged
per-record in `exclusion_log.csv`. Notably, two papers on Brazilian river-basin-committee
formation (Abers & Jorge 2005; Jacobi & Monteiro 2006), despite using real
survey/documentary data, were excluded as E07 (wrong service): they examine
water-*resources*-management governance-institution formation, not
household or community water/sanitation *service* access.

Totals as of this update: **296 of 3,659 full-text records decided (140
include / 156 exclude)**; **140 studies fully extracted (S001–S140)**, all
92 `CODEBOOK.md` fields populated; evidence map current at 140 rows.

## 2026-09-15 — Third full-text screening batch: 29 records decided, 14 new includes (S123–S136)

A third wave of 29 researcher-supplied full-text PDFs was screened against
`INCLUSION_EXCLUSION.md`. **14 included and fully extracted:**

- S123 Del Grande, Galvão, Miranda & Guerra Sobrinho 2016 (Campina Grande,
  Brazil) — qualitative case study of income- and location-differentiated
  household capacity to absorb the burden of a 2014–2015 municipal water
  rationing crisis, against a backdrop of federal/state jurisdictional
  fragmentation over the Açude Boqueirão reservoir.
- S124 Paludo & Borba 2013 (Indaial vs. Itapema, Santa Catarina, Brazil) —
  comparative documentary case study of shared/co-managed vs. privatized
  water-utility models, including social-tariff exemptions and disconnection
  rates.
- S125 Galizoni & Ribeiro 2011 (Minas Gerais, Brazil) — 18-community
  ethnographic study (2002–2009) of customary water-commons norms and their
  collision with formal state conservation law/enforcement (IEF fines).
- S126 Murphy, Corston-Pine, Post & McBean 2015 (Ontario/British Columbia,
  Canada) — mixed-methods study of First Nations drinking-water operators
  documenting Band Council budget-approval discretion over operational
  purchases (including a denied chlorine-purchase request) and a structural
  80:20 federal/community funding-split burden.
- S127 McCullough & Farahbakhsh 2012 (Ontario, Canada) — qualitative
  grounded-theory study of the rigid federal Major Capital Works approval
  process governing First Nations drinking-water infrastructure funding.
- S128 Giatti & Cutolo 2012 (Amazônia Legal, Brazil) — mixed-methods
  macro-statistical and multi-case study documenting a political "estratégia
  da escassez" and 250,000 Manaus residents with zero access to the public
  water network.
- S129 Bichir 2009 (São Paulo, Brazil) — quantitative CHAID multivariate
  analysis of historical municipal investment patterns as a determinant of
  differential infrastructure access among the poorest 40% of the city's
  population.
- S130 Boelens et al. 2012 (Colombia/Ecuador/Peru) — comparative qualitative
  action-research study of formal water-rights allocation systems enabling
  large-scale hydropower/drinking-water/agribusiness encroachment on
  Indigenous collective water territories.
- S131 Ojeda et al. 2015 (Montes de María, Colombia) — 18-month ethnographic
  study documenting land/water title legalization used to formalize violent
  dispossession ("del rifle y el título").
- S132 Varela 2016 (Santa Cruz, Cabo Verde) — household survey (n=286) on
  water-tariff affordability far exceeding OECD/national benchmarks and a
  three-unpaid-bill disconnection policy.
- S133 Soriano et al. 2016 (São Paulo, Brazil) — documentary/hydrological
  case study of the 2014–2015 Cantareira System water crisis, including a
  utility regulatory-grant-condition breach and government denial of
  rationing contradicted by its own regulator.
- S134 Britto, Formiga-Johnsson & Carneiro 2016 (Rio de Janeiro, Brazil) —
  documentary/interview case study of "hydrosocial scarcity" showing how a
  centralized, monopolistic utility management model (not bulk-water
  scarcity alone) produces intermittent or absent supply in peripheral
  metropolitan districts.
- S135 Gasteyer, Lai, Tucker, Carrera & Moss 2016 (United States) —
  county-level ecological regression finding a statistically significant
  racial disparity in access to complete plumbing facilities, situated
  alongside the Flint/Detroit water crises.
- S136 Murtha, Castro & Heller 2015 (Brazil) — historical-archival analysis
  of colonial-era water/sanitation policy formation, documenting that
  nominally free public fountains still required enslaved labor for
  practical household water access.

**15 excluded** (E01 ×2, E03 ×2, E04 ×3, E05 ×5, E06 ×2, E07 ×1, E08 ×1;
the R7B0F55DA7FE0 Schnegg 2016 "Lost in Translation" paper was excluded as a
duplicate of the same underlying LINGS-project dataset/analysis already
extracted as S092, per `REPRODUCIBILITY.md` §6), full reasoning logged
per-record in `exclusion_log.csv`.

Totals as of this update: **281 of 3,659 full-text records decided (136
include / 145 exclude)**; **136 studies fully extracted (S001–S136)**, all
92 `CODEBOOK.md` fields populated; evidence map current at 136 rows.

## 2026-09-15 — Second large full-text screening batch: 19 records decided, 9 new includes (S114–S122); `final_decision` backfill fix

A second wave of 19 researcher-supplied full-text PDFs was screened against
`INCLUSION_EXCLUSION.md`. **9 included and fully extracted:**

- S114 Cardoso-Castro, Ravena & Mendes 2020 (Belém, Brazil) — document
  analysis and stakeholder interviews on fragmented, redundant governance
  responsibilities blocking rainwater-system implementation.
- S115 Velásquez 2020 (San Andrés Island, Colombia) — two-wave interview
  study (2016/2018) of Raizal ethnic-minority water-crisis response and
  discretionary state technocratic institutions.
- S116 Castleden et al. 2017 (Canada) — secondary systematic realist review
  (279 screened / 63 included) of Indigenous/Western knowledge integration
  in water governance; flagged `study_design_class = systematic_review_secondary`.
- S117 Pinheiro, Savoia & de Angelo 2016 (Brazil) — quantitative comparative
  economic-financial/operational indices of public vs. private water and
  sanitation providers, 2000–2010.
- S118 Rusca, Schwartz, Hadzovic & Ahlers 2015 (Lilongwe, Malawi) —
  institutional bricolage and elite capture of peri-urban Water Users
  Associations under a generic donor-promoted participatory model.
- S119 Kithatu-Kiwekete 2013 (Johannesburg and Nairobi) — comparative
  documentary analysis of local fiscal autonomy (revenue-sharing vs.
  revenue-assignment) in water/sanitation financing legislation; assessed
  with the project's Legal Institutional Evidence Appraisal Framework.
- S120 Jackson & Palmer 2012 (Australia and East Timor) — comparative case
  study of statutory water-allocation modernization marginalizing parallel
  customary governance systems.
- S121 Feler & Henderson 2008 (Brazil, NBER working paper) — quantitative
  quasi-experimental strategic-interaction model showing local governments
  deliberately under-service water/sewerage connections to discourage
  poor-migrant in-migration where formal zoning is ineffective; highest
  `mechanism_certainty` (3) and `risk_of_bias_tool = ROBINS-I` in this batch;
  `peer_reviewed = FALSE` (unpublished working paper), disclosed as a
  limitation.
- S122 Vargas & Lima 2004 (Brazil, PRINWASS case studies: Niterói/Região dos
  Lagos, Limeira) — qualitative multiple-case study of decentralization and
  privatization of Brazil's water/sanitation regulatory apparatus.

**10 excluded** (E01 ×1, E04 ×2, E05 ×5, E06 ×1, E07 ×1), full reasoning
logged per-record in `exclusion_log.csv` with page/section citations.

Also fixed a data-integrity gap discovered while regenerating the retrieval
queue: `final_decision` had only been populated for 68 of the (then) 233
already-decided full-text records — earlier batches set `full_text_decision`
but left `final_decision` blank, which `build_full_text_queue.py` relies on
to exclude decided records from the open queue. Backfilled `final_decision`
to mirror `full_text_decision` for all 184 affected rows (this project runs
a single AI reviewer with no `reviewer_2` process yet active, so the two
fields are equivalent in practice). Totals as of this update: **252 of 3,659
full-text records decided (122 include / 130 exclude)**; **122 studies fully
extracted (S001–S122)**, all 92 `CODEBOOK.md` fields populated; evidence map
current at 122 rows (6 studies now flagged `systematic_review_secondary`:
S015, S019, S027, S052, S079, S116).

## 2026-09-15 — Large full-text screening batch: 34 records decided, 19 new includes (S095–S113)

A large wave of researcher-supplied full-text PDFs (32 new records, plus one
previously-missed record from the Antigravity retrieval queue) was screened
against `INCLUSION_EXCLUSION.md`. **19 included and fully extracted:**

- S095 Wagner, Koehler & Hope 2025 (Mali) — contract-theory case study of
  professional rural water service delivery, contract incompleteness and
  renegotiation, tariff-burden and demand-enforcement mechanisms.
- S096 Tshona, Lungisa & Mgweba 2025 (South Africa, Amathole) — municipal
  governance obstacles to rural water provision.
- S097/S098 Mwale et al. 2025 (Zambia, George Compound, Lusaka) — two
  companion papers from the same fieldwork: stakeholder-perceived sanitation
  mitigation measures (household pit-latrine registration for scheduled
  desludging) and gendered exclusion in on-site sanitation.
- S099 Bolados García, Undurraga & Ibarra 2025 (Chile, Aconcagua) —
  constitutionally-grounded water-rights-holder eligibility mechanism
  historically excluding rural drinking-water associations, and the 2022
  Water Code reform's shift toward collaborative governance.
- S100 Abubakari 2025 (Ghana, Wa West) — community borehole-use rules
  (age-based eligibility restriction, enforcement via locking/hygiene
  prohibition) and women's substantive role in rule formulation.
- S101 Jeppesen 2025 (Kenya, Nairobi) — formal connection not equalling
  reliable access; water rights "concretized" through relationships with
  infrastructurally powerful actors rather than legal entitlement alone.
- S102 Alvaredo 2025 (Portugal, Barreiro) — historical-institutional case
  study (mid-20th century to early 1990s) of compulsory water-tariff
  payment creating new economic dependence.
- S103 Perry Lavado 2024 (Peru) — formal sanitation-sector complaints
  process as a regulatory-oversight mechanism, against national connection
  statistics (3.3M without water network, 6.4M without sewerage).
- S104 Thomas-Possee et al. 2024 (Zambia) — quantitative multilevel
  cross-sectional analysis (n=3,047 households linked to utility/regulator
  data) of piped-water intermittency; home ownership, provider, and
  utility-level GDP per capita as significant risk/protective factors
  (genuine calculable odds ratios).
- S105 Meetei 2024 (India, Manipur) — government universal tap-water
  scheme implementation gap and unenforced illegal-mining regulation.
- S106 Fernandes 2023 (India, Chennai/Bengaluru) — the Tamil Nadu
  Groundwater Act 2003's segregated regulation of city vs. hinterland
  groundwater, empirically linked to rural-to-urban middle-class water
  extraction and documented community resistance.
- S107 Hutete & Sibanda 2022 (South Africa) — procedural vs. distributive
  equity imbalance in rural municipal water governance.
- S108 Pillay & Mutereko 2022 (South Africa, eThekwini) — the municipal
  indigent policy's income-eligibility/registration mechanism and its
  implementation failure, disproportionately affecting informally-housed
  residents.
- S109 Rocha Neto 2022 (Brazil) — constitutionally fragmented federal
  sanitation competence and inspection-agency penalization (rather than
  accommodation) of smaller municipalities' technical/financial weakness.
- S110 Alba & Bruns 2022 (Ghana, Accra) — plot-owner-mediated informal
  ("bricolage") water access for unconnected kiosk-compound tenants within
  a formally well-served neighborhood.
- S111 Valenciano-Hernández 2021 (Costa Rica) — state-led inter-community
  water reallocation conflict; participatory governance activated only
  once conflict escalates.
- S112 Besana & Fernández Bouzo 2020 (Argentina, Buenos Aires) — 32-year
  case study of informal-settlement residents' intermediary-mediated,
  self-organized burden in securing potable-water network extension.
- S113 Kemp & Vyas-Doorgapersad 2020 (South Africa, Protea Glen) —
  multi-service municipal governance study with separately-documented
  water/sanitation access findings tied to institutional coordination gaps.

**15 excluded**, spanning E01 (wrong topic: GIS/MCDA vulnerability
indices, World Water Forum discourse analysis, Slovak housing policy,
Galápagos ecological conflicts, US-Mexico transboundary governance), E03
(water pollution/environmental injustice, wrong exposure), E04 (wrong
outcome: WSMT governance-participation quality, OECD investment-climate
scorecards, infrastructure project-financing performance, emotional
response to water scarcity, general corruption/service-delivery studies),
E05 (conceptual/policy-review papers without primary data collection),
and E06 (EU wastewater-directive technical compliance, utility
infrastructure-delivery engineering barriers).

Extraction database and evidence map now hold **113 fully extracted
studies (S001–S113)**. Full-text screening stands at **233 of 3,659
records decided (113 include / 120 exclude)**. Refreshed
`PRISMA_WORKFLOW.md`, `README.md`, `prisma_flow.md`, and
`preliminary_results.md` with these totals, and regenerated
`full_text_retrieval_queue.csv` (3,610 records still open). All 13
tracked schemas re-validated clean.

## 2026-09-15 — First externally-retrieved full-text batch (Antigravity/Gemini): 6 records screened, 2 new includes (S093–S094)

The researcher enlisted a separate agentic AI tool (Google Antigravity,
running Gemini) to help close the full-text retrieval backlog, using a
comprehensive handoff prompt drafted in this session (mirroring
`COWORK_RETRIEVAL_INSTRUCTIONS.md`'s conventions: open-access-first
retrieval, honest `not_retrievable` outcomes, no PDFs committed to the
repo, results handed back as a `record_id,full_text_status,
full_text_location,notes` CSV). Applied its first batch
(`full_text_retrieval_results_ProQuest_20260915.csv`, 30 ProQuest-sourced
records) via `bulk_import_full_text_results.py`: **8 retrieved via
legitimate open-access routes (Unpaywall/publisher-OA/repository copies),
22 not_retrievable** (no OA copy found, or a 403 on the OA link found).

Of the 8 retrieved, the researcher uploaded 6 PDFs to this session for
full-text screening (2 remain retrieved-but-unscreened pending upload —
Grisaffi/R3858447F3CCC and Dewi/R844EAC3AEE12):

- **Include (2):** S093 Gonçalves, Paiva Júnior & Cerqueira 2026
  (Cadernos de Gestão Pública e Cidadania) — qualitative IAD-framework
  case study of Brazil's São Francisco river transposition (PISF) water
  governance, documenting differential water access privileging
  wealthier/better-infrastructure localities and weak enforcement of
  access-limiting rules, with indigenous (Pipipã) and quilombola
  community fieldwork; S094 Mora González & Wing Ching Díaz 2026
  (Ciencia y Sociedad) — 32-year (1990–2022) sociohistorical case study
  of persistent drinking-water access/quality/sustainability deficiencies
  in the Bribri indigenous community of Amubri, Talamanca, Costa Rica,
  attributed to centralized state water governance (AyA) applied without
  adequate intercultural negotiation.
- **Exclude (4):** Mathumbu & Tafeni 2026 (KSD Municipality, South
  Africa) — E07, the paper's own stated limitation confirms it is
  primarily an electrification study with water/sanitation only
  incidental; Alrowais et al. 2026 (Scientific Reports) — E05, an
  illustrative indicator-scoring framework built on secondary data and
  expert judgment, explicitly not "confirmatory empirical measurement";
  Clerc et al. 2026 (Global Sustainability) — E05, a "Concepts and
  Perspectives" conceptual framework paper with no data collection;
  Tekeli 2026 (Actual Problems of Economics and Law) — E05, doctrinal
  statutory-interpretation analysis of Slovak water-tariff regulation.

Extraction database and evidence map now hold **94 fully extracted
studies (S001–S094)**. Full-text screening stands at **199 of 3,659
records decided (94 include / 105 exclude)**. Refreshed
`PRISMA_WORKFLOW.md`, `README.md`, `prisma_flow.md`, and
`preliminary_results.md` with these totals, and regenerated
`full_text_retrieval_queue.csv` (3,644 records still open). All 13
tracked schemas re-validated clean.

## 2026-09-13 — Full-text screening: Schnegg, Bollig & Linke (Namibia) included and extracted as S092

Screened Schnegg, Bollig & Linke (2016), "Moral equality and success of
common-pool water governance in Namibia" (Ambio 45:581-590). **Included**:
a mixed-methods study (60-community comparative survey + ethnographic
fieldwork + calibrated agent-based simulation) examining how Namibia's
decentralization of rural water-point management from the state to
community Water Point Associations shapes the cost/benefit-sharing rule
communities adopt (flat "numerical equality" fee vs. usage-based
"proportional equality"), and how that institutional choice produces
measurable affordability-burden and wealth-inequality consequences.
Classified BURDEN=TRUE (flat per-household fee disproportionately
burdens low-livestock households relative to actual water usage) and
DISCRETION_ACCOMMODATION=TRUE (state/NGO officials exercise discretion
in how actively they intervene to support poorer households against
wealthier residents' bargaining power — documented in a named
Ministry-official/community vignette). Extracted as **S092** with full
92-field data; `mechanism_certainty=2` (statistically significant
cross-community correlations plus named ethnographic vignettes, but an
observational/cross-sectional rather than quasi-experimental design).

Extraction database and evidence map now hold **92 fully extracted
studies (S001–S092)**. Full-text screening stands at **193 of 3,659
records decided (92 include / 101 exclude)**. Refreshed
`PRISMA_WORKFLOW.md`, `README.md`, `prisma_flow.md`, and
`preliminary_results.md` with these totals (also caught and fixed two
stale leftover counts in `prisma_flow.md` from an earlier round); all 13
tracked schemas re-validated clean.

## 2026-09-13 — Full-text screening: Acey "Hybrid Governance and the Human Right to Water" excluded (E05)

Screened Acey (2016), "Hybrid Governance and the Human Right to Water"
(Berkeley Planning Journal 28(1)). Excluded **E05 (no empirical
evidence)**: the paper is a narrative/doctrinal literature review and
policy essay on the international human-right-to-water framework
(normative content, progressive realization, third-party/non-state-actor
duty-bearer theory, a comparative table of countries' legal recognition
mechanisms compiled from the ESCR-Net/Global Health and Human Rights
Databases). The author explicitly frames the method as "a review of the
literature on human rights implementation and gathering data on how
countries have been implementing the right to water" — no defined
systematic search/synthesis methodology and no primary empirical
fieldwork of its own; every empirical claim in the piece is attributed to
other cited studies.

Full-text screening now stands at **192 of 3,659 records decided (91
include / 101 exclude)**. Updated `PRISMA_WORKFLOW.md`, `README.md`,
`prisma_flow.md`, and `preliminary_results.md` with these totals; all 13
tracked schemas re-validated clean.

## 2026-09-13 — Full-text screening batch: 10 more records decided, 5 new includes extracted (S087–S091)

Continued Phase 6 full-text screening on a rolling batch of researcher-
supplied PDFs, processed via the standard pipeline (convert →
`pdftotext -layout` → screen against `INCLUSION_EXCLUSION.md`'s E01–E12
codes → record via `code/screening/update_full_text_record.py` → log any
exclusion to `exclusion_log.csv` → extract into
`extraction_database.csv` and `evidence_map.csv` for every include →
`validate_schemas.py`).

**10 records decided this batch:**
- **Include (5):** S087 Grönwall (Ghana, mixed-methods, tenure/PURC/WRC/
  CWSA regulatory fragmentation); S088 Otsuki 2016 (Kibera, Kenya —
  Tosha Network CBO certification, chief's-permission bottleneck to
  connect a bio-centre to the city water grid); S089 Tutu & Stoler 2016
  (Accra, Ghana — tenure-based denial of formal water supply in two
  informal settlements); S090 Awunyo-Akaba et al. 2016 (Ghana — tenure/
  land-rights status shaping sanitation investment across three
  comparative communities); S091 Rodina & Harris 2016 (Khayelitsha, Cape
  Town — RDP housing-formalisation process gating individual in-house
  water/sanitation connection vs. communal-tap access, plus differential
  councillor responsiveness to formalized vs. informal residents'
  grievances).
- **Exclude (5):** Wilhelm-Solomon 2016 (E01 — eviction/urban
  regeneration, not service access); Ojha 2021 (Nepal water policy —
  included as S086, logged separately); Liddle et al. 2016 (Ndola,
  Zambia informal water supply — E06, core contribution is technical/
  engineering: well protection, smart hand pumps, not a legal-
  administrative access mechanism); Kanyamurwa 2016 (Uganda — E04,
  quantitative survey of political interference/accountability in
  utility governance, not household-level access/exclusion tied to a
  legal-administrative mechanism).

`extraction_database.csv` and `evidence_map.csv` now hold **91 fully
extracted studies (S001–S091)**. Full-text screening stands at **191 of
3,659 records decided (91 include / 100 exclude)**. All 13 tracked
schemas re-validated clean after every write. Updated `PRISMA_WORKFLOW.md`,
`README.md`, `06_outputs/prisma/prisma_flow.md`, and
`06_outputs/supplementary/preliminary_results.md` with these totals —
the already-published `preliminary_report_2026-09-13.md`/`.docx` is left
as a dated historical snapshot and not retroactively edited.

## 2026-09-13 — Exploratory Results/Discussion/Conclusion added to the preliminary report, explicitly labeled as a sketch

At the researcher's explicit, repeated request (after an initial version
of this report deliberately omitted these sections per
`manuscript_outline.md`'s own rule), added §6–8 to
`07_manuscript/draft/preliminary_report_2026-09-13.md`: "Preliminary
Results (Exploratory, Non-Representative)," "Preliminary Discussion
(Exploratory)," and "Preliminary Conclusion (Exploratory, Highly
Provisional)." Given a choice between a bare placeholder skeleton, a
labeled exploratory sketch, and a full unhedged synthesis, the researcher
chose the labeled exploratory sketch.

Content is grounded entirely in real extracted data — no fabrication.
Read through all 37 studies flagged `quantitative_synthesis_eligible` and
found that most report descriptive access statistics without a
comparison that isolates a legal/administrative exposure; six
(Lubeck-Schricker et al. 2023 [S084], Gaikwad & Thomas 2026 [S085],
Filčák & Škobla 2021 [S078], Kozole et al. 2023 [S057], dos Santos Alves
Romanato et al. 2025 [S021], Rajput & Pu 2025 [S029]) do isolate such a
comparison and are reported by name with their actual effect estimates.
All six point in the direction the Legal Last Mile framework predicts;
this is stated as weak, non-representative, hand-selected support, not a
finding — the document says so at the top (revised status callout),
before §6, in §7, in §8, and again in a new §10 ("Why §6–8 Are Sketches,
Not the Review's Findings," renumbered from the original §7 "Why This
Report Stops Here") and §11's expanded Limitations. Existing §6–8
(PRISMA-phase status, stopping rationale, limitations) renumbered to
§9–11 without other content changes. Re-generated the matching `.docx`.

## 2026-09-13 (earlier) — Preliminary protocol + interim descriptive report drafted

At the researcher's request for "a preliminary paper," wrote
`07_manuscript/draft/preliminary_report_2026-09-13.md`: a
methods-and-status document, not a findings paper. It contains the
pre-specified conceptual framework and methods (unchanged since
2026-08-22), the actual current PRISMA flow (27,481 unique records →
3,659 past title/abstract screening → 175/3,659 full-text screened,
85 include/90 exclude → 85/85 extracted), and purely descriptive
characteristics of the 85 extracted studies (region, legal system, study
design, mechanism family, outcome family, publication years) plus a full
alphabetical reference list of those 85 studies as Appendix A.

**Deliberately excludes Results, Discussion, Comparative Findings, and
Conclusion sections** — consistent with `manuscript_outline.md`'s own
rule that those sections may not be drafted from illustration or the
preliminary source papers alone, and with `PROJECT_SPEC.md` §1's
governing principle (determine what the evidence allows before deciding
on synthesis, not the reverse). With full-text screening at ≈4.8%
complete and risk-of-bias appraisal and the quantitative-feasibility
decision tree (Phases 9 and 11) both unrun, writing those sections now
would produce either an empty section or an illustration presented as a
finding — exactly what the anti-confirmation-bias rule exists to
prevent. The document says this explicitly in its own §7 rather than
silently omitting the sections.

## 2026-09-12 (latest, cont. 14) — CITATION.cff added for a standalone Zenodo deposit; abstract-redistribution question raised and resolved by researcher decision

Preparing a standalone Zenodo deposit of this `legal-last-mile-systematic-review/`
subdirectory (separate from the repository's existing dataset-scoped DOI,
`10.5281/zenodo.19836413`, whose own title/citation history is being left
untouched). Added `CITATION.cff` scoped to the review itself, since
Zenodo's automatic GitHub-release integration reads the repo root's
existing `CITATION.cff` (dataset-scoped) and a manual, subdirectory-only
deposit needs its own.

Also raised, and the researcher explicitly resolved, a real question: the
review's screening-stage CSVs (`deduplicated_records.csv`,
`screening_database.csv`, `reviewer_2_queue.csv`,
`exclude_spotcheck_sample.csv`) carry ~38MB / 26,222 verbatim abstracts
bulk-exported from Scopus/Web of Science, the same category of
copyright/redistribution concern already caught once for full-text PDFs
(2026-08-26 entry above). Flagged before creating any public deposit,
including the note that this is separately a Scopus/WoS license
(contract) question independent of copyright fair-use analysis, and that
EU text-and-data-mining exceptions (relevant given the researcher's
Erasmus University Rotterdam affiliation) are narrower than US fair use
and generally cover the mining/analysis itself, not public republication
of the underlying text. **Researcher decision: include the abstracts as-is,
accepting the redistribution risk.** Logged here per this project's
standing "flagged, not hidden" practice — this is a disclosed,
researcher-owned risk decision, not an oversight.

## 2026-09-12 (latest, cont. 13) — OSF preregistration draft brought to submission-ready state, with an explicit retrospective-registration disclosure

At the researcher's request, prepared the OSF Generalized Systematic
Review draft (`00_admin/preregistration/osf_preregistration_draft.md`)
for actual submission. This environment has no OSF account, so the
submission click itself remains the researcher's to do. Two substantive
changes, not just formatting:

1. Added an explicit "Disclosure: this is a retrospective registration,
   not a fully a priori one" section. The protocol's *content* (research
   question, `INCLUSION_EXCLUSION.md`, `CODEBOOK.md`, `RISK_OF_BIAS.md`
   tool assignments, `ANALYSIS_PLAN.md`) was fixed 2026-08-22, before any
   database was searched, and has not been revised since in response to
   what the search/screening turned up. But the *registration itself* is
   only being submitted now (2026-09-12), roughly three weeks after
   search execution began and after search closed, title/abstract
   screening completed, and full-text screening/extraction were already
   underway. Both dates need to be stated on OSF itself, not left
   implicit — a registration that reads as fully a priori when it isn't
   would undercut the entire point of registering.
2. Filled in "Existing data / prior work" and "Anticipated timeline" with
   the actual realized dates from this changelog (search closed
   2026-09-11; title/abstract screening complete 2026-09-12; full-text
   screening/extraction live) rather than leaving them at their
   2026-08-22 draft state or blank.

Confirmed PROSPERO remains the wrong registry (health/welfare-outcome
scope; also does not accept registration once extraction has begun,
which this review's already has) — OSF stays the plan. Submission
checklist updated accordingly, including a step to cross-link the
eventual OSF DOI with any Zenodo archival DOI via each platform's
related-identifiers field.

## 2026-09-12 (latest, cont. 12) — Corpus-wide scan for the R88194172BEF6 corruption pattern: no further instances found

The earlier QA spot-check (cont. 9) found one exclude record
(`R88194172BEF6`) whose stored `ai_rationale` was completely mismatched to
its actual title/abstract — an oncology rationale attached to a Sicilian
wastewater-reuse paper, attributed to the 39-parallel-batch merge process.
A 120-record random sample only samples ~0.5% of the 22,557-record exclude
pool, so rather than drawing another random batch, scanned the **entire**
pool's `ai_rationale` text (`ai_first_pass_rationale.csv`) for the same
failure signature: a rationale citing a domain wholly foreign to
water/sanitation/legal-administrative research (oncology, cardiovascular,
psychiatric, blockchain, cryptocurrency, semiconductor, stock-market
trading, etc.) — the kind of mismatch a corrupted merge would produce.
74 records matched at least one such term. Manually verified a diverse
sample of 18 against their actual `screening_database.csv` title/abstract
(spanning every matched term at least once, including the ones read in
full above): all 18 rationales accurately described their real paper —
these are genuine off-topic records correctly swept up and excluded by
the broad keyword search (e.g., 8 near-duplicate stock-market newsletter
records for ticker "SJW" — South Jersey Industries, a water utility
holding company — correctly excluded as wrong-topic noise; a 1990 case
study of a semiconductor company's drinking-water contamination correctly
excluded as historical/policy commentary rather than a water-access
study). **No further instance of the R88194172BEF6 corruption pattern was
found.** This is a stronger result than another random sample would give
for this specific failure mode, since it covers the whole pool rather than
estimating a rate from ~0.5% of it; it does not rule out other, differently
-shaped errors the same merge process might have introduced, which the
120-record random sample (cont. 9) remains the relevant check for.

## 2026-09-12 (latest, cont. 11) — Closed the last extraction gap: S084/S085

While the researcher was mid-download on a fresh PDF batch, audited the
extraction pipeline for other work available without new uploads. Found
that both PDFs behind the two long-flagged "no cached full text" records
(Lubeck-Schricker et al. 2023; Gaikwad & Thomas 2026) were already present
in the session's upload store — uploaded 2026-09-12 alongside that day's
main batch — but had never been converted to text or extracted, apparently
missed in the earlier batch pass rather than genuinely absent. Converted
both (`pdftotext -layout`), read them in full, and extracted them as S084
and S085 following the same `CODEBOOK.md`/`EXTRACTION_FORM.md` process used
for the other 83 studies, then populated `evidence_map.csv` for both
(mechanical fields via `code/analysis/build_evidence_map.py`, judgment-call
fields — `outcome_family`, `evidence_level`,
`quantitative_synthesis_eligible`/`qualitative_synthesis_eligible` — by
hand). `extraction_database.csv` now holds all 85 current full-text
includes with zero gap. S085 (Gaikwad & Thomas) is a genuine
cluster-randomized field experiment (`mechanism_certainty=4`), the
strongest-design study extracted so far, and a clean empirical instance of
`PROJECT_SPEC.md` §8's candidate Family B (bureaucratic assistance →
connection/application success) — though its own finding is that the
mechanism only operates jointly with political coordination, a genuine
complication for treating Family B as a simple main effect. Also
separately fixed a hardcoded, author-machine-specific Windows path
fallback in the (out-of-scope but same-repo) judicial-decisions-dataset
project's `research-assistant/data_loader.py`, and a stale κ figure plus a
broken copy-pasteable command in that project's `validation/README.md` and
`validation/kappa_calculator.py` — flagged separately to the researcher
since they fall outside this systematic review's own scope. Ran
`code/analysis/validate_schemas.py` after every write; all 13 tracked
files matched schema throughout. Updated `PRISMA_WORKFLOW.md` Phases 8 and
10 to reflect 85/85 extraction with no outstanding gap (up from 83/85 with
2 studies flagged as awaiting re-upload that were never actually needed).

## 2026-09-12 (latest, cont. 10) — Full-text reviewer_2 handoff tooling; final_decision normalization

Built `code/screening/build_full_text_reviewer2_queue.py`, mirroring the
title/abstract stage's queue mechanism, so a human `reviewer_2` for Phase
6 (full-text screening) can start immediately whenever the researcher
assigns one rather than needing tooling built first. Generated the queue
for real: `02_screening/full_text/full_text_reviewer_2_queue.csv`, 175
rows (85 include / 90 exclude), plus
`02_screening/full_text/REVIEWER_2_README.md` documenting how to use it
and — unlike the title/abstract stage — the added wrinkle that Phase 8
extraction has already run on every include, so a reviewer_2 override on
an include also means removing/flagging the corresponding
`extraction_database.csv`/`evidence_map.csv` row.

While building this, found that 18 full-text records had `final_decision`
already populated (mirroring `reviewer_1`'s decision) despite no human
reviewer_2 pass ever having happened for this phase — an inconsistency
from recent batches, not intentional. Blanked `final_decision` back out
on all 18, consistent with this project's own stated rule (`final_decision`
is set only after conflict resolution between two independent reviewers).
This did not affect any Phase 8 extraction or Phase 10 evidence-map
work, both of which key off `full_text_decision`, not `final_decision`.

## 2026-09-12 (latest, cont. 9) — QA spot-check of the 120-record exclude sample; pipeline consistency audit

Manually reviewed all 120 records in `exclude_spotcheck_sample.csv`
(fixed-seed random sample of title/abstract-stage excludes, previously
unreviewed) against `INCLUSION_EXCLUSION.md`. 119 of 120 exclusion
decisions and their stated rationale checked out. One discrepancy found:
`R88194172BEF6` (a Sicilian wastewater-reservoir bacterial-removal
modeling study for agricultural irrigation reuse) carried a stored
`ai_rationale` ("Oncology biomarker study; unrelated to water/sanitation")
that plainly did not match its title/abstract — a mismatch that survived
into both `screening_database.csv` and the QA sample, most likely from
the 39-parallel-batch merge process. The `exclude` decision itself was
still correct; only the `exclusion_reason` code was off (`E01` instead of
`E07`, since the actual content is agricultural/irrigation water reuse,
not an unrelated topic). Corrected the code and rationale in both files
and the affected title/abstract exclusion-code breakdown in
`prisma_flow.md` (E01 16,667→16,666; E07 1,039→1,040) — see
`PRISMA_WORKFLOW.md` Phase 5 for the full note.

Also ran a pipeline consistency audit: no duplicate DOIs among the 85
full-text includes, no invalid/missing `exclusion_reason` codes among the
90 full-text excludes, and every include reconciles to an extraction row
except the two records already known to be awaiting full-text re-upload
(Lubeck-Schricker et al.; Gaikwad & Thomas) — no hidden extraction gaps.

## 2026-09-12 (latest, cont. 8) — Added companion bibliometric manuscript as SOURCES.md exemplar

Added Klaus (2026), "The Evolution of Basic Sanitation Research in
Brazil: A Bibliometric Analysis (1987 to 2026)" — this review's own
author's unpublished scientometric manuscript — as `SOURCES.md` entry 14
and a corresponding `sources.bib` entry, at the researcher's request.
This manuscript was supplied via chat upload but is not part of the
search-derived corpus (no `record_id` in
`02_screening/full_text/full_text_screening_database.csv`), so it was
deliberately not forced through Phase 6 full-text screening; it is cited
as background/methodological context on the state of Brazilian
sanitation-law scholarship, not as a candidate primary study for this
review's evidence base.

## 2026-09-12 (latest, cont. 7) — Live full-text screening, full extraction, and evidence classification underway

Phase 6 (full-text screening) went from scaffolding to live, ongoing work
once the researcher began supplying full-text PDFs via chat upload —
expected to continue over roughly a month. Each PDF is converted with
`pdftotext -layout`, screened by Claude as `reviewer_1`
(`Claude-AI-fulltext-2026-09-12`) against `INCLUSION_EXCLUSION.md`, and
recorded via `update_full_text_record.py`; every exclusion is also logged
to `exclusion_log.csv`. As of this entry: **126 of 3,659 records decided
(62 include / 64 exclude)** — see `PRISMA_WORKFLOW.md` Phase 6 for the
exclusion-reason breakdown. `reviewer_2` for this phase has not yet been
assigned; open question for the researcher.

At the researcher's explicit instruction ("go ahead and start an
extraction for the 44 included papers... I'm accompanying you every step
of the way"), Phase 8 (full extraction) began directly rather than first
drawing a separate ~10-study Phase 7 pilot sample — Phase 7 is marked
superseded in `PRISMA_WORKFLOW.md` rather than completed. **42 studies
(S001-S042) are now fully extracted** into `extraction_database.csv`
against `CODEBOOK.md`'s complete 92-field schema, in six batches of
seven. Two studies with no cached full text available in this session
(Lubeck-Schricker et al.; Gaikwad) were explicitly *not* extracted from
memory and are flagged for re-upload — extraction accuracy takes priority
over completeness. Three of the 42 (Basnet & Sherchan; Ilangovan et al.;
Fanaian et al.) are themselves secondary systematic reviews, flagged
`study_design_class = systematic_review_secondary` and never to be pooled
as an independent primary effect, per `RISK_OF_BIAS.md` §1.

**Every one of the 42 extracted rows has `risk_of_bias_rating` left
deliberately blank.** `RISK_OF_BIAS.md` is explicit that none of the six
validated appraisal tools (RoB 2, ROBINS-I, the two JBI checklists, CASP,
MMAT) or AMSTAR 2 may be reconstructed from memory — the current official
version must be obtained before appraising a study with it. Each row
correctly identifies `risk_of_bias_tool` (design-matched, or the
project's own Legal Institutional Evidence Appraisal Framework where no
conventional tool fits) and carries an `extraction_note` deferring the
actual rating to a follow-up pass with the official instrument in hand.
This is a disclosed limitation of the review's current state, to be
reported as such in any manuscript output, not an oversight to be quietly
fixed later.

`code/analysis/build_evidence_map.py` was run against the real
extraction database for the first time, then the judgment-call fields it
deliberately leaves blank were filled by hand for all 42 studies:
`study_design_class` for the six studies using the Legal Institutional
Evidence Appraisal Framework (resolved doctrinal vs. jurimetric per
study — the tool name alone can't distinguish them), `outcome_family`
mapped to `PROJECT_SPEC.md` §7's hierarchy based on each study's actual
central/tested outcome rather than a mechanical restatement of the
outcome booleans, `evidence_level` written as prose per
`DATA_DICTIONARY.md`'s instruction that it is a narrative tier rather
than a score, and `quantitative_synthesis_eligible`/
`qualitative_synthesis_eligible` set per study (18 of 42 have a genuine,
study-generated, calculable effect estimate; all 42 are eligible for
qualitative/thematic synthesis, consistent with this project's standing
protection of qualitative socio-legal evidence as first-class rather than
a fallback). See `05_analysis/descriptive/EVIDENCE_MAP_README.md`.

`PRISMA_WORKFLOW.md` and `06_outputs/prisma/prisma_flow.md` updated
throughout to replace stale "not started"/"blocked" language for Phases
6-10 with the real, live counts above.

## 2026-09-12 (latest, cont. 6) — Cowork full-text retrieval instructions and bulk-import tooling

At the researcher's request, built the missing piece to actually
unblock Phase 6 rather than more scaffolding downstream of it:

- **`code/screening/bulk_import_full_text_results.py`** (new): applies a
  whole batch of retrieval (or screening) results to
  `full_text_screening_database.csv` in one atomic write. Reuses
  `init_full_text_db.py`'s own `SCHEMA`/`VALID_STATUS`/`VALID_DECISION`
  constants (loaded dynamically, same pattern as `validate_schemas.py`)
  rather than redeclaring them. **Rejects the entire batch if any row is
  invalid** -- a typo in row 400 of 500 can never leave 399 good rows
  applied and one silently wrong; nothing is written until every row
  passes. Never overwrites a record that already has a `final_decision`,
  and never auto-adds an unrecognized `record_id`. Tested against a
  synthetic copy of the real database before ever touching it for real:
  a valid two-row batch applied correctly (plus an unknown record_id
  correctly skipped and reported), an invalid-enum batch correctly
  rejected the whole import with zero writes, and an already-decided
  record was correctly left untouched by a later batch that tried to
  touch it.
- **`02_screening/full_text/COWORK_RETRIEVAL_INSTRUCTIONS.md`** (new): a
  ready-to-paste instruction set for a browser-capable Claude Cowork
  session, mirroring how this project's original database searches were
  actually done (Cowork does the browser work, reports results back as a
  file, the main session applies them). Scopes the task explicitly to
  *retrieval only* (never full-text screening/inclusion decisions,
  which stay a separate, later, judgment-heavy step); works in
  small per-database batches rather than all 3,659 at once; explicitly
  tells Cowork **not** to commit retrieved PDFs into this git
  repository (publisher copyright, repo bloat) and to record only a
  location/link instead; specifies the exact 4-column results-file
  format `bulk_import_full_text_results.py` expects; and carries the
  same "never guess or fabricate a retrieval outcome" discipline used
  throughout this project's screening tools.
- `FULL_TEXT_README.md` updated to reference both.

This is the one piece of work this session that actually has a path to
unblocking Phases 6 onward, rather than more scaffolding ahead of data
that still can't run until real full texts exist.

## 2026-09-12 (latest, cont. 5) — Phases 12-16 scaffolding built (meta-analysis through PRISMA reporting)

At the researcher's request ("keep scaffolding further downstream
phases... regardless"), built shells for every remaining phase, with an
explicit disclosure this time that matters more than in prior rounds:
**none of the R code below has actually been executed** — no R
interpreter was available in the environment that wrote it (checked:
`which R` / `which Rscript` both came back empty). This is a materially
different situation from every stdlib-Python script built earlier this
project, which were tested directly. Brace/parenthesis balance was
sanity-checked mechanically as a minimal safety net, but that is not the
same as a real run.

- **`08_code/R/01_meta_analysis.R`** (Phase 12): random-effects model per
  candidate synthesis family (`ANALYSIS_PLAN.md` §5), heterogeneity +
  prediction interval (§6), subgroup analysis gated on a minimum study
  count (§7), meta-regression gated at the ~10-studies-per-moderator
  threshold (§8). Flags rather than silently pools when a study
  contributes more than one effect to a family (`CODEBOOK.md` §12's
  dependence-modeling requirement). Joins `extraction_database.csv` in
  for moderator/subgroup fields, since `effect_sizes.csv` itself has none
  — and explicitly does NOT invent a clean mapping between
  `ANALYSIS_PLAN.md`'s colloquial moderator names ("jurisdiction",
  "decentralization") and `extraction_database.csv`'s actual column names
  (`country`, `regulatory_model`), since no such 1:1 mapping currently
  exists in this project's own schema.
- **`08_code/R/02_sensitivity_analysis.R`** (Phase 14): the five specific
  checks `ANALYSIS_PLAN.md` §10 names, each reported as run or explicitly
  skipped (never silently omitted) depending on what fields are actually
  available for a given family.
- **`08_code/R/03_publication_bias.R`** (Phase 15): funnel plot, Egger,
  Begg — **refuses to run below `ANALYSIS_PLAN.md` §9's ~10-studies-per-
  family threshold** rather than producing an uninterpretable plot, same
  discipline as `code/extraction/select_pilot_sample.py`'s refusal logic.
  Prints the "asymmetry is not proof of publication bias" caveat
  alongside every result it does produce.
- **`06_outputs/supplementary/SWIM_SYNTHESIS_TEMPLATE.md`** (Phase 13):
  structural template for families the decision tree routes away from
  meta-analysis — explicitly does not reproduce SWiM's own reporting
  checklist verbatim, same unverified-citation caveat as the
  risk-of-bias tools.
- **`06_outputs/prisma/PRISMA_2020_CHECKLIST.md`** (Phase 16): all 27
  items mapped to where each is already substantively addressed in this
  repository (most of them, well before any manuscript gets drafted) —
  two items (funding, competing interests) flagged as having no home yet
  since they're disclosures the researcher supplies, not pipeline
  outputs. Item wording reconstructed from well-established knowledge of
  PRISMA 2020's structure, not a live fetch against the publisher — flag
  to verify against the official checklist before submission.
- Fixed a stale `ANALYSIS_PLAN.md` §13 status line still blaming the
  (long-closed) search phase; the real current blocker is Phase 6 not
  having produced full-text decisions yet.
- `PRISMA_WORKFLOW.md` Phase 12-16 rows and current-phase summary updated
  accordingly, each carrying the "not yet run" caveat explicitly rather
  than only in `08_code/R/README.md`.

No new CSV schemas, so `validate_schemas.py` needed no updates. No
analysis has actually been run on real data — templates only, and
honestly labeled as untested where that's genuinely true (unlike this
project's Python tooling, which has been run and verified throughout).

## 2026-09-12 (latest, cont. 4) — Phase 10 (evidence classification) tooling built; Phase 11 deliberately left unscaffolded

At the researcher's request ("go on"), built `code/analysis/
build_evidence_map.py`: an idempotent, append-only script (same design
as `init_screening_db.py`/`init_full_text_db.py`) that fills
`evidence_map.csv` with whatever can be safely derived from
`extraction_database.csv` and leaves the rest blank with an explicit
warning rather than guessing:

- **Derived mechanically** (safe, because each is either already a
  closed-form fact recorded during extraction, or a direct application
  of a mapping this project's own docs already commit to):
  `study_design_class` (inverts `RISK_OF_BIAS.md` §1's design↔tool
  table), `mechanism_family` (from the four top-level mechanism
  booleans, `MULTIPLE` when more than one is true), `legal_context`/
  `institutional_context` (copied straight from already-extracted
  fields).
- **Left blank on purpose, with a printed warning**: `study_design_class`
  when the tool was the project's own Legal Institutional Evidence
  Appraisal Framework (covers both doctrinal and jurimetric studies,
  RISK_OF_BIAS.md §2 — the tool name alone can't disambiguate);
  `mechanism_family` when no top-level boolean came through true (a
  data-quality flag); `evidence_level` (a narrative tier per
  `DATA_DICTIONARY.md`, never a formula); and **`outcome_family`, every
  time** — `PROJECT_SPEC.md` §7's own outcome hierarchy lists
  "approval/refusal" under both the primary outcome and a secondary
  "administrative outcomes" category, so a study coded with
  `application_success`/`refusal`/`delay_outcome` genuinely cannot be
  mechanically resolved to one family without reading which specific
  approval/refusal the study actually measured. Guessing here would risk
  the "manufactured comparability" `PROJECT_SPEC.md` §3 exists to
  prevent, since outcome family gates what can ever be pooled together.

Tested against a synthetic four-study extraction database before
touching real data: correct tool→design-class mapping across RoB 2/
ROBINS-I/JBI/the project's own framework, correct single-vs-`MULTIPLE`
mechanism handling, correct warnings on the deliberately-blank fields,
and a verified no-op/no-duplicate on a second run (idempotency check).
Then run against the real `extraction_database.csv` — currently empty,
so a correct zero-row no-op.

`05_analysis/descriptive/EVIDENCE_MAP_README.md` (new) documents both
what the script does and, in its closing section, **why Phase 11
(quantitative feasibility assessment) gets no equivalent tooling**:
`ANALYSIS_PLAN.md` §2's decision tree is a corpus-level methodological
judgment applied per candidate synthesis family, not a per-study
mechanical fact — the decision tree itself already *is* the complete
process, so there's nothing safe left to automate ahead of real evidence
the way Phase 10's script helps with mechanical fields. `PRISMA_WORKFLOW.md`
Phase 10/11 rows and current-phase summary updated accordingly.

No new CSV schemas (evidence_map.csv's header is unchanged), so
`validate_schemas.py` needed no updates. No study has actually been
classified — tooling only, and honest about where tooling stops being
appropriate.

## 2026-09-12 (latest, cont. 3) — Phase 9 (risk of bias) process scaffolding built

At the researcher's request ("keep going"), scaffolded Phase 9 ahead of
any study actually reaching the appraisal stage:

- **`04_quality/appraisal_forms/APPRAISAL_FORM.md`** (new): the process
  guide — classify design, obtain the current official tool, complete it,
  save the filled checklist alongside a provenance-style filename
  (`<study_id>_<tool>.<ext>`), record the result into
  `extraction_database.csv`'s quality fields. **Deliberately does not
  reproduce any of the six validated tools' (RoB 2, ROBINS-I, two JBI
  checklists, CASP, MMAT) own checklist items or signaling questions
  anywhere in this repository** — those are living instruments their
  publishers revise, and this project has not independently re-verified
  their citations against the publisher (network access to publisher
  domains stays blocked from this environment).
- **`SOURCES.md`** §9–13: added citations for all six standard tools
  named in `RISK_OF_BIAS.md` §1 that had never been logged there, using
  the exact same honest hedge already established for PRISMA-P and
  AMSTAR 2 in that file — "not independently re-confirmed this session,
  standard and internally consistent with its well-known form, confirm
  before manuscript use." No citation is presented as more verified than
  it actually is.
- **`legal_institutional_evidence_appraisal_framework_form.md`** (new):
  a fully worked fillable form for the one instrument this project
  actually authored (`RISK_OF_BIAS.md` §2's 13 domains) — safe to
  reproduce in full since it's this project's own content, unlike the six
  validated tools above.
- **`04_quality/risk_of_bias/EVIDENCE_LIMITATIONS_TEMPLATE.md`** (new):
  shell for the end-of-phase cross-cutting narrative `RISK_OF_BIAS.md`
  §3 already calls for but never had a template for.
- Fixed a stale line in **`RISK_OF_BIAS.md`** §4 that still said "the
  search has not been executed" as the reason no study has been
  appraised — the search closed 2026-09-11; the real current blocker is
  that extraction (Phase 8) hasn't started yet, since Phase 6 (full-text
  screening) hasn't produced real decisions.
- `PRISMA_WORKFLOW.md` Phase 9 row and current-phase summary updated to
  match.

No new CSV files were created and no schema changed, so
`validate_schemas.py` needed no updates for this round. No study has
actually been appraised — process scaffolding only.

## 2026-09-12 (latest, cont. 2) — Phase 7 (pilot extraction) scaffolding built

At the researcher's request ("go on to the next"), scaffolded Phase 7
ahead of Phase 6 actually producing any full-text decisions — the same
build-ahead pattern used for Phase 6 itself:

- **`03_extraction/extraction_form/EXTRACTION_FORM.md`** (new):
  operationalizes `CODEBOOK.md`'s 12 sections into an ordered, fillable
  checklist for extracting one study into `extraction_database.csv` --
  explicitly flags the unit-of-analysis decision (`PROJECT_SPEC.md` §4)
  as something to nail down before extracting a single number, and the
  one-effect-per-study-and-outcome-family default (`CODEBOOK.md` §12)
  before extracting statistics from a multi-effect study.
- **`code/extraction/select_pilot_sample.py`** (new): draws the ~10-study
  pilot sample `PROTOCOL.md` §6 requires, stratified proportionally by
  source database (largest-remainder apportionment) with a fixed seed for
  reproducibility -- same practice as `exclude_spotcheck_sample.csv`.
  **Correctly refuses to run right now**: 0 of `full_text_screening_
  database.csv`'s 3,659 seeded records currently carry `final_decision ==
  "include"` (Phase 6 retrieval/screening hasn't started), so drawing a
  10-study sample from an empty pool would be meaningless. Verified the
  refusal path, and separately verified the actual stratification logic
  against a synthetic 30-record pool (15/10/5 split across three fake
  databases correctly yielded a 5/3/2 pilot draw) -- synthetic test files
  deleted after verification, nothing real touched.
- **`03_extraction/extraction_form/PILOT_EXTRACTION.md`** (new):
  documents why the pilot can't run yet, how to run it once it can, and
  -- the actual point of piloting -- that a disagreement between two
  independent pilot extractions should prompt asking whether `CODEBOOK.md`
  itself needs revision, not just resolving that one study's numbers; any
  such revision is a protocol amendment to log in this changelog per
  `PROTOCOL.md` §12.
- `PRISMA_WORKFLOW.md` Phase 7 row and current-phase summary, `CODEBOOK.md`'s
  opening paragraph, and `DATA_DICTIONARY.md` (a new entry for
  `pilot_sample.csv`, explicitly marked not-yet-generated) all updated to
  point at this tooling.

`pilot_sample.csv`'s schema is intentionally **not yet** added to
`validate_schemas.py` -- the file cannot legitimately exist until the
script actually runs for real, and adding a schema entry for a file that
doesn't exist yet would turn `validate_schemas.py`'s otherwise-clean
report into a false "MISSING" failure. Add it once Phase 6 has enough
real includes and the pilot is actually drawn.

No study has been extracted and no pilot has been drawn -- this is
scaffolding only, ready to use the moment Phase 6 produces enough
full-text includes.

## 2026-09-12 (latest, cont.) — Phase 6 retrieval tooling added

Following the scaffolding entry directly below, added three small
`code/screening/` scripts to support the actual retrieval/screening loop
the researcher (or a future full-text reviewer) will run repeatedly —
none of them retrieve anything themselves (still no outbound network
access from this environment), but they take the error-prone parts of
*recording* progress off the researcher:

- **`build_full_text_queue.py`**: regenerates a disposable
  `full_text_retrieval_queue.csv` from `full_text_screening_database.csv`
  joined against `screening_database.csv` for the `database` field —
  every still-open record (no `final_decision` yet), sorted by database
  then year descending, so retrieval can be batched one platform at a
  time instead of context-switching every row. Never writes to the
  authoritative file.
- **`update_full_text_record.py`**: the safe way to record one record's
  status or decision, instead of hand-editing the CSV (real risk: broken
  quoting on titles/authors with commas, or a typo'd enum value nothing
  else would catch). Validates every field against the same enums as
  `init_full_text_db.py`, touches only the fields passed, writes
  atomically (`tempfile.mkstemp()` + `os.replace()`) so a crash mid-write
  can't corrupt the file. Tested: happy-path update, an invalid `--status`
  value (correctly rejected by argparse before any write), and an unknown
  `--record-id` (correctly refused with no write) — all verified against
  a backup copy of the real database, which was restored and
  re-validated clean afterward.
- **`full_text_progress.py`**: read-only progress report — counts by
  retrieval status, by decision, by exclusion reason (E01–E12), any
  unresolved conflicts, and the exact numbers `PRISMA_WORKFLOW.md`/
  `prisma_flow.md` need for their "Reports sought/not retrieved/assessed"
  lines.

`full_text_retrieval_queue.csv`'s schema (`build_full_text_queue.py`'s own
`OUTPUT_FIELDS`) added to `validate_schemas.py` the same way as the other
generated schemas — no hand-duplicated declaration. All **13** tracked
files (up from 12) validate clean. `FULL_TEXT_README.md` and
`DATA_DICTIONARY.md` updated with usage and the new file's schema.

No full-text retrieval or screening has actually happened yet — this
remains tooling only, ready to use.

## 2026-09-12 (latest) — Phase 6 (full-text screening) scaffolding built

At the researcher's request, built the infrastructure for full-text
screening without doing any actual retrieval or screening work yet:

- **`code/screening/init_full_text_db.py`**: new idempotent, append-only
  seeding script mirroring `init_screening_db.py`'s design one stage
  later. Reads `screening_database.csv`, takes every record with
  `final_decision == "include"`, and appends any not already present to
  `02_screening/full_text/full_text_screening_database.csv` — never
  overwrites an existing row's retrieval status or decision, never
  silently resolves a record_id collision, warns (rather than deletes)
  if a record already in the full-text database no longer shows
  `final_decision == "include"` upstream.
- Ran it: seeded **3,659 records** (exactly the `final_decision ==
  "include"` count from the reviewer_2 merge above), all retrieval/
  decision/reviewer fields blank.
- **Deliberate design choice**: full-text tracking lives in this
  entirely separate file rather than reusing `screening_database.csv`'s
  existing-but-unused `full_text_decision`/`reviewer_1`/`reviewer_2`/
  `conflict` columns — reusing them would overwrite the title/abstract
  stage's own audit trail and gives full-text screening nowhere to put
  fields that stage never needed (retrieval status, file location).
  `screening_database.csv`'s own `full_text_decision` and reviewer
  columns are now unused/superseded; documented as such in
  `DATA_DICTIONARY.md`.
- `code/analysis/validate_schemas.py` updated to import the new file's
  schema from `init_full_text_db.py.SCHEMA`, matching how
  `screening_database.csv`'s schema is sourced from
  `init_screening_db.py` — no hand-duplicated schema declarations. All
  **12** tracked files (up from 11) validate clean.
- New `02_screening/full_text/FULL_TEXT_README.md` written for the
  researcher: how to record retrieval status (`sought`/`retrieved`/
  `not_retrievable`), where to log a retrieved file's location, how to
  apply E01–E12 exclusion codes at the full-text stage with page/section-
  level detail now possible, the same two-reviewer/conflict process as
  Phase 5, and a note that a possible future independent re-review of
  Phase 5 (raised separately by the researcher, not yet requested) would
  flow through to this file automatically via the same idempotent
  re-run, without disturbing any full-text work already logged.
- `DATA_DICTIONARY.md`, `PRISMA_WORKFLOW.md` (Phase 6 row and schema
  block), and `06_outputs/prisma/prisma_flow.md` ("Reports sought for
  retrieval" line, now n = 3,659) all updated to reflect this.
- `README.md`'s "Current status" section and top status line, both
  several rounds stale (still describing the pre-ProQuest/JSTOR search
  state and an unreviewed first-pass-only screening result), rewritten
  to match the actual current state through this Phase 6 scaffolding
  step — including carrying the reviewer_2 agreement-rate caveat
  forward rather than only having it live in `PRISMA_WORKFLOW.md`.

No full-text retrieval or screening has actually happened — this is
scaffolding only, ready for the researcher (or a future reviewer) to
start filling in.

## 2026-09-12 — Human reviewer_2 pass completed, with a flagged caveat

The researcher was sent a purpose-built Excel worksheet covering all
3,665 records reviewer_1 (AI) marked `include` or `unsure` — a one-click
dropdown decision column (Yes = include, left blank = exclude), the row
turning green on Yes, plus title/year/authors/abstract/AI-rationale/DOI/
URL for each record so no other file was needed to make the call.

The completed worksheet came back with **3,659 of 3,665 rows (99.8%)
marked Yes**. This is far above what an independent second-pass PRISMA
screening typically produces — the whole point of a second reviewer is
to catch cases the first pass got wrong, and a near-total agreement rate
is itself informative, in a way worth being honest about rather than
recording silently. Before merging anything, this was raised directly
with the researcher (not assumed to be an error, not assumed to be
genuine review) via an explicit question distinguishing three
possibilities: an accidental fill-down across the whole column, a
genuine deliberate review that happened to agree this strongly, or a
mix of both. The researcher's answer: proceed with the file as
delivered.

Merged into `screening_database.csv` on that basis:
`reviewer_2` = `Human-reviewer2-2026-09-12` for all 3,665 records;
`conflict` computed per `DATA_DICTIONARY.md`'s clarified definition
(true only where reviewer_1 made a firm `include` call that reviewer_2
then excluded -- **zero such conflicts occurred**; all 6 reviewer_2
excludes were resolutions of reviewer_1 `unsure` records, not
disagreements with a firm decision); `final_decision` populated for all
3,665 records (**3,659 include / 6 exclude**). All 11 tracked schemas
validated clean.

`PRISMA_WORKFLOW.md`, `06_outputs/prisma/prisma_flow.md`, and
`DATA_DICTIONARY.md` all updated to carry this result **alongside the
agreement-rate caveat**, explicitly instructing that any manuscript
output reporting this screening step disclose it rather than presenting
a two-reviewer PRISMA process as routine. `exclude_spotcheck_sample.csv`
(120-record random QA sample of reviewer_1's excludes) remains
unreviewed and available if the researcher wants an independent check on
that population later.

## 2026-09-11 (latest) — Search phase closed; full corpus screened; corruption caught and fixed

Six real events, in order:

1. **ProQuest full export delivered and ingested** — `SEARCH_039`, 7,728
   records via the researcher's new "My Research" account, superseding
   the earlier 100-record guest-mode sample (confirmed 97% redundant by
   title overlap, not separately ingested).
2. **ProQuest/Sociological Abstracts delivered and ingested** —
   `SEARCH_040`, 16,736 records, a broader thesaurus-term pull with a
   correspondingly wider topical spread (documented, not treated as a
   search-string defect).
3. **Search phase closed by researcher decision** — candidate pool
   (34,594 raw records at that point) judged large enough to move to
   screening. `search_log.csv` and `SEARCH_PROTOCOL.md` §7 updated to
   document this honestly, including the real gap it leaves: SSRN and
   Westlaw/Lexis were never searched at all (`SEARCH_042`/`SEARCH_043`
   stub rows record this rather than omitting it).
4. **JSTOR's 4 outstanding delivery files finally arrived** —
   `SEARCH_041`'s 50-record export, closing out a three-round "reported
   but never delivered" gap. A 100-record ProQuest file delivered
   alongside it was checked for overlap (97% redundant with SEARCH_039)
   and not separately ingested.
5. **First-pass AI screening of all 19,085 newly-added records, with a
   real data-corruption incident caught and fixed mid-round.** Screening
   19,085 records required 39 parallel ~500-record agent batches. The
   first attempt used a shared output directory across all 39 agents;
   validation afterward found several "completed" batches missing
   hundreds of rows each, with one agent's own report describing a
   helper script silently overwritten and its output redirected into a
   different batch's file — a genuine multi-agent file collision, not a
   screening-quality problem. All 39 batches were discarded and redone
   from isolated per-batch scratch directories, then validated
   record-for-record against their source files (exact record_id-set
   match, no duplicates, no foreign IDs) before merging. Final result:
   1,351 include / 17,379 exclude / 355 unsure across the 19,085 records.
6. **A second, independent gap caught during PRISMA-number
   reconciliation**: `SEARCH_041`'s 50 JSTOR records had been written to
   `raw_exports/` but never actually run through
   `deduplicate.py`/`init_screening_db.py` — caught because the raw-file
   total didn't match the dedup-output total. Re-ran the full-corpus
   dedup (34,594 raw → 27,481 unique, 7,113 merged) and screened the 28
   newly-surfaced abstract-bearing records directly: 1 include, 27
   exclude.

**Final state**: `screening_database.csv` holds 27,481 unique records,
26,222 screened (1,259 undecided for lack of an abstract) — **3,062
include / 22,557 exclude / 603 unsure**. `reviewer_2_queue.csv`
regenerated at 3,665 rows; `exclude_spotcheck_sample.csv` regenerated
(same fixed seed, 120 rows) against the corrected exclude population.
`PRISMA_WORKFLOW.md` and `06_outputs/prisma/prisma_flow.md` updated with
these final numbers and the Phase 3 closure. All 11 tracked schemas
validated clean throughout.

Two real code bugs found and fixed along the way, both now standing
protections for any future large export: (a) `csv.field_size_limit`
wasn't raised in `deduplicate.py`, `init_screening_db.py`, or
`validate_schemas.py`, which would have crashed on the two ProQuest
conference-abstract-supplement records carrying a single 600K+ character
abstract field (genuine platform behavior, not a parsing error — verified
against the raw RIS by line number); (b) the multi-agent shared-directory
corruption above, now avoided by confining each parallel screening agent
to its own scratch subdirectory.

## 2026-09-11 (later) — ProQuest and JSTOR: two methodological decisions

Cowork's next round surfaced two real, platform-forced compromises that
needed a decision from the researcher rather than being resolved
unilaterally (`PROJECT_SPEC.md` §14.18) — both logged in
`search_log.csv` (`SEARCH_039`, `SEARCH_041`) alongside the technical
detail; the decisions themselves:

- **ProQuest** (`SEARCH_039`, 8,137 total hits): guest/no-account export
  works mechanically but caps at roughly 100–200 records per session
  before a login-required error, and saves under an unrecoverable random
  filename. **Decision: the researcher will create a personal ProQuest
  "My Research" account**, which unlocks a documented 20,000-record bulk
  export — Cowork cannot create the account or enter a password on the
  researcher's behalf. Full ProQuest export is pending that account.
- **JSTOR** (`SEARCH_041`): the full search string is rejected outright
  as "too long," forcing a trim to ~9 terms across 3 clauses (a
  materially smaller vocabulary than every other database in this
  project), and even that returned 5,217 hits until an ad-hoc
  "Subject: Law" filter narrowed it to a workable 356 — excluding
  whatever JSTOR classifies under Development Studies, Public Policy,
  Urban Studies, etc. **Decision: accept the narrower, Subject:Law-only
  JSTOR search as a supplementary source** (consistent with
  `SEARCH_PROTOCOL.md` §1's own Tier 2 framing for JSTOR/SSRN/Google
  Scholar — supplementing, not matching, Tier 1 recall) rather than
  running further subject-filtered sub-searches to widen it. The full
  356 (not just the 7-record sample already pulled) still needs
  exporting — no bulk "select all" exists on JSTOR, so this is manual,
  per-item selection across roughly 15 pages.

## 2026-09-11 (earlier still) — HeinOnline begins; a SEARCH_035 integrity scare, resolved

- **`SEARCH_037` (HeinOnline, Title-restricted secondary search per
  `heinonline.md`)** ingested: 1 record ("Hear Their Voices: Australia's
  First Nations Women and the Legal Recognition of Their Rights to
  Water," O'Bryan & Harriden 2023). No structured abstract available
  from HeinOnline for this record — left blank, not fabricated; gets
  title-only triage like other abstract-less records.
- **`SEARCH_036` (HeinOnline, main three-clause full-text search)**
  logged as **count-only**: 71,226 hits, far too many to hand-compile
  and no bulk results-list export exists on HeinOnline at that volume.
  Per `REPRODUCIBILITY.md`, a real search that ran and produced a real
  total is logged even when it yields no exportable records — no records
  added under this `search_id`.
- **A serious, since-resolved integrity question on `SEARCH_035`.** A
  run log received the same day claimed the Web of Science export
  ingested in the previous round had never actually succeeded ("no
  download was ever produced... confirmed nothing in Downloads"),
  directly contradicting the 4,058 real-looking records already screened
  and pushed. Flagged to the researcher rather than resolved
  unilaterally either way (`PROJECT_SPEC.md` §14.18); a technical
  read at the time (realistic WOS accession-number entropy, correct
  journal/ISSN/publisher metadata, WoS-internal ResearcherID/GA-code
  fields very hard to fabricate at scale) suggested the data was
  genuine, but this was not independently verifiable from this
  environment.
  - **Conclusively resolved**: checked directly on the researcher's
    machine, file by file. The 5 files exist under Windows' standard
    duplicate-naming convention (`savedrecs.txt`, `savedrecs (1).txt`,
    `savedrecs (2).txt`, `savedrecs (3).txt`) rather than the 4 distinct
    names originally assumed — 1000+1000+1000+58 = 4,058 records, zero
    WOS-ID overlap, timestamped 03:52–03:57 UTC, predating the later
    session that logged the HTTP 500 failures. **The originally-ingested
    4,058 records are genuine and stand as final — nothing in this
    project's data was ever wrong.**
  - **A second, smaller instance of the same failure mode surfaced
    during the resolution itself**: the later session's own retry
    produced a `savedrecs (4).txt` that returned HTTP 200 (apparent
    success) but was a byte-for-byte duplicate of the first batch — no
    new file actually written despite the "successful" network
    response. Worth carrying forward as a standing caution for future
    rounds: a Cowork session's own claim of export success (status
    code, dialog closing normally) is not sufficient on its own for
    this platform — confirm against the actual file on disk.

## 2026-09-11 (earlier) — SEARCH_035 ingested: first Web of Science batch, second Tier 1 database

- **Web of Science is the second Tier 1 database actually searched for
  real** (`SEARCH_035`, 2026-09-11) — sent as 5 sequential tab-delimited
  `savedrecs.txt`-style export batches (WoS's native 1,000-record export
  cap; the researcher used `cowork_instructions_2026-09-11_wos_heinonline.md`
  to run it), zero overlap between batches confirmed via UT/accession
  number comparison, totaling 4,058 records after removing one exact
  internal repeat.
- **Found and fixed two real bugs in `wos_adapter.py`, previously
  unvalidated speculative code, while processing this batch:**
  1. It only handled a single CSV file; added tab-delimited
     auto-detection (comparing tab vs. comma counts in the header line)
     and multi-file merging (`--input` now takes one or more files).
  2. **A real data-corruption bug**: WoS's tab-delimited export has no
     quote-escaping at all, so a literal double-quote inside an abstract
     (common — quoting a term) was being misread by Python's csv module
     under its default quoting mode as *opening* a quoted field, which
     then silently swallowed every subsequent tab and newline as literal
     text until some *later* stray quote happened to close it —
     corrupting or merging an unpredictable number of downstream records.
     Caught by comparing each file's raw physical line count (1,000)
     against its parsed row count (as low as 988 before the fix) rather
     than assuming a clean parse; fixed by switching to
     `csv.QUOTE_NONE` for the tab-delimited path, which is actually
     correct for this format. Re-verified exact 1,000/1,000 parsing
     after the fix, then spot-checked field alignment on real records.
     `wos_adapter.py` is now genuinely validated against a real export,
     not just written speculatively.
- Full-corpus re-dedup (10,079 raw records now that WoS is in) found
  **2,934 duplicates** — far more than any prior round, as expected:
  Scopus and Web of Science index a lot of the same journal literature,
  so heavy cross-database overlap is exactly what a working dedup should
  catch. Leaves **7,145 unique records, 7,109 with a real abstract**.
  Same benign `record_id` flag as the previous round (`R36A2B99DC8AD`,
  the SEARCH_026/SEARCH_027 Scopus year-metadata quirk) recurred and was
  left untouched, as before — not a new issue.
- Screened the 1,664 newly-unique records (5 more batches, same
  independent-validation method as every prior round) against
  `INCLUSION_EXCLUSION.md`: **201 include / 1,404 exclude / 59 unsure**.
  Notably lower yield than the Scopus batches (~13% include/unsure vs.
  ~25-30%) — expected, not a screening-quality problem: `TS=` is broader
  than Scopus's `TITLE-ABS-KEY` (also searches Keywords Plus), and this
  batch is only the WoS-unique residue *after* cross-database dedup
  already removed everything WoS shared with Scopus, so it's
  disproportionately the noise Scopus's narrower field didn't also catch.
- Screening database now has **7,145 total records, 7,109 screened**
  (36 still lack a real abstract and remain deliberately undecided).
  Cumulative first-pass totals: **1,710 include / 5,151 exclude / 248
  unsure.** Refreshed `reviewer_2_queue.csv` (1,958 rows) and
  `exclude_spotcheck_sample.csv` (120-row sample, seed `20260911035`,
  regenerated fresh over the full exclude population) accordingly.
  `code/analysis/validate_schemas.py` confirms all 11 checked project
  CSVs still match their documented schema.
- `search_log.csv`'s `SEARCH_035` row documents what's confirmed (exact
  query string, per-batch counts, zero-overlap verification) and flags
  what wasn't reported back (Core Collection index selection, the
  platform's own on-screen total count) rather than guessing either —
  worth the researcher confirming for the record.

## 2026-09-11 — SEARCH_026 ingested: Scopus batch plan complete (18 of 18)

- Received and ingested `SEARCH_026` (2020, 274 records) — the one
  outstanding gap from `scopus_batch_plan_2026-08-26.md` flagged in the
  previous entry. Record count cross-checked against the researcher's run
  log (`scopus_batch_run_log_20260910.csv`, 274 shown/exported) and an
  independent file row count, both matching exactly. **All 18 planned
  Scopus batches are now done.**
- Full-corpus re-dedup (5,747 → 6,021 raw records, +274 from SEARCH_026) found 541 duplicates
  (2 more than the previous round), leaving **5,480 unique records**. One
  of the 2 new duplicates is worth noting: the same DOI appeared in both
  `SEARCH_026` (PUBYEAR=2020) and `SEARCH_027` (PUBYEAR=2019) with a
  trivial title-capitalization difference and a one-year metadata
  discrepancy — a Scopus indexing quirk (same paper, inconsistent
  year field across two of Scopus's own query contexts), not a data
  error on this project's side. Correctly DOI-matched and merged;
  `init_screening_db.py`'s existing safety check flagged the resulting
  text mismatch against the already-screened `SEARCH_027` copy rather
  than silently overwriting it — verified benign and left as-is, no
  action needed since the underlying study was already screened
  (`title_abstract_decision = include`) under its existing `record_id`.
- Screened the 272 newly-added records (batch 16, following the same
  15-batch method and validation as the previous round) against
  `INCLUSION_EXCLUSION.md`: **73 include / 182 exclude / 17 unsure**.
  Screening database now has **5,480 total records, 5,445 with a real
  abstract, all 5,445 screened** (35 records still lack an abstract and
  remain deliberately undecided). Cumulative first-pass screening
  totals: **1,509 include / 3,747 exclude / 189 unsure.**
- Refreshed `reviewer_2_queue.csv` (now 1,698 rows) and
  `exclude_spotcheck_sample.csv` (regenerated fresh over the full 3,747
  excludes, seed `20260911`) to cover the complete corpus; appended
  `SEARCH_026`'s rationale to `ai_first_pass_rationale.csv` (now 5,445
  rows). `code/analysis/validate_schemas.py` confirms all 11 checked
  project CSVs still match their documented schema.

## 2026-09-10 (final) — Reviewer 2 prep packet, PRISMA flow diagram, RIS adapter

- **Built the reviewer_2 handoff.** `02_screening/title_abstract/
  reviewer_2_queue.csv`: every `include`/`unsure` record from the AI
  first pass (1,608 rows), with title/abstract/authors/year/doi/url and
  the first-pass rationale attached, so a human second reviewer works
  from one file instead of filtering a 5,208-row database by hand.
  `exclude_spotcheck_sample.csv`: a random, fixed-seed (`20260910`,
  reproducible) 100-record sample of the 3,565 first-pass excludes, for
  false-negative spot-checking rather than a full second pass over every
  exclude — standard systematic-review QA practice. `REVIEWER_2_README.md`
  explains how to use both and is explicit that screening only these
  1,608 does not by itself satisfy `PROTOCOL.md`'s two-reviewer
  requirement for the whole title/abstract stage. Both new CSVs added to
  `validate_schemas.py` and `DATA_DICTIONARY.md`.
- **Populated `06_outputs/prisma/prisma_flow.md`** (previously an
  all-placeholder stub) with real counts through the title/abstract
  screening stage: 5,710 records identified from Scopus, 37 from the
  WebSearch pilot/exemplars, 539 duplicates removed, 5,173 screened (35
  left unscreened — no abstract), 3,565 excluded (full E01–E12 code
  breakdown), 1,608 carried forward. Everything from "reports sought for
  retrieval" onward is left genuinely blank — that work hasn't started —
  and every screening-stage number is explicitly flagged provisional
  (reviewer_1/AI only, no `reviewer_2` yet).
- **Added `code/search/adapters/ris_adapter.py`**: one shared,
  **unvalidated** adapter for the RIS citation-export format, covering
  HeinOnline, ProQuest, Sociological Abstracts, JSTOR, and SSRN — all of
  which offer RIS export per their `database_strategies/*.md` files.
  Grounded in the RIS format itself (a real, long-published standard),
  not a guessed platform-specific CSV layout, which is why one adapter
  can responsibly cover five platforms at once. Handles multiple authors,
  wrapped/continuation lines, and both common tag variants per field
  (TI/T1, PY/Y1, AB/N2, UR/L1/L2) — tested against synthetic RIS data
  covering all of that plus a missing-title record and a not-actually-RIS
  file, both of which fail cleanly rather than silently producing
  garbage.
- **Deliberately did not** build adapters for Westlaw/Lexis (neither
  platform offers a standard bulk export to build against without
  guessing — `PROJECT_SPEC.md` §14) or for CanLII/Rechtspraak.nl/
  Brazilian court portals/ANA-SNIS (these feed the doctrinal/jurimetric
  strand of the project, not this screening pipeline — merging their
  hits through this pipeline would be wrong, not just premature). Each
  `database_strategies/*.md` file now says so explicitly rather than
  leaving the absence unexplained.

## 2026-09-10 (earlier) — First-pass AI title/abstract screening, all 5,173 abstract-bearing records

- **Real title/abstract screening against `INCLUSION_EXCLUSION.md` has now
  actually happened**, for the first time in this project, on every
  record with a real abstract. This is a first pass by Claude, explicitly
  authorized by the researcher as an AI reviewer (`reviewer_1`) — per
  `PROTOCOL.md` §"Selection process" ("two reviewers where feasible") and
  `PROJECT_SPEC.md` §14.18 ("ask for human confirmation when a major
  methodological choice is genuinely ambiguous"), this was surfaced to
  the researcher as a choice rather than decided unilaterally, then
  proceeded on explicit instruction. **`reviewer_2` (a human) and
  conflict resolution have not happened — these decisions are
  provisional, not final**, exactly like any single reviewer's pass in a
  real dual-review PRISMA process.
- Method: the 5,173 records with a real abstract were split into 15
  batches of ~350 and screened independently by subagents, each reading
  `INCLUSION_EXCLUSION.md` directly and applying its 9 inclusion criteria,
  11 exclusion criteria, and E01–E12 exclusion-code table. Every batch's
  output was validated before merging: exact record_id order and coverage
  match against its input, every `exclude` decision carries exactly one
  valid E01–E12 code, no `include`/`unsure` row carries a stray code, no
  duplicate record_ids across batches, and no already-decided row was
  ever touched (the merge script refuses outright on any of these). The
  35 records without a real abstract (grey literature / older exports)
  were deliberately left undecided — this project's own convention (see
  `title_only_triage_memo.md`) is that title-only triage is non-binding,
  never a substitute for reading an abstract.
- **Results: 1,436 include / 3,565 exclude / 172 unsure**, out of 5,173
  screened (35 of 5,208 total records left undecided, no abstract).
  Exclusion code breakdown: E01 wrong topic 1,555; E06 engineering only
  780; E05 no empirical evidence 487; E04 wrong outcome 255; E07 wrong
  service 320; E03 water-quality-only 65; E09 insufficient information
  63; E02 wrong population 21; E08 duplicate 18; E11 wrong
  jurisdiction/context 1. Consistent with the batch plan's own
  expectation (`scopus_batch_plan_2026-08-26.md`, `EXECUTION_CHECKLIST.md`)
  that this broad, high-recall OR-heavy Boolean search would surface a
  lot of engineering/hydrology/water-quality noise alongside the
  genuinely on-topic records.
- `reviewer_1` is set to `Claude-AI-1stpass-2026-09-10` on every screened
  row, so it's always traceable which decisions came from this pass
  versus a human reviewer. `title_abstract_decision` of `unsure` should
  be treated the same as `include` for full-text-stage purposes (proceed
  to read it) — these are records the first-pass reviewer explicitly
  could not confidently resolve from title+abstract alone, not a
  rejection.
- **What this is not**: not a final inclusion/exclusion decision (needs
  `reviewer_2` and conflict resolution per `PROTOCOL.md`), not full-text
  screening, not data extraction, not risk-of-bias appraisal. The 1,436
  (+172 unsure = up to 1,608) candidate records are the pool that Phase 6
  (full-text screening) will actually work from once a human reviewer's
  pass exists to compare against.
- `code/analysis/validate_schemas.py` confirms all 8 checked project CSVs
  still match their documented schema after this round.

## 2026-09-10 (later still) — Stable record_id migration; Web of Science adapter

- **Replaced positional `record_id` assignment with a stable content
  hash**, closing the follow-up flagged in the previous entry.
  `code/search/deduplicate.py`'s `compute_record_id()` now keys on the
  normalized DOI when present, else normalized title+year — the same
  fields the duplicate matcher itself already uses — so a record's ID no
  longer depends on which files happen to be present or what order they
  sort in. Collision-checked: three genuine content collisions surfaced
  during the full re-run (two different generic-titled records sharing a
  normalized title+year, e.g. a recurring report-series title), correctly
  disambiguated with a `-1` suffix rather than silently merged.
- Did this migration now specifically because it was still safe to:
  confirmed **zero rows** in `screening_database.csv` had any decision
  field set (`title_abstract_decision`, `full_text_decision`,
  `reviewer_1`, `reviewer_2`, `final_decision`) before touching a single
  ID. Regenerated `deduplicated_records.csv` and
  `screening_database.csv` in full from a fresh re-run across all of
  `01_search/raw_exports/` under the new scheme, then verified **zero
  orphans**: every one of the previous 5,314 rows matches (by DOI or
  normalized title+year) something in the new 5,208-row output. The
  106-row reduction is not data loss — it's genuine duplicates that had
  slipped past the old positional-ID incremental matching across earlier
  rounds, now correctly collapsed by one clean full-corpus dedup pass.
  Remapped the 37 `record_id`s referenced in
  `06_outputs/supplementary/title_only_triage_memo.md` to match.
- Added `code/search/adapters/wos_adapter.py`: **unvalidated** (no real
  Web of Science export exists in this project yet, same status
  `pubmed_adapter.py` carried before SEARCH_018), written ahead of time so
  ingestion is instant once the researcher runs
  `database_strategies/wos.md`. Handles both CSV shapes Web of Science's
  UI can produce (full-word "Export → Excel" headers, and the classic
  two-letter Core Collection field tags), tested against synthetic data
  covering both plus a missing-required-column failure case.
- `code/analysis/validate_schemas.py` confirms all 8 checked project CSVs
  still match their documented schema after the migration.

## 2026-08-22 (later) — PR opened; preregistration draft + Phase 4/5 tooling

- Opened PR #3 (`claude/legal-last-mile-review-spec-8ri0zs` → `main`) on the
  jrklaus8/water-law-dataset repository.
- Drafted the OSF Generalized Systematic Review preregistration text
  (`00_admin/preregistration/osf_preregistration_draft.md`) — not
  submitted; this environment has no OSF account access.
- Wrote and tested `code/search/deduplicate.py` (DOI-match and
  title/year-similarity-match deduplication, with a full merge log for
  auditability) against synthetic data — not yet run on real data, since
  none exists. Documents that it expects input already normalized to a
  common schema; per-database raw-export adapters remain future work to be
  developed against real exports once Phase 3 produces any.
- Wrote and tested `code/screening/init_screening_db.py` (idempotent merge
  of newly deduplicated records into the persistent screening database,
  never overwriting an existing reviewer decision) against synthetic data.
- Updated `PRISMA_WORKFLOW.md` and `README.md` status tables accordingly.
  Phase 3 (database searching) remains the hard blocker — no credentials
  exist in this environment for any Tier 1 database.

## 2026-08-25 — Confirmed network egress is blocked; ran exploratory WebSearch pilot

- Tested direct access to PubMed's API (`curl`) and to PubMed, Google
  Scholar, CanLII, Rechtspraak.nl, and SSRN (`WebFetch`) — every one was
  denied by this environment's network egress policy (confirmed via
  `/root/.ccr/agentproxy/status`, a genuine policy denial rather than a
  transient failure, per that tool's own guidance not to retry). This
  environment therefore cannot reach any database, free or paid, by direct
  fetch or API call — only Claude's first-party `WebSearch` tool works.
- Amended the screening-database schema to add a `url` field alongside
  `doi` (`02_screening/title_abstract/screening_database.csv`,
  `code/search/deduplicate.py`, `code/screening/init_screening_db.py`,
  `DATA_DICTIONARY.md`, `PRISMA_WORKFLOW.md`) — real candidate records,
  especially grey literature, routinely have no DOI, and a URL is the only
  way to relocate them.
- Ran six explicitly non-systematic `WebSearch` queries drawn from
  `SEARCH_PROTOCOL.md`'s terms, logged as `SEARCH_003`–`SEARCH_008` in
  `01_search/search_logs/search_log.csv` with the pilot's method and
  limitations stated on every row. Extracted only title + URL from
  WebSearch's structured result data (never from its prose summary, which
  is itself an LLM paraphrase and risks introducing unverified specifics)
  into `01_search/raw_exports/SEARCH_003-008_WEBSEARCH_PILOT_2026-08-25.csv`
  — 25 candidate records, no fabricated authors/years/DOIs (left blank
  where not directly legible from the search result itself).
- Ran `code/search/deduplicate.py` and `code/screening/init_screening_db.py`
  on this real data for the first time (previously only synthetic-data
  tested) — 0 duplicates within the batch, 25 records now in
  `02_screening/title_abstract/screening_database.csv` with no screening
  decision made on any of them.
- Updated `SEARCH_PROTOCOL.md`, `PRISMA_WORKFLOW.md`, `README.md`, and
  `06_outputs/supplementary/preliminary_results.md` to state clearly, in
  each place, that this pilot is not Phase 3 and does not substitute for
  it — it exists so the deduplication/screening tooling has real data to
  operate on and so genuine (if low-recall) candidate studies are already
  identified once real screening capacity exists.

## 2026-08-25 (later) — Second pilot round, schema-validation tooling, triage memo

- Added `code/analysis/validate_schemas.py`: checks every project CSV's
  actual header against its documented (or script-generated) schema.
  Verified it catches real drift with a synthetic test, then confirmed all
  8 checked files are currently consistent — useful given the schema has
  already changed once (the `url` field).
- Ran a second WebSearch pilot round: an approximated backward-citation
  search on all 4 exemplar papers from `SOURCES.md` (WebSearch has no real
  citation-graph capability, so this is a keyword approximation, logged as
  such), plus a World Bank/UN-Habitat grey-literature query and a
  connection/service-refusal query. Logged as `SEARCH_009`–`SEARCH_013`,
  including two searches that found nothing new (Gaikwad/Thomas citations,
  too recent for a citation index; Halling/Bækgaard citations, real hits
  but out of this review's water/sanitation scope — logged as a scope
  demonstration, not a failure).
- Added 6 new genuine candidates from this round to
  `01_search/raw_exports/SEARCH_009-013_CITATION_GREYLIT_PILOT_2026-08-25.csv`;
  total candidate pool now 31 records, still 0 duplicates.
- Added `06_outputs/supplementary/title_only_triage_memo.md`: a title/URL-only,
  explicitly non-binding read of all 31 candidates against
  `INCLUSION_EXCLUSION.md`, since this environment cannot fetch abstracts.
  Does not populate `title_abstract_decision` for any record. Flagged a
  recurring pattern for the eventual reviewer: three law-review articles
  whose doctrinal-vs-empirical status can't be resolved from the title.

## 2026-08-25 (later still) — Third pilot round targeting gaps; exemplars added to pipeline; PubMed adapter

- Ran a third WebSearch round targeting gaps identified in the first two:
  Family B (bureaucratic assistance/political coordination + water),
  Dutch-language empirical studies specifically, Brazilian ANA/SNIS
  regulatory-data studies, and WHO/UNICEF JMP grey literature. Logged as
  `SEARCH_014`-`SEARCH_017`.
- Found a likely duplicate-publication pair: an earlier working-paper
  title appears to be a pre-publication version of the Gaikwad & Thomas
  2026 exemplar. Logged both per `REPRODUCIBILITY.md` §6 (identify, don't
  silently merge) rather than dropping the earlier one.
- Second Dutch-language query in a row surfaced zero empirical studies
  (only primary legal/regulatory sources) — logged as a preliminary,
  WebSearch-only pattern, explicitly caveated as far too thin a basis to
  draw any conclusion about the Dutch empirical literature.
- WHO/UNICEF JMP 2025 report deliberately excluded from the candidate pool:
  relevant background, but per its own summary it doesn't treat legal/
  administrative barriers as a distinct topic, failing inclusion
  criterion 2 — a scope-discipline exclusion, not a search failure.
- **Found and fixed a real gap**: 3 of the 4 substantive exemplar studies
  in `SOURCES.md` (Lubeck-Schricker et al. 2023, Gaikwad & Thomas 2026,
  Apio/Thiam/Dinar 2025) had been cited as methodological context but
  never actually entered the screening pipeline, meaning they'd never be
  formally screened like everything else. Added them with their
  already-verified DOIs. The 4th exemplar, Halling & Bækgaard 2024,
  deliberately was not added — it's administrative-burden methodological
  literature with no water/sanitation content, failing inclusion
  criterion 1; it remains a `SOURCES.md`-only methodological reference.
- Total candidate pool now 37 records, still 0 duplicates found by the
  automated dedup script (the 2 likely-duplicate pairs identified above
  differ enough in title that automated matching correctly can't catch
  them — exactly why they were logged manually instead).
- Added `code/search/adapters/pubmed_adapter.py`: normalizes PubMed's
  documented CSV export format to the project's common schema. Explicitly
  marked **unvalidated against a real export** (PubMed is unreachable from
  this environment) — tested against a synthetic file matching the
  documented format (works) and a deliberately wrong format (correctly
  refuses to guess rather than producing silently-wrong output).
- Updated `06_outputs/supplementary/title_only_triage_memo.md` for the 6
  new records.

## 2026-08-25 (latest) — Execution checklist for real institutional access

- The researcher confirmed a working EUR (Erasmus University Rotterdam)
  institutional research account, which should give real access to
  Scopus, Web of Science, HeinOnline, Westlaw, Lexis, and ProQuest.
- Added `01_search/EXECUTION_CHECKLIST.md`: a literal, step-by-step
  "what to actually click" guide per database — access route (via the
  library, not the database directly), where to paste each search string,
  export format/field selection (emphasizing abstracts, not just
  citations, since every candidate identified so far has been title-only),
  file-naming convention, and exactly what to hand back to Claude. Written
  to be followable without the rest of this repo's context, since the
  researcher intends to execute it via a separate tool (Claude Cowork).
- This does not touch credentials at all: Claude does not have and will
  not request the researcher's institutional login. Two independent
  reasons this has to be human-executed rather than automated from this
  environment: (1) network egress from this environment is blocked for
  every external domain tested, regardless of credentials; (2)
  institutional SSO logins involve MFA/interactive flows a script can't
  drive, and most of these platforms' license terms prohibit automated or
  bulk retrieval even by authorized users.
- Cross-linked from `README.md` and `SEARCH_PROTOCOL.md` §8.

## 2026-08-26 — First real Tier 1 database data (Scopus)

- The researcher ran the pilot Scopus string for real via EUR institutional
  access (Claude Cowork assisted) and uploaded the results as two GitHub
  PRs (#4, #5) containing PDFs and CSVs. **Flagged immediately: PR #4/#5
  contain 24 copyrighted journal-article PDFs (Nature, Springer, BMC)
  pushed to public branches — a likely redistribution problem independent
  of this project. Recommended deleting those branches/files rather than
  merging; only bibliographic metadata belongs in this repo.**
- Of the uploaded files, one was actually usable as review data:
  `export_d3841da0-...csv`, a genuine 500-record Scopus export (Authors,
  Title, Year, Source title, DOI, Link, Document Type, etc. — confirmed
  real Scopus export header). `Scopus-200-Analyze-Year.csv` was not a
  document-level export at all — it's Scopus's "Analyze results by Year"
  aggregate count feature, useful only for reconstructing the *total* hit
  count (summed to ~5,443 for the unrefined pilot string) and not ingested
  as data.
- Wrote and ran `code/search/adapters/scopus_adapter.py` — **validated
  against a real export**, unlike the still-unvalidated PubMed adapter.
  Normalized 500 records into `01_search/raw_exports/SEARCH_018_SCOPUS_2026-08-26.csv`,
  logged as `SEARCH_018` with the real query, the ~5,443 total count, and
  the gaps (no abstracts in this export; only 500 of ~5,443 exported).
- Ran the full pipeline on the combined pool (37 WebSearch-pilot + 500
  Scopus records): `deduplicate.py` found **1 real cross-source
  duplicate** — the Gaikwad & Thomas 2026 exemplar, independently added
  earlier from `SOURCES.md`, also appeared in the live Scopus results,
  correctly matched by DOI. This is the first real validation of the
  dedup logic against two independent real sources, not synthetic test
  data. Screening database now has **536 unique records**.
- Spot-checked the first 15 Scopus titles: a healthy mix of clearly
  on-topic hits and expected noise from a broad, sensitive Boolean string
  (corona-discharge hardware, blockchain, coastal-ecosystem valuation) —
  normal at this stage; screening exists to filter exactly this.
- Two follow-ups flagged for the researcher: (1) re-export with the
  Abstract field explicitly selected — none of these 500 records have one;
  (2) only ~9% of the total ~5,443 matching documents were exported —
  getting the rest needs either batching (e.g. by year range, since
  Scopus's bulk-export UI appears to cap a single CSV well below the full
  result count) or narrowing the query.

## 2026-08-26 (later) — Removed all 43 copyrighted PDFs from every branch

- 43 full-text journal-article PDFs (Nature, Springer, BMC/BioMed Central)
  had accumulated across three separate uploads: 10 on `jrklaus8-patch-1`
  (PR #4), 13 on `jrklaus8-patch-2` (PR #5), and 20 directly on this
  review branch. Flagged to the researcher as a copyright/redistribution
  concern independent of the research use itself.
- Closed PR #4 and PR #5 without merging.
- Removed the 10 and 13 PDFs from `jrklaus8-patch-1`/`jrklaus8-patch-2` via
  a direct git push updating each branch (GitHub's file-delete API choked
  on the large binaries; branch *deletion* was blocked by the same
  ruleset that blocked branch creation earlier in this project, but a
  normal branch *update* was not).
- Removed the 20 PDFs from this branch the same way.
- Before removing anything, recovered all 43 from git history and sent
  them directly to the researcher (not through GitHub) for them to store
  privately, per their request — see
  `01_search/raw_exports/native/README.md` for the accounting. None of
  the 43 remain in this repository in any form; their bibliographic
  metadata (for the 10+13 that came from the Scopus session) is preserved
  in `01_search/raw_exports/native/SEARCH_018_SCOPUS_2026-08-26_native.csv`.
- Confirmed via `git ls-tree` on both upload branches after the push that
  no PDF remains reachable from either branch tip. Noted as a caveat to
  the researcher: this doesn't purge the blobs from git's object history
  (recoverable by anyone with the old commit SHA) — a harder guarantee
  would need branch deletion (blocked here) or a GitHub-side history purge.

## 2026-09-10 — First abstracts; SEARCH_021b ingested

- Received the first batch from `scopus_batch_plan_2026-08-26.md`:
  `SEARCH_021b` (2025, non-article/non-review document types — the
  "everything else" half of the 2025 split; `SEARCH_021a`, articles and
  reviews, has not been run yet), 106 records. **This export includes
  Abstract, Author Keywords, and Index Keywords** — the first real
  abstract-bearing data in this project.
- Amended the project schema to actually carry this through, since
  neither the adapter nor the screening database had an `abstract` field
  before now:
  - `code/search/deduplicate.py`: added `abstract` as an *optional*
    normalized field (not required — older files without it still load).
    Also fixed a latent correctness bug this surfaced: when two sources
    describe the same record and only one has an abstract, the dedup
    logic was keeping whichever file sorted first alphabetically and
    discarding the other's abstract along with the duplicate. Now the
    kept record is backfilled with the abstract if it was missing one —
    verified with a synthetic test using filenames ordered the way they
    actually appear in production (abstract-less source sorting first),
    which is the case that would have silently failed before.
  - `code/screening/init_screening_db.py`: same backfill logic for a
    record already sitting in the screening database from an earlier,
    abstract-less run — the one narrow exception to "never touch an
    existing row," since backfilling a blank abstract isn't touching a
    decision field.
  - `code/search/adapters/scopus_adapter.py`: now maps the Abstract
    column through when present (previously just warned that it existed
    and dropped it).
  - Migrated all 536 existing `screening_database.csv` rows to the new
    16-field schema (blank `abstract`) rather than leaving them on an
    incompatible header.
- Ran the full pipeline on the combined pool: 0 new duplicates from this
  batch specifically (the one duplicate in the log is the pre-existing
  Gaikwad & Thomas exemplar match from 2026-08-26). Screening database now
  has **642 unique records, 106 of which have a real abstract** for the
  first time — real title/abstract screening against
  `INCLUSION_EXCLUSION.md` is now possible on that subset, though it
  hasn't been done yet.
- Note on this specific batch's composition: because `SEARCH_021b` is
  deliberately the non-article/review half of 2025 (book chapters,
  conference papers, an erratum, etc. — see the batch plan), it is not
  representative of Scopus's 2025 output as a whole; `SEARCH_021a`
  (articles + reviews) is where the more substantive primary research is
  expected to land.

## 2026-09-10 (later) — 17 of 18 Scopus batches ingested

- Received and processed the remaining 16 batches of
  `scopus_batch_plan_2026-08-26.md` in one round: `SEARCH_019` (2027, 2),
  `SEARCH_020a` (2026 articles+reviews, 556), `SEARCH_020b` (2026
  everything else, 100), `SEARCH_021a` (2025 articles+reviews, 477),
  `SEARCH_022` (2024, 392), `SEARCH_023` (2023, 337), `SEARCH_024` (2022,
  326), `SEARCH_025` (2021, 324), `SEARCH_027` (2019, 254), `SEARCH_028`
  (2018, 241), `SEARCH_029` (2016–2017, 375), `SEARCH_030` (2014–2015,
  315), `SEARCH_031` (2012–2013, 293), `SEARCH_032` (2009–2011, 367),
  `SEARCH_033` (2003–2008, 388), `SEARCH_034` (1928–2002, 357). All 16
  were exported with Abstract, Author Keywords, and Index Keywords, same
  as `SEARCH_021b`. Every native file preserved untouched in
  `01_search/raw_exports/native/`; every normalized file in
  `01_search/raw_exports/`; every batch logged as its own row in
  `search_log.csv`, built from the researcher's own authoritative run log
  (`scopus_batch_run_log_20260910.csv`) rather than reconstructed — every
  exported-record count cross-checked against that log and against an
  independent row count of each raw file, all matching exactly. Confirms
  `SEARCH_020a`/`SEARCH_021a`'s earlier finding that there is no hard
  500-record export ceiling when signed in via EUR proxy — both
  oversized DOCTYPE halves (556 and 477 records) exported whole.
- 17 of the 18 planned batches are now done. `SEARCH_026` (2020, ~274
  records per the run log) was run by the researcher but its export CSV
  has not been uploaded to this project yet — flagged in
  `scopus_batch_plan_2026-08-26.md` as the one remaining gap.
- Re-ran `code/search/deduplicate.py` across the full accumulated corpus
  (all `01_search/raw_exports/*.csv`): **5,208 unique records kept, 539
  duplicates merged** (mostly by DOI match; several backfilled a missing
  abstract from the surviving record's duplicate per the existing
  backfill rule). Re-ran `code/screening/init_screening_db.py`: 4,659 new
  records appended, 501 existing records backfilled with an abstract they
  previously lacked.
- **Found and fixed a latent record_id collision bug** surfaced by this
  round's scale: `deduplicate.py` assigns `record_id` positionally
  (`R0001`, `R0002`, ...) by file-processing order across
  `01_search/raw_exports/`. Adding 16 new files shifted that ordering
  enough that 13 IDs in the new dedup run collided with unrelated,
  already-screened-pool records from earlier rounds (same ID, different
  title/DOI). `init_screening_db.py`'s existing safety check correctly
  refused to overwrite the 13 old rows (so nothing was corrupted), but
  also silently skipped appending the 13 legitimately-new records under
  those colliding IDs — a real (if narrow) data-loss risk, not a
  duplicate. Manually verified all 13 were genuinely different
  title+DOI pairs, then appended them under 13 fresh unused IDs
  (`R5748`–`R5760`). **This is a structural limitation of the current
  positional ID scheme, not a one-off bug** — it will recur any time a
  new file is added whose sort position is before existing files' tail
  end and the corpus is large enough for a same-position collision;
  a content-hash-based `record_id` would eliminate it, but that is a
  larger migration (it would need to remap 5,300+ existing IDs) and is
  left as a known follow-up rather than done inline here.
- Screening database now has **5,314 unique records, 5,279 of which have
  a real abstract**. `code/analysis/validate_schemas.py` confirms all 8
  checked project CSVs still match their documented schema after this
  round. No screening decision has been made on any of them — this is
  still search, not screening.

## 2026-08-26 (latest) — Scopus batch export plan

- Added `01_search/scopus_batch_plan_2026-08-26.md`: 16 ready-to-paste
  batch queries to capture the remaining ~4,944 of ~5,444 total matching
  Scopus records, computed from the real year-by-year breakdown (not a
  guess) so each batch stays comfortably under the 500-record ceiling the
  first export hit. Flags that 2026 and 2025 alone (619 and 583 records)
  exceed that ceiling even as single years and need a further
  `DOCTYPE`-based split.
- Cross-linked from `EXECUTION_CHECKLIST.md`. Every batch still needs
  Abstract selected explicitly in the export field picker — the one gap
  that actually blocks real screening, and the main reason to finish
  Scopus before moving to a second database.
- Not yet executed — this is a plan, not new data.

## 2026-08-22 — Initial scaffold

- Repository structure created per the eleven-phase folder architecture
  (`00_admin/` through `11_archive/`, plus `data/` and `code/`).
- Governing documents written: `README.md`, `PROJECT_SPEC.md`,
  `PROTOCOL.md`, `SEARCH_PROTOCOL.md`, `INCLUSION_EXCLUSION.md`,
  `CODEBOOK.md`, `RISK_OF_BIAS.md`, `ANALYSIS_PLAN.md`,
  `PRISMA_WORKFLOW.md`, `DATA_DICTIONARY.md`, `REPRODUCIBILITY.md`,
  `PUBLICATION_PLAN.md`, `SOURCES.md`, `sources.bib`.
- Empty, header-only CSV templates created for the search log, screening
  database, exclusion log, extraction database, evidence map, and effect
  sizes — no data populated.
- Per-database search strings drafted for Scopus, Web of Science, PubMed/
  Global Health, HeinOnline, Westlaw/Lexis, ProQuest/Sociological
  Abstracts, JSTOR/Google Scholar/SSRN, CanLII, Rechtspraak.nl, and
  Brazilian legal/regulatory databases, plus grey-literature guidance —
  **none executed**.
- Eight preliminary methodological sources checked against independent web
  sources (publisher domains and doi.org were unreachable in this
  environment; see `SOURCES.md` for method and caveats). Two sources
  (PRISMA-P 2015, AMSTAR 2) remain unverified beyond the original citation
  and are flagged as such.
- Decided, following `PROJECT_SPEC.md` §3, that no title or framing implying
  a completed meta-analysis will be used until Phase 11–12 of
  `PRISMA_WORKFLOW.md` establishes that pooling is defensible for a given
  evidence family.
- Decided the systematic review's evidence base and the existing Global
  Water Law Judicial Decisions Dataset in this repository will not be
  merged (`PROJECT_SPEC.md` §9); they are cross-referenced but kept as
  separate evidence populations even though they share a git repository.

No search has been executed. No study has been screened, extracted, or
appraised. No effect size exists anywhere in this project.
