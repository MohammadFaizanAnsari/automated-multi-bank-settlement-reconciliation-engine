from app.services.matching_service import MatchingService


class ReconciliationEngine:

    @staticmethod
    def reconcile(transactions):

        matched = []

        for i in range(len(transactions)):

            tx1 = transactions[i]

            if tx1.match_status == "MATCHED":
                continue

            for j in range(i + 1, len(transactions)):

                tx2 = transactions[j]

                if tx2.match_status == "MATCHED":
                    continue

                if tx1.bank_name == tx2.bank_name:
                    continue

                score, reasons = MatchingService.calculate_match_score(
                    tx1,
                    tx2
                )

                if score >= 90:

                    tx1.match_status = "MATCHED"
                    tx2.match_status = "MATCHED"

                    tx1.match_score = score
                    tx2.match_score = score

                    tx1.match_reason = ", ".join(reasons)
                    tx2.match_reason = ", ".join(reasons)

                    tx1.matched_transaction_id = tx2.transaction_id
                    tx2.matched_transaction_id = tx1.transaction_id

                    matched.append(
                        {
                            "transaction_1": tx1.transaction_id,
                            "transaction_2": tx2.transaction_id,
                            "score": score,
                            "reason": reasons
                        }
                    )

                    break

        return matched