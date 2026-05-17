"""
Residual Classification Audit
==============================
Reproduces the audit in validation/RESIDUAL_AUDIT.md.
Run from the repo root: python validation/residual_audit.py

Requires: pandas
Input:    data/water_law_global_coded.csv  (or set CODED_CSV env var)
Output:   prints to stdout; saves validation/residual_audit_results.json
"""
import re, os, json, sys
from pathlib import Path
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

try:
    import pandas as pd
except ImportError:
    sys.exit('pip install pandas')

# ── Locate the coded CSV ───────────────────────────────────────────────────────
DEFAULT_CSV = Path(__file__).parent.parent / 'data' / 'water_law_global_coded.csv'
CSV_PATH = Path(os.getenv('CODED_CSV', DEFAULT_CSV))

if not CSV_PATH.exists():
    sys.exit(
        f'Coded CSV not found at {CSV_PATH}.\n'
        'Either run utils/jurimetric_coding.py first, or set the CODED_CSV '
        'environment variable to the correct path.'
    )

print(f'Loading: {CSV_PATH}')
df = pd.read_csv(CSV_PATH, low_memory=False, encoding='utf-8-sig')
country_col = 'country' if 'country' in df.columns else 'pais'
print(f'  {len(df):,} cases loaded\n')

# ── Water core vocabulary ─────────────────────────────────────────────────────
WATER_CORE = re.compile(
    r'\bwater(?:schap|leiding|kering|winning|onttrekking|toets|berging|peil'
    r'|beheer|overlast|staat|taak|schade|gang|werk|staat)?\b'
    r'|\bdrinkwater\b|\bgrondwater\b|\briolering\b|\bwateroverlast\b|\bwaterschade\b'
    r'|\bdijk\b|\bkade\b|\bwaterkering\b|\bpeilbesluit\b|\bwatergang\b'
    r'|\b[aáàâã]gua\b|\bfornecimento\b|\bsaneamento\b'
    r'|\bcaesb\b|\bsabesp\b|\bcasan\b|\bcaesb\b|\bcaema\b|\bcagece\b'
    r'|\beau\b|\baquifer\b|\birrigat\b|\bwetland\b|\bdrinkbaar\b',
    re.I
)

# ── Thematic patterns for Brazil genuine residual ──────────────────────────────
BRAZIL_THEMES = {
    'tariff_missed':      re.compile(
        r'débit[oa].*?[aáàâã]gua|[aáàâã]gua.*?débit[oa]'
        r'|inexistência.*?débit[oa].*?[aáàâã]gua'
        r'|declaratória.*?[aáàâã]gua'
        r'|excesso.*?cobranç[ao].*?[aáàâã]gua'
        r'|fatura.*?[aáàâã]gua.*?cobranç[ao]'
        r'|cobrança.*?água.*?indevid',
        re.I
    ),
    'connection_missed':  re.compile(
        r'obriga[çc][aã]o de fazer.*?[aáàâã]gua|[aáàâã]gua.*?obriga[çc][aã]o de fazer'
        r'|abastecimento.*?[aáàâã]gua.*?ausênci'
        r'|extensão.*?rede.*?[aáàâã]gua|rede.*?extensão.*?[aáàâã]gua'
        r'|implantação.*?rede.*?[aáàâã]gua',
        re.I
    ),
    'informal_missed':    re.compile(
        r'irregular.*?[aáàâã]gua|favela|invasão.*?[aáàâã]gua'
        r'|assentamento.*?[aáàâã]gua|loteamento.*?irregular',
        re.I
    ),
    'pipe_missed':        re.compile(
        r'dano.*?[aáàâã]gua.*?vazamento|vazamento.*?[aáàâã]gua'
        r'|ruptura.*?[aáàâã]gua|rompimento.*?[aáàâã]gua'
        r'|infiltração.*?[aáàâã]gua',
        re.I
    ),
    'precatorio_caesb':   re.compile(r'precatório.*caesb|caesb.*precatório|adpf.*caesb', re.I),
    'concurso_caesb':     re.compile(r'concurso.*caesb|caesb.*concurso', re.I),
    'family_law':         re.compile(r'guarda|alimento|divórcio|família.*[aáàâã]gua', re.I),
    'criminal':           re.compile(r'tráfico|latrocínio|crime.*[aáàâã]gua', re.I),
    'processual_only':    re.compile(r'processual.*embargos|embargos de declaração', re.I),
}

