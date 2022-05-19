from IngestorInterface import IngestorInterface
from QuoteModel import QuoteModel

class PDFIngestor(IngestorInterface):

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        extention = path.split('.')[-1]
        return extention in cls.allowed_file_extention()

    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        return []

    @classmethod
    def allowed_file_extention(cls) -> list[str]:
        return ['pdf']
    
#The project contains a PDFIngestor class.
#The PDFIngestor class inherits from the IngestorInterface class.
#The PDFIngestor class utilizes the subprocess module to call the pdftotext CLI utility—creating a pipeline that converts PDFs to text and then ingests the text.
#The class handles deleting temporary files.
#The parse method returns a valid QuoteModel
#NOTE: Do not use the pdftotext PIP Library - we'd like you to demonstrate your understanding of the subprocess module.