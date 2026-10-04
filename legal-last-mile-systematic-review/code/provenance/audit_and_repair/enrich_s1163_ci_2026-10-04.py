"""2026-10-04: S1163 (Cronk, Guo, Fleming & Bartram 2021, Sci Total Environ 761:144226) effect-size row. The adjusted odds ratio for 'external organization has sponsored/implemented a WASH program in the past year'
was recorded as 1.4 with the confidence interval blank. The researcher's full text (Drive) gives it in the adjusted-model table as OR 1.4 (95% CI 1.1, 1.7), p = 0.021 (Wald 0.0207), so the interval is filled.
NOT changed, but noted in provenance_note: the recorded sample '2,677 schools, 13 countries' cannot be found in the text, which reports 2,690 schools surveyed, 2,722 contacted, '14 countries' in the title and
methods and '13 countries' in a map caption; the analytic n of the adjusted model was not located. Idempotent. Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
P = '05_analysis/effect_sizes/effect_sizes.csv'
raw = open(P, newline='').read(); crlf = '\r\n' in raw[:5000]
with open(P, newline='') as f:
    rd = csv.DictReader(f); fields = rd.fieldnames; rows = list(rd)
n0 = len(rows); done = False; changed = False
for r in rows:
    if r['study_id'] != 'S1163':
        continue
    if 'Full-text check 2026-10-04' in r['provenance_note']:
        print('already applied'); done = True; continue
    assert r['effect_estimate'] == '1.4' and r['lower_CI'] == '' and r['upper_CI'] == ''
    r['lower_CI'], r['upper_CI'] = '1.1', '1.7'
    r['provenance_note'] += (' Full-text check 2026-10-04: adjusted OR 1.4 (95% CI 1.1, 1.7), p = 0.021 confirmed in the adjusted-model table; CI filled from it. The recorded sample (2,677 schools, 13 countries) was not found in the text, '
                             'which reports 2,690 schools surveyed and 2,722 contacted, 14 countries in the title/methods and 13 in a map caption; the analytic n of the adjusted model was not located.')
    done = True; changed = True
assert done and len(rows) == n0
fd, tmp = tempfile.mkstemp(dir=os.path.dirname(P), suffix='.tmp')
with os.fdopen(fd, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator='\r\n' if crlf else '\n'); w.writeheader(); w.writerows(rows)
os.replace(tmp, P)
if changed:
    print('S1163 CI filled: 1.1 - 1.7')
