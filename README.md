# QuantoPort API — examples

Minimal, runnable examples for the [QuantoPort](https://quantoport.com) API gateway.

One key, every model — **OpenAI-compatible and Anthropic-compatible endpoints** in front of Claude,
GPT, DeepSeek, Qwen, Kimi, GLM, MiniMax and more.

## Quick start

1. Create an API key in the console: <https://console.quantoport.com>
2. Export it:

   ```bash
   export QP_API_KEY="sk-..."
   ```

3. Run an example:

   | Example | What it does |
   | --- | --- |
   | `examples/curl.sh` | raw HTTP chat completion with curl |
   | `examples/python_openai.py` | OpenAI Python SDK (chat completions) |
   | `examples/python_anthropic.py` | Anthropic Python SDK (messages) |
   | `examples/python_stream.py` | streaming tokens |
   | `examples/node_openai.mjs` | OpenAI Node SDK (ESM) |
   | `examples/models.sh` | list the models your key can use |

## Connection details

| | |
| --- | --- |
| Base URL (OpenAI style) | `https://console.quantoport.com/v1` |
| Auth | `Authorization: Bearer $QP_API_KEY` |
| Auth (Anthropic style) | `x-api-key: $QP_API_KEY` |
| Anthropic base URL | `https://console.quantoport.com` (the SDK appends `/v1/messages`) |

Endpoints:

- `POST /v1/chat/completions` — chat completions (vision models accept `image_url` content parts)
- `POST /v1/messages` — Anthropic Messages API
- `POST /v1/responses` — OpenAI Responses API
- `GET  /v1/models` — models available to your key

Also reachable with the same key (add the endpoint you need, using the model IDs `GET /v1/models` returns):

- `POST /v1/completions`
- `POST /v1/embeddings`
- `POST /v1/rerank`
- `POST /v1/moderations`
- `POST /v1/images/generations`
- `POST /v1/audio/speech`, `POST /v1/audio/transcriptions`, `POST /v1/audio/translations`

Status codes: `400` bad request · `401` missing or invalid key · `403` not permitted for this key ·
`429` rate limited — back off and retry.

## Model IDs

Send the ID exactly as `GET /v1/models` returns it. Commonly used ones:

```
claude-opus-5       claude-sonnet-5      claude-haiku-4.5
gpt-5.5             gpt-5.6-terra        gpt-6-astra
deepseek-v4.1-flash deepseek-v4-pro
qwen3.8-max         qwen3.8-flash        qwen3-vl-plus
kimi-k3             glm-5.3              minimax-m3
```

Availability, context lengths and current pricing live on <https://quantoport.com> and in the
console — this repository deliberately does not hardcode prices.

## Vision example

Any vision-capable model (for example `qwen3-vl-plus` or `qwen/qwen3-vl-plus`) takes the standard
OpenAI-style content parts — confirm the exact ID with `GET /v1/models` first:

```json
POST /v1/chat/completions
{
  "model": "qwen3-vl-plus",
  "messages": [{
    "role": "user",
    "content": [
      {"type": "text", "text": "Describe this image"},
      {"type": "image_url", "image_url": {"url": "https://example.com/photo.jpg"}}
    ]
  }]
}
```

## Support

- Documentation: <https://quantoport.com/docs/>
- Email: support@quantoport.com
- Community: <https://quantoport.com/community/>

## Notes

- Everything reads the key from the `QP_API_KEY` environment variable — never commit a real key.
- `QP_BASE_URL` and `QP_MODEL` override the defaults shown above.
- Python examples only need the official SDKs: `pip install openai anthropic`.
