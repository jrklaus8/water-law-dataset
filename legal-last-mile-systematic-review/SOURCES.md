# Preliminary Methodological Sources

These are **starting points, not the final evidence base** — none of them
were found through the protocol search (`SEARCH_PROTOCOL.md`), which has not
yet been executed. Each citation below has been checked in this session
against independent web sources; the verification method and result are
recorded for each so the check itself is auditable. `doi.org` and every
publisher domain (academic.oup.com, journals.sagepub.com, ajps.org,
link.springer.com, bmj.com) were unreachable in this environment — blocked
by the outbound network egress proxy — so verification here relied on
independent web search rather than a direct DOI/publisher fetch. This is a
weaker verification than resolving the DOI directly, and a researcher with
working publisher access should confirm each entry directly against the
DOI before the sources are relied on in the manuscript.

## 1. Halling & Bækgaard 2024 — Administrative burden systematic review

> Halling, A., & Bækgaard, M. (2024). Administrative Burden in
> Citizen–State Interactions: A Systematic Literature Review. *Journal of
> Public Administration Research and Theory*, 34(2), 180–195.
> https://doi.org/10.1093/jopart/muad023

**Verification:** Confirmed via web search (Oxford Academic listing,
Aarhus University repository record). Volume/issue/pages match. The review
covers 119 articles and working papers on administrative burden in
citizen-state interactions since 2012, PRISMA-based.

**Why it matters:** demonstrates that a heterogeneous administrative
literature can be systematically coded and theoretically synthesized while
maintaining clear distinctions among different empirical designs and
claims — the methodological precedent this project follows for §"core
methodological verdict" in `PROJECT_SPEC.md` §3.

## 2. Lubeck-Schricker et al. 2023 — Legal exclusion, Mumbai water inequality

> Lubeck-Schricker, M., Patil-Deshmukh, A., Murthy, S. L., Chaubey, M. D.,
> Boomkar, B., Shaikh, N., Shitole, T., Eliasziw, M., & Subbaraman, R.
> (2023). Divided infrastructure: legal exclusion and water inequality in
> an urban slum in Mumbai, India. *Environment & Urbanization*, 35(1),
> 178–196. https://doi.org/10.1177/09562478221121737

**Verification:** Confirmed via web search (SAGE Journals listing, PMC open
version PMC10237587). 593 households in Mandala slum, comparing notified
(legally recognized) vs. non-notified neighborhoods on water infrastructure,
accessibility, reliability, and spending.

**Why it matters:** candidate primary study for meta-analytic Family A
(legal recognition and access) in `PROJECT_SPEC.md` §8 — an observational
comparison, not a causal intervention; do not pool with Family B evidence.

## 3. Gaikwad et al. 2026 — Field experiment, bureaucratic assistance

> Gaikwad, N., & Thomas, A. (2026). Getting on the grid: A field experiment
> on bottom-up political pressure and access to essential public services.
> *American Journal of Political Science*.
> https://doi.org/10.1111/ajps.70068

**Verification:** Confirmed via web search (Wiley/AJPS listing, AJPS author
summary, CASI event page). **Note on authorship:** independent sources
identify exactly two authors — Nikhar Gaikwad (Columbia) and Anjali Thomas
(Georgia Tech) — rather than a larger "et al." author list; the original
"Gaikwad et al." shorthand in the preliminary source list appears to
simply mean "Gaikwad and coauthor(s)," which resolves to Gaikwad & Thomas.
Confirm the full byline against the published version before citing.
**Note on duplicate publication:** a related/earlier working paper titled
"Bureaucratic Hurdles, Political Resistance, and Public Service Access:
Evidence from a Field Experiment in India" was also found; verify at
full-text screening whether this is an earlier version of the same
underlying study (`REPRODUCIBILITY.md` §6) before treating both as
independent evidence.

**Why it matters:** large factorial field experiment (~7,000 households,
Mumbai informal settlements) — candidate primary study for meta-analytic
Family B (administrative assistance and access), a genuinely causal
estimand. Reported result (per the preliminary source description, not yet
independently re-verified against the primary text by this project):
bureaucratic assistance combined with political coordination increased the
likelihood of a municipal water connection by ~19 percentage points among
policy-eligible settlements (~45% of the control mean). Do not combine this
estimate with observational Family A studies (`ANALYSIS_PLAN.md` §3).

