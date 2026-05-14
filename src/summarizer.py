import nltk
import numpy as np
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist

from src.base import BaseSummarizer

# Download punkt_tab once on first import
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab', quiet=True)


class Summarizer(BaseSummarizer):
    def __init__(self, num_sentences: int = 5) -> None:
        self.num_sentences = num_sentences

    def summarize(self, text: str) -> str:
        if not text or not text.strip():
            return ""
        sentences = sent_tokenize(text)
        tokens = self._tokenize(text)
        freq = self._build_freq_dist(tokens)
        scores = self._score_sentences(sentences, freq)
        top = sorted(scores, key=scores.get, reverse=True)[: self.num_sentences]
        return " ".join(top)

    def _tokenize(self, text: str) -> list:
        return [word.lower() for word in word_tokenize(text)]

    def _build_freq_dist(self, tokens: list) -> dict:
        freq_dist = FreqDist(tokens)
        max_freq = max(freq_dist.values())
        return {word: count / max_freq for word, count in freq_dist.items()}

    def _score_sentences(self, sentences: list, freq: dict) -> dict:
        scores = {}
        for sentence in sentences:
            for word in self._tokenize(sentence):
                if word in freq:
                    scores[sentence] = scores.get(sentence, 0.0) + freq[word]
        return scores
