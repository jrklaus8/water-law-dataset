#!/usr/bin/env python3
"""Sensitivity analysis of the three SWiM syntheses (Families A, B, C) and of the descriptive counts.

Question answered: does any stated conclusion move if the weakest inputs are removed or the non-independent ones collapsed?

Scenarios (each applied to the study lists in the SWiM documents):
  S0 baseline
  S1 drop the abstract-/metadata-only extractions           (05_analysis/sensitivity/abstract_only_extractions_2026-09-28.csv logic)
  S1b drop every strong or moderate row of the sparse-record audit (added 2026-10-04: the prefix-based abstract-only set misses shallow extractions that DO carry effect-size rows)
  S2 drop effect-size rows for studies not flagged quantitative_synthesis_eligible   (S589)
  S3 collapse linked reports that share underlying data     (linked_reports_2026-09-28.csv, same_underlying_data = yes)
  S4 drop the coding judgment call in Family A               (S404: a lower water-poverty score read as favourable; S358, the other call, left the families under A26)
  (S4b, which dropped S1140 and S1136, was retired on 2026-10-14: the A29 ruling moved both to the reasoned non-fits, so the primary count already excludes them. Scenario labels are not renumbered, so dated documents still point at the right scenario.)
  S4c recode S471 as Null            (its fully adjusted estimate is not significant; the primary estimate is the organisation-only model, kept in the main count by the author)
  S4e recode S879 as Null            (household water access alone was null; payment compliance, a utility-side outcome, rose by 30 percentage points; kept as Mixed in the main count by the author)
  S5 S1 to S4c and S4e together
  S4d drop every study whose raw coefficient sign and substantive direction come apart (inverted outcome polarity or a restated pole), i.e. keep only studies where '+' means Favourable and '-' means Unfavourable

Pre-stated conclusion tests (written before the numbers were computed, so they cannot be tuned to the result):
  A: a majority (> 50%) of studies is concordant with "legal recognition/eligibility improves access" (Favourable in the substantive-direction table of the Family A document)
  B: every study is Favourable or Mixed in substantive direction (none Unfavourable or Null)
  C: no single category holds a majority of studies ("no dominant direction"), by raw coefficient sign AND by substantive direction
Since 2026-10-14 each family document carries two tables: the raw coefficient sign (positive/negative/null/mixed) and the substantive direction for household access, affordability or equity
(Favourable/Unfavourable/Null/Mixed); they were conflated before (see SWIM_DIRECTION_CODING_2026-10-14.csv for how the second is derived from the first).

Inputs are the SWiM documents themselves (single source of truth for the direction coding; a test checks them against SWIM_DIRECTION_CODING_2026-10-14.csv) and the CSV databases. Deterministic;
rewrites 05_analysis/sensitivity/SENSITIVITY_ANALYSIS_2026-09-28.md and sensitivity_scenarios_2026-09-28.csv.
Run from the project root:  python3 code/analysis/sensitivity_analysis.py
"""
import csv, re, sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import current_figures as cf  # noqa: E402
import audit_sparse_records as asr  # noqa: E402

ROOT = cf.ROOT
SW = ROOT / '06_outputs/supplementary'
OUT_MD = ROOT / '05_analysis/sensitivity/SENSITIVITY_ANALYSIS_2026-09-28.md'
OUT_CSV = ROOT / '05_analysis/sensitivity/sensitivity_scenarios_2026-09-28.csv'


def swim_text(fam):
    return (SW / f'family_{fam}_swim_synthesis_2026-09-28.md').read_text(encoding='utf-8')


def parse_signs(fam):
    t = swim_text(fam)
    sec = t[t.index('\n## Results'):]
    sec = sec[:sec.index('\n## ', 5)]
    signs = {}
    for m in re.finditer(r'^\| (Positive|Negative|Null|Mixed)[^|]*\| (\d+) \| ([^|]*)\|', sec, re.M):
        ids = re.findall(r'S\d+', m.group(3))
        assert len(ids) == int(m.group(2)), (fam, m.group(1))
        signs.update({i: m.group(1).lower() for i in ids})
    return signs


def parse_substantive(fam):
    """Substantive direction (Favourable / Unfavourable / Null / Mixed) from the family document's second Results table; rows read '| Favourable | 13 (72%) | S057, ... |'."""
    t = swim_text(fam)
    sec = t[t.index('\n## Results'):]
    sec = sec[:sec.index('\n## ', 5)]
    out = {}
    for m in re.finditer(r'^\| (Favourable|Unfavourable|Null|Mixed)[^|]*\| (\d+) \((\d+(?:\.\d+)?)%\) \| ([^|]*)\|', sec, re.M):
        ids = re.findall(r'S\d+', m.group(4))
        assert len(ids) == int(m.group(2)), (fam, m.group(1))
        out.update({i: m.group(1).lower() for i in ids})
    return out


