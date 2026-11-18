"""2026-10-04: do the AMSTAR 2 systematic reviews share primary studies with the rest of the corpus (the double-counting risk the preliminary report flagged as unchecked)?

What it does: for every AMSTAR 2 review whose full-text PDF is on this machine (7 of 23: S052, S319, S324, S325, S327, S344, S418; S697 and S438 were read through Drive and are not
local), it extracts the reference list with pypdf and matches it against the 1,159 included studies by DOI and by normalised title. A hit means "this corpus study is CITED anywhere in the review's
reference list" -- an UPPER BOUND on the primary studies the review actually pooled (background citations count too). It does not read the included-studies tables or appendices.
Reproducibility: the PDFs are not committed and the paths below are local to the 2026-10-04 session, so this script documents the method and regenerates the CSV only where the PDFs exist.
The output is not re-derived by verify_repository.py. Run from legal-last-mile-systematic-review/. Nothing in any database is changed."""
import csv, glob, re, sys
from collections import defaultdict
from pathlib import Path
sys.path.insert(0, 'code/analysis')
import current_figures as cf  # noqa: E402
import pypdf  # noqa: E402

UP = '/root/.claude/uploads/13a4d716-bf67-5f8e-b123-127698a45259/'
PDFS = {'S052': '0d8cfe19-fenvs-11-1097716_1.pdf', 'S319': '25b72693-ksppe-2025-28-5-581.pdf', 'S324': '62958fc7-journal.pone.0270847.pdf', 'S325': 'f19c157e-11768326012_visor_jats.pdf',
        'S327': '5d663b44-journal.pgph.0001720_1.pdf', 'S344': '9367d809-shsconf_iccb2026_01001.pdf', 'S418': '57acc13c-PIIS2214109X23000062.pdf'}
OUT_CSV = Path('05_analysis/descriptive/amstar2_overlap_check_2026-10-04.csv')
OUT_MD = Path('05_analysis/descriptive/AMSTAR2_OVERLAP_CHECK_2026-10-04.md')
norm = lambda t: re.sub(r'[^a-z0-9]', '', t.lower())
DOI = re.compile(r'10\.\d{4,9}/[^\s"<>]+', re.I)


def refs_of(path):
    r = pypdf.PdfReader(path)
    full = '\n'.join(p.extract_text() or '' for p in r.pages)
    heads = [m.start() for m in re.finditer(r'\n\s*(references?|bibliography|referencias|literature cited)\s*\n', full, re.I)]
    cut = heads[-1] if heads else int(len(full) * 0.7)
    return full[cut:], bool(heads)


ed = {r['study_id']: r for r in cf.read('ed')}
ft = {r['record_id']: r for r in cf.read('ft')}
am = {s for s, r in ed.items() if cf.tool_of(r['risk_of_bias_tool']) == 'AMSTAR 2'}
corpus = {}
for s, r in ed.items():
    f = ft[r['record_id']]
    title = re.split(r'\s*[\[;]\s*', f['title'])[0]
    corpus[s] = {'title_n': norm(title), 'doi': (f['doi'] or r['doi']).lower().strip(), 'short': f['title'][:90], 'is_review': s in am, 'year': f['year']}
rows, cited = [], defaultdict(set)
for s, fn in PDFS.items():
    refs, found = refs_of(UP + fn)
    rn = norm(refs)
    dois = {d.lower().rstrip('.,;)') for d in DOI.findall(refs)}
    hits = {}
    for c, d in corpus.items():
        if c == s:
            continue
        by_doi = bool(d['doi']) and any(d['doi'] in x or x in d['doi'] for x in dois if len(x) > 12)
        by_title = len(d['title_n']) >= 40 and d['title_n'] in rn
        if by_doi or by_title:
            hits[c] = 'doi' if by_doi else 'title'
            cited[c].add(s)
    n_refs = max(len(dois), len(re.findall(r'\n\s*\[?\d{1,3}[\].)]\s', refs)))
    rows.append({'review': s, 'rating': ed[s]['risk_of_bias_rating'].split(' (')[0], 'reference_section_found': found, 'approx_references': n_refs, 'dois_in_reference_list': len(dois),
                 'corpus_studies_cited': len(hits), 'cited_corpus_reviews': ';'.join(sorted(c for c in hits if corpus[c]['is_review'])), 'cited_corpus_study_ids': ';'.join(sorted(hits, key=lambda x: int(x[1:])))})
with open(OUT_CSV, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator='\r\n'); w.writeheader(); w.writerows(rows)
shared = {c: v for c, v in cited.items() if len(v) >= 2}
L = ["# AMSTAR 2 reviews: do they share primary studies with the corpus? (2026-10-04)", "",
     "*Produced by `code/provenance/audit_and_repair/check_amstar2_overlap_2026-10-04.py`. Read-only; changes no database. A hit means a corpus study is **cited anywhere** in a review's reference list (DOI or exact-title match), "
     "so it is an **upper bound** on the primary studies the review pooled (background citations count). Only 7 of the 23 AMSTAR 2 reviews could be checked (their PDFs were on this machine); the other 16 — including S697 and S438, "
     "which were read through Drive — are **unchecked**. Matching is by DOI or a title of at least 40 normalised characters, so it misses references with different wording or no DOI.*", "",
     "| Review | Rating | Reference section found | DOIs in reference list | Corpus studies cited | Corpus AMSTAR 2 reviews cited |", "|---|---|---|---|---|---|"]
for r in rows:
    L.append(f"| {r['review']} | {r['rating']} | {'yes' if r['reference_section_found'] else 'no (last 30% used)'} | {r['dois_in_reference_list']} | {r['corpus_studies_cited']} | {r['cited_corpus_reviews'] or '—'} |")
L += ["", "## Corpus studies cited by two or more of the checked reviews", ""]
if shared:
    L += ["| Corpus study | Cited by | Title |", "|---|---|---|"]
    for c, v in sorted(shared.items(), key=lambda x: int(x[0][1:])):
        L.append(f"| {c} | {', '.join(sorted(v))} | {corpus[c]['short']} |")
else:
    L.append("None found: no corpus study appears in the reference lists of two of the seven checked reviews.")
L += ["", "## What this does and does not show", "",
      f"- Across the 7 checked reviews, **{len(cited)} distinct corpus studies** are cited at least once and **{len(shared)}** by two or more. Most hits, if any, are background citations rather than pooled primary studies.",
      "- A review citing another corpus review is a different risk: that review's findings may already be counted through its own extraction. Column 6 lists those.",
      "- The question the report asks — *would the same primary study be counted once as its own row and again inside a review?* — can only be settled from each review's included-studies list (appendix or table), which this check did not read.",
      "- Nothing was changed: reviews stay secondary evidence and are never pooled as independent primary effects (RISK_OF_BIAS.md §1).", ""]
OUT_MD.write_text('\n'.join(L), encoding='utf-8')
print(OUT_CSV, [(r['review'], r['reference_section_found'], r['dois_in_reference_list'], r['corpus_studies_cited']) for r in rows], 'shared', len(shared))
