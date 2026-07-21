from pathlib import Path

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors


class PDFReport:

    @staticmethod
    def generate(matches: list, output_file: str):

        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        document = SimpleDocTemplate(str(output_path))
        styles = getSampleStyleSheet()

        elements = []

        elements.append(
            Paragraph(
                "<b>ReconX Reconciliation Report</b>",
                styles["Title"]
            )
        )

        elements.append(Spacer(1, 20))

        elements.append(
            Paragraph(
                f"Matched Transactions: {len(matches)}",
                styles["Normal"]
            )
        )

        elements.append(Spacer(1, 15))

        table_data = [
            [
                "Transaction 1",
                "Transaction 2",
                "Score",
                "Reason"
            ]
        ]

        for match in matches:

            table_data.append(
                [
                    match["transaction_1"],
                    match["transaction_2"],
                    str(match["score"]),
                    ", ".join(match["reason"])
                ]
            )

        table = Table(table_data)

        table.setStyle(
            TableStyle([
                ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
                ("GRID", (0,0), (-1,-1), 1, colors.black),
                ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
                ("BOTTOMPADDING", (0,0), (-1,0), 10),
            ])
        )

        elements.append(table)

        document.build(elements)

        return str(output_path)