"""Regenerate CAMPAIGN_NOTES.md from the study JSONs in this directory (run from legal-last-mile-systematic-review/)."""
import csv, glob, json, os, sys
csv.field_size_limit(sys.maxsize)
HERE = os.path.dirname(os.path.abspath(__file__))
ed = {r['study_id']: r for r in csv.DictReader(open('03_extraction/extracted_data/extraction_database.csv'))}
L = ["# Full-text re-extraction campaign — notes (2026-10-04)", "",
     "Rows whose full texts turned out to be in the researcher's Drive were re-extracted from the full text by the AI (one JSON per study in this directory; applied by `../run_reextract_2026-10-04.py`, which rewrites only the fields in the JSON). Nothing here has been human-checked.", "",
     "**What was and was not done.** Fields were re-extracted; flags were not removed; `effect_sizes.csv` and the evidence_map quantitative flag were not changed (one exception: S174's existing Family C row was updated with n and coefficients, see CHANGELOG); where the full text shows the appraisal tool does not fit the design, the old rating was **left in place** and flagged below for the reclassification step (a researcher decision). Many Drive files labelled 'retrieved' were repository landing pages or paywall previews and could not be extracted on 2026-10-04 (S268, S285, S280, S310, S311, S284, S286, S308, S315, S250, S256, S264, S271, S291, S303, S317, S301, S270, S273, S186, S210, S214, S329 and others). Several of these were later replaced by real PDFs and re-extracted (S285, S270, S273, S291, S303, S308, S311, S268, S214, S210, S250 and S286 on 2026-10-04; S271, S304, S310, S315, S352 and the rows S395, S415, S416, S417 on 2026-10-09, whose JSONs carry a `date` entry of 2026-10-09); the rest stay at abstract level.", "",
     "Two groups: **(A) abstract-only rows** (note prefix 'Extracted from published abstract', removed from the abstract-only list when applied) and **(B) sparse-audit rows** (`nonprefix: true`; flagged by `code/analysis/audit_sparse_records.py`, not on the abstract-only list).", ""]
for title, flag in (("A. Abstract-only rows", False), ("B. Sparse-audit rows", True)):
    rows = []
    for f in sorted(glob.glob(os.path.join(HERE, 'S*.json')), key=lambda x: int(os.path.basename(x)[1:-5])):
        d = json.load(open(f, encoding='utf-8'))
        if bool(d.get('nonprefix')) != flag:
            continue
        s = os.path.basename(f)[:-5]; r = ed[s]
        rows.append(f"| {s} | {r['risk_of_bias_tool'][:22]} | {d['fields'].get('study_design', '')[:110]} | {d.get('notes', '')} |".replace('\n', ' '))
    L += [f"## {title} ({len(rows)})", "", "| Study | Tool now | Design as found | Note |", "|---|---|---|---|"] + rows + [""]
L.append("Files still at abstract level (landing page or paywall preview, or no Drive file) need the real PDFs from the researcher: see `03_extraction/extracted_data/abstract_only_fulltext_request_list_2026-09-29.csv` and `05_analysis/descriptive/SPARSE_RECORD_AUDIT_2026-10-04.md`.")
open(os.path.join(HERE, 'CAMPAIGN_NOTES.md'), 'w').write('\n'.join(L) + '\n')
print('wrote CAMPAIGN_NOTES.md')
