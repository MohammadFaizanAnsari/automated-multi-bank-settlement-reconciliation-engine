from rapidfuzz import fuzz


class MatchingEngine:
    """
    Handles transaction reconciliation.
    """

    @staticmethod
    def exact_match(txn1: dict, txn2: dict) -> bool:
        """
        Match by transaction ID.
        """

        return (
            txn1["transaction_id"]
            == txn2["transaction_id"]
        )

    @staticmethod
    def amount_match(txn1: dict, txn2: dict) -> bool:
        """
        Match by amount.
        """

        return (
            float(txn1["amount"])
            == float(txn2["amount"])
        )

    @staticmethod
    def date_match(txn1: dict, txn2: dict) -> bool:
        """
        Match by transaction date.
        """

        return (
            txn1["transaction_date"]
            == txn2["transaction_date"]
        )

    @staticmethod
    def description_match(txn1: dict, txn2: dict) -> int:
        """
        Fuzzy description similarity.
        Returns score from 0–100.
        """

        return fuzz.token_sort_ratio(
            txn1["description"],
            txn2["description"]
        )

    @staticmethod
    def reconcile(txn1: dict, txn2: dict) -> dict:

        result = {
            "matched": False,
            "confidence": 0,
            "reason": ""
        }

        if MatchingEngine.exact_match(txn1, txn2):
            result["matched"] = True
            result["confidence"] = 100
            result["reason"] = "Exact Transaction ID Match"

            return result

        if (
            MatchingEngine.amount_match(txn1, txn2)
            and MatchingEngine.date_match(txn1, txn2)
        ):

            score = MatchingEngine.description_match(
                txn1,
                txn2
            )

            if score >= 80:

                result["matched"] = True
                result["confidence"] = score
                result["reason"] = (
                    "Amount + Date + Description Match"
                )

                return result

        return result