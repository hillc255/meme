from numpy import append
from IngestorInterface import IngestorInterface
from QuoteModel import QuoteModel
import pandas as pd


class CSVIngestor(IngestorInterface):

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        extention = path.split('.')[-1]
        return extention in cls.allowed_file_extention()

    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        df = pd.read_csv(path)
        quoteList = []
        for _, row in df.iterrows():
            quoteList.append(QuoteModel(row['body'], row['author']))
        return quoteList
        
    @classmethod
    def allowed_file_extention(cls) -> list[str]:
        return ['csv']


#The project contains a CSVIngestor class.
#The class inherits the IngestorInterface.
#The class depends on the pandas library to complete the defined, abstract method signatures to parse CSV files.
#The parse method returns a valid QuoteModel