#!/bin/bash
# Wraps critical shell executions to prevent n8n workflow silent failures

TARGET_SCRIPT=$1
FALLBACK_WEBHOOK="http://n8n.internal/webhook/error-fallback"

if [ -z "$TARGET_SCRIPT" ]; then
    echo "Usage: ./n8n_shell_failsafe.sh <script_to_run.sh>"
    exit 1
fi

echo "[Infra] Executing $TARGET_SCRIPT with fail-safe wrapper..."

# Run the script and capture exit status
bash "$TARGET_SCRIPT"
EXIT_CODE=$?

if [ $EXIT_CODE -ne 0 ]; then
    echo "[!] Execution Failed (Code: $EXIT_CODE). Triggering fallback webhook."
    curl -X POST -H "Content-Type: application/json" \
         -d "{\"failed_script\": \"$TARGET_SCRIPT\", \"exit_code\": $EXIT_CODE}" \
         $FALLBACK_WEBHOOK
    exit $EXIT_CODE
else
    echo "[+] Execution Successful."
    exit 0
fi
