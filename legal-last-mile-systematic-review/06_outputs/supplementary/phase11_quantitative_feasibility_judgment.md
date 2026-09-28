# Phase 11 — Corpus-Level Quantitative-Feasibility Judgment

**Status: written 2026-09-28.** This is the first time `ANALYSIS_PLAN.md`
§2's decision tree has been applied explicitly, at the family level,
across the whole of `05_analysis/effect_sizes/effect_sizes.csv` — not
scattered across individual `exclusion_from_pooling_reason` fields, which
is where this reasoning previously lived (see `PRISMA_WORKFLOW.md`'s
Phase 11 row and `README.md`'s "How to continue" item 5, both of which
flagged this document as outstanding). Full-text retrieval (Phase 6) is
closed as of 2026-09-28 (`CHANGELOG.md`), so the underlying effect-size
pool this judgment is based on is now final unless a future researcher
reopens retrieval — see the caveat under "What this document does not do."

## 1. Data basis

`effect_sizes.csv` holds **61 rows** as of this writing (S001–S1164
extraction range). Family assignment, after one correction made as part
of this pass (§5 below):

| `synthesis_family` | k (studies) |
|---|---|
| A — Legal recognition and access | 20 |
| B — Administrative assistance and access | 6 |
| C — Administrative/legal barriers and access inequality | 17 |
| *(blank — does not map cleanly to A/B/C)* | 18 |
| **Total** | **61** |

(Before this pass: 20/6/16/19. S749 moved from blank to C — see §5.)

## 2. Method

`ANALYSIS_PLAN.md` §2's tree is applied **per candidate family**
(`PROJECT_SPEC.md` §8), not once globally. For each family, the
operative question is not "is there an empirical study with a locatable
effect size" (every row here already clears that, or it would not be in
`effect_sizes.csv` — see `evidence_status = OBSERVED` on every row) but:
**do two or more studies within the family share a substantively
comparable exposure–comparator–outcome estimand**, per the tree's central
fork:

```
Does the estimate represent a substantively comparable estimand?
        +---- NO ---> structured quantitative synthesis (SWiM-style)
```

`ANALYSIS_PLAN.md`'s own opening rule governs this judgment: *"A
mathematically convertible statistic is not automatically a
substantively comparable effect."* Two studies both reporting an odds
ratio, or both reporting a percentage-point difference, are not thereby
comparable — the underlying legal/institutional mechanism, population,
and outcome construct have to match too (`ANALYSIS_PLAN.md` §3's
critical pooling rule gives the canonical example: legal recognition
raising access vs. bureaucratic assistance raising access are different
estimands even though both are "about access").

This pass re-examined all 61 rows **together, side by side**, rather than
trusting each row's own isolated `exclusion_from_pooling_reason` (written
in different batches, weeks apart, without visibility into the other 60
rows) — the point of doing this at the family level now that the pool is
closed. That re-examination did surface real candidate sub-groupings
(§§3–5) that the individual per-row notes, written one at a time, had not
connected to each other.

## 3. Family A — Legal recognition and access (k = 20)

