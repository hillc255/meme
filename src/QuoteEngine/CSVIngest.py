from numpy import append
from typing import List
from IngestorInterface import IngestorInterface
from QuoteModel import QuoteModel
import pandas as pd


class CSVIngestor(IngestorInterface):

    allowed_file_extention: List[str] = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quoteList = []
        df = pd.read_csv(path, header=0)
        
        for index, row in df.iterrows():
            new_quoteList = QuoteModel(row['body'], row['author'])
            quoteList.append(new_quoteList)
        return quoteList
        
        
if __name__ == "__main__":
    
    quoteList = (CSVIngestor.parse('./_data/DogQuotes/DogQuotesCSV.csv'))
    print(quoteList)



#The project contains a CSVIngestor class.
#The class inherits the IngestorInterface.
#The class depends on the pandas library to complete the defined, abstract method signatures to parse CSV files.
#The parse method returns a valid QuoteModel

#hillc@LAPTOP-C1T59ERH MINGW64 ~/meme/src (main)
#$ python QuoteEngine/CSVIngest.py

#results in exception
#quoteList = (CSVIngestor.parse('./_data/DogQuotes/DogQuotesPDF.pdf'))
#print(quoteList)