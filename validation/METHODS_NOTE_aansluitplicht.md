# Lexical Confounds in Multilingual Jurimetric Classification: The Dutch *Aansluitplicht* Problem

**Draft methods note — for submission to *Artificial Intelligence and Law* or *Journal of Empirical Legal Studies***  
**Author:** Claudio Klaus Junior  
**Date:** May 2026  
**Dataset:** Global Water Law Judicial Decisions Dataset v0.3.0  
(doi:10.5281/zenodo.19836413; Harvard Dataverse doi:10.7910/DVN/C9PEFS)

---

## Abstract

Computational classification of multilingual administrative law corpora is subject to a class
of error that has not, to our knowledge, been systematically documented in the jurimetrics
literature: **cross-utility lexical confounds**, in which a legal concept with a stable meaning
in one regulatory domain shares its vocabulary with structurally different concepts in adjacent
domains. We document one instance from Dutch administrative law: the term *aansluitplicht*
(connection obligation), which is the natural query term for searching household service-access
disputes, is in practice almost entirely monopolised by electricity and heat network litigation
under the Elektriciteitswet 1998 (Article 23) and the Warmtewet (Heat Act). A search for
*aansluitplicht* in a corpus of 68,654 Dutch administrative court decisions produces 14 hits in
the `not_water_related` category — zero of which involve water or sanitation. This finding has
two implications: (1) researchers using keyword search to identify water service-connection
disputes in Dutch administrative law risk high false-positive rates from energy utility
litigation; and (2) the near-total absence of water-sanitation *aansluitplicht* litigation is
itself a substantive finding about the Dutch administrative architecture, not a data artefact.

---

## 1. Background

The Global Water Law Judicial Decisions Dataset covers 83,596 judicial decisions from Brazil,
the Netherlands, and Canada, classified across 21 governance categories by a multilingual
jurimetric coding engine. The project's theoretical frame — the Administrative Ghost thesis
(Klaus 2026) — posits that populations excluded from formal administrative systems are rendered
invisible in the formal judicial record. Testing this claim requires distinguishing between
two causes of low case counts in any given category:

(a) genuine absence of litigation (no legal disputes of this type reach courts), versus  
(b) classification failure (decisions exist but the classifier does not recognise them).

For the Dutch corpus, the thesis predicts genuine absence: the Netherlands' layered pre-litigation
absorption architecture (bezwaar procedure under the Awb, Geschillencommissie Energie & Water,
National Ombudsman) resolves household service-access disputes before courts. Only 8 Dutch
decisions in the v0.3.0 dataset are classified as connection refusal (0.012 % of 68,654 total).
A peer reviewer may ask whether these 8 represent a classification failure rather than genuine
absence. The *aansluitplicht* search is the strongest available test.

---

## 2. The Confound

In Dutch administrative law, the word *aansluiten* (to connect) and its derivatives
(*aansluitplicht*, *aansluitvergunning*, *aansluitrecht*) describe the legal obligation of a
network operator to connect a premises to a utility network. The concept exists across:

| Utility | Governing statute | Jurisdiction | Key article |
|---|---|---|---|
| Electricity | Elektriciteitswet 1998 (E-wet) | CBB | Art. 23 |
| Gas | Gaswet | CBB | Art. 10 |
| Heat network | Warmtewet | CBB / RvS | Art. 6 |
| Telecommunications | Telecommunicatiewet | CBB | Arts. 6.6–6.10 |
| Drinking water | Drinkwaterbesluit | Geschillencommissie / Awb / Ombudsman | Arts. 8–11 |
| Sewer / sanitation | Gemeentewet / Bouwbesluit | Municipal level | — |

The crucial asymmetry is **jurisdictional**: for electricity, gas, and heat, disputes about
connection obligations reach the CBB (College van Beroep voor het bedrijfsleven, Trade and
Industry Appeals Tribunal), the Raad van State (Council of State), and the district courts.
For drinking water and sanitation, equivalent disputes are resolved through administrative
objection procedures and specialist consumer tribunals — not through the courts indexed in the
Rechtspraak.nl database.

This asymmetry means that a keyword search for *aansluitplicht* in the Rechtspraak.nl corpus
systematically retrieves electricity and heat network disputes while failing to retrieve water
and sanitation disputes — not because the latter are absent from the legal system, but because
they are processed through a different institutional channel.

---

## 3. Data

We searched the 67,665 Dutch decisions classified as `not_water_related` in the v0.3.0
dataset for the terms *aansluitplicht*, *aansluitvergunning*, and *weigering aansluiting*
(connection refusal). We identified **14 decisions** containing these terms.

### Table 1: The 14 *aansluitplicht* decisions in NL `not_water_related`

| ECLI | Court | Governing statute | Subject |
|---|---|---|---|
| ECLI:NL:CBB:2016:243 | CBB | Warmtewet | Heat network connection obligation |
| ECLI:NL:CBB:2020:382 | CBB | Art. 23 E-wet | Electricity grid *aansluitplicht* (netbeheerder) |
| ECLI:NL:CBB:2020:383 | CBB | Art. 23 E-wet | Electricity grid connection, business premises |
| ECLI:NL:CBB:2020:364 | CBB | Art. 23 E-wet | Electricity *aansluitplicht* + WOZ valuation |
| ECLI:NL:CBB:2020:649 | CBB | Art. 23 E-wet | Connection < 10 MVA, 18-week term |
| ECLI:NL:CBB:2020:650 | CBB | Art. 23 E-wet | Connection < 10 MVA (companion case) |
| ECLI:NL:CBB:2021:927 | CBB | Art. 23 E-wet | Wind park grid connection |
| ECLI:NL:CBB:2022:63 | CBB | Art. 51 + Art. 23 E-wet | Electricity grid connection |
| ECLI:NL:CBB:2025:290 | CBB | E-wet | ACM enforcement of Liander connection obligation |
| ECLI:NL:RBAMS:2020:2413 | Rb Amsterdam | Warmtewet / Bouwbesluit 2012 | Warmteplan Sluisbuurt — heat network |
| ECLI:NL:RVS:2022:517 | RvS | Warmtewet | Warmteplan Sluisbuurt 2018 |
| ECLI:NL:RVS:2017:1757 | RvS | Bouwbesluit | Building permit + incidental sewer mention |
| ECLI:NL:RBMNE:2021:4523 | Rb Midden-NL | Wet Natuurbescherming | Stikstof/nitrogen enforcement |
| ECLI:NL:RBMNE:2022:1789 | Rb Midden-NL | Wet Natuurbescherming | Stikstof/nitrogen (pig farming) |

