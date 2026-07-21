from dataclasses import dataclass
from decimal import Decimal
from datetime import datetime
from typing import Optional


@dataclass
class Transaction:
    transaction_id: str
    bank_code: str
    amount: Decimal
    currency: str
    transaction_date: datetime
    direction: str
    reference: str
    counterparty: str
    narration: Optional[str] = None
    source_file: Optional[str] = None