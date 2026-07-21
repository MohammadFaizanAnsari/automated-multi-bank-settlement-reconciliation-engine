from datetime import datetime


class TransactionNormalizer:

    @staticmethod
    def normalize(transaction: dict) -> dict:
        """
        Convert transactions from different bank formats
        into one standard structure.
        """

        return {
            "transaction_id": str(
                transaction.get("transaction_id", "")
            ).strip(),

            "bank_name": str(
                transaction.get("bank_name", "")
            ).strip(),

            "source_file": str(
                transaction.get("source_file", "")
            ).strip(),

            "amount": float(
                transaction.get("amount", 0)
            ),

            "currency": str(
                transaction.get("currency", "INR")
            ).upper(),

            "transaction_date": TransactionNormalizer.parse_date(
                transaction.get("transaction_date")
            ),

            "description": str(
                transaction.get("description", "")
            ).strip(),

            "status": str(
                transaction.get("status", "PENDING")
            ).upper()
        }

    @staticmethod
    def parse_date(value):

        if isinstance(value, datetime):
            return value

        formats = [
            "%Y-%m-%d",
            "%d-%m-%Y",
            "%d/%m/%Y",
            "%Y/%m/%d",
            "%d-%b-%Y"
        ]

        for fmt in formats:
            try:
                return datetime.strptime(value, fmt)
            except Exception:
                pass

        raise ValueError(
            f"Unsupported date format: {value}"
        )