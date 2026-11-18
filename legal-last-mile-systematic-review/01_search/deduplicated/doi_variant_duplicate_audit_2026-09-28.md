# DOI-variant duplicate audit across the full 27,481-record pool — 2026-09-28

Closes `README.md`'s "How to continue this project" item 4: "Run a DOI-variant duplicate audit
across the full 27,481-record pool, not just the extracted subset, given three known instances
of the same paper carrying two `record_id`s. A script that normalizes DOIs... before matching
would catch more of these than exact-string comparison does."

## Method

Ran against `01_search/deduplicated/deduplicated_records.csv` (27,481 records, the full
post-merge search pool — not just the 1,162 extracted studies). For each of the 14,076 records
with a non-empty `doi` field:

1. **Normalized** each DOI: lowercased, whitespace-stripped, and stripped of common URL/prefix
   wrappers (`https://doi.org/`, `http://dx.doi.org/`, `doi:`).
2. **Exact-match pass**: grouped by normalized DOI, looking for two or more distinct
   `record_id`s sharing one normalized DOI.
3. **Prefix-match pass**: sorted all normalized DOIs lexicographically and checked, within a
   sliding window of nearby entries, whether one DOI is a strict prefix of another — the exact
   corruption pattern already documented for the S063 case (`.../territorios/a.9931` vs.
   `.../territorios/a.9931vol462021`, an extra suffix concatenated with no separator, which
   exact-string or simple URL-stripped matching cannot catch).

## Result: zero new exact-match duplicates; one new, already-correctly-resolved prefix-match case found; the rest are false positives from the method itself, disclosed rather than hidden

**Exact-match pass: 0 duplicate groups.** No two distinct `record_id`s share an identical
normalized DOI anywhere in the 27,481-record pool — the original search-phase deduplication
already caught every exact-DOI duplicate.

**Prefix-match pass: 40 candidate pairs**, none of which turned out to be a new, unresolved
duplicate. Manually reviewing all 40 (title, authors, year, database for each) sorts them into
three categories:

1. **~20 pairs are book-DOI/chapter-DOI parent-child relationships** — legitimate publisher DOI
   conventions (e.g. Springer/Routledge assign a book DOI like `10.1007/978-3-540-76707-7` and
   then append `_11`, `_15`, `_16` etc. for each chapter). These are genuinely distinct citable
   works with different titles and often different authors, correctly represented as separate
   records. **Not duplicates** — a prefix relationship here reflects publisher DOI hierarchy,
   not the same paper indexed twice.
2. **4 pairs are coincidental numeric-string prefix collisions** in journals that assign
   sequential numeric DOI suffixes (e.g. `10.1057/dev.2011.6` is, as a *string*, a prefix of
   `10.1057/dev.2011.67` purely because "6" prefixes "67" — these are article numbers 6 and 67
   in the same journal issue sequence, unrelated papers with different titles and authors).
   **A known limitation of prefix-matching on this kind of data**, disclosed here rather than
   silently filtered: any future re-run of this method should additionally require a
   non-numeric-suffix check, or title-similarity confirmation, before treating a prefix match
   as a real candidate.
3. **16 pairs involve one single record with a corrupted/truncated DOI**: `RCD78B89FE287`
   ("Egypt: Building an Information Society for International Development," ProQuest, 2003)
   carries `doi = https://doi.org/10.1080/07` — a DOI truncated after the registrant prefix,
   evidently a data-capture error in the original ProQuest export. This spuriously
   prefix-matches against unrelated papers whose real DOIs happen to start `10.1080/07...`.
   **This record was already excluded at title/abstract screening (E01, wrong topic) before
   this audit**, so the truncated DOI had no downstream effect on any inclusion/exclusion
   decision — but it is recorded here as a genuine, disclosed data-quality defect in
   `deduplicated_records.csv`, not silently ignored because it happened not to matter this
   time.

**Two of the 40 pairs are genuine same-paper duplicates**, both already known to this project,
not new discoveries — which is itself useful confirmation that the pipeline's downstream
duplicate-catching discipline works even where the search-phase automated dedup missed them:

- **R7EECD84CD3AA / RF043AAD78E8E** (Metropolitan water-access study) — the already-documented
  S063 case (`CHANGELOG.md`, "Post-hoc duplicate-detection audit," and the 2026-09-27
  reviewer-matching entry). Finding it again here is exactly the validation this audit's
  method needed: it recovers a duplicate that plain exact-string DOI matching could not.
- **R6ABD0B221622 / RD9FA1D5723A2** ("How a water trucking governance mechanism in the West
  Bank enhances equity and sustainability," Cesari et al.) — **not previously listed in
  `README.md`'s "at least three known cases" inventory, but already correctly caught and
  resolved at the full-text screening stage**, well before this audit ran:
  `full_text_screening_database.csv` already documents RD9FA1D5723A2 as excluded (E08,
  duplicate publication) and cross-referenced to R6ABD0B221622, with the reviewer's own note
  explaining the mechanism — Practical Action Publishing appends an "OA" suffix to a paper's
  DOI when it re-publishes the final open-access version (`...18-00036` in 2019 vs.
  `...18-00036OA` in 2022, same title/authors/abstract), which the search-phase DOI-match
  deduplication did not catch because the DOIs are not identical. `REPRODUCIBILITY.md` §6 is
  cited in that record's own exclusion note as the governing rule. **No correction was needed
  here** — this audit found that the pipeline had already handled this case correctly, four
  months before this dedicated audit ran, via ordinary full-text screening discipline rather
  than an automated DOI check. It is still added to the known-cases inventory below, since
  `README.md` did not previously list it.

## What this means for `README.md`'s "at least three known cases" claim

`README.md`'s **Known limitations** item 7 should be read as **at least four** known cases now,
not three: S227 (duplicate of S063), the `record_id`-level R7EECD84CD3AA/RF043AAD78E8E pair
(same S063 case, found via a different mechanism), and now this audit's confirmation of the
R6ABD0B221622/RD9FA1D5723A2 West Bank water-trucking pair (already resolved, previously
undocumented at the README level). See `CHANGELOG.md`'s 2026-09-28 entry and the updated
README bullet.

## What this audit does not do

This audit is a `record_id`-level DOI check against `deduplicated_records.csv`'s `doi` field
only. It does not re-check title-based duplicate detection (two records with different DOIs —
say, a preprint DOI and a final-publication DOI — describing the same underlying paper would
not be caught by this method at all, only by a title/author-similarity pass, which this audit
did not run at the 27,481-record scale). It also does not guarantee every DOI-truncation or
DOI-corruption artifact in the pool has been found — only that the specific `RCD78B89FE287`
case surfaced as a byproduct of the prefix-match pass. A future researcher wanting a more
exhaustive duplicate audit would need a fuzzy title/author-similarity pass across all 27,481
records, which is a substantially larger undertaking than this DOI-focused check.
