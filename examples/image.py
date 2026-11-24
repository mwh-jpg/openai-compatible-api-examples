"""Image generation against an OpenAI-compatible images endpoint."""
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    base_url=os.environ["OPENAI_BASE_URL"],
)


def main() -> None:
    result = client.images.generate(
        model=os.environ.get("IMAGE_MODEL_ID", "your-provider-image-model"),
        prompt="a red freight truck on a mountain road, flat illustration",
        size="1024x1024",
    )
    print(result.data[0].url or "(base64 response)")


if __name__ == "__main__":
    main()
