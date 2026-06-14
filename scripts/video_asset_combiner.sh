#!/bin/bash
# Automatically aligns video, audio, and thumbnails for processing

VIDEO_DIR="./assets/videos"
AUDIO_DIR="./assets/audio"
OUTPUT_DIR="./ready_to_upload"

mkdir -p "$OUTPUT_DIR"

echo "[*] Scanning for assets to combine..."
for video in "$VIDEO_DIR"/*.mp4; do
    filename=$(basename -- "$video")
    name="${filename%.*}"
    
    if [ -f "$AUDIO_DIR/$name.wav" ]; then
        echo "[+] Match found for $name. Moving to processing queue..."
        # FFMPEG combination logic would go here
        cp "$video" "$OUTPUT_DIR/"
    fi
done
echo "[*] Automation complete."
