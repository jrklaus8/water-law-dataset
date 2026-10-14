"""2026-10-14 (PI ruling on open item A2, reviewer CK): the 73 decided full-text rows with a blank `reviewer_1` get the label `Claude-AI-fulltext-2026-09-16`, with a dated provenance note.
Evidence for the label: 26 of the 27 excludes carry that reviewer in the exclusion log, and the extraction records of the 46 includes (and their later re-extractions) trace back to
`Claude-AI-extraction-2026-09-16`; the one remaining row, R64A7E6073EF0 (S397, whose exclusion-log entry the PI's own A16 ruling overwrote with CK), is labelled with the batch as the PI directed.
The label is inferred, not recorded at the time, and it is not human review: human second-review tracking stays under open item A6. No decision, code or other field changes.
Idempotent. Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
P = '02_screening/full_text/full_text_screening_database.csv'
LABEL = 'Claude-AI-fulltext-2026-09-16'
NOTE = 'reviewer_1 label inferred from 2026-09-16 exclusion log and extraction record'
MARK = 'reviewer_1 label inferred'
raw = open(P, newline='', encoding='utf-8').read(); eol = '\r\n' if '\r\n' in raw[:5000] else '\n'
with open(P, newline='', encoding='utf-8') as f:
    rd = csv.DictReader(f); fields = rd.fieldnames; rows = list(rd)
todo = [r for r in rows if r['final_decision'] in ('include', 'exclude') and not r['reviewer_1']]
done = [r for r in rows if MARK in r['notes']]
assert len(todo) + len(done) == 73, (len(todo), len(done))
for r in todo:
    r['reviewer_1'] = LABEL
    r['notes'] = (r['notes'] + ' | ' if r['notes'] else '') + f"[{NOTE}; A2 ruling 2026-10-14 by CK; human second review is tracked under open item A6]"
if todo:
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(P), suffix='.tmp')
    with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator=eol); w.writeheader(); w.writerows(rows)
    os.replace(tmp, P)
print(len(todo), 'rows labelled;', len(done), 'already done')
