"""TxtIngest module provides ingestor with txt extension files."""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TxtIngestor(IngestorInterface):
    """TxtIngestor class for IngestorInterface.

    Class has a classmethod to parse txt extension then
    extract 'body' and 'author' for a QuoteModel object.
    """

    allowed_file_extension: List[str] = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse() extracts 'body' and 'author' QuoteModel objects.

        Parameters:
            path (str) : path of txt file.
        Return:
            List[QuoteModel] : List of QuoteModel objects.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quoteList = []

        with open(path, encoding='utf8') as f:

            for line in f:
                line = line.strip('\n\n\r').strip().replace(u'\ufeff', '')
                body, author = tuple(line.split(' - '))
                quoteList.append(QuoteModel(body, author))
        return quoteList
