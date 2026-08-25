# Title-Only Triage Memo (Non-Binding)

Status: **not a screening decision.** This memo is a title/URL-only read of
the 37 candidate records currently in
`02_screening/title_abstract/screening_database.csv`, produced because this
environment cannot fetch full text or even an abstract for any of them
(network egress is blocked — `SEARCH_PROTOCOL.md` §7). It exists purely to
give a human reviewer a head start; it does **not** populate the
`title_abstract_decision` field in the screening database, which remains
blank for all 31 records and must be filled in by an actual title/abstract
review per `PROTOCOL.md` §6 and `INCLUSION_EXCLUSION.md`.

A title alone cannot establish exposure, outcome, population, or empirical
content with any confidence — several judgments below will be wrong once
the abstract is actually read. Treat every "LIKELY INCLUDE" as no more than
"worth reading the abstract" and every "LIKELY EXCLUDE (tentative)" as no
more than "check this isn't being excluded by mistake."

## Triage categories

- **LIKELY INCLUDE** — title plausibly satisfies all of INCLUSION_EXCLUSION.md's
  criteria 1–4; recommend prioritizing for abstract review.
- **UNCERTAIN** — title is ambiguous on empirical content, mechanism, or
  outcome fit; needs the abstract to decide either way.
- **LIKELY EXCLUDE (tentative)** — title suggests a specific exclusion code;
  flagged with that code, but not applied to the record.

## Triage table

