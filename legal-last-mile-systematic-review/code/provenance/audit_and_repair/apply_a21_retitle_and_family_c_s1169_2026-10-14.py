"""2026-10-14: (1) bring S1169 (Olmstead 2004, Thirsty Colonias) into the Family C SWiM synthesis (k 19 to 20) and (2) apply the PI's open-item A21 ruling (options a + c).

A21: the keyword audit (05_analysis/effect_sizes/FAMILY_FIT_AUDIT_2026-10-04.md) found that many effect-size rows sit outside the wording of the synthesis family they were placed in. The PI ruled (2026-10-14):
(a) retitle the descriptive headings so that they describe the mechanism clusters actually synthesised, and (c) state in the synthesis text and the manuscript methods that Families A, B and C are thematic
mechanism groupings for structured vote counting (SWiM), not homogeneous exposure-outcome pairs. The codes A/B/C in effect_sizes.csv, the study assignments, the table formats read by
sensitivity_analysis.py and the existing rows are untouched. PROJECT_SPEC.md section 8 keeps its pre-evidence wording and gets a dated note; ANALYSIS_PLAN.md gets a dated note.

New titles: A "Legal status, tenure, recognition and governance-arrangement mechanisms"; B "Assistance, participation, trust and external-support mechanisms";
C "Ownership, regulation, institutional-capacity and administrative-structure mechanisms".

Idempotent (each file carries a marker). Run from legal-last-mile-systematic-review/."""
import io
import sys
from pathlib import Path

SW = Path('06_outputs/supplementary')
TITLES = {
    'A': ('Legal recognition and access', 'Legal status, tenure, recognition and governance-arrangement mechanisms'),
    'B': ('Administrative assistance and access', 'Assistance, participation, trust and external-support mechanisms'),
    'C': ('Administrative/legal barriers and access inequality', 'Ownership, regulation, institutional-capacity and administrative-structure mechanisms'),
}
COMMON = ("Families A, B and C are **thematic mechanism groupings used to organise the structured vote count (SWiM)**, not homogeneous exposure–outcome pairs. "
          "Their member studies share a broad theme, not a comparable exposure, comparator and outcome measure; that is why Phase 11 rejected pooling "
          "(`phase11_quantitative_feasibility_judgment.md`; `ANALYSIS_PLAN.md` §2). The `synthesis_family` codes in `effect_sizes.csv` and every study assignment are unchanged; "
          "only the descriptive heading changed. The pre-evidence wording of the families stays in `PROJECT_SPEC.md` §8 (see the dated note there).")
LABEL = {
    'A': ("Family A groups studies whose exposure is a legal status, tenure, recognition or governance arrangement (slum notification, municipal incorporation, regulatory primacy, zoning, "
          "water-user-association membership, land titling, customary governance, participation arrangements). The protocol heading, 'Legal recognition and access', was narrower than what was synthesised."),
    'B': ("Family B groups studies of assistance, participation, trust and external support (bureaucratic assistance with political coordination, community institutional strengthening, "
          "capital-cost contribution, network capital, NGO/CBO trust, external programme funding). Only S085 tests bureaucratic assistance in the protocol's sense; the protocol heading, "
          "'Administrative assistance and access', was narrower than what was synthesised."),
    'C': ("Family C groups studies of ownership, regulation, institutional capacity and administrative structure (private versus public ownership, price regulation, government form, "
          "political proximity, registration status, corruption, administrative category). The protocol heading, 'Administrative/legal barriers and access inequality', "
          "was broader in one respect and narrower in another than what was synthesised."),
}
MARK = 'A21 ruling 2026-10-14'


def rd(p):
    return Path(p).read_text(encoding='utf-8')


def wr(p, t):
    Path(p).write_text(t, encoding='utf-8')


def rep(t, old, new, label):
    assert old in t, f'pattern not found ({label}): {old[:70]!r}'
    return t.replace(old, new, 1)


