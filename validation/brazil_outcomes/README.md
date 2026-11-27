# Brazil `unclear` outcomes: disposition audit (2026-11-27)

Scope: diagnosis only. No `win_loss` value in the dataset was changed and no user/utility label was assigned.

Of 11,724 Brazilian rows, 7,243 (61.8%) are `unclear`. Reading the last 700 characters of each `unclear` summary:

| Disposition found in the tail | Rows | Share |
|---|---|---|
| none recognised | 3,796 | 52.4% |
| desprovido / improvido / negado provimento (appeal failed) | 1,714 | 23.7% |
| provido (appeal succeeded) | 1,517 | 20.9% |
| parcialmente provido | 123 | 1.7% |
| não conhecido | 93 | 1.3% |

So about 47.6% of the `unclear` rows (3,447) state whether the appeal succeeded, and the existing coder does not read it (for example "RECURSO CONHECIDO ... NO MÉRITO, DESPROVIDO" and "Apelação conhecida e provida" both come out `unclear`).

**Why this does not become a user/utility label automatically.** "Provido" means the appellant won. The label the dataset needs is whether the water user or the utility won, so the appellant must be known. The summary names it in a recognisable way for only a minority: a utility named as appellant in 557 `unclear` rows, an appellant word without a utility in 1,543, no appellant word in 5,143. A rule that guessed would put real error into the Priority 2 validation set in FUTURE_WORK.md.

Options for the researcher: (a) code only "appeal succeeded / failed" as a new variable and keep user/utility for the rows where the appellant is readable; (b) fetch the party data from the TJDFT and TJRJ sources, which publish it; (c) leave as is and report the 61.8% denominator.

Files: `disposition_audit.py` (rebuilds the CSV from the Dataverse file) and `brazil_disposition_audit.csv` (one row per Brazilian row: court, case_id, current win_loss, disposition found).
Caveat: the phrase lists were written for this audit and not validated against a human-coded sample.
