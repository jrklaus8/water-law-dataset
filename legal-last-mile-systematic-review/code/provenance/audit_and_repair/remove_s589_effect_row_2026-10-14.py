"""2026-10-14: remove the effect_sizes.csv row (and its FULLTEXT_VERIFICATION row) of S589 (World Bank / IDB 2004, Machala, Ecuador; Family A) on the PI's ruling that closes open item A1.
The row records an unadjusted, descriptive city-level comparison of connected and unconnected households (Box 3.2 of a policy report: no sample size, interval or test), and evidence_map.csv does
not flag S589 quantitative_synthesis_eligible, so the row failed effect_sizes.csv's own inclusion standard; it was the only row of a study not flagged eligible. The study itself stays in the
review (it is a full-text include with an extraction row and a Legal Institutional Evidence Appraisal Framework rating); only its quantitative row goes. The Family A SWiM synthesis is recomputed at k = 18
(06_outputs/supplementary/family_A_swim_synthesis_2026-09-28.md). The removed rows are appended verbatim to 11_archive/effect_sizes_removed_2026-10-13.csv and
11_archive/fulltext_verification_removed_2026-10-13.csv, which already hold the rows of S312, S435, S348 and S969. Idempotent. Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
IDS = ('S589',)
JOBS = (('05_analysis/effect_sizes/effect_sizes.csv', '11_archive/effect_sizes_removed_2026-10-13.csv'),
        ('05_analysis/effect_sizes/FULLTEXT_VERIFICATION_2026-10-04.csv', '11_archive/fulltext_verification_removed_2026-10-13.csv'))


def read(p):
    raw = open(p, newline='', encoding='utf-8').read()
    with open(p, newline='', encoding='utf-8') as f:
        rd = csv.DictReader(f)
        return rd.fieldnames, list(rd), '\r\n' if '\r\n' in raw[:5000] else '\n'


def write(p, fields, rows, eol):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(p) or '.', suffix='.tmp')
    with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator=eol)
        w.writeheader()
        w.writerows(rows)
    os.replace(tmp, p)


os.makedirs('11_archive', exist_ok=True)
for src, arch in JOBS:
    fields, rows, eol = read(src)
    out = [r for r in rows if r['study_id'] in IDS]
    if not out:
        print(f'{src}: nothing to remove')
        continue
    assert len(out) == len(IDS), (src, [r['study_id'] for r in out])
    keep = [r for r in rows if r['study_id'] not in IDS]
    if os.path.exists(arch):
        af, ar, ae = read(arch)
        assert af == fields
        ar = [r for r in ar if r['study_id'] not in IDS] + out  # keeps the 2026-10-13 rows, adds these
        write(arch, af, ar, ae)
    else:
        write(arch, fields, out, eol)
    write(src, fields, keep, eol)
    print(f'{src}: removed {[r["study_id"] for r in out]} ({len(rows)} -> {len(keep)} rows); archived to {arch}')
