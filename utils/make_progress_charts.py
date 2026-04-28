"""Generate progress PNG charts for the Brazil water law dataset."""
import os
import json, sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec
import numpy as np

DL = Path(os.getenv('DATA_DIR', '.'))

# ── Data ──────────────────────────────────────────────────────────────────────
COURTS = [
    # (UF, court, cases_water, cases_total, status)
    # status: 'done', 'done_noisy', 'blocked'
    ('SP', 'TJSP',  574,   574,  'done'),
    ('SC', 'TJSC', 1224,  1224,  'done'),
    ('DF', 'TJDFT',4894,  8421,  'done_noisy'),
    ('RR', 'TJRR',   21,    21,  'done'),
    ('AC', 'TJAC',   33,    33,  'done'),
    ('TO', 'TJTO',   17,    17,  'done'),
    ('PI', 'TJPI',   15,    15,  'done'),
    # blocked — sorted by estimated population (rough proxy for caseload)
    ('MG', 'TJMG',    0,     0,  'blocked'),
    ('RJ', 'TJRJ',    0,     0,  'blocked'),
    ('BA', 'TJBA',    0,     0,  'blocked'),
    ('RS', 'TJRS',    0,     0,  'blocked'),
    ('PR', 'TJPR',    0,     0,  'blocked'),
    ('PE', 'TJPE',    0,     0,  'blocked'),
    ('CE', 'TJCE',    0,     0,  'blocked'),
    ('PA', 'TJPA',    0,     0,  'blocked'),
    ('MA', 'TJMA',    0,     0,  'blocked'),
    ('GO', 'TJGO',    0,     0,  'blocked'),
    ('AM', 'TJAM',    0,     0,  'blocked'),
    ('ES', 'TJES',    0,     0,  'blocked'),
    ('MS', 'TJMS',    0,     0,  'blocked'),
    ('MT', 'TJMT',    0,     0,  'blocked'),
    ('PB', 'TJPB',    0,     0,  'blocked'),
    ('RN', 'TJRN',    0,     0,  'blocked'),
    ('AL', 'TJAL',    0,     0,  'blocked'),
    ('SE', 'TJSE',    0,     0,  'blocked'),
    ('RO', 'TJRO',    0,     0,  'blocked'),
    ('AP', 'TJAP',    0,     0,  'blocked'),
]

COLORS = {
    'done':       '#2d7a45',   # dark green
    'done_noisy': '#7ec8a4',   # lighter green (full-text noise)
    'blocked':    '#d64045',   # red
}
LABELS = {
    'done':       'Coletado (ementa limpa)',
    'done_noisy': 'Coletado (texto integral, ~58% relevante)',
    'blocked':    'Bloqueado / inacessível',
}

# ── Figure layout ─────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(18, 14), facecolor='#f7f9fc')
fig.suptitle('Dataset: Jurisprudência Hídrica – Tribunais Estaduais Brasileiros (2016–2026)',
             fontsize=16, fontweight='bold', color='#1a2a4a', y=0.98)

gs = GridSpec(2, 2, figure=fig, hspace=0.42, wspace=0.35,
              left=0.06, right=0.97, top=0.93, bottom=0.06)

ax1 = fig.add_subplot(gs[0, :])   # top full width  – bar by court
ax2 = fig.add_subplot(gs[1, 0])   # bottom left     – pie
ax3 = fig.add_subplot(gs[1, 1])   # bottom right    – year distribution

# ── Chart 1: Cases per court (horizontal bar) ─────────────────────────────────
ax1.set_facecolor('#f0f4f8')
labels = [f'{c[1]}  ({c[0]})' for c in COURTS]
water  = [c[2] for c in COURTS]
noise  = [c[3] - c[2] for c in COURTS]   # extra (noisy) for TJDFT
colors = [COLORS[c[4]] for c in COURTS]

y_pos = np.arange(len(COURTS))
bars1 = ax1.barh(y_pos, water, color=colors, height=0.65, zorder=3)

# Add the noisy portion on top for TJDFT
noisy_idx = [i for i, c in enumerate(COURTS) if c[4] == 'done_noisy']
for i in noisy_idx:
    ax1.barh(i, noise[i], left=water[i], color='#b8dfc9', height=0.65, zorder=3)
    ax1.text(water[i] + noise[i] + 30, i, f'+{noise[i]:,} ruído',
             va='center', ha='left', fontsize=7.5, color='#666')

# Value labels
for i, (bar, w) in enumerate(zip(bars1, water)):
    if w > 0:
        ax1.text(w + 15, i, f'{w:,}', va='center', ha='left',
                 fontsize=8.5, color='#1a2a4a', fontweight='bold')

ax1.set_yticks(y_pos)
ax1.set_yticklabels(labels, fontsize=9)
ax1.set_xlabel('Número de acórdãos coletados', fontsize=10)
ax1.set_title('Acórdãos coletados por tribunal', fontsize=12, fontweight='bold',
              color='#1a2a4a', pad=10)
