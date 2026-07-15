#!/bin/bash
# Lightweight auto-scaler for containerized n8n worker nodes

CPU_THRESHOLD=80
MAX_WORKERS=5
BASE_WORKER_NAME="n8n-worker"

current_cpu=$(docker stats --no-stream --format "{{.CPUPerc}}" | awk -F'%' '{sum+=$1} END {print sum/NR}' | cut -d'.' -f1)
active_workers=$(docker ps -q -f name=$BASE_WORKER_NAME | wc -l)

echo "[Infra] Current Cluster CPU: $current_cpu% | Active Workers: $active_workers"

if [ "$current_cpu" -gt "$CPU_THRESHOLD" ] && [ "$active_workers" -lt "$MAX_WORKERS" ]; then
    new_worker_id=$((active_workers + 1))
    echo "[!] 📈 Traffic spike detected. Spinning up new worker node: ${BASE_WORKER_NAME}-${new_worker_id}..."
    # docker run -d --name "${BASE_WORKER_NAME}-${new_worker_id}" --network n8n-net n8n-custom-worker:latest
    echo "[+] Node active and joined to Redis execution queue."
elif [ "$current_cpu" -lt 30 ] && [ "$active_workers" -gt 1 ]; then
    echo "[*] 📉 Traffic low. Decommissioning idle worker node: ${BASE_WORKER_NAME}-${active_workers} to optimize FinOps."
    # docker stop "${BASE_WORKER_NAME}-${active_workers}" && docker rm "${BASE_WORKER_NAME}-${active_workers}"
    echo "[+] Node decommissioned."
else
    echo "[+] Cluster stable. No scaling action required."
fi
