from .QuoteModel import QuoteModel
from abc import ABC

List = []

class IngestorInterface(ABC):
    
    #helper methods https://docs.python.org/3/library/abc.html
    @abstractmethod
    def can_ingest(cls, path) -> boolean:
        #don't know what this does
        pass

    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        #don't kow what this does
        pass