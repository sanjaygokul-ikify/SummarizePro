import pytest
from src.file_loader import FileLoader
from src.base import BaseLoader


# --- ABC enforcement ---

def test_base_loader_cannot_be_instantiated():
    with pytest.raises(TypeError):
        BaseLoader()


# --- Fixtures ---

@pytest.fixture
def tmp_file(tmp_path):
    """Helper: write text to a temp file, return its path."""
    def _make(content: str, encoding: str = "utf-8"):
        p = tmp_path / "test.txt"
        p.write_text(content, encoding=encoding)
        return str(p)
    return _make


# --- load() ---

def test_load_returns_correct_text(tmp_file):
    path = tmp_file("Hello world.")
    assert FileLoader(file_path=path).load() == "Hello world."

def test_load_empty_file_returns_empty_string(tmp_file):
    path = tmp_file("")
    assert FileLoader(file_path=path).load() == ""

def test_load_multiline_content_preserved(tmp_file):
    content = "Line one.\nLine two.\nLine three."
    path = tmp_file(content)
    assert FileLoader(file_path=path).load() == content

def test_load_missing_file_raises_file_not_found():
    with pytest.raises(FileNotFoundError):
        FileLoader(file_path="no_such_file.txt").load()

def test_load_custom_encoding_works(tmp_file):
    path = tmp_file("Café résumé", encoding="utf-8")
    result = FileLoader(file_path=path, encoding="utf-8").load()
    assert "Café" in result

def test_load_bad_bytes_no_crash(tmp_path):
    p = tmp_path / "bad.txt"
    p.write_bytes(b"Hello \xff world")
    result = FileLoader(file_path=str(p), errors="replace").load()
    assert "Hello" in result
