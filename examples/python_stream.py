"""Streaming chat completion.

    pip install openai
    export QP_API_KEY="sk-..."
    python python_stream.py
"""

import os

from openai import OpenAI

client = OpenAI(
    api_key=os.environ["QP_API_KEY"],
    base_url=os.environ.get("QP_BASE_URL", "https://console.quantoport.com/v1"),
)

stream = client.chat.completions.create(
    model=os.environ.get("QP_MODEL", "deepseek-v4.1-flash"),
    messages=[{"role": "user", "content": "Count from 1 to 10, one number per line."}],
    stream=True,
)

for chunk in stream:
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)
print()
