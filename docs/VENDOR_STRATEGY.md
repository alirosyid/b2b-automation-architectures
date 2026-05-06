# 🛡️ Vendor Lock-In Mitigation Strategy

## 1. Orchestration Layer (n8n)
Semua logika bisnis tingkat lanjut **TIDAK** disimpan di dalam node n8n. Logika diekstrak ke dalam layanan mikro Python. Jika migrasi diperlukan (ke Make.com atau custom script), n8n dapat diganti hanya dalam waktu 48 jam.

## 2. LLM Engine (Groq / Gemini)
Sistem menggunakan `HighAvailabilityLLMRouter`. Kami tidak menggunakan SDK spesifik vendor untuk logika inti, melainkan wrapper standar. Berpindah dari Llama-3 ke model GPT-4 atau Claude dapat dilakukan hanya dengan mengubah variabel lingkungan (.env).

## 3. Database
Sistem ini sepenuhnya *database-agnostic* melalui penggunaan ORM standar.
