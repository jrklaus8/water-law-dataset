"""2026-10-04: refresh stale wording in the narrative `evidence_level` column of evidence_map.csv. 515 of 1,159 rows still said the study's risk-of-bias rating was "deferred pending official
application of <instrument>" (wording from the 2026-09 Phase 11 map), although every instrument was applied afterwards (batch appraisals 2026-09-16 to 2026-09-28; full-text appraisals since). The ratings live
in extraction_database.csv `risk_of_bias_rating`, which is unchanged.
  Pattern 1 (431 rows, the standard sentence): replaced by "risk-of-bias appraisal (<instrument>) is recorded in extraction_database.csv risk_of_bias_rating for <id>; the earlier 'deferred' wording was superseded
    (refreshed 2026-10-04)".
  Other rows that say "deferred" (84, free-text variants that also carry the AI's provisional-confidence reasoning): original text kept, and a one-line note appended saying the deferral wording is superseded.
No other column, row or value changes; idempotent. Run from legal-last-mile-systematic-review/."""
import csv, os, re, sys, tempfile
csv.field_size_limit(sys.maxsize)
EM = '05_analysis/descriptive/evidence_map.csv'
PAT = re.compile(r'risk-of-bias rating deferred pending official application of (?:the |a )?([^(]+?) \(see RISK_OF_BIAS\.md and extraction_database\.csv risk_of_bias_tool/risk_of_bias_rating for (S\d+)\)')
NOTE = " [2026-10-04: any 'rating deferred' wording above is superseded; the current appraisal is in extraction_database.csv risk_of_bias_rating.]"
raw = open(EM, newline='', encoding='utf-8').read(); crlf = '\r\n' in raw[:5000]
with open(EM, newline='', encoding='utf-8') as f:
    rd = csv.DictReader(f); fields = rd.fieldnames; rows = list(rd)
n1 = n2 = 0
for r in rows:
    e = r['evidence_level']
    if 'deferred' not in e:
        continue
    m = PAT.search(e)
    if m:
        r['evidence_level'] = PAT.sub(lambda m: f"risk-of-bias appraisal ({m.group(1)}) is recorded in extraction_database.csv risk_of_bias_rating for {m.group(2)}; the earlier 'deferred' wording was superseded (refreshed 2026-10-04)", e)
        n1 += 1
    elif not e.endswith(NOTE):
        r['evidence_level'] = e + NOTE
        n2 += 1
fd, tmp = tempfile.mkstemp(dir=os.path.dirname(EM), suffix='.tmp')
with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator='\r\n' if crlf else '\n'); w.writeheader(); w.writerows(rows)
os.replace(tmp, EM)
print('pattern-1 rows replaced', n1, '| other rows annotated', n2)
