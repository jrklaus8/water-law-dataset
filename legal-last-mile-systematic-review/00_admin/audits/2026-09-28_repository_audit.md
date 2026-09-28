# Repository audit — 2026-09-28

> **Update, later 2026-09-28: S356 (finding 10) was resolved too.** The researcher supplied the full text; it is a non-systematic OECD policy overview with no method or primary data, so it was excluded as E05 and retired (1,160 → 1,159 included, 1,116 → 1,117 excluded, E05 134 → 135, Legal Framework 448 → 447, abstract-only 70 → 69, blank `reviewer_1` 74 → 73). The record now carries a real full-text reviewer stamp and location. See `CHANGELOG.md`.
>
> **Update, later 2026-09-28: finding 13's merge was approved by the researcher and executed.** All counts
> in this report are **as of audit time (1,162 included studies, 1,114 excludes)** unless stated; the merge
> then reduced them to **1,160 included / 1,116 excluded**, retired one MMAT row (S233) and one Legal
> Framework row (S299), and moved the affected derived figures (tool distribution MMAT 205 / Legal
> Framework 448; 1,148 tool-applicable studies; 70 abstract-only extractions; 247 quantitative-synthesis-eligible).
> The current-status documents carry the post-merge values; this report is kept as the record of what the
> audit saw.

**Scope.** After the corpus-wide risk-of-bias pass, Phase 11 follow-ups, and three Phase 13 SWiM
syntheses were complete, the whole project was audited for (1) claims in documents that no longer
match the live data, (2) integrity between the CSV databases, (3) code health, (4) secrets/PII, and
(5) whether a future reader could reconstruct how the data came to be.

**Important limit on independence.** This audit was performed by the same AI system that wrote most
of the material being audited, working from the CSVs and documents in this repository. It can catch
arithmetic, internal-consistency, and cross-file errors (it caught several of its own). It **cannot**
verify that any extracted value matches its source paper — the source PDFs are not in the environment
— and it is not a substitute for the independent human review still listed as open in `README.md`
(reviewer_2 full-text confirmation, second-extractor pass, human review of risk-of-bias ratings).

**Method.** (Finding 13 came from a second-pass duplicate check added after the numeric review.)
Every number quoted in the current-status documents was recomputed from the live CSVs with
scripts in `code/provenance/audit_and_repair/` (`live_numbers.py` is the main one). Tool names in
`risk_of_bias_tool` were bucketed by the *earliest* tool keyword in the string, because several rows
carry annotation text naming a second tool and substring matching mis-buckets them.

## Findings

| # | Finding | Severity | Status |
|---|---|---|---|
| 1 | Tool-distribution table and several derived figures were wrong in `2026-09-28_evidence_limitations.md`, `README.md`, and `PRISMA_WORKFLOW.md` Phase 9 row | High | **Fixed** |
| 2 | "1,154 studies with an applicable tool / 8 `NONE`" is wrong: it is 1,150 / 12 | Medium | **Fixed** |
| 3 | Family A SWiM synthesis conflated *sign* with *valence*: "18 of 20 (90%)" is really 15 of 20 (75%); its robustness paragraph mixed two different measures | High | **Fixed** |
| 4 | 22 `study_design_class` values in `evidence_map.csv` were stale after later tool reassignments | Medium | **Fixed** |
| 5 | S589's `effect_sizes.csv` row is an unadjusted descriptive comparison for a study `evidence_map.csv` does not flag quantitative-synthesis-eligible | Medium | **Disclosed — needs researcher decision** |
| 6 | "61 + 187 = 248" re-mining arithmetic and "62 rows from 248 eligible studies" wording were inaccurate (S589) | Low | **Fixed** |
| 7 | 71 studies (6.1%) were extracted from abstract/metadata only; no corpus-level disclosure existed | Medium | **Disclosed** |
| 8 | 59 of 140 JBI ratings are "High concern", which means sparse extraction, not poor conduct; not stated in the narrative | Medium | **Disclosed** |
| 9 | 74 decided full-text rows have a blank `reviewer_1`; reviewer labels are inconsistent | Medium | **Open — needs researcher input** |
| 10 | 13 decided full-text rows still carry `full_text_status = not_retrievable`; one (S356) is an include decided without a recorded reviewer or full text | Low–Medium | **Open — needs researcher input** |
| 11 | One-off scripts cited by `CHANGELOG.md` existed only in an ephemeral scratchpad; `title_dup_results.txt` was cited but not in the repo | Medium | **Fixed** (earliest work remains unarchivable — disclosed) |
| 12 | Three `preliminary_*` outputs describe a 509-study snapshot with no superseded banner | Low | **Fixed** |
| 13 | **Two papers were double-counted among the 1,162 included studies** (S233/S1008 and S299/S392); the earlier "zero live double-counting" conclusion was wrong | **High** | **Fixed — merged with the researcher's approval; 1,162 → 1,160** |
| 14 | Extraction is per report, not per underlying study: 4 documented pairs share underlying data (2 fully, 2 partly), so "5 RoB 2 studies" are 4 trials; no machine-readable links existed | Medium | **Disclosed + linked (`linked_reports_2026-09-28.csv`); recount is a researcher decision** |
| 15 | Family C SWiM said the ownership cluster spans "three countries" and "three independent studies"; it is two countries, and S526/S539 samples probably overlap | Medium | **Fixed (text)** |
| 16 | No study↔record index existed (extraction database has no `record_id` column) | Low | **Fixed** (`study_record_map.csv`) |

### 1 and 2 — Wrong tool distribution and derived figures (fixed)

Live values (sum 1,162): Legal Framework **449** (38.6%), CASP **263** (22.6%), MMAT **206** (17.7%),
JBI **140** (12.0%), ROBINS-I **63** (5.4%), AMSTAR 2 **24** (2.1%), NONE **12** (1.0%), RoB 2 **5**
(0.4%). The documents had 433/245/207/166/72/22/12/5 (evidence-limitations table) and
425/245/207/166/63/22/12/5 (README, PRISMA_WORKFLOW), the latter summing to 1,145, not 1,162 — a
visible sign something was off. Root cause: figures written from mid-session snapshots before the
last reassignment batches finished, plus an early substring-matching helper. Derived claims corrected:
causal-capable designs 77 (7%) → **68 (6%)**; Legal Framework measurement-quality fields populated
365/433 (84%) → **389/449 (87%)**; CASP+MMAT 452 (39%) → **469 (40%)**; "roughly 1,050" studies rated
by CASP/MMAT/Legal Framework → **918**; Legal Framework net change 573 → 433 → **573 − 148 + 24 = 449**
(the 24 = 9 reverted after an over-correction + 8 from the unassigned batch + 6 JBI mis-tags + 1 other);
the Legal Framework batch document covers 434 studies (425 + a 9-study follow-up), and the other 15
were appraised more thinly in other batches. "1,154 rated" → **1,150** tool-applicable studies, all
rated; of the 12 `NONE` studies, 4 carry an explicit NOT APPLICABLE note and 8 have a blank rating by
design. **No conclusion changed**; two caveats (few causal-capable designs; the CASP/MMAT
"Can't tell" gap) got slightly stronger. Historical dated annotations in `RISK_OF_BIAS.md` and
`CHANGELOG.md` were left as written, with a dated correction note appended.

### 3 — Family A: sign versus valence (fixed)

