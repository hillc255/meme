"""IngestorInterface module provides generic abstract base classes."""

from QuoteModel import QuoteModel
from abc import ABC, abstractmethod
from typing import List


class IngestorInterface(ABC):
    """IngestorInterface class for generic classmethods.

    Class has a classmethod for parsing of files and
    extracting 'body' and 'author' for a QuoteModel object.
    """

    allowed_file_extension: List[str] = []

    @classmethod
    def can_ingest(cls, path: str):
        """Can_ingest classmethod to determine allowed_file_extension."""
        extension = path.split('.')[-1]
        return extension in cls.allowed_file_extension

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse abstract method used for strategy object parsing."""
        pass
