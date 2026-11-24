"""Streaming chat completion against any OpenAI-compatible endpoint."""
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    base_url=os.environ["OPENAI_BASE_URL"],
)
MODEL = os.environ.get("MODEL_ID", "your-provider-model-id")


def main() -> None:
    stream = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": "Say hello in one sentence."}],
        stream=True,
    )
    for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="", flush=True)
    print()


if __name__ == "__main__":
    main()
