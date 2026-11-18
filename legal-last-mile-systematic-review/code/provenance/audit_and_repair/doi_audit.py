import csv, sys, re
csv.field_size_limit(sys.maxsize)

PATH = "/home/user/water-law-dataset/legal-last-mile-systematic-review/01_search/deduplicated/deduplicated_records.csv"

with open(PATH) as f:
    rows = list(csv.DictReader(f))

def normalize(doi):
    d = doi.strip().lower()
    if not d:
        return ""
    # strip common URL/prefix wrappers
    d = re.sub(r'^(https?://)?(dx\.)?doi\.org/', '', d)
    d = re.sub(r'^doi:\s*', '', d)
    d = d.strip()
    return d

entries = []
for row in rows:
    n = normalize(row['doi'])
    if n:
        entries.append((n, row['record_id'], row['title'][:80], row['year'], row['database']))

print("total records:", len(rows))
print("records with non-empty DOI:", len(entries))

# 1. Exact normalized-DOI duplicates
from collections import defaultdict
by_doi = defaultdict(list)
for n, rid, title, year, db in entries:
    by_doi[n].append((rid, title, year, db))

exact_dupes = {k: v for k, v in by_doi.items() if len(v) > 1}
print("\n=== EXACT normalized-DOI duplicate groups:", len(exact_dupes), "===")
for doi, group in list(exact_dupes.items())[:50]:
    print(f"-- {doi}")
    for rid, title, year, db in group:
        print(f"     {rid} | {year} | {db} | {title}")

# 2. Prefix-relationship duplicates (one DOI is a strict prefix of another) -- the S063 pattern
entries_sorted = sorted(set((n, rid) for n, rid, *_ in entries))
info = {rid: (title, year, db) for n, rid, title, year, db in entries}

prefix_pairs = []
WINDOW = 8
for i in range(len(entries_sorted)):
    n1, rid1 = entries_sorted[i]
    for j in range(i+1, min(i+1+WINDOW, len(entries_sorted))):
        n2, rid2 = entries_sorted[j]
        if n2 == n1:
            continue  # already covered by exact-dupes above
        if not n2.startswith(n1):
            break  # sorted, so once it stops sharing prefix window can stop growing for this n1 in most cases
        if rid1 == rid2:
            continue
        # require a meaningful shared prefix, not just a couple chars
        if len(n1) >= 10:
            prefix_pairs.append((n1, rid1, n2, rid2))

print("\n=== PREFIX-relationship candidate pairs (one DOI is a prefix of another):", len(prefix_pairs), "===")
for n1, rid1, n2, rid2 in prefix_pairs[:100]:
    t1, y1, d1 = info[rid1]
    t2, y2, d2 = info[rid2]
    print(f"-- SHORT: {rid1} ({y1}, {d1}) doi={n1!r} | {t1}")
    print(f"   LONG : {rid2} ({y2}, {d2}) doi={n2!r} | {t2}")
