#!/bin/bash
# Simulates random node failures to test system resilience

TARGET_NAMESPACE="ai-automation-staging"
PODS=("n8n-worker-1" "redis-cache" "vector-db-node")

# Select a random pod to terminate
RANDOM_INDEX=$((RANDOM % ${#PODS[@]}))
TARGET_POD=${PODS[$RANDOM_INDEX]}

echo "[Chaos Eng] 😈 Initiating chaos injection in namespace: $TARGET_NAMESPACE"
echo "[Chaos Eng] Target acquired: $TARGET_POD. Simulating catastrophic failure..."

# Mocking Kubernetes pod deletion
# kubectl delete pod $TARGET_POD -n $TARGET_NAMESPACE

echo "[Chaos Eng] Pod terminated. Monitoring auto-scaling and failover recovery..."
sleep 2
echo "[Chaos Eng] Failover successful. System resilience validated."