Vote counts in the three SWiM syntheses are arithmetically right *as counts of the sign of each
study's extracted association* (A 12 Positive / 6 Negative / 2 Null; B 5 Positive / 1 Mixed; C 7 / 9 / 4
Mixed). But Family A's text treated "Positive + Negative" as "recognition helps access" (18 of 20,
90%) while its own next sentence named S1020 and S104 as running counter to that pattern — and S1121
does too. Recounted by substance: **15 concordant (75%), 3 counter-pattern (S104, S1020, S1121), 2
null.** The robustness paragraph's "drops to 10/18 (56%)" mixed the positive-only share with the
discarded sign-sum; on the corrected count, dropping S358 and S404 gives 13/18 (72%) and also dropping
S589 gives 12/17 (71%), so the family-level pattern is not fragile to those coding decisions. Family C
now carries an explicit caution that its 7/9/4 split is a *sign* count that must not be read as
"beneficial vs adverse" (S539/S749 are Positive but worse for affordability; S471/S1038 are Negative
but better), and that a valence-normalized recount is deliberately not offered because the
beneficial/adverse assignment for exposures like "private ownership" is a normative call the protocol
does not make. All three documents now state that direction categories were assigned from each study's
full direction text, naming the judgment calls (S358, S404, S294, S879, S1062).

### 4 — Stale `study_design_class` (fixed)

The 2026-09-28 normalization ran before the JBI→CASP reassignments finished. 22 studies (19 CASP, 1
MMAT, 2 AMSTAR 2) were re-synced to the value their tool implies. Details:
`05_analysis/descriptive/study_design_class_normalization_2026-09-28.md`, addendum.

### 5 — S589 (open; researcher decision)

`effect_sizes.csv` row S589 (Family A, Ecuador) records "descriptive group comparison (unadjusted…)",
while the file's own stated bar is regression-based estimates isolating a mechanism, and
`evidence_map.csv` has `quantitative_synthesis_eligible = FALSE` for it. It is the only such row of 62.
**Not changed**, because either fix moves published counts. Options: (a) remove the row (Family A 20 →
19; total 62 → 61; update README, three SWiM/Phase 11 documents) — the option this audit recommends,
since the row fails the file's own inclusion standard; or (b) keep the row and flip the flag, with a
provenance note explaining the exception. The Family A synthesis already discloses the issue and shows
the counts with S589 dropped.

### 7 and 8 — Abstract-only extractions; JBI "High concern" (disclosed)

71 studies' `extraction_note` says they were extracted from the abstract, introduction, or repository
metadata only (CASP 30, MMAT 14, JBI 11, Legal Framework 10, AMSTAR 2 5, RoB 2 1). Their appraisals
are honest (CASP entries record "Can't tell" on 6–8 of 10 items; S366's RoB 2 is labelled
LOW-CONFIDENCE), but the limitation appeared only in scattered `CHANGELOG.md` entries. It is now in
`2026-09-28_evidence_limitations.md`. A sensitivity analysis excluding these 71 is straightforward
later (filter on `extraction_note`) and is recommended before any synthesis leans on them. **Follow-up:** the
70 that remain after the duplicate merge are listed in
`05_analysis/sensitivity/abstract_only_extractions_2026-09-28.csv`, and none of them has an `effect_sizes.csv`
row, so the SWiM syntheses and any future pooling are untouched by this limitation; it bears on the
descriptive counts, mechanism/context tabulations and risk-of-bias ratings only.

### 9 — Blank `reviewer_1` on 74 decided rows (open)

Of 2,276 decided full-text rows, **74 (48 include, 26 exclude) have no `reviewer_1` value** and none has
a `reviewer_2`. In addition, `reviewer_1` uses several labels for the same AI reviewer: date-stamped
`Claude-AI-fulltext-YYYY-MM-DD` (most rows), plain `Claude` (501), `claude_sonnet_5` (60), and lowercase
`claude` (18). Who or what made those 74 decisions cannot be reconstructed from the repository;
nothing was back-filled, because a guessed value would be fabricated provenance. Suggested handling:
route the 74 to the reviewer_2 queue as a priority, and normalize the label variants only with a
documented mapping (they do not change any decision).

### 10 — Stale `full_text_status` on 13 decided rows (open, low priority)

