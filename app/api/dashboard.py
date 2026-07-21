from fastapi import APIRouter
from sqlalchemy import func

from app.database.database import SessionLocal
from app.models.raw_transaction import RawTransaction

router = APIRouter(tags=["Dashboard"])


@router.get("/dashboard")
def dashboard():

    db = SessionLocal()

    try:

        total_transactions = db.query(
            RawTransaction
        ).count()

        matched = db.query(
            RawTransaction
        ).filter(
            RawTransaction.match_status == "MATCHED"
        ).count()

        unmatched = total_transactions - matched

        total_banks = db.query(
            func.count(
                func.distinct(RawTransaction.bank_name)
            )
        ).scalar()

        total_files = db.query(
            func.count(
                func.distinct(RawTransaction.source_file)
            )
        ).scalar()

        return {
            "total_transactions": total_transactions,
            "matched_transactions": matched,
            "unmatched_transactions": unmatched,
            "banks": total_banks,
            "imported_files": total_files,
            "match_percentage": round(
                (matched / total_transactions) * 100,
                2
            ) if total_transactions else 0
        }

    finally:
        db.close()