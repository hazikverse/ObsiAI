import os
from src.gemini_client import generate_text

def main():
    # Ensure environment variable is set (example)
    if not os.getenv("AIzaSyBwag8gx-3cIFxyS3CF_vztf314pNw3LCA") and not os.getenv("AIzaSyBwag8gx-3cIFxyS3CF_vztf314pNw3LCA"):
        print("Set GEMINI_API_KEY or GOOGLE_API_KEY first.")
        return

    prompt = "Write a short README intro for a Python GitHub repo that calls Gemini 2.0."
    out = generate_text(prompt, model="gemini-2.0-flash", max_output_tokens=200)
    print("=== Model output ===")
    print(out)

if __name__ == "__main__":
    main()