Eight includes (extracted as S559–S570; six with a populated location, two French-language papers
without) have detailed extraction notes documenting the papers' content, so their `not_retrievable`
status is stale; four excludes carry substantive exclusion reasons (E01/E04)
but a leftover retrieval note. Status is loosely maintained across the file (432 decided rows have a
blank status), so this is a hygiene issue rather than a decision error, with **one exception — the ninth
include, R1827C03DA45A
(S356, "Economic regulation of water supply and sanitation services")** is an include with no
`reviewer_1`, no location, the note "No OA copy found via Unpaywall", and an extraction note saying it
was extracted from abstract/introduction text only. Under the project's own rule (E10, inaccessible full
text) that record should be either excluded/unretrieved or explicitly retained as an abstract-level
include; the researcher should decide. It is not changed here.

### 13 — Two live double-counted papers (merged with researcher approval)

A language-agnostic check of the 1,162 extracted studies — same year plus shared author surnames plus
title-token overlap, then title-only Jaccard ≥ 0.6, then DOI equality — found two papers each counted
under two `record_id`s, both records `include`, both extracted:

| Pair | Paper | Records | Why the earlier audits missed it |
|---|---|---|---|
| **S233 / S1008** | Morales & Zambrano (2018), *Población y Salud en Mesoamérica* 16(1), DOI 10.15517/psm.v1i1.32031 | `RFEFB1427701B` / `RB26ACD9EDC54` | English vs Spanish title (no shared tokens); one record has a blank DOI |
| **S299 / S392** | Minaverry (2017), *Tecnología y Ciencias del Agua* 8(1):5-20, DOI 10.24850/j-tyca-2017-01-01 | `R7896D097B364` / `R56D409CF27A6` | one title carries a bilingual `[translation]` suffix, dropping token-Jaccard below 0.75; one record has a blank DOI field |

The DOI-variant audit compares DOI strings and cannot see a blank; the title audit's 0.75 token-Jaccard
threshold cannot match across languages. Both are inherent method limits, now stated in the
title/author audit document with a correction banner (its "zero live double-counting" headline was
wrong). The pairs are also **classified inconsistently**: S233 is flagged
`quantitative_synthesis_eligible = TRUE` (mechanism `DISCRETION_ACCOMMODATION`) while its twin S1008 is
`FALSE` (mechanism `legal_status`), so the 248 eligible-study count and the mechanism-family tabulations
each count this paper differently depending on which row is read. Neither pair has an `effect_sizes.csv`
row, so no pooled or SWiM figure is affected. Two other same-author-team pairs that surfaced
(S175/S891, S427/S1158) were checked and are different papers.

**What was done.** First the four extraction-note and four screening-note fields were annotated
`PROBABLE LIVE DUPLICATE` (`annotate_live_duplicates_2026-09-28.py`) and the decision was put to the
researcher, because the merge changes published counts. The researcher then approved the merge, which
was executed by `code/provenance/audit_and_repair/merge_live_duplicates_2026-09-28.py` following the
project's `S399` → `S102` precedent (retire one row, leave a permanent gap in the study-ID sequence, record
the retired screening record as an `E08` duplicate exclusion):

| | Kept | Retired | Basis for keeping |
|---|---|---|---|
| Pair 1 | **S1008** (record `RB26ACD9EDC54`) | S233 (record `RFEFB1427701B`) | full-text-based extraction (45 vs 35 populated fields), DOI, sample size, table/section locations; S233 was abstract-level |
| Pair 2 | **S392** (record `R56D409CF27A6`) | S299 (record `R7896D097B364`) | fuller full-text-based extraction and appraisal note; S299 was abstract/metadata-only |