ax1.set_xlim(0, 5800)
ax1.grid(axis='x', linestyle='--', alpha=0.5, zorder=0)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.invert_yaxis()

# Legend
patches = [mpatches.Patch(color=COLORS[k], label=LABELS[k]) for k in COLORS]
patches.append(mpatches.Patch(color='#b8dfc9', label='Ruído de texto integral (TJDFT)'))
ax1.legend(handles=patches, loc='lower right', fontsize=8.5, framealpha=0.8)

# ── Chart 2: Pie — courts status ─────────────────────────────────────────────
ax2.set_facecolor('#f0f4f8')
n_done      = sum(1 for c in COURTS if c[4] in ('done', 'done_noisy'))
n_blocked   = sum(1 for c in COURTS if c[4] == 'blocked')

pie_vals    = [n_done, n_blocked]
pie_labels  = [f'Coletados\n({n_done}/27)', f'Bloqueados\n({n_blocked}/27)']
pie_colors  = ['#2d7a45', '#d64045']
explode     = [0.05, 0]

wedges, texts, autotexts = ax2.pie(
    pie_vals, labels=pie_labels, colors=pie_colors, explode=explode,
    autopct='%1.0f%%', startangle=90,
    textprops={'fontsize': 10}, pctdistance=0.65
)
for at in autotexts:
    at.set_fontsize(12)
    at.set_fontweight('bold')
    at.set_color('white')

ax2.set_title('Status de coleta\n(27 Tribunais Estaduais)', fontsize=11,
              fontweight='bold', color='#1a2a4a', pad=10)

# Add total cases annotation
total_water = sum(c[2] for c in COURTS)
ax2.text(0, -1.35, f'Total acórdãos hídricos coletados: {total_water:,}',
         ha='center', va='center', fontsize=10, fontweight='bold', color='#1a2a4a')

# ── Chart 3: Year distribution ────────────────────────────────────────────────
ax3.set_facecolor('#f0f4f8')

FILES = [
    ('TJSP', 'SP', DL / 'tjsp_cases_all.json',          'ano',  False),
    ('TJSC', 'SC', DL / 'tjsc_cases_2016_2026.json',    'ano',  False),
    ('TJRR', 'RR', DL / 'tjrr_cases_2016_2026.json',    'ano',  False),
    ('TJAC', 'AC', DL / 'tjac_cases_2016_2026.json',    'ano',  False),
    ('TJPI', 'PI', DL / 'tjpi_cases_2016_2026.json',    'year', False),
    ('TJTO', 'TO', DL / 'tjto_cases_2016_2026.json',    'year', False),
    ('TJDFT','DF', DL / 'tjdft_cases_2016_2026.json',   'ano',  True),
]
WATER_KW = ['água','agua','saneamento','abastecimento','esgoto',
            'hídrico','hidrico','manancial','potável','potavel',
            'fornecimento','distribuição','distribuicao']

years = list(range(2016, 2027))
year_counts = {y: 0 for y in years}

for court, uf, path, yr_field, filter_water in FILES:
    if not path.exists():
        continue
    with open(path, encoding='utf-8') as f:
        cases = json.load(f)
    if filter_water:
        cases = [c for c in cases if any(
            kw in (c.get('ementa','') + c.get('decisao','')).lower()
            for kw in WATER_KW)]
    for c in cases:
        y = c.get(yr_field)
        if y and 2016 <= int(y) <= 2026:
            year_counts[int(y)] = year_counts.get(int(y), 0) + 1

yr_vals = [year_counts[y] for y in years]
bar_colors = ['#2d7a45' if y < 2026 else '#7ec8a4' for y in years]

bars3 = ax3.bar(years, yr_vals, color=bar_colors, width=0.7, zorder=3)
for bar, val in zip(bars3, yr_vals):
    ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
             f'{val:,}', ha='center', va='bottom', fontsize=8, fontweight='bold', color='#1a2a4a')

ax3.set_xticks(years)
ax3.set_xticklabels([str(y) for y in years], rotation=45, fontsize=9)
ax3.set_ylabel('Acórdãos', fontsize=10)
ax3.set_title('Distribuição temporal\n(acórdãos hídricos relevantes por ano)', fontsize=11,
              fontweight='bold', color='#1a2a4a', pad=10)
ax3.grid(axis='y', linestyle='--', alpha=0.5, zorder=0)
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax3.text(2025.5, max(yr_vals) * 0.92, '2026\nparcial', ha='center', fontsize=7.5,
         color='#888', style='italic')

# ── Save ──────────────────────────────────────────────────────────────────────
out = DL / 'water_law_progress.png'
fig.savefig(out, dpi=150, bbox_inches='tight', facecolor='#f7f9fc')
plt.close()
print(f'Salvo: {out}')