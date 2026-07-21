# ReconX Engine

> Enterprise Automated Multi-Bank Settlement Reconciliation Platform

ReconX Engine is a scalable reconciliation platform designed to automate transaction matching across multiple banking systems. It supports multiple financial data formats, performs intelligent transaction matching, identifies reconciliation exceptions, and provides a complete audit trail for financial operations.

---

## Features

- Multi-bank transaction reconciliation
- CSV, MT940, and ISO 20022 CAMT.053 support
- Automated data ingestion pipeline
- Transaction normalization
- Exact, fuzzy, and rule-based matching
- Exception management
- Immutable audit logging
- RESTful API using FastAPI
- PostgreSQL database
- Docker support
- Secure environment variable management

---

## Tech Stack

### Backend

- Python 3.12
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic

### Data Processing

- RapidFuzz
- lxml
- PyYAML

### DevOps

- Docker
- Docker Compose
- GitHub Actions

### Testing

- Pytest
- Ruff
- Black
- MyPy

---

## Project Structure

```
app/
configs/
docs/
tests/
data/
migrations/
scripts/
```

---

## Security

- Environment variables
- API Key Authentication
- Input Validation
- SHA-256 File Integrity
- PAN Masking
- Audit Logging

---

## Development Status

Day 1 ✔ Repository Setup

Day 2 ⏳ In Progress

---

## Author

Mohammad Faizan Ansari

---

## License

Educational Project