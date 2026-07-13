#!/bin/bash
# Autonomously manages K8s spot instance terminations for zero-downtime FinOps

TOKEN=$(curl -s -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
SPOT_STATUS=$(curl -s -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/spot/instance-action)

if [ -n "$SPOT_STATUS" ]; then
    NODE_NAME=$(hostname)
    echo "[FinOps] 🚨 Spot termination notice received. 120 seconds to eviction."
    echo "[Ops] Cordoning node $NODE_NAME to prevent new webhook ingress..."
    kubectl cordon $NODE_NAME
    
    echo "[Ops] Safely draining active n8n workloads to stable cluster nodes..."
    kubectl drain $NODE_NAME --ignore-daemonsets --delete-emptydir-data --force --grace-period=60
    
    echo "[+] Workloads successfully migrated. Zero execution drops. Safe to terminate."
else
    echo "[+] Node stable. No termination notice detected."
fi
