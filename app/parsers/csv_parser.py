import csv
from decimal import Decimal
from datetime import datetime

from app.config.config_loader import ConfigLoader
from app.models.transaction import Transaction
from app.parsers.base_parser import BaseParser
from app.validation.validator import TransactionValidator
from app.utils.file_hash import calculate_sha256


class CSVParser(BaseParser):

    def __init__(self, bank_code: str):
        loader = ConfigLoader()
        self.config = loader.load(bank_code)
        self.mapping = self.config["column_mappings"]
        self.bank_code = bank_code

    def parse(self, file_path: str) -> list[Transaction]:

        transactions = []

        file_hash = calculate_sha256(file_path)
        print(f"Processing File SHA256: {file_hash}")

        with open(file_path, mode="r", newline="", encoding="utf-8") as csv_file:

            reader = csv.DictReader(csv_file)

            for line_number, row in enumerate(reader, start=2):

                try:

                    mapped_data = {
                        "transaction_id": row.get(
                            self.mapping.get("transaction_id", ""),
                            ""
                        ).strip(),

                        "transaction_date": row.get(
                            self.mapping.get("transaction_date", ""),
                            ""
                        ).strip(),

                        "amount": row.get(
                            self.mapping.get("amount", ""),
                            ""
                        ).strip(),

                        "currency": row.get(
                            self.mapping.get("currency", ""),
                            ""
                        ).strip(),

                        "description": row.get(
                            self.mapping.get("description", ""),
                            ""
                        ).strip(),

                        "reference": row.get(
                            self.mapping.get("reference", ""),
                            ""
                        ).strip()
                    }

                    TransactionValidator.validate(mapped_data)

                    transaction = Transaction(
                        transaction_id=mapped_data["transaction_id"],
                        bank_code=self.bank_code,
                        amount=Decimal(mapped_data["amount"]),
                        currency=mapped_data["currency"],
                        transaction_date=datetime.fromisoformat(
                            mapped_data["transaction_date"]
                        ),
                        direction=row.get("Direction", "").strip(),
                        reference=mapped_data["reference"],
                        counterparty=row.get("Counterparty", "").strip(),
                        narration=mapped_data["description"],
                        source_file=file_path
                    )

                    transactions.append(transaction)

                except Exception as error:

                    print(
                        f"Row {line_number} skipped: {error}"
                    )

        print(
            f"Successfully parsed {len(transactions)} transactions."
        )

        return transactions