# ── Run audit ─────────────────────────────────────────────────────────────────
other = df[df['governance_cat'] == 'other_water'].copy()
text_cols = [c for c in ['title', 'summary', 'ementa', 'snippet'] if c in df.columns]
other['_txt'] = other[text_cols].fillna('').apply(
    lambda r: ' '.join(str(v) for v in r), axis=1
)
other['has_water_vocab'] = other['_txt'].apply(lambda t: bool(WATER_CORE.search(t)))

results = {
    'total_corpus': len(df),
    'total_other_water': len(other),
    'other_water_pct': round(len(other) / len(df) * 100, 1),
    'by_country': {}
}

print('=' * 60)
print(f'RESIDUAL AUDIT — other_water category')
print('=' * 60)
print(f'\nTotal corpus:       {len(df):>7,}')
print(f'Total other_water:  {len(other):>7,} ({results["other_water_pct"]}%)')

for country in [c for c in ['Netherlands', 'Brazil', 'Canada'] if c in df[country_col].unique()]:
    sub = other[other[country_col] == country]
    no_water = sub[~sub['has_water_vocab']]
    yes_water = sub[sub['has_water_vocab']]

    country_result = {
        'residual_total': len(sub),
        'false_positive_no_vocab': len(no_water),
        'false_positive_pct': round(len(no_water) / max(len(sub), 1) * 100, 1),
        'genuine_unclassified': len(yes_water),
        'genuine_pct': round(len(yes_water) / max(len(sub), 1) * 100, 1),
    }

    print(f'\n{country}: {len(sub):,} residual')
    print(f'  False positives (no water vocab): {len(no_water):,} ({country_result["false_positive_pct"]}%)')
    print(f'  Genuine unclassified:             {len(yes_water):,} ({country_result["genuine_pct"]}%)')

    if country == 'Brazil' and len(yes_water) > 0:
        print(f'\n  Thematic breakdown of Brazil genuine residual:')
        theme_counts = {}
        for theme, pat in BRAZIL_THEMES.items():
            n = yes_water['_txt'].apply(lambda t: bool(pat.search(t))).sum()
            theme_counts[theme] = int(n)
            print(f'    {theme:<25} {n:>4} ({n/len(yes_water)*100:.1f}%)')
        country_result['brazil_themes'] = theme_counts

        # Thesis robustness check
        connection_current = len(df[(df[country_col] == 'Brazil') &
                                    (df['governance_cat'] == 'connection_refusal')])
        informal_current = len(df[(df[country_col] == 'Brazil') &
                                  (df['governance_cat'] == 'informal_settlement')])
        brazil_total = len(df[df[country_col] == 'Brazil'])

        missed_conn = theme_counts.get('connection_missed', 0)
        missed_inf  = theme_counts.get('informal_missed', 0)

        print(f'\n  --- Thesis robustness check ---')
        print(f'  connection_refusal (classified):  {connection_current:,} ({connection_current/brazil_total*100:.1f}%)')
        print(f'  + missed in residual:            +{missed_conn}')
        print(f'  = revised:                        {connection_current + missed_conn:,} ({(connection_current+missed_conn)/brazil_total*100:.1f}%)')
        print(f'')
        print(f'  informal_settlement (classified): {informal_current:,} ({informal_current/brazil_total*100:.2f}%)')
        print(f'  + missed in residual:            +{missed_inf}')
        print(f'  = revised:                        {informal_current + missed_inf:,} ({(informal_current+missed_inf)/brazil_total*100:.2f}%)')

        country_result['thesis_robustness'] = {
            'connection_refusal_current': connection_current,
            'connection_refusal_missed': missed_conn,
            'connection_refusal_revised': connection_current + missed_conn,
            'informal_settlement_current': informal_current,
            'informal_settlement_missed': missed_inf,
            'informal_settlement_revised': informal_current + missed_inf,
        }

    results['by_country'][country] = country_result

# ── Save results ───────────────────────────────────────────────────────────────
out_path = Path(__file__).parent / 'residual_audit_results.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f'\n\nResults saved to: {out_path}')
print('\nConclusion: See validation/RESIDUAL_AUDIT.md for full interpretation.')