## 4. Apio, Thiam & Dinar 2025 — Meta-analysis of water institutions

> Apio, A. T., Thiam, D. R., & Dinar, A. (2025). A Meta-Analysis of Water
> Institutions and Their Performance: Implications for Water Resource
> Management. *Water Resources Management*, 39, 907–938.
> https://doi.org/10.1007/s11269-024-04000-w

**Verification:** Confirmed via web search (RePEc/IDEAS listing giving
volume 39, issue 2; ResearchGate preprint listing). Meta-analysis /
meta-regression of 23 primary studies on water-institution performance,
reporting evidence of publication selection bias favoring positive effects.

**Why it matters:** demonstrates water-governance literature *can* support
quantitative synthesis where primary studies are sufficiently comparable —
and equally demonstrates how heterogeneous operationalizations create
substantial variation, supporting the strict conceptual pooling rules in
`ANALYSIS_PLAN.md`. Because this source is itself a secondary
synthesis, if it or a similar meta-analysis is later included as a
retrieved record, appraise it with AMSTAR 2, not a primary-study
risk-of-bias tool (`RISK_OF_BIAS.md` §1).

## 5. PRISMA 2020

> Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T.
> C., Mulrow, C. D., et al. (2021). The PRISMA 2020 statement: an updated
> guideline for reporting systematic reviews. *BMJ*, 372, n71.
> https://doi.org/10.1136/bmj.n71

**Verification:** Confirmed via web search (prisma-statement.org, PubMed
33782057, multiple institutional repositories). Used for reporting per
`PRISMA_WORKFLOW.md`.

## 6. PRISMA-P 2015

> Moher, D., Shamseer, L., Clarke, M., et al. (2015). Preferred Reporting
> Items for Systematic Review and Meta-Analysis Protocols (PRISMA-P) 2015
> statement. *Systematic Reviews*, 4, 1.
> https://doi.org/10.1186/2046-4053-4-1

**Verification status:** **not independently re-confirmed in this
session** beyond the researcher-supplied citation (publisher domains
blocked; a targeted web search was not run for this specific entry). This
is a very widely cited, standard methodological reference and the citation
details are internally consistent with its well-known form, but treat this
as unverified until a direct check is done. Used for `PROTOCOL.md`'s
PRISMA-P-style structure.

## 7. SWiM 2020

> Campbell, M., McKenzie, J. E., Sowden, A., Katikireddi, S. V., Brennan,
> S. E., Ellis, S., et al. (2020). Synthesis without meta-analysis (SWiM)
> in systematic reviews: reporting guideline. *BMJ*, 368, l6890.
> https://doi.org/10.1136/bmj.l6890

**Verification:** Confirmed via web search (Monash/White Rose/York
repository listings, EQUATOR Network guideline registry, PMC7190266).
Used in `ANALYSIS_PLAN.md` and `PROTOCOL.md` §9 for reporting evidence that
cannot legitimately be meta-analyzed.

## 8. AMSTAR 2

> Shea, B. J., Reeves, B. C., Wells, G., et al. (2017). AMSTAR 2: a
> critical appraisal tool for systematic reviews that include randomised
> or non-randomised studies of healthcare interventions, or both. *BMJ*,
> 358, j4008. https://doi.org/10.1136/bmj.j4008

**Verification status:** **not independently re-confirmed in this
session**, for the same access-blocked reason as PRISMA-P above; this is
likewise a very widely cited, standard instrument and the citation is
internally consistent with its well-known form. Used strictly as a
secondary-review appraisal tool (`RISK_OF_BIAS.md` §1) — explicitly not as
the primary-study risk-of-bias instrument.

## Core methodological principles drawn from this literature

1. Systematic review does not require meta-analysis.
2. Meta-analysis requires meaningful comparability, not merely mathematical convertibility.
3. Administrative-burden literature is methodologically heterogeneous.
4. Water-governance literature can support quantitative synthesis when study measures are sufficiently comparable.
5. Institutional heterogeneity is substantively meaningful.
6. Publication-bias tests are unreliable with very small numbers of studies.
7. The judicial dataset stays separate from household-level evidence synthesis (`PROJECT_SPEC.md` §9).

## Status

This is a preliminary source list of eight methodological/exemplar
references, not a bibliography of the review's evidence base. The
evidence-base bibliography does not exist yet — it is built during Phase 3
onward of `PRISMA_WORKFLOW.md`.
