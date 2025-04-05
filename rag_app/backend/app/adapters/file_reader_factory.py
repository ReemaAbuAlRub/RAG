import os
from file_handler.file_reader import PDFReader, TXTReader, DOCXReader

class FileReaderFactory:
    @staticmethod
    def get_reader(file_path: str):
        extension = os.path.splitext(file_path)[1].lower()
        if extension == ".pdf":
            return PDFReader()
        elif extension == ".txt":
            return TXTReader()
        elif extension == ".docx":
            return DOCXReader()
        else:
            raise ValueError(f"Unsupported file type: {extension}")
