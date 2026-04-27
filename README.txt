CivicContracts
============

CivicContracts is the CivicSuite module for central contract registry support, clause topic lookup, expiration tracking, renewal visibility, and public-records-aware exports.

Current state: v0.1.0 contract repository foundation release. It ships deterministic sample helpers and an accessible public sample UI at /civiccontracts.

Not shipped: live contract management platforms, official legal interpretation, legal advice, live LLM calls, contract execution workflows, or contract system-of-record integrations.

API surface:
- GET /
- GET /health
- GET /civiccontracts
- POST /api/v1/civiccontracts/registry
- POST /api/v1/civiccontracts/clauses/lookup
- POST /api/v1/civiccontracts/expirations
- POST /api/v1/civiccontracts/renewals/summary
- POST /api/v1/civiccontracts/export

License: code Apache License 2.0; documentation CC BY 4.0.
