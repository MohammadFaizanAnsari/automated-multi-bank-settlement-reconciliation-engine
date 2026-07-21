from fastapi import APIRouter
from sqlalchemy import func

from app.database.database import SessionLocal
from app.models.raw_transaction import RawTransaction

router = APIRouter(tags=["Import History"])


@router.get("/imports")
def import_history():

    db = SessionLocal()

    try:

        imports = (
            db.query(
                RawTransaction.source_file,
                RawTransaction.bank_name,
                func.count(RawTransaction.id).label("transactions"),
                func.min(RawTransaction.created_at).label("import_time")
            )
            .group_by(
                RawTransaction.source_file,
                RawTransaction.bank_name
            )
            .all()
        )

        results = []

        for item in imports:

            results.append(
                {
                    "bank": item.bank_name,
                    "file": item.source_file,
                    "transactions": item.transactions,
                    "import_time": item.import_time
                }
            )

        return results

    finally:
        db.close()