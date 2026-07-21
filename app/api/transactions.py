from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.raw_transaction import RawTransaction

router = APIRouter(tags=["Transactions"])


@router.get("/transactions")
def get_transactions(db: Session = Depends(get_db)):
    transactions = db.query(RawTransaction).all()

    return [
        {
            "id": str(transaction.id),
            "transaction_id": transaction.transaction_id,
            "bank_name": transaction.bank_name,
            "source_file": transaction.source_file,
            "amount": float(transaction.amount),
            "currency": transaction.currency,
            "transaction_date": transaction.transaction_date,
            "description": transaction.description,
            "status": transaction.status,
            "created_at": transaction.created_at,
        }
        for transaction in transactions
    ]