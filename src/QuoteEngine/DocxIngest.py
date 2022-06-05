"""DocxIngestor module provides ingestor for files with docx extensions."""
from typing import List
from IngestorInterface import IngestorInterface
from QuoteModel import QuoteModel
import docx


class DocxIngestor(IngestorInterface):
    """DocxIngestor class for IngestorInterface."""

    allowed_file_extension: List[str] = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quoteList = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')

                if len(parse) == 2:
                    new_quoteList = QuoteModel(parse[0], str(parse[1]))
                    new_quoteList = para.text.replace('"', '')
                    quoteList.append(new_quoteList)

        return quoteList
