# Systematic Review — *The Legal Last Mile*

> **Preliminary, AI-assisted, only partly human-verified.** A large language model (Claude, Anthropic) did most of the screening, data extraction, risk-of-bias appraisal and synthesis drafting, under the researcher's direction and a written protocol. A human independently checked only part of it. Treat every figure on this page as AI-produced and unverified against the source papers unless it is stated that a human confirmed it.

**Full title:** *The Legal Last Mile: An AI-Assisted Systematic Review of Legal and Administrative Barriers to Water and Sanitation Access* (preliminary, with contingent meta-analysis and structured quantitative evidence synthesis).
**Companion to:** the doctoral dissertation *The Legal Last Mile: Administrative Law as a Mechanism of Connectivity and Exclusion in Sanitation Governance — a comparative study of the Netherlands, Canada (Ontario) and Brazil* (Claudio Klaus).
**Release:** `0.2.0-interim`, figures as of **2026-10-14**.

---

## Where to look

| What | Where |
|------|-------|
| **Interactive results (the Atlas)** — results preview, methodology, PRISMA flow, evidence map, appraisal, harvest plot, 10 sensitivity scenarios, gaps, and the full text lists | https://jrklaus8.github.io/water-law-dataset/atlas/ |
| The review's files (protocol, databases, code, outputs) | Folder `legal-last-mile-systematic-review/` on the branch [`claude/legal-last-mile-review-spec-8ri0zs`](https://github.com/jrklaus8/water-law-dataset/tree/claude/legal-last-mile-review-spec-8ri0zs/legal-last-mile-systematic-review). It is **not on `main` yet**; this link will move when the branch is merged. |
| **New to the project? Start here** | [`START_HERE.md`](https://github.com/jrklaus8/water-law-dataset/blob/claude/legal-last-mile-review-spec-8ri0zs/legal-last-mile-systematic-review/START_HERE.md): the whole project on one page, what to trust, three reading paths (supervisor, auditor, replicator). [`GLOSSARY.md`](https://github.com/jrklaus8/water-law-dataset/blob/claude/legal-last-mile-review-spec-8ri0zs/legal-last-mile-systematic-review/GLOSSARY.md) explains every label (`A28`, `CK`, "AI-checked"). Each numbered folder has its own `README.md` |
| If you are auditing | `AI_USE_STATEMENT.md`, then `AUDITING_GUIDE.md`, `00_admin/DECISIONS_AND_OPEN_ITEMS.md`, `00_admin/CURRENT_FIGURES.md` |
| Re-check the whole repository | `python3 code/analysis/verify_repository.py` (it must report no failed checks) |

The Atlas is generated from the review's databases by `code/analysis/build_evidence_atlas.py`; a test checks that the published page equals the generator's output.

---

## Research question and design

How do legal and administrative arrangements — eligibility rules, documentation requirements, fees, service-area rules, administrative burden, enforcement, discretion, review and appeal — condition whether households obtain and keep water and sanitation services?

- **Protocol:** pre-specified inclusion and exclusion criteria and a 92-field extraction codebook, fixed on 2026-08-22, before any database was searched.
- **Registration:** the work was done before it was registered. A **retrospective** OSF registration has been prepared and frozen at the interim release but **has not been submitted**.
- **Reporting standards:** PRISMA 2020 for the flow; SWiM (Campbell et al. 2020) for synthesis without meta-analysis; harvest plot (Ogilvie et al. 2008) for display. **No pooling and no GRADE rating** — the syntheses report direction of association only.

---

## Search and screening (PRISMA flow)

| Stage | n | Note |
|-------|---|------|
| Records identified | **34,594** | Searched 2026-08-25 to 2026-09-11 |
| After de-duplication | **27,481** | 7,113 duplicates merged |
| Title and abstract: proceeded to full text | **3,659** | 26,222 records had an abstract and were screened by the AI; a human second pass covered the 3,665 include-or-unsure records, **not** the AI's exclusions |
| Full text assessed | **2,277** | 1,382 candidates were never assessed (1,200 not retrievable, 182 wrong file); retrieval was closed by researcher decision |
| **Included studies** | **1,072** | 1,205 excluded on full text |
| With an extractable effect-size row | 52 rows | 21 are reasoned non-fits outside the three synthesis families; none is pooled |
| In the three SWiM families | **31** | Vote counting of direction only |

**Records by source:** Scopus 5,984 · Web of Science 4,058 · ProQuest full-text/abstract query 7,728 · ProQuest Sociological Abstracts (thesaurus terms) 16,736 · JSTOR 50 · HeinOnline 1 · exploratory web-search pilot 37 · SSRN 0.

**Exclusions on full text (1,205):** wrong topic 490 · no empirical evidence 157 · inaccessible full text 151 · engineering only 106 · wrong exposure 93 · wrong outcome 88 · wrong study design 46 · wrong population 34 · wrong service 30 · duplicate 8 · insufficient information 2.

---

## What was included (1,072 studies)

- **Designs:** qualitative 529 · mixed methods 229 · observational 140 · quasi-experimental 57 · doctrinal 54 · jurimetric 36 · systematic reviews and other secondary 20 · experimental 5 · other 2.
- **Places:** 961 studies name exactly one country and 110 name several countries or a region. Most frequent: India 121, Brazil 80, South Africa 77, United States 62, Ghana 51, Kenya 47, Mexico 36. Publication years run from 1955 to 2026.
- **Legal systems:** common law 507 · civil law 377 · mixed, both or customary 174 · other 3 · blank 11.

## Risk of bias

Every included study carries a design-matched appraisal tool and rating: Legal Framework 426 · CASP Qualitative 248 · MMAT 195 · JBI Cross-Sectional 127 · ROBINS-I 53 · AMSTAR 2 18 · RoB 2 5. Among the 58 causal-capable studies, ROBINS-I ratings are Moderate 44 and Serious 9, and all five RoB 2 studies are "Some concerns".

> **What these ratings are:** rule-based batch ratings from the extracted fields using each instrument's structure, **not** a signalling-question read of each paper. No human second appraiser. The Legal Framework instrument is the project's own and is not validated.

---

## Synthesis: direction of association (SWiM)

No family clears the bar for meta-analysis, so all three are summarised by vote counting. Each study carries two codings: the **raw sign** of the reported estimate and the **substantive direction for households** (raw sign × outcome polarity × exposure orientation: for example, an odds ratio above 1 for a piped-water *interruption* among owners has a positive raw sign but an *Unfavourable* substantive direction).

| Family | Theme | Studies | Favourable | Unfavourable | Null | Mixed |
|--------|-------|---------|-----------|-------------|------|-------|
| A | Recognition and formal status | 13 | 10 | 1 | 2 | 0 |
| B | Assistance, participation and trust | 3 | 3 | 0 | 0 | 0 |
| C | Ownership, regulation and institutional structure | 15 | 5 | 7 | 0 | 3 |

Raw sign in Family C: 4 positive, 8 negative, 0 null, 3 mixed.

**Three conclusion tests were fixed before the numbers were computed:**
1. More than half of Family A Favourable — **holds** (10 of 13).
2. No Family B study Unfavourable or Null — **holds** (3 of 3 Favourable; but three studies testing three different mechanisms is too few to call a pattern).
3. No single direction holds a majority in Family C — **holds for substantive direction** (7 of 15 Unfavourable) but **fails for raw sign** (8 of 15 negative).

**Ten sensitivity scenarios** (baseline S0; drop abstract-only extractions; drop sparse-audit rows; drop rows for studies not flagged eligible; collapse linked reports; drop the Family A coding judgment call; recode S471 as Null; recode S879 as Null; all of these together; drop every study whose raw sign and substantive direction come apart). Tests 1 and 2 hold in all ten. The Family A Favourable share stays between 75% and 77%. The Family C raw-sign test fails in seven of ten scenarios and the substantive-direction test holds in all ten.

What the scenarios **do not** test: the direction coding itself, studies that were never extracted, and overlap between reports not flagged as linked. A vote count ignores effect size, precision and sample size, is not causal, and supports only a statement about direction.

---

## Human verification, counted strictly

Only decisions a human actually reviewed and ruled on are counted as human-verified. The reviewer initials **CK** are used only for the principal investigator's own rulings.

| Item | Figure |
|------|--------|
| Full-text decisions with human verification or adjudication | **459 of 2,277 (20.2%)** |
| — includes confirmed by a human second reviewer | 197 |
| — further decisions ruled on by the principal investigator (172 exclusions, 90 inclusions) | 262 |
| Includes flagged as borderline by the principal investigator (kept, flagged) | 13 |
| Decisions blind re-screened by a second AI model, and conflicts found | 112 and 31 |
| SWiM studies with a human-verified inclusion decision | **13 of 31** |
| SWiM studies checked by the AI only (no human confirmation) | **18 of 31** |
| SWiM studies whose direction coding the author has confirmed | **0 of 31** |
| Data extraction with a second extractor | **None** |
| Risk-of-bias appraisal checked by a human | **None** |

An audit of the AI's exclusions re-read 62 sampled records and reversed 3 (4.8%, 95% CI 1.7%–13.3%). Scaled to the pool of 1,046 this suggests roughly 51 wrongly excluded records (plausible range 17–139).

---

## Known limitations

1. **The search closed with disclosed gaps.** SSRN and Westlaw/Lexis were never searched; HeinOnline yielded one usable record despite 71,226 raw hits because no bulk export existed at that volume; only 50 of 356 JSTOR results were exported.
2. **Full-text retrieval was closed by decision.** 1,382 of the 3,659 records that reached full-text stage were never assessed (62.2% were).
3. **Extraction and appraisal were not independently verified.** The same system produced and audited much of the work, so its checks find inconsistencies and arithmetic errors but cannot confirm that a value matches its source paper. Ten extractions are from abstracts or metadata only.
4. **A data-corruption incident was caught and repaired in the open** (parallel screening batches sharing one output directory); the repository's audit trail records it and the repair.
5. **The protocol was not registered before the work was done** (see above).
6. **The source PDFs are not in the public repository** because many are subject to publisher copyright and licensing terms.

## Open items for the author

- **A30** — the author's own verification of the 31 SWiM studies against the source PDFs, including direction coding, and a blind second-extraction pass. A dossier with the stored values and verbatim passages exists; every verification box is blank.
- **A32** — approval or rejection of three proposed corrections to stored numbers (S037 sample size, S470 robustness estimate, S593 standard-error range). None has been applied.
- Further adjudication tiers, the second-extractor sample (many source PDFs are still missing) and the retrospective OSF registration upload.

The authoritative list is `00_admin/DECISIONS_AND_OPEN_ITEMS.md` in the review folder.

---

## How to cite

See [[Citation]]. Never treat any count or figure from the interim release as final; re-check the source CSVs and the changelog for the version you cite. See also [[AI Disclosure]].
