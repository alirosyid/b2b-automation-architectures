# Gunakan image Python ringan sebagai fondasi
FROM python:3.11-slim

# Set direktori kerja di dalam kontainer
WORKDIR /app

# Instal dependensi sistem yang dibutuhkan untuk scraping
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Salin file requirements dan instal dependensi Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh kode aplikasi ke dalam kontainer
COPY . .

# Ekspos port yang digunakan FastAPI
EXPOSE 8000

# Perintah eksekusi saat kontainer dijalankan
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]