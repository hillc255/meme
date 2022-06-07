"""CSVIngest module provides ingestor with csv extension files."""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import pandas as pd


class CSVIngestor(IngestorInterface):
    """CSVIngestor class for IngestorInterface.

    Class has a classmethod to parse csv extension then
    extract 'body' and 'author' for a QuoteModel object.
    """

    allowed_file_extension: List[str] = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse() extracts 'body' and 'author' QuoteModel objects.

        Parameters:
            path (str) : path of csv file.
        Return:
            List[QuoteModel] : List of QuoteModel objects.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quoteList = []
        df = pd.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quoteList = QuoteModel(row['body'], row['author'])
            quoteList.append(new_quoteList)
        return quoteList
