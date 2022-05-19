from IngestorInterface import IngestorInterface
from QuoteModel import QuoteModel

class TextIngestor(IngestorInterface):
    
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        extention = path.split('.')[-1]
        return extention in cls.allowed_file_extention()

    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        return []

    @classmethod
    def allowed_file_extention(cls) -> list[str]:
        return ['txt']

#The project contains a TextIngestor class.
#The class inherits the IngestorInterface.
#The class does not depend on any 3rd party library to complete the defined, abstract method signatures to parse Text files.
#The parse method returns a valid QuoteModel