| record_id | Title (short) | Triage | Tentative code | Rationale |
|---|---|---|---|---|
| R0001 | Barriers to sewer connection, urban Dhaka | LIKELY INCLUDE | — | Administrative + organisational barriers to sewer connection is squarely on-topic |
| R0002 | Water governance and well-being, multi-site | UNCERTAIN | — | "Well-being" outcome isn't in the outcome hierarchy (`PROJECT_SPEC.md` §7); needs abstract to confirm a legal/administrative mechanism and a mapped outcome |
| R0003 | Water/sanitation access, informal vendors, Brazil | LIKELY INCLUDE | — | Rights/responsibilities framing, Brazil, informal population |
| R0004 | Tenure and water insecurity, Nairobi slums | LIKELY INCLUDE | — | Direct tenure-and-access study, Family A analog |
| R0005 | Land tenure and informal-settlement upgrading, Colombo | LIKELY INCLUDE | — | Tenure + infrastructure outcome |
| R0006 | Matrix of Land Tenure Property Right for Water Settlement Area | UNCERTAIN | E10 (possible) | Hosted only on academia.edu; publication venue and peer-review status unclear — verify before treating as a citable study |
| R0007 | Communities of water practice, Agra | UNCERTAIN | — | "Communities of practice" framing may be more anthropological than legal/administrative; check for an eligibility/burden/discretion/enforcement mechanism |
| R0008 | Socio-economic inequalities in drinking water access, South Africa informal settlements | UNCERTAIN | — | Inequality framing plausible, but title doesn't name a legal/administrative mechanism explicitly |
| R0009 | Transitional infrastructures, Nairobi, cross-sectional | UNCERTAIN | E06 (possible) | May be infrastructure/engineering-forward rather than governance-forward; check |
| R0010 | Typology of land rights in informal settlements, infrastructure retrofit | LIKELY INCLUDE | — | Land-rights typology directly engages the tenure/eligibility mechanism |
| R0011 | Saneamento básico em áreas irregulares (industry report) | LIKELY INCLUDE (grey lit) | — | On-topic; code `peer_reviewed=false` if included |
| R0012 | REURB/saneamento, Sapucaia, Pará | LIKELY INCLUDE | — | Regularização fundiária + saneamento, peer-reviewed venue |
| R0013 | Regularização fundiária e saneamento (industry blog) | UNCERTAIN | E05 (possible) | Blog/industry-explainer register; verify it reports empirical evidence rather than commentary |
| R0014 | Saneamento adequado, Defensoria Pública RJ report | LIKELY INCLUDE (grey lit) | — | Public defender's office report, likely documents real access barriers; code `peer_reviewed=false` |
| R0015 | Saneamento em áreas irregulares, Insper programme page | UNCERTAIN | E05 (possible) | Looks like a course/programme description rather than a study — verify |
| R0016 | Ocupação Bela Vista, Passo Fundo (conference paper) | LIKELY INCLUDE (grey lit) | — | Conference paper on an irregular occupation case, on-topic |
| R0017 | National Assessment of First Nations Water/Wastewater Systems, Ontario roll-up | UNCERTAIN | — | Administrative data report rather than a study with an explicit exposure/outcome design — useful as a data source, questionable as a "study" per `INCLUSION_EXCLUSION.md` criterion 7 |
| R0018 | Proximate causes of unsafe drinking water, Ontario First Nations vs. non-First Nations | LIKELY INCLUDE | — | Direct comparative empirical study |
| R0019 | Improving First Nations water security through governance (Alcantara 2020) | LIKELY INCLUDE | — | Public-administration journal, governance mechanism, strong disciplinary fit |
| R0020 | Water insecurity in Ontario First Nations, exploratory study | LIKELY INCLUDE | — | Governance-focused exploratory study |
| R0021 | No Taps, No Toilets: constitutional right to water, Canada (McGill Law Journal) | UNCERTAIN | E01/E05 (possible) | Law journal article — may be doctrinal commentary rather than empirical; check specifically for this before including |
| R0022 | Water-sharing arrangements, First Nations/Ontario municipalities | LIKELY INCLUDE | — | Institutional-arrangement study, governance mechanism |
| R0023 | Costs of urban utility water connections, global research program | LIKELY INCLUDE | — | Quantitative, cross-country, connection-cost barrier — strong Family B/C candidate |
| R0024 | Metrics in water/wastewater affordability programs, US (Pacific Institute) | UNCERTAIN | — | Affordability-metrics framing; check for an explicit eligibility/documentation mechanism vs. pure economics |
| R0025 | Low-income water customer assistance program assessment (NACWA) | LIKELY INCLUDE (grey lit) | — | Assistance-program eligibility/documentation is squarely on-topic |
| R0026 | Legal status and deprivation in urban slums over two decades | LIKELY INCLUDE | — | Directly on-topic, likely a precursor/companion to the Lubeck-Schricker et al. exemplar |
| R0027 | Review of drivers/barriers of water and sanitation policy, informal settlements (LMICs) | LIKELY INCLUDE | — | This is itself a review — classify as `study_design_class = systematic_review_secondary` and appraise with AMSTAR 2 if included (`RISK_OF_BIAS.md` §1), never as an independent primary effect |
| R0028 | Informal mechanisms to regularize settlements, São Paulo favelas water services | LIKELY INCLUDE | — | Brazil, regularization + water services, strong fit |
| R0029 | Turning Off the Tap: water service delivery and global administrative law (EJIL) | LIKELY INCLUDE | — | Administrative-law framing with reported comparative fieldwork (6 countries per the search snippet) |
| R0030 | Lien In: municipalities' discriminatory water practices (Harvard CRCL) | UNCERTAIN | E01/E05 (possible) | Law journal article — check for empirical/case content vs. pure legal argument |
| R0031 | Turning Participation Into Power: a water justice case study (George Mason Law Review) | UNCERTAIN | E01/E05 (possible) | "Case study" suggests possible empirical content, but law-review venue raises the same doctrinal-vs-empirical question as R0021/R0030 |
| R0032 | Bureaucratic Hurdles, Political Resistance, and Public Service Access (working paper) | LIKELY INCLUDE, flag duplicate | E08 (possible, pending verification) | Appears to be an earlier version of the Gaikwad & Thomas 2026 exemplar (R0036) — verify at full-text stage per `REPRODUCIBILITY.md` §6 before extracting both as independent studies |
| R0033 | Pesquisa Saneamento Básico em Áreas Irregulares — full report | LIKELY INCLUDE | — | Full underlying report behind R0011 (press-release summary of the same study) — prefer this record for extraction, treat R0011 as a companion source |
| R0034 | Desafios do saneamento em SP e alternativas à privatização | UNCERTAIN | — | Governance/privatization framing plausible but title doesn't clearly name a household-level access outcome or a specific legal/administrative mechanism; check |
| R0035 | Divided infrastructure: legal exclusion and water inequality, Mumbai (Lubeck-Schricker et al. 2023) | LIKELY INCLUDE | — | Verified exemplar (`SOURCES.md`); strong Family A candidate — genuinely needs the same screening as every other record, not an informal pre-approval |
| R0036 | Getting on the grid (Gaikwad & Thomas 2026) | LIKELY INCLUDE | — | Verified exemplar; strong Family B candidate; note likely duplicate-publication link to R0032 |
| R0037 | A Meta-Analysis of Water Institutions and Their Performance (Apio, Thiam & Dinar 2025) | LIKELY INCLUDE, flag as secondary synthesis | — | Verified exemplar; this is itself a meta-analysis — classify `study_design_class = systematic_review_secondary` and appraise with AMSTAR 2 if included, same treatment as R0027 |

## Summary

- LIKELY INCLUDE: 23 (2 of which carry a duplicate-publication flag, 1 a secondary-synthesis flag)
- UNCERTAIN: 14
- (No record was confident enough to tentatively exclude outright from a
  title alone — that determination is deliberately left to the actual
  screener; several "UNCERTAIN" rows carry a plausible exclusion code as a
  flag, not a decision.)

## Recurring pattern worth flagging to the reviewer

Several UNCERTAIN records are law-review/law-journal articles (R0021,
R0030, R0031). Law reviews routinely publish both empirical legal
scholarship and pure doctrinal argument under similar-sounding titles —
this is exactly the distinction `INCLUSION_EXCLUSION.md` exclusion 1 exists
to make, and it is not resolvable from a title. These three should be
prioritized for full-text (not just abstract) review specifically on that
question.
