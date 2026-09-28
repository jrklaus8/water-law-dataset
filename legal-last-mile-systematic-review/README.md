# The Legal Last Mile — Systematic Review

**Preliminary Systematic Review and Contingent Meta-Analysis, with Structured
Quantitative Evidence Synthesis**

Companion project to the doctoral dissertation *The Legal Last Mile:
Administrative Law as a Mechanism of Connectivity and Exclusion in
Sanitation Governance: A Comparative Study of the Netherlands, Canada
(Ontario), and Brazil* (Claudio Klaus).

**Last updated: 2026-09-28.** Current phase: Phases 1–5 complete; Phase 6
(full-text screening) live and roughly 62% through its pool; Phase 8
(extraction) fully caught up with Phase 6; Phase 9 (risk of bias) barely
started relative to how much has been extracted; Phase 10 (evidence
classification) caught up with extraction; Phase 11 (corpus-level
quantitative-feasibility judgment) not yet formally written up. See
**Current project status** below for exact figures, and **What future
researchers must know before using this dataset** for what those figures do
and do not mean.

This document is written as an audit record, not a summary for display. It
is meant to let a future researcher, collaborator, supervisor, reviewer, or
auditor open this project for the first time and understand, within a few
minutes, what has actually been done, what has not, where the judgment
calls and irregularities are, and which files to trust for which purpose.
Where the project's history is messy — and parts of it are — that messiness
is preserved here rather than cleaned up.

---

## Known limitations and unresolved issues (read this first)

A reader should see these before relying on anything below. Each is
explained in full further down; this is the index.

1. **The search closed with real, disclosed gaps.** Two planned databases —
   SSRN and Westlaw/Lexis — were never searched at all. HeinOnline yielded
   essentially one usable record despite 71,226 raw hits, because no bulk
   export mechanism existed at that volume and most of what Cowork retrieved
   never made it back into this pipeline as a file. JSTOR: only 50 of 356
   identified results were ever exported. See **Chronological workflow → 2.
   A closed, disclosed search**.
2. **A genuine multi-agent data-corruption incident occurred and was caught,
   not avoided.** Screening 19,085 newly-added records as 39 parallel
   batches sharing one output directory caused several batches to lose
   hundreds of rows to file collisions. All 39 were discarded and rebuilt
   from isolated directories, validated record-for-record before merging.
   See **Chronological workflow → 4**.
3. **A second, smaller data-corruption artifact survived that fix and was
   found later**, during a random QA spot-check of excluded records — one
   record's stored AI rationale and exclusion code were from a different,
   unrelated paper (an oncology study), evidently misassigned during the
   same 39-batch merge. A full-pool scan for the same corruption signature
   found 74 matching records; manual review confirmed all 74 were genuinely
   off-topic, not further corruption. See **Chronological workflow → 4**.
4. **Title/abstract reviewer agreement was unusually high (99.8%)** for
   genuinely independent two-reviewer screening — high enough that it was
   flagged to the researcher and confirmed before being merged into the
   permanent record, rather than treated as a routine result. See
   **Chronological workflow → 5**.
5. **Full-text human second-review (reviewer_2) is real but only 8.7%
   complete.** As of 2026-09-27, the PI has independently reviewed and
   confirmed the first 100 of 1,162 current full-text includes (S001–S100).
   The remaining 1,062 includes, and all 1,114 excludes, at the full-text
   stage still carry no human second reviewer. Do not read "a human
   reviewer_2 pass has begun" as "the full-text stage is independently
   verified." See **Current project status** and **Human and AI
   involvement**.
6. **Risk-of-bias appraisal is the most under-done phase relative to how far
   extraction has progressed.** 1,116 of 1,162 extracted studies have their
   design-matched appraisal *tool* identified, but only 33 have an actual
   *rating*, and 29 of those 33 are explicitly partial/pilot judgments (many
   literally recorded as "Not ratable" or "at least [severity]"), not
   completed appraisals against the real instrument.
7. **At least three known cases of the same paper being assigned two
   different `record_id`s exist**, caused by DOI-formatting variants across
   different search-database exports of the same article (e.g. a trailing
   volume/year fragment appended to one export's DOI field but not the
   other's). Two were caught during a 2026-09-16 post-hoc duplicate audit
   (`S227`, `S399` — see `CHANGELOG.md`); a third was caught today,
   2026-09-27, while matching studies to reviewer confirmations (see
   **Chronological workflow → 5**, "S063"). There is no guarantee every such
   variant across the full 27,481-record pool has been found.
8. **Several governing documents in this repository contain status sections
   that are now significantly out of date and must not be read as current.**
   `PRISMA_WORKFLOW.md`'s Phase 6 entry, `RISK_OF_BIAS.md` §4, and
   `ANALYSIS_PLAN.md` §13 all still describe an earlier, much less advanced
   state of the project. The parent repository's own top-level `README.md`
   ("Companion Project" section) is stale by roughly the same margin. See
   **A warning about stale documentation** for exactly what is wrong in each
   and where the current truth actually lives.
9. **Quantitative synthesis remains genuinely contingent, by design, not by
   accident.** 61 effect-size rows have been extracted from 248
   quantitative-synthesis-eligible studies; zero are currently pooled into
   any meta-analytic estimate. That is the expected, correct state of a
   project that refuses to manufacture comparability — see **The review does
   not assume meta-analysis is appropriate** — not a sign that this phase has
   stalled.
10. **A small number of "wrong file retrieved" and "partial/unusable
    extraction" cases are deliberately left open, not force-decided.**
    159 records currently carry a `wrong_file_retrieved` flag (the delivered
    PDF did not match the target citation, or the extraction tool returned
    an unusable fragment of the real document); these are not screened and
    not counted in any decided total until the correct file is retrieved.
    A more insidious variant was first confirmed 2026-09-27: 14 of these
    records (across three consecutive batches) are cases where the
    Drive file's own filename/title metadata matched the target exactly,
    but the actual PDF **content** behind that fileId was a completely
    unrelated paper — a title check alone would have missed this; only
    reading full-text content before every decision caught it. A separate
    case was confirmed the same day where the identical wrong content was
    delivered a second time under a different `record_id`. See
    `CHANGELOG.md`, "Two-hundred-thirty-fourth" through
    "Two-hundred-thirty-sixth full-text screening batch" entries, for the
    full account.
11. **A named, systemic cause of the wrong-file problem was identified
    2026-09-28: a delivery tool's own "verified" label cannot be trusted.**
    A second large Drive delivery's own tracking file
    (`systematic_review_retrieval_final_master.csv`) showed 99 of its
    records were harvested by fuzzy title-word matching against local
    Zotero storage — confidence as low as 40%, 95 of 99 below 80% — yet
    every one was self-labeled `RETRIEVED_AND_VERIFIED`. Of 69 genuinely
    open records in that delivery, 68 turned out, on direct full-text
    reading, to be wrong-file deliveries; 65 of those 68 fell inside this
    low-confidence set. One record's correct target content was found
    mislabeled under a *different* record's file entirely (see
    **Chronological workflow → 5** for that specific correction). This
    tool's self-reported retrieval/verification status must never be
    treated as evidence of actual content correctness — only direct
    full-text reading, as this pipeline has always done, establishes that.
    See `CHANGELOG.md`, "Two-hundred-thirty-seventh full-text screening
    batch," for the full account.

---

## What this project is

A systematic review of the empirical literature on how legal and
administrative institutions shape the translation of the physical
availability of water/sanitation infrastructure into effective household
access — plus a *contingent* structured quantitative evidence synthesis and
restricted meta-analysis, conducted only where the completed search turns
up genuinely comparable study families.

**Research question** (`PROTOCOL.md` §2.1): How do legal and administrative
institutions shape the translation of physical availability of water and
sanitation infrastructure into effective household access, and what
evidence exists concerning the mechanisms — eligibility screening,
administrative burden, discretion and accommodation, and enforcement —
through which this happens? A secondary, narrower question governs the
quantitative arm: where sufficiently comparable evidence exists, what is
the magnitude of the association between specific legal/administrative
access conditions and household water/sanitation access outcomes?

### The review does not assume meta-analysis is appropriate

This is a governing methodological commitment, not a caveat added after the
fact. `PROJECT_SPEC.md` §3 states the core verdict explicitly: **a single
pooled meta-analysis of "administrative law and sanitation access" is not
justified at the outset.** A systematic review is justified; a structured
quantitative evidence synthesis is justified; restricted meta-analyses
*may* be justified once (and only where) the evidence turns out to contain
genuinely comparable study families. The rule that supersedes every
technique in `ANALYSIS_PLAN.md`:

> **Do not manufacture comparability.** A mathematically convertible
> statistic is not automatically a substantively comparable effect.

Concretely: legal recognition vs. non-recognition, administrative
assistance vs. usual procedure, documentation requirements, service-area
eligibility, political coordination, and judicial review are not one common
"intervention." Formal connection, water quantity, reliability,
affordability, application success, and service continuity are not one
common "outcome" merely because they are all colloquially "access."
`ANALYSIS_PLAN.md` §2's decision tree is applied **per candidate synthesis
family** (Family A — legal recognition and access; Family B — administrative
assistance and access; Family C — administrative/legal barriers and access
inequality; `PROJECT_SPEC.md` §8), not once globally, and pooling only
happens where a family survives every branch of that tree. As of this
writing, no family has: see **Current project status**.

### How this relates to, and stays separate from, the judicial decisions dataset

The rest of this git repository (outside this `legal-last-mile-systematic-
review/` folder) hosts the **Global Water Law Judicial Decisions Dataset**
— 83,596 court decisions scraped from Brazil (27 state courts), Canada
(federal + provincial via CanLII), and the Netherlands (Raad van State +
all district courts), coded via jurisdiction-specific regex into thematic
categories. It is a **different empirical strand of the same doctoral
project**, not a data source for this review, and the two are deliberately
never merged into one statistical model (`PROJECT_SPEC.md` §9):

- The judicial dataset observes **litigation** — a *selected* pathway. A
  household can experience administrative exclusion from water/sanitation
  access without ever producing a court decision, so case counts cannot be
  treated as a representative sample of the underlying access problem.
- This review observes **households, applicants, and communities**
  directly, through empirical studies (survey, case study, program
  evaluation, regression) of legal/administrative access conditions.
- The judicial dataset's legitimate role here is **triangulation and
  hypothesis generation** — "a separate source of evidence concerning the
  legal visibility and adjudication of water governance disputes," never
  "statistical validation of household-level evidence" — and as the basis
  for a possible, separate future jurimetric comparison paper.
- They live in the same git repository as a matter of convenience (it's the
  repository the researcher was already working in), not because they
  share a research design.

See `PROJECT_SPEC.md` §9 for the full reasoning and the doctoral
mixed-methods architecture that connects them.

---

## Current project status

Every number below is traceable to a specific CSV, script output, or dated
`CHANGELOG.md` entry as of **2026-09-27**. Where a document elsewhere in
this repository disagrees with a number here, this section and the live
CSVs it is drawn from are authoritative — see **A warning about stale
documentation**.

| Stage | Status |
|---|---|
| Records identified | 34,594 raw (34,557 database + 37 grey-literature/pilot) |
| Deduplication | 27,481 unique candidates (7,113 duplicates merged) |
| Title/abstract screening | **Complete, double-reviewed.** 26,222 of 27,481 had a real abstract and were screened; 1,259 deliberately left undecided (no abstract). Final: **3,659 include / 6 exclude**, zero firm conflicts, after AI first pass (3,062/22,557/603 unsure) + human second pass over all 3,665 include+unsure records |
| Full-text screening | **Live, in progress.** 2,276 of 3,659 assessed (**1,162 include / 1,114 exclude**); 1,383 still open; **159 flagged `wrong_file_retrieved`** (not counted in any total) |
| Full-text human reviewer_2 | **Just begun, 8.7% complete.** 100 of 1,162 current includes (S001–S100) independently confirmed by the PI, zero conflicts. 1,062 includes and all 1,114 excludes still unreviewed by a human second reviewer at this stage |
| Extraction (92-field codebook) | **Fully caught up with full-text screening.** 1,162 studies extracted, `S001`–`S1164` (`S227`, `S399` retired as documented post-hoc-duplicate corrections — real gaps in the numbering, not an error) |
| Risk-of-bias appraisal | **Barely started relative to extraction.** Design-matched tool identified for 1,116 of 1,162 studies; an actual **rating** exists for only **33** — 29 of those are explicit partial/pilot judgments (2026-09-16 batch), 2 are complete AMSTAR 2 ratings for included secondary reviews (S370, S372 — both "Critically Low"), 2 more are complete individual ratings (S468 CASP Qualitative "Moderate"; S469 MMAT "Moderate") |
| Evidence classification | **Caught up with extraction.** `evidence_map.csv` populated for all 1,162 studies — 248 flagged quantitative-synthesis-eligible, 1,062 qualitative-synthesis-eligible (categories overlap) |
| Quantitative evidence (effect sizes) | 61 rows extracted from the 248 eligible studies (a much stricter subset — only regression-based estimates directly isolating a legal/institutional mechanism qualify): 20 Family A, 6 Family B, 16 Family C, **19 rows added before the Family A/B/C tag was consistently applied and still carry a blank family** (a real, disclosed data-cleanliness gap) |
| Pooled/meta-analytic estimates | **Zero.** Every effect_sizes.csv row has `included_in_pooled_estimate = FALSE`; almost every one cites "single study defining this exact exposure-comparator pairing" as the reason, per `ANALYSIS_PLAN.md` §2 |
| Corpus-level quantitative-feasibility judgment (Phase 11) | **Not yet formally written up** as its own document, though the decision-tree reasoning is already recorded per-effect-size in `effect_sizes.csv`'s `exclusion_from_pooling_reason` field |
| Meta-analysis / sensitivity / publication-bias code (Phases 12–15) | Templates exist (`08_code/R/*.R`, `06_outputs/supplementary/SWIM_SYNTHESIS_TEMPLATE.md`) but have **never been run against real data** |
| Preregistration | Draft ready (`00_admin/preregistration/osf_preregistration_draft.md`), **not submitted** — no OSF account access from this environment |
| Manuscript | Outline only (`07_manuscript/draft/manuscript_outline.md`) plus a non-final preliminary report (`preliminary_report_2026-09-13.md/.docx`) — no real draft |

Exclusion-reason breakdown at full-text stage (E01–E12,
`INCLUSION_EXCLUSION.md`), of 1,114 total: E01 wrong topic 496 · E02 wrong
population 34 · E03 wrong exposure 34 · E04 wrong outcome 77 · E05 no
empirical evidence 134 · E06 engineering only 106 · E07 wrong service 26 ·
E08 duplicate 6 · E09 insufficient information 2 · E10 inaccessible full
text 151 · E11 wrong jurisdiction/context 0 · E12 wrong study design 48.

For the full, growing, dated history behind every one of these numbers —
including every batch of screening decisions, every included/excluded
study and why — see `CHANGELOG.md` and
`06_outputs/supplementary/preliminary_results.md`, both updated after every
batch of work. For the PRISMA 2020 flow-diagram presentation of the same
numbers, see `06_outputs/prisma/prisma_flow.md` (kept in sync with these
CSVs; **not** the same as, and more current than, `PRISMA_WORKFLOW.md` —
see below).

---

## What future researchers must know before using this dataset

This expands the index at the top of this document.

### Search coverage is real but incomplete, and was closed by a judgment call, not exhaustion

The search phase closed 2026-09-11 by the researcher's decision that the
candidate pool (34,594 raw records at that point) was already large enough
to move to screening — **not** because every planned database had been
searched. SSRN and Westlaw/Lexis were never searched at all. HeinOnline
found 71,226 raw hits but had no bulk-export mechanism at that volume, and
of the small number of records Cowork did retrieve, most never reached this
pipeline as an actual file — real yield was effectively one record. JSTOR
identified 356 relevant results but only 50 were ever exported. None of
this is hidden in `search_log.csv`'s stub rows (`SEARCH_042`, `SEARCH_043`)
or in `SEARCH_PROTOCOL.md` §7 — but a reader relying only on a manuscript's
prose summary rather than this repository could easily miss how real these
gaps are. Any manuscript drawn from this review must report them, per PRISMA's
search-strategy transparency requirement.

### Two real data-corruption incidents happened during screening — both caught, one after the fact

See **Chronological workflow → 4** below for the full account of the
39-parallel-batch file-collision incident (all 39 batches discarded and
rebuilt) and the separate, smaller corrupted-rationale artifact caught
later by a random QA spot-check. Both are disclosed in detail in
`CHANGELOG.md` at their original dates. The fact that both were caught is
evidence the project's validation discipline works; it is not evidence
that no further undetected corruption exists anywhere in a 27,481-record
pipeline that has passed through this many batch-processing rounds.

### The reviewer-agreement rate at title/abstract stage is unusually high, and that was treated as a flag, not a compliment

99.8% agreement between the AI first-pass reviewer and the human second
reviewer, over 3,665 records, is far higher than independent two-reviewer
screening typically produces. This was surfaced to the researcher **before**
being merged into `final_decision`, and the researcher reviewed it and
confirmed proceeding with the delivered file. Any manuscript reporting this
review's screening statistics should disclose this caveat alongside the
99.8% figure, not report the number alone.

### Human independent review of full-text decisions is real, but only just begun

Until today, no full-text include or exclude decision in this review had
been independently confirmed by a human second reviewer — `reviewer_2`
was blank for all 3,659 rows of `full_text_screening_database.csv`. As of
2026-09-27, the PI has reviewed and confirmed the first 100 chronologically
included studies (`S001`–`S100`), agreeing with the AI reviewer's
classification in all 100 cases, zero conflicts. **This is 100 of 1,162
current includes (8.7%) and 0 of 1,114 current excludes.** Treat every
full-text decision beyond those 100 confirmed includes as AI-reviewer-only
until this README says otherwise, and check `full_text_screening_database.csv`'s
`reviewer_2` column directly rather than assuming this document is current
if substantial time has passed since 2026-09-27.

