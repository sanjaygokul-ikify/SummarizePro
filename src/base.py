from abc import ABC, abstractmethod


class BaseLoader(ABC):
    @abstractmethod
    def load(self) -> str: ...


class BaseSummarizer(ABC):
    @abstractmethod
    def summarize(self, text: str) -> str: ...
