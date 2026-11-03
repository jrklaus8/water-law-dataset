"""2026-10-14: remove the effect_sizes.csv rows (and their FULLTEXT_VERIFICATION rows) of S348 (Andrews, Beynon & Baafi 2025; Family C) and S969 (Njoh & Akiwumi 2011; Family A) before the two studies
are retired by the PI's A24 rulings of 2026-10-14 (exclude E03: the institutional context is background only and no legal or administrative rule is tested).
resolve_a16_pending_reversals.py refuses to retire a study that still has an effect-size row, so the rows are taken out first. UNLIKE the 2026-10-13 removal of S312 and S435 these two rows carried a family,
so the Family A and Family C SWiM syntheses change (k 20 to 19 each; see 06_outputs/supplementary/family_A_swim_synthesis_2026-09-28.md and family_C_swim_synthesis_2026-09-28.md). The removed rows are appended verbatim to
11_archive/effect_sizes_removed_2026-10-13.csv (effect rows) and 11_archive/fulltext_verification_removed_2026-10-13.csv, which keep the 2026-10-13 rows of S312 and S435.
Idempotent. Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
IDS = ('S348', 'S969')
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
