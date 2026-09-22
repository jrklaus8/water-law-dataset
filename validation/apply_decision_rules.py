#!/usr/bin/env python3
"""
apply_decision_rules.py — reproducible inter-coder reliability under stated rules
================================================================================
`kappa_calculator.py` computes raw agreement between two coders' labels. Raw
agreement penalises a disagreement that is really a *protocol* ambiguity rather
than a coding error: where the protocol did not say how to treat a case type,
one coder hedged UNCERTAIN and the other committed. Resolving the ambiguity with
a written rule and re-scoring is legitimate, but only if the rule is written
down and the re-scoring is runnable. This script does both.

The problem it fixes
--------------------
`validation/README.md` reports a headline of kappa = 0.832 "with the documented
*mananciais* rule applied". No committed artefact produced that number:
`kappa_results.json`, described in the same file as the "Official kappa output",
holds the pre-rule baseline of 0.5684, and the rule itself existed only as prose.
A reviewer checking the headline against the repository found a contradiction.

This script makes every reported figure reproducible from committed data, and
reports the rule's sensitivity instead of a single unexplained number.

The rule
--------
RULE-BR-MANANCIAIS. In Brazilian law, *área de proteção aos mananciais* is the
statutory protection zone around a public water source (São Paulo state Leis
898/1975 and 1.172/1976; federally, APAs under Lei 9.985/2000). Litigation over
irregular construction or subdivision inside such a zone is a dispute about
protecting a drinking water source, and is therefore a water case.

The original protocol (`second_coder_protocol.md`) did not say so. Coder 1
hedged these UNCERTAIN; coder 2 coded them WATER. That single omission accounts
for 18 of the 26 disagreements in the 91-case kappa set.

Applying the rule means: where a decision matches the *mananciais* vocabulary,
coder 1's hedge is resolved to WATER. Coder 2's labels are never altered.

Scope variants
--------------
The rule's reach is a judgement call, so this script scores all of them and
prints the spread rather than picking one silently:

  narrow     only explicit manancial / mananciais / watershed vocabulary
  standard   the above, plus "área de proteção ambiental" (APA)
  broad      the above, applied to NOT_WATER hedges as well as UNCERTAIN

Report the variant you adopt, by name, alongside the kappa it produces.

Usage
-----
    python validation/apply_decision_rules.py
    python validation/apply_decision_rules.py --variant standard \
        --output validation/kappa_results_ruled.json
"""
import argparse
import csv
import json
import random
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

HERE = Path(__file__).resolve().parent

# ── RULE-BR-MANANCIAIS vocabulary ─────────────────────────────────────────────
MANANCIAIS_NARROW = re.compile(
    r'manancia(?:l|is)|manacial|watershed', re.I)
MANANCIAIS_STANDARD = re.compile(
    r'manancia(?:l|is)|manacial|watershed'
    r'|[aá]rea de prote[çc][aã]o ambiental|prote[çc][aã]o ambiental'
    r'|\bapa\b', re.I)

VARIANTS = {
    'narrow':   {'pattern': MANANCIAIS_NARROW,   'targets': ('UNCERTAIN',)},
    'standard': {'pattern': MANANCIAIS_STANDARD, 'targets': ('UNCERTAIN',)},
    'broad':    {'pattern': MANANCIAIS_STANDARD, 'targets': ('UNCERTAIN', 'NOT_WATER')},
}


def read_csv(path):
    with open(path, newline='', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))


def cohen_kappa(y1, y2):
    labels = sorted(set(y1) | set(y2))
    n = len(y1)
    if n == 0:
        return float('nan'), float('nan')
    po = sum(a == b for a, b in zip(y1, y2)) / n
    pe = sum((y1.count(l) / n) * (y2.count(l) / n) for l in labels)
    return ((po - pe) / (1 - pe) if pe != 1 else float('nan')), po


def bootstrap_ci(y1, y2, n_boot=2000, seed=42):
    rnd = random.Random(seed)
    n = len(y1)
    ks = []
    for _ in range(n_boot):
        idx = [rnd.randrange(n) for _ in range(n)]
        k, _ = cohen_kappa([y1[i] for i in idx], [y2[i] for i in idx])
        if k == k:  # not NaN
            ks.append(k)
    if not ks:
        return [float('nan')] * 2
    ks.sort()
    return [round(ks[int(0.025 * len(ks))], 4), round(ks[int(0.975 * len(ks)) - 1], 4)]


def interpret(k):
    if k != k:
        return 'undefined'
    for lim, txt in ((0.81, 'almost perfect'), (0.61, 'substantial'),
                     (0.41, 'moderate'), (0.21, 'fair')):
        if k >= lim:
            return txt
    return 'slight'


def apply_rule(rows, variant):
    """Return (relabelled coder1 labels, list of cases the rule touched)."""
    spec = VARIANTS[variant]
    out, touched = [], []
    for r in rows:
        lab = r['coder1_label']
        text = r.get('_text', '') or ''
        if lab in spec['targets'] and spec['pattern'].search(text):
            out.append('WATER')
            touched.append({'case_id': r['case_id'], 'country': r.get('country', ''),
                            'from': lab, 'to': 'WATER'})
        else:
            out.append(lab)
    return out, touched


