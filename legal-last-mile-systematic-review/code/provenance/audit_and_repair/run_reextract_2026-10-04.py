"""2026-10-04 full-text re-extraction campaign runner. Each reextract_2026-10-04/<study>.json holds {fields, evidence_level, pdf_note, optional date} written after reading that study's PDF
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
when = {}  # study -> date stamped on the row (the JSON's optional "date"; the 2026-10-04 campaign default otherwise)
DEFAULT_DATE = L.DATE
for p in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reextract_2026-10-04', 'S*.json'))):
    s = os.path.basename(p)[:-5]
    d = json.load(open(p, encoding='utf-8'))
    when[s] = d.get('date', DEFAULT_DATE)
    if d.get('nonprefix'):  # sparse-audit rows without the abstract-only prefix; idempotent via the re-extraction marker in the note
        if 'Re-extracted ' + when[s] not in notes_now.get(s, ''):
            u2[s], e2[s], n2[s] = d['fields'], d['evidence_level'], d['pdf_note']
        continue
    if not state.get(s):
        continue
    upd[s], ev[s], note[s] = d['fields'], d['evidence_level'], d['pdf_note']


def run(u, e, n, label, strict):
    for dt in sorted({when[s] for s in u}):  # one apply() per stamp date, because the row stamp and the note text use L.DATE
        ids = {s for s in u if when[s] == dt}
        L.DATE = dt
        L.apply(label + ' ' + ', '.join(sorted(ids, key=lambda x: int(x[1:]))), {s: u[s] for s in ids}, {s: e[s] for s in ids}, {s: n[s] for s in ids}, strict=strict)
    L.DATE = DEFAULT_DATE


if upd:
    run(upd, ev, note, 're-extraction', True)
if u2:
    run(u2, e2, n2, 're-extraction (non-prefix)', False)
if not upd and not u2:
    print('nothing to apply')