### Risk-of-bias appraisal is real but thin, and much of what exists is explicitly partial

`RISK_OF_BIAS.md` assigns each extracted study a design-matched tool (RoB 2,
ROBINS-I, one of two JBI checklists, CASP, MMAT, or AMSTAR 2 for
already-systematic-review sources); that assignment step is essentially
done (1,116 of 1,162). Actually *rating* a study against the real
instrument is a slower, harder step, and only 33 studies have any rating at
all. Of those, 29 come from a single 2026-09-16 pilot batch and are
frequently recorded as "Not ratable" (e.g. AMSTAR 2 applied to a study that
turned out not to fit the tool) or "at least [severity]" (a partial,
conservative judgment, not a completed determination). Only 4 studies
(S370, S372, S468, S469) currently carry what reads as a complete,
non-partial rating. **Do not cite this review's risk-of-bias appraisal as
substantially complete** — appraising the remaining ~1,116 extracted
studies is the single largest piece of unfinished work in the pipeline
relative to how far everything upstream of it has progressed.

### At least three known duplicate-record_id cases exist from DOI-formatting drift across databases

The same underlying paper can enter this pipeline's `27,481`-record pool
twice under two different `record_id`s if its DOI is formatted slightly
differently in two different source-database exports (a trailing
volume/year fragment, a URL prefix, a case difference). Three such cases
are documented: `S227` and `S399` (found in a 2026-09-16 post-hoc duplicate
audit and retired from the extraction numbering) and a third, involving
`record_id`s `R7EECD84CD3AA`/`RF043AAD78E8E` for the same paper (Pastrana-
Miranda & González-Caamal 2022), found 2026-09-27 while matching studies to
human reviewer confirmations (see `CHANGELOG.md`, same date). All three
were caught by deliberate audits or cross-checks, not by any systematic
guarantee — a future researcher extending this dataset should not assume
the pool is fully de-duplicated at the DOI-variant level, only that known
instances have been fixed.

### The quantitative arm is intentionally thin — this is a finding, not a failure

245 studies are flagged quantitative-synthesis-eligible, but only 58
effect-size rows have actually been extracted, and zero are pooled. This
reflects the project's governing rule against manufacturing comparability
(see above), applied consistently: almost every effect-size row's own
`exclusion_from_pooling_reason` field says, in effect, "this is currently
the only study operationalizing this exact exposure-comparator pairing."
That is not a temporary gap to be closed by working faster — pooling
becomes appropriate only if and when a genuinely comparable second (and
further) study is found and extracted for the same family, which the
ongoing full-text screening may or may not eventually produce.

---

## Chronological workflow: what was actually done, in order

This is the narrative account — written so a reader can follow what
happened and why without reading every underlying protocol document
first. It is a companion to, not a replacement for, the documents it
references, which carry the exact numbers, scripts, and decision rules.

### 1. Protocol first, search second

Before any database was queried, `PROTOCOL.md` fixed the research
questions and conceptual framework, and `PROJECT_SPEC.md` fixed the
scope-discipline rules everything downstream had to obey — most
importantly, the instruction *not* to assume a pooled meta-analysis is the
goal, and to treat whether one is even justified as itself a question the
review has to answer with evidence.

### 2. A closed, disclosed search

`SEARCH_PROTOCOL.md` lays out the databases, concept blocks, and
per-database search strings. This environment has no direct network access
to any of these platforms (confirmed 2026-08-25) — the search was run
entirely by the researcher via EUR institutional access, largely relayed
through a separate browser-capable Claude Cowork session, with raw exports
handed back to this pipeline for normalization and screening. It covered
Scopus (18/18 planned batches), Web of Science, HeinOnline (mostly lost to
delivery failures, not search failures — see above), ProQuest, ProQuest/
Sociological Abstracts, and JSTOR (partial), and closed 2026-09-11
**before** two planned databases — SSRN and Westlaw/Lexis — were ever
reached, because the candidate pool was already judged large enough to move
forward. That is recorded as a real, disclosed gap (`SEARCH_PROTOCOL.md`
§7), not smoothed over.

Separately, three rounds of an explicitly **non-systematic exploratory
pilot** used Claude's `WebSearch` tool (37 candidate records,
`SEARCH_003`–`SEARCH_017`) before the real search phase began. This never
counted toward the protocol search and must never be described as a
substitute for it in any manuscript output — weaker recall, no
reproducible result set, and initially no full-text/abstract access beyond
a search snippet.

### 3. Deduplication with a stable, auditable identifier

34,594 raw records were merged and deduplicated
(`code/search/deduplicate.py`, DOI-match + title/year-similarity match)
into 27,481 unique candidates, with every merge logged in
`01_search/deduplicated/merge_log.csv`. Each record's ID is a **stable
content hash** (of its DOI, or title+year) rather than a row number, so a
record's identity survives re-exports, re-ordering, or partial re-runs.
Two real adapter bugs were found and fixed during this phase: a
data-corrupting quote-escaping issue in the Web of Science adapter, and a
`csv` field-size-limit default that would have silently truncated large
ProQuest conference-abstract-supplement fields.

### 4. Two-reviewer screening — including a real corruption incident, caught and fixed

**Title/abstract (Phase 5).** All 26,222 abstract-bearing records were
screened by an AI first-pass reviewer against `INCLUSION_EXCLUSION.md`'s
twelve exclusion codes, explicitly authorized as a methodological choice in
`PROJECT_SPEC.md` §14.18. The largest single round — 19,085 newly-added
ProQuest/Sociological Abstracts records — was screened as 39 parallel
~500-record agent batches. **The first attempt used a shared output
directory across all 39 agents.** Post-hoc validation found several
"completed" batches missing hundreds of rows each; one agent's own report
described a helper script silently overwritten and its output redirected
into a different batch's file — a genuine multi-agent file collision, not
a screening-quality problem. **All 39 batches were discarded and redone**
from isolated per-batch scratch directories, then validated
record-for-record against their source files (exact record_id-set match,
no duplicates, no foreign IDs) before merging.