**Verdict: routes to structured quantitative synthesis (SWiM), not
meta-analysis.** No two studies share a substantively comparable
estimand. The 20 studies span at least 15 countries/jurisdictions and 14
genuinely distinct legal/institutional exposures — slum-notification
status (S084), municipal incorporation (S142), tribal vs. state
regulatory primacy (S358), ZEIS zoning designation (S398), WRUA legal
membership (S404), land titling (S765), ethnic-autonomous-county status
(S780), formal utility connection fees (S882), participatory
water-user-association management (S920), customary indigenous
governance (S930), colonial-era governance duration (S969), watershed
programme participation (S1020), CBO establishment (S1042), community
design participation (S1057), water-adequacy growth-control screening
(S1121), and zoning status (S1122) — each with its own outcome metric
(adjusted % differences, ORs, hazard ratios, DiD coefficients, PSM ATTs,
minutes of time saved, incidence-rate ratios). `ANALYSIS_PLAN.md` §4's
own rule ("a linear-probability coefficient should **not** simply be
treated as an odds ratio") rules out silently converting these onto one
scale to force a pool.

Two candidate **narrative sub-groupings** were identified for the Phase 13
SWiM write-up (grouping, not pooling — see `ANALYSIS_PLAN.md` §7's
subgroup framing):

- **Recognized vs. unrecognized settlement status** (S084 Mumbai
  notification status; S1122 Ouagadougou zoning status) — both compare a
  household's *settlement's* formal-recognition status to a water-access
  outcome, in informal/peri-urban contexts. Different outcome metrics (%
  difference in LPCD vs. Cox hazard ratio for first connection) and
  different countries/legal systems still block pooling, but they are the
  closest conceptual pair in this family and worth presenting together.
- **Quasi-experimental institutional-reform studies with a
  percentage-point-scale access outcome** (S765 Peru land titling, DiD;
  S920 Brazil WUA management model, DiD/kernel-matching; S930 Oaxaca
  customary governance, PSM/ATT) — all three use a credible
  quasi-experimental design and report an effect in the same rough units
  (a several-percentage-point increase in a water/sanitation access
  outcome). They are **not** pooled here because the underlying legal
  mechanisms are three different things — individual land titling,
  participatory management-model choice, and customary-law governance
  recognition are not the same intervention, and pooling them would be
  exactly the "manufactured comparability" `ANALYSIS_PLAN.md` opens by
  prohibiting. They are flagged because a future researcher who wanted to
  argue for pooling would look here first, and the reason not to should be
  on record rather than rediscovered.

## 4. Family B — Administrative assistance and access (k = 6)

**Verdict: routes to structured quantitative synthesis (SWiM), not
meta-analysis; too few studies to even reach the comparability question
meaningfully.** `PROJECT_SPEC.md` §8 itself anticipated this ("study count
may be too small to pool — use structured quantitative synthesis if so").
Six studies, six distinct mechanisms: bureaucratic assistance × political
coordination (S085, RCT); community WASH institutional strengthening
(S294, RCT); capital-cost contribution/meeting attendance (S1102, PSM);
network capital in funding applications (S1140, logit); NGO/CBO trust
(S1144, logit); external WaSH programme funding (S1163, multilevel
logistic). Three of the six (S1140, S1144, S1163) happen to report odds
ratios/log-odds from a logit-family model, which is worth grouping
narratively in the SWiM write-up as "administrative/institutional-trust
mechanisms measured via logistic models" — but the actual exposures
(network capital, trust, external funding) remain distinct constructs,
so this is a presentation grouping, not a pooling candidate.

## 5. Family C — Administrative/legal barriers and access inequality (k = 17, after correction)

**Verdict: routes to structured quantitative synthesis (SWiM), not
meta-analysis** — but this family contains the **single strongest
candidate sub-cluster in the entire corpus** for a future restricted
synthesis, and it is worth stating plainly rather than burying it in the
same "17 unrelated studies" framing as Families A and B.

### 5.1 The ownership/regulatory-structure-and-price cluster

Three studies test the **same exposure** — private/investor-owned vs.
public or cooperative-owned water utility, an institutional-ownership
mechanism — against a **price or affordability outcome**:

| Study | Country | Comparator | Outcome | Effect |
|---|---|---|---|---|
| S526 | US (1,183 utilities) | Government-owned utility | Unit-price ratio (UPR) at 30,000 gal/month | −0.167 (more regressive pricing), p<0.001 |
| S539 | US (500 utilities) | Government/cooperative-owned | Annual household bill (USD); % of lowest-quintile income | +$144.04/yr, p<0.01; +1.55 pp income share, p<0.01 |
| S749 | Brazil (51 corporations) | Public/mixed-capital utility | Tariff level (R$/m3) | +0.3456 R$/m3, significant |

**S749 was reclassified from a blank `synthesis_family` to `C` as part of
this pass.** Its own prior note said the ownership exposure "does not
cleanly map onto... Family A/B/C," but that was inconsistent with S526
and S539 — the identical exposure (private vs. public ownership) already
carrying a `C` tag for the identical reason (an institutional/regulatory
mechanism producing a price/affordability outcome). Leaving S749 blank
while its two closest analogues were tagged C was a labeling
inconsistency introduced by the studies having been added to
`effect_sizes.csv` in different batches, not a principled distinction —
the same kind of drift this project's `CHANGELOG.md` has already
disclosed and corrected elsewhere (e.g. the "245/58" stale figures, the
frozen `prisma_flow.md` paragraph). See `effect_sizes.csv`'s updated
`exclusion_from_pooling_reason` for S749 for the full note.

**This cluster is still not pooled**, and should not be without a
deliberate methods decision: the three outcomes are on three genuinely
different metrics — a dimensionless unit-price ratio (S526), a
dollar-denominated bill amount and an income-share percentage (S539), and
a local-currency tariff-per-cubic-metre level (S749). `ANALYSIS_PLAN.md`
§4 permits converting to a common estimand only when "a defensible
transformation exists" — converting all three to, say, a standardized
percentage effect on price would require decisions (What's the reference
price level in each currency/context? Is R$/m3 vs. USD/month vs. a
dimensionless ratio genuinely on a convertible scale, or only
superficially so?) that deserve their own dedicated methods note before
anyone attempts it, not a decision made in passing here. **This is the
single most concrete, actionable next step this document identifies** —
see §8.

A fourth, related-but-not-identical study, **S1038** (US, 1965,
state-vs-local *economic regulation* — not ownership type — vs. monopoly
welfare loss as % of bill), shares the general theme (institutional/
regulatory structure → affordability) but tests a different exposure
(regulatory jurisdiction, not ownership) on a different outcome metric
(% welfare loss). It is presented alongside the ownership cluster in the
Phase 13 SWiM write-up as the same broader mechanism family, not folded
into it as a fourth comparable estimand.

### 5.2 The remaining 13 Family C studies

The other 13 studies (S174, S590, S593, S606, S631, S879, S947, S1032,
S1062, S1136, S1143, S1146, S1162) each test a distinct
administrative/legal-barrier mechanism — institutional-capacity factor
scores, historical franchise structure, fiscal-autonomy/administrative
classification, household-registration status, jurisdiction-splitting,
contract-enforcement RCTs, national regulatory-quality indices,
redress-seeking behavior, cost-recovery policy, political capture,
service-delivery rules, corruption incidence, and local-government
administrative category — in as many different countries and legal
systems. None shares a comparable estimand with another study in this
set or with the ownership/price cluster above.

## 6. The 18 blank-`synthesis_family` rows

These 18 rows cannot be judged against `ANALYSIS_PLAN.md` §2 at all yet,
because the tree is explicitly applied **per candidate family**
(`PROJECT_SPEC.md` §8's three named families) — a study with no family
assignment has nothing to be compared against. Re-examining all 19
original blank rows together (before the S749 correction) surfaced a
real split that was not visible when each was added in isolation:

**9 rows carry an explicit, reasoned non-fit judgment** in their
`provenance_note` — a genuine "I considered Family A/B/C and this does
not match" call, not an omission: S149 (community-governance
participation — a citizen-side mechanism distinct from Family B's
provider-side assistance), S178 (water-quality/health outcome, not an
access outcome), S312 (jurisdiction-level policy adoption, not a
household outcome), S353 (provider-level regulatory-compliance outcome,
not a household-facing barrier), S388 (management-capacity exposure — "a
real judgment call... left for a human/manuscript-stage decision"), S636
(fiscal-grant exposure not matching any family definition), S649
(fiscal-transfer exposure, same reasoning as S636), S795 (privatization/
ownership-vs-**access** — as opposed to the ownership-vs-**price**
studies now in §5.1 — explicitly anchored to the same reasoning as the
pre-correction S749), and S869 (intermunicipal-cooperation-arrangement
exposure).

**9 rows carry no family-fit discussion at all** in their
`provenance_note` — they describe the study and its finding but never
address whether it was considered against Family A/B/C's definitions:
**S434, S435, S445, S448, S470, S471, S483, S489, S491**. This looks like
an omission in the batches that added them (the family field was
apparently left blank by default rather than by a documented decision),
not a considered judgment — the same kind of gap this project's own
`README.md` "Known limitations" section already discloses for other
fields. **This is a genuine, itemized open item this document does not
resolve** (see §8) — assigning these 9 to a family now, under time
pressure and without the same side-by-side reasoning given to the other
52 rows, would risk exactly the kind of rushed, under-justified call this
project has consistently avoided.

Re-examining S795 against the now-corrected S749: S795's outcome is
household **connection probability**, not price — a genuinely different
outcome type from the §5.1 ownership/price cluster, so it is *not*
reclassified alongside S749. It remains blank, correctly.

## 7. Overall corpus-level verdict

**No family currently clears `ANALYSIS_PLAN.md` §2's bar for
meta-analysis.** Families A, B, and C all route to Phase 13's structured
quantitative synthesis (SWiM) instead. This is the correct conclusion
given the evidence actually in hand — not a gap, and not a failure of the
review. `05_analysis/meta_analysis/` should continue to hold nothing;
`included_in_pooled_estimate = FALSE` on all 61 rows remains accurate and
should not change until a future researcher makes and documents a
specific, defensible case for one of the sub-clusters named above
(most plausibly §5.1's ownership/price cluster, if a genuinely defensible
common-metric transformation is found).

## 8. What this document does not do

**Status update, 2026-09-28 (later the same day): the three items below are now done.**

- ~~It does not perform the actual Phase 13 SWiM write-ups.~~ **Done**: three files created
  from `06_outputs/supplementary/SWIM_SYNTHESIS_TEMPLATE.md` —
  `family_A_swim_synthesis_2026-09-28.md`, `family_B_swim_synthesis_2026-09-28.md`,
  `family_C_swim_synthesis_2026-09-28.md` — each citing this document as why that family did
  not proceed to meta-analysis, and incorporating that day's completed risk-of-bias ratings
  into each family's "Certainty in this body of evidence" section.
- ~~It does not resolve the 9 never-evaluated blank rows in §6.~~ **Done**: see
  `phase11_blank_family_resolution_2026-09-28.md`. 2 of the 9 (S470, S471) were corrected to
  Family C after being checked against real precedent elsewhere in the corpus (S1038); the
  other 7 were confirmed as genuine non-fits, each citing the specific precedent applied
  (S312, S636/S649, or S869). Family C's count moved from 17 to 19; the blank-reasoned-non-fit
  count moved from 18 to 16.
- ~~It does not attempt the S526/S539/S749 price-metric conversion floated in §5.1.~~ **Done**:
  see `phase11_pooling_feasibility_S526_S539_S749.md`, a dedicated methods note. Verdict: no
  defensible transformation exists with the data currently extracted — S526's outcome measures
  rate-structure progressivity (a different construct from S539/S749's price-*level* outcomes),
  and converting S539's dollar bill to S749's R$/m³ tariff rate (or vice versa) would require
  inventing an assumed household consumption volume, a currency-conversion reference year, and
  an inflation adjustment that neither source paper's extracted data supports. The cluster
  remains a structured-synthesis (SWiM) grouping, not a pooling candidate — see §6 of that note
  for what would change this answer.
- It does not assume the 61-row pool is final in the sense of never
  changing — it is final in the sense that no further full-text
  retrieval will add candidate studies (Phase 6 closed 2026-09-28), but a
  future researcher could still add effect sizes by re-mining the 1,162
  already-included full texts for quantitative results not yet extracted
  into `effect_sizes.csv`, or by resolving the family assignment of the
  studies in §6. (This last item remains open — no re-mining of full texts
  for additional effect sizes was performed today.)
