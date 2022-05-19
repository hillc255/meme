from IngestorInterface import IngestorInterface
from QuoteModel import QuoteModel
#from docx.document import Document

class DocxIngestor(IngestorInterface):
    
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        extention = path.split('.')[-1]
        return extention in cls.allowed_file_extention()

    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        return []

    @classmethod
    def allowed_file_extention(cls) -> list[str]:
        return ['doc', 'docx']

#The project contains a DocxIngestor class.
#The class inherits from the IngestorInterface class.
#The class depends on the python-docx library to complete the defined, abstract method signatures to parse DOCX files.
#The parse method returns a valid QuoteModel