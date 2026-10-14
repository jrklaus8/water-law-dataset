# OSF Generalized Systematic Review Registration — Transparent Retrospective / Post-Execution Protocol Registration

**Frozen at Release `0.2.0-interim` (2026-10-14).** Snapshot: the git commit tagged `v0.2.0-interim` of
`github.com/jrklaus8/water-law-dataset` (branch `claude/legal-last-mile-review-spec-8ri0zs`). The tag marks the commit that carries this file, which is the **complete state after open items A13, A14 and A8 were closed**; record its full hash (`git rev-parse 'v0.2.0-interim^{commit}'`) on the OSF form. The tag is pushed by the researcher from a local clone. An earlier local tag on `a23f63e`, made before those three items were closed, is superseded and was never pushed.

Status: **ready for upload; not yet submitted.** The AI that prepared this file has no OSF account access, so the
submission itself can only be done by the researcher. Every section maps to a section of `PROTOCOL.md`; where the two differ,
`PROTOCOL.md` and the dated notes in the files it points to are the source of truth. Per `PROTOCOL.md` §11, PROSPERO was
considered and ruled out (it is scoped to health-outcome reviews and does not accept registration once extraction has begun;
extraction began 2026-09-12). OSF is the registry used.

**What kind of registration this is.** The review was planned in writing on 2026-08-22 and then *executed* (search, screening,
extraction, appraisal, synthesis) before anything was registered. This registration therefore does **not** carry the evidentiary
weight of a registration whose timestamp precedes data collection. What it does is (1) freeze, with a verifiable timestamp, the
state of the protocol and the evidence base at release `0.2.0-interim`; (2) separate what was fixed before any database was searched
from what was clarified, decided or departed from afterwards, each with its date and where it is logged; and (3) bind the
manuscript to those disclosures. It is labelled retrospective on purpose, and the OSF form should say so in its first line.

---

## 1. Two dates, stated together

- **Protocol fixed:** 2026-08-22 (git commit `d591062`, "Scaffold Legal Last Mile systematic review project"; `CHANGELOG.md`
  "2026-08-22 — Initial scaffold"). The first real database data (Scopus) arrived on 2026-08-26.
- **Registered:** [fill in the actual OSF submission date]. State both dates in the OSF entry.

## 2. Specified a priori (2026-08-22, before any database was searched)

Recoverable from the first commit; the files have since changed only in the ways listed in §3.

| Element | Where it is fixed |
|---|---|
| Research questions (primary: how legal and administrative institutions shape the translation of physical availability into effective household access; secondary: magnitude where comparable evidence exists) | `PROTOCOL.md` §2, `PROJECT_SPEC.md` |
| PECO, outcome hierarchy | `PROTOCOL.md` §3 and §7, `PROJECT_SPEC.md` §5–7 |
| Eligibility: inclusion criteria 1–10 (criterion 2: a legal, administrative, institutional, regulatory or governance factor; criterion 3: empirical evidence or a systematic empirical synthesis; criterion 4: an access-relevant outcome), exclusion criteria 1–11 and the codes E01–E12 | `INCLUSION_EXCLUSION.md` |
| Information sources and search strings (Tier 1/2 academic databases, legal/institutional repositories, grey literature) | `SEARCH_PROTOCOL.md`, `01_search/database_strategies/` |
| Selection process: two reviewers where feasible, conflicts to discussion or a third reviewer, a coded reason for every exclusion | `PROTOCOL.md` §6 |
| Data collection: a 92-field codebook piloted on about ten studies | `CODEBOOK.md`, `03_extraction/extraction_form/` |
| Risk of bias: design-matched tools (RoB 2, ROBINS-I, JBI, CASP, MMAT) plus a supplementary, explicitly non-validated Legal Institutional Evidence Appraisal Framework | `RISK_OF_BIAS.md`, `PROTOCOL.md` §8 |
| Synthesis: a quantitative-feasibility decision tree applied per candidate family, SWiM reporting where meta-analysis is not justified, candidate families A, B and C, sensitivity analyses, publication-bias assessment only with about ten studies or more | `ANALYSIS_PLAN.md`, `PROJECT_SPEC.md` §8 |
| **Binding commitment:** no title, abstract or manuscript section asserts or implies a pooled meta-analytic finding unless the decision tree was satisfied for that evidence family | `ANALYSIS_PLAN.md` §2, `PROJECT_SPEC.md` §3 |
| No directional hypothesis: an evidence test of the Legal Last Mile framework, not a confirmatory study | `PROJECT_SPEC.md` §2 and §11 |

