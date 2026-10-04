"""2026-10-04 full-text re-extraction campaign runner. Each reextract_2026-10-04/<study>.json holds {fields, evidence_level, pdf_note} written after reading that study's PDF
from the researcher's Drive. The runner applies every JSON whose extraction row still carries the abstract-only note prefix (idempotent: applied studies are skipped).
See _reextract_lib.py. Run from legal-last-mile-systematic-review/."""
import csv, glob, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _reextract_lib as L
csv.field_size_limit(sys.maxsize)
state = {r['study_id']: r['extraction_note'].startswith(L.PREFIX) for r in csv.DictReader(open(L.ED, newline=''))}
upd, ev, note = {}, {}, {}
notes_now = {r['study_id']: r['extraction_note'] for r in csv.DictReader(open(L.ED, newline=''))}
u2, e2, n2 = {}, {}, {}
for p in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reextract_2026-10-04', 'S*.json'))):
    s = os.path.basename(p)[:-5]
    d = json.load(open(p, encoding='utf-8'))
    if d.get('nonprefix'):  # sparse-audit rows without the abstract-only prefix; idempotent via the re-extraction marker in the note
        if 'Re-extracted ' + L.DATE not in notes_now.get(s, ''):
            u2[s], e2[s], n2[s] = d['fields'], d['evidence_level'], d['pdf_note']
        continue
    if not state.get(s):
        continue
    upd[s], ev[s], note[s] = d['fields'], d['evidence_level'], d['pdf_note']
if upd:
    L.apply('re-extraction ' + ', '.join(sorted(upd, key=lambda x: int(x[1:]))), upd, ev, note)
if u2:
    L.apply('re-extraction (non-prefix) ' + ', '.join(sorted(u2, key=lambda x: int(x[1:]))), u2, e2, n2, strict=False)
if not upd and not u2:
    print('nothing to apply')
