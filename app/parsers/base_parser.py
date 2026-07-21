from abc import ABC, abstractmethod

from app.models.transaction import Transaction


class BaseParser(ABC):

    @abstractmethod
    def parse(self, file_path: str) -> list[Transaction]:
        """
        Parse bank statement file
        """
        pass