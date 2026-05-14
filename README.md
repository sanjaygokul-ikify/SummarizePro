# SummarizePro
A Python-based library for efficient text summarization of large documents.

## Installation
```bash
pip install -r requirements.txt
```
## Usage
```python
from src.file_loader import FileLoader
from src.summarizer import Summarizer

text = FileLoader(file_path='example.txt').load()
print(Summarizer(num_sentences=5).summarize(text))
```
## Architecture
```mermaid
graph LR
A[Text File] -->|Read| B[Summarizer]
B -->|Summarize| C[Summary]
C -->|Output| D[Console]
```
## Project Structure
```
SummarizePro/
|---- src/
|       |---- __init__.py
|       |---- base.py
|       |---- file_loader.py
|       |---- summarizer.py
|---- main.py
|---- requirements.txt
|---- README.md
```
## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to this project.
