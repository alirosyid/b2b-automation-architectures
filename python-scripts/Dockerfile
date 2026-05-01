# Gunakan image Python yang ringan untuk performa server
FROM python:3.10-slim

# Set direktori kerja di dalam container
WORKDIR /app

# Salin file dependensi yang kemarin kita rapikan
COPY requirements.txt .

# Install semua pustaka tanpa menyimpan cache agar ukuran container kecil
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh skrip utilitas dan API ke dalam container
COPY . .

# Ekspos port standar FastAPI
EXPOSE 8000

# Perintah default untuk menjalankan server OCR/RAG
CMD ["uvicorn", "gemini_vision_ocr_api:app", "--host", "0.0.0.0", "--port", "8000"]
