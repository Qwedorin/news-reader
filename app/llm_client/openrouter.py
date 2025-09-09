import requests
from app.llm_client.base import LLMClient

class OpenRouterAPIWrapper(LLMClient):
    """Wrapper for the OpenRouter API."""
    BASE_URL = "https://openrouter.ai/api/v1"

    def __init__(self, api_key):
        self.api_key = api_key

    def generate_text(self, messages, model="meta-llama/llama-3.3-70b-instruct:free", max_tokens=500, temperature=0.7):
        """
        Generate text using the OpenRouter API.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content' keys
            model: The model to use (default: "meta-llama/llama-3.3-70b-instruct:free")
            max_tokens: Maximum number of tokens to generate
            temperature: Temperature for generation (higher = more random)
            
        Returns:
            Generated text as a string
        """
        url = f"{self.BASE_URL}/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://webtracker-backend",  # Required by OpenRouter
            "X-Title": "WebTracker Backend"  # Optional but recommended
        }
        
        payload = {
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature
        }

        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
        else:
            raise Exception(f"OpenRouter API Error: {response.status_code} {response.text}")
