import uuid

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database.database import Base


class RawTransaction(Base):

    __tablename__ = "raw_transactions"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    transaction_id = Column(
        String,
        nullable=False
    )

    bank_name = Column(
        String,
        nullable=False
    )

    source_file = Column(
        String,
        nullable=False
    )

    # SHA-256 hash of the imported file
    file_hash = Column(
        String(64),
        nullable=False
    )

    amount = Column(
        Numeric(18, 2),
        nullable=False
    )

    currency = Column(
        String(10),
        nullable=False
    )

    transaction_date = Column(
        DateTime,
        nullable=False
    )

    description = Column(
        String
    )

    status = Column(
        String,
        default="IMPORTED"
    )

    matched_transaction_id = Column(
        String,
        nullable=True
    )

    match_status = Column(
        String,
        default="UNMATCHED"
    )

    match_score = Column(
        Float,
        default=0
    )

    match_reason = Column(
        String,
        nullable=True
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )