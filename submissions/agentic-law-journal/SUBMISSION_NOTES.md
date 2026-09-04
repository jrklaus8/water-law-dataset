# Agentic Law Journal — submission package

This directory holds the manuscript prepared for the *Agentic Law Journal*
(ALJ), Volume I (2026), "First Contact: Law for the Agentic Web"
(https://niccoloridi.com/agentic-law-journal/), and the exact field values
to use when calling its submission API. It was written in a session whose
network egress policy blocked `niccoloridi.com`, so submission is still
pending. `manuscript.md` is the complete paper (title, abstract, body,
bibliography, footnotes) in one file. Below are the same values split out
for the `POST /editorial/submit` call.

## API sequence (from the journal's own skill file)

```
GET  /editorial/challenge               -> { token, question }
POST /editorial/register                -> { name, operator, token, answer } -> api_key
POST /editorial/submit  (Bearer key)    -> { title, abstract, body_markdown,
                                             model, human_involvement,
                                             contact_email (optional) }
                                          -> manuscript number (ALJ-2026-NNNN)
GET  /editorial/status?id=ALJ-2026-NNNN -> under_review | accepted | declined
```

Base URL: `https://niccoloridi.com`. Full skill file (if this copy is
stale): `GET https://niccoloridi.com/agentic-law-journal-skill.md`.
Treaty (needed to answer the reverse-CAPTCHA challenge question):
`https://niccoloridi.com/treaties/`.

## Registration fields

- `name`: `Claude Sonnet 5`
- `operator`: `Anthropic`
- `token` / `answer`: from `GET /editorial/challenge`, answered by reading
  the Treaty at the URL above.

## Submission fields

- `title`: `Ghosts Before the Claim: What Water Law's Missing Litigants Should Teach Agentic Eligibility Systems`
- `abstract`: the text under `## Abstract` in `manuscript.md` (250 words,
  fits the journal's 250-word cap).
- `body_markdown`: the full contents of `manuscript.md` (~7,180 words,
  under the 10,000-word cap).
- `model`: `Claude Sonnet 5 (Anthropic)`
- `human_involvement`:

  > A human researcher (the maintainer of the underlying Global Water Law
  > Judicial Decisions Dataset, https://github.com/jrklaus8/water-law-dataset)
  > requested that this submission be prepared and directed the submitting
  > agent to the dataset's public GitHub repository as source material. The
  > human did not select the paper's specific thesis, structure, argument,
  > or any of its prose; those were determined by the submitting agent. The
  > human's contribution was limited to: (1) the instruction to write and
  > submit a paper to this journal; (2) provision of access to the
  > repository (a dataset, prior human-authored preliminary research, and
  > documentation) that the paper cites and draws upon as external
  > empirical source material, in the same way any published dataset or
  > article might be cited; and (3) no review, editing, or revision of the
  > paper's text prior to submission. All analysis, argument, citation
  > selection, drafting, and editing of this manuscript were performed by
  > the agent identified in the `model` field.

- `contact_email` (optional, kept private by the journal, never published):
  the submitting user's own email address for this account. Do not commit
  it to this file or to the repository; read it from the session's own
  user context and pass it directly in the API call.

## Before submitting

Re-verify word/character counts against the journal's current limits
(title ≤ 200 chars, abstract ≤ 250 words, body ≤ 10,000 words) in case the
rules have changed since this package was written, and re-check that every
citation in `manuscript.md` still resolves to a real source. All citations
were verified against live search results at drafting time (September
2026); none were fabricated.

## After submitting

Report the manuscript number (`ALJ-2026-NNNN`) back to the user, and note
that `GET /editorial/status?id=...` can be polled later for the decision.
