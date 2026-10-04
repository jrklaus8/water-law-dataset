# Cross-Cutting Evidence Limitations — 2026-09-28

## Status of this note

This supersedes `2026-09-16_evidence_limitations.md`, which was explicitly a placeholder —
written when only 12 of what was then a 366-study corpus had been appraised at all, with its
own "Overall confidence" section deliberately left blank pending real ratings. As of today,
`risk_of_bias_tool` is correctly classified for all 1,160 extracted studies (1,162 when this note was first written; two duplicates were merged and S356 excluded on full text later the same day, see the audit caveat at the end), and every study
for which a rating is possible has one (see `RISK_OF_BIAS.md` §4 and `CHANGELOG.md`'s
2026-09-28 entries for the full account of how). This narrative is therefore the first
version of this file that can actually do what `RISK_OF_BIAS.md` §3 asks: summarize
limitations of the evidence base **as a whole**, informed by real ratings rather than corpus
composition alone.

**Audit correction, 2026-09-28 (later the same day).** A repository-wide audit recomputed every
figure in this narrative against the live `extraction_database.csv` and found that the
tool-distribution table, several percentages, and the Legal Framework counts had been written
from mid-session snapshots taken *before* the later reassignment batches finished (and, in one
case, from a tool-classification helper that matched tool names by substring and so mis-bucketed
rows whose annotation text mentions a second tool). The figures below are the recomputed live
values (method: earliest tool keyword in `risk_of_bias_tool`); the affected sentences are edited
in place with the earlier figure recorded in parentheses where it changes a claim, and the full
account is in `CHANGELOG.md`'s audit-correction entry and
`00_admin/audits/2026-09-28_repository_audit.md`. None of the corrections changes a conclusion:
every qualitative caveat below survives, and two (the causal-capable share and the CASP/MMAT
share) get slightly stronger, not weaker. **A later same-day duplicate merge** (S233 → S1008, S299 → S392, with the researcher's approval) reduced the corpus from 1,162 to 1,160 studies, removing one MMAT and one Legal Framework row; every figure below is the *post-merge* live value.

**What "appraised" means here needs to be read carefully, not assumed to mean uniform
depth.** Today's appraisal was necessarily a rule-based, disclosed batch process across a
corpus this size, not a signalling-question-level read of each study's actual source
document. For the 915 studies rated via CASP (263), MMAT (205), or the condensed Legal
Framework method (447) (an earlier draft said "roughly 1,050"), most individual domains are honestly "Can't tell"/"not assessable" rather
than a real judgement — because this project's extraction fields were built to capture
legal/institutional exposure-outcome content, not each study's own methodological reporting.
This section-by-section narrative says exactly where that limitation bites and where it
doesn't.

## Coverage of designs

`risk_of_bias_tool` (now fully consistent across all 1,159 studies. `evidence_map.csv`'s
`study_design_class` field was also partially normalized later the same day, once
`risk_of_bias_tool` was trustworthy enough to normalize against — see
`05_analysis/descriptive/study_design_class_normalization_2026-09-28.md`: 482 distinct
free-text values reduced to 297 by mapping the 707 studies whose tool unambiguously implies a
design onto `DATA_DICTIONARY.md`'s 8-value enum (228 of 707 needed correction). The remaining
455 Legal-Framework/`NONE`-tool studies were deliberately left as free text (counts as of that
pass; 26 studies were reclassified afterwards, and an audit re-sync on 2026-09-28 corrected 22
`study_design_class` values that the later reclassifications had left stale — see that
document's audit addendum), since the enum
itself has no category for their real methodological diversity — a genuine schema gap, not
unfinished normalization):

| Tool (design family) | n | % |
|---|---|---|
| Legal Institutional Evidence Appraisal Framework (doctrinal/documentary/jurimetric) | 447 | 39% |
| CASP Qualitative | 263 | 23% |
| MMAT (mixed methods) | 205 | 18% |
| JBI Cross-Sectional | 140 | 12% |
| ROBINS-I (non-randomized intervention/quasi-experimental) | 63 | 5% |
| AMSTAR 2 (secondary systematic reviews) | 23 | 2% |
| NONE (no validated tool applies — narrative/conceptual/simulation studies) | 13 | 1% |
| RoB 2 (randomized controlled trials) | 5 | 0.4% |

**This is the same underlying pattern the 2026-09-16 note already identified, now confirmed
at more than 3x the corpus size**: only 68 of 1,159 studies (6% — the 63 ROBINS-I plus 5 RoB
2; an earlier draft said "77 (7%)") use a design capable of supporting a causal claim about a
legal/administrative mechanism's effect on access. The other 94% are doctrinal/documentary
analysis (39%), qualitative research (23%), mixed-methods (18%), cross-sectional observational
association (12%), or secondary reviews and no-tool studies (3%). This
is corroborated by `mechanism_certainty`: only 35 of 1,159 studies (3%) reach level 3
("quasi-experimental evidence") or 4 ("experimental evidence"); 238 (21%) sit at level 1
("documented association") and 286 (25%) at level 2. **596 of 1,159 (51%) carry narrative
text rather than the intended 0–4 numeric code** — a real scale inconsistency inherited
across different extraction-batch eras, not smoothed over here (see `RISK_OF_BIAS.md` §4's
similar note about the Legal Framework batch's use of this same field). **The great majority
of this evidence base documents that legal/administrative mechanisms and access outcomes
co-occur, not that the former causes the latter** — this remains, at 1,159 studies, exactly
the single most important cross-cutting limitation the 366-study version identified, not a
finding that more data has since overturned.

## Coverage by jurisdiction / legal system

**Method caveat (audit, 2026-09-28).** `country` and `legal_system` are free-text fields, not controlled
vocabularies. Of the 1,159 studies, 1,031 name exactly one country, **125 name several countries or a region and are
not counted under any single country below**, and 3 are blank; `legal_system` has hundreds of distinct strings
(`common law`, `common_law`, `common law (India)` …). The counts here are rule-based buckets (rules in
`code/analysis/current_figures.py`; figures in `00_admin/CURRENT_FIGURES.md`), so they understate every country
that also appears in a multi-country study, and the "top countries" are shares of all 1,159 studies.

Top single-country values: India 133 (11%), Brazil 87 (7.5%), South Africa 84 (7%),
United States 71 (6%), Ghana 53 (5%), Kenya 50 (4%), Mexico 37 (3%), Indonesia 30 (3%),
Nigeria 28 (2%), Bangladesh 27 (2%), with the remaining ~95 single-country values each contributing
fewer. India, Brazil, and South Africa alone account for 26% of the corpus (an earlier draft said 25%, from summing rounded shares) — a shift from the
366-study snapshot (Brazil/India/South Africa then led at 29% combined, in a different order),
but the same underlying caution applies: any synthesis finding should be checked for whether
it is really general or a small set of country literatures dressed as a general one.

Legal-system coverage (rule-based buckets): common law only 546 (47%), civil law only 394 (34%),
mixed / both / customary 188 (16%), blank 28 (2%), other 3. (An earlier draft of this paragraph quoted
"common law 651 (56%), civil law 412 (36%), mixed 66 (6%)" from an undocumented bucketing that counted mixed
entries under common law; the rules are now in code.) This is a real shift from the
366-study snapshot's near-even common/civil split (41%/39%) toward common-law
over-representation — worth flagging as a genuine change in corpus composition as full-text
retrieval progressed, not an artifact of this appraisal pass. The disclosed search-strategy
limitation that likely shapes this remains unchanged from the 2026-09-16 note: SSRN and
Westlaw/Lexis were never searched at all (`SEARCH_PROTOCOL.md` §7), and jurisdiction coverage
here reflects what the databases actually searched, plus researcher-supplied PDFs, surfaced —
not a deliberate sampling frame.

## Measurement quality patterns

`legal_measurement_quality` and `outcome_measurement_quality` are populated for 389 of the
447 Legal Framework studies (87%) and for most of the quantitative-tool populations
(ROBINS-I, JBI, RoB 2) via the `covariates`/`outcome`-related fields used in today's
rule-based appraisals — but **not as a dedicated, uniform quality-coding pass**: these fields
were populated at different points across many extraction batches spanning weeks, using an
inconsistent mix of a `high`/`moderate`/`low` scale and a `1`–`4` numeric scale (the same
inconsistency noted for `mechanism_certainty` above). A future researcher wanting to compute
a single cross-study quality tabulation from these fields will need a normalization pass
first, not a direct `groupby`.

Today's appraisal surfaced a second, larger measurement-quality pattern directly: **for the
CASP Qualitative batch (263 studies) and the MMAT batch (205 studies) — 40% of the entire
corpus between them — 6 to 8 of each tool's roughly 10 quality items are honestly "Can't
tell" for nearly every single study**, because this project's extraction was built to
capture each study's substantive legal/institutional finding, not its own recruitment
strategy, reflexivity statement, ethics approval, or analytic process. This is not evidence
that these 468 studies are poorly conducted — it is evidence that this review cannot
currently say whether they are, for the specific methodological dimensions CASP and MMAT ask
about. See `04_quality/appraisal_forms/CASP_Qualitative_batch_2026-09-28.md` and
`MMAT_batch_2026-09-28.md` for the full item-by-item accounting; this is, by a wide margin,
the single largest unresolved measurement-quality gap in the whole risk-of-bias effort.

## Mechanism-family coverage

`evidence_map.csv`'s `mechanism_family` field was not recomputed as part of today's
risk-of-bias work (it tracks a separate derivation pipeline, `build_evidence_map.py`, keyed
off different fields) and should not be assumed current — this is a distinct, still-open
staleness gap from the `study_design_class` field discussed above, which was partially
normalized later today (see that section's update). What today's work does newly connect: the
Phase 11 quantitative-feasibility judgment
(`06_outputs/supplementary/phase11_quantitative_feasibility_judgment.md`, 2026-09-28) found
20 Family A, 6 Family B, and 17 Family C studies with a genuine, poolable effect size (plus
18 studies whose family assignment remained unresolved at that point — updated later the same
day: after the 9-row blank-family follow-up and the S348 addition, `effect_sizes.csv` holds 62
rows, Family A 20 / B 6 / C 20, with 16 rows left blank on a documented, reasoned non-fit basis,
`phase11_blank_family_resolution_2026-09-28.md`) — consistent with the
366-study snapshot's own finding that Family A and Family B "each currently rest on a small
handful of studies," now confirmed at a larger, still-small scale. **No candidate family has
enough independent, comparably-operationalized studies to support pooling** — Phase 11's own
verdict, unchanged in substance from what this note's predecessor anticipated.

## Studies appraised with the non-validated framework

447 of 1,159 studies (39%) carry `risk_of_bias_tool` = "Legal Institutional Evidence
Appraisal Framework" — up from 20% at the 366-study snapshot, both in raw count and as a
share of the corpus, reflecting real growth in doctrinal/jurimetric full-text retrieval since
then, not a classification drift (today's design audit, `CHANGELOG.md`, actually *reduced*
the raw tag count by moving 148 misclassified studies onto validated tools: 573 − 148 = 425,
which later rose to 449 when 24 studies were moved *into* the framework — 9 reverted after an
over-correction, 8 from the previously unassigned batch, 6 JBI mis-tags, and 1 other (S409) — and fell
to 447 when the duplicate S299 was retired). `RISK_OF_BIAS.md` §2 remains explicit that this framework's output is a
**narrative judgment call, not a citable, validated score**, and today's condensed appraisal
of the framework studies (`LegalFramework_batch_2026-09-28.md` covers 434 as originally run — the 425 plus a
9-study follow-up, before S299 was retired; the other ~15 were appraised in the unassigned-studies and reassignment
batches, generally more thinly) only strengthens that caveat rather than
resolving it: only 5 of the framework's 13 domains were populated from real prior-extraction
data (jurisdictional specificity, exposure definition, outcome definition, causal
identification, institutional context) for the 389 studies with that data on record; the
other 8 domains — including legal source accuracy, sampling transparency, and researcher
reflexivity — are "not assessable" for all 447. This caveat must travel with any synthesis
finding drawn from more than a third of this corpus.

## Overall confidence in the body of evidence

Reported per candidate synthesis family, per `RISK_OF_BIAS.md` §3's own instruction, drawing
on both today's risk-of-bias ratings and the Phase 11 quantitative-feasibility judgment:

- **Family A (legal recognition/eligibility, 20 effect-size rows):** the studies underlying
  this family are drawn mainly from the ROBINS-I and JBI Cross-Sectional populations. Of
  today's 63 rule-based ROBINS-I ratings, 54 land at "Moderate" confounding risk and 9 at
  "Serious" — meaning even the strongest-designed quasi-experimental studies in this family
  carry real, undocumented confounding risk by this project's own conservative reading.
  **Low-to-moderate confidence**, not because the individual studies are necessarily weak,
  but because this review cannot currently document that they are strong.
- **Family B (bureaucratic assistance, 6 effect-size rows):** the smallest family, and the
  one where today's appraisal happens to be richest — S085 and **S294** (both RoB 2
  cluster-trial-rated today; corrected 2026-09-28 from an earlier draft of this paragraph
  that misnamed the second study as S879, which is actually a Family C study) carry real
  pre-registration evidence and the most complete appraisal forms in the whole corpus. **Low
  confidence on sample size grounds alone** (6 studies, per Phase 11), independent of the
  individual studies' own reasonably solid RoB 2 ratings ("Some concerns," not "High risk,"
  for both).
- **Family C (administrative/legal barriers, 20 effect-size rows; 17 in the original Phase 11 judgment):** the largest of the
  three families and the most design-heterogeneous — spanning ROBINS-I, JBI Cross-Sectional,
  and Legal Framework-appraised studies. Phase 11 §5.1 already identified this family's
  strongest internal candidate (the ownership/price sub-cluster, S526/S539/S749), and
  today's ratings do not change that judgment: S526 and S539 (both JBI-appraised) land at
  "Some concern," consistent with the rest of Family C. **Low-to-moderate confidence**, with
  the same caveat as Family A.

**No family currently supports a claim stronger than "the direction of association is
plausible and repeatedly documented across heterogeneous settings" — nothing in today's
risk-of-bias work changes Phase 11's verdict that none of the three families clears the bar
for meta-analysis.** This is not a failure of today's appraisal effort; it is the honest
product of an evidence base that is, by design and by the discipline's own nature, dominated
by observational and qualitative work rather than by a large pool of directly comparable
quasi-experimental studies.

> **Correction 2026-09-29:** the "only 35 of 1,159 studies" at `mechanism_certainty` 3–4 below is a count of the field's values, not of quasi-experimental or experimental studies — only 10 of those 35 are ROBINS-I/RoB 2 studies (`05_analysis/descriptive/DATA_QUALITY_AUDIT_2026-09-29.md` §5). The text below is left as written.

## Four further caveats surfaced by the 2026-09-28 audit

**1. Some appraisals rest on abstract- or metadata-level extraction only.** 36 of the 1,159
studies (3.2%) carry an `extraction_note` stating they were extracted from the published
abstract, introduction, or repository metadata only, because the full text was never
obtained at extraction time (CASP 20, MMAT 7, JBI Cross-Sectional 6, Legal Framework 4, AMSTAR 2 0, RoB 2 0). The count has fallen over time as full texts were found: 69 before 2026-09-29; S277, S326 and S366 re-read from full text on 2026-09-29; S319, S324, S325 and S344 on 2026-10-02; 13 more (S331-S347) and then 5 (S257, S278, S279, S281, S288) and 3 (S260, S267, S274) on 2026-10-04 from PDFs already in the researcher's Drive (see `code/provenance/audit_and_repair/reextract_2026-10-04/CAMPAIGN_NOTES.md`); two abstract-only rows were retired (S299, a duplicate; S356, an E05 exclusion). Their appraisals are honest about this — the CASP entries, for example,
record "Can't tell" on 6 to 8 of 10 items (typically 7) — and S366 (RoB 2) is explicitly labelled
LOW-CONFIDENCE. But a reader tabulating ratings by tool should not treat those 37 as
equivalent to full-text appraisals; filter on `extraction_note` before doing so — the 37 are listed in
`05_analysis/sensitivity/abstract_only_extractions_2026-09-28.csv`, and **none of them has an `effect_sizes.csv`
row**, so no Family A/B/C synthesis figure rests on an abstract-only extraction. This
limitation was previously documented only in scattered `CHANGELOG.md` entries, not in any
corpus-level summary.

**2. A "High concern" JBI rating usually means "sparse extraction", not "flawed study".** 59
of the 140 JBI Cross-Sectional studies (42%) are rated "High concern" (`RISK_OF_BIAS.md` §4
already states this in the rating text: no `covariates` or named statistical method captured
in this project's extraction fields). It measures how much methodological detail the extraction
captured, not the study's actual conduct, and must not be read as a finding that 42% of
cross-sectional studies in this corpus are methodologically poor.

**3. Two papers were counted twice, and were merged the same day.** The repository audit found
S233/S1008 (Morales & Zambrano 2018) and S299/S392 (Minaverry 2017) to be the same papers extracted
and appraised under two `record_id`s each (language-variant titles and a blank DOI defeated the earlier
duplicate audits). With the researcher's approval the fuller full-text-based row of each pair was kept
(S1008, S392) and S233 and S299 were retired, taking the corpus from 1,162 to **1,160** distinct
studies; every figure in this note is the post-merge value, and the two retired rows were an MMAT and a
Legal Framework row. Neither pair contributed an `effect_sizes.csv` row, so no synthesis figure moved
(`00_admin/audits/2026-09-28_repository_audit.md`, finding 13). This kind of duplicate — same paper,
different-language titles, blank DOI — remains undetectable by the DOI and title audits, and the
check that found these two covered only the included studies.

**S356 (added later the same day).** The researcher supplied the full text of S356, the OECD working paper on
economic regulation of water services (Trémolet & Smith 2026), which had been an abstract-only include with no
reviewer. It states no search strategy or method and analyses no primary data, so it was excluded as E05 (the
project's precedent for non-systematic policy overviews) and retired: 1,160 → 1,159 studies, Legal Framework
448 → 447, and 70 → 69 abstract-only extractions. No synthesis figure is affected (it had no `effect_sizes.csv` row).

**4. Counts are of reports, and some reports share an underlying study.** Extraction is per report. Two
pairs are the same underlying data (S294/S366, one cluster-randomised trial; S097/S098, one interview
sample) and two overlap partially (S681/S682, S357/S369), so the 1,159 rows correspond to roughly 1,157
distinct studies on the definite links and 1,155 counting the partial ones
(`03_extraction/extracted_data/linked_reports_2026-09-28.csv`; nothing merged — researcher decision). The
practical consequences for this note: the **5 RoB 2 studies are 4 distinct trials** (S294 and S366 report
the same DRC trial), so the "68 causal-capable designs" are 67 distinct studies; and the S366 appraisal is
itself one of the abstract-only, low-confidence ones flagged in caveat 1. Independence also matters
within effect sizes: the audit-inferred pair S526/S539 (two US large-utility studies whose samples
probably overlap) are both in `effect_sizes.csv`, which the Family C synthesis now discloses.
