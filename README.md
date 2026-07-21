# 🚀 Automated Multi-Bank Settlement Reconciliation Engine (ReconX)

An enterprise-grade backend application built with **FastAPI**, **PostgreSQL**, and **Docker** that automates the reconciliation of settlement transactions received from multiple banks. The system imports bank statements, validates records, detects duplicate uploads, performs intelligent transaction matching, and generates reconciliation reports.

---

# 📌 Project Objective

Financial institutions often receive settlement files from different banks in varying formats. Manually reconciling these transactions is time-consuming and error-prone.

This project automates the reconciliation process by:

- Importing bank statements
- Validating transaction data
- Preventing duplicate imports
- Matching transactions across banks
- Generating reconciliation reports
- Providing dashboard statistics

---

# ✨ Features

- ✅ Multi-bank transaction import
- ✅ CSV Parser
- ✅ YAML-based bank configuration
- ✅ Transaction validation
- ✅ SHA-256 duplicate file detection
- ✅ PostgreSQL storage
- ✅ Automated reconciliation engine
- ✅ Intelligent fuzzy description matching
- ✅ Dashboard API
- ✅ Transaction Search API
- ✅ Import History API
- ✅ Excel Report Generation
- ✅ Dockerized deployment
- ✅ Interactive Swagger Documentation

---

# 🛠 Technology Stack

| Technology | Purpose |
|------------|---------|
| FastAPI | REST API Framework |
| Python 3 | Backend |
| PostgreSQL | Database |
| SQLAlchemy | ORM |
| Docker | Containerization |
| Docker Compose | Multi-container Deployment |
| Redis | Cache Layer |
| PyYAML | Bank Configuration |
| RapidFuzz | Fuzzy Matching |
| OpenPyXL | Excel Report Generation |
| ReportLab | PDF Support |
| Uvicorn | ASGI Server |

---

# 📂 Project Structure

```
Automated Multi-Bank Settlement Reconciliation Engine
│
├── app
│   ├── api
│   ├── audit
│   ├── config
│   ├── database
│   ├── exceptions
│   ├── matching
│   ├── models
│   ├── parsers
│   ├── reconciliation
│   ├── reports
│   ├── repositories
│   ├── services
│   ├── utils
│   └── validation
│
├── configs
├── data
├── scripts
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# 🏦 Supported Banks

Currently Supported

- HDFC Bank (CSV)
- ICICI Bank (CSV)

Architecture supports adding additional banks through YAML configuration files.

---

# ⚙ System Workflow

```
Bank Statement Upload
          │
          ▼
Duplicate File Detection
          │
          ▼
CSV Parser
          │
          ▼
Transaction Validation
          │
          ▼
PostgreSQL Database
          │
          ▼
Matching Engine
          │
          ▼
Reconciliation Result
          │
          ▼
Dashboard & Reports
```

---

# 🔍 Matching Logic

Transactions are compared using multiple rules.

| Rule | Weight |
|------|---------|
| Amount | 40 |
| Transaction Date | 20 |
| Currency | 10 |
| Transaction ID | 20 |
| Description Similarity | 10 |

Transactions with sufficient confidence are automatically reconciled.

---

# 📡 REST APIs

## Upload Bank Statement

```
POST /upload
```

Uploads and imports a bank statement.

---

## View Transactions

```
GET /transactions
```

Returns all imported transactions.

---

## Reconcile Transactions

```
POST /reconcile/database
```

Matches transactions from different banks.

---

## Dashboard

```
GET /dashboard
```

Displays reconciliation statistics.

---

## Import History

```
GET /history
```

Returns uploaded file history.

---

## Search Transactions

```
GET /search
```

Search transactions using filters.

---

## Download Excel Report

```
GET /reports/excel
```

Downloads reconciliation report in Excel format.

---

# 📊 Dashboard Statistics

The dashboard provides:

- Total Transactions
- Matched Transactions
- Unmatched Transactions
- Total Imported Files
- Total Banks
- Match Percentage

---

# 📈 Report Generation

The system generates an Excel report containing:

- Summary Sheet
- Matched Transactions
- Unmatched Transactions

---

# 🚀 Running the Project

## Clone Repository

```bash
git clone https://github.com/<your-username>/automated-multi-bank-settlement-reconciliation-engine.git
```

## Open Project

```bash
cd automated-multi-bank-settlement-reconciliation-engine
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Start Docker Containers

```bash
docker compose up --build
```

---

# 🌐 API Documentation

Swagger UI

```
http://localhost:8000/docs
```

Application

```
http://localhost:8000
```

---

# 🧪 Sample Reconciliation Result

```
HDFC Transaction
Amount : ₹1500.50

↓

ICICI Transaction
Amount : ₹1500.50

↓

Score : 100%

↓

Status : MATCHED
```

---

# 🔮 Future Enhancements

- MT940 Parser
- CAMT.053 Parser
- Authentication & Authorization
- PDF Statement Support
- Scheduled Reconciliation
- Email Notifications
- Advanced Analytics Dashboard
- Role-Based Access Control (RBAC)

---

# 👨‍💻 Author

**Mohammad Faizan Ansari**

B.Tech – Computer Science Engineering

GitHub:
https://github.com/<your-username>

---

# 📄 License

This project is developed for educational and internship evaluation purposes.