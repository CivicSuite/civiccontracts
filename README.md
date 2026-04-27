# CivicContracts

CivicContracts is the CivicSuite module for central contract registry support, clause topic lookup, expiration tracking, renewal visibility, and public-records-aware exports.

Current state: **v0.1.0 contract repository foundation release**. This repo ships a FastAPI package, health/root endpoints, documentation gates, deterministic sample contract registry, clause topic lookup, expiration tracking helper, renewal visibility helper, public-records export checklist, and accessible public sample UI at `/civiccontracts`. It does **not** ship live contract management platforms, official legal interpretation, legal advice, live LLM calls, contract execution workflows, or contract system-of-record integrations.

## What CivicContracts Does

- Create sample contract registry stubs and review notes.
- Flag common clause topics for staff/legal review.
- Build expiration reminder plans.
- Summarize renewal visibility without approving renewals.
- Produce public-records-aware export checklists.
- Demonstrate a public contract-support UI at `/civiccontracts`.

## What CivicContracts Does Not Do

- It does not interpret legal obligations.
- It does not approve renewals or execute contracts.
- It does not provide legal advice.
- It does not call live LLMs in v0.1.0.
- It does not replace a contract system of record.

## API Surface

- `GET /` returns the shipped/planned boundary.
- `GET /health` returns package and CivicCore versions.
- `GET /civiccontracts` returns the accessible public sample UI.
- `POST /api/v1/civiccontracts/registry` returns a sample contract registry stub.
- `POST /api/v1/civiccontracts/clauses/lookup` returns clause topic flags.
- `POST /api/v1/civiccontracts/expirations` returns expiration reminders.
- `POST /api/v1/civiccontracts/renewals/summary` returns renewal visibility items.
- `POST /api/v1/civiccontracts/export` returns a public-records export checklist.

## Local Development

```bash
python -m pip install -e ".[dev]"
python -m pytest -q
bash scripts/verify-release.sh
```

## License

Code is Apache License 2.0. Documentation is CC BY 4.0.
