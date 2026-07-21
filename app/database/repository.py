from sqlalchemy.orm import Session

from app.models.raw_transaction import RawTransaction


class RawTransactionRepository:

    def __init__(self, db: Session):
        self.db = db

    def save(self, transaction):

        raw_transaction = RawTransaction(
            transaction_id=transaction.transaction_id,
            bank_name=transaction.bank_code,
            source_file=transaction.source_file,
            amount=transaction.amount,
            currency=transaction.currency,
            transaction_date=transaction.transaction_date,
            description=transaction.narration,
            status="IMPORTED"
        )

        self.db.add(raw_transaction)

    def save_all(self, transactions):

        for transaction in transactions:
            self.save(transaction)

        self.db.commit()