def parse_concordance():
    """Family A concordance with 'recognition/eligibility improves access': the Favourable / Unfavourable / Null rows of its substantive table."""
    return {i: {'favourable': 'concordant', 'unfavourable': 'counter', 'null': 'null', 'mixed': 'mixed'}[v] for i, v in parse_substantive('A').items()}


RECODE_S471 = {'S471'}                  # primary estimate significant, fully adjusted estimate not
RECODE_S879 = {'S879'}                  # household access alone null, payment compliance up
FAVOURABLE_IF = {('positive', 'favourable'), ('negative', 'unfavourable')}   # sign and valence agree: '+' is Favourable and '-' is Unfavourable


def scenarios():
    es_ids = {r['study_id'] for r in cf.read('es')}
    ed = {r['study_id']: r for r in cf.read('ed')}
    em = {r['study_id']: r for r in cf.read('em')}
    links = cf.read('links')
    abstract_only = {s for s, r in ed.items() if r['extraction_note'].startswith(cf.ABSTRACT_ONLY_PREFIXES)}
    not_eligible = {s for s in es_ids if em[s]['quantitative_synthesis_eligible'] != 'TRUE'}
    # collapse: for each definite link, drop the later member (keep the first-listed study) if both are in the analysed set
    signs = {f: parse_signs(f) for f in 'ABC'}
    in_families = {s for f in 'ABC' for s in signs[f]}
    collapse_drop = {r['study_id_b'] for r in links if r['same_underlying_data'] == 'yes' and r['study_id_a'] in in_families and r['study_id_b'] in in_families}
    subst = {f: parse_substantive(f) for f in 'ABC'}
    for f in 'ABC':
        assert set(signs[f]) <= es_ids, f'{f}: SWiM document lists a study not in effect_sizes.csv'
        assert set(signs[f]) == set(subst[f]), f'{f}: the raw-sign and substantive-direction tables do not cover the same studies'
    shallow = {r['study_id'] for r in asr.audit() if r['strength'] in ('strong', 'moderate')}
    diverge = {s for f in 'ABC' for s, v in signs[f].items() if v in ('positive', 'negative') and (v, subst[f][s]) not in FAVOURABLE_IF}   # sign and valence come apart
    S = {
        'S0 baseline': set(),
        'S1 drop abstract-only extractions': abstract_only,
        'S1b drop sparse-audit strong+moderate rows': shallow,
        'S2 drop rows for studies not flagged eligible': not_eligible,
        'S3 collapse linked reports (same underlying data)': collapse_drop,
        'S4 drop the Family A coding judgment call (S404; S358 left the families under A26)': {'S404'},
        'S4c recode S471 as Null (fully adjusted estimate not significant)': set(),
        'S4e recode S879 as Null (household water access alone)': set(),
    }
    S['S5 S1 to S4c and S4e together'] = set().union(*[v for k, v in S.items() if k != 'S0 baseline'])
    S['S4d drop every study whose raw sign and substantive direction come apart'] = diverge
    rows = []
    for name, drop in S.items():
        recode = (RECODE_S471 if name.startswith(('S4c', 'S5')) else set()) | (RECODE_S879 if name.startswith(('S4e', 'S5')) else set())
        rec = {'scenario': name, 'dropped_studies_in_families': ';'.join(sorted((d for d in drop if any(d in signs[f] for f in 'ABC')), key=lambda x: int(x[1:]))), 'recoded_as_null': ';'.join(sorted(recode))}
        for f in 'ABC':
            keep = [s for s in signs[f] if s not in drop]
            raw = {s: ('null' if s in recode else signs[f][s]) for s in keep}
            sub = {s: ('null' if s in recode else subst[f][s]) for s in keep}
            c, cs = Counter(raw.values()), Counter(sub.values())
            rec[f'{f}_k'] = len(keep)
            for lab in ('positive', 'negative', 'null', 'mixed'):
                rec[f'{f}_{lab}'] = c.get(lab, 0)
            rec[f'{f}_favourable'], rec[f'{f}_unfavourable'], rec[f'{f}_subst_null'], rec[f'{f}_subst_mixed'] = (cs.get(x, 0) for x in ('favourable', 'unfavourable', 'null', 'mixed'))
        rec['A_concordant'], rec['A_counter'], rec['A_null_concordance'] = rec['A_favourable'], rec['A_unfavourable'], rec['A_subst_null']
        rec['A_concordant_pct'] = round(100 * rec['A_concordant'] / rec['A_k'], 1) if rec['A_k'] else ''
        rec['A_test_majority_concordant'] = 'holds' if rec['A_k'] and rec['A_concordant'] * 2 > rec['A_k'] else 'FAILS'
        rec['B_test_none_negative_or_null'] = 'holds' if rec['B_k'] and rec['B_unfavourable'] == 0 and rec['B_subst_null'] == 0 else 'FAILS'
        rec['C_test_no_dominant_sign'] = 'holds' if rec['C_k'] and max(rec[f'C_{l}'] for l in ('positive', 'negative', 'null', 'mixed')) * 2 <= rec['C_k'] else 'FAILS'
        rec['C_test_no_dominant_direction'] = 'holds' if rec['C_k'] and max(rec[f'C_{l}'] for l in ('favourable', 'unfavourable', 'subst_null', 'subst_mixed')) * 2 <= rec['C_k'] else 'FAILS'
        rows.append(rec)
    return rows, abstract_only, not_eligible, collapse_drop, signs


