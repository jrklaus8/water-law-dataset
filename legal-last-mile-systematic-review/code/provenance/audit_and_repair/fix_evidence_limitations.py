import io
P='04_quality/risk_of_bias/2026-09-28_evidence_limitations.md'
s=open(P,encoding='utf-8').read()
def rep(old,new,count=1):
    global s
    assert s.count(old)==count,(s.count(old),old[:70])
    s=s.replace(old,new)

rep("""This narrative is therefore the first
version of this file that can actually do what `RISK_OF_BIAS.md` §3 asks: summarize
limitations of the evidence base **as a whole**, informed by real ratings rather than corpus
composition alone.
""","""This narrative is therefore the first
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
share) get slightly stronger, not weaker.
""")

rep("""For the roughly 1,050 studies rated via CASP, MMAT, or the condensed Legal
Framework method, most individual domains""","""For the 918 studies rated via CASP (263), MMAT (206), or the condensed Legal
Framework method (449) (an earlier draft said "roughly 1,050"), most individual domains""")

rep("""455 Legal-Framework/`NONE`-tool studies were deliberately left as free text""","""455 Legal-Framework/`NONE`-tool studies were deliberately left as free text (counts as of that
pass; 26 studies were reclassified afterwards, and an audit re-sync on 2026-09-28 corrected 22
`study_design_class` values that the later reclassifications had left stale — see that
document's audit addendum)""")

rep("""| Legal Institutional Evidence Appraisal Framework (doctrinal/documentary/jurimetric) | 433 | 37% |
| CASP Qualitative | 245 | 21% |
| MMAT (mixed methods) | 207 | 18% |
| JBI Cross-Sectional | 166 | 14% |
| ROBINS-I (non-randomized intervention/quasi-experimental) | 72 | 6% |
| AMSTAR 2 (secondary systematic reviews) | 22 | 2% |""","""| Legal Institutional Evidence Appraisal Framework (doctrinal/documentary/jurimetric) | 449 | 39% |
| CASP Qualitative | 263 | 23% |
| MMAT (mixed methods) | 206 | 18% |
| JBI Cross-Sectional | 140 | 12% |
| ROBINS-I (non-randomized intervention/quasi-experimental) | 63 | 5% |
| AMSTAR 2 (secondary systematic reviews) | 24 | 2% |""")

rep("""at more than 3x the corpus size**: only 77 of 1,162 studies (7% — the 72 ROBINS-I plus 5 RoB
2) use a design capable of supporting a causal claim about a legal/administrative mechanism's
effect on access. The other 93% are either doctrinal/documentary analysis (37%), qualitative
research (21%), mixed-methods (18%), or cross-sectional observational association (14%).""","""at more than 3x the corpus size**: only 68 of 1,162 studies (6% — the 63 ROBINS-I plus 5 RoB
2; an earlier draft said "77 (7%)") use a design capable of supporting a causal claim about a
legal/administrative mechanism's effect on access. The other 94% are doctrinal/documentary
analysis (39%), qualitative research (23%), mixed-methods (18%), cross-sectional observational
association (12%), or secondary reviews and no-tool studies (3%).""")

rep("""populated for 365 of the
433 Legal Framework studies (84%)""","""populated for 389 of the
449 Legal Framework studies (87%)""")

rep("""CASP Qualitative batch (245 studies) and the MMAT batch (207 studies) — 39% of the entire
corpus between them""","""CASP Qualitative batch (263 studies) and the MMAT batch (206 studies) — 40% of the entire
corpus between them""")
rep("""that these 452 studies are poorly conducted""","""that these 469 studies are poorly conducted""")

rep("""20 Family A, 6 Family B, and 17 Family C studies with a genuine, poolable effect size (plus
18 studies whose family assignment remains genuinely unresolved)""","""20 Family A, 6 Family B, and 17 Family C studies with a genuine, poolable effect size (plus
18 studies whose family assignment remained unresolved at that point — updated later the same
day: after the 9-row blank-family follow-up and the S348 addition, `effect_sizes.csv` holds 62
rows, Family A 20 / B 6 / C 20, with 16 rows left blank on a documented, reasoned non-fit basis,
`phase11_blank_family_resolution_2026-09-28.md`)""")

rep("""433 of 1,162 studies (37%) carry `risk_of_bias_tool` = "Legal Institutional Evidence
Appraisal Framework" — up from 20% at the 366-study snapshot""","""449 of 1,162 studies (39%) carry `risk_of_bias_tool` = "Legal Institutional Evidence
Appraisal Framework" — up from 20% at the 366-study snapshot""")
rep("""actually *reduced*
the raw tag count from 573 to 433 by correcting 148 misclassified studies onto validated
tools instead).""","""actually *reduced*
the raw tag count by moving 148 misclassified studies onto validated tools: 573 − 148 = 425,
which later rose to 449 when 24 studies were moved *into* the framework — 9 reverted after an
over-correction, 8 from the previously unassigned batch, 6 JBI mis-tags, and 1 other (S409)).""")
rep("""of all 433 (`LegalFramework_batch_2026-09-28.md`) only strengthens""","""of the framework studies (`LegalFramework_batch_2026-09-28.md` covers 434 — the 425 plus a
9-study follow-up; the other 15 were appraised in the unassigned-studies and reassignment
batches, generally more thinly) only strengthens""")
rep("""for the 365 studies with that data on record; the
other 8 domains — including legal source accuracy, sampling transparency, and researcher
reflexivity — are "not assessable" for all 433.""","""for the 389 studies with that data on record; the
other 8 domains — including legal source accuracy, sampling transparency, and researcher
reflexivity — are "not assessable" for all 449.""")

rep("""- **Family C (administrative/legal barriers, 17 effect-size rows):**""","""- **Family C (administrative/legal barriers, 20 effect-size rows; 17 in the original Phase 11 judgment):**""")

s=s.rstrip('\n')+"""

## Two further caveats surfaced by the 2026-09-28 audit

**1. Some appraisals rest on abstract- or metadata-level extraction only.** 71 of the 1,162
studies (6.1%) carry an `extraction_note` stating they were extracted from the published
abstract, introduction, or repository metadata only, because the full text was never
obtained at extraction time (CASP 30, MMAT 14, JBI Cross-Sectional 11, Legal Framework 10,
AMSTAR 2 5, RoB 2 1). Their appraisals are honest about this — the CASP entries, for example,
record "Can't tell" on 7 or 8 of 10 items — and S366 (RoB 2) is explicitly labelled
LOW-CONFIDENCE. But a reader tabulating ratings by tool should not treat those 71 as
equivalent to full-text appraisals; filter on `extraction_note` before doing so. This
limitation was previously documented only in scattered `CHANGELOG.md` entries, not in any
corpus-level summary.

**2. A "High concern" JBI rating usually means "sparse extraction", not "flawed study".** 59
of the 140 JBI Cross-Sectional studies (42%) are rated "High concern" (`RISK_OF_BIAS.md` §4
already states this in the rating text: fewer than 3 of 8 items answerable "Yes" from this
project's extraction fields). It measures how much methodological detail the extraction
captured, not the study's actual conduct, and must not be read as a finding that 42% of
cross-sectional studies in this corpus are methodologically poor.
"""
open(P,'w',encoding='utf-8').write(s)
print('ok')
