#!/usr/bin/env bash
# List the models your key can use.
#
#   export QP_API_KEY="sk-..."
#   ./models.sh
set -euo pipefail

BASE="${QP_BASE_URL:-https://console.quantoport.com/v1}"
: "${QP_API_KEY:?QP_API_KEY is required - create a key at https://console.quantoport.com}"

curl -sS "${BASE}/models" -H "Authorization: Bearer ${QP_API_KEY}"
