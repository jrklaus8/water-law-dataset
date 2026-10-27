"""
Kappa sensitivity specifications for the LLM-assisted reproducibility audit
============================================================================
Reproduces the four specifications reported in validation/RESIDUAL_AUDIT.md section 5.2 from the case-by-case file
validation/kappa_agreement_detail.csv, and stores them under `sensitivity_analysis` in validation/kappa_results.json
(and in validation_report_data.json when that file exists). Standard library only.

Specifications (labels are WATER / NOT_WATER / UNCERTAIN):
  mananciais_rule      coder 1's UNCERTAIN becomes WATER for Brazilian decisions (documented decision rule: Sao Paulo
                       'mananciais' watershed-protection cases are water law for Legal Last Mile purposes)
  exclude_uncertain    only decisions where neither coder said UNCERTAIN (binary WATER / NOT_WATER)
  coder1_confident     only decisions where coder 1 gave a non-UNCERTAIN label
  baseline             all 91 decisions, three labels, no rule (pre-calibration)

Confidence intervals: percentile bootstrap, 5,000 resamples, seed 42 (same estimator as kappa_calculator.py, so the
numbers are reproducible; the primary `ci_95` in kappa_results.json uses 2,000 resamples).

Usage (from the repository root):
    python validation/kappa_sensitivity.py
"""
import argparse
import csv
import json
import random
from collections import Counter
from pathlib import Path

N_BOOT = 5000
SEED = 42
BASE = Path(__file__).parent


def cohen_kappa(y1, y2):
    n = len(y1)
    p_o = sum(a == b for a, b in zip(y1, y2)) / n
    c1, c2 = Counter(y1), Counter(y2)
    p_e = sum((c1[c] / n) * (c2[c] / n) for c in set(y1) | set(y2))
    return (1.0 if p_e == 1.0 else (p_o - p_e) / (1 - p_e)), p_o


def bootstrap_ci(y1, y2, n_boot=N_BOOT, seed=SEED, alpha=0.05):
    rng = random.Random(seed)
    pairs = list(zip(y1, y2))
    ks = []
    for _ in range(n_boot):
        s1, s2 = zip(*rng.choices(pairs, k=len(pairs)))
        ks.append(cohen_kappa(list(s1), list(s2))[0])
    ks.sort()
    return ks[int(alpha / 2 * n_boot)], ks[int((1 - alpha / 2) * n_boot)]


def sensitivity_analysis(rows):
    """rows: dicts with country, coder1_label, coder2_label. Returns a list of specification results."""
    y1 = [r['coder1_label'] for r in rows]
    y2 = [r['coder2_label'] for r in rows]
    brazil = [r['country'] == 'Brazil' for r in rows]
    y1_rule = ['WATER' if (b and a == 'UNCERTAIN') else a for a, b in zip(y1, brazil)]
    both = [i for i in range(len(rows)) if y1[i] != 'UNCERTAIN' and y2[i] != 'UNCERTAIN']
    c1conf = [i for i in range(len(rows)) if y1[i] != 'UNCERTAIN']
    specs = [
        ('mananciais_rule', 'Mananciais rule applied (coder 1 UNCERTAIN -> WATER for Brazil)', y1_rule, y2),
        ('exclude_uncertain', 'Exclude UNCERTAIN: neither coder said UNCERTAIN (binary WATER / NOT_WATER)',
         [y1[i] for i in both], [y2[i] for i in both]),
        ('coder1_confident', 'Coder 1 confident: coder 1 gave a non-UNCERTAIN label',
         [y1[i] for i in c1conf], [y2[i] for i in c1conf]),
        ('baseline', 'Three labels, no rule (pre-calibration baseline)', y1, y2),
    ]
    out = []
    for key, label, a, b in specs:
        kappa, p_o = cohen_kappa(a, b)
        lo, hi = bootstrap_ci(a, b)
        out.append({'specification': key, 'description': label, 'n_cases': len(a),
                    'cohen_kappa': round(kappa, 4), 'ci_95': [round(lo, 4), round(hi, 4)],
                    'observed_agreement': round(p_o, 4), 'n_boot': N_BOOT, 'seed': SEED})
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[1])
    ap.add_argument('--detail', default=str(BASE / 'kappa_agreement_detail.csv'))
    ap.add_argument('--results', default=str(BASE / 'kappa_results.json'))
    args = ap.parse_args()
    with open(args.detail, newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    block = sensitivity_analysis(rows)
    targets = [Path(args.results), Path(args.results).with_name('validation_report_data.json')]
    for path in targets:
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding='utf-8'))
        holder = data['kappa'] if path.name == 'validation_report_data.json' else data
        # the baseline row must agree with the kappa already stored (guards against a stale detail file)
        base = next(b for b in block if b['specification'] == 'baseline')
        assert abs(holder['cohen_kappa'] - base['cohen_kappa']) < 1e-4, f'{path.name}: stored kappa differs from the detail file'
        holder['sensitivity_analysis'] = block
        path.write_text(json.dumps(data, indent=2), encoding='utf-8')
        print(f'updated {path.name}')
    for b in block:
        print(f"{b['specification']:<18} n={b['n_cases']:<3} kappa={b['cohen_kappa']:.3f}  95% CI [{b['ci_95'][0]:.3f}, {b['ci_95'][1]:.3f}]  agreement {b['observed_agreement'] * 100:.1f}%")


if __name__ == '__main__':
    main()
