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

        call = subprocess.call(['pdftotext', '-simple', path, tmp])
        print(tmp)

        quoteList = []

        with open(tmp, encoding="utf-8") as fList:

            for line in fList:
                #
                # line = line.replace('\x0C', '')
                #line  = line.replace("\r", " ")
                #line = line.replace("\n", " ")
                #line = line.encode("ascii", "ignore")
                #line = line.decode()
                #line = line.rstrip().replace('\x0c\x0c', '')
                line = line.strip('\n\n\r').strip().rstrip().replace('"','')
                print(f'Each line: ',line)

                
                #body, author = tuple(line.split(' - '))
                #quoteList.append(QuoteModel(body, author))
                quoteList.append(line)
        return quoteList

        #-----------------------------------------------
        #file_ref = open(tmp, "r")
        #quoteList = []
        #for line in file_ref.readlines():
            #line = line.strip('\n\r').strip()

            #if len(line) > 0:
                #body, author = line.split('-')
                #new_quoteList = QuoteModel(body[0], str(author[1]))
                #quoteList.append(new_quoteList)
                
        #file_ref.close()
        #os.remove(tmp)
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