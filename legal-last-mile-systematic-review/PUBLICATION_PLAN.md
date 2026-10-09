# Publication Plan

## 1. Relationship to the dissertation

The standalone review paper establishes: what empirical literature exists;
which mechanisms have empirical support; which mechanisms have only
theoretical or doctrinal support; which populations and jurisdictions have
been studied; which outcomes have been measured; where quantitative evidence
does and does not exist; methodological weaknesses; and the remaining
research gap. It does **not** attempt to prove the dissertation. The
dissertation subsequently builds on the review's findings, the comparative
doctrinal analysis, the judicial-dataset analysis, and further empirical
work (`PROJECT_SPEC.md` §10).

## 2. Publication ethics and overlap

When incorporating the review into the dissertation:

1. Cite the published article.
2. Disclose its relationship to the doctoral project.
3. Check the publisher's dissertation-reuse rules before reproducing
   substantial text or figures.
4. Avoid submitting substantially identical material to more than one venue.
5. Do not republish the same meta-analytic results as a "new" study without
   a substantive new contribution.
6. Clearly label any updated/re-run review as an update, with a version
   number.
7. Preserve versioned datasets and scripts (`REPRODUCIBILITY.md` §8).
8. Document all changes between the published review and any dissertation
   version in `CHANGELOG.md`.

## 3. Candidate journal families

Evaluate against fit, not prestige alone (§4).

- **Socio-legal:** International Journal of Law in Context; Law & Policy; Journal of Empirical Legal Studies
- **Regulatory governance:** Regulation & Governance; International Review of Administrative Sciences
- **Public administration:** Journal of Public Administration Research and Theory
- **Water governance:** Water Policy; Utilities Policy; Journal of Water, Sanitation and Hygiene for Development; Urban Water Journal

## 4. Selection criteria (in priority order)

1. Methodological fit
2. Substantive fit
3. Audience
4. Article type
5. Word limit
6. Open-access policy
7. Acceptance of interdisciplinary empirical-legal research

Before submission, verify current: aims and scope; article types; word
limits; open-access options; review format; data-availability policies;
preregistration expectations; AI-disclosure policies; duplicate-publication
rules. None of this has been verified yet — no journal has been selected,
and no submission timeline exists at this stage of the project.

## 5. Standalone paper structure

See `07_manuscript/draft/manuscript_outline.md` for the section-by-section
outline this maps to.

1. Title (working, per `PROTOCOL.md` §1)
2. Abstract (Background / Objective / Methods / Results / Conclusions)
3. Introduction (access problem; infrastructure vs. realized access;
   administrative dimension; fragmented literature; research gap; research
   question; contribution)
4. Conceptual Framework (Legal Last Mile; legal and administrative access
   conditions; eligibility; burden; discretion and accommodation; enforcement)
5. Methods (review design; research question; eligibility criteria; search
   strategy; databases; screening; extraction; risk of bias; evidence
   classification; quantitative synthesis rules)
6. Search and Study Selection (results; duplicate removal; screening; PRISMA flow)
7. Study Characteristics (geography; study design; population; legal
   mechanism; service type; outcome)
8. Risk of Bias (study-level appraisal; legal-institutional evidence
   appraisal; overall evidence limitations)
9. Quantitative Evidence (effect-measure availability; candidate synthesis
   families; included effect estimates)
10. Meta-Analysis (only if justified)
11. Heterogeneity (statistical; institutional; legal; methodological)
12. Comparative Findings (eligibility; burden; discretion; accommodation; enforcement)
13. Discussion (what evidence supports; what it qualifies; what it does not
    establish; institutional differences; implications for administrative
    law and sanitation governance)
14. Limitations (literature heterogeneity; measurement; language;
    publication bias; jurisdictional coverage; causal inference; database
    limitations)
15. Future Research (judicial dataset; administrative records; process
    tracing; interviews if justified; comparative legal analysis)
16. Conclusion — must answer: *what does the existing evidence actually
    allow us to conclude?*

## 6. Status

No manuscript drafting has begun beyond the outline. No journal has been
selected. This plan is written ahead of the search precisely so that
publication-shape decisions (journal fit, structure) do not retroactively
pressure the evidence synthesis.

## 7. Post-publication idea: agentifying the review's methodology

**Not actionable now — noted here so it isn't lost by the time it is.**
Once this review is published, its codebase (deduplication, screening,
extraction, and evidence-classification scripts under `code/`, run against
`CODEBOOK.md`'s 92-field schema and `INCLUSION_EXCLUSION.md`'s E01–E12
criteria) is a plausible candidate for Paper2Agent-style "agentification"
(Miao, Davis, Zhang, Pritchard & Zou, "Reimagining research papers as
interactive and reliable AI agents," *Nature*, 2026,
[github.com/jmiao24/Paper2Agent](https://github.com/jmiao24/Paper2Agent)).
Unlike most legal scholarship, this review has a real, reproducible,
scripted methodology rather than only a narrative account of one — which is
the specific precondition Paper2Agent's tool-extraction pipeline requires.

The resulting agent could let another researcher point it at their own
full-text corpus and have it apply this review's eligibility screen,
92-field extraction schema, and mechanism/outcome evidence-classification
logic to their own jurisdiction or service sector — making the
methodology reusable, not just reported. Even the non-code parts (the
conceptual framework, the codebook, the risk-of-bias appraisal framework)
could be exposed as queryable MCP resources. This would be citable
directly against the Paper2Agent paper in the dissertation's contribution
or future-research discussion.

This is deliberately deferred: the review is still mid-screening, has no
manuscript yet, and Paper2Agent operates on a published paper plus its
codebase — both preconditions this project doesn't yet meet.
