#!/bin/bash
# Generates workspace for new automation clients

CLIENT_NAME=$1

if [ -z "$CLIENT_NAME" ]; then
    echo "Error: Please provide a client name."
    exit 1
fi

BASE_DIR="./clients/$CLIENT_NAME"
mkdir -p "$BASE_DIR"/{contracts,invoices,workflows,assets,reports}
touch "$BASE_DIR/README.md"

echo "# $CLIENT_NAME - Automation Hub" > "$BASE_DIR/README.md"
echo "[+] Workspace successfully generated for $CLIENT_NAME"
