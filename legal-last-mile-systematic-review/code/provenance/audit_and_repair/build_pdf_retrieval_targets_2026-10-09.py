"""2026-10-09: a self-contained target list for a browser agent (Claude in Chrome) or a person to retrieve the missing full texts lawfully.
Snapshot of MISSING_FULLTEXTS_REQUEST_LIST_2026-10-04.csv (regenerated after the 2026-10-04 inbox batches) plus the hand-written context the list lacks:
journal, what the AI must be able to answer from the paper, and what earlier automated attempts met. Tier A = the 10 that change a decision or a rating; tier B = abstract-only
extractions (S079 is already in hand); tier C = stale 'no full text read' statuses on included studies. Writes 02_screening/full_text/PDF_RETRIEVAL_TARGETS_2026-10-09.csv.
Run from legal-last-mile-systematic-review/. Idempotent (it rewrites the file from the current list)."""
import csv, sys
csv.field_size_limit(sys.maxsize)
SRC = '02_screening/full_text/MISSING_FULLTEXTS_REQUEST_LIST_2026-10-04.csv'
OUT = '02_screening/full_text/PDF_RETRIEVAL_TARGETS_2026-10-09.csv'
FIELDS = ['order', 'tier', 'id', 'year', 'authors', 'title', 'venue', 'doi', 'doi_link', 'library_or_database_record', 'why_we_need_it', 'what_to_confirm_in_the_paper', 'earlier_attempts', 'file_name_to_use', 'outcome_to_record']
EARLIER_AUTOMATED = ('An earlier automated attempt from a cloud server failed (publisher 403 or Cloudflare checks, Crossref 429); a person\'s own browser, on a university network or login, '
                     'usually succeeds where that failed. The Drive copy, if any, is a web page saved with a .pdf name, not the article.')
A = {  # id -> (venue, why, confirm, earlier)
    'R803988411D3E': ('Routledge edited book (2013), chapters by several authors', 'Excluded at full-text stage (E12, edited volume) on the book record alone; a chapter may meet the inclusion criteria',
                      'The table of contents. For each chapter: is it an empirical study (case, survey, interviews, document analysis) of how rules, regulators, tenure, tariffs or other institutions shape access to sanitation or water in East Africa? Name any such chapter(s) and, if legitimately available, download those chapter PDFs. If none qualifies, record "no qualifying chapter".',
                      'Only a book record or preview was found. Chapter-level retrieval is still needed.'),
    'R155FFF508359': ('Geoforum 2015', 'Excluded E01 (wrong topic) on a landing page; a code of E07 (wrong service, irrigation) may fit better', 'Does the paper study drinking water or sanitation access, or only irrigation water? Is it empirical (interviews, fieldwork, documents)? Does an institution (rules, rights, water-user associations, law) shape access?', EARLIER_AUTOMATED),
    'RA1F6E143593E': ('Agriculture and Human Values 2016', 'Excluded E01 on a landing page; E07 (irrigation, not drinking water) may fit better', 'Same questions as the Geoforum paper: drinking water or irrigation? empirical? which institutions shape access?', EARLIER_AUTOMATED),
    'RF5C6D981DB3B': ('Regional Environmental Change (listed as 2023; the DOI suggests online in 2022)', 'Excluded E01 on a paywall preview', 'Does the study measure household water access or only water quality and land cover? Is governance or any institution (rule, regulator, programme) analysed as a factor? Empirical design and sample.', EARLIER_AUTOMATED),
    'RAB6AA06D8E9D': ('European Journal of Public Health, 2025 (abstract 286; ckaf180.144)', 'Excluded E09 (conference abstract) on the metadata record', 'Is there a separate full journal article by the same authors (climate change, water quality, socioeconomic impacts on vulnerable groups, Catalonia)? If only the abstract exists, record "abstract only" (that settles it).', 'DOI identifies a conference abstract; no separate full article found yet.'),
    'S264': ('Local Environment 2014', 'Included study that may fail criterion 3 (conceptual, no empirical design); the Drive copy is only a repository abstract page', 'Methods and data: is it empirical (case study, fieldwork, interviews, documents) or a conceptual argument? Sample or cases, years, place.', 'Repository record: UvA DARE (dare.uva.nl) and a Wageningen portal page; no full text obtained after publisher, repository and author searches.'),
    'S513': ('World Development 2015', 'Included study that may fail criterion 3 (conceptual); no Drive copy', 'Is it empirical (case studies, data) or a conceptual and policy argument about the right to sanitation? What evidence does it use?', 'No verified full text after publisher, repository and title/author searches.'),
    'S314': ('Habitat International 2015', 'Included study that may fail criterion 3 (conceptual); Drive copy is only a portal page', 'Methods and data for the Ghaziabad, Delhi case: fieldwork, interviews, documents? sample?', 'No verified full text obtained.'),
    'S340': ('Gender and Behaviour 23(2), 2025 (AJOL)', 'Included study that may fail criterion 3 (conceptual, feminist analysis); no Drive copy', 'Is there primary data (interviews, survey, fieldwork) or only a conceptual/literature argument? Sample and place.', 'AJOL lists the PDF as subscription-required; publisher 403 for the automated attempt.'),
    'S027': ('WIREs Water 2025', 'Included review whose AMSTAR 2 appraisal is still pending (the last of 23)', 'AMSTAR 2 items: protocol or registration; databases and dates searched; duplicate screening and extraction; a list of excluded studies; a risk-of-bias method; how quality shaped the conclusions; funding. Is it a systematic review or a narrative review?', 'Login or browser needed in the tracker; no copy obtained.'),
}
ORDER = ['R803988411D3E', 'R155FFF508359', 'RA1F6E143593E', 'RF5C6D981DB3B', 'RAB6AA06D8E9D', 'S264', 'S513', 'S314', 'S340', 'S027']
src = {(r['study_id'] or r['record_id']): r for r in csv.DictReader(open(SRC, encoding='utf-8'))}
rows = []
def row(i, tier, r, venue, why, confirm, earlier):
    return dict(order=len(rows) + 1, tier=tier, id=i, year=r['year'], authors=r['authors'][:140], title=r['title'], venue=venue, doi=r['doi'], doi_link=r['doi_link'],
                library_or_database_record=r['other_link'], why_we_need_it=why, what_to_confirm_in_the_paper=confirm, earlier_attempts=earlier, file_name_to_use=r['file_name_to_use'], outcome_to_record='')
for i in ORDER:
    r = src[i]; v, why, conf, earl = A[i]
    rows.append(row(i, 'A', r, v, why, conf, earl))
for k, r in sorted(src.items(), key=lambda kv: (kv[1]['year'], kv[0])):
    if r['priority'] == '5' and k != 'S079':   # S079 is already in hand (its Drive copy was read)
        rows.append(row(k, 'B', r, '', 'Extracted from the abstract or record only; the full text would give the sample, methods and findings', 'Sample size, design, place and years, the main findings, and what legal or administrative institution is studied.', 'Not obtained; see the retrieval tracker.'))
for k, r in sorted(src.items(), key=lambda kv: (kv[1]['year'], kv[0])):
    if r['priority'] == '6':
        rows.append(row(k, 'C', r, '', 'Included/decided but the recorded full-text status says no full text was read (probably a stale status)', 'Only a quick check that the paper matches the extraction (design, sample, country). Lowest priority.', 'Not obtained.'))
with open(OUT, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator='\r\n'); w.writeheader(); w.writerows(rows)
from collections import Counter
print('wrote', OUT, dict(Counter(r['tier'] for r in rows)))
