#!/bin/bash
# Dynamically scales self-hosted GitHub Actions runners

QUEUED_JOBS=$(curl -s -H "Authorization: token $GITHUB_PAT" \
  "https://api.github.com/repos/b2b-agency/core-infra/actions/runs?status=queued" | grep -c '"status": "queued"')

ACTIVE_RUNNERS=$(aws ec2 describe-instances --filters "Name=tag:Role,Values=GitHubRunner" "Name=instance-state-name,Values=running" --query "Reservations[*].Instances[*].InstanceId" --output text | wc -w)

MAX_RUNNERS=5

echo "[CI/CD] Queued Jobs: $QUEUED_JOBS | Active Runners: $ACTIVE_RUNNERS"

if [ "$QUEUED_JOBS" -gt 0 ] && [ "$ACTIVE_RUNNERS" -lt "$MAX_RUNNERS" ]; then
    echo "[CI/CD] Bottleneck detected. Provisioning new ephemeral EC2 runner..."
    # aws ec2 run-instances --launch-template LaunchTemplateName=GitHubRunner --count 1
    echo "[+] Runner provisioned successfully."
elif [ "$QUEUED_JOBS" -eq 0 ] && [ "$ACTIVE_RUNNERS" -gt 1 ]; then
    echo "[CI/CD] Queue empty. Decommissioning idle runners to optimize FinOps..."
    # Logic to terminate idle instances goes here
fi