# ---- SWiM files: retitle + disclosure block (+ Family C S1169) -------------------------------------------------------------------------------------------------------------
for fam, (old_t, new_t) in TITLES.items():
    p = SW / f'family_{fam}_swim_synthesis_2026-09-28.md'
    t = rd(p)
    if MARK in t:
        print(p.name, 'already retitled')
        continue
    t = rep(t, f'# SWiM Synthesis — Family {fam} ({old_t}) — 2026-09-28', f'# SWiM Synthesis — Family {fam} ({new_t}) — 2026-09-28', 'title')
    block = (f"> **What the family label means (added 2026-10-14 under the {MARK}, open item A21).** {LABEL[fam]} {COMMON}\n"
             "> The keyword audit that prompted this is `05_analysis/effect_sizes/FAMILY_FIT_AUDIT_2026-10-04.md`.\n\n")
    t = rep(t, '## Why this family did not proceed to meta-analysis', block + '## Why this family did not proceed to meta-analysis', 'disclosure anchor')
    if fam == 'C':
        top = ("> **Update 2026-10-14 (k 19 to 20, S1169 added).** The PI included Olmstead (2004, *Thirsty Colonias*, Land Economics 80(1):136–150) as S1169 after a full-text read of pages 2–15. "
               "Its one access-relevant estimate (probit on whether a Texas border-county colonia household is served, N = 781; price (rate) regulation of the provider, coefficient −1.1858, SE 0.4163, p = 0.004) "
               "is now a Family C row (`effect_sizes.csv`). Counts below were recomputed on the 20 studies: Negative 9 (was 8), Positive 7 and Mixed 4 unchanged. S1169 sits in the remaining group, not in the "
               "ownership/price cluster, because its outcome is service coverage, not affordability. The 19-study version is in the git history.\n>\n")
        t = rep(t, '> **Update 2026-10-14 (k 20 to 19).**', top + '> **Earlier update 2026-10-14 (k 20 to 19).**', 'top note')
        t = rep(t, 'of the 19 studies (17 originally, plus S470 and\nS471 corrected in from blank on 2026-09-28 — see\n`phase11_blank_family_resolution_2026-09-28.md`; a twentieth, S348, was added by a re-mining pass the same day, see `effect_sizes_remining_2026-09-28.md`, and removed on 2026-10-14), only one genuine',
                'of the 20 studies (17 originally, plus S470 and\nS471 corrected in from blank on 2026-09-28 — see\n`phase11_blank_family_resolution_2026-09-28.md`; S348, added by a re-mining pass the same day, see `effect_sizes_remining_2026-09-28.md`, was removed on 2026-10-14, and S1169 was added the same day), only one genuine', 'k text')
        t = rep(t, 'The other 16 studies each test a\ndistinct', 'The other 17 studies each test a\ndistinct', 'other 16')
        t = rep(t, '| S1162 | India | Panel/cross-sectional multilevel regression | Negative — lower admin. capacity/category → lower access | JBI Cross-Sectional — Some concern |\n',
                '| S1162 | India | Panel/cross-sectional multilevel regression | Negative — lower admin. capacity/category → lower access | JBI Cross-Sectional — Some concern |\n'
                '| S1169 | United States | Cross-sectional probit (781 Texas colonias) | Negative — price-regulated provider → lower probability of service | JBI Cross-Sectional — Some concern |\n', 'table row')
        t = rep(t, '## The remaining 14 studies\n\nThe other 14 studies (S174, S590, S593, S606, S631, S879, S947, S1032, S1062, S1136, S1143,\nS1146, S1162, and S470 — S470 groups more naturally here than with the ownership/price\ncluster, since it concerns eligibility-based tariff *enrollment*, not ownership structure)',
                '## The remaining 15 studies\n\nThe other 15 studies (S174, S590, S593, S606, S631, S879, S947, S1032, S1062, S1136, S1143,\nS1146, S1162, S1169, and S470 — S470 groups more naturally here than with the ownership/price\ncluster, since it concerns eligibility-based tariff *enrollment*, not ownership structure; S1169 tests\nprice regulation of the provider, but its outcome is the probability of being served at all, not affordability)', 'remaining')
        t = rep(t, 'local-government administrative category. **None shares', 'local-government administrative category, and price regulation of the provider against the probability of service in unserved border-county settlements. **None shares', 'mechanism list')
        t = rep(t, 'Mechanical for 18 of 19 studies', 'Mechanical for 19 of 20 studies', 'mechanical')
        t = rep(t, '(2) the remaining 14\nstudies', '(2) the remaining 15\nstudies', 'grouping')
        t = rep(t, 'Vote count across all 19 studies, as extracted.', 'Vote count across all 20 studies, as extracted.', 'vote')
        t = rep(t, 'The 7/8/4 split therefore\nmust not be read as "7 beneficial, 8 adverse".', 'The 7/9/4 split therefore\nmust not be read as "7 beneficial, 9 adverse".', 'split warn')
        t = rep(t, '| Negative | 8 | S471, S526, S606, S631, S1032, S1038, S1146, S1162 |', '| Negative | 9 | S471, S526, S606, S631, S1032, S1038, S1146, S1162, S1169 |', 'neg row')
        t = rep(t, 'Unlike Family A (58% positive) or Family B (83% positive), **Family C shows no dominant\ndirection across its full 19-study set** — 7 positive, 8 negative, 4 mixed,',
                'Unlike Family A (61% positive) or Family B (83% positive), **Family C shows no dominant\ndirection across its full 20-study set** — 7 positive, 9 negative, 4 mixed,', 'dominant')
        t = rep(t, 'averaging it into the full 19-study vote count', 'averaging it into the full 20-study vote count', 'avg')
        t = rep(t, 'The full-family 7/8/4 split is not meaningfully robust to any single exclusion — it is already\nclose to an even three-way split, so removing or reclassifying any one or two studies could flip\nwhich direction is nominally "most common" without changing the substantive conclusion (there is\nno dominant direction).',
                'The full-family 7/9/4 split is not meaningfully robust to any single exclusion — no direction holds a\nmajority (the largest, negative, is 9 of 20), so removing or reclassifying any one or two studies could change\nwhich direction is nominally "most common" without changing the substantive conclusion (there is\nno dominant direction).', 'robust')
        t = rep(t, 'The\n14 non-ownership studies span ROBINS-I', 'The\n15 non-ownership studies span ROBINS-I', 'non-ownership')
        t = rep(t, 'spread across 14 unrelated mechanisms', 'spread across 15 unrelated mechanisms', 'unrelated')
        t = rep(t, '19 studies testing 14+\ndistinct mechanisms cannot be meaningfully reduced to a single directional headline, and this\nsynthesis\'s own 7/8/4 split',
                '20 studies testing 15+\ndistinct mechanisms cannot be meaningfully reduced to a single directional headline, and this\nsynthesis\'s own 7/9/4 split', 'limitations')
    wr(p, t)
    print(p.name, 'updated')

