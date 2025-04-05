from adapters.file_reader_factory import FileReaderFactory
from adapters.chunker import SimpleChunkStrategy

class FileHandler:
    def __init__(self, chunk_strategy=None):
        self.chunk_strategy= chunk_strategy or SimpleChunkStrategy()

    def process_file(self, file_path: str, chunk_size: int = 500, overlap: int = 50) -> list:
        reader = FileReaderFactory.get_reader(file_path)
        text = reader.read(file_path)
        return self.chunk_strategy.chunk(text, chunk_size, overlap)
