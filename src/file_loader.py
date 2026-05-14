from src.base import BaseLoader


class FileLoader(BaseLoader):
    def __init__(self, file_path: str, encoding: str = "utf-8", errors: str = "replace") -> None:
        self.file_path = file_path
        self.encoding = encoding
        self.errors = errors

    def load(self) -> str:
        with open(self.file_path, "r", encoding=self.encoding, errors=self.errors) as fh:
            return fh.read()
