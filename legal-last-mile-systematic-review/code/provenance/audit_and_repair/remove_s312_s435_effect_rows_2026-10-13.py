"""2026-10-13: remove the effect_sizes.csv rows (and their FULLTEXT_VERIFICATION rows) of S312 (Warner, Zhang & Gonzalez Rivas 2020) and S435 (Allaire & Ignacio 2026) before the two studies
are retired by the PI's A24 rulings of 2026-10-13 (exclude E04 on criterion 4, as for S397: the dependent variable is jurisdiction- or utility-level policy adoption, not a household access outcome).
resolve_a16_pending_reversals.py refuses to retire a study that still has an effect-size row, so the rows are taken out first; both were reasoned non-fits (no family, not pooled), so no
synthesis changes. The removed rows are kept verbatim in 11_archive/effect_sizes_removed_2026-10-13.csv (effect rows) and 11_archive/fulltext_verification_removed_2026-10-13.csv.
Idempotent. Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
IDS = ('S312', 'S435')
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
        ar = [r for r in ar if r['study_id'] not in IDS] + out
        write(arch, af, ar, ae)
    else:
        write(arch, fields, out, eol)
    write(src, fields, keep, eol)
    print(f'{src}: removed {[r["study_id"] for r in out]} ({len(rows)} -> {len(keep)} rows); archived to {arch}')
