#!/usr/bin/env python3
"""Fill the 'key figures' block of START_HERE.md from the databases.

START_HERE.md is the one-page entry point for supervisors, auditors and future researchers. Its prose is hand-written and carries no numbers;
the figures live in a table between two marker comments and are rewritten here from `current_figures.py` and the PRISMA flow that the atlas
generator already computes, so they cannot go stale (the 2026-09-28 audit found hand-typed figures drifting across documents).
`verify_repository.py` and `code/tests/test_reader_guides.py` fail if the block differs from what this script produces.

Run from legal-last-mile-systematic-review/:  python3 code/analysis/build_start_here.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import current_figures as cf  # noqa: E402
import build_evidence_atlas as bea  # noqa: E402

TARGET = Path('START_HERE.md')
BEGIN = '<!-- BEGIN GENERATED: key figures (code/analysis/build_start_here.py) -->'
END = '<!-- END GENERATED: key figures -->'


def block():
    F = cf.compute()
    flow = {x['k']: x['n'] for x in bea.gather()['flow']}
    share = F['human_verified_rows'] / F['full_text_decided'] * 100
    rows = [
        ('Records found in the database searches', f"{flow['identified']:,}", 'Searches ran 2026-08-25 to 2026-09-11 and were closed by decision; SSRN and Westlaw/Lexis were never searched'),
        ('After removing duplicates', f"{flow['unique']:,}", ''),
        ('Passed title and abstract screening to the full-text stage', f"{F['full_text_records']:,}", 'The AI screened every abstract; a human second pass covered only the include-or-unsure records'),
        ('Full texts actually assessed', f"{F['full_text_decided']:,}", f"{F['full_text_undecided']:,} candidates were never assessed ({F['unretrieved_not_retrievable']:,} could not be retrieved, {F['unretrieved_wrong_file']:,} were the wrong file)"),
        ('**Included studies**', f"**{F['full_text_include']:,}**", f"{F['full_text_exclude']:,} full texts were excluded, each with a coded reason"),
        ('Full-text decisions a human checked or ruled on', f"{F['human_verified_rows']:,} of {F['full_text_decided']:,} ({share:.1f}%)", f"{F['reviewer_2_confirmed_includes']} includes confirmed by a human second reviewer; {F['human_adjudicated_rows']} further decisions ruled on by the principal investigator"),
        ('Studies with extracted data and a risk-of-bias rating', f"{F['extraction_rows']:,}", 'Extraction and ratings were made by the AI; no second extractor and no human re-appraisal yet'),
        ('Studies in the three structured (SWiM) syntheses', f"{F['swim_core_studies']}", f"{F['swim_core_inclusion_human_verified']} have a human-verified inclusion decision, {F['swim_core_ai_checked_not_human']} are AI-checked only; the author has confirmed the direction coding of {F['swim_core_direction_ck_confirmed']}"),
        ('Effect sizes pooled into a meta-analysis', f"{F['effect_size_rows_pooled']}", f"No family met the bar for pooling; {F['effect_size_rows']} effect-size rows are reported by direction of association only"),
    ]
    out = [BEGIN, '', '| Stage | Figure | What to know |', '|---|---|---|']
    out += [f'| {a} | {b} | {c} |' for a, b, c in rows]
    out += ['', 'These figures are rewritten from the databases by `code/analysis/build_start_here.py`; the full list is in `00_admin/CURRENT_FIGURES.md`.', '', END]
    return '\n'.join(out)


def render(text):
    i, j = text.index(BEGIN), text.index(END) + len(END)
    return text[:i] + block() + text[j:]


def main():
    text = TARGET.read_text(encoding='utf-8')
    new = render(text)
    if new != text:
        TARGET.write_text(new, encoding='utf-8')
    print(f'wrote {TARGET} (key figures block {"updated" if new != text else "already current"})')


if __name__ == '__main__':
    main()
