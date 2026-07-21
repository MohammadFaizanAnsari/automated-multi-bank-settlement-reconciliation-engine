from app.services.matching_engine import MatchingEngine


class ReconciliationService:
    """
    Service responsible for reconciling
    transactions from multiple banks.
    """

    def __init__(self):
        self.matcher = MatchingEngine()

    def reconcile_transactions(
        self,
        bank1_transactions: list,
        bank2_transactions: list
    ) -> dict:

        matched = []
        unmatched_bank1 = []
        unmatched_bank2 = bank2_transactions.copy()

        for txn1 in bank1_transactions:

            found = False

            for txn2 in unmatched_bank2:

                result = self.matcher.reconcile(
                    txn1,
                    txn2
                )

                if result["matched"]:

                    matched.append({
                        "bank1_transaction": txn1,
                        "bank2_transaction": txn2,
                        "confidence": result["confidence"],
                        "reason": result["reason"]
                    })

                    unmatched_bank2.remove(txn2)
                    found = True
                    break

            if not found:
                unmatched_bank1.append(txn1)

        return {
            "matched": matched,
            "unmatched_bank1": unmatched_bank1,
            "unmatched_bank2": unmatched_bank2,
            "summary": {
                "matched_count": len(matched),
                "unmatched_bank1": len(unmatched_bank1),
                "unmatched_bank2": len(unmatched_bank2)
            }
        }