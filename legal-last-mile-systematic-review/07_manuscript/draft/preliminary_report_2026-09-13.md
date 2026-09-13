# The Legal Last Mile: Legal and Administrative Barriers to Water and Sanitation Access

### Systematic Review Protocol and Interim Descriptive Report

Junior Klaus
Erasmus University Rotterdam
Draft of 2026-09-13

---

> **Status of this document.** This is a **preliminary, in-progress working
> draft**, not a completed manuscript. It reports the pre-specified protocol
> and framework (fixed 2026-08-22, before any database was searched) and the
> **actual, current, provisional** state of search, screening, and
> extraction. It contains **no Results, Discussion, or Conclusion section**,
> and it draws no inference about whether the "Legal Last Mile" framework is
> supported, qualified, or rejected by the evidence. That is a deliberate
> choice, not an omission: only 175 of the 3,659 records that passed
> title/abstract screening have been assessed at full text (≈4.8%), risk-of-
> bias appraisal has not started for any of the 85 studies extracted so far,
> and the quantitative-synthesis feasibility decision tree
> (`ANALYSIS_PLAN.md` §2) has not been run. Writing conclusions ahead of that
> work is exactly what this project's own governing principle forbids (see
> §7 below). Every number in this document should be treated as provisional
> and expected to change — often substantially — as screening continues.
> Source data: `legal-last-mile-systematic-review/` in
> `github.com/jrklaus8/water-law-dataset`.

---

## Abstract

**Background.** Physical proximity to water or sanitation infrastructure
does not guarantee a household's formal, effective access to it. This
project investigates the "Legal Last Mile" — the legal and administrative
space between physical availability of a service and its actual realization
for a household — as a candidate mechanism, comparing evidence primarily
drawn from Brazil, the Netherlands, and Canada (Ontario) but not restricted
to them.

**Objective.** To systematically review empirical evidence on how legal
eligibility rules, administrative burden, discretion/accommodation, and
enforcement shape household water and sanitation access, and to determine
what quantitative synthesis, if any, that evidence supports.

**Methods (pre-specified).** PRISMA 2020-guided systematic review with a
structured quantitative evidence synthesis and contingent, restricted
meta-analysis (never a single universal pooled estimate — see §3.7).
Six databases searched (Scopus, Web of Science, HeinOnline, ProQuest,
ProQuest/Sociological Abstracts, JSTOR), with disclosed coverage gaps
(§3.3). Two-stage screening (title/abstract, then full text) against
standardized E01–E12 exclusion criteria. Extraction against a 92-field
codebook. Design-matched risk-of-bias tools, not yet applied.

**Status as of 2026-09-13 (all figures provisional).** 27,481 unique
candidate records after deduplication; 3,659 advanced past title/abstract
screening; full-text screening 175/3,659 complete (85 include / 90
exclude); all 85 current full-text includes fully extracted, spanning 36
countries/territories across six world regions, publication years
2021–2026. No risk-of-bias ratings assigned. No quantitative-synthesis
feasibility determination made. No pooled or narrative findings are
reported here.

**This is a methods-and-status report, not a findings report.**

---

## 1. Introduction

Inadequate access to water and sanitation is conventionally analyzed as a
problem of physical infrastructure — pipes, treatment capacity, distance to
source. A parallel and less-studied possibility is that even where
infrastructure exists nearby, a household's *legal and administrative*
status can determine whether that infrastructure ever becomes a formal,
usable connection. Legal recognition of a settlement, the burden of
documentation required to apply for service, the discretion an official
exercises in processing an application, and the mechanisms available to
enforce or contest a denial are all candidate explanations for why
geographically similar households end up on opposite sides of a connection
line.

This review takes as its working device the **"Legal Last Mile"**: the
space between physical availability and formal realization of a water or
sanitation connection. Consistent with this project's anti-confirmation-bias
commitment (`PROJECT_SPEC.md` §1–2), the Legal Last Mile is treated
throughout as a hypothesis to be tested against the assembled evidence, not
a conclusion the review is designed to prove. No directional hypothesis is
pre-registered; the review instead pre-specifies a mechanism framework (§2
below) to be supported, qualified, or rejected by what the literature
actually shows.

Two studies extracted into this review so far illustrate why the question is
live rather than settled. Lubeck-Schricker et al. (2023) find that within a
single Mumbai slum, non-notified (legally unrecognized) households used 37%
less water per capita than notified households in the same neighborhood,
after adjusting for income and religion — a legal-status effect operating
*within*, not just *between*, informal settlements. Gaikwad and Thomas
(2026), in a cluster-randomized field experiment in the same city, find that
bureaucratic assistance with the application process increased formal water
connections only when *combined with* organized political pressure on
elected officials — suggesting the relevant barrier is not a single
administrative step but an interaction between bureaucratic and political
constraints. These two studies alone illustrate both the promise of the
Legal Last Mile framework and the reason a single pooled effect across all
such studies would misrepresent what is actually a heterogeneous set of
mechanisms — the core methodological judgment this review is built around
(`PROJECT_SPEC.md` §3).

