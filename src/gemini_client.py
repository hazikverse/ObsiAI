import os
from google import genai

# The SDK will read GEMINI_API_KEY or GOOGLE_API_KEY from the environment.
# NEVER hardcode the key in the file or in source control.
# Example: export GEMINI_API_KEY="your_key_here"

def make_client():
    # With google-genai, client picks up API key from GEMINI_API_KEY / GOOGLE_API_KEY env var.
    # See Google Gen AI SDK docs for details.
    return genai.Client()

def generate_text(prompt: str, model: str = "gemini-2.0-flash", max_output_tokens: int = 256):
    """
    Generate text with a Gemini model.
    Note: model names evolve (eg. gemini-2.5-flash etc). Choose the one you need.
    """
    client = make_client()
    # generate_content is one of the SDK calls for text generation
    resp = client.models.generate_content(
        model=model,
        contents=prompt,
        # optional: you can pass other generation params via "temperature", "max_output_tokens", etc.
        max_output_tokens=max_output_tokens
    )
    # resp may include multiple fields; often `resp.text` or `resp.output` contains the text
    return getattr(resp, "text", None) or resp