Effects: extraction and evidence-map rows 1,162 → 1,160; full-text includes 1,162 → 1,160 and excludes
1,114 → 1,116 (E08 6 → 8; two new `exclusion_log.csv` rows attributed to `Claude-AI-audit-2026-09-28`);
quantitative-synthesis-eligible 248 → 247 (S233 was flagged eligible from its abstract; the kept S1008's
full-text coding is not eligible, and that coding was retained); qualitative-eligible 1,062 → 1,060; tool
distribution MMAT 206 → 205 and Legal Framework 449 → 448. **Nothing was overwritten in a kept row** except
that S392's blank DOI was filled from S299 (a bibliographic fact recorded in the retired record); no
judgement codings were carried across. S233's abstract-level effect estimate and its
`discretion_accommodation` coding are preserved in S1008's extraction note so nothing is lost. The
retired screening records' `reviewer_1` now reads `Claude-AI-audit-2026-09-28` (the original
`Claude-AI-fulltext-2026-09-15` stamp and include decision are recorded in each record's notes and in git
history), so the current decision is not attributed to a reviewer who did not make it. `effect_sizes.csv` was
untouched. Note that the kept S392 record has no `reviewer_1` and a stale `oa_page_candidate` status — one of
the hygiene items in findings 9 and 10 — and was not altered beyond the merge note.

### 14 — Reports versus studies (linked; recount is a researcher decision)

`REPRODUCIBILITY.md` §6 requires that several reports of one underlying study be treated as one study and
cross-referenced by `study_id`; the project instead extracted companion papers as separate rows (a precedent
disclosed in S369's note) and recorded the relationship only in free-text notes. The audit gathered every
explicit "companion / same trial / same fieldwork" statement and added inferred candidates (same author team +
same country + same period) into `03_extraction/extracted_data/linked_reports_2026-09-28.csv`: **12 links, 8
extractor-documented and 4 audit-inferred (marked low confidence, unverified against the source papers)**.
Definitely the same underlying data: **S294/S366** (one cluster-randomised trial in rural DRC, two outcome
reports) and **S097/S098** (one interview sample). Partly overlapping: S681/S682 (overlapping fieldwork) and
S357/S369 (one programme, earlier vs later report). The rest are same-author-team pairs with distinct data
(S008/S009, S541/S542, S761/S763, S794/S803) or inferred candidates (S526/S539, S175/S891, the Kooy & Bakker
Jakarta papers). Consequences: the 1,160 rows are roughly **1,158 distinct studies on the definite links, 1,156
counting the partial ones**, and the **5 RoB 2 "studies" are 4 trials** (S057, S085, S294/S366, S879). No
linked pair has both members in `effect_sizes.csv` except the audit-inferred S526/S539. Cross-reference
notes were appended to the six extraction rows of documented pairs that lacked them; **nothing was merged or
recounted**, because unlike the exact duplicates in finding 13 these are different papers reporting different
results, and how to treat them (collapse for counting, keep separate for extraction, link only) is a
methods decision for the researcher.

### 15 — Family C text errors and the S526/S539 independence question (fixed)

The Family C synthesis said the ownership cluster (S526, S539, S749) spans "three different countries (US ×2,
Brazil)" — it is two — and `phase11_pooling_feasibility_S526_S539_S749.md` called them "three independent
studies in three different national contexts". Corrected in both. S526 (1,183–1,189 US utilities serving
40,000+) and S539 (the 500 largest US community water systems) very probably sample overlapping utilities, so
the ownership finding rests on two effectively independent samples (US, Brazil), not three; this is an
inference from the extracted sample descriptions, disclosed as such. The cluster's "5 of 5 same direction"
paragraph was also tempered (S471 attenuates to non-significance under full covariate adjustment; whether
"mayor-led" is the more "accountable" structure is an interpretive reading; and it now says explicitly that this
is a substantive judgment, consistent with the sign-versus-valence caution added earlier).

### 16 — Study↔record index (fixed)

