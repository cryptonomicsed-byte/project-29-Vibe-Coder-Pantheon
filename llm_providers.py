"""
LLM Provider Abstraction Layer
Supports: OpenAI, Claude, Gemini, Mistral, Groq, Perplexity
"""

import os
import requests
from abc import ABC, abstractmethod

class LLMProvider(ABC):
    """Base class for LLM providers"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
    
    @abstractmethod
    def generate(self, prompt: str, max_tokens: int = 1000) -> str:
        """Generate response from LLM"""
        pass

class OpenAIProvider(LLMProvider):
    """OpenAI GPT-4 / GPT-3.5"""
    
    def generate(self, prompt: str, max_tokens: int = 1000) -> str:
        try:
            import openai
            openai.api_key = self.api_key
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=max_tokens
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"OpenAI Error: {str(e)}"

class ClaudeProvider(LLMProvider):
    """Anthropic Claude 3.5 Sonnet"""
    
    def generate(self, prompt: str, max_tokens: int = 1000) -> str:
        try:
            import anthropic
            
            client = anthropic.Anthropic(api_key=self.api_key)
            message = client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=max_tokens,
                messages=[{"role": "user", "content": prompt}]
            )
            return message.content[0].text
        except Exception as e:
            return f"Claude Error: {str(e)}"

class GeminiProvider(LLMProvider):
    """Google Gemini"""
    
    def generate(self, prompt: str, max_tokens: int = 1000) -> str:
        try:
            import google.generativeai as genai
            
            genai.configure(api_key=self.api_key)
            model = genai.GenerativeModel('gemini-pro')
            
            response = model.generate_content(
                prompt,
                generation_config={
                    'max_output_tokens': max_tokens,
                    'temperature': 0.7
                }
            )
            return response.text
        except Exception as e:
            return f"Gemini Error: {str(e)}"

class MistralProvider(LLMProvider):
    """Mistral AI"""
    
    def generate(self, prompt: str, max_tokens: int = 1000) -> str:
        try:
            from mistralai import Mistral
            
            client = Mistral(api_key=self.api_key)
            response = client.chat.complete(
                model="mistral-large-latest",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=max_tokens
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Mistral Error: {str(e)}"

class GroqProvider(LLMProvider):
    """Groq (fast LLM inference)"""
    
    def generate(self, prompt: str, max_tokens: int = 1000) -> str:
        try:
            from groq import Groq
            
            client = Groq(api_key=self.api_key)
            response = client.chat.completions.create(
                model="mixtral-8x7b-32768",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=max_tokens
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Groq Error: {str(e)}"

class PerplexityProvider(LLMProvider):
    """Perplexity AI (web search + LLM)"""
    
    def generate(self, prompt: str, max_tokens: int = 1000) -> str:
        try:
            from openai import OpenAI
            
            client = OpenAI(
                api_key=self.api_key,
                base_url="https://api.perplexity.ai"
            )
            
            response = client.chat.completions.create(
                model="sonar",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=max_tokens
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Perplexity Error: {str(e)}"

class OllamaProvider(LLMProvider):
    """Local Ollama (self-hosted)"""
    
    def __init__(self, api_key: str, base_url: str = "http://127.0.0.1:11434", model: str = "llama3.1:latest"):
        super().__init__(api_key)
        self.base_url = base_url
        self.model = model
    
    def generate(self, prompt: str, max_tokens: int = 1000) -> str:
        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                    "temperature": 0.7
                },
                timeout=120
            )
            
            if response.status_code == 200:
                return response.json().get("response", "No response")
            else:
                return f"Ollama Error: {response.status_code}"
        except requests.exceptions.Timeout:
            return "Ollama Timeout: Model is slow, try smaller model or increase timeout"
        except Exception as e:
            return f"Ollama Error: {str(e)}"

class CohereProvider(LLMProvider):
    """Cohere API"""
    
    def generate(self, prompt: str, max_tokens: int = 1000) -> str:
        try:
            import cohere
            
            client = cohere.ClientV2(api_key=self.api_key)
            response = client.chat(
                model="command-r-plus",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens
            )
            return response.message.content[0].text
        except Exception as e:
            return f"Cohere Error: {str(e)}"

# Provider factory
PROVIDERS = {
    'openai': OpenAIProvider,
    'claude': ClaudeProvider,
    'gemini': GeminiProvider,
    'mistral': MistralProvider,
    'groq': GroqProvider,
    'perplexity': PerplexityProvider,
    'ollama': OllamaProvider,
    'cohere': CohereProvider,
}

def get_provider(provider_name: str, api_key: str, **kwargs) -> LLMProvider:
    """Factory function to get LLM provider"""
    
    provider_name = provider_name.lower()
    
    if provider_name not in PROVIDERS:
        raise ValueError(f"Unknown provider: {provider_name}. Available: {list(PROVIDERS.keys())}")
    
    ProviderClass = PROVIDERS[provider_name]
    
    if provider_name == 'ollama':
        return ProviderClass(api_key, **kwargs)
    else:
        return ProviderClass(api_key)

if __name__ == "__main__":
    # Test providers
    print("Available LLM Providers:")
    for name in PROVIDERS.keys():
        print(f"  • {name}")
