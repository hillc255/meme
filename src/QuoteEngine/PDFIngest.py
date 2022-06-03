from IngestorInterface import IngestorInterface
from QuoteModel import QuoteModel
from numpy import append
import subprocess
import tempfile
import os
from typing import List
import random

class PDFIngestor(IngestorInterface):

    allowed_file_extension = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        tmp = f'{random.randint(0,100000000)}.txt'
        #print(tmp)

        call = subprocess.call(['pdftotext', '-simple', '-nopgbrk', path, tmp])
 
        quoteList = []

        with open(tmp, 'r') as fList:

            for line in fList:
                line = line.strip('\n\n\r').replace('"','')           
                body, author = tuple(line.split(' - '))
                quoteList.append(QuoteModel(body, author))
        os.remove(tmp)

        return quoteList
       


if __name__ == "__main__":
    
    quoteList = (PDFIngestor.parse('./_data/DogQuotes/DogQuotesPDF.pdf'))
    print(quoteList)
    
    
# clear;python QuoteEngine/PDFIngest.py   
# pdftotext DogQuotesPDF.pdf
#The project contains a PDFIngestor class.
#The PDFIngestor class inherits from the IngestorInterface class.
#The PDFIngestor class utilizes the subprocess module to call the pdftotext 
# CLI utility—creating a pipeline that converts PDFs to text and then ingests the text.
#The class handles deleting temporary files.
#The parse method returns a valid QuoteModel
#NOTE: Do not use the pdftotext PIP Library - we'd like you to demonstrate your 
# understanding of the subprocess module.