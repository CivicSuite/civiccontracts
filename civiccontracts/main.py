"""FastAPI runtime foundation for CivicContracts."""

from datetime import date

from civiccore import __version__ as CIVICCORE_VERSION
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from civiccontracts import __version__
from civiccontracts.clause_lookup import lookup_clause_topics
from civiccontracts.contract_registry import register_contract_stub
from civiccontracts.expiration_tracker import build_expiration_plan
from civiccontracts.public_ui import render_public_lookup_page
from civiccontracts.records_export import build_contract_records_export
from civiccontracts.renewal_visibility import summarize_renewal_visibility


app = FastAPI(
    title="CivicContracts",
    version=__version__,
    description="Contract repository, clause lookup, expiration tracking, renewal visibility, and public-records-aware export support for CivicSuite.",
)


class ContractRegistryRequest(BaseModel):
    contract_id: str
    vendor_name: str
    contract_type: str


class ClauseLookupRequest(BaseModel):
    query: str
    contract_text: str


class ExpirationRequest(BaseModel):
    contract_id: str
    expiration_date: date


class RenewalRequest(BaseModel):
    contract_id: str
    renewal_terms: str
    department_notes: str = ""


class RecordsExportRequest(BaseModel):
    contract_id: str
    title: str
    format: str = "markdown"


@app.get("/")
def root() -> dict[str, str]:
    """Return current product state without overstating unshipped behavior."""

    return {
        "name": "CivicContracts",
        "version": __version__,
        "status": "contract repository foundation",
        "message": (
            "CivicContracts package, API foundation, sample contract registry, clause lookup, "
            "expiration tracking helper, renewal visibility helper, public-records export checklist, "
            "and public UI foundation are online; live contract management platforms, official legal "
            "interpretation, legal advice, live LLM calls, contract execution workflows, and contract "
            "system-of-record integrations are not implemented yet."
        ),
        "next_step": "Post-v0.1.0 roadmap: local contract catalog configuration, CivicRecords file links, and staff review queues",
    }


@app.get("/health")
def health() -> dict[str, str]:
    """Return dependency/version health for deployment smoke checks."""

    return {
        "status": "ok",
        "service": "civiccontracts",
        "version": __version__,
        "civiccore_version": CIVICCORE_VERSION,
    }


@app.get("/civiccontracts", response_class=HTMLResponse)
def public_civiccontracts_page() -> str:
    """Return the public sample contract repository support UI."""

    return render_public_lookup_page()


@app.post("/api/v1/civiccontracts/registry")
def contract_registry(request: ContractRegistryRequest) -> dict[str, object]:
    return register_contract_stub(
        contract_id=request.contract_id,
        vendor_name=request.vendor_name,
        contract_type=request.contract_type,
    ).__dict__


@app.post("/api/v1/civiccontracts/clauses/lookup")
def clause_lookup(request: ClauseLookupRequest) -> dict[str, object]:
    return lookup_clause_topics(
        query=request.query,
        contract_text=request.contract_text,
    ).__dict__


@app.post("/api/v1/civiccontracts/expirations")
def expiration_plan(request: ExpirationRequest) -> dict[str, object]:
    return build_expiration_plan(
        contract_id=request.contract_id,
        expiration_date=request.expiration_date,
    ).__dict__


@app.post("/api/v1/civiccontracts/renewals/summary")
def renewal_summary(request: RenewalRequest) -> dict[str, object]:
    return summarize_renewal_visibility(
        contract_id=request.contract_id,
        renewal_terms=request.renewal_terms,
        department_notes=request.department_notes,
    ).__dict__


@app.post("/api/v1/civiccontracts/export")
def records_export(request: RecordsExportRequest) -> dict[str, object]:
    return build_contract_records_export(
        contract_id=request.contract_id,
        title=request.title,
        format=request.format,
    ).__dict__
