# Production Depth: Contract Registry Persistence

## Summary

CivicContracts now supports optional SQLAlchemy-backed contract registry and renewal visibility records through `CIVICCONTRACTS_REGISTRY_DB_URL`.

## Shipped

- `ContractRegistryRepository` with schema-aware SQLAlchemy tables.
- Persisted contract registry records.
- Persisted renewal visibility records.
- Retrieval endpoints:
  - `GET /api/v1/civiccontracts/registry/{contract_id}`
  - `GET /api/v1/civiccontracts/renewals/{contract_id}`
- Actionable `503` guidance when persistence is not configured.
- Regression tests for repository reload, API round trip, missing-record `404`, no-config `503`, and stateless fallback behavior.

## Still Not Shipped

- Live contract management platforms.
- Official legal interpretation.
- Legal advice.
- Live LLM calls.
- Contract execution workflows.
- Contract system-of-record integrations.
