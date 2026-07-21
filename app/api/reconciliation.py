from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.raw_transaction import RawTransaction
from app.services.reconciliation_engine import ReconciliationEngine

router = APIRouter(tags=["Reconciliation"])


@router.post("/reconcile/database")
def reconcile_database(db: Session = Depends(get_db)):

    transactions = db.query(RawTransaction).all()

    if len(transactions) < 2:
        return {
            "message": "Not enough transactions to reconcile."
        }

    matches = ReconciliationEngine.reconcile(transactions)

    db.commit()

    return {
        "total_transactions": len(transactions),
        "matched_pairs": len(matches),
        "matches": matches
    }
    