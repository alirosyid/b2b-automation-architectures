#!/bin/bash
# Catatan: Pastikan Anda memberikan hak akses eksekusi di Linux/Docker:
# chmod +x start_api.sh

echo "🚀 Memulai server FastAPI AI Microservices..."
cd ../python-scripts
uvicorn gemini_vision_ocr_api:app --host 0.0.0.0 --port 8000