## 3. Decided, clarified or departed from after execution began (dated, logged in `CHANGELOG.md`)

Wording of the criteria and of the research question was **not** rewritten; the clarifications below were added as dated notes
next to the original text, which was kept as written (`PROTOCOL.md` §12).

| Date | What | Kind | Effect |
|---|---|---|---|
| 2026-09-11 | **Search phase closed by the researcher.** Searched: Scopus (18 of 18 planned batches), Web of Science, HeinOnline (only a handful of records reached the pipeline), ProQuest, ProQuest/Sociological Abstracts, JSTOR (356 identified, 50 exported, none reached the pipeline). **Never searched: SSRN and Westlaw/Lexis.** The AI had no database access; the researcher searched through institutional access | Execution decision / departure (a gap) | 34,594 raw records, 27,481 after deduplication. The gap must be reported in the manuscript (`SEARCH_PROTOCOL.md` §7) |
| 2026-09-12 | Title/abstract screening complete: an AI first pass on every record; a human second reviewer on the include-plus-unsure records only, not on the AI's exclusions | Departure from "two reviewers where feasible" | 3,659 records advanced to full text |
| 2026-09-28 | **Full-text retrieval (Phase 6) closed by the researcher** once institutional access to further providers was exhausted | Execution decision / departure (a gap) | 2,277 of 3,659 records assessed; **1,382 never assessed** (1,200 not retrievable, 182 wrong file) |
| 2026-09-28 | Official RoB 2, ROBINS-I, JBI, CASP, MMAT and AMSTAR 2 documents supplied; **appraisal done as rule-based batch ratings from the extracted fields, not as a signalling-question read of each paper**; the project's own framework is non-validated | Departure in depth of method | Ratings describe the extraction as much as the paper |
| 2026-09-28 | Title amended to "AI-Assisted Systematic Review…" (not the question, criteria or synthesis approach) | Amendment (title) | `PROTOCOL.md` §12, `AI_USE_STATEMENT.md` |
| 2026-09-28 | Phase 11 applied the decision tree: **no family clears the bar for meta-analysis**; all three route to SWiM; Phase 12 (meta-analysis) not run. A methods note found no defensible common metric for the ownership/price cluster | Pre-specified branch taken | Nothing pooled; no pooled claim made |
| 2026-10-04 to 2026-10-14 | Blind second-model re-screen (two other AI models) of 121 AI excludes found about half of a stratified sample read as `include` (adjudication A16). Not a human check | Added check (AI versus AI) | Led to the scope question below |
| 2026-10-13 | **Criterion 2 read narrowly (A16 ruling by the PI):** a legal or administrative access rule or mechanism (eligibility screening, administrative burden, documentation or tenure rules, tariff or cost-recovery rules, discretion or accommodation, enforcement, utility ownership or regulatory structure) rather than project delivery, behavioural promotion or unanalysed macro-governance background. Applied to **both** includes and excludes. **This was decided after seeing the independent-model disagreement**, so it is a post-hoc interpretive clarification | Post-hoc clarification (`INCLUSION_EXCLUSION.md` note; wording unchanged) | A16, A22, A24 and A25 passes: 3 excludes reversed to includes and 83 includes reversed to excludes (E03 wrong exposure and E05 no empirical evidence mostly), two never-assessed records added as includes |
| 2026-10-13/14 | **Consistency rulings under criteria 3 and 4 (A24, A25, A20 residue):** E05 for narrative or doctrinal papers with no primary access data and no systematic method; E04 where the outcome is not a household access outcome (for example policy adoption); E03 where no rule is tested | Post-hoc application of the original criteria | See `CHANGELOG.md` 2026-10-13/14 |
| 2026-10-14 | **Results never decide eligibility** (A18): significance, magnitude or direction of an effect estimate is never an eligibility ground | Post-hoc clarification | One exclusion re-coded, one reversed |
| 2026-10-14 | Families A, B, C retitled as **thematic mechanism groupings** for vote counting, not homogeneous exposure–outcome pairs (A21); codes and assignments unchanged | Clarification (`PROJECT_SPEC.md` §8 note) | Headings only |
| 2026-10-14 | Controlled vocabularies adopted for `mechanism_family`, `outcome_family` and `study_design_class` (nine design values plus `other`); originals preserved | Post-hoc classification, keyword-based and unvalidated | Descriptive tables only |
| 2026-10-14 | Linked companion reports kept as separate rows (A3); the SWiM sensitivity analysis made a standing requirement (A4) | Counting convention; added requirement | 1,078 reports = 1,076 distinct studies |
| 2026-10-14 | **A26 rulings** (outcome and scope): S358, S590 and S606 moved from Families A and C to the reasoned non-fits (outcomes are aquifer decline, a city's decision to build waterworks, and back-end treatment capacity, not household access); S1121 (building permits) and S1143 (garbage collection) excluded E04 and E07; S1038's exposure and comparator corrected to its reported contrast; each family-assigned study coded for the raw sign of its estimate and its substantive direction | Post-hoc rulings after a scope check of the effect rows | Family A 18 to 16, Family C 20 to 17; included reports 1,080 to 1,078 |
| 2026-10-14 | **A29**: S1140 (Family B) and S1136 (Family C) moved to the reasoned non-fits because their outcomes are not household water or sanitation access outcomes (criterion 4); the sensitivity scenario that dropped them is retired | Post-hoc ruling after the A26 scope check | Family B 6 to 5, Family C 17 to 16; 37 studies in the three families, 21 reasoned non-fits |
| 2026-10-14 | **A27**: `mechanism_certainty` normalised to the design-driven scale of the codebook (levels 3 and 4 only for RoB 2 and for ROBINS-I rated Low or Moderate; narrative labels mapped to levels) | Post-hoc recoding, originals preserved | Descriptive tables only |

Not departed from: the research question, the eligibility *wording*, the codebook fields, the synthesis decision tree.

## 4. Headline figures at the freeze (computed; the live values are in `00_admin/CURRENT_FIGURES.md`)

| Item | Figure |
|---|---|
| Records | 34,594 raw; 27,481 after deduplication |
| Advanced to full text | 3,659; assessed 2,277; never assessed 1,382 |
| Full-text decisions | **1,078 included reports** and **1,199 excluded** |
| Distinct studies | **1,076** on the definite same-data links (S294/S366, S097/S098); **1,074** counting the partial-overlap links (S681/S682, S357/S369); the 5 RoB 2 report rows are 4 trials |
| Extraction | 1,078 rows of 92 fields |
| Effect-size rows | **58**: Family A 16, Family B 5, Family C 16 and 21 reasoned non-fits; **none pooled** |
| Human involvement | 197 full-text includes confirmed by the researcher (S001–S200 less three the researcher later excluded); a further 270 full-text records adjudicated by the researcher (166 exclusions, 104 inclusions; A6, A16, A19, A22–A26), so 467 of 2,277 full-text decisions (20.5%) carry human verification or adjudication; no human second extractor |

**Closed between the first draft of this registration and the freeze (2026-10-14, all PI rulings, reviewer CK).** (1) Open item A13: the adjusted odds ratio of S331 (Sarfo 2025, 4.27, 95% CI 3.07–5.93, n = 938) is an effect-size row placed with the reasoned non-fits, because its outcome is compliance with a notice deadline, not household access; Families A, B and C and every SWiM table are unchanged. (2) Open item A14: ten included studies whose full text is a landing page or absent carry the `full_text_status` values `landing_page_only` (8) and `abstract_only` (2); no count and no decision changed. (3) Open item A8: the disclosure statements (funding, competing interests, author contributions in the 14 standard CRediT roles, ethics, AI-tool provenance) are complete. These are the reasons the freeze was moved from the first release commit `a23f63e` to the later commit.

## 5. Disclosure on AI use and verification

Most screening, extraction, appraisal and drafting was carried out by a large language model (Claude, Anthropic) under the
researcher's direction (`AI_USE_STATEMENT.md`). Extracted values, risk-of-bias ratings, the direction coding of the syntheses and
the vocabulary mapping have **not** been verified by a human; a planned human second-extraction sample and the reviewer-2 queue
(open item A6) remain. The repository's own verifier checks internal consistency, not correctness against source papers.

## 6. OSF form fields

**Title.** *The Legal Last Mile: Legal and Administrative Barriers to Water and Sanitation Access — An AI-Assisted Systematic Review and Structured Quantitative Evidence Synthesis.* ("…and Meta-Analysis" is not used: nothing was pooled.)

**Authors.** Claudio Klaus, External Doctoral Candidate, Erasmus School of Law, Erasmus University Rotterdam, Rotterdam, The Netherlands.
Companion systematic review to the PhD dissertation *The Legal Last Mile: Administrative Law as a Mechanism of Connectivity and Exclusion
in Sanitation Governance: A Comparative Study of the Netherlands, Canada (Ontario), and Brazil*.

**Research questions.** Primary and secondary as in §2.

**Condition or domain.** Access to water and sanitation services as shaped by legal and administrative institutions (`PROJECT_SPEC.md` §5–6). The comparative scope of the parent project centres on Brazil, the Netherlands and Canada (Ontario); the search was not restricted to them.

**Existing data at registration.** All of it: the search, screening, extraction, appraisal and synthesis are complete to the extent set out in §3–4. `06_outputs/PRELIMINARY_RESULTS_REPORT_2026-09-29.md` and `07_manuscript/draft/MANUSCRIPT_DRAFT_2026-10-04.md` (an AI-generated draft not yet reviewed by a human author) are the public accounts of the results.

**Hypotheses.** None directional (§2).

**Eligibility, sources, study records, risk of bias, synthesis, meta-bias.** As in §2, with §3 for the dated clarifications; per-item detail in `INCLUSION_EXCLUSION.md`, `SEARCH_PROTOCOL.md`, `CODEBOOK.md`, `RISK_OF_BIAS.md`, `ANALYSIS_PLAN.md`.

**Funding and competing interests.** See `00_admin/disclosures/FUNDING_AND_COMPETING_INTERESTS_TEMPLATE.md` (filled): no specific grant from any funding agency in the public, commercial or not-for-profit sectors; database access through institutional subscriptions at Erasmus University Rotterdam; the costs of Anthropic Claude and OpenAI Codex were paid personally by the author and the Google Gemini runs (`gemini-3.1-flash-lite`) used the author's free-tier API key; the author declares no competing financial or non-financial interests and no relationship with Anthropic, OpenAI, Google or any other AI vendor. Ethics approval was not required (a review of published and grey literature, no primary data collection from human participants).

**Amendments from now on.** Any change after this registration is logged as a dated, reasoned amendment on OSF itself and in `CHANGELOG.md` (`PROTOCOL.md` §12); nothing is changed silently.

---

## Submission checklist (for the researcher)

- [x] OSF Generalized Systematic Review is the registry; PROSPERO ruled out (2026-09-12).
- [x] Draft reconciled with `PROTOCOL.md`, the files in §2 and `CHANGELOG.md` at release `0.2.0-interim` (2026-10-14).
- [ ] Push the tag `v0.2.0-interim` (the commit that carries this file; the command and hash are in the session report) so the registration can point at it, and record the full commit hash on the OSF form.
- [ ] On the OSF form state both dates (protocol fixed 2026-08-22; registered [date]) and label the registration retrospective in its first line.
- [ ] Attach or link this file, `PROTOCOL.md`, `INCLUSION_EXCLUSION.md`, `ANALYSIS_PLAN.md`, `CHANGELOG.md` and `00_admin/RELEASE_0.2.0-interim_2026-10-14.md`.
- [ ] Submit; record the OSF DOI/URL in `PROTOCOL.md` §11 and as a new dated `CHANGELOG.md` entry (not an edit to an old one); update the PRISMA checklist item 24a.
- [ ] If the repository is also archived on Zenodo, cross-link the two DOIs.
