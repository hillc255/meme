from QuoteModel import QuoteModel
from abc import ABC, abstractmethod
from typing import List


class IngestorInterface(ABC):

    allowed_file_extension: List[str] = []

    @classmethod
    def can_ingest(cls, path: str):
        extension = path.split('.')[-1]
        return extension in cls.allowed_file_extension

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