A human second reviewer (`reviewer_2`) then independently reviewed all
3,665 records the AI marked `include` or `unsure`, via a purpose-built
spreadsheet handoff (`02_screening/title_abstract/REVIEWER_2_README.md`).
Result: 3,659 include / 6 exclude, zero conflicts under the strict
definition (all 6 excludes were resolutions of AI `unsure` calls, not
overturned AI `include` calls). **The 99.8% agreement rate was flagged to
the researcher before merging**, as unusually high for genuinely
independent screening; the researcher reviewed it and confirmed proceeding.

A follow-up 120-record random QA spot-check of the *excluded* population
(fixed seed, reproducible) found 119/120 correctly reasoned exclusions and
**one real corruption artifact**: a record's stored AI rationale and
exclusion code belonged to an entirely different, unrelated paper (an
oncology biomarker study), evidently misassigned during the same 39-batch
merge described above. The exclude decision itself happened to still be
correct (the actual paper was an unrelated wastewater-reservoir modeling
study, correctly out of scope, just under the wrong stated reason). This
was fixed, and — rather than assuming the single random sample had caught
everything — the **entire 22,557-record exclude pool was scanned for the
same corruption signature** (a rationale citing a domain wholly foreign to
water/sanitation/legal-administrative research). 74 records matched; an
18-record manual check confirmed all 74 were genuinely off-topic, not
further instances of the corruption.

**Full text (Phase 6, live).** The researcher supplies PDFs on a rolling
basis; each is converted to text, screened against the same E01–E12 codes,
and recorded via atomic-write Python scripts rather than hand-edited, to
keep the tracking CSV internally consistent. A human `reviewer_2` for this
stage was an explicitly open, unresolved question for most of this
project's history — see **Human and AI involvement** for its current,
partial resolution as of today.

### 5. Extraction against a fixed codebook — and a hard rule against filling gaps from memory

Every included study is extracted into a 92-column database
(`03_extraction/extracted_data/extraction_database.csv`) against
`CODEBOOK.md`: jurisdiction, population, legal mechanism family
(ELIGIBILITY / BURDEN / DISCRETION_ACCOMMODATION / ENFORCEMENT), outcome
hierarchy, mediators, statistical information, and provenance. The rule
that shapes this phase more than any other: **never fabricate data.**
Studies that clear full-text screening but whose retrieved text is
unusable (missing chapters, wrong file, truncated extraction) are left
unextracted and flagged, not reconstructed from a general sense of what
such a paper "probably" reports.

**A DOI-formatting duplicate was caught mid-workflow, 2026-09-27, and is
recorded here as a concrete example of what "the pipeline is imperfect but
self-correcting" actually looks like.** While matching `S001`–`S100` back
to their `record_id`s to record the PI's reviewer_2 confirmation (see
below), `S063`'s extraction DOI matched a `record_id`
(`R7EECD84CD3AA`) that was *itself* already flagged `exclude` (E08,
duplicate) — because that record_id's own extraction attempt had already
been identified as a duplicate of `S063` and correctly retired. The real
match was a second record_id, `RF043AAD78E8E`, whose DOI in its own source
export carried an extra `vol462021` suffix the other export's DOI lacked.
A same-paper "matched but final_decision=exclude" sanity check caught this
before any write. See `CHANGELOG.md`, 2026-09-27, for the full account —
it is exactly the kind of "known DOI-drift duplicate" class already
disclosed above, not a new problem, but a fresh instance of an old one.

**A second, different kind of cross-record mislabeling was caught the
following day, 2026-09-28, by the same discipline of never trusting a
label without reading the actual content.** Record `RC8E1C6959D2C` had
been flagged `wrong_file_retrieved` in an earlier batch after an unrelated
Kampala, Uganda paper was delivered under its record_id. During a later
Drive delivery's reconciliation, that record's real target citation
(Sámano Romero & Chávez-Mejía 2025, "Water Access in Mexico City") was
found — by direct full-text reading, not by trusting any filename or
tool-reported status — sitting under a *different* record_id's file
entirely, `R023B3A0D827A`. Confirmed via the read tool's own
`.viewUrl`/`.title` fields that this was a genuine delivery-side
cross-contamination, not a mapping error on this pipeline's end.
`RC8E1C6959D2C` was corrected to `include` (`S1157`) using that content;
`R023B3A0D827A` was separately flagged `wrong_file_retrieved`, since its
own target citation remains unretrieved. See `CHANGELOG.md`,
"Two-hundred-thirty-seventh full-text screening batch," for the full
account.

### 6. Risk-of-bias ratings are mostly still blank, deliberately

`RISK_OF_BIAS.md` assigns each study a design-matched appraisal tool. None
of the validated instruments (RoB 2, ROBINS-I, the JBI checklists, CASP,
MMAT, AMSTAR 2) may be reconstructed from memory — appraising a study
against "roughly what RoB 2 asks" is not the same as appraising it against
the actual current instrument. So the tool field is populated broadly
(1,116 of 1,162), while the rating field is left blank pending a real,
careful pass with the correct instrument in hand — except for the 33
studies described in **Current project status**, most of which are
themselves only partial/pilot judgments. This is reported as a disclosed
limitation of the review's current state, not hidden as a completed step.

### 7. Evidence classification: mechanical where safe, judgment where not

`code/analysis/build_evidence_map.py` derives what can be derived
mechanically and safely — study design class from the appraisal tool
assigned, mechanism family from the extraction's own boolean fields,
legal/institutional context copied straight from the extraction record —
and stops there. Fields that require actual judgment (which outcome family
a study's central finding belongs to; whether a study's statistics are
calculable enough to be quantitative-synthesis-eligible) are filled by
hand, one study at a time. The script prints an explicit warning for every
field it leaves blank for a human to decide, rather than guessing.

