import csv
import json
from pathlib import Path


class ReportGenerator:
    """
    Generates reconciliation reports.
    """

    @staticmethod
    def export_json(result: dict, output_path: str):

        output_file = Path(output_path)

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                result,
                file,
                indent=4,
                default=str
            )

    @staticmethod
    def export_csv(result: dict, output_path: str):

        output_file = Path(output_path)

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            output_file,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Transaction ID",
                "Bank 1",
                "Bank 2",
                "Amount",
                "Confidence",
                "Reason"
            ])

            for match in result["matched"]:

                txn1 = match["bank1_transaction"]
                txn2 = match["bank2_transaction"]

                writer.writerow([
                    txn1["transaction_id"],
                    txn1["bank_name"],
                    txn2["bank_name"],
                    txn1["amount"],
                    match["confidence"],
                    match["reason"]
                ])

    @staticmethod
    def print_summary(result: dict):

        summary = result["summary"]

        print("=" * 50)
        print("RECONCILIATION SUMMARY")
        print("=" * 50)

        print(
            f"Matched Transactions : "
            f"{summary['matched_count']}"
        )

        print(
            f"Unmatched Bank 1 : "
            f"{summary['unmatched_bank1']}"
        )

        print(
            f"Unmatched Bank 2 : "
            f"{summary['unmatched_bank2']}"
        )

        print("=" * 50)