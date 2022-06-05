"""TxtIngest module provides ingestor for files with pdf extensions."""
from typing import List
from IngestorInterface import IngestorInterface
from QuoteModel import QuoteModel


class TxtIngestor(IngestorInterface):
    """TxtIngestor class for IngestorInterface."""

    allowed_file_extension: List[str] = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quoteList = []

        with open(path, encoding='utf8') as f:

            for line in f:
                line = line.strip('\n\n\r').strip().replace(u'\ufeff', '')
                body, author = tuple(line.split(' - '))
                quoteList.append(QuoteModel(body, author))
        return quoteList
