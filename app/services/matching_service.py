from decimal import Decimal

from rapidfuzz import fuzz


class MatchingService:

    @staticmethod
    def calculate_match_score(tx1, tx2):

        score = 0
        reasons = []

        # Amount Match (40)
        if Decimal(tx1.amount) == Decimal(tx2.amount):
            score += 40
            reasons.append("Amount")

        # Date Match (25)
        if tx1.transaction_date.date() == tx2.transaction_date.date():
            score += 25
            reasons.append("Date")

        # Currency Match (15)
        if tx1.currency.upper() == tx2.currency.upper():
            score += 15
            reasons.append("Currency")

        # Description Similarity (20)
        similarity = fuzz.token_sort_ratio(
            tx1.description or "",
            tx2.description or ""
        )

        if similarity >= 80:
            score += 20
            reasons.append(f"Description ({similarity:.0f}%)")

        return score, reasons