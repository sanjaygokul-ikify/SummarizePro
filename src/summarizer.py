import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
import numpy as np
class Summarizer:
    def __init__(self, file_path):
        self.file_path = file_path
    def summarize(self):
        with open(self.file_path, 'r') as file:
            text = file.read()
        sentences = sent_tokenize(text)
        word_freq = FreqDist(word.lower() for word in word_tokenize(text))
        max_freq = max(word_freq.values())
        sentence_scores = {}
        for sentence in sentences:
            for word in word_tokenize(sentence.lower()):
                if word in word_freq:
                    sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_freq[word] / max_freq
        summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:5]
        return ' '.join(summary_sentences)
