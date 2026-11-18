#!/usr/bin/env python3
"""Build blind evidence cards for the 50 tier-3 includes of the reviewer-2 queue (open item A6).

Reads only repository files plus a record_id -> Google Drive file id map. Writes a Markdown
card pack and a CSV fill-in sheet. The reviewer columns are written BLANK; nothing here
records a human decision. The AI's own reasoning is placed after the decision boxes.
"""
import argparse, csv, hashlib, random

EXPOSURE = ['eligibility','burden','discretion_accommodation','enforcement','documentation','tenure','property',
            'planning','zoning','building_permit','service_area','fees','procedural_steps','delay','discretion',
            'hardship_exception','administrative_review','complaint','judicial_review','disconnection',
            'reconnection','sanction','participation','institutional_fragmentation','political_coordination',
            'bureaucratic_assistance','formal_connection']
OUTCOME = ['water_access','sanitation_access','service_coverage','service_reliability','service_quantity',
           'service_quality','affordability','service_continuity','application_success','refusal','delay_outcome']

def rd(p): return list(csv.DictReader(open(p, encoding='utf-8')))
def clip(s, n): s = ' '.join((s or '').split()); return s if len(s) <= n else s[:n-1] + '…'

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--drive-map', required=True)
    ap.add_argument('--out-md', required=True)
    ap.add_argument('--out-csv', required=True)
    ap.add_argument('--out-blind-csv', required=True, help='input file for a blind second AI: no tier, no AI decision, no extraction, shuffled')
    ap.add_argument('--seed', type=int, default=20261118)
    a = ap.parse_args()
    q = [r for r in rd('02_screening/full_text/full_text_reviewer_2_priority_queue_2026-09-28.csv') if r['priority_tier'] == '3']
    ext = {r['study_id']: r for r in rd('03_extraction/extracted_data/extraction_database.csv')}
    trail = {r['study_id']: r for r in rd('00_admin/STUDY_AUDIT_TRAIL.csv')}
    drive = {r['record_id']: r['drive_file_id'] for r in rd(a.drive_map)}
    q.sort(key=lambda r: int(r['priority_rank']))
    md = ['# A6 tier-3 evidence cards (50 AI includes)', '',
          'Prepared 2026-11-15. **Nothing on these cards is a human decision.** Reviewer boxes are blank.',
          'Decide each record from the paper first (Drive link), using the checklist. Only then read the',
          '"AI reasoning" at the bottom of the card. Fill `A6_TIER3_FILL_IN_SHEET_2026-11-15.csv`.', '',
          'Criteria and codes: `REVIEWER_2_CHECKLIST.md` and `INCLUSION_EXCLUSION.md`. For includes, step 5 asks you to check',
          'that the extraction summary on the card matches the paper (country, design, sample size, exposure, outcome, effect direction).', '']
    rows = []
    for r in q:
        s, rid = r['study_id'], r['record_id']
        e, t = ext[s], trail.get(s, {})
        link = f"https://drive.google.com/file/d/{drive[rid]}/view" if rid in drive else ''
        exp = [k for k in EXPOSURE if e.get(k, '').upper() == 'TRUE']
        out = [k for k in OUTCOME if e.get(k, '').upper() == 'TRUE']
        eff = ' | '.join(f"{k}: {clip(e[k], 320)}" for k in ('effect_measure','effect_estimate','lower_CI','upper_CI','p_value','adjusted_or_unadjusted') if e.get(k))
        md += [f"## {r['priority_rank']}. {s} — {r['authors'][:90]} ({r['year']})", '',
               f"**{r['title']}**  ", f"record `{rid}` · DOI {r['doi'] or 'none recorded'}  ",
               f"**Paper:** {link or 'NOT FOUND in Drive; retrieve via DOI/URL: ' + (r['url'] or 'none')}", '',
               '**Where the extractor says to look:** ' + (clip(e.get('exact_location'), 200) or 'not recorded') +
               (f" (source: {clip(e.get('source_document'), 120)}; p. {e.get('page') or '?'}; section: {clip(e.get('section'), 80) or '?'})"), '',
               '**Extraction row to check against the paper (checklist step 5):**', '',
               f"- Country / place: {e.get('country') or '?'}; {e.get('subnational_unit') or '-'}",
               f"- Design: {e.get('study_design') or '?'} ({t.get('study_design_class') or '-'})",
               f"- Population / sample: {clip(e.get('population'), 160) or '?'}; n = {clip(e.get('extraction_sample_size') or e.get('sample_size'), 120) or '?'}",
               f"- Legal/administrative exposure flags marked TRUE: {', '.join(exp) or 'none'}",
               f"- Outcome flags marked TRUE: {', '.join(out) or 'none'}",
               f"- Effect as extracted: {eff or 'none recorded'}",
               f"- In the 31-study SWiM set: {t.get('swim_inclusion_status') or 'no'}; direction confirmed by author: {t.get('direction_coding_confirmed_by_author') or 'no'}", '',
               '**Your decision (blank):** decision ____  code ____  agree with AI Y/N ____  extraction matches Y/N ____  comment ____', '',
               '---', f"*AI reasoning (read only after you decide).* AI decision: **{r['ai_decision']}** by {r['ai_reviewer_label']}. "
               + clip(r['ai_reasoning_READ_AFTER_YOUR_OWN_JUDGMENT'], 600), '']
        rows.append({'priority_rank': r['priority_rank'], 'study_id': s, 'record_id': rid, 'year': r['year'],
                     'title': r['title'], 'doi': r['doi'], 'paper_link': link,
                     'reviewer_decision (include/exclude/cannot_tell)': '', 'exclusion_code (E01-E12)': '',
                     'agrees_with_AI (Y/N)': '', 'extraction_matches_paper (Y/N)': '', 'comment': '',
                     'reviewer_initials': '', 'date_decided (YYYY-MM-DD)': '',
                     'paper_read (full/partial/abstract_only/not_read)': '',
                     'saw_AI_reasoning_before_deciding (Y/N)': '', 'saw_Gemini_output_before_deciding (Y/N)': '',
                     'minutes_spent (optional)': ''})
    open(a.out_md, 'w', encoding='utf-8').write('\n'.join(md))
    with open(a.out_csv, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    order = list(range(len(rows)))
    random.Random(a.seed).shuffle(order)
    blind_fields = ['order', 'record_id', 'title', 'authors', 'year', 'doi', 'paper_link']
    with open(a.out_blind_csv, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=blind_fields); w.writeheader()
        for n, i in enumerate(order, 1):
            r, src = rows[i], q[i]
            w.writerow({'order': n, 'record_id': r['record_id'], 'title': r['title'], 'authors': src['authors'],
                        'year': r['year'], 'doi': r['doi'], 'paper_link': r['paper_link']})
    print('blind input: shuffled with seed', a.seed, '; sha256', hashlib.sha256(open(a.out_blind_csv, 'rb').read()).hexdigest()[:16])
    print(len(rows), 'cards;', sum(1 for r in rows if r['paper_link']), 'with Drive link')

if __name__ == '__main__':
    main()
