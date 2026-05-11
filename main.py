from summarizer import Summarizer
import argparse
parser = argparse.ArgumentParser(description='Summarize a text file.')
parser.add_argument('--file', type=str, help='Path to the text file.')
args = parser.parse_args()
summarizer = Summarizer(file_path=args.file)
print(summarizer.summarize())
