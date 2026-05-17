import pytest
from src.summarizer import Summarizer
from src.base import BaseSummarizer

SAMPLE = (
    "Natural language processing is a subfield of linguistics and AI. "
    "It gives computers the ability to understand text and spoken words. "
    "Summarization produces a shorter version of a document. "
    "Extractive methods select key sentences directly from the source. "
    "Frequency-based scoring weights sentences by word importance. "
    "The most frequent words tend to carry the most meaning. "
    "NLTK provides tools for tokenization, tagging, and parsing. "
    "Python is widely used in data science and machine learning. "
    "Good summaries capture main ideas without losing key information. "
    "This tool uses a simple but effective frequency-based approach."
)


# --- ABC enforcement ---

def test_base_summarizer_cannot_be_instantiated():
    with pytest.raises(TypeError):
        BaseSummarizer()


# --- summarize() ---

def test_summarize_returns_str():
    assert isinstance(Summarizer().summarize(SAMPLE), str)

def test_summarize_empty_text_returns_empty():
    assert Summarizer().summarize("") == ""

def test_summarize_whitespace_only_returns_empty():
    assert Summarizer().summarize("   \n\t  ") == ""

def test_summarize_valid_text_returns_nonempty():
    assert len(Summarizer().summarize(SAMPLE)) > 0

def test_default_num_sentences_is_five():
    assert Summarizer().num_sentences == 5

def test_num_sentences_param_respected():
    result = Summarizer(num_sentences=2).summarize(SAMPLE)
    output_sentences = [s.strip() for s in result.split(".") if s.strip()]
    assert len(output_sentences) <= 2

def test_output_is_extractive():
    """All output sentences must appear verbatim in the source."""
    result = Summarizer().summarize(SAMPLE)
    assert result in SAMPLE or all(s in SAMPLE for s in result.split(". ") if s)

def test_single_sentence_no_crash():
    result = Summarizer().summarize("This is a single sentence.")
    assert isinstance(result, str)


# --- _tokenize() ---

def test_tokenize_returns_list():
    tokens = Summarizer()._tokenize("Hello World")
    assert isinstance(tokens, list)

def test_tokenize_lowercases_all():
    tokens = Summarizer()._tokenize("Hello WORLD Foo")
    assert all(t == t.lower() for t in tokens)

def test_tokenize_nonempty_for_real_text():
    tokens = Summarizer()._tokenize(SAMPLE)
    assert len(tokens) > 0


# --- _build_freq_dist() ---

def test_build_freq_dist_returns_dict():
    tokens = Summarizer()._tokenize(SAMPLE)
    freq = Summarizer()._build_freq_dist(tokens)
    assert isinstance(freq, dict)

def test_build_freq_dist_max_normalized_to_one():
    tokens = Summarizer()._tokenize(SAMPLE)
    freq = Summarizer()._build_freq_dist(tokens)
    assert max(freq.values()) == pytest.approx(1.0)

def test_build_freq_dist_all_values_positive():
    tokens = Summarizer()._tokenize(SAMPLE)
    freq = Summarizer()._build_freq_dist(tokens)
    assert all(v > 0 for v in freq.values())


# --- _score_sentences() ---

def test_score_sentences_returns_dict():
    s = Summarizer()
    tokens = s._tokenize(SAMPLE)
    freq = s._build_freq_dist(tokens)
    scores = s._score_sentences(["NLP is great.", "Python is used in AI."], freq)
    assert isinstance(scores, dict)

def test_score_sentences_values_positive():
    s = Summarizer()
    tokens = s._tokenize(SAMPLE)
    freq = s._build_freq_dist(tokens)
    scores = s._score_sentences(
        ["Natural language processing is a subfield of linguistics and AI."], freq
    )
    assert all(v > 0 for v in scores.values())
