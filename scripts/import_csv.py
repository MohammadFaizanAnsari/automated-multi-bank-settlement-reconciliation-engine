from app.database.database import SessionLocal
from app.database.repository import RawTransactionRepository
from app.parsers.csv_parser import CSVParser


def main():

    db = SessionLocal()

    parser = CSVParser("HDFC")

    transactions = parser.parse(
        "data/sample_csv/hdfc_transactions.csv"
    )

    repository = RawTransactionRepository(db)

    repository.save_all(transactions)

    print(f"{len(transactions)} transactions imported successfully.")

    db.close()


if __name__ == "__main__":
    main()