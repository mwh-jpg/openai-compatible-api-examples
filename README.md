# OpenAI-Compatible API Examples

Minimal, runnable Python snippets for calling chat and image models through any
**OpenAI-compatible** endpoint. Switch providers by changing one environment
variable instead of rewriting the client code.

**AI Model Hub** — <https://94ie.com/> — is one provider this pattern works
with: a single account and one OpenAI-compatible API for chat, image, video,
music and voice models.

## Why this exists

Most model providers expose an OpenAI-compatible `/v1/chat/completions`
surface, but their quickstarts are usually tied to a single vendor. These
examples use the standard `openai` Python package with a configurable
`OPENAI_BASE_URL`, so the same code works across providers. Every file is
standalone and under 40 lines.

## Setup

```bash
pip install openai
cp .env.example .env
# edit .env with your own provider's values
python examples/chat.py
```

> Always check your provider's current documentation for its base URL,
> available model IDs, authentication and rate limits. This repository
> deliberately does not hard-code any provider-specific endpoint or model ID.

## Examples

| File | What it shows |
| --- | --- |
| `examples/chat.py` | streaming chat completion |
| `examples/image.py` | image generation via `client.images.generate` |

## Scope

No framework, no agent loop, no vendor-specific SDK. The goal is a small,
readable reference you can copy into a real project, not a full SDK.

## Links

- AI Model Hub — <https://94ie.com/>
- OpenAI Python SDK — <https://github.com/openai/openai-python>
