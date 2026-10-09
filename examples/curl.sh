#!/usr/bin/env bash
# Raw HTTP chat completion against the QuantoPort gateway.
#
#   export QP_API_KEY="sk-..."
#   ./curl.sh
set -euo pipefail

BASE="${QP_BASE_URL:-https://console.quantoport.com/v1}"
MODEL="${QP_MODEL:-deepseek-v4.1-flash}"
: "${QP_API_KEY:?QP_API_KEY is required - create a key at https://console.quantoport.com}"

curl -sS "${BASE}/chat/completions" \
  -H "Authorization: Bearer ${QP_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "{
    \"model\": \"${MODEL}\",
    \"messages\": [
      {\"role\": \"user\", \"content\": \"Reply with one short sentence: what is an API gateway?\"}
    ]
  }"
