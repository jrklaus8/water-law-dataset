"""
nl_outcome_coding.py
====================
Closes the dataset's single most-cited limitation (see "Known Limitations" in
README.md and Priority 1 in FUTURE_WORK.md): the 68,654 Netherlands decisions
carry dispute-type coding but no outcome variable, so the dataset can show
*what* is litigated but not *who prevails*.

Pipeline (mirrors the FUTURE_WORK.md Priority 1 walkthrough, consolidated into
one runnable script):
  1. Retrieve full decision XML for every NL ECLI via the rechtspraak.nl Open
     Data content API (no auth; ~10 req/s documented limit) — same endpoint
     and request pattern as scrapers/netherlands/rechtspraak_scraper.py
  2. Extract the "Beslissing" (operative-conclusion) section from the XML
  3. Classify WIN / LOSS / PARTIAL / INADMISSIBLE / REMAND / UNCLASSIFIED via
     regex (resolves ~85-90% per the validated 200-case manual sample in
     FUTURE_WORK.md)
  4. Pass UNCLASSIFIED residue through an LLM fallback (push accuracy from
     ~87% to ~96%)
  5. Merge the resulting `outcome` column back into water_law_global_coded.csv

Usage:
  export DATA_DIR=./data
  export ANTHROPIC_API_KEY=...      # only required for the LLM fallback pass
  python utils/nl_outcome_coding.py [--skip-llm] [--limit N]

Estimated runtime: ~2 hours for the full 68,654-case retrieval at 10 req/s
(per FUTURE_WORK.md). Progress checkpoints to <DATA_DIR>/nl_outcome_TEMP.json
every 250 ECLIs — safe to interrupt (Ctrl-C) and resume by re-running.
"""
import os, re, sys, json, time, argparse
import urllib.request, urllib.parse, ssl
from pathlib import Path
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')

try:
    import pandas as pd
except ImportError:
    raise SystemExit('pip install pandas')

# ── HTTP setup — matches scrapers/netherlands/rechtspraak_scraper.py exactly ──
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
HDRS = {'User-Agent': 'research/water-law-dataset (academic use; contact your-email@example.com)'}

CONTENT_URL = 'https://data.rechtspraak.nl/uitspraken/content'

DL = Path(os.getenv('DATA_DIR', '.'))
CSV_IN     = DL / 'water_law_global_coded.csv'
CHECKPOINT = DL / 'nl_outcome_TEMP.json'
RATE_DELAY = 0.1   # ~10 req/s — the rate documented in FUTURE_WORK.md Step 1


# ════════════════════════════════════════════════════════════════════════════
# Step 1 — Retrieve full decision XML
# ════════════════════════════════════════════════════════════════════════════
def fetch_decision_xml(ecli, retries=3):
    url = CONTENT_URL + '?id=' + urllib.parse.quote(ecli)
    req = urllib.request.Request(url, headers=HDRS)
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=20, context=ctx) as r:
                return r.read().decode('utf-8', errors='replace')
        except Exception:
            if attempt == retries - 1:
                return None
            time.sleep(2 ** attempt)
    return None


# ════════════════════════════════════════════════════════════════════════════
# Step 2 — Extract the Beslissing (operative conclusion)
# ════════════════════════════════════════════════════════════════════════════
# Regex-against-raw-XML, not a full XML parse — this matches how
# rechtspraak_scraper.parse_content() already extracts <inhoudsindicatie>,
# and avoids adding an lxml dependency to a stdlib-only scraping toolchain.
_SECTION_RE = re.compile(
    r'<section[^>]*role="([^"]*)"[^>]*>(.*?)</section>', re.DOTALL | re.IGNORECASE)
_HEADING_RE = re.compile(
    r'>(?:\d+(?:\.\d+)*\.?\s*)?Beslissing<.*?</(?:para|nr|section)>(.*?)'
    r'(?:</uitspraak>|</section>|$)', re.DOTALL | re.IGNORECASE)
_TAG_RE = re.compile(r'<[^>]+>')


def _strip_tags(fragment):
    return re.sub(r'\s+', ' ', _TAG_RE.sub(' ', fragment)).strip()


