import logging
from docling.document_converter import DocumentConverter

logger = logging.getLogger(__name__)

class DoclingEnterpriseParser:
    """
    Enterprise Document Ingestion Engine.
    Leverages IBM's Docling framework to parse highly complex B2B PDF documents 
    (including nested tables and multi-column layouts) into pristine Markdown 
    suitable for RAG context windows.
    """
    def __init__(self):
        self.converter = DocumentConverter()

    def parse_document(self, file_path: str) -> str:
        logger.info(f"Initializing Docling PDF conversion for {file_path}...")
        
        try:
            result = self.converter.convert(file_path)
            markdown_output = result.document.export_to_markdown()
            
            logger.info("Document successfully parsed into structural Markdown.")
            return markdown_output
            
        except Exception as e:
            logger.error(f"Docling conversion failed: {e}")
            raise ValueError("Unable to parse enterprise document.")
