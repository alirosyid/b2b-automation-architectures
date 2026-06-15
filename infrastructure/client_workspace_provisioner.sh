#!/bin/bash
set -e

CLIENT_ID=$1
if [ -z "$CLIENT_ID" ]; then
  echo "[Error] Client ID is required for workspace provisioning."
  exit 1
fi

BASE_DIR="./client_templates/$CLIENT_ID"
mkdir -p "$BASE_DIR"/{n8n_data,config,logs,vault}

cat <<EOF > "$BASE_DIR/docker-compose.yml"
version: '3.8'
services:
  n8n-$CLIENT_ID:
    image: n8nio/n8n:latest
    environment:
      - N8N_HOST=n8n.$CLIENT_ID.internal
      - WEBHOOK_URL=https://api.gateway.com/$CLIENT_ID/webhook
    volumes:
      - ./n8n_data:/home/node/.n8n
EOF

echo "[Business Ops] Zero-touch provisioning complete for $CLIENT_ID."
