# Security and privacy policy

This is a research repository, not a service. The realistic security and privacy problems are an exposed credential, personal data of third parties, licensed or confidential material that should not be public, and scraper behaviour that harms a data source.

## Reporting a problem

**Do not describe the problem in a public issue.** Instead:

1. If GitHub's *Report a vulnerability* feature (Security tab) is enabled for this repository, use it.
2. Otherwise open a public issue titled "Request for private contact" with no details, and the maintainer will reply with a way to send them. *(The maintainer should replace this paragraph with a monitored contact address once one has been chosen; none is recorded in the repository.)*

Please include the file path and line number and what you found. **Do not paste the secret, the personal data or the licensed text into the report.** If you find a credential, assume it is compromised.

## What is in scope

| Kind | Examples |
|---|---|
| Credentials | an API key (CanLII, Legal Data Hunter, Anthropic), a token, a password in code, configuration, documents or data |
| Personal data | e-mail addresses or names of authors or parties in data files or documents |
| Licensed or confidential content | subscription-database exports, publisher full texts, links to a private shared folder |
| Source harm | a scraper that ignores a site's terms or rate limits, disables TLS verification or impersonates a browser |
| CI and supply chain | a workflow with excessive permissions, an unpinned or compromised action |

## What to expect

*Proposed handling, drafted by an AI assistant for the maintainer to confirm or change; it is not a commitment the maintainer has made.* Reports would be handled by one researcher alongside other work, so there is no response-time guarantee. The suggested order is: confirm the report; remove or restrict the material in the working tree; rotate any credential; decide separately whether Git history or a deposit must be cleaned (history is not rewritten without a deliberate decision); record the event, without the secret, in `docs/audit-report.md` or the review's errors register.

## Known issues

Open, documented issues of this kind are listed in [`docs/findings-register.csv`](docs/findings-register.csv) (for example F-01 TLS verification, F-04 database exports, F-05 e-mail addresses, F-07 a shared-folder identifier). A known issue does not need a new report unless you have new information.

## Supported versions

Only the current default branch and the latest tagged release receive attention. The review is an interim, preliminary deposit.

## Safe handling in this repository

- `.env` files are git-ignored; only `.env.example` with placeholders is tracked.
- `tests/test_repository_hygiene.py` scans code, configuration and documents for common credential patterns and reports only the file and line, never the value. Data files are not scanned.
- Nothing in the test suite touches the network.
