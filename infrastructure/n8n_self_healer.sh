#!/bin/bash
# Monitors critical n8n webhook ingress and auto-restarts on failure

WEBHOOK_URL="http://n8n.internal/webhook-test/health"
CONTAINER_NAME="n8n_production"
MAX_RETRIES=3

check_health() {
    HTTP_STATUS=$(curl -o /dev/null -s -w "%{http_code}\n" "$WEBHOOK_URL")
    if [ "$HTTP_STATUS" -eq 200 ]; then
        echo "[Infra] N8N Webhook is healthy (200 OK)."
        return 0
    else
        echo "[Infra] N8N Webhook failed with status $HTTP_STATUS."
        return 1
    fi
}

FAILURES=0
for i in $(seq 1 $MAX_RETRIES); do
    if ! check_health; then
        ((FAILURES++))
        sleep 5
    else
        exit 0
    fi
done

if [ "$FAILURES" -eq "$MAX_RETRIES" ]; then
    echo "[Infra] CRITICAL: Webhook unresponsive. Initiating self-healing restart sequence..."
    docker restart "$CONTAINER_NAME"
    echo "[Infra] Container $CONTAINER_NAME restarted successfully."
fi
