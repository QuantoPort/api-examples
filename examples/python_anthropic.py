"""Anthropic Messages API against the QuantoPort gateway.

    pip install anthropic
    export QP_API_KEY="sk-..."
    python python_anthropic.py
"""

import os

from anthropic import Anthropic

base = os.environ.get("QP_BASE_URL", "https://console.quantoport.com/v1")
# The Anthropic SDK appends /v1/messages itself, so pass the origin without the /v1 suffix.
base = base[: -len("/v1")] if base.endswith("/v1") else base

client = Anthropic(api_key=os.environ["QP_API_KEY"], base_url=base)
# Sends x-api-key; the gateway accepts that header as well as Authorization: Bearer.

msg = client.messages.create(
    model=os.environ.get("QP_MODEL", "claude-sonnet-5"),
    max_tokens=256,
    messages=[{"role": "user", "content": "Say hello in five words."}],
)

for block in msg.content:
    if block.type == "text":
        print(block.text)
