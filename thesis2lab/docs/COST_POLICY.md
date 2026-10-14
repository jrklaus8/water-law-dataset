# Cost policy

## Public runtime
Zero model calls, zero servers, zero paid services. The site is static files. `requires_ai: true` fails validation.

## Development
- Do local inspection and deterministic scripts first. Delegate to a model only for reading and judgement work that scripts cannot do.
- One coordinator; at most one specialist agent at a time unless tasks are independent and the benefit is clear.
- Use economical models for formatting, metadata extraction and routine edits. Reserve stronger models for architecture, validation design and methodological interpretation.
- Do not send whole documents to a model when a targeted extraction works. Never send confidential material to an external service without authorisation.
- Cache by digest. `npm run changes` shows what is stale; revalidate only that.
- Retry loops stop after three attempts; document the blocker instead.
- Never invent token or billing figures. `npm run cost` reports only what the repository can measure and marks the rest "not measured". Record real spend by hand in `docs/cost-ledger.json` (`{"entries":[{"date","item","amount","note"}]}`).

## Infrastructure
GitHub free tier only. CI runs on pull requests that touch `thesis2lab/` and uses dependency caching. Deployment is manual. No custom domain, no paid hosting, no secrets in the repository.