**Zero** of the 14 decisions involve water or sanitation connection obligation.

Nine decisions (all CBB) involve the Art. 23 Elektriciteitswet 1998 obligation of electricity
network operators to connect premises. Two decisions involve the *warmteplan* instrument under
the Warmtewet (compulsory heat-district connection). Two decisions involve nitrogen-emission
enforcement where the word *weigering* (refusal) matches the search term but the subject is
agri-environmental, not utility. One decision involves a building permit with an incidental
mention of sewer (*riolering*) connection.

---

## 4. Why This Happens — and Why It Matters

### 4.1 Statutory architecture

The Dutch Drinkwaterbesluit (Drinking Water Decree, implementing Art. 15 Drinkwaterwet)
establishes an obligation on water supply companies to provide connections (*aansluiting*).
However, disputes about that obligation follow the Awb administrative objection procedure
(*bezwaar* and *beroep*). If the dispute is not resolved through bezwaar, it goes to the
Geschillencommissie Energie & Water (consumer disputes tribunal) or the National Ombudsman.
Only residual cases reach the administrative courts — and those are indexed in Rechtspraak.nl.
The v0.3.0 dataset finds 8 such cases.

By contrast, electricity grid connection obligations under Art. 23 E-wet generate substantial
CBB litigation, because commercial electricity consumers (including wind park developers and
large industrial facilities) routinely litigate connection refusals by network operators. The
asymmetry is not about the strength of the legal right but about **who the right-holders are
and what institutional channels they use**.

### 4.2 Implications for jurimetric research design

Cross-utility lexical confounds of this type have a predictable structure:

1. A legal concept X has the same name (and often the same doctrinal logic) across regulatory
   domains A and B.
2. Domain A (electricity) generates high-volume court litigation (high institutional visibility).
3. Domain B (water) routes disputes through pre-litigation channels (low institutional visibility).
4. A keyword search for X retrieves domain-A decisions and produces a false impression of
   domain-B activity (or, conversely, its absence).

The researcher who finds "no water connection refusal cases" after searching *aansluitplicht*
has not found a classification success — they have found a cross-utility confound. The correct
inference requires independent investigation of the institutional channel (here, the
Geschillencommissie Energie & Water and the Ombudsman) to determine where domain-B disputes go.

### 4.3 A note on cross-jurisdictional generalisability

Analogous confounds likely exist in other multilingual administrative law corpora:

- **Brazil:** *ligação* (connection) is used in electricity, telephone, and water/sanitation
  contexts; ANATEL and ANEEL regulatory filings use the same vocabulary as CAESB/SABESP
  administrative acts.
- **Canada:** "connection" litigation in provincial utility boards covers electricity, gas,
  and telecom; water service disputes are handled by municipal administrative procedures.
- **Portugal / Spain:** *acometida* (service connection) appears across utility regimes.

Jurimetric studies classifying access disputes in administrative law corpora should, as a
minimum, inspect the regulatory-law context of connection-language hits before reporting counts.

---

## 5. Substantive Contribution

Beyond the methodological caveat, the *aansluitplicht* finding constitutes a substantive
contribution to comparative water governance research:

> **The near-absence of water-sanitation *aansluitplicht* litigation in Dutch administrative
> courts is not a data artefact — it is a structural feature of the Dutch administrative
> architecture.** Even in the legal domain where the vocabulary of connection obligation is
> most developed and most litigated (electricity), the equivalent water-sanitation mechanism
> operates entirely outside the court system.

This strengthens, rather than weakens, the pre-litigation absorption thesis. The Dutch
administrative architecture does not merely *reduce* water connection-refusal litigation —
it *eliminates* it from the judicial record. The 8 classified connection-refusal cases (0.012 %
of 68,654 decisions) are residual outliers, not representatives of a hidden mass.

---

## 6. Suggested Citation

Klaus, CJ (2026) 'Lexical confounds in multilingual jurimetric classification: the Dutch
*aansluitplicht* problem' [draft methods note, Global Water Law Judicial Decisions Dataset
v0.3.0, doi:10.5281/zenodo.19836413].

---

## References

- Drinkwaterbesluit (Decree of 23 May 2011, Stb. 2011, 293)  
- Elektriciteitswet 1998 (Law of 2 July 1998, Stb. 1998, 427), Art. 23  
- Warmtewet (Law of 12 July 2012, Stb. 2012, 441)  
- Algemene wet bestuursrecht (Awb), Arts. 7:1–7:28 (bezwaar), Arts. 8:1–8:119 (beroep)  
- Klaus, CJ (2026) *The Legal Last Mile: Administrative Law, Water Access, and the Limits of
  Judicial Inclusion* [preliminary research]  
- Geschillencommissie Energie & Water, Jaarverslag 2023 (annual report)
