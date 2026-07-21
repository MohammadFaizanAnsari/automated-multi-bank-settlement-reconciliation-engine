from fastapi import APIRouter
from fastapi import Depends
from fastapi import Query
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.raw_transaction import RawTransaction

router = APIRouter(tags=["Search"])


@router.get("/search")
def search_transactions(
    bank: str | None = Query(default=None),
    status: str | None = Query(default=None),
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=10, ge=1, le=100),
    sort_by: str = Query(default="transaction_date"),
    order: str = Query(default="desc"),
    db: Session = Depends(get_db)
):

    query = db.query(RawTransaction)

    if bank:
        query = query.filter(
            RawTransaction.bank_name.ilike(bank)
        )

    if status:
        query = query.filter(
            RawTransaction.match_status == status.upper()
        )

    sortable_columns = {
        "transaction_date": RawTransaction.transaction_date,
        "amount": RawTransaction.amount,
        "bank": RawTransaction.bank_name,
        "created_at": RawTransaction.created_at
    }

    sort_column = sortable_columns.get(
        sort_by,
        RawTransaction.transaction_date
    )

    if order.lower() == "asc":
        query = query.order_by(sort_column.asc())
    else:
        query = query.order_by(sort_column.desc())

    total = query.count()

    transactions = (
        query.offset((page - 1) * page_size)
        .limit(page_size)
        .all()
    )

    return {
        "page": page,
        "page_size": page_size,
        "total_records": total,
        "total_pages": (
            (total + page_size - 1) // page_size
        ),
        "transactions": transactions
    }