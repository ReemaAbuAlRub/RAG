from abc import ABC, abstractmethod

class FileReader(ABC):
    @abstractmethod
    def read(self, file_path: str) -> str:
        """Extract and return text from the file."""
        pass

class PDFReader(FileReader):
    def read(self, file_path: str) -> str:
        import PyPDF2
        text = ""
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text

class TXTReader(FileReader):
    def read(self, file_path: str) -> str:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

class DOCXReader(FileReader):
    def read(self, file_path: str) -> str:
        import docx
        doc = docx.Document(file_path)
        paragraphs = [para.text for para in doc.paragraphs]
        return "\n".join(paragraphs)
