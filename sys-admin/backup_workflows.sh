#!/bin/bash
# Backs up all critical automation scripts and workflows

TIMESTAMP=$(date +"%Y-%m-%d_%H-%M")
BACKUP_DIR="./backups"
SOURCE_DIRS="./n8n-workflows ./scripts ./marketing-automations"

mkdir -p "$BACKUP_DIR"
ARCHIVE_NAME="$BACKUP_DIR/automation_backup_$TIMESTAMP.tar.gz"

echo "[*] Initiating backup of critical directories..."
tar -czf "$ARCHIVE_NAME" $SOURCE_DIRS

echo "[+] Backup successfully created at $ARCHIVE_NAME"
