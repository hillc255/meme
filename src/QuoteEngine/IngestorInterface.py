from QuoteModel import QuoteModel
from abc import ABC, abstractmethod
from typing import List


class IngestorInterface(ABC):

    #allowed_file_extention: List[str] = []
    
    #strategy  interface helper methods https://docs.python.org/3/library/abc.html
    @classmethod
    @abstractmethod
    def can_ingest(cls, path: str) -> bool:
        pass

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        return []

        
       #return extention in cls.allowed_file_extention

# if __name__ == "__main__":
#     print (type(True))
#     print(type(IngestorInterface.can_ingest("")))

#     #instance = IngestorInterface()
#     pass