`03_extraction/extracted_data/study_record_map.csv` links each of the 1,160 extraction rows to its screening
`record_id` (992 by the record_id in the row's note, 122 by DOI, 41 by title, 5 by hand) — a bijection with the
1,160 full-text includes — plus the two retired duplicates. The links were sanity-checked: all 30 low
title-overlap cases were translated titles of the same paper, and the 27 year differences were ±1-year
online-first/issue gaps apart from five same-title cases (e.g. S931's screening record says 2025 for a
2010 chapter — a source-metadata error, not a wrong link).

### Other sweeps that found nothing to fix

Effect-size numeric consistency (no lower > upper, estimate outside CI, or negative SE among the few rows that
carry them; only 4 rows have a CI and 6 an SE — the file is mostly free-text estimates by design); boolean-field
formats in the extraction database (all `TRUE`/`FALSE`/blank; three `migrant_population` values carry annotation
text and were left); no shared DOI across extraction rows; no shared journal+volume+page+year; the one blank
`adjusted` value (S312) is genuinely unrecorded in the extraction and was not inferred.

### 11 — Provenance scripts (fixed, with a disclosed gap)

542 scripts and two raw output files (6.0 MB) are archived in `code/provenance/` with a README that
explains they are a historical record, not a runnable pipeline. Scanned for credentials and contact
details (none); all 542 parse. **Gap:** the archive starts at `record_batch64` and study S532;
earlier work has no surviving script, only `git log` and `CHANGELOG.md`.

## Checks that passed

- Headline screening numbers: 27,481 records; 3,659 title/abstract includes / 6 excludes; 2,276 of 3,659
  full-text decided (1,162 include / 1,114 exclude); 1,383 undecided, all `not_retrievable` (1,201) or
  `wrong_file_retrieved` (182); exclusion log has 1,114 rows; `reviewer_2` confirmed on 100 includes.
- ID integrity: `extraction_database.csv` and `evidence_map.csv` hold the same 1,162 study IDs;
  every `effect_sizes.csv` ID exists in both (62 unique studies, no duplicates). Each of the 1,162
  full-text includes maps to one extraction row (994 by record ID in the extraction note, 54 by DOI,
  109 by title match, 5 resolved by hand — accent/spelling variants); no DOI appears on two
  extraction rows. Note the extraction database has **no `record_id` column** — the link lives only in
  free-text notes for most rows, which is what made finding 13 hard to see; adding one is recommended.
- Recomputed and found correct: `mechanism_certainty` distribution, top-country and legal-system
  shares, the ROBINS-I (54 Moderate / 9 Serious) and RoB 2 (5 × Some concerns) rating counts, the
  effect-size family counts (A 20 / B 6 / C 20 / 16 reasoned non-fits; all `included_in_pooled_estimate
  = FALSE`).
- Code: all 45 tracked Python files and all 542 archived scripts parse; the three R templates were
  test-run earlier the same day against a synthetic fixture (four `sprintf` bugs found and fixed then).
- Secrets/PII: none in tracked files or the archived scripts. No PDFs are tracked.

## Decisions needed from the researcher

*(The finding-13 merge decision was made and executed — see above.)*

1. **S589** — remove the row (recommended) or keep it and flip the eligibility flag (finding 5).
2. **The 74 blank-`reviewer_1` rows** — who screened them, and whether to prioritize them for
   reviewer_2 (finding 9).
3. ~~**S356**~~ — resolved: full text supplied and read; excluded as E05 (finding 10).
4. Whether to require a sensitivity analysis excluding the 70 abstract-only extractions (71 at audit time) before any
   synthesis statement is published (finding 7).
5. **Linked reports** (finding 14) — collapse, keep-and-link, or leave as is: S294/S366 and S097/S098 are the
   same underlying data (1,158 distinct studies); adding S681/S682 and S357/S369 gives 1,156.

Already on the researcher's earlier to-do list and unchanged by this audit: reviewer_2 human pass
(100 of 1,162 confirmed), the `mechanism_family`/`outcome_family` taxonomy decision, OSF
preregistration, PRISMA items 25/26, and item-wording verification against the publisher checklists.
