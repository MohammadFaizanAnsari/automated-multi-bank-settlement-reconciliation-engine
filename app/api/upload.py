from pathlib import Path

from fastapi import APIRouter
from fastapi import Depends
from fastapi import File
from fastapi import Form
from fastapi import HTTPException
from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.raw_transaction import RawTransaction
from app.parsers.parser_factory import ParserFactory
from app.utils.file_hash import calculate_sha256

router = APIRouter(tags=["Upload"])

UPLOAD_DIRECTORY = Path("data/uploads")
UPLOAD_DIRECTORY.mkdir(parents=True, exist_ok=True)


@router.post("/upload")
async def upload_file(
    bank_code: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    file_path = UPLOAD_DIRECTORY / file.filename

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Calculate SHA-256 hash
    file_hash = calculate_sha256(str(file_path))

    # Check duplicate
    existing = (
        db.query(RawTransaction)
        .filter(RawTransaction.file_hash == file_hash)
        .first()
    )

    if existing:
        return {
            "message": "Duplicate file detected.",
            "file_hash": file_hash
        }

    # Parse transactions
    parser = ParserFactory.get_parser(
    str(file_path),
    bank_code
)
    transactions = parser.parse(str(file_path))

    if not transactions:
        return {
            "message": "No valid transactions found.",
            "transactions_imported": 0
        }

    # Save transactions
    for transaction in transactions:

        db.add(
            RawTransaction(
                transaction_id=transaction.transaction_id,
                bank_name=transaction.bank_code,
                source_file=str(file_path),
                file_hash=file_hash,
                amount=transaction.amount,
                currency=transaction.currency,
                transaction_date=transaction.transaction_date,
                description=transaction.narration,
                status="IMPORTED"
            )
        )

    db.commit()

    return {
        "message": "File uploaded successfully.",
        "bank": bank_code,
        "filename": file.filename,
        "transactions_imported": len(transactions),
        "file_hash": file_hash
    }