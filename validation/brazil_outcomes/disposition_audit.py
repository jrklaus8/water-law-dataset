#!/usr/bin/env python3
"""Audit of Brazil `win_loss = unclear` rows: how many carry an explicit disposition (provido, desprovido, ...) in the tail of the summary.

This does NOT assign user_wins / utility_wins. A disposition says whether the APPEAL succeeded; mapping that to the user or the
utility needs the identity of the appellant, which the dataset does not store as a field. The script reports how often the
appellant can be read from the summary text (apelante/agravante followed by a utility name) so the researcher can judge the route.

Usage: python validation/brazil_outcomes/disposition_audit.py CODED_CSV OUT_CSV
"""
import collections
import csv
import re
import sys

csv.field_size_limit(10 ** 9)
rows = [r for r in csv.DictReader(open(sys.argv[1], encoding="utf-8-sig")) if r["country"] == "Brazil"]

PARC = re.compile(r"parcial(?:mente)?\s+provid|provimento\s+parcial|dar?\s+parcial\s+provimento|parcial\s+provimento", re.I)
DESP = re.compile(r"desprovid|improvid|negar?(?:-se)?\s+provimento|nega(?:-se|do)?\s+provimento|negou\s+provimento|nega-se|recurso\s+n[aã]o\s+provido", re.I)
PROV = re.compile(r"\bprovid[oa]s?\b|\bdar?(?:-se)?\s+provimento|d[aá]-se\s+provimento|dou\s+provimento|deu\s+provimento|recurso\s+acolhido", re.I)
NCONH = re.compile(r"n[aã]o\s+conhecid|n[aã]o\s+se\s+conhece|recurso\s+inadmitido|deserto", re.I)
UTIL = r"(?:CAESB|SABESP|CEDAE|SANEAGO|COPASA|SANEPAR|CASAN|EMBASA|COMPESA|CAGECE|CORSAN|Companhia\s+de\s+Saneamento|Concession[aá]ria|Águas\s+do\s+Rio|Rio\s+Águas|Iguá|BRK)"
APEL_UTIL = re.compile(r"(?:apelante|agravante|recorrente|embargante|requerente)[^.]{0,80}" + UTIL, re.I)
APEL_PERSON = re.compile(r"(?:apelante|agravante|recorrente)\s*:?\s*(?!" + UTIL + ")", re.I)


def disposition(summary):
    tail = summary[-700:]
    if PARC.search(tail):
        return "PARTIAL_PROVIDO"
    if DESP.search(tail):
        return "DESPROVIDO"
    if NCONH.search(tail):
        return "NAO_CONHECIDO"
    if PROV.search(tail):
        return "PROVIDO"
    return "NONE"


out = []
c = collections.Counter()
ap = collections.Counter()
for r in rows:
    d = disposition(r["summary"])
    if r["win_loss"] == "unclear":
        c[d] += 1
        ap["utility_named_as_appellant" if APEL_UTIL.search(r["summary"]) else ("appellant_word_only" if APEL_PERSON.search(r["summary"]) else "no_appellant_word")] += 1
    out.append({"court_name": r["court_name"], "case_id": r["case_id"], "win_loss": r["win_loss"], "disposition": d})
with open(sys.argv[2], "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["court_name", "case_id", "win_loss", "disposition"])
    w.writeheader()
    w.writerows(out)
n = sum(c.values())
print("unclear rows:", n)
for k, v in c.most_common():
    print("  disposition %-16s %5d (%.1f%%)" % (k, v, 100 * v / n))
print("appellant readable from summary (unclear rows):", dict(ap))
