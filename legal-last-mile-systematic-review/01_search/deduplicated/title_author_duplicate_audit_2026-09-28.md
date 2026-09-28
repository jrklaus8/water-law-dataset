# Title/author-similarity duplicate audit across the full 27,481-record pool — 2026-09-28

Follow-up to `doi_variant_duplicate_audit_2026-09-28.md`, which explicitly named its own
limit: a DOI-only method cannot catch a same-paper duplicate indexed under two unrelated DOIs
(a preprint vs. a final publication, or a working-paper repository entry vs. a journal
indexing). This audit closes that specific gap using title and author similarity instead.

## Method

Ran against the same 27,481-record `01_search/deduplicated/deduplicated_records.csv` pool.

1. **Normalized** each of the 27,481 titles: lowercased, stripped of punctuation, collapsed
   whitespace, and reduced to a content-word token set (a short, disclosed stopword list
   removed generic words like "the," "of," "water," "sanitation," "access," "study" — chosen
   because this corpus's titles are saturated with those specific terms, which would otherwise
   dominate every similarity score and hide genuine differences).
2. **Pass 1 (exact match)**: grouped records by their exact normalized title string — catches
   the same title reproduced with different capitalization/punctuation across databases.
   **165 duplicate-title groups found.**
3. **Pass 2 (near-duplicate)**: blocked records by (publication year, alphabetically-smallest
   content token) — checking year, year−1, and year+1 to catch preprint/final-publication year
   drift — then computed Jaccard token-set similarity within each block, at a 0.75 threshold.
   **125 further candidate pairs found**, none overlapping Pass 1's exact matches.

**290 total candidate groups/pairs** — far more than the DOI audit's 40, because most of this
corpus's cross-database duplication (ProQuest re-indexing a Scopus record, Sociological
Abstracts re-indexing a ProQuest record, a working paper vs. its published version) does not
carry a shared or even similar DOI at all.

## The central finding: zero live double-counting, checked exhaustively

> **Correction, 2026-09-28 (later the same day, repository audit —
> `00_admin/audits/2026-09-28_repository_audit.md`, finding 13).** The headline below is
> **wrong for two cases**. A language-agnostic author/year/citation check across the 1,162
> extracted studies found two papers counted twice: **S233 / S1008** (Morales & Zambrano 2018)
> and **S299 / S392** (Minaverry 2017). This audit's token-Jaccard method (threshold 0.75)
> cannot match a pair whose titles are in different languages (S233/S1008) or where one title
> carries a bilingual `[translation]` suffix and one record's DOI field is blank
> (S299/S392) — an inherent limit of the method that the "What this audit does not do"
> section only partly anticipated. The two pairs are annotated, not merged, pending the
> researcher's decision. The text below is preserved as the record of what this audit
> concluded; read it with this correction.

**For every one of the 290 candidate groups, checked against `full_text_screening_database.csv`'s
`final_decision` field: no group has two or more members both currently `include`.** This was
checked two ways — first restricted to the 165 exact-title groups, then separately across all
125 near-duplicate pairs — and both checks returned zero. **This corpus's 1,162 included,
extracted studies do not currently double-count any paper under two different `record_id`s
via a title-based duplicate this audit can detect.**

## What the 290 candidates actually are

Manually sorting all 290 into categories (title text, authors, and status all reviewed, not
just counted):

### 1. Already-correct: one included, the duplicate genuinely never retrieved (5 records, 3 clusters)

The most operationally interesting finding. In 3 cases, the same underlying paper is indexed
2–3 times in the 27,481-record pool; one indexing was successfully retrieved and included;
the other 1–2 indexings sit among the 1,383 records Phase 6 formally closed as
`not_retrievable`/`wrong_file_retrieved`:

- **Coville, Galiani, Gertler & Yoshida, "Financing Municipal Water and Sanitation Services in
  Nairobi's Informal Settlements"** — included as `R4D81D56EA98B` (Scopus 2025, final study
  S879). Two further indexings, `RF25B3781B68F` (ProQuest 2020) and `RA62BAA92506A` (ProQuest
  2021), never retrieved.
