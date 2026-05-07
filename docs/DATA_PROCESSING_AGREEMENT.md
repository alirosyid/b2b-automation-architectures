# Data Processing Agreement (DPA) Summary

Sistem otomatisasi ini mematuhi standar pemrosesan data B2B internasional:

1. **Data in Transit:** Semua *payload* webhook n8n dienkripsi menggunakan TLS 1.3.
2. **Data at Rest:** Layanan mikro Python tidak menyimpan data *Personally Identifiable Information* (PII) secara permanen. Data hanya ada di memori selama pemrosesan (OCR/Enrichment) dan langsung dihapus setelah dikirim ke CRM tujuan.
3. **AI Vendor Policy:** API LLM (Groq/Gemini) dikonfigurasi dengan kebijakan *Zero Data Retention* (data klien tidak digunakan untuk melatih model mereka).