This introduction is illustrative, not a literature review in itself — the
systematic literature review is the object of this project, still in
progress, and its own results are what should eventually populate this
section in full.

---

## 2. Conceptual Framework

*(Pre-specified in full before any database was searched — `PROJECT_SPEC.md`
§5–7; unchanged since 2026-08-22.)*

```
STRUCTURAL CONDITIONS
  legal status · property status · documentation · income · geography · institutional capacity
        ↓
ADMINISTRATIVE ARCHITECTURE
  eligibility screening · administrative burden · discretion · accommodation · enforcement · review · participation
        ↓
ADMINISTRATIVE NAVIGATION
  understand requirements · apply · satisfy requirements · obtain accommodation · challenge decisions
        ↓
SERVICE ACCESS
  formal connection · continuity · reliability · quantity · affordability · effective use
        ↓
INCLUSION / EXCLUSION
```

Administrative law is treated as the central analytical lens, not the only
possible causal factor — evidence may equally involve property law,
planning law, municipal law, identity systems, land regularization, utility
regulation, or political institutions.

**Mechanism families** (a study may exhibit more than one):

| Family | Description |
|---|---|
| `ELIGIBILITY` | Legal/administrative rules determining who may apply for or receive service |
| `BURDEN` | Documentation, procedural steps, cost, and time required to establish eligibility |
| `DISCRETION_ACCOMMODATION` | Official discretion in processing applications; hardship exceptions; accommodation |
| `ENFORCEMENT` | Sanctions, disconnection/reconnection, complaint and review mechanisms |

**Outcome hierarchy** (never pooled across families simply because all are
colloquially "access" — `PROJECT_SPEC.md` §7):

1. **Primary:** formal household connection (connected vs. not; probability
   of connection/formalization; approval/refusal)
2. **Effective access:** quantity, reliability, continuity, service hours,
   quality, distance to source
3. **Economic access:** connection cost, expenditure, affordability, tariff
   burden
4. **Administrative outcomes:** submission, completion, approval, refusal,
   delay, appeal, complaint, enforcement action

**Candidate meta-analytic families** identified in advance
(`PROJECT_SPEC.md` §8) — whether any contains enough comparable studies to
pool is a question for Phase 11, not yet answered:

- **Family A** — legal recognition (recognized vs. unrecognized settlement,
  formal vs. informal tenure) → formal connection / access / quantity /
  reliability. *Strong a priori candidate.*
- **Family B** — bureaucratic/administrative assistance → formal connection
  / application success. *Potentially highly causal but the study count may
  be too small to pool.*
- **Family C** — legal/administrative barriers → unequal access. *Likely
  too heterogeneous to pool; probable candidate for structured narrative
  synthesis instead.*

---

## 3. Methods

### 3.1 Research question

How do legal and administrative institutions shape the translation of
physical availability of water and sanitation infrastructure into effective
household access, and what evidence exists on the mechanisms — eligibility
screening, administrative burden, discretion, accommodation, and
enforcement — through which they produce or mitigate exclusion?

### 3.2 PECO

- **Population:** households, individuals, applicants, or communities with
  potential physical access to water or sanitation infrastructure.
- **Exposure:** legal and administrative access conditions (eligibility
  screening, administrative burden, discretion/accommodation, enforcement).
- **Comparator:** varies by study family — usual procedure, absence of the
  condition, or a recognized/unrecognized contrast; recorded per study.
- **Outcome:** per the hierarchy in §2.

### 3.3 Eligibility criteria and information sources

Standardized exclusion codes (`INCLUSION_EXCLUSION.md`):

| Code | Reason | Code | Reason |
|---|---|---|---|
| E01 | Wrong topic | E07 | Wrong service |
| E02 | Wrong population | E08 | Duplicate |
| E03 | Wrong exposure | E09 | Insufficient information |
| E04 | Wrong outcome | E10 | Inaccessible full text |
| E05 | No empirical evidence | E11 | Wrong jurisdiction/context |
| E06 | Engineering only | E12 | Wrong study design |

**Databases searched, with disclosed gaps:** Scopus (18/18 planned batches,
full coverage) and Web of Science were the two Tier-1 databases fully
covered; HeinOnline, ProQuest (full account export), and ProQuest/
Sociological Abstracts were reached with real, disclosed limitations in
each; JSTOR contributed 50 records via a targeted search. **SSRN and
Westlaw/Lexis were never searched** — the search phase was closed by
researcher decision before either was reached. CanLII, Rechtspraak.nl, and
comparable legal-institutional repositories were not systematically
searched in this pass. This is a real, disclosed limitation on the
completeness of the evidence base, not an oversight.

### 3.4 Study selection