- **Taing, "Policy implementation considerations for basic services: A South African urban
  sanitation case"** — included as `RAE15E6363DF0` (Scopus 2019). A further indexing,
  `R80C0C7C65752` (Scopus 2020), was retrieved but the wrong file arrived (already documented
  in that record's own notes before this audit) and was never re-attempted before Phase 6
  closed.
- **McCullough, "Square Peg, Round Hole"** (Ontario First Nations drinking water
  infrastructure dissertation) — included as `R05D446594BE6` ("...First Nations Drinking
  Water Infrastructure and Federal Policies, Programs, and Processes," ProQuest Sociological
  Abstracts 2012). Two further indexings under a longer, differently-worded title
  (`R962EAA5E4835`, `R40E7D0B743D0`, ProQuest 2011/2012) never retrieved.

**Each of these 5 not-retrieved records' `notes` field in `full_text_screening_database.csv`
has been annotated** (this audit, 2026-09-28) to disclose the probable duplication — without
changing `full_text_status`, `full_text_decision`, or `final_decision`, since none of these 5
records' own full text was ever actually retrieved and directly compared; the match is on
title and author only, strong but not the same standard of evidence used for the
already-retrieved-and-compared cases below. **This means a small number of the 1,383
"permanently unretrieved" records represent no additional lost evidence beyond what the
corpus already captured under the paper's other, included indexing** — a genuinely positive,
disclosable nuance to the headline 1,383 figure, not previously stated anywhere in this
project's documentation.

### 2. Already correctly resolved via full-text-stage E08 exclusion (2 clusters, 1 newly surfaced)

- **West Bank water-trucking governance paper** (Cesari et al.) — already found and documented
  via the DOI-variant audit (`doi_variant_duplicate_audit_2026-09-28.md`); confirmed again
  here independently via title matching.
- **Thapa, Farid & Prevost, "Governance Drivers of Rural Water Sustainability"** (PAMSIMAS
  Indonesia study) — **newly surfaced by this audit, not by the DOI audit**, because the
  duplicate record (`R346D1BF8F31D`, 2021 ProQuest) carries no DOI at all, only a URL — a DOI
  audit has no signal to work with here at all. `full_text_screening_database.csv` shows this
  was already correctly caught during full-text screening (`R346D1BF8F31D` excluded E08,
  cross-referenced to the included `RC41D17900D05`), months before this audit ran. No
  correction needed; added to the known-cases inventory below.

### 3. Inert leftover records from the abandoned exploratory pilot (9 title matches, no action needed)

9 of the exact-title matches pair a `WebSearch(general)` record — from the non-systematic,
low-recall exploratory pilot round (`SEARCH_003`–`SEARCH_017`, 2026-08-25, `PRISMA_WORKFLOW.md`
§3) that explicitly never counted toward the systematic search — against the real,
systematically-retrieved record for the same paper. Checked: every one of these 9
`WebSearch(general)` records has a **blank `title_abstract_decision`** in
`screening_database.csv` — they were never screened at all, consistent with the pilot's
disclosed out-of-scope status. They sit inertly in `deduplicated_records.csv` but never
entered the screening pipeline as competing decisions. No action needed; noted here as
confirmation that the pilot's disclosed non-participation in Phase 3 held in practice, not
just on paper.

### 4. Everything else: genuinely distinct works or an unresolved-but-not-live pair (274 of 290)

- **~15 groups are recurring generic section-header titles** — "Introduction," "Discussion,"
  "Editorial," "Bibliography," "Reviews," "Who's Who," "News Briefs," "Rating Changes" — shared
  by unrelated books/journal issues across different years, authors, and publishers. Confirmed
  false positives from title-only matching; not duplicates.
- **A recurring pattern of periodic/annually-refreshed report series** (market-research
  "Strategic SWOT [and Financial/PESTLE] Insights" reports on named utilities, "Company
  Capsule" profiles, recurring financial news-wire headlines like "SJW announces dividend")
  appear identically titled across adjacent years in ProQuest's business-database content.
  These are a real, disclosed characteristic of this corpus's grey-literature/financial-news
  component — the same report title genuinely republished with updated content each cycle —
  not duplicate indexing of one document. None of these reached title/abstract inclusion
  (verified: this is business/financial-database noise from `SEARCH_040`'s ProQuest pull, not
  literature this review's E01–E12 criteria would ever include), so this pattern has no
  operational consequence, but is disclosed here rather than left as an unexplained "165
  duplicate groups" headline number without an honest accounting of what they actually are.
- **The remaining groups** are genuine same-paper duplicates (preprint/final-publication pairs,
  cross-database re-indexing) where **neither** copy has yet reached `include` at the full-text
  stage — most sit among the 1,383 unretrieved, a handful are still genuinely pending. These
  are not currently operationally relevant (no live decision depends on resolving them), and
  are not individually itemized here; the method and full candidate list
  are reproducible from this document's own method section, and the raw candidate-pair
  output plus the scripts that produced it are archived at
  `code/provenance/audit_results/title_dup_results.txt` and
  `code/provenance/audit_and_repair/title_dup_*.py` (added by the 2026-09-28 repository audit).

## Updated known-duplicate-cases count

`README.md`'s "Known limitations" inventory (already at "at least four" after the DOI audit)
is updated to **at least five**: adding the Thapa/PAMSIMAS case found here. The true count is
almost certainly higher still — this audit is thorough but not exhaustive (see below).

## What this audit does not do

- **Cross-language duplicates.** Bilingual or translated titles fall below the token-similarity
  threshold; two live cases were later found this way (see the correction at the top).
- It is still a **title/author-similarity method**, not a semantic or full-text comparison. A
  same-paper duplicate with a substantially reworded title (a book chapter adapted from a
  journal article, say) would not be caught by either pass.
- The 0.75 Jaccard threshold and the specific stopword list are disclosed choices, not
  validated against a ground truth — a lower threshold would likely surface more of the
  "everything else" category's genuine duplicates at the cost of more false positives from the
  report-series/generic-title patterns already identified.
- This audit, like the DOI-variant audit before it, checked the full 27,481-record pool, but
  neither one is a substitute for a human duplicate-detection pass on the subset that matters
  most: the 1,162 currently-included studies' own reference lists and citation records, which
  neither method touches at all.
