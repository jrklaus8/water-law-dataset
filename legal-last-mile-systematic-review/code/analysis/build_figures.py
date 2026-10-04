#!/usr/bin/env python3
"""Draw the descriptive and synthesis figures for the report and manuscript from the databases (no hand-typed numbers).

Writes light-mode SVGs (text kept as text) to 06_outputs/figures/: fig1_design_mix, fig2_publication_years, fig3_countries, fig4_direction_by_family,
fig5_appraisal_tools. Palette: the dataviz reference palette (blue #2a78d6, orange #eb6834, violet #4a3aa7 validated as a set; neutral grey for null/other).
Every bar carries its count as a direct label, so no figure relies on colour alone. Deterministic (fixed svg hash salt). Run from the project root.
"""
import sys
from collections import Counter
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parent))
import current_figures as cf  # noqa: E402
import sensitivity_analysis as sa  # noqa: E402

OUT = cf.ROOT / '06_outputs/figures'
BLUE, ORANGE, VIOLET, GREY, INK, MUTED, SURF = '#2a78d6', '#eb6834', '#4a3aa7', '#8a8984', '#0b0b0b', '#52514e', '#fcfcfb'
plt.rcParams.update({'svg.fonttype': 'none', 'svg.hashsalt': 'legal-last-mile', 'font.family': 'sans-serif', 'font.size': 10, 'axes.edgecolor': '#c8c7c1',
                     'axes.labelcolor': MUTED, 'xtick.color': MUTED, 'ytick.color': INK, 'figure.facecolor': SURF, 'axes.facecolor': SURF, 'text.color': INK})
META = {'Creator': None, 'Date': None}


def finish(fig, ax, name, title, sub):
    for sp in ('top', 'right'):
        ax.spines[sp].set_visible(False)
    ax.tick_params(length=0)
    h = fig.get_figheight()
    fig.tight_layout(rect=[0, 0, 1, 1 - 0.75 / h])  # leave 0.75 in at the top for the two header lines
    fig.text(0.01, 1 - 0.22 / h, title, ha='left', va='top', fontsize=12, fontweight='bold')
    fig.text(0.01, 1 - 0.50 / h, sub, ha='left', va='top', fontsize=8.5, color=MUTED)
    fig.savefig(OUT / f'{name}.svg', metadata=META)
    plt.close(fig)


def hbar(names, vals, color, name, title, sub, xlabel):
    fig, ax = plt.subplots(figsize=(7.2, 0.38 * len(names) + 1.3))
    y = range(len(names))
    ax.barh(list(y), vals, color=color, height=0.62)
    ax.set_yticks(list(y)); ax.set_yticklabels(names); ax.invert_yaxis()
    ax.grid(axis='x', color='#e6e5e0', linewidth=0.6); ax.set_axisbelow(True)
    for i, v in enumerate(vals):
        ax.text(v + max(vals) * 0.01, i, f'{v:,}', va='center', fontsize=9, color=INK)
    ax.set_xlabel(xlabel); ax.set_xlim(0, max(vals) * 1.12)
    finish(fig, ax, name, title, sub)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    F = cf.compute()
    ed, em = cf.read('ed'), cf.read('em')
    n = len(ed)
    enum = {'experimental', 'quasi_experimental', 'observational', 'qualitative', 'doctrinal', 'jurimetric', 'systematic_review_secondary', 'mixed_methods'}
    dc = Counter(r['study_design_class'] if r['study_design_class'] in enum else 'free-text label (outside the 8-value list)' for r in em)
    items = sorted(dc.items(), key=lambda kv: -kv[1])
    hbar([k.replace('_', ' ') for k, _ in items], [v for _, v in items], BLUE, 'fig1_design_mix', f'Study designs in the {n:,} included studies',
         'Evidence-map design class; only quasi-experimental and experimental designs can support a causal claim', 'Studies')
    yrs = Counter(int(r['publication_year']) for r in ed if r['publication_year'].strip().isdigit())
    lo, hi = min(yrs), max(yrs)
    fig, ax = plt.subplots(figsize=(7.2, 3.4))
    xs = list(range(lo, hi + 1))
    ax.bar(xs, [yrs.get(x, 0) for x in xs], color=BLUE, width=0.8)
    ax.grid(axis='y', color='#e6e5e0', linewidth=0.6); ax.set_axisbelow(True)
    peak = max(yrs, key=yrs.get)
    ax.annotate(f'{peak}: {yrs[peak]}', (peak, yrs[peak]), xytext=(-6, 4), textcoords='offset points', ha='right', fontsize=9)
    ax.set_xlabel('Publication year'); ax.set_ylabel('Studies')
    since = sum(v for k, v in yrs.items() if k >= 2010)
    finish(fig, ax, 'fig2_publication_years', 'When the included studies were published', f'{since:,} of {sum(yrs.values()):,} ({100 * since / sum(yrs.values()):.0f}%) were published in 2010 or later; {hi} is a partial year')
    top = F['country_top10_single_name']
    hbar([c for c, _ in top], [v for _, v in top], BLUE, 'fig3_countries', 'The ten most frequent single countries',
         f"Free-text country field; {F['country_multi_or_regional_studies']} multi-country or regional studies and {F['country_blank_studies']} blank are not counted", 'Studies')
    # direction by family (sign of each study's own estimate; not effect sizes)
    fams = {f: sa.parse_signs(f) for f in 'ABC'}
    names = {'A': 'A  Legal recognition and eligibility', 'B': 'B  Administrative assistance', 'C': 'C  Administrative barriers, ownership, price'}
    cols = [('positive', BLUE, 'Positive'), ('negative', ORANGE, 'Negative'), ('mixed', VIOLET, 'Mixed'), ('null', GREY, 'Null')]
    fig, ax = plt.subplots(figsize=(7.4, 3.3))
    for i, f in enumerate('ABC'):
        c = Counter(fams[f].values()); left = 0
        for key, col, lab in cols:
            v = c.get(key, 0)
            if v:
                ax.barh(i, v, left=left, color=col, height=0.55, edgecolor=SURF, linewidth=2)
                ax.text(left + v / 2, i, str(v), ha='center', va='center', color='white', fontsize=10, fontweight='bold')
                left += v
        ax.text(left + 0.4, i, f'k = {left}', va='center', fontsize=9, color=MUTED)
    ax.set_yticks(range(3)); ax.set_yticklabels([names[f] for f in 'ABC']); ax.invert_yaxis(); ax.set_xlim(0, 24); ax.set_xlabel('Studies (sign of each study\'s own extracted association)')
    handles = [plt.Rectangle((0, 0), 1, 1, color=col) for _, col, _ in cols]
    ax.legend(handles, [lab for _, _, lab in cols], ncol=4, frameon=False, loc='upper center', bbox_to_anchor=(0.5, -0.28), fontsize=9)
    finish(fig, ax, 'fig4_direction_by_family', 'Direction of association in the three structured syntheses', 'Counts of studies; sign and valence can differ. Nothing is pooled and no effect size is shown')
    tools = F['tools']
    items = sorted(tools.items(), key=lambda kv: -kv[1])
    hbar([k for k, _ in items], [v for _, v in items], BLUE, 'fig5_appraisal_tools', 'Which appraisal instrument each study received',
         'Rule-based ratings; the Legal Framework instrument is the project\'s own and is not validated', 'Studies')
    print('wrote', len(list(OUT.glob('fig*.svg'))), 'figures to', OUT.relative_to(cf.ROOT))


if __name__ == '__main__':
    main()
