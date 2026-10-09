#!/usr/bin/env python3
"""List the abstract-only extractions in priority order, with the details needed to fetch each full text.

Priority: 1 = RoB 2 / ROBINS-I studies; 2 = AMSTAR 2 reviews (eligibility never confirmed from full text); 3 = quantitative-synthesis-eligible;
4 = JBI Cross-Sectional; 5 = MMAT; 6 = Legal Framework; 7 = CASP Qualitative; 8 = no tool applies. Within a tier, by study_id.
Writes 03_extraction/extracted_data/abstract_only_fulltext_request_list_2026-09-29.csv. Run from the project root.
"""
import csv, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import current_figures as cf  # noqa: E402

OUT = cf.ROOT / '03_extraction/extracted_data/abstract_only_fulltext_request_list_2026-09-29.csv'
TIER = {'RoB 2': 1, 'ROBINS-I': 1, 'AMSTAR 2': 2, 'JBI Cross-Sectional': 4, 'MMAT': 5, 'Legal Framework': 6, 'CASP Qualitative': 7, 'NONE': 8}  # an abstract-only ROBINS-I or NONE row used to raise KeyError (2026-10-04 review)
WHY = {1: 'RoB 2 / ROBINS-I causal-capable design; rating is low-confidence', 2: 'AMSTAR 2 review; systematic-review eligibility never confirmed from full text',
       3: 'quantitative-synthesis-eligible', 4: 'quantitative cross-sectional design', 5: 'mixed-methods design', 6: 'documentary/doctrinal design', 7: 'qualitative design', 8: 'no appraisal tool applies (narrative or documentary review)'}


def rows():
    ed = {r['study_id']: r for r in cf.read('ed')}
    em = {r['study_id']: r for r in cf.read('em')}
    ft = {r['record_id']: r for r in cf.read('ft')}
    out = []
    for s, r in ed.items():
        if not r['extraction_note'].startswith(cf.ABSTRACT_ONLY_PREFIXES):
            continue
        tool = cf.tool_of(r['risk_of_bias_tool'])
        tier = TIER[tool]
        if tier > 3 and em[s]['quantitative_synthesis_eligible'] == 'TRUE':
            tier = 3
        f = ft[r['record_id']]
        out.append({'priority_tier': tier, 'study_id': s, 'record_id': r['record_id'], 'risk_of_bias_tool': tool, 'why': WHY[tier], 'year': f['year'], 'authors': f['authors'],
                    'title': f['title'], 'doi': f['doi'], 'url': f['url'], 'full_text_status': f['full_text_status'], 'extraction_note_start': r['extraction_note'][:140]})
    return sorted(out, key=lambda x: (x['priority_tier'], int(x['study_id'][1:])))


if __name__ == '__main__':
    rs = rows()
    with open(OUT, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rs[0]), lineterminator='\r\n'); w.writeheader(); w.writerows(rs)
    print('wrote', OUT.name, len(rs), 'rows')
