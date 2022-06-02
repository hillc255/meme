from numpy import append
from typing import List
from IngestorInterface import IngestorInterface
from QuoteModel import QuoteModel
import docx

class DocxIngestor(IngestorInterface):

    allowed_file_extention = ['docx']
    
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
                    quoteList.append(new_quoteList)

        return quoteList

if __name__ == "__main__":
    
    quoteList = (DocxIngestor.parse('./_data/DogQuotes/DogQuotesDOCX.docx'))
    print(quoteList)

#hillc@LAPTOP-C1T59ERH MINGW64 ~/meme/src (main)
#$ python QuoteEngine/DocxIngest.py

#The project contains a DocxIngestor class.
#The class inherits from the IngestorInterface class.
#The class depends on the python-docx library to complete the defined, abstract method signatures to parse DOCX files.
#The parse method returns a valid QuoteModel