from typing import List
from IngestorInterface import IngestorInterface
from QuoteModel import QuoteModel


class TxtIngestor(IngestorInterface):

    allowed_file_extension = ['txt']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quoteList = []

        with open(path, encoding='utf8') as f:
            print(f'PATH: ',path)

            for line in f:
                line = line.strip('\n\n\r').strip().replace(u'\ufeff', '')
                body, author = tuple(line.split(' - '))
                quoteList.append(QuoteModel(body, author))
        return quoteList
       
if __name__ == "__main__":
    
    quoteList = (TxtIngestor.parse('./_data/DogQuotes/DogQuotesTXT.txt'))
    print(quoteList)



#The project contains a TextIngestor class.
#The class inherits the IngestorInterface.
#The class does not depend on any 3rd party library to complete the defined, 
# abstract method signatures to parse Text files.
#The parse method returns a valid QuoteModel


#hillc@LAPTOP-C1T59ERH MINGW64 ~/meme/src (main)
#$ python QuoteEngine/TxtIngest.py

#results in exception
#quoteList = (CSVIngestor.parse('./_data/DogQuotes/DogQuotesPDF.pdf'))
#print(quoteList)