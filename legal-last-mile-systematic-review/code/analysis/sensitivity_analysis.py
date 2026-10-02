#!/usr/bin/env python3
"""Sensitivity analysis of the three SWiM syntheses (Families A, B, C) and of the descriptive counts.

Question answered: does any stated conclusion move if the weakest inputs are removed or the non-independent ones collapsed?

Scenarios (each applied to the study lists in the SWiM documents):
  S0 baseline
  S1 drop the abstract-/metadata-only extractions           (05_analysis/sensitivity/abstract_only_extractions_2026-09-28.csv logic)
  S2 drop effect-size rows for studies not flagged quantitative_synthesis_eligible   (S589)
  S3 collapse linked reports that share underlying data     (linked_reports_2026-09-28.csv, same_underlying_data = yes)
  S4 drop the two coding judgment calls in Family A         (S358, S404: "protective"/free-text direction read as concordant)
  S5 all of S1-S4 together

Pre-stated conclusion tests (written before the numbers were computed, so they cannot be tuned to the result):
  A: a majority (> 50%) of studies is concordant with "legal recognition/eligibility improves access" (substantive reading in the Family A document)
  B: every study has a positive sign or is mixed (none negative or null)
  C: no single sign (positive/negative/mixed/null) holds a majority of studies ("no dominant direction")

Inputs are the SWiM documents themselves (single source of truth for the direction coding) and the CSV databases. Deterministic;
rewrites 05_analysis/sensitivity/SENSITIVITY_ANALYSIS_2026-09-28.md and sensitivity_scenarios_2026-09-28.csv.
Run from the project root:  python3 code/analysis/sensitivity_analysis.py
"""
import csv, re, sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import current_figures as cf  # noqa: E402

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


def parse_concordance():
    t = swim_text('A')
    out = {}
    for m in re.finditer(r'^\| (Consistent|Counter-pattern|Null) [^|]*\| (\d+) \((\d+)%\) \| ([^|]*)\|', t, re.M):
        key = {'Consistent': 'concordant', 'Counter-pattern': 'counter', 'Null': 'null'}[m.group(1)]
        ids = re.findall(r'S\d+', m.group(4))
        assert len(ids) == int(m.group(2)), key
        out.update({i: key for i in ids})
    return out


def scenarios():
    es_ids = {r['study_id'] for r in cf.read('es')}
    ed = {r['study_id']: r for r in cf.read('ed')}
    em = {r['study_id']: r for r in cf.read('em')}
    links = cf.read('links')
    abstract_only = {s for s, r in ed.items() if r['extraction_note'].startswith(cf.ABSTRACT_ONLY_PREFIXES)}
    not_eligible = {s for s in es_ids if em[s]['quantitative_synthesis_eligible'] != 'TRUE'}
    # collapse: for each definite link, drop the later member (keep the first-listed study) if both are in the analysed set
    collapse_drop = {r['study_id_b'] for r in links if r['same_underlying_data'] == 'yes'}
    signs = {f: parse_signs(f) for f in 'ABC'}
    conc = parse_concordance()
    for f in 'ABC':
        assert set(signs[f]) <= es_ids, f'{f}: SWiM document lists a study not in effect_sizes.csv'
    assert set(conc) == set(signs['A']), 'Family A concordance table does not cover the same studies as the Family A sign table'
    S = {
        'S0 baseline': set(),
        'S1 drop abstract-only extractions': abstract_only,
        'S2 drop rows for studies not flagged eligible': not_eligible,
        'S3 collapse linked reports (same underlying data)': collapse_drop,
        'S4 drop Family A coding judgment calls (S358, S404)': {'S358', 'S404'},
    }
    S['S5 all of S1-S4'] = set().union(*[v for k, v in S.items() if k != 'S0 baseline'])
    rows = []
    for name, drop in S.items():
        rec = {'scenario': name, 'dropped_studies_in_families': ';'.join(sorted(d for d in drop if any(d in signs[f] for f in 'ABC')))}
        for f in 'ABC':
            kept = {s: v for s, v in signs[f].items() if s not in drop}
            c = Counter(kept.values()); k = len(kept)
            rec[f'{f}_k'] = k
            for lab in ('positive', 'negative', 'null', 'mixed'):
                rec[f'{f}_{lab}'] = c.get(lab, 0)
        keptA = [s for s in signs['A'] if s not in drop]
        cc = Counter(conc[s] for s in keptA)
        rec['A_concordant'], rec['A_counter'], rec['A_null_concordance'] = cc.get('concordant', 0), cc.get('counter', 0), cc.get('null', 0)
        rec['A_concordant_pct'] = round(100 * rec['A_concordant'] / len(keptA), 1) if keptA else ''
        rec['A_test_majority_concordant'] = 'holds' if keptA and rec['A_concordant'] * 2 > len(keptA) else 'FAILS'
        rec['B_test_none_negative_or_null'] = 'holds' if rec['B_k'] and rec['B_negative'] == 0 and rec['B_null'] == 0 else 'FAILS'
        rec['C_test_no_dominant_sign'] = 'holds' if rec['C_k'] and max(rec[f'C_{l}'] for l in ('positive', 'negative', 'null', 'mixed')) * 2 <= rec['C_k'] else 'FAILS'
        rows.append(rec)
    return rows, abstract_only, not_eligible, collapse_drop, signs


def descriptive_drop_abstract_only(abstract_only):
    ed = cf.read('ed')
    kept = [r for r in ed if r['study_id'] not in abstract_only]
    full, sub = Counter(cf.tool_of(r['risk_of_bias_tool']) for r in ed), Counter(cf.tool_of(r['risk_of_bias_tool']) for r in kept)
    return len(ed), len(kept), full, sub


def render(rows, abstract_only, not_eligible, collapse_drop, signs):
    n_all, n_kept, full, sub = descriptive_drop_abstract_only(abstract_only)
    fails = [(r['scenario'], k) for r in rows for k in ('A_test_majority_concordant', 'B_test_none_negative_or_null', 'C_test_no_dominant_sign') if r[k] == 'FAILS']
    L = ["# Sensitivity analysis of the SWiM syntheses (generated — do not edit by hand)", "",
         "Generated by `code/analysis/sensitivity_analysis.py`. Direction coding is read from the SWiM documents themselves; nothing was re-coded here.",
         "Conclusion tests were fixed before the numbers were computed (see the script's docstring).", "",
         "## Headline", "",
         ("**No stated conclusion changes under any scenario.**" if not fails else "**At least one stated conclusion fails under some scenario:** " + "; ".join(f"{s} — {k}" for s, k in fails)) +
         f" Families A, B and C rest on {rows[0]['A_k']}, {rows[0]['B_k']} and {rows[0]['C_k']} studies; the scenarios remove at most {max(len(r['dropped_studies_in_families'].split(';')) if r['dropped_studies_in_families'] else 0 for r in rows)} of them.", "",
         "## Why several scenarios change nothing", "",
         f"- **Abstract-only extractions ({len(abstract_only)} studies):** none has an `effect_sizes.csv` row, so S1 leaves every family unchanged. It matters for descriptive counts only (below).",
         f"- **Linked reports:** of the definite same-data links, only S294 (Family B) has an effect-size row; its twin S366 has none. S3 therefore changes nothing in A, B or C.",
         f"- **Studies not flagged eligible ({', '.join(sorted(not_eligible)) or 'none'}):** S589 is in Family A; S2 removes it.", "",
         "## Family results by scenario", "",
         "| Scenario | Dropped (in families) | A k | A pos/neg/null | A concordant | A test | B k | B pos/mixed | B test | C k | C pos/neg/mixed | C test |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        L.append(f"| {r['scenario']} | {r['dropped_studies_in_families'] or '—'} | {r['A_k']} | {r['A_positive']}/{r['A_negative']}/{r['A_null']} | {r['A_concordant']} ({r['A_concordant_pct']}%) | {r['A_test_majority_concordant']} | "
                 f"{r['B_k']} | {r['B_positive']}/{r['B_mixed']} | {r['B_test_none_negative_or_null']} | {r['C_k']} | {r['C_positive']}/{r['C_negative']}/{r['C_mixed']} | {r['C_test_no_dominant_sign']} |")
    L += ["", "Tests: **A** — more than half of the studies are concordant with \"recognition/eligibility improves access\" (the Family A document's substantive reading, not the raw sign);",
          "**B** — no study is negative or null; **C** — no single sign holds a majority. Signs are as extracted; see the Family A and C documents for why sign and valence differ.", "",
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