Records were deduplicated (34,594 raw records → 27,481 unique), then
screened at title/abstract by an AI first-pass reviewer against
`INCLUSION_EXCLUSION.md`, with a human `reviewer_2` pass over every
include/unsure record. **Disclosed methodological caveat:** the
reviewer_1/reviewer_2 agreement rate on this pass was unusually high for an
independent second-reviewer process, and the turnaround was fast relative
to the volume (3,665 records). This is flagged here, as it is throughout
the project's own records, because it bears on how much independent
verification this screening stage should be credited with in any
assessment of the review's rigor. Full-text screening follows the same
two-code structure (`full_text_decision` + standardized exclusion reason)
and is livein progress.

### 3.5 Data extraction

Each included study is extracted against a 92-field codebook
(`CODEBOOK.md`) covering identification, jurisdiction, population, the four
mechanism families and their sub-codes, the outcome hierarchy, statistical
information (effect measure, estimate, CI, p-value, model type), study
design and risk-of-bias tool, and a `mechanism_certainty` scale (0 =
inferred only, through 4 = experimental evidence) distinguishing "authors
argue X" from "the study directly demonstrated X." Every extracted
statistic carries source provenance (document, page, section, exact
location).

### 3.6 Risk of bias (not yet applied)

Design-matched tools are assigned per study — RoB 2 (randomized), ROBINS-I
(non-randomized intervention), JBI checklists (cross-sectional/cohort),
CASP (qualitative), MMAT (mixed methods), AMSTAR 2 (secondary systematic
reviews), and a supplementary, explicitly non-validated Legal Institutional
Evidence Appraisal Framework for legal-empirical studies without a
conventional design match. **No rating has been assigned to any study**:
this project's own rule is that none of these instruments may be
reconstructed from memory, so appraisal is deferred until the official,
current version of each tool is obtained and applied — a disclosed
limitation of this interim report, not an oversight.

### 3.7 Data synthesis (contingent, not yet run)

A single universal pooled meta-analysis is judged inappropriate a priori
(`PROJECT_SPEC.md` §3): the literature is expected to differ too much in
legal mechanism, institutional setting, population, service type, outcome,
study design, and effect measure for one pooled estimate to be
substantively meaningful. Instead, a quantitative-feasibility decision tree
(`ANALYSIS_PLAN.md` §2) is applied *per candidate synthesis family*
(Families A/B/C, §2 above), asking in sequence whether the exposure,
outcome, population, and comparator are sufficiently comparable, whether an
effect estimate is available or defensibly calculable, and whether enough
independent studies exist — routing each family to a restricted
meta-analysis, a structured quantitative synthesis (SWiM 2020), or neither.
**This decision tree has not yet been run against the current evidence
base.** Of the 85 studies extracted so far, 37 are judged to report a
genuine, study-generated, calculable effect estimate and are marked
eligible *at the individual-study level* for quantitative synthesis; all 85
are eligible for qualitative/narrative synthesis. This is a per-study
eligibility flag, not a determination that pooling is warranted for any
family — that determination is Phase 11, and it has not been made.

### 3.8 Registration and transparency

The protocol, codebook, and analysis plan referenced throughout this
document were fixed on 2026-08-22, before any database was searched, and
have not been revised since in response to what the search or screening
later produced. Formal registration (OSF Generalized Systematic Review) is
being submitted separately, with an explicit disclosure that the
registration *timestamp* postdates search execution even though the
protocol *content* predates it — see
`00_admin/preregistration/osf_preregistration_draft.md`. This repository's
full screening and extraction databases are additionally being prepared for
archival deposit (Zenodo) as an interim, versioned snapshot.

---

## 4. Search Results and Study Selection — Interim PRISMA Flow

**All figures below are provisional and will change as screening
continues.** Full detail: `06_outputs/prisma/prisma_flow.md`.

| Stage | n | Note |
|---|---:|---|
| Raw records identified (6 databases + pilot rounds) | 34,594 | |
| Duplicates removed | 7,113 | |
| Unique records after deduplication | 27,481 | 26,222 carry a real abstract |
| Advanced past title/abstract screening | 3,659 | final_decision=include, zero conflicts under the strict disagreement definition (see §3.4 caveat) |
| Full-text screening complete | 175 / 3,659 (≈4.8%) | 85 include, 90 exclude |
| Full-text exclusions by reason | | E02 (29), E01 (19), E04 (16), E05 (10), E06 (8), E07 (4), E08 (2), E03 (1), E09 (1) |
| Studies fully extracted | 85 / 85 current includes | No extraction gap; 3,484 records remain unreached at full text |

---

## 5. Preliminary Descriptive Characteristics of the 85 Extracted Studies

**Purely descriptive. No inference beyond this snapshot should be drawn** —
these 85 studies are ≈4.8% of the 3,659-record pool still to be screened,
and both the count and the composition will change, plausibly
substantially, as screening continues.

### 5.1 Geographic distribution

36 distinct countries/territories represented (plus 2 explicitly
global/multi-country synthesis studies); a study spanning multiple
countries is counted once per region it touches:

| Region | Studies touching this region |
|---|---:|
| Sub-Saharan Africa | 27 |
| South Asia | 21 |
| East Asia & Pacific | 12 |
| Latin America & Caribbean | 12 |
| North America | 11 |
| Middle East & North Africa | 4 |
| Global / multi-country synthesis | 2 |
| Europe & Central Asia | 1 |

The three jurisdictions of the parent doctoral comparison are represented
unevenly at this stage: Brazil (6 studies), Canada (1), Netherlands (0) —
a direct consequence of which full-text PDFs have been supplied and
screened so far, not a substantive finding about jurisdictional coverage.

### 5.2 Legal system

| Legal system | Studies |
|---|---:|
| Common law | 39 |
| Civil law | 23 |
| Mixed / plural (customary, religious, or multi-jurisdictional) | 21 |
| Not recorded (global/multi-country synthesis) | 2 |

### 5.3 Study design

| Design class | Studies |
|---|---:|
| Qualitative | 26 |
| Mixed methods | 22 |
| Doctrinal (legal-institutional) | 16 |
| Observational (quantitative, non-experimental) | 10 |
| Secondary systematic/focused review | 5 |
| Jurimetric (quantitative legal-institutional) | 3 |
| Experimental (randomized) | 2 |
| Quasi-experimental | 1 |

The evidence base assembled so far is dominated by qualitative and mixed-
methods work; only 3 of 85 studies (Gaikwad & Thomas 2026 ×1 experimental;
1 quasi-experimental) offer randomized or quasi-experimental identification
of a causal effect. This composition is itself informative for §3.7's
eventual feasibility determination, but is not that determination.

### 5.4 Mechanism family (from the four top-level booleans)

| Mechanism family | Studies |
|---|---:|
| Multiple families present | 64 |
| Discretion/Accommodation only | 9 |
| Enforcement only | 4 |
| Eligibility only | 4 |
| Burden only | 1 |
| Not yet classifiable (mechanism not directly assessed) | 3 |

Most extracted studies (64/85) implicate more than one mechanism family
simultaneously — an early indication, not yet tested, that the four
families may operate as an interacting bundle rather than as cleanly
separable exposures.

### 5.5 Outcome family

| Outcome family | Studies |
|---|---:|
| Effective access (quantity, reliability, continuity, quality) | 35 |
| Primary connection (formal connection/formalization) | 34 |
| Economic access (cost, affordability) | 11 |
| Administrative outcome (submission, approval, appeal, delay) | 5 |

### 5.6 Publication years

Extracted studies span **2021–2026**, reflecting the search's emphasis on
recent literature; no systematic attempt has yet been made to characterize
how representative this window is of the full field.

---

## 6. Current Status by PRISMA Phase

| Phase | Status |
|---|---|
| 1–5 (protocol through title/abstract screening) | Complete |
| 6 (full-text screening) | Live, 175/3,659 (≈4.8%) |
| 7 (pilot extraction) | Superseded — extraction proceeds directly on every include |
| 8 (full extraction) | Fully caught up with Phase 6; 85/85, no gap |
| 9 (risk of bias) | **Not started** — see §3.6 |
| 10 (evidence classification) | Populated for all 85 extracted studies |
| 11 (quantitative feasibility) | **Not started** — see §3.7 |
| 12–16 (meta-analysis, sensitivity, publication bias, PRISMA reporting) | Tooling/templates built; **not run against real data** |

---

## 7. Why This Report Stops Here

This project's governing methodological commitment
(`PROJECT_SPEC.md` §1) is: *first determine what the existing evidence
allows us to conclude, then decide what statistical synthesis, if any, is
justified* — not the reverse. `07_manuscript/draft/manuscript_outline.md`
correspondingly marks Results, Discussion, Comparative Findings, and
Conclusion as sections that "may not be drafted from assumption,
illustration, or the preliminary source papers alone," pending the
corresponding phase of work. That constraint is not a formality here: with
risk-of-bias appraisal unrun and only 4.8% of the full-text pool assessed,
any Results or Discussion section written today would necessarily be
either empty or an illustration dressed up as a finding — precisely the
outcome the project's anti-confirmation-bias rule exists to prevent. This
report therefore ends at the descriptive status the evidence currently
supports.

## 8. Limitations of This Interim Report Itself

