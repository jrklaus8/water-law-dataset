"""Add TJRJ to the national Brazil water law dataset."""
import os
import json, csv, sys
from pathlib import Path
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')

DL = Path(os.getenv('DATA_DIR', '.'))

def normalize(c):
    return {
        'tribunal':        c.get('tribunal', ''),
        'estado':          c.get('estado', ''),
        'num_processo':    c.get('num_processo', '') or c.get('numero_processo', ''),
        'data_julgamento': c.get('data_julgamento', '') or c.get('data_publicacao', ''),
        'ano':             c.get('ano', ''),
        'classe':          c.get('classe', ''),
        'camara_orgao':    c.get('camara_orgao', '') or c.get('orgao_julgador', ''),
        'relator':         c.get('relator', ''),
        'ementa':          (c.get('ementa', '') or '')[:3000],
        'url':             c.get('url', ''),
    }

# Load existing CSV (already has TJSP, TJSC, TJRR, TJAC, TJPI, TJTO, TJDFT)
existing = []
csv_path = DL / 'brazil_water_law_national.csv'
with open(csv_path, encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        existing.append(row)
print(f'Existing records: {len(existing)}')

# Check courts already present
courts_present = Counter(r['tribunal'] for r in existing)
print(f'Courts: {dict(courts_present)}')

# Load TJRJ
with open(DL / 'tjrj_cases_2016_2026.json', encoding='utf-8') as f:
    tjrj = json.load(f)
print(f'TJRJ cases: {len(tjrj)}')

# Normalize and add
rj_norm = [normalize(c) for c in tjrj]

# Combine
all_cases = existing + rj_norm
print(f'Total after merge: {len(all_cases)}')

# Save updated CSV
fieldnames = list(existing[0].keys())
with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in all_cases:
        # Ensure all fields present
        out = {k: row.get(k, '') for k in fieldnames}
        writer.writerow(out)
print(f'CSV saved: {csv_path}')

# Update XLSX
try:
    from openpyxl import load_workbook
    from openpyxl.styles import PatternFill, Font, Alignment

    xl_path = DL / 'brazil_water_law_national.xlsx'
    wb = load_workbook(xl_path)
    ws = wb['Dados']

    # Find last row
    max_row = ws.max_row

    # Court colour for TJRJ (yellow)
    fill_rj = PatternFill('solid', fgColor='FFF2CC')

    start_row = max_row + 1
    for i, c in enumerate(rj_norm):
        row_num = start_row + i
        vals = [
            c['tribunal'], c['estado'], c['num_processo'],
            c['data_julgamento'], c['ano'], c['classe'],
            c['camara_orgao'], c['relator'],
            c['ementa'][:500], c['url'],
        ]
        for col, val in enumerate(vals, 1):
            cell = ws.cell(row=row_num, column=col, value=val)
            cell.fill = fill_rj

    # Update pivot sheet
    if 'Pivot' in wb.sheetnames:
        wp = wb['Pivot']
        # Just clear and rewrite note
        wp['A1'] = f'Total geral: {len(all_cases)} casos | Atualizado 2026-04-25'

    wb.save(xl_path)
    print(f'XLSX updated: {xl_path}')
except Exception as e:
    print(f'XLSX error: {e}')

# Summary by court and year
print('\n=== Final dataset summary ===')
by_court = Counter(r['tribunal'] for r in all_cases)
for court, n in sorted(by_court.items(), key=lambda x: -x[1]):
    print(f'  {court}: {n}')
print(f'\nGRAND TOTAL: {len(all_cases)} water law cases')
