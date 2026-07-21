from fastapi import FastAPI
from pydantic import BaseModel

from app.api.upload import router as upload_router
from app.api.transactions import router as transactions_router
from app.api.reconciliation import router as reconciliation_router
from app.api.dashboard import router as dashboard_router
from app.api.reports import router as reports_router
from app.api.import_history import router as import_history_router
from app.api.search import router as search_router

from app.services.reconciliation_service import ReconciliationService
from app.services.report_generator import ReportGenerator


app = FastAPI(
    title="ReconX Engine",
    version="1.0.0",
    description="""
Automated Multi-Bank Settlement Reconciliation Engine

Features:
- Multi-bank CSV Import
- Duplicate File Detection
- Transaction Validation
- Automated Reconciliation
- Dashboard Analytics
- Excel Report Generation
""",
    contact={
        "name": "Mohammad Faizan Ansari"
    },
    license_info={
        "name": "MIT"
    }
)

# Register API Routers
app.include_router(upload_router)
app.include_router(transactions_router)
app.include_router(reconciliation_router)
app.include_router(dashboard_router)
app.include_router(reports_router)
app.include_router(import_history_router)
app.include_router(search_router)


@app.get("/", tags=["Home"])
def root():
    return {
        "application": "ReconX Engine",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health", tags=["Health"])
def health():
    return {
        "status": "healthy"
    }


class ReconciliationRequest(BaseModel):
    bank1_transactions: list
    bank2_transactions: list


@app.post("/reconcile", tags=["Reconciliation"])
def reconcile(request: ReconciliationRequest):

    service = ReconciliationService()

    result = service.reconcile_transactions(
        request.bank1_transactions,
        request.bank2_transactions
    )

    ReportGenerator.export_json(
        result,
        "reports/report.json"
    )

    ReportGenerator.export_csv(
        result,
        "reports/report.csv"
    )

    return result