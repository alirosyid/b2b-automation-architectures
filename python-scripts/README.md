# 🐍 Python AI Microservices

Layanan mikro berbasis FastAPI untuk menangani tugas spesifik seperti OCR dan RAG yang dipanggil oleh n8n.

**Menjalankan Server Lokal:**
```bash
pip install -r requirements.txt
uvicorn gemini_vision_ocr_api:app --reload --port 8000
