"""
Cohen's Kappa Calculator for Inter-Coder Reliability
======================================================
Computes Cohen's kappa between two coders on the same decision sample,
with 95% confidence interval via bootstrap and per-category agreement.

Usage:
    python validation/kappa_calculator.py \\
        --coder1 validation/coder1_labels.csv \\
        --coder2 validation/coder2_labels.csv \\
        [--output validation/kappa_results.json]

Input CSV format (both files must have same columns):
    case_id,label
    NL_001,not_water_related
    BR_001,tariff_dispute
    ...

Output:
    Prints kappa, CI, confusion matrix, and per-category agreement.
    Saves JSON to --output path.
"""
import argparse, json, sys, random
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

try:
    import pandas as pd
    import numpy as np
except ImportError:
    sys.exit('pip install pandas numpy')

VALID_CATEGORIES = {
    'tariff_dispute', 'connection_refusal', 'water_quality', 'informal_settlement',
    'groundwater', 'sanitation_sewage', 'flooding', 'riparian_waterway',
    'environmental_protection', 'spatial_planning_water', 'waterboard_governance',
    'pipe_leak_damage', 'water_theft_fraud', 'regulatory_permit', 'hydroelectric_dam',
    'irrigation_agricultural', 'fisheries_water', 'water_infrastructure_contract',
    'flood_protection', 'not_water_related', 'other_water', 'unclear',
    # short codes (see second_coder_protocol.md)
    'TAR', 'CON', 'QUA', 'INF', 'GRD', 'SAN', 'FLD', 'RIP', 'ENV', 'PLN',
    'WBD', 'PIP', 'THF', 'REG', 'HYD', 'IRR', 'FSH', 'FP', 'OTH', 'UNK',
}

SHORT_TO_FULL = {
    'TAR': 'tariff_dispute', 'CON': 'connection_refusal', 'QUA': 'water_quality',
    'INF': 'informal_settlement', 'GRD': 'groundwater', 'SAN': 'sanitation_sewage',
    'FLD': 'flooding', 'RIP': 'riparian_waterway', 'ENV': 'environmental_protection',
    'PLN': 'spatial_planning_water', 'WBD': 'waterboard_governance',
    'PIP': 'pipe_leak_damage', 'THF': 'water_theft_fraud', 'REG': 'regulatory_permit',
    'HYD': 'hydroelectric_dam', 'IRR': 'irrigation_agricultural',
    'FSH': 'fisheries_water', 'FP': 'not_water_related', 'OTH': 'other_water',
    'UNK': 'unclear',
}


def normalize_label(label: str) -> str:
    label = str(label).strip()
    return SHORT_TO_FULL.get(label, label)


def cohen_kappa(y1: list, y2: list) -> float:
    """Compute Cohen's kappa for two lists of labels."""
    n = len(y1)
    assert n == len(y2), "Label lists must have the same length"
    categories = sorted(set(y1) | set(y2))
    # Observed agreement
    p_o = sum(a == b for a, b in zip(y1, y2)) / n
    # Expected agreement
    c1 = Counter(y1)
    c2 = Counter(y2)
    p_e = sum((c1[cat] / n) * (c2[cat] / n) for cat in categories)
    if p_e == 1.0:
        return 1.0
    return (p_o - p_e) / (1 - p_e)


def bootstrap_kappa_ci(y1: list, y2: list, n_boot: int = 1000,
                        alpha: float = 0.05, seed: int = 42) -> tuple:
    """Bootstrap 95% CI for kappa."""
    rng = random.Random(seed)
    n = len(y1)
    pairs = list(zip(y1, y2))
    kappas = []
    for _ in range(n_boot):
        sample = rng.choices(pairs, k=n)
        s1, s2 = zip(*sample)
        kappas.append(cohen_kappa(list(s1), list(s2)))
    kappas.sort()
    lo = kappas[int(alpha / 2 * n_boot)]
    hi = kappas[int((1 - alpha / 2) * n_boot)]
    return lo, hi


