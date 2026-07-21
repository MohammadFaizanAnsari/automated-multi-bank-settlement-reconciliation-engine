from sqlalchemy.orm import Session

from app.models.raw_transaction import RawTransaction


class TransactionRepository:

    def __init__(self, db: Session):
        self.db = db

    def save(self, transaction: RawTransaction):
        self.db.add(transaction)

    def save_all(self, transactions: list[RawTransaction]):
        self.db.add_all(transactions)

    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()

    def get_all(self):
        return self.db.query(RawTransaction).all()