### 8. What has not started yet, and why that is a decision rather than an oversight

Quantitative feasibility assessment (Phase 11) applies `ANALYSIS_PLAN.md`
§2's decision tree to each candidate synthesis family as a corpus-level
methodological judgment — not a per-study fact — and has deliberately had
no tooling built ahead of it, because the decision tree itself already *is*
the whole process. It will be written up formally once enough of the
corpus is extracted and classified to ask the question meaningfully at the
family level, though the per-effect-size reasoning that will feed it is
already being recorded as each effect size is extracted. Meta-analysis,
structured synthesis, sensitivity analysis, and publication-bias assessment
(Phases 12–15) have templates already built and committed, but are
explicitly untested against real data and gated on Phase 11 actually
finding a synthesis family eligible.

### 9. Mechanics that keep the record honest, not just the conclusions

- **Atomic writes** (`tempfile.mkstemp()` + `os.replace()`) on every script
  that touches a tracked CSV, so a crash mid-write can never leave a
  half-written, silently-corrupt data file behind.
- **Schema validation** (`code/analysis/validate_schemas.py`) run after
  every batch of edits, checking each CSV's real header against its
  documented or generated schema — currently 13/13 clean.
- **Single-record / single-batch CLI scripts**, not hand-editing, for both
  screening databases — reduces the chance of an off-by-one or copy-paste
  error silently corrupting a neighboring row.
- **Provenance fields on every record** — which reviewer, which model
  version, which date — so a decision can always be traced back to who (or
  what) made it and when.

---

## A warning about stale documentation

Several files in this repository describe an earlier state of the project
and have not been kept in sync with the live databases. **Do not treat any
of the following as current without cross-checking the CSVs directly**:

- **`PRISMA_WORKFLOW.md`, Phase 6 entry.** Currently frozen at "1,535 of
  3,659 records decided (795 include / 740 exclude)" with an 11-record
  `wrong_file_retrieved` list that no longer matches the current 118. The
  live figure is **2,276 of 3,659 (1,162 include / 1,114 exclude)** — see
  **Current project status** above. The rest of `PRISMA_WORKFLOW.md`'s
  16-phase table (Phases 1–5) is accurate; only its later-phase entries
  have drifted.
- **`RISK_OF_BIAS.md` §4 ("Status")** still says "No study has yet been
  appraised... full-text screening (Phase 6) and pilot extraction (Phase 7)
  are both scaffolded but not yet run against real decisions." This was
  true when written and is now badly wrong: full-text screening is 62%
  through its pool, extraction is fully caught up with it, and 33 studies
  have some risk-of-bias rating (see **Current project status** for what
  "some" actually means here).
- **`ANALYSIS_PLAN.md` §13 ("Status")** still says "No data has been
  extracted, so no analysis in this document has actually been run...
  full-text screening (Phase 6) hasn't produced real decisions yet." Also
  now badly wrong for the same reason.
- **The parent repository's top-level `README.md`**, "Companion Project:
  Systematic Review" section, currently says "full-text screening is live
  (131 assessed so far)... 62 studies fully extracted." The real figures
  are roughly 17× and 18× higher respectively. This file lives outside
  this folder and is not something this review's own batch-processing
  workflow touches automatically — a future update to this README should
  be paired with an update there.
- **This README itself, before this rewrite**, had already drifted
  internally: its own top-line status paragraph correctly said 2,253/1,142/
  1,111, while a lower section still said "all 488 fully-extracted studies
  (S001–S490)" — a number from many batches earlier. That inconsistency is
  fixed as of this rewrite, but it is worth recording as a concrete
  demonstration that **this document is not automatically immune to the
  same drift** described above; if you are reading this long after
  2026-09-27, verify the numbers above against the CSVs before trusting
  them.

**What is always current:** the CSVs themselves
(`02_screening/full_text/full_text_screening_database.csv`,
`03_extraction/extracted_data/extraction_database.csv`,
`05_analysis/descriptive/evidence_map.csv`,
`05_analysis/effect_sizes/effect_sizes.csv`,
`02_screening/exclusion_log/exclusion_log.csv`), plus
`06_outputs/prisma/prisma_flow.md` and
`06_outputs/supplementary/preliminary_results.md`, both of which are
regenerated or appended to after every batch of screening/extraction work
as a matter of process discipline. When in doubt, re-derive a number from
one of these rather than trusting any narrative document's restatement of
it — including this one, if enough time has passed since the date at the
top.

---

## Which files are authoritative for what

| File | Authoritative for |
|---|---|
| [`PROJECT_SPEC.md`](PROJECT_SPEC.md) | The governing methodological *reasoning* — why the review is designed this way, scope discipline, the anti-confirmation-bias rule, the relationship to the judicial dataset |
| [`PROTOCOL.md`](PROTOCOL.md) | The registered review design — research questions, PECO, PRISMA-P structure (draft, not yet submitted) |
| [`SEARCH_PROTOCOL.md`](SEARCH_PROTOCOL.md) | Databases, concept blocks, per-database search strings, and the real current search-coverage status |
| [`INCLUSION_EXCLUSION.md`](INCLUSION_EXCLUSION.md) | Screening criteria and the E01–E12 exclusion codes |
| [`CODEBOOK.md`](CODEBOOK.md) | Extraction rules — the 92-field schema, mechanism/outcome coding, evidence-status labels |
| [`RISK_OF_BIAS.md`](RISK_OF_BIAS.md) | Which appraisal tool applies to which study design (its own §4 "Status" is stale — see above) |
| [`ANALYSIS_PLAN.md`](ANALYSIS_PLAN.md) | Synthesis decisions — the quantitative-feasibility decision tree, effect-size strategy, contingent meta-analytic model (its own §13 "Status" is stale — see above) |
| [`PRISMA_WORKFLOW.md`](PRISMA_WORKFLOW.md) **and the live databases** | The 16-phase workflow narrative — reliable for Phases 1–5, **stale for Phase 6 onward**; for current numbers use this README's status table, `06_outputs/prisma/prisma_flow.md`, and the CSVs directly |
| [`CHANGELOG.md`](CHANGELOG.md) | The full, dated history of every methodological decision, correction, and status change, in the order it actually happened — the primary audit trail |
| [`DATA_DICTIONARY.md`](DATA_DICTIONARY.md) | Field-by-field type and allowed-value definitions for every tracked CSV |
| [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md) | Raw-vs-processed data separation, provenance-field requirements, missing-data policy, duplicate-publication policy |
| [`SOURCES.md`](SOURCES.md) | Preliminary methodological references, each with its own independent verification note |

---

## Auditability and reproducibility

- **Stable record identifiers.** Every screening-stage record carries a
  `record_id` that is a content hash (DOI, or title+year), not a row
  number — identity survives re-exports and re-ordering. Every extracted
  study carries a sequential `study_id` (`S001`, `S002`, …) assigned in the
  order it cleared full-text screening.
- **Provenance on every extracted statistic**, per `CODEBOOK.md` §11:
  `source_document`, `page`, `table`, `figure`, `section`,
  `exact_location`, `extraction_note`, `researcher`, `date_extracted`.
- **Atomic writes everywhere.** Every script that touches a tracked CSV
  writes to a temp file and `os.replace()`s it, so a crash mid-write can
  never leave a half-written file in place.
- **Schema validation after every batch.** `code/analysis/validate_schemas.py`
  checks every tracked CSV's real header against its documented/generated
  schema (currently 13/13 clean); this is run and its output checked as a
  standard step in every batch of work, not occasionally.
- **Raw vs. processed data are kept separate** (`REPRODUCIBILITY.md` §2):
  `data/raw/` holds untouched exports; `data/processed/` holds
  script-derived versions; raw exports are never overwritten.
  Search-export naming convention:
  `SEARCH_{NNN}_{DATABASE}_{YYYY-MM-DD}.csv` in `01_search/raw_exports/`.
- **A named transformation log** (`09_data_dictionary/transformations/`) is
  where any non-trivial derived statistic's calculation and assumptions
  must be recorded, rather than left implicit.
- **Duplicate-publication policy** (`REPRODUCIBILITY.md` §6): where
  multiple reports describe the same underlying study (conference abstract
  + journal article, working paper + published version, multiple reports
  from the same dataset), the underlying study is treated as one study,
  with the most complete report used for primary extraction and linked
  reports cross-referenced. See also the DOI-formatting duplicate class
  described above, which is a related but distinct failure mode (same
  report, two different `record_id`s, not two different reports of the
  same study).
- **The rule against inventing missing information** governs every phase:
  if an effect size, a risk-of-bias rating, or any other value is not
  actually available from the source material or the correct instrument,
  the field is left blank with a note explaining why — never filled with a
  plausible-sounding guess. See `PROJECT_SPEC.md` §14 and
  `REPRODUCIBILITY.md` §5 for the exact missing-data escalation procedure
  (check supplementary material → repository version → author manuscript →
  working-paper version → contact authors → record the gap explicitly).

---

## Human and AI involvement

This section states plainly which stages were AI-conducted, which involved
independent human review, which still need it, and where a methodological
caveat applies. It is not softened.

**AI-conducted, not yet independently human-reviewed:**
- Title/abstract screening, AI first pass (all 26,222 abstract-bearing
  records) — independently human-reviewed for the 3,665 records that
  reached the second-reviewer queue (see below); the 22,557 straight
  AI-excludes were only spot-checked (120 random + a 74-record targeted
  scan for a known corruption signature), not fully independently
  re-screened.
- Full-text screening, AI first pass (2,276 of 3,659 records assessed so
  far) — independently human-confirmed for **100 of the 1,162 current
  includes only** (S001–S100, as of 2026-09-27). The remaining 1,062
  includes and all 1,114 excludes at this stage are AI-reviewer-only.
- Extraction against the 92-field codebook (1,162 studies) — not
  independently human-reviewed at scale; spot-checking this is recommended
  future work (see **How to continue this project**).
- Evidence classification (mechanism/outcome family assignment) — the
  mechanically-derivable fields are script-generated from the extraction
  record; the judgment-requiring fields are filled by the same AI process
  that did extraction, with reasoning recorded but without independent
  human re-derivation.
- Risk-of-bias tool assignment (1,116 studies) and the 33 existing ratings
  (see **Current project status**) — AI-conducted; none independently
  human-reviewed yet.

**Human-conducted, independent of the AI process:**
- Title/abstract screening, human second reviewer — completed 2026-09-12,
  all 3,665 include+unsure records, by the PI via a spreadsheet handoff.
  **Caveat that must travel with this**: the 99.8% agreement rate with the
  AI first pass is unusually high for genuinely independent screening; this
  was flagged to and confirmed by the researcher before being merged, and
  any manuscript reporting this figure should disclose the caveat alongside
  it, not report the number alone.
- Full-text screening, human second reviewer — **begun 2026-09-27**, 100 of
  1,162 current includes reviewed and confirmed, zero conflicts. This is a
  real, independent confirmation (the PI reviewed the articles and the
  classification, not merely the AI's summary), but it covers 8.7% of
  current includes and 0% of excludes. Do not describe this stage as
  "human-reviewed" without that qualifier.
- Every closure decision recorded in `CHANGELOG.md` as "researcher
  confirmed proceeding" (e.g. the 99.8%-agreement flag, the decision to
  supersede pilot extraction with direct full extraction) — a genuine human
  methodological judgment call, not an AI decision presented as one.

**What still requires independent human confirmation, unambiguously:**
- The remaining 1,062 full-text includes and all 1,114 full-text excludes
  (reviewer_2).
- All 1,162 extractions (no second-extractor pass has been run at all).
- ~1,116 of 1,162 risk-of-bias ratings (only tool-assignment is largely
  done; rating is not).
- A corpus-level Phase 11 quantitative-feasibility write-up (currently
  reasoned only per-effect-size, not per-family).
- Any eventual manuscript's Methods/Limitations sections, which must
  accurately state all of the above rather than a cleaned-up version of it.

---

## Repository map

```
00_admin/            protocol, preregistration, ethics, correspondence
01_search/           database-specific search strings, search logs, raw exports, deduplication
02_screening/        title/abstract and full-text screening, exclusion log
03_extraction/       extraction form, codebook, extracted data
04_quality/          risk-of-bias / appraisal tools and completed appraisals (mostly empty so far)
05_analysis/         descriptive evidence map, effect sizes, meta-analysis, heterogeneity,
                     sensitivity, publication bias (the latter four folders are templates only)
06_outputs/          tables, figures, PRISMA flow diagram, supplementary material
07_manuscript/       draft, revisions, response to reviewers (outline stage only)
08_code/             R and Python analysis code (R code is templates, untested against real data)
09_data_dictionary/  variable definitions and transformation logic
10_reproducibility/  computational environment, version history
11_archive/          superseded material, kept rather than deleted
data/                raw / processed / metadata (canonical machine-readable data)
code/                search / screening / extraction / analysis scripts (these are the tools that
                     actually run; see each subfolder's scripts for the real, executable pipeline)
```

---

## How to continue this project

In roughly this order, for whoever picks this up next:

1. **Keep retrieving and screening full-text PDFs.** 1,383 of 3,659 records
   are still open. Use `code/screening/build_full_text_queue.py` to
   regenerate the retrieval queue, `update_full_text_record.py` or a
   batch-recording script (see recent `CHANGELOG.md` entries for the
   pattern) to record decisions, and always run
   `code/analysis/validate_schemas.py` after each batch.
2. **Extend the human full-text reviewer_2 pass past S100.** This is
   currently the most under-resourced verification gap relative to how
   much AI-reviewed material already exists (1,062 includes, 1,114
   excludes with no human check at all). Prioritize a random or systematic
   sample of the excludes first if full coverage isn't feasible — excludes
   are the harder failure mode to catch later, since an incorrectly
   excluded study simply never appears anywhere downstream.
3. **Do a real risk-of-bias pass**, not more partial pilot judgments,
   against the actual RoB 2 / ROBINS-I / JBI / CASP / MMAT / AMSTAR 2
   instruments in hand — the 29 "partial pilot" ratings from 2026-09-16
   should be revisited and completed, not left as the permanent record.
4. **Run a DOI-variant duplicate audit across the full 27,481-record
   pool**, not just the extracted subset, given three known instances of
   the same paper carrying two `record_id`s. A script that normalizes DOIs
   (stripping URL prefixes, case, and — per the `S063` case above — any
   trailing non-DOI suffix a source export may have appended) before
   matching would catch more of these than exact-string comparison does.
5. **Once each of Families A, B, and C has more than one comparable
   effect-size row, run `ANALYSIS_PLAN.md` §2's decision tree explicitly at
   the family level and write up Phase 11 as its own document** —
   currently the reasoning exists only scattered across individual
   `exclusion_from_pooling_reason` fields.
6. **Only after Phase 11 finds a family eligible**, run the actual
   meta-analysis / sensitivity / publication-bias code in `08_code/R/`
   against real data for the first time, and validate it against a
   hand-calculated check on at least one family before trusting its output.
7. **Update the stale documents** listed in **A warning about stale
   documentation** — `PRISMA_WORKFLOW.md`'s Phase 6+ entries,
   `RISK_OF_BIAS.md` §4, `ANALYSIS_PLAN.md` §13, and the parent
   repository's top-level README's "Companion Project" section — to match
   whatever the live numbers are at that time, or at minimum add a pointer
   to this README's status table if a full rewrite isn't practical yet.
8. **Do not change the research question, the E01–E12 inclusion/exclusion
   criteria, the 92-field codebook, or the planned synthesis approach
   without logging the change, its date, and its rationale in
   `CHANGELOG.md`**, per `PROTOCOL.md` §12. These are the methodological
   rules that must not be silently amended.

---

## Non-negotiable research integrity rules

These bind any contributor to this project, human or AI, without exception:

1. **Never invent missing data** — literature, search results, sample
   sizes, effect sizes, confidence intervals, legal authorities, or a
   plausible-sounding risk-of-bias rating when the source material or the
   correct instrument is not actually in hand. Leave the field blank and
   say why.
2. **Never present assumptions as observed evidence.** Every extracted
   statistic must be labeled `OBSERVED`, `CALCULATED`, `ASSUMED`, or
   `INTERPRETED` (`PROJECT_SPEC.md` §13), and these categories must never
   be blurred — an `ASSUMED` standard error must never be presented
   alongside `OBSERVED` values without the distinction being visible.
3. **Never pool studies merely because their statistics can be
   mathematically converted to a common metric.** Substantive comparability
   — population, mechanism, outcome, institutional context — is a separate,
   prior question that a convertible statistic does not answer.
4. **Never silently overwrite raw data.** `data/raw/` holds untouched
   exports; derived versions go in `data/processed/`, produced by scripts
   in `code/`, never by hand-editing the raw file.
5. **Never hide search or screening limitations.** The SSRN/Westlaw-Lexis
   gap, the HeinOnline/JSTOR delivery failures, the 99.8% reviewer
   agreement, and every other item in **Known limitations and unresolved
   issues** above must appear in any manuscript drawn from this review, not
   be smoothed into a clean-sounding methods paragraph.
6. **Never remove methodological irregularities from the historical
   record.** The 39-batch corruption incident, the corrupted-rationale
   artifact, and the DOI-duplicate cases stay in `CHANGELOG.md` and in this
   README permanently, even after they are fixed — a fixed problem is still
   part of the true record of how this review was actually conducted.
7. **Always record substantive methodological changes in the change
   history**, with a date and rationale, per `PROTOCOL.md` §12 and
   `REPRODUCIBILITY.md` §8 — never as a silent edit to a protocol document
   with no trace of what changed or why.

---

## License

MIT, inherited from the parent repository — see [`../LICENSE`](../LICENSE).