def per_category_agreement(y1: list, y2: list) -> dict:
    """Per-category precision, recall, and agreement rate."""
    categories = sorted(set(y1) | set(y2))
    results = {}
    for cat in categories:
        tp = sum(a == cat and b == cat for a, b in zip(y1, y2))
        fp = sum(a != cat and b == cat for a, b in zip(y1, y2))
        fn = sum(a == cat and b != cat for a, b in zip(y1, y2))
        n_cat = sum(a == cat or b == cat for a, b in zip(y1, y2))
        results[cat] = {
            'tp': tp, 'fp': fp, 'fn': fn,
            'precision': tp / (tp + fp) if (tp + fp) else None,
            'recall': tp / (tp + fn) if (tp + fn) else None,
            'n_in_either': n_cat,
        }
    return results


def main():
    parser = argparse.ArgumentParser(description='Compute Cohen\'s kappa between two coders.')
    parser.add_argument('--coder1', required=True, help='CSV with case_id,label for coder 1')
    parser.add_argument('--coder2', required=True, help='CSV with case_id,label for coder 2')
    parser.add_argument('--output', default='validation/kappa_results.json',
                        help='Output JSON path')
    args = parser.parse_args()

    c1 = pd.read_csv(args.coder1).rename(columns={'label': 'label1'})
    c2 = pd.read_csv(args.coder2).rename(columns={'label': 'label2'})

    merged = c1.merge(c2, on='case_id')
    if len(merged) == 0:
        sys.exit('No matching case_ids between the two files.')
    if len(merged) < len(c1) or len(merged) < len(c2):
        print(f'Warning: {abs(len(c1)-len(merged))} case_ids unmatched. Using {len(merged)} matched cases.')

    y1 = [normalize_label(v) for v in merged['label1']]
    y2 = [normalize_label(v) for v in merged['label2']]

    kappa = cohen_kappa(y1, y2)
    lo, hi = bootstrap_kappa_ci(y1, y2)
    per_cat = per_category_agreement(y1, y2)
    p_o = sum(a == b for a, b in zip(y1, y2)) / len(y1)

    print('=' * 60)
    print('INTER-CODER RELIABILITY RESULTS')
    print('=' * 60)
    print(f'\nN cases coded by both:    {len(merged):,}')
    print(f'Observed agreement (p_o): {p_o:.3f} ({p_o*100:.1f}%)')
    print(f"Cohen's kappa (κ):        {kappa:.4f}")
    print(f'95% CI (bootstrap):       [{lo:.4f}, {hi:.4f}]')

    if kappa >= 0.80:
        interp = 'Near-perfect — strong for peer review'
    elif kappa >= 0.75:
        interp = 'Substantial — acceptable for JELS/L&SR/Jurimetrics'
    elif kappa >= 0.60:
        interp = 'Moderate — discuss in methods section; consider category revision'
    else:
        interp = 'Fair/poor — revise coding guide and categories before submission'
    print(f'Interpretation:           {interp}')

    print(f'\nPer-category agreement (categories with n ≥ 5 in either coder):')
    print(f'  {"Category":<30} {"TP":>4} {"FP":>4} {"FN":>4} {"Prec":>6} {"Rec":>6}')
    for cat, v in sorted(per_cat.items(), key=lambda x: -x[1]['n_in_either']):
        if v['n_in_either'] < 5:
            continue
        prec = f"{v['precision']:.2f}" if v['precision'] is not None else ' N/A'
        rec  = f"{v['recall']:.2f}"    if v['recall']    is not None else ' N/A'
        print(f'  {cat:<30} {v["tp"]:>4} {v["fp"]:>4} {v["fn"]:>4} {prec:>6} {rec:>6}')

    # Disagreements on key thesis categories
    print('\nDisagreements on thesis-critical categories:')
    for cat in ['connection_refusal', 'informal_settlement']:
        disagree = [(a, b) for a, b in zip(y1, y2) if (a == cat) != (b == cat)]
        print(f'  {cat}: {len(disagree)} disagreements')

    results = {
        'n_cases': len(merged),
        'observed_agreement': round(p_o, 4),
        'cohen_kappa': round(kappa, 4),
        'ci_95': [round(lo, 4), round(hi, 4)],
        'interpretation': interp,
        'per_category': {
            cat: {k: round(v, 4) if isinstance(v, float) else v
                  for k, v in vals.items()}
            for cat, vals in per_cat.items()
        }
    }

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    print(f'\nResults saved to: {out}')


if __name__ == '__main__':
    main()
