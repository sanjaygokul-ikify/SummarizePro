import argparse

from src.file_loader import FileLoader
from src.summarizer import Summarizer


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Summarize a text file.")
    parser.add_argument("--file", type=str, required=True, help="Path to the text file.")
    parser.add_argument(
        "--sentences",
        type=int,
        default=5,
        help="Number of sentences in summary (default: 5).",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    text = FileLoader(file_path=args.file).load()
    summary = Summarizer(num_sentences=args.sentences).summarize(text)
    print(summary)


if __name__ == "__main__":
    main()