def extract_beslissing(xml_text):
    """Return the Beslissing section text, or the best available fallback."""
    sections = _SECTION_RE.findall(xml_text)
    for role, body in reversed(sections):           # Beslissing is always last
        if 'beslissing' in role.lower():
            return _strip_tags(body)
    m = _HEADING_RE.search(xml_text)
    if m:
        return _strip_tags(m.group(1))[:3000]
    # Last resort: operative conclusions sit at the tail of the body text
    return _strip_tags(xml_text)[-1500:]


# ════════════════════════════════════════════════════════════════════════════
# Step 3 — Classify via regex (resolves ~85-90% per the validated sample)
# ════════════════════════════════════════════════════════════════════════════
# Order matters: more specific dispositions are checked before the generic
# WIN/LOSS phrases they could otherwise be swallowed by (e.g. a remand often
# also "vernietigt" the lower decision, but REMAND is the more informative label).
OUTCOME_PATTERNS = [
    ('INADMISSIBLE', r'niet-ontvankelijk|onbevoegd'),
    ('REMAND',       r'verwijst de zaak terug|draagt.*?opnieuw te beslissen'),
    ('PARTIAL',      r'gedeeltelijk gegrond'),
    ('WIN',          r'verklaart het beroep gegrond|vernietigt\b'),
    ('LOSS',         r'verklaart het beroep ongegrond|bevestigt de aangevallen'),
]
_OUTCOME_RE = [(label, re.compile(pattern, re.I)) for label, pattern in OUTCOME_PATTERNS]


def classify_outcome_regex(beslissing_text):
    text = beslissing_text.lower()
    for label, rx in _OUTCOME_RE:
        if rx.search(text):
            return label
    return 'UNCLASSIFIED'


# ════════════════════════════════════════════════════════════════════════════
# Step 4 — LLM fallback for UNCLASSIFIED residue
# ════════════════════════════════════════════════════════════════════════════
OUTCOME_PROMPT = """You are classifying the outcome of a Dutch administrative court decision.
Read the following "Beslissing" (operative conclusion) paragraph and classify the outcome
as exactly one of:

  WIN          — the appellant's appeal was upheld (fully or substantially)
  LOSS         — the appeal was dismissed; the original decision stands
  PARTIAL      — the appeal was partly upheld and partly dismissed
  INADMISSIBLE — the court declined jurisdiction or declared the appeal inadmissible
  REMAND       — the case was sent back to a lower court or authority for fresh decision
  UNCLEAR      — genuinely ambiguous; cannot be classified from this text alone

Respond with ONLY the label. No explanation, no punctuation.

Beslissing text:
\"\"\"{text}\"\"\"
"""
_VALID_LLM_LABELS = {'WIN', 'LOSS', 'PARTIAL', 'INADMISSIBLE', 'REMAND', 'UNCLEAR'}
LLM_MODEL = os.getenv('NL_OUTCOME_LLM_MODEL', 'claude-haiku-4-5')


def classify_outcome_llm(beslissing_text, client):
    message = client.messages.create(
        model=LLM_MODEL,
        max_tokens=10,
        messages=[{'role': 'user',
                   'content': OUTCOME_PROMPT.format(text=beslissing_text[:2000])}],
    )
    label = message.content[0].text.strip().upper()
    return label if label in _VALID_LLM_LABELS else 'UNCLEAR'


# ════════════════════════════════════════════════════════════════════════════
# Pipeline driver — retrieval + classification with checkpointing
# ════════════════════════════════════════════════════════════════════════════
def load_checkpoint():
    if CHECKPOINT.exists():
        with open(CHECKPOINT, encoding='utf-8') as f:
            return json.load(f)
    return {}


def save_checkpoint(results):
    tmp = CHECKPOINT.with_suffix('.json.tmp')
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False)
    tmp.replace(CHECKPOINT)


def make_llm_client(skip_llm):
    if skip_llm:
        return None
    try:
        import anthropic
        return anthropic.Anthropic()
    except Exception as e:
        print(f'  LLM fallback unavailable ({e}) — UNCLASSIFIED rows stay UNCLASSIFIED')
        return None