def _fam_of(sid):
    return [f for f in 'ABC' if sid in parse_signs(f)]


def abs_line(abstract_only):
    es_ids = {r['study_id'] for r in cf.read('es')}
    hit = sorted(abstract_only & es_ids, key=lambda x: int(x[1:]))
    if not hit:
        return f"- **Abstract-only extractions ({len(abstract_only)} studies, prefix definition):** none has an `effect_sizes.csv` row, so S1 leaves every family unchanged. It matters for descriptive counts only (below)."
    return f"- **Abstract-only extractions ({len(abstract_only)} studies, prefix definition):** {len(hit)} have an `effect_sizes.csv` row ({', '.join(hit)}); S1 removes them from the families."


def link_line():
    es_ids = {r['study_id'] for r in cf.read('es')}
    yes = [r for r in cf.read('links') if r['same_underlying_data'] == 'yes']
    inv = sorted({x for r in yes for x in (r['study_id_a'], r['study_id_b']) if x in es_ids}, key=lambda x: int(x[1:]))
    return (f"- **Linked reports:** {len(yes)} definite same-data links; {len(inv)} {'involves' if len(inv) == 1 else 'involve'} a study that has an effect-size row ({', '.join(f'{i} (Family {_fam_of(i)[0] if _fam_of(i) else chr(8212)})' for i in inv) or 'none'}), so S3 "
            + ("changes nothing in A, B or C (only one member of each linked pair has an effect-size row, so there is no second member to remove)." if not any(r['study_id_a'] in inv and r['study_id_b'] in inv for r in yes) else "removes the later member of a linked pair in which both members have an effect-size row."))


def elig_line(not_eligible):
    ne = sorted(not_eligible, key=lambda x: int(x[1:]))
    return f"- **Studies with an effect-size row but not flagged eligible ({', '.join(ne) or 'none'}):** " + ('; '.join(f"{i} is in Family {'/'.join(_fam_of(i)) or '—'}" for i in ne) or 'none') + f"; S2 removes {'it' if len(ne) == 1 else 'them'}."


def shallow_line(rows):
    r = next(x for x in rows if x['scenario'].startswith('S1b'))
    base = rows[0]
    return (f"- **Sparse-audit strong and moderate rows (S1b):** removes {len(r['dropped_studies_in_families'].split(';')) if r['dropped_studies_in_families'] else 0} study(ies) from the families ({r['dropped_studies_in_families'] or 'none'}); "
            f"Family A goes from k = {base['A_k']} to {r['A_k']}, B from {base['B_k']} to {r['B_k']}, C from {base['C_k']} to {r['C_k']}. "
            "The sparse-audit signals are heuristics (`05_analysis/descriptive/SPARSE_RECORD_AUDIT_2026-10-04.md`).")


def descriptive_drop_abstract_only(abstract_only):
    ed = cf.read('ed')
    kept = [r for r in ed if r['study_id'] not in abstract_only]
    full, sub = Counter(cf.tool_of(r['risk_of_bias_tool']) for r in ed), Counter(cf.tool_of(r['risk_of_bias_tool']) for r in kept)
    return len(ed), len(kept), full, sub