- **Coverage is partial and search access was constrained.** SSRN and
  Westlaw/Lexis were never searched; CanLII and Rechtspraak.nl were not
  systematically searched for this literature (distinct from the separate
  judicial-decisions dataset in this repository, which must never be pooled
  with this review's evidence — `PROJECT_SPEC.md` §9).
- **The title/abstract reviewer_2 agreement rate was unusually high** for
  an independent second pass, and the turnaround was fast relative to
  volume; treat the "zero conflicts" figure with that in mind (§3.4).
- **Full-text screening is ≈4.8% complete.** Every descriptive statistic in
  §5 describes only the 85 studies screened so far, not the eventual
  evidence base.
- **No risk-of-bias rating exists for any extracted study.** Design/tool
  assignment is complete; appraisal is not.
- **No synthesis feasibility determination has been made.** The 37/85
  "quantitative-synthesis eligible" flag is a per-study data property, not
  a decision that pooling any family is warranted.
- **This document itself has not been peer reviewed** and is not a
  substitute for the eventual registered, completed systematic review.

---

## Appendix A — Studies Extracted So Far (n = 85, alphabetical by first author)

*Full citation, jurisdiction, and coding detail for every study below is in
`03_extraction/extracted_data/extraction_database.csv`. Listed here for
reference only; inclusion in this list reflects full-text screening and
extraction to date, not a final, closed evidence base.*

Abungu V, Dadashi Firouzjaei M, Terry LG, Elliott MA (2026) Water supply and infrastructure challenges in rural low-Income arid and semi-arid lands (ASALs): A case study of Turkana, Kenya. PLOS Water 5(3): e0000509

Agyeman NK, Tantoh HB, Kamika I (2026) Assessing water security and governance complexity in the Owabi river catchment in Ghana. Discover Sustainability 7:934

Ahmed F, Malik NI, Anjum R, Ahmad JB, Zia S, Al Sabbah H, Dincer H, Yüksel S (2026) Experiencing modular adaptive decentralized water security systems in southern Pakistan and implications for public health and nutrition: a qualitative exploratory study. Frontiers in Public Health 14:1780817

Altaf S, Goetzke F (2025) Community-led water utility governance and corruption: the case of Faisalabad, Pakistan. Ecology and Society 30(2):18

Annala Tesfaye L, Sarin A, Tesfaye Y (2025) Ownership, hegemony, and resistance in Ethiopia's rural drinking water governance. Ecology and Society 30(4):19

Armstrong A, Hope R, Koehler J (2022). Piped water revenue and investment strategies in rural Africa. Environmental Research: Infrastructure and Sustainability 2, 035003.

Basnet GB, Sherchan S (2026) Urban Water Insecurity and Public Health in Kathmandu Valley, Nepal: A Systematic Review of Contamination Sources, Health Risks, and Governance Gaps. Water 18(12):1514

Caldera Ortega AR, Tagle Zamora D (2023). Balance on social inclusion and environmental justice at the end of the 30 years of the drinking water service concession in the city of Aguascalientes, Mexico. Frontiers in Sustainable Cities 5:1177179.

Carrard N, Gonzalez D, MacArthur J, Nguyen Anh Minh, Nguyen Dinh Giang Nam, Rodgers D, Foster T (2026) Groundwater-based water services as complex socio-hydrogeological systems: insights from Vietnam's Mekong Delta. Hydrogeology Journal 34:1927–1942

Carvalho JIC, Jesus Júnior G, Gomes RL (2022). Análise da universalização, investimento e governança do serviço de esgoto sanitário de sedes municipais das Bacias Hidrográficas do Leste (BHL) na Bahia. Revista de Direito Econômico e Socioambiental 13(1), 122-152.

Cesari G, Johnson SO, Cancelliere G, Von Medeazza G (2022). How a water trucking governance mechanism in the West Bank enhances equity and sustainability. Waterlines 41(1), 24-34.

Chumo I, Mberu B, Wainaina C, Murigi W, Sumba L, Kabaria C (2023). Sanitation services for the urban poor: A social capital approach to sanitation challenges in informal settlements. PLOS Water 2(12): e0000086.

Cruxen IA (2022). The limits of insulation: the long-term political dynamics of public-private service delivery. International Development Planning Review 44(3), 317-338.

Cáceres V, Tobías M, Koutsovitis ME (2025) Infraestructuras hídricas y modelos descentralizados de gestión de agua y saneamiento. El caso de los servicios "desvinculados" en el Área Metropolitana de Buenos Aires, Argentina. Territorios 53-Especial, Bogotá, pp. 1-25

Dasgupta S, Agarwal N (2022). Experimenting with Urban-Rural Partnerships for Sustainable Sanitation in India: Learning from Practice. Land 11(7), 1021.

dos Santos Alves Romanato L, da Silva NF, Lucena SV, Beser de Deus LA (2025) Managing Water Supply Infrastructure in Medium-Sized Cities to Meet User Demands: A Case Study of Natal, Brazil. World Water Policy

Dovie DBK, Obuah GA, Miyittah M, Christian AK (2026) Settlement morphology, demographics, and governance challenges of water, sanitation, and hygiene in low-income urban communities in Ghana. Discover Environment 4:371

Dugard J (2021). Water Rights in a Time of Fragility: An Exploration of Contestation and Discourse around Cape Town's 'Day Zero' Water Crisis. Water 13(22), 3247.

Endarti EW (2024). Evaluation of Open Defecation Free Program Policy in Tambak Osowilangun Village Surabaya City. Daengku: Journal of Humanities and Social Sciences Innovation 4(4): 694-705.

Espinoza V, Viers JH (2024). The paradox of production: Surface water supply drives agricultural productivity but not prosperity in California's San Joaquin Valley. PLOS Water 3(6): e0000192.

Ezeudu OB, Ezeudu TS, Ugochukwu UC, Okolo OJ, Ani CD, Ajogu AP, Ajaero CC, Mbakwe UI, Nduji NN (2022). Coping Strategies, Cultural Practices and Policy Implications on Domestic Water Supply in an Erosion Susceptible Rural Community, Nigeria. Resources 11(8), 77.

Fanaian S, Fanaian F (2023). A tug of war between centralization and decentralization: the co-evolution of urban governance and water risks in Guwahati, India. Environmental Research Communications 5:065012.

Fanaian S, Manero A, Nguyen N-M, Grafton RQ (2025) Beyond a Decade of Water Justice: Review, Directions, and Pathways to Achieve "Water for All". WIREs Water

Faulmino CJP, Rola AC (2023). Arsenic in Philippine Groundwaters: Exploring Governance Limitations for Drinking Water Safety. Journal of Environmental Science and Management Special Issue 1-2023:14-27.

Filčák R, Škobla D (2021). Sanitation Infrastructure at the Systemic Edge: Segregated Roma Settlements and Multiple Health Risks in Slovakia. International Journal of Environmental Research and Public Health 18(11), 6079.

Fordjour G, Anbazu J, Antwi NS, Adam MU, Asibey MO (2024). Self-help and spontaneous heroism in urban service delivery in Ghana's informal neighbourhoods: a case study of Moshie Zongo. Local Environment 29(10): 1384-1401.

Fracalanza AP, da Paz MGA, Alves EM (2023). Water and sanitation in Brazil: conflicts, appropriation, and climate injustice. Desenvolvimento e Meio Ambiente 62 (special section: Water, Sanitation and SDGs in Brazil), p.904-918.

Gaikwad N, Thomas A (2026). Getting on the grid: A field experiment on bottom-up political pressure and access to essential public services. American Journal of Political Science, early view.

Gallandat K, Hutchins C, Malembaka EB, Jeandron A, Saidi JM, Rumedeka BB, Muhemeri JB, Bompangue D, Sewa G, Seon A, Durand P-Y, Machuel D, Cumming O (2024). Process evaluation of an urban piped water supply infrastructure improvement programme in Uvira, Democratic Republic of the Congo. PLOS Water 3(10): e0000185.

Hujaleh A, Larimian T, Goodall S, Kayaga S (2026). Experiences of accessing water services in water scarce displacement settings: A case study of internally displaced people and host communities in Hargeisa, Somaliland. PLOS Water 5(5): e0000544.

Humňalová H, Ficek F (2023). Sanitation strategies for reducing open defecation in rural areas of India and Ethiopia. AUC Geographica 58(1), 51-63.

Hussain N, Chaves C (2023). Perspectives from the Ground: Governing Informality of Water in Metro Manila. Water Alternatives 16(2), 683-704.

Huston A, Gaskin S, Moriarty P, Watsisi M (2021). More Sustainable Systems Through Consolidation? The Changing Landscape of Rural Drinking Water Service Delivery in Uganda. Water Alternatives 14(1), 248-270.

Ilangovan K, Sankar JG, Srinivasan M (2026) Systematic review of rural drinking water interventions under Jal Jeevan mission. Discover Environment 4:189

Khan HF, Arshad SA (2022). Beyond water scarcity: Water (in)security and social justice in Karachi. Journal of Hydrology: Regional Studies 42, 101140.

Koros JK, Juuti PS, Juuti RP, Asokan SM (2026) Exploring Kenya's Small-Scale Water Services for a More Sustainable Future. Public Works Management & Policy

Koros JK, Juuti PS, Juuti RP, Mutie J (2026) Accelerating Safe Water and Sanitation Access in Urban Periphery and Low-Income Areas: The Case of Kenya. Public Works Management & Policy 31(2):172-199

Kosoe EA, Osumanu IK, Ogwu MC (2025) Reimagining Rural and Small-Town Water Supply in Ghana Through Inclusive Governance and Sustainable Models. Journal of Sustainability 1(2)

Kozole T, Ross M, Nicoletti C, Rogla J, Ives N, Ali A, Prom R (2023). Impact of targeted subsidies on access to resilient sanitation for climate-vulnerable households in rural Cambodia. Journal of Water, Sanitation and Hygiene for Development 13(12):931.

Lindt K (2026) Community-based to centralized provision: the transformation of aflaj beyond Oman's national drinking water strategy. International Journal of Water Resources Development 42(4):476-496

Loewenson R, Mhlanga G, Gotto D, Chayikosa S, Goma F, Walyaro C (2023). Equity dimensions in initiatives promoting urban health and wellbeing in east and southern Africa. Frontiers in Public Health 11:1113550.

Lubeck-Schricker M, Patil-Deshmukh A, Murthy SL, Chaubey MD, Boomkar B, Shaikh N, Shitole T, Eliasziw M, Subbaraman R (2023). Divided infrastructure: legal exclusion and water inequality in an urban slum in Mumbai, India. Environment & Urbanization 35(1):178-198.

Luis N, Raffa C (2022). La accion de Obras Sanitarias de la Nacion en Mendoza: infraestructura y saneamiento entre acuerdos y conflictos (1918-1928). Historia Regional 35(47), 1-16.

Mallory A, Mdee A, Agol D, Hyde-Smith L, Kiogora D, Riungu J, Parker A (2022). The potential for scaling up container-based sanitation in informal settlements in Kenya. Journal of International Development 34(7), 1347-1361.

Mantey EP, Kanwar RS, Appiah-Effah E (2024). Assessment of Water Service Levels and User Satisfaction for Domestic Water Use in Emina-Boadi-Kumasi to Achieve the Sustainable Development of Urban Water Supply Systems in Ghana. Water 16(22): 3193.

Maskey G, Pandey CL, Giri M (2023). Water scarcity and excess: water insecurity in cities of Nepal. Water Supply 23(4):1544-1558.

Mau MLB, Sriyana S, Purnaweni H, Lituhayu D (2024) The importance of institutional capacity in drinking water supply system governance: A policy evaluation from border area. Edelweiss Applied Science and Technology 8(4):1448-1461

Mgala E, Nobert J, Mabhuye EB, Gwambene B (2025) Enhancing access to underutilized ground water potential for improving livelihoods and conflict reduction in Kagera Sub-Basin, Tanzania. Frontiers in Water 7:1572231

Mian HR, Avila J, De Coste M, Saleem S, Mohseni M, Hewage K, Sadiq R (2026) Assessing the water infrastructure in Small and Rural Indigenous (SRI) communities: a risk assessment framework. Journal of Water and Health 24(5):673

Moretto L, Faldi G, Rosati FN, Teller J (2023). Coproduced urban water services: When technical and governance hybridisation go hand in hand. Frontiers in Sustainable Cities 4:969755.

Muller M (2023). Water and welfare: Free basic water revisited. Development Southern Africa 40(6):1365-1379.

Muoghalu C, Semiyaga S, Manga M (2023). Faecal sludge emptying in Sub-Saharan Africa, South and Southeast Asia: A systematic review of emptying technology choices, challenges, and improvement initiatives. Frontiers in Environmental Science 11:1097716.

Murthy SL (2024). Disrupting Utility Law for Water Justice. Stanford Law Review, Vol. 76 (forthcoming). SSRN 4385404.

Muyukani WP, Muthama NJ, Mutune MJ (2023). Integration and implementation of rainwater harvesting technologies in development programs, planning and budgeting in Matungulu Sub-County, Machakos County, Kenya. East African Journal of Science, Technology and Innovation 4(Special Issue).

Narzetti DA, Marques RC (2022). Policies and incentives for developing universal access to water and sanitation for vulnerable families. Water Policy 24(3), 485-497.

Nassar N, Al Zabadi H, Chabaane Z (2026) Environmental stress, water inequality, and environmental justice in Palestinian urban areas: a GIS-based assessment of sanitation and infrastructure disparities in the southern West Bank. Environmental Health 25:39

Nicolas-Artero C, Blanco G, Bopp C, Carrasco N (2022). Modes of access to water for domestic use in rural Chile: a typological proposal. Water Policy 24(7), 1179-1196.

Nijhawan A, Howard G, Poudel M, Pregnolato M, Lo YTE, Ghimire A, Baidya M, Geremew A, Flint A, Mulugeta Y (2022). Assessing the Climate Resilience of Community-Managed Water Supplies in Ethiopia and Nepal. Water 14(8), 1293.

Nishu NA, Roy T, Razu SR, Akter S (2025) Barriers to Accessing Water, Sanitation, and Hygiene Services for Persons With Disabilities in the Southwestern Region of Bangladesh. SAGE Open (July-September 2025)

Nurmaningtyas AR, Hamzah B, Aprianti E (2026) Characteristics of Settlement on Water in Tobati Village, Papua: Challenges and Sustainability Strategies. Journal of Design and Built Environment 26(1)

Obayomi A, Popoola A, Medayese S, Wahab B (2023). Examining liveability in the informal community of Kabawa, Nigeria. Town and Regional Planning, no. 82, pp.18-33.

Okolie AM, Nnamani KE, Nwangwu C, Agbo HN, Ike CC (2023). Public procurement law, political economy of the lowest responsive bidding, and the development of the water, sanitation and hygiene sector in Nigeria. Review of African Political Economy 49(174), 550-568.

Paran RC, Ocampo COV, Aparente MEA, Calibo-Senit DI, Ybañez AP (2026) Water Security System Assessment in a Philippine Rural Area. Environment and Ecology Research 14(1):61-70

Pastrana-Miranda T, Gonzalez-Caamal MM (2022). Injusticia ambiental y marginacion: la falta de acceso al agua en la Zona Metropolitana del Valle de Mexico. Territorios (46), 1-25.

Patterson LA, Bryson SA, Doyle MW (2023). Affordability of household water services across the United States. PLOS Water 2(5): e0000123.

Phinney S (2023). The policing of Black debt: how the municipal bond market regulates the right to water. Urban Geography 44(8):1584-1607.

Rajput R, Pu J (2025) A political industrial ecology of water in Bodh Gaya, India: Pre- and Post-the World Heritage designation. Journal of Industrial Ecology

Saidani MA, Aslekar U, Kuper M, Kemerink-Seyoum J (2023). Sharing Difficult Waters: Community-Based Groundwater Recharge and Use in Algeria and India. Water Alternatives 16(1):108-133.

Saikia BB, Dutta M, Dutta SB (2026) Pots to Pipelines: Ethnographic Narratives of Women's Engagements With Water in Jorhat District of Assam. World Water Policy 12:e70092

Saker A, Bernal Pedraza A, Narayan AS (2022). Regulating Citywide Inclusive Sanitation (CWIS) in Colombia. International Journal of Environmental Research and Public Health 19(9), 5669.

Salauddin M, Piracha A (2026) Issues of Bounded Geographies and Participatory Governance in Accessing Water in Informal Settlements: A Case of Khulna City, Bangladesh. World Water Policy

Saldaña Almazán M, Leyva Zuñiga AP, Moreno Mendoza E, Calderón Arellanes MP, Suastegui Cruz S (2025) Community Management and Sustainability of Water Supply in a Rural Area of Guerrero, Mexico. Sustainability 17(10):4633

Savelli LB, Koonce D, Viera KE, Thapa S, Woods CG (2026) 'Bad water just means bad health': identifying barriers and promoters of safe drinking water in rural Eastern North Carolina. Environmental Research: Health 4:025001

Shah R (2022). Laying Bare: Determinants of Informal Water Vendors for Domestic Water Supply in Himalayan Mountain Towns. HIMALAYA 41(1), 74-90.

Sharma M, Sharma B, Kumar N, Kumar A (2025) A framework to assess urban water resilience in developing countries like India: Looking beyond water utilities and networked cities. Water Policy 27(1):88

Souza A, Souza MAA, Diniz FR (2024) Reconfigurations in The Ownership And Control Of Sanitation services: Is Brazil going against a global trend? Revista Brasileira de Geografia Física 17(5):3603-3619

Thapa D, Farid MN, Prevost C (2022). Governance drivers of rural water sustainability: Collaboration in frontline service delivery. Journal of Infrastructure, Policy and Development 6(1), 1380.

Torres-Sandoval AJ, Tavera-Cortés ME, Acevedo-Ortiz MA, Ortiz-Hernández YD (2025) Transparency, Governance, and Public Service Management: Challenges of Citizen Participation in Ecatepec de Morelos. Administrative Sciences 15(4):144

Vidhyadharan A (2023). Disparities in Drinking Water and Sanitation in the Urban Slums of Kerala, India. Sustainability 15(9):7559.

Wang RY (2026) (Re)producing uneven waterscapes in South China: the materiality and spatiality of the Dongshen inter-basin water supply project. Asia Pacific Viewpoint

Webb WA, Wells EC, Prouty C, Zarger R, Trotz M (2024) Ethics and ambiguity in wastewater development on the Placencia Peninsula, Belize. Annals of Anthropological Practice

Win CZ, Jawjit W, Thongdara R, Gheewala SH, Prapaspongsa T (2024) Towards more sustainable Water, Sanitation and Hygiene (WASH) projects in Magway Region, Myanmar. Environment, Development and Sustainability 26:22149-22173

Wutich A, Jepson W, Velasco C, Roque A, Gu Z, Hanemann M, Hossain MJ, Landes L, Larson R, Li WW, Morales-Pate O, Patwoary N, Porter S, Tsai Y-S, Zheng M, Westerhoff P (2022). Water insecurity in the Global North: A review of experiences in U.S. colonias communities along the Mexico border. WIREs Water 9(4), e1595.

Yap C, Mcfarlane C, Ndezi T, Makoba FD (2023). Sanitation challenges in Dar es Salaam: the potential of Simplified Sewerage Systems. Environment & Urbanization 35(1).

Yasmin S, Ghafran C (2026) Accountability to "the other": conceptualising NGO accountability through differentiated governmentality. Accounting, Auditing & Accountability Journal 39(1):101-130

---

*Prepared with AI assistance (Claude, Anthropic) for search, screening,
extraction, and drafting under direct researcher supervision and
instruction throughout — see `CHANGELOG.md` for the complete, dated
methodological log of every decision reflected in this document.*