def run_pipeline(eclis, skip_llm=False):
    results = load_checkpoint()
    already = sum(1 for e in eclis if e in results)
    print(f'Resuming from checkpoint: {already:,} of {len(eclis):,} ECLIs already processed')

    client = make_llm_client(skip_llm)
    llm_calls = 0

    for i, ecli in enumerate(eclis):
        if ecli in results:
            continue

        xml = fetch_decision_xml(ecli)
        if xml is None:
            results[ecli] = 'FETCH_ERROR'
        else:
            beslissing = extract_beslissing(xml)
            label = classify_outcome_regex(beslissing)
            if label == 'UNCLASSIFIED' and client is not None and beslissing:
                try:
                    label = classify_outcome_llm(beslissing, client)
                    llm_calls += 1
                except Exception as e:
                    print(f'  LLM error on {ecli}: {e}')
            results[ecli] = label

        if (i + 1) % 250 == 0 or (i + 1) == len(eclis):
            save_checkpoint(results)
            done = i + 1
            print(f'  {done:,}/{len(eclis):,} retrieved '
                  f'({llm_calls:,} LLM fallback calls so far) — checkpoint saved')

        time.sleep(RATE_DELAY)

    save_checkpoint(results)
    return results


# ════════════════════════════════════════════════════════════════════════════
# Step 5 — Merge outcome back into the main coded dataset
# ════════════════════════════════════════════════════════════════════════════
def find_ecli_column(df):
    """FUTURE_WORK.md assumes a dedicated `ecli` column; the actual
    merge_national.py schema stores the ECLI in `case_id` (and duplicates it
    into `title`) for Netherlands rows — there is no separate `ecli` column.
    Support both so this script works against the schema that really exists."""
    for col in ('ecli', 'case_id', 'title'):
        if col in df.columns:
            return col
    raise SystemExit('No ECLI-bearing column found (looked for ecli, case_id, title)')


def merge_outcomes(df, nl_mask, ecli_col, results):
    if 'outcome' not in df.columns:
        df['outcome'] = pd.NA
    df.loc[nl_mask, 'outcome'] = df.loc[nl_mask, ecli_col].map(results)
    return df


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--skip-llm', action='store_true',
                    help='Run regex classification only (no Anthropic API calls)')
    ap.add_argument('--limit', type=int, default=None,
                    help='Process only the first N NL ECLIs (smoke-test mode)')
    args = ap.parse_args()

    if not CSV_IN.exists():
        raise SystemExit(f'Not found: {CSV_IN}\nSet DATA_DIR or run merge_national.py first.')

    print('Loading dataset...')
    df = pd.read_csv(CSV_IN, low_memory=False, encoding='utf-8-sig')
    nl_mask = df['country'].astype(str).str.contains('Netherlands|NL', case=False, na=False)
    print(f'  {len(df):,} total rows — {int(nl_mask.sum()):,} Netherlands rows')

    ecli_col = find_ecli_column(df)
    print(f'  Using `{ecli_col}` as the ECLI column for Netherlands rows')

    eclis = df.loc[nl_mask, ecli_col].dropna().unique().tolist()
    eclis = [e for e in eclis if str(e).startswith('ECLI:')]
    if args.limit:
        eclis = eclis[:args.limit]
    print(f'  {len(eclis):,} unique ECLIs to retrieve/classify')
    if not eclis:
        raise SystemExit('No ECLI-formatted values found — check the column mapping above.')

    results = run_pipeline(eclis, skip_llm=args.skip_llm)

    counts = Counter(results[e] for e in eclis if e in results)
    n_total = sum(counts.values())
    print('\nOutcome distribution:')
    for label, n in counts.most_common():
        print(f'  {label:14s} {n:6,d}  ({100*n/n_total:.1f}%)')

    df = merge_outcomes(df, nl_mask, ecli_col, results)
    df.to_csv(CSV_IN, index=False)
    print(f'\nSaved {CSV_IN} — `outcome` populated for '
          f'{df.loc[nl_mask, "outcome"].notna().sum():,} Netherlands rows')


if __name__ == '__main__':
    main()
