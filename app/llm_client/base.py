from abc import ABC, abstractmethod

class LLMClient(ABC):
    """Abstract class to define an LLM client interface."""

    @abstractmethod
    def generate_text(self, messages, model="default-model", max_tokens=500, temperature=0.7):
        pass