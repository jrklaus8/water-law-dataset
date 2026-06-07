"""
post_marco_legal_analysis.py
============================
Closes the "What's Left" step of Priority 6 in FUTURE_WORK.md: now that
`utils/jurimetric_coding.py` populates a `post_marco_legal` column (1 = decided
on/after 15 Jul 2020, the date Lei 14.026/2020 — the Marco Legal do Saneamento
Básico — was sanctioned; 0 = before; None = non-Brazilian or unparseable date),
this script runs the cross-tabulation the flag exists to enable.

Lei 14.026/2020 restructured the eligibility landscape: pre-reform decisions
sit under the old CESB-obligation framework, post-reform decisions sit under
the new ANA rulemaking authority and the privatization framework. If
post-reform `connection_refusal` / `informal_settlement` rates are flat or
higher than pre-reform rates, that is direct empirical evidence for the
gatekeeper thesis — the reform was explicitly meant to drive *universalização*.

Usage:
  export DATA_DIR=./data
  python utils/post_marco_legal_analysis.py

Requires `water_law_global_coded.csv` with `post_marco_legal` and
`governance_cat` columns populated (i.e. jurimetric_coding.py has been re-run
since the post_marco_legal flag was added).
"""
import os, sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

try:
    import pandas as pd
except ImportError:
    raise SystemExit('pip install pandas')

DL  = Path(os.getenv('DATA_DIR', '.'))
CSV = DL / 'water_law_global_coded.csv'

# Categories most directly relevant to the gatekeeper / universalização thesis
FOCUS_CATS = ['connection_refusal', 'informal_settlement', 'tariff_dispute',
              'sanitation_sewage', 'water_infrastructure_contract']


def load_brazil_rows():
    if not CSV.exists():
        raise SystemExit(f'Not found: {CSV}\n'
                         f'Set DATA_DIR, or run merge_national.py + jurimetric_coding.py first.')
    df = pd.read_csv(CSV, low_memory=False, encoding='utf-8-sig')
    if 'post_marco_legal' not in df.columns:
        raise SystemExit(
            "Column 'post_marco_legal' not found — re-run utils/jurimetric_coding.py "
            "(it now populates this column; see Priority 6 in FUTURE_WORK.md)."
        )
    if 'governance_cat' not in df.columns:
        raise SystemExit("Column 'governance_cat' not found — run jurimetric_coding.py first.")

    country_col = 'country' if 'country' in df.columns else 'pais'
    br = df[df[country_col].astype(str).isin(['Brazil', 'BR'])].copy()
    br = br.dropna(subset=['post_marco_legal'])
    br['post_marco_legal'] = br['post_marco_legal'].astype(int)
    return br


def cross_tab(br):
    """governance_cat distribution, split pre/post Marco Legal, as proportions."""
    xt = (
        br.groupby('post_marco_legal')['governance_cat']
          .value_counts(normalize=True)
          .unstack(fill_value=0)
    )
    xt.index = xt.index.map({0: 'pre_marco_legal (< 2020-07-15)',
                             1: 'post_marco_legal (>= 2020-07-15)'})
    return xt


def category_shift(xt):
    """Percentage-point shift for each focus category, post minus pre."""
    rows = []
    for cat in FOCUS_CATS:
        if cat not in xt.columns:
            continue
        pre  = xt.loc['pre_marco_legal (< 2020-07-15)', cat]
        post = xt.loc['post_marco_legal (>= 2020-07-15)', cat]
        rows.append((cat, pre, post, post - pre))
    return pd.DataFrame(rows, columns=['governance_cat', 'pre_share', 'post_share', 'pp_shift'])


def win_loss_shift(br):
    """If win_loss is coded, compare user_wins rate pre/post for connection_refusal
    and informal_settlement — the categories Priority 6 flags as 'critical rows'."""
    if 'win_loss' not in br.columns:
        return None
    sub = br[br['governance_cat'].isin(['connection_refusal', 'informal_settlement'])]
    sub = sub[sub['win_loss'].isin(['user_wins', 'utility_wins', 'mixed'])]
    if sub.empty:
        return None
    rate = (
        sub.groupby(['governance_cat', 'post_marco_legal'])['win_loss']
           .apply(lambda s: (s == 'user_wins').mean())
           .unstack(fill_value=float('nan'))
    )
    rate.columns = ['pre_marco_legal_user_win_rate', 'post_marco_legal_user_win_rate'][:len(rate.columns)]
    return rate


def main():
    print('Loading dataset...')
    br = load_brazil_rows()
    n_pre  = int((br['post_marco_legal'] == 0).sum())
    n_post = int((br['post_marco_legal'] == 1).sum())
    print(f'  {len(br):,} Brazilian rows with a parseable decision date')
    print(f'  pre-Marco Legal  (< 2020-07-15): {n_pre:,}')
    print(f'  post-Marco Legal (>= 2020-07-15): {n_post:,}')

    if n_pre == 0 or n_post == 0:
        print('\nOnly one side of the Marco Legal split is populated — '
              'cross-tabulation needs both pre- and post-reform decisions. '
              'No further analysis possible with the current data.')
        return

    print('\n' + '=' * 78)
    print('Governance-category distribution: pre vs. post Marco Legal do Saneamento')
    print('=' * 78)
    xt = cross_tab(br)
    with pd.option_context('display.float_format', '{:.3f}'.format,
                           'display.width', 160, 'display.max_columns', None):
        print(xt[[c for c in FOCUS_CATS if c in xt.columns]])

    print('\n' + '=' * 78)
    print('Percentage-point shift (post minus pre) — focus categories')
    print('=' * 78)
    shift = category_shift(xt)
    for _, row in shift.iterrows():
        direction = 'UP' if row['pp_shift'] > 0 else ('DOWN' if row['pp_shift'] < 0 else 'flat')
        print(f"  {row['governance_cat']:28s} "
              f"{row['pre_share']*100:5.1f}% -> {row['post_share']*100:5.1f}%  "
              f"({row['pp_shift']*100:+.1f} pp, {direction})")
    print('\n  Reading guide: a flat-or-rising connection_refusal / informal_settlement')
    print('  share after 2020-07-15 supports the gatekeeper thesis (the reform did not')
    print('  reduce the litigated-access gap); a sharp drop would cut against it.')

    wl = win_loss_shift(br)
    if wl is not None:
        print('\n' + '=' * 78)
        print('User win-rate, pre vs. post Marco Legal — critical rows per FUTURE_WORK.md')
        print('=' * 78)
        with pd.option_context('display.float_format', '{:.3f}'.format):
            print(wl)
    else:
        print('\n(win_loss column not present/codeable — skipping win-rate comparison)')


if __name__ == '__main__':
    main()
