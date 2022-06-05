"""PDFIngest odule provides ingestor for files with pdf extensions."""
from IngestorInterface import IngestorInterface
from QuoteModel import QuoteModel
import subprocess
import tempfile
import os
from typing import List
import random


class PDFIngestor(IngestorInterface):
    """PDFIngestor class for IngestorInterface."""

    allowed_file_extension: List[str] = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        tmp = f'{random.randint(0,100000000)}.txt'

        call = subprocess.call(['pdftotext', '-simple', '-nopgbrk', path, tmp])

        quoteList = []

        with open(tmp, 'r') as fList:

            for line in fList:
                line = line.strip('\n\n\r').replace('"', '')
                body, author = tuple(line.split(' - '))
                quoteList.append(QuoteModel(body, author))
        os.remove(tmp)

        return quoteList
