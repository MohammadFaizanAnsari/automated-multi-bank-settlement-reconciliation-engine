from app.database.database import SessionLocal
from app.models.raw_transaction import RawTransaction
from app.parsers.parser_factory import ParserFactory
from app.repositories.transaction_repository import TransactionRepository


class ImportService:

    @staticmethod
    def import_file(file_path: str, bank_code: str):

        parser = ParserFactory.get_parser(
            file_path,
            bank_code
        )

        transactions = parser.parse(file_path)

        db = SessionLocal()

        try:
            repo = TransactionRepository(db)

            raw_transactions = []

            for tx in transactions:

                raw_transactions.append(
                    RawTransaction(
                        transaction_id=tx.transaction_id,
                        bank_name=tx.bank_code,
                        source_file=tx.source_file or file_path,
                        amount=tx.amount,
                        currency=tx.currency,
                        transaction_date=tx.transaction_date,
                        description=tx.narration,
                        status="IMPORTED"
                    )
                )

            repo.save_all(raw_transactions)
            repo.commit()

            return transactions

        except Exception:
            db.rollback()
            raise

        finally:
            db.close()