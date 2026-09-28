# Cross-Cutting Evidence Limitations — 2026-09-28

## Status of this note

This supersedes `2026-09-16_evidence_limitations.md`, which was explicitly a placeholder —
written when only 12 of what was then a 366-study corpus had been appraised at all, with its
own "Overall confidence" section deliberately left blank pending real ratings. As of today,
`risk_of_bias_tool` is correctly classified for all 1,162 extracted studies, and every study
for which a rating is possible has one (see `RISK_OF_BIAS.md` §4 and `CHANGELOG.md`'s
2026-09-28 entries for the full account of how). This narrative is therefore the first
version of this file that can actually do what `RISK_OF_BIAS.md` §3 asks: summarize
limitations of the evidence base **as a whole**, informed by real ratings rather than corpus
composition alone.

**What "appraised" means here needs to be read carefully, not assumed to mean uniform
depth.** Today's appraisal was necessarily a rule-based, disclosed batch process across a
corpus this size, not a signalling-question-level read of each study's actual source
document. For the roughly 1,050 studies rated via CASP, MMAT, or the condensed Legal
Framework method, most individual domains are honestly "Can't tell"/"not assessable" rather
than a real judgement — because this project's extraction fields were built to capture
legal/institutional exposure-outcome content, not each study's own methodological reporting.
This section-by-section narrative says exactly where that limitation bites and where it
doesn't.

## Coverage of designs

`risk_of_bias_tool` (now fully consistent across all 1,162 studies, unlike the 482
inconsistent free-text values still sitting in `05_analysis/descriptive/evidence_map.csv`'s
`study_design_class` field — a genuine, disclosed data-cleanliness gap in that file that
today's work did not touch, since it tracks a different pipeline than `risk_of_bias_tool`):

| Tool (design family) | n | % |
|---|---|---|
| Legal Institutional Evidence Appraisal Framework (doctrinal/documentary/jurimetric) | 433 | 37% |
| CASP Qualitative | 245 | 21% |
| MMAT (mixed methods) | 207 | 18% |
| JBI Cross-Sectional | 166 | 14% |
| ROBINS-I (non-randomized intervention/quasi-experimental) | 72 | 6% |
| AMSTAR 2 (secondary systematic reviews) | 22 | 2% |
| NONE (no validated tool applies — narrative/conceptual/simulation studies) | 12 | 1% |
| RoB 2 (randomized controlled trials) | 5 | 0.4% |

**This is the same underlying pattern the 2026-09-16 note already identified, now confirmed
at more than 3x the corpus size**: only 77 of 1,162 studies (7% — the 72 ROBINS-I plus 5 RoB
2) use a design capable of supporting a causal claim about a legal/administrative mechanism's
effect on access. The other 93% are either doctrinal/documentary analysis (37%), qualitative
research (21%), mixed-methods (18%), or cross-sectional observational association (14%). This
is corroborated by `mechanism_certainty`: only 35 of 1,162 studies (3%) reach level 3
("quasi-experimental evidence") or 4 ("experimental evidence"); 241 (21%) sit at level 1
("documented association") and 286 (25%) at level 2. **596 of 1,162 (51%) carry narrative
text rather than the intended 0–4 numeric code** — a real scale inconsistency inherited
across different extraction-batch eras, not smoothed over here (see `RISK_OF_BIAS.md` §4's
similar note about the Legal Framework batch's use of this same field). **The great majority
of this evidence base documents that legal/administrative mechanisms and access outcomes
co-occur, not that the former causes the latter** — this remains, at 1,162 studies, exactly
the single most important cross-cutting limitation the 366-study version identified, not a
finding that more data has since overturned.

## Coverage by jurisdiction / legal system

Top countries (`country`, of 1,162): India 133 (11%), Brazil 87 (7%), South Africa 84 (7%),
United States 71 (6%), Ghana 53 (5%), Kenya 49 (4%), Mexico 37 (3%), Indonesia 30 (3%),
Nigeria 28 (2%), Bangladesh 27 (2%), with the remaining ~100 countries each contributing
fewer. India, Brazil, and South Africa alone account for 25% of the corpus — a shift from the
366-study snapshot (Brazil/India/South Africa then led at 29% combined, in a different order),
but the same underlying caution applies: any synthesis finding should be checked for whether
it is really general or a small set of country literatures dressed as a general one.

Legal-system coverage: common law (incl. variants) 651 (56%), civil law (incl. variants) 414
(36%), mixed/hybrid/customary-overlay 66 (6%), blank 28 (2%). This is a real shift from the
366-study snapshot's near-even common/civil split (41%/39%) toward common-law
over-representation — worth flagging as a genuine change in corpus composition as full-text
retrieval progressed, not an artifact of this appraisal pass. The disclosed search-strategy
limitation that likely shapes this remains unchanged from the 2026-09-16 note: SSRN and
Westlaw/Lexis were never searched at all (`SEARCH_PROTOCOL.md` §7), and jurisdiction coverage
here reflects what the databases actually searched, plus researcher-supplied PDFs, surfaced —
not a deliberate sampling frame.

## Measurement quality patterns

`legal_measurement_quality` and `outcome_measurement_quality` are populated for 365 of the
433 Legal Framework studies (84%) and for most of the quantitative-tool populations
(ROBINS-I, JBI, RoB 2) via the `covariates`/`outcome`-related fields used in today's
rule-based appraisals — but **not as a dedicated, uniform quality-coding pass**: these fields
were populated at different points across many extraction batches spanning weeks, using an
inconsistent mix of a `high`/`moderate`/`low` scale and a `1`–`4` numeric scale (the same
inconsistency noted for `mechanism_certainty` above). A future researcher wanting to compute
a single cross-study quality tabulation from these fields will need a normalization pass
first, not a direct `groupby`.

Today's appraisal surfaced a second, larger measurement-quality pattern directly: **for the
CASP Qualitative batch (245 studies) and the MMAT batch (207 studies) — 39% of the entire
corpus between them — 6 to 8 of each tool's roughly 10 quality items are honestly "Can't
tell" for nearly every single study**, because this project's extraction was built to
capture each study's substantive legal/institutional finding, not its own recruitment
strategy, reflexivity statement, ethics approval, or analytic process. This is not evidence
that these 452 studies are poorly conducted — it is evidence that this review cannot
currently say whether they are, for the specific methodological dimensions CASP and MMAT ask
about. See `04_quality/appraisal_forms/CASP_Qualitative_batch_2026-09-28.md` and
`MMAT_batch_2026-09-28.md` for the full item-by-item accounting; this is, by a wide margin,
the single largest unresolved measurement-quality gap in the whole risk-of-bias effort.

## Mechanism-family coverage

`evidence_map.csv`'s `mechanism_family` field was not recomputed as part of today's
risk-of-bias work (it tracks a separate derivation pipeline, `build_evidence_map.py`, keyed
off different fields) and should not be assumed current — see the design-class inconsistency
noted above as the same underlying staleness. What today's work does newly connect: the
Phase 11 quantitative-feasibility judgment
(`06_outputs/supplementary/phase11_quantitative_feasibility_judgment.md`, 2026-09-28) found
20 Family A, 6 Family B, and 17 Family C studies with a genuine, poolable effect size (plus
18 studies whose family assignment remains genuinely unresolved) — consistent with the
366-study snapshot's own finding that Family A and Family B "each currently rest on a small
handful of studies," now confirmed at a larger, still-small scale. **No candidate family has
enough independent, comparably-operationalized studies to support pooling** — Phase 11's own
verdict, unchanged in substance from what this note's predecessor anticipated.

## Studies appraised with the non-validated framework

433 of 1,162 studies (37%) carry `risk_of_bias_tool` = "Legal Institutional Evidence
Appraisal Framework" — up from 20% at the 366-study snapshot, both in raw count and as a
share of the corpus, reflecting real growth in doctrinal/jurimetric full-text retrieval since
then, not a classification drift (today's design audit, `CHANGELOG.md`, actually *reduced*
the raw tag count from 573 to 433 by correcting 148 misclassified studies onto validated
tools instead). `RISK_OF_BIAS.md` §2 remains explicit that this framework's output is a
**narrative judgment call, not a citable, validated score**, and today's condensed appraisal
of all 433 (`LegalFramework_batch_2026-09-28.md`) only strengthens that caveat rather than
resolving it: only 5 of the framework's 13 domains were populated from real prior-extraction
data (jurisdictional specificity, exposure definition, outcome definition, causal
identification, institutional context) for the 365 studies with that data on record; the
other 8 domains — including legal source accuracy, sampling transparency, and researcher
reflexivity — are "not assessable" for all 433. This caveat must travel with any synthesis
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
  one where today's appraisal happens to be richest — S085 and S879 (both RoB 2
  cluster-trial-rated today) carry real pre-registration evidence and the most complete
  appraisal forms in the whole corpus. **Low confidence on sample size grounds alone** (6
  studies, per Phase 11), independent of the individual studies' own reasonably solid
  RoB 2 ratings ("Some concerns," not "High risk," for both).
- **Family C (administrative/legal barriers, 17 effect-size rows):** the largest of the
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
