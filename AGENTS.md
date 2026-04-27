# CivicContracts Agent Contract

## Source of Truth

- Upstream suite spec: `CivicSuite/civicsuite/docs/CivicSuiteUnifiedSpec.md`, especially the CivicContracts catalog entry and suite-wide non-negotiables.
- CivicContracts supports central contract registry stubs, clause topic lookup, expiration tracking, renewal visibility, and public-records-aware export checklists.
- Staff own every decision.

## Hard Boundaries

- CivicContracts never interprets legal obligations, approves renewals, executes contracts, provides legal advice, or updates a contract system of record.
- CivicContracts v0.1.0 must not call live LLMs or live contract management platforms.
- Clause lookups, renewal visibility, and records exports must be marked staff-review-required where applicable.
- CivicContracts depends on CivicCore; CivicCore must never depend on CivicContracts.
- CivicContracts may reference CivicProcure and CivicRecords concepts only through released contracts or deterministic sample data in v0.1.0.

## Verification

Run `bash scripts/verify-release.sh` before every push or release.
