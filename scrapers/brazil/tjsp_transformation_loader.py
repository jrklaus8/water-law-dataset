"""
TJSP Transformation Analysis loader
====================================
Converts the hand-coded TJSP Transformation Analysis 2021 XLSX
(TJSP-All Cases-transformation-2021.xlsx) into a normalized JSON
compatible with merge_national.py.

The XLSX contains 200 TJSP cases (1997-2015) hand-coded for:
- Human rights language (HR Lang)
- Sustainability language (Sust Lang)
- Governance category (basic services / building / environment)
- MP involvement, collective claims, win/loss, municipality, etc.

Usage:
  python tjsp_transformation_loader.py \
    --xlsx "path/to/TJSP-All Cases-transformation-2021.xlsx" \
    --out "path/to/tjsp_transformation_analysis.json"
"""
import sys, json, re, argparse
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    raise SystemExit("Install pandas: pip install pandas openpyxl")

def clean(v):
    if pd is not None and hasattr(pd, 'isna') and pd.isna(v): return ''
    return str(v).strip() if v is not None else ''

def intval(v):
    try: return int(float(v)) if v is not None and str(v).strip() not in ('', 'nan') else None
    except: return None

def gov_cat(row):
    cats = []
    if intval(row.get('Governance category: basic services 1=yes')) == 1:
        cats.append('basic_services')
    if intval(row.get('Governance category: building in protected areas or in environmentally destructive ways 1=yes')) == 1:
        cats.append('building_protected_areas')
    if intval(row.get('Governance category: environment, not building 1=yes')) == 1:
        cats.append('environment_not_building')
    return '|'.join(cats)

def lang_cat(row):
    hr   = intval(row.get('HR Lang? 1=yes'))
    sust = intval(row.get('Sust Lang? 1=yes'))
    if hr == 1 and sust == 1: return 'HR+Sustainability'
    if hr == 1:  return 'HR_only'
    if sust == 1: return 'Sustainability_only'
    return 'None'

def convert(xlsx_path, out_path):
    xl   = pd.ExcelFile(xlsx_path)
    main = xl.parse('TJSP ALL Cases 4 Analysis')
    notes_df = xl.parse('LJH Case notes-ALL')
    notes_by_id = {str(r.get('Case #','')).strip(): r for _, r in notes_df.iterrows()}

    cases = []
    for _, row in main.iterrows():
        case_id = clean(row.get('Number',''))
        yr = intval(row.get('Judgment year'))

        topic  = clean(row.get('Key Topic of Case (what principle is at stake?)', ''))
        ruling = clean(row.get('What is the ruling on this principle?', ''))
        decision = clean(row.get('Decision', ''))
        topic_pt = clean(row.get('Topic of the case', ''))
        goal   = clean(row.get('Goal', ''))
        legal  = clean(row.get('Legal basis of judgment', ''))
        nr = notes_by_id.get(case_id, {})
        useful_q = clean(nr.get('Useful quotes','') if hasattr(nr,'get') else '')

        parts = []
        if topic:    parts.append(f'Key topic: {topic}')
        if ruling:   parts.append(f'Ruling: {ruling}')
        if topic_pt: parts.append(f'Topic (PT): {topic_pt}')
        if decision: parts.append(f'Decision: {decision}')
        if goal:     parts.append(f'Goal: {goal}')
        if legal:    parts.append(f'Legal basis: {legal}')
        if useful_q: parts.append(f'Useful quotes: {useful_q}')
        summary = ' | '.join(parts)[:3000]

        import datetime
        jdate = clean(row.get('Judgment date',''))
        try:
            if isinstance(row.get('Judgment date'), datetime.datetime):
                jdate = row['Judgment date'].strftime('%Y-%m-%d')
        except: pass

        cases.append({
            'country': 'Brazil', 'source': 'TJSP-Transformation-2021',
            'tribunal': 'TJSP', 'court_name': 'Tribunal de Justiça de São Paulo',
            'case_id': case_id, 'title': f'TJSP {case_id} ({yr})',
            'date': jdate, 'year': yr,
            'case_type': clean(row.get('Category of action','')),
            'chamber':   clean(row.get('Court Section','')),
            'judge':     clean(row.get('Deciding Judge(s)','')),
            'legal_area': clean(row.get('Court Type','')),
            'summary': summary, 'url': '',
            'municipality':      clean(row.get('Municipality of case','')),
            'plaintiff':         clean(row.get('Plaintff/Appellant','')),
            'defendant':         clean(row.get('Defendant/Appellee','')),
            'key_topic':         topic,
            'key_legislation':   clean(row.get('Key legislation','')),
            'hr_language':       intval(row.get('HR Lang? 1=yes')),
            'sust_language':     intval(row.get('Sust Lang? 1=yes')),
            'collective_claim':  intval(row.get('Collective claim? 1=yes')),
            'mp_involved':       intval(row.get('MP involved? 1=yes')),
            'collective_impact': intval(row.get('Collective impact? 1=yes')),
            'target_municipality': intval(row.get('Target? 1=municipality')),
            'target_water_company': intval(row.get('Target? 1=w&s co')),
            'win':               intval(row.get('Win? 1=yes')),
            'mixed_result':      intval(row.get('Mixed result? 1=yes')),
            'governance_category': gov_cat(row),
            'language_category':   lang_cat(row),
            'notes':             clean(row.get('Notes','')),
        })

    out_path = Path(out_path)
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(cases, f, ensure_ascii=False, indent=2)
    print(f'Saved {len(cases)} cases → {out_path}')

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--xlsx', required=True)
    ap.add_argument('--out',  required=True)
    args = ap.parse_args()
    convert(args.xlsx, args.out)
