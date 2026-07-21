from pathlib import Path

from app.parsers.csv_parser import CSVParser


class ParserFactory:
    @staticmethod
    def get_parser(file_path: str, bank_code: str):
        extension = Path(file_path).suffix.lower()

        if extension == ".csv":
            return CSVParser(bank_code)

        raise ValueError(
            f"No parser available for '{extension}' files."
        )