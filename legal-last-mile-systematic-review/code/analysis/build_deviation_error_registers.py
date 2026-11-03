#!/usr/bin/env python3
"""Readable view of the deviations register and the errors-found register.

Both registers are hand-maintained CSV files in 00_admin/ (DEVIATIONS_REGISTER.csv: every departure from the protocol, dated, with whether it was decided after results were visible;
ERRORS_FOUND_REGISTER.csv: every error the project found in itself, how it was found, its effect and its fix). This script renders them to 00_admin/DEVIATIONS_AND_ERRORS.md and keeps the view in
step with the CSVs; code/tests/test_registers.py checks the CSVs (dates, allowed values, cited files exist).

Run from legal-last-mile-systematic-review/:  python3 code/analysis/build_deviation_error_registers.py
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEV = ROOT / '00_admin/DEVIATIONS_REGISTER.csv'
ERR = ROOT / '00_admin/ERRORS_FOUND_REGISTER.csv'
OUT = ROOT / '00_admin/DEVIATIONS_AND_ERRORS.md'


def read(p):
    with open(p, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def cell(v):
    return v.replace('|', '/').replace('\n', ' ')


def render():
    dev, err = read(DEV), read(ERR)
    after = sum(r['decided_after_seeing_results'] == 'yes' for r in dev)
    partly = sum(r['decided_after_seeing_results'] == 'partly' for r in dev)
    open_err = [r for r in err if r['status'] in ('open',) or r['status'].startswith('fixed on a branch')]
    md = ['# Deviations from the protocol, and errors the project found in itself', '',
          '*Rendered by `code/analysis/build_deviation_error_registers.py` from `DEVIATIONS_REGISTER.csv` and `ERRORS_FOUND_REGISTER.csv`, which are the data (edit those, not this page). The AI drafted both from the repository\'s own records (the registration draft, the 2026-09-28 audit, the changelog and the decisions log); the researcher has not yet confirmed every entry.*', '',
          '## Departures from the protocol', '',
          f'{len(dev)} dated departures, clarifications and added checks. **{after} were decided after the results they could affect were visible and {partly} partly so** (column "after seeing results"): those are the ones to look at hardest, because eligibility or grouping decisions made with the effect rows in view can shift a result even when made in good faith. '
          'The protocol itself was fixed in writing on 2026-08-22 (commit `d591062`), before any database was searched; the research question, the eligibility wording, the codebook fields and the synthesis decision tree were not rewritten.', '',
          '| ID | Date | Stage | Departure | Kind | After seeing results | Effect on the evidence base |', '|---|---|---|---|---|---|---|']
    md += [f"| {r['id']} | {r['date_recorded']} | {cell(r['stage'])} | {cell(r['deviation'])} | {cell(r['kind'])} | {r['decided_after_seeing_results']} | {cell(r['effect_on_evidence_base'])} |" for r in dev]
    md += ['', 'The plan, what was done, the recorded reason, who decided and where it is documented are in `DEVIATIONS_REGISTER.csv`. "After seeing results" is the AI\'s reading of the dated records.', '',
           '## Errors the project found in itself', '',
           f'{len(err)} errors, by how they were found. Most were found by the project\'s own audits and corrected in the open; **{len(open_err)} are still open or only fixed on an unmerged branch**. The register is a measure of how much checking was done, not a claim that these are all the errors: assume more exist.', '',
           '| ID | Found | How | Stage | Error | Introduced by | Effect | Status |', '|---|---|---|---|---|---|---|---|']
    md += [f"| {r['id']} | {r['date_found']} | {cell(r['found_by'])} | {cell(r['stage'])} | {cell(r['error'])} | {cell(r['introduced_by'])} | {cell(r['effect_on_findings'])} | {cell(r['status'])} |" for r in err]
    md += ['', 'The fix and where each is documented are in `ERRORS_FOUND_REGISTER.csv`.', '',
           '## Reading these together with the other registers', '',
           '- Weaknesses that remain (and how to test them): `WEAKNESSES.md`.', '- What the AI did and what is not archived: `AI_USE_LEDGER.md`.', '- What a human has checked for each study: `STUDY_AUDIT_TRAIL.csv`.', '']
    return '\n'.join(md)


def main():
    OUT.write_text(render(), encoding='utf-8')
    print(f'wrote {OUT.name}')


if __name__ == '__main__':
    main()
