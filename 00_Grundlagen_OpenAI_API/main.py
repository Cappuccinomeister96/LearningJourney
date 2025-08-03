#!/usr/bin/env python3

from openai import OpenAI
from dotenv import load_dotenv
import os
import tiktoken # Token counting library, if needed - Number of tokens in a text

# Load environment variables from .env file
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# enc = tiktoken.encoding_for_model("gpt-4.1-nano") # 4.1-nano not supported


def main():
    #texts = [
    #    "Sag Hallo Welt!",
    #    "Dies ist ein längerer Text, um Tokenzählung zu demonstrieren. Wie viele Tokens werden verwendet?",
    #    "In der OpenAI-API findest du im Response-Objekt das Feld 'usage', das genaue Zahlen liefert."
    #]

    #for t in texts:
    #    print(f"Text: {t!r}")
    #    print("Tokens:", len(enc.encode(t)))
    #    print("---")

    response = client.responses.create(
        model="gpt-4.1-nano",
        input="Sag Hallo Welt!"
    )

    print(response.output_text)

if __name__ == "__main__":
    main()
