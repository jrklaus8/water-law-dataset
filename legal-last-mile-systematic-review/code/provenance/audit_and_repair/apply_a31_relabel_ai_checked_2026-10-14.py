"""2026-10-14, open item A31 (PI instruction, reviewer CK): keep the `CK` human-verification count strictly to records the author reviewed and ruled on.

The Round-11 pass (apply_a26_swim_core_checks_2026-10-14.py) recorded 18 SWiM core studies as confirmed by the author ('A26 ruling ... by CK', reviewer_2 = 'CK') although the confirmation rested on the AI's extraction-level
scope and outcome check, not on the author reading the paper's passages. The author ruled that those 18 rows are to be recorded as AI-checked, not as human `CK` confirmations.

What this script does (idempotent; run from legal-last-mile-systematic-review/):
1. In 02_screening/full_text/full_text_screening_database.csv, for each of the 18 rows: the 'A26 ruling 2026-10-14 by CK: confirms ...' note is replaced by an 'A31 relabel' note that says AI-checked, not a human
   confirmation (the AI's reason is kept); `reviewer_2` goes back to its value before the A26 pass (blank; S1062 keeps its Codex second-model label, which was never changed). Decision, code and conflict fields are untouched.
2. The status file SWIM_CK_CHECKS_2026-10-14.csv is replaced by SWIM_AI_SCOPE_CHECKS_2026-10-14.csv: the same 28 studies, but the column that said 'passed' / 'flagged' is now `ai_scope_check` and the author's direction-coding
   confirmation columns are empty for every study (the author has not confirmed any study's direction coding in this file). The ten A28 studies keep their flag text; the A28 script adds their `a28_outcome`.
S1140 and S1136 (reasoned non-fits since the A29 ruling) keep the 'A26 ruling' entry in their full-text notes because those rest on the author's own A26 and A29 rulings, not on the AI scope check.
Do not re-run apply_a26_swim_core_checks_2026-10-14.py after this script: it would restore the CK labels (it now stops if the new file exists)."""
import csv, os, re, sys, tempfile
sys.path.insert(0, 'code/analysis')
csv.field_size_limit(sys.maxsize)
import current_figures as cf

FT = '02_screening/full_text/full_text_screening_database.csv'
OLD = '05_analysis/effect_sizes/SWIM_CK_CHECKS_2026-10-14.csv'
NEW = '05_analysis/effect_sizes/SWIM_AI_SCOPE_CHECKS_2026-10-14.csv'
OK_MARK = 'A26 ruling 2026-10-14 by CK'
NEW_MARK = 'A31 relabel 2026-10-14'
STUDIES = 'S404 S765 S780 S882 S930 S1122 S470 S471 S526 S539 S593 S631 S749 S879 S1032 S1038 S1062 S1162'.split()
WHY_RE = re.compile(r'\(narrow scope and outcome check passed: (.*?)\) and the two-column direction coding')
SEG_RE = re.compile(re.escape(OK_MARK) + r': confirms the inclusion.*?checked against the full text by the AI, not by a human\.', re.S)


def read(p):
    raw = open(p, newline='', encoding='utf-8').read()
    with open(p, newline='', encoding='utf-8') as f:
        rd = csv.DictReader(f)
        return rd.fieldnames, list(rd), '\r\n' if '\r\n' in raw[:20000] else '\n'


def write(p, fields, rows, eol):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(p) or '.', suffix='.tmp')
    with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator=eol)
        w.writeheader(); w.writerows(rows)
    os.replace(tmp, p)


def note_for(why):
    why = why.replace('A26 ruling', 'A26 effect-row decision')   # the old wording would count as a human ruling mark
    return (f'{NEW_MARK}: AI-checked, NOT a human confirmation. The AI read this study\'s extraction row against the narrow reading of criterion 2 (a legal or administrative access rule or mechanism) and criterion 4 '
            f'(a household access outcome) and found no red flag ({why}). The author has not reviewed this study\'s evidence and has not confirmed its inclusion or its two-column direction coding (open item A30); '
            f'reviewer_2 is restored to its value before the A26 pass. The effect estimate was extracted and checked against the full text by the AI, not by a human.')


ed = {r['study_id']: r for r in cf.read('ed')}
fields, ft, eol = read(FT)
by = {r['record_id']: r for r in ft}
n = n_rev = 0
for s in STUDIES:
    r = by[ed[s]['record_id']]
    if NEW_MARK in r['notes']:
        continue
    m = SEG_RE.search(r['notes'])
    assert m, f'{s}: the A26 confirmation note was not found'
    why = WHY_RE.search(m.group(0)).group(1)
    r['notes'] = (r['notes'][:m.start()] + note_for(why) + r['notes'][m.end():]).strip(' |')
    if r['reviewer_2'] == 'CK':
        r['reviewer_2'] = ''; n_rev += 1
    else:
        assert s == 'S1062' and r['reviewer_2'].startswith('Codex-'), (s, r['reviewer_2'])
    assert not any(k in r['notes'] for k in cf.HUMAN_RULING_MARKS), f'{s}: still carries a human-ruling mark'
    n += 1
write(FT, fields, ft, eol)

if os.path.exists(OLD):
    f0, rows, e0 = read(OLD)
    out = []
    for r in rows:
        out.append({'study_id': r['study_id'], 'family': r['family'], 'ai_scope_check': r['scope_outcome_check'], 'check_note': r['check_note'].replace('A26 ruling', 'A26 effect-row decision'),
                    'a28_outcome': '', 'ck_raw_sign_agrees (Y/N)': '', 'ck_substantive_direction_agrees (Y/N)': '',
                    'ck_comment': 'AI-checked only; awaits the author (A30)' if r['scope_outcome_check'] == 'passed' else r['ck_comment']})
    with open(NEW, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(out[0]), lineterminator='\r\n'); w.writeheader(); w.writerows(out)
    os.remove(OLD)
print(f'relabelled {n} rows ({n_rev} reviewer_2 values restored to blank); checks file now {NEW}')
