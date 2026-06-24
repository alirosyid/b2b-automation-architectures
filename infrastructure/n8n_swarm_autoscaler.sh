#!/bin/bash
# Dynamically scales n8n worker nodes based on CPU threshold

SERVICE_NAME="n8n_worker"
MAX_REPLICAS=10
CPU_THRESHOLD=80

current_cpu=$(docker stats --no-stream --format "{{.CPUPerc}}" | awk -F'%' '{sum+=$1} END {print sum/NR}')
current_replicas=$(docker service ls --filter name=$SERVICE_NAME --format "{{.Replicas}}" | cut -d'/' -f1)

echo "[Infra] Current N8N Cluster CPU Usage: $current_cpu%"

if (( $(echo "$current_cpu > $CPU_THRESHOLD" | bc -l) )); then
    if [ "$current_replicas" -lt "$MAX_REPLICAS" ]; then
        new_replicas=$((current_replicas + 2))
        echo "[Infra] 📈 Traffic spike detected. Scaling $SERVICE_NAME to $new_replicas replicas."
        docker service scale ${SERVICE_NAME}=${new_replicas}
    else
        echo "[Infra] ⚠️ Max replicas reached. Paging SRE team."
    fi
else
    echo "[Infra] Traffic is stable. No scaling required."
fi
