"""2026-10-04: normalise the case of the `conflict` column in 02_screening/full_text/full_text_screening_database.csv. The column held 'FALSE' (200 rows), 'false' (83)
and 'true' (38) side by side; the data dictionary and the import scripts define it as true/false/blank in lower case, and every reader already compares case-insensitively.
Only the 200 'FALSE' cells change (to 'false'); no other cell, row or line ending changes. The title/abstract database uses 'FALSE' uniformly (3,665 rows) and is left as it is
(a uniform legacy spelling, not a mixed one). Idempotent. Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
P = '02_screening/full_text/full_text_screening_database.csv'
raw = open(P, 'rb').read().decode('utf-8'); crlf = raw.split('\n', 1)[0].endswith('\r')
with open(P, encoding='utf-8', newline='') as f:
    rd = csv.DictReader(f); fields = rd.fieldnames; rows = list(rd)
n0 = len(rows)
todo = [r for r in rows if r['conflict'] == 'FALSE']
assert all(r['conflict'] in ('', 'true', 'false', 'FALSE') for r in rows), 'unexpected conflict value'
for r in todo:
    r['conflict'] = 'false'
assert len(rows) == n0
if not todo:
    print('already normalised'); sys.exit(0)
fd, tmp = tempfile.mkstemp(dir=os.path.dirname(P), suffix='.tmp')
with os.fdopen(fd, 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator='\r\n' if crlf else '\n'); w.writeheader(); w.writerows(rows)
os.replace(tmp, P)
print(f'{len(todo)} conflict cells normalised FALSE -> false')
