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

 # exception for extension which is not on list?   
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
    print(f'\nCSV: ',csvList)

    txtList = (Ingestor.parse('./_data/DogQuotes/DogQuotesTXT.txt'))
    print(f'\nTXT: ',txtList)

    docxList = (Ingestor.parse('./_data/DogQuotes/DogQuotesDOCX.docx'))
    print(f'\nDOC: ',docxList)

    #not working
    #pdfList = (Ingestor.parse('./_data/DogQuotes/DogQuotesPDF.pdf'))
    #print(f'\nPDF: ',pdfList)

    #extension does not exist
    try:
        docmList = (Ingestor.parse('./_data/DogQuotes/DogQuotesDOCM.docm'))
        #print(f'\nError should throw Exception')
        raise
    except:
        print(f'Ingestor extension not valid')

    #file does not exist
    try:
        docmtxtList = (Ingestor.parse('./_data/DogQuotes/DogQuotesDOCM.txt'))
        #print(f'\nError should throw Exception')
        raise
    except:
        print(f'File not found')

#All ingestors are packaged into a main Ingestor class.
# This class encapsulates all the ingestors to provide one interface 
# to load any supported file type.

#hillc@LAPTOP-C1T59ERH MINGW64 ~/meme/src (main)
# python QuoteEngine/Ingestor.py