def render(rows, abstract_only, not_eligible, collapse_drop, signs):
    n_all, n_kept, full, sub = descriptive_drop_abstract_only(abstract_only)
    fails = [(r['scenario'], k) for r in rows for k in ('A_test_majority_concordant', 'B_test_none_negative_or_null', 'C_test_no_dominant_sign', 'C_test_no_dominant_direction') if r[k] == 'FAILS']
    L = ["# Sensitivity analysis of the SWiM syntheses (generated — do not edit by hand)", "",
         "Generated by `code/analysis/sensitivity_analysis.py`. Direction coding (raw coefficient sign and substantive direction) is read from the SWiM documents themselves; nothing was re-coded here.",
         "Conclusion tests were fixed before the numbers were computed (see the script's docstring).", "",
         "## Headline", "",
         ("**No stated conclusion changes under any scenario.**" if not fails else "**At least one stated conclusion fails under some scenario:** " + "; ".join(f"{s} — {k}" for s, k in fails)) +
         f" Families A, B and C rest on {rows[0]['A_k']}, {rows[0]['B_k']} and {rows[0]['C_k']} studies; the scenarios remove at most {max(len(r['dropped_studies_in_families'].split(';')) if r['dropped_studies_in_families'] else 0 for r in rows)} of them.", "",
         "## Why several scenarios change nothing (or not)", "",
         abs_line(abstract_only),
         link_line(),
         elig_line(not_eligible),
         shallow_line(rows), "",
         "## Family results by scenario", "",
         "| Scenario | Dropped (in families) | Recoded | A k | A raw +/-/null | A Fav/Unfav/null | A test | B k | B Fav/mixed | B test | C k | C raw +/-/mixed | C Fav/Unfav/mixed | C tests (sign, direction) |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        L.append(f"| {r['scenario']} | {r['dropped_studies_in_families'] or '—'} | {r['recoded_as_null'] or '—'} | {r['A_k']} | {r['A_positive']}/{r['A_negative']}/{r['A_null']} | {r['A_favourable']}/{r['A_unfavourable']}/{r['A_subst_null']} ({r['A_concordant_pct']}%) | {r['A_test_majority_concordant']} | "
                 f"{r['B_k']} | {r['B_favourable']}/{r['B_subst_mixed']} | {r['B_test_none_negative_or_null']} | {r['C_k']} | {r['C_positive']}/{r['C_negative']}/{r['C_mixed']} | {r['C_favourable']}/{r['C_unfavourable']}/{r['C_subst_mixed']} | {r['C_test_no_dominant_sign']}, {r['C_test_no_dominant_direction']} |")
    L += ["", "Tests: **A** — more than half of the studies are Favourable (concordant with \"recognition/eligibility improves access\") in the substantive-direction table;",
          "**B** — no study is Unfavourable or Null in substantive direction; **C** — no single category holds a majority, by raw coefficient sign and by substantive direction. "
          "The raw sign is the sign of the reported estimate; the substantive direction is its meaning for household access, affordability or equity once the outcome polarity and the exposure pole are taken into account "
          "(`05_analysis/effect_sizes/SWIM_DIRECTION_CODING_2026-10-14.csv`). **S4c** recodes S471 (significant in its organisation-only model, not after full adjustment) as Null; **S4e** recodes S879 as Null (household water access alone was null; the 30-point rise was in payment compliance); "
          "**S4d** keeps only the studies where the two readings agree ('+' is Favourable, '-' is Unfavourable), which tests whether the Family A and C conclusions depend on the inverted-outcome and restated-pole judgments.", "",
          f"## Descriptive counts with the {len(abstract_only)} abstract-only extractions removed", "",
          f"Studies: {n_all:,} → {n_kept:,}. Risk-of-bias tool distribution:", "", "| Tool | All | Without abstract-only | Change |", "|---|---|---|---|"]
    for t in full:
        L.append(f"| {t} | {full[t]} | {sub[t]} | {sub[t] - full[t]:+d} |")
    rank = lambda c: [t for t, _ in sorted(c.items(), key=lambda kv: (-kv[1], kv[0]))]
    biggest = sorted(((full[t] - sub[t], t) for t in full), reverse=True)[:3]
    L += ["", ("Every tool population keeps its rank order" if rank(full) == rank(sub) else "The rank order of tool populations changes") +
          "; the largest reductions are " + ", ".join(f"{t} ({d})" for d, t in biggest) + ".", "",
          "## What this does not test", "",
          "- The direction coding itself (a judgment by the same AI; a human should re-code a sample).",
          "- Whether other studies belong in the families, or whether unextracted studies would change them.",
          "- Overlap between separate papers that were not flagged as linked (e.g. S526 and S539 both use large US utilities; `linked_reports_2026-09-28.csv` LR09, audit-inferred).",
          "- Any effect size: none is pooled, so there is nothing to test for heterogeneity or publication bias."]
    return "\n".join(L) + "\n"


if __name__ == '__main__':
    rows, ab, ne, cd, signs = scenarios()
    with open(OUT_CSV, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator='\r\n'); w.writeheader(); w.writerows(rows)
    OUT_MD.write_text(render(rows, ab, ne, cd, signs), encoding='utf-8')
    print(f'wrote {OUT_MD.name} and {OUT_CSV.name}')
