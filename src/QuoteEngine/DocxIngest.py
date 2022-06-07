"""DocxIngest module provides ingestor with docx extension files."""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import docx


class DocxIngestor(IngestorInterface):
    """DocxIngestor class for IngestorInterface.

    Class has a classmethod to parse docx extension then
    extract 'body' and 'author' for a QuoteModel object.
    """

    allowed_file_extension: List[str] = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse() extracts 'body' and 'author' QuoteModel objects.

        Parameters:
            path (str) : path of docx file.
        Return:
            List[QuoteModel] : List of QuoteModel objects.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quoteList = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.replace('"', '').split('-')
                if len(parse) == 2:
                    new_quoteList = QuoteModel(parse[0], str(parse[1]))
                    quoteList.append(new_quoteList)

        return quoteList