# ---- PROJECT_SPEC.md: dated note under section 8 (protocol wording untouched) -------------------------------------------------------------------------------------------------
NOTE_SPEC = (
    f"> **Dated note, 2026-10-14 ({MARK}, open item A21; the protocol wording above is unchanged).** The three family titles above were written before any evidence was gathered. "
    "A keyword audit of the effect-size rows (`05_analysis/effect_sizes/FAMILY_FIT_AUDIT_2026-10-04.md`) found that many assigned rows sit outside the wording of their family, so the PI ruled "
    "that the synthesis documents carry descriptive titles that reflect the rule-type mechanism clusters actually synthesised: **A — legal status, tenure, recognition and governance-arrangement mechanisms; "
    "B — assistance, participation, trust and external-support mechanisms; C — ownership, regulation, institutional-capacity and administrative-structure mechanisms.** "
    "The codes A, B and C, every study assignment and the rule that the families are not pooled are unchanged. The families are thematic mechanism groupings for structured vote counting (SWiM), "
    "not homogeneous exposure–outcome pairs, and the manuscript methods say so. The protocol is an unregistered draft, so no registration is amended.\n\n")
p = Path('PROJECT_SPEC.md')
t = rd(p)
if MARK not in t:
    t = rep(t, 'consistent.\n\n## 9. Relationship with the Global Water Law Judicial Decisions Dataset', 'consistent.\n\n' + NOTE_SPEC + '## 9. Relationship with the Global Water Law Judicial Decisions Dataset', 'spec')
    wr(p, t)
    print('PROJECT_SPEC.md noted')

# ---- ANALYSIS_PLAN.md ---------------------------------------------------------------------------------------------------------------------------------------------------------------
NOTE_PLAN = (
    f"\n> **Dated note, 2026-10-14 ({MARK}, open item A21).** Families A, B and C are thematic mechanism groupings used to organise structured vote counting (SWiM), not homogeneous exposure–outcome pairs; "
    "the synthesis documents now carry descriptive titles for the mechanism clusters they contain (see the dated note in `PROJECT_SPEC.md` §8). The tree above is applied per family exactly as written, "
    "and the family codes are unchanged.\n")
p = Path('ANALYSIS_PLAN.md')
t = rd(p)
if MARK not in t:
    t = rep(t, 'not once globally — Family A, B, and C may land in different branches.\n', 'not once globally — Family A, B, and C may land in different branches.\n' + NOTE_PLAN, 'plan')
    wr(p, t)
    print('ANALYSIS_PLAN.md noted')

# ---- Phase 11 note: bring the stale row count current -------------------------------------------------------------------------------------------------------------------------------
p = SW / 'phase11_quantitative_feasibility_judgment.md'
t = rd(p)
old = 'leaving 59 rows: Family A 19, B 6, C 19, 15 non-fits. The verdict'
if old in t:
    t = rep(t, old, 'leaving 59 rows: Family A 19, B 6, C 19, 15 non-fits. Later the same day S589 (Family A) left and S1169 (Family C, Olmstead 2004) was added, so the current figures are 59 rows: Family A 18, B 6, C 20, 15 non-fits (the family titles were also made descriptive under the A21 ruling; the codes are unchanged). The verdict', 'phase11')
    wr(p, t)
    print('phase11 note updated')

# ---- README -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
p = Path('README.md')
t = rd(p)
old = 'family** (Family A — legal recognition and access; Family B — administrative\nassistance and access; Family C — administrative/legal barriers and access\ninequality; `PROJECT_SPEC.md` §8)'
if old in t:
    t = rep(t, old, 'family** (Family A — legal recognition and access; Family B — administrative\nassistance and access; Family C — administrative/legal barriers and access\ninequality; `PROJECT_SPEC.md` §8; since 2026-10-14 the synthesis documents retitle them as thematic\nmechanism groupings, A21)', 'readme')
    wr(p, t)
    print('README noted')
