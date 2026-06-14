#!/bin/bash
# Sends system status alerts to Discord via Webhook

WEBHOOK_URL="YOUR_DISCORD_WEBHOOK_URL_HERE"
MESSAGE=$1

if [ -z "$MESSAGE" ]; then
    echo "Usage: ./discord_alert.sh 'Message text'"
    exit 1
fi

curl -H "Content-Type: application/json" \
     -d "{\"content\": \"🔔 **Automation Alert:** $MESSAGE\"}" \
     $WEBHOOK_URL

echo "Alert sent to Discord."
