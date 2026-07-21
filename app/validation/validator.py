from decimal import Decimal
from datetime import datetime


class TransactionValidator:

    REQUIRED_FIELDS = [
        "transaction_id",
        "transaction_date",
        "amount",
        "currency"
    ]

    @staticmethod
    def validate(transaction: dict) -> None:

        # Validate required fields
        for field in TransactionValidator.REQUIRED_FIELDS:
            if field not in transaction or transaction[field] in ("", None):
                raise ValueError(f"Missing required field: {field}")

        # Validate amount
        try:
            Decimal(str(transaction["amount"]))
        except Exception:
            raise ValueError("Invalid amount")

        # Validate date
        try:
            datetime.fromisoformat(
                str(transaction["transaction_date"])
            )
        except Exception:
            raise ValueError("Invalid transaction date")

        # Validate currency
        currency = str(transaction["currency"]).strip().upper()

        if len(currency) != 3:
            raise ValueError("Invalid currency code")

        # Reference is optional
        if "reference" not in transaction:
            transaction["reference"] = ""