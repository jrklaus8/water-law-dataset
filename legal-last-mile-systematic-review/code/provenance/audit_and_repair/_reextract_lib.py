"""Shared helper for the 2026-10-04 full-text re-extraction campaign (abstract-only rows whose PDFs turned out to be in the researcher's Drive).
apply(batch_name, updates, evidence_levels) rewrites extraction_database.csv rows (asserting each still carries the abstract-only note prefix), the
evidence_map `evidence_level` text, and removes the studies from the abstract-only sensitivity CSV. Atomic writes, row-count asserts, line endings kept.
Derived files (request list, audits, report) are regenerated afterwards by the build scripts. Run from legal-last-mile-systematic-review/."""
import csv, os, sys, tempfile
csv.field_size_limit(sys.maxsize)
ED = '03_extraction/extracted_data/extraction_database.csv'
EM = '05_analysis/descriptive/evidence_map.csv'
AB = '05_analysis/sensitivity/abstract_only_extractions_2026-09-28.csv'
PREFIX = ('Extracted from published abstract', 'Extracted from abstract')
DATE = '2026-10-04'


def _rw(path, fn):
    raw = open(path, newline='').read(); crlf = '\r\n' in raw[:5000]
    with open(path, newline='') as f:
        rd = csv.DictReader(f); fields = rd.fieldnames; rows = list(rd)
    n = len(rows); rows = fn(rows)
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), suffix='.tmp')
    with os.fdopen(fd, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator='\r\n' if crlf else '\n'); w.writeheader(); w.writerows(rows)
    os.replace(tmp, path)
    return n, len(rows)


def apply(batch, updates, evidence_levels, pdf_note):
    """updates: {study_id: {field: value}}; pdf_note: {study_id: short description of the PDF read (pages, language, what was not read)}."""
    ids = set(updates)

    def m_ed(rows):
        seen = set()
        for r in rows:
            s = r['study_id']
            if s not in ids:
                continue
            assert r['extraction_note'].startswith(PREFIX), (s, r['extraction_note'][:60])
            for k, v in updates[s].items():
                assert k in r, (s, k)
                r[k] = v
            r['researcher'] = f'Claude-AI-extraction-{DATE} (re-extraction; original {r["researcher"]})'
            r['date_extracted'] = DATE
            rated = ('Rating re-answered on the full text (item-level, in risk_of_bias_rating). ' if 'risk_of_bias_rating' in updates[s] else
                     'The old risk_of_bias_rating was NOT re-answered here because the full text shows the appraisal tool does not fit the design (see CAMPAIGN_NOTES.md); it is left for the reclassification step. ')
            r['extraction_note'] = (f'Re-extracted {DATE} from the full-text PDF in the researcher\'s Drive ({pdf_note[s]}); supersedes the abstract-only extraction. '
                                    f'{rated}Flags not removed; flags added only where the text supports them. effect_sizes.csv and the evidence_map '
                                    f'quantitative flag were NOT changed (see DECISIONS_AND_OPEN_ITEMS.md). record_id {r["record_id"]}.')
            seen.add(s)
        assert seen == ids, ids - seen
        return rows
    _rw(ED, m_ed)

    def m_em(rows):
        for r in rows:
            if r['study_id'] in evidence_levels:
                r['evidence_level'] = evidence_levels[r['study_id']]
        return rows
    _rw(EM, m_em)
    n0, n1 = _rw(AB, lambda rows: [x for x in rows if x['study_id'] not in ids])
    assert n0 - n1 == len(ids), (n0, n1)
    print(f'{batch}: {len(ids)} studies re-extracted; abstract-only set {n0} -> {n1}')