def load_joined():
    detail = read_csv(HERE / 'kappa_agreement_detail.csv')
    raw = {r['sample_id']: r for r in read_csv(HERE / 'second_coder_sample_raw.csv')}
    for r in detail:
        src = raw.get(r['sample_id'], {})
        r['_text'] = f"{src.get('title','')} {src.get('summary','')}"
    return detail


def score(y1, y2, label, n_boot):
    k, po = cohen_kappa(y1, y2)
    return {'label': label, 'n': len(y1), 'cohen_kappa': round(k, 4),
            'observed_agreement': round(po, 4),
            'agreement_fraction': f'{sum(a==b for a,b in zip(y1,y2))}/{len(y1)}',
            'ci_95': bootstrap_ci(y1, y2, n_boot),
            'interpretation': interpret(k)}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--variant', choices=sorted(VARIANTS), default='standard')
    ap.add_argument('--boot', type=int, default=2000)
    ap.add_argument('--output', default=str(HERE / 'kappa_results_ruled.json'))
    a = ap.parse_args()

    rows = load_joined()
    y2 = [r['coder2_label'] for r in rows]
    y1_base = [r['coder1_label'] for r in rows]

    results = {'baseline_three_label': score(y1_base, y2, 'baseline (no rule)', a.boot)}

    # Every variant, so the sensitivity is on the record.
    sensitivity = []
    for name in ('narrow', 'standard', 'broad'):
        y1, touched = apply_rule(rows, name)
        s = score(y1, y2, f'RULE-BR-MANANCIAIS:{name}', a.boot)
        s['cases_relabelled'] = len(touched)
        sensitivity.append(s)
    results['rule_variants'] = sensitivity

    y1_sel, touched = apply_rule(rows, a.variant)
    results['adopted'] = dict(score(y1_sel, y2, f'RULE-BR-MANANCIAIS:{a.variant}', a.boot),
                              variant=a.variant, cases_relabelled=len(touched))
    results['relabelled_cases'] = touched

    # Binary WATER/NOT_WATER, dropping cases either coder left UNCERTAIN.
    pairs = [(x, y) for x, y in zip(y1_base, y2) if 'UNCERTAIN' not in (x, y)]
    if pairs:
        results['binary_exclude_uncertain'] = score([p[0] for p in pairs],
                                                    [p[1] for p in pairs],
                                                    'binary (UNCERTAIN dropped)', a.boot)

    results['rule_definition'] = {
        'id': 'RULE-BR-MANANCIAIS',
        'statement': ('Litigation over irregular construction or subdivision inside a '
                      'statutory water-source protection zone (area de protecao aos '
                      'mananciais; APA) is a water case.'),
        'legal_basis': ('Sao Paulo Leis 898/1975 and 1.172/1976; APAs under Lei '
                        '9.985/2000 art. 15.'),
        'applies_to': 'coder 1 hedges only; coder 2 labels are never altered',
        'variant_patterns': {k: VARIANTS[k]['pattern'].pattern for k in VARIANTS},
        'variant_targets': {k: list(VARIANTS[k]['targets']) for k in VARIANTS},
    }

    Path(a.output).write_text(json.dumps(results, ensure_ascii=False, indent=2),
                              encoding='utf-8')

    # ── Report ────────────────────────────────────────────────────────────────
    b = results['baseline_three_label']
    print('=' * 72)
    print('INTER-CODER RELIABILITY UNDER STATED DECISION RULES')
    print('=' * 72)
    print(f"\nBaseline, three-label, no rule applied   n={b['n']}")
    print(f"  kappa = {b['cohen_kappa']}  CI95 {b['ci_95']}  "
          f"agreement {b['agreement_fraction']} ({b['interpretation']})")

    print('\nRULE-BR-MANANCIAIS, sensitivity across scope variants:')
    print(f"  {'variant':10} {'relabelled':>10} {'kappa':>8} {'CI95':>18} {'agreement':>11}")
    for s in sensitivity:
        v = s['label'].split(':')[1]
        print(f"  {v:10} {s['cases_relabelled']:>10} {s['cohen_kappa']:>8.4f} "
              f"{str(s['ci_95']):>18} {s['agreement_fraction']:>11}")

    if 'binary_exclude_uncertain' in results:
        bi = results['binary_exclude_uncertain']
        print(f"\nBinary WATER/NOT_WATER, UNCERTAIN dropped   n={bi['n']}")
        print(f"  kappa = {bi['cohen_kappa']}  CI95 {bi['ci_95']}  "
              f"agreement {bi['agreement_fraction']} ({bi['interpretation']})")

    ad = results['adopted']
    print(f"\nAdopted variant: {a.variant}  ->  kappa = {ad['cohen_kappa']} "
          f"({ad['cases_relabelled']} cases relabelled)")
    print(f"Written to {a.output}")
    print('\nReport the variant by name whenever you report the kappa. The spread\n'
          'above is the honest uncertainty in the figure.')


if __name__ == '__main__':
    sys.exit(main())
