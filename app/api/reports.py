from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.raw_transaction import RawTransaction
from app.reports.excel_report import ExcelReport

router = APIRouter(tags=["Reports"])


@router.get("/reports/excel")
def generate_excel_report(
    db: Session = Depends(get_db)
):

    transactions = db.query(
        RawTransaction
    ).all()

    matches = []

    processed = set()

    for transaction in transactions:

        if (
            transaction.match_status == "MATCHED"
            and transaction.transaction_id not in processed
        ):

            matches.append(
                {
                    "transaction_1": transaction.transaction_id,
                    "transaction_2": transaction.matched_transaction_id,
                    "score": transaction.match_score,
                    "reason": (
                        transaction.match_reason.split(", ")
                        if transaction.match_reason
                        else []
                    )
                }
            )

            processed.add(
                transaction.transaction_id
            )

            processed.add(
                transaction.matched_transaction_id
            )

    report_path = ExcelReport.generate(
        matches,
        transactions,
        "reports/reconciliation_report.xlsx"
    )

    return FileResponse(
        path=report_path,
        filename="ReconX_Reconciliation_Report.xlsx",
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )