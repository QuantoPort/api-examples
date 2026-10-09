"""Chat completion with the OpenAI Python SDK against the QuantoPort gateway.

    pip install openai
    export QP_API_KEY="sk-..."
    python python_openai.py
"""

import os

from openai import OpenAI

client = OpenAI(
    api_key=os.environ["QP_API_KEY"],
    # The OpenAI SDK appends /chat/completions, so the /v1 must be part of the base URL.
    base_url=os.environ.get("QP_BASE_URL", "https://console.quantoport.com/v1"),
)

resp = client.chat.completions.create(
    model=os.environ.get("QP_MODEL", "deepseek-v4.1-flash"),
    messages=[{"role": "user", "content": "Say hello in five words."}],
)

print(resp.choices[0].message.content)
