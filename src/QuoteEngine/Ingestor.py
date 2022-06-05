
from typing import List
from QuoteModel import QuoteModel
from IngestorInterface import IngestorInterface
from DocxIngest import DocxIngestor
from CSVIngest import CSVIngestor
from PDFIngest import PDFIngestor
from TxtIngest import TxtIngestor
from os.path import exists


class Ingestor(IngestorInterface):
    importers = [DocxIngestor, CSVIngestor, PDFIngestor, TxtIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not exists(path):
            raise Exception('file does not exist')
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
        raise Exception('cannot ingest exception')


if __name__ == "__main__":

    csvList = (Ingestor.parse('./_data/DogQuotes/DogQuotesCSV.csv'))
    print(f'\nCSV: ', csvList)

    txtList = (Ingestor.parse('./_data/DogQuotes/DogQuotesTXT.txt'))
    print(f'\nTXT: ', txtList)

    docxList = (Ingestor.parse('./_data/DogQuotes/DogQuotesDOCX.docx'))
    print(f'\nDOC: ', docxList)

    pdfList = (Ingestor.parse('./_data/DogQuotes/DogQuotesPDF.pdf'))
    print(f'\nPDF: ', pdfList)

    try:
        docmList = (Ingestor.parse('./_data/DogQuotes/DogQuotesDOCM.docm'))
    except ValueError:
        print("\nDOCMdocm: Ingestor extension not valid")

    try:
        docmtxtList = (Ingestor.parse('./_data/DogQuotes/DogQuotesDOCM.txt'))
    except FileNotFoundError:
        print(f'\nDOCMtxt: File not found')
