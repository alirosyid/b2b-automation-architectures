# Incident Response Plan (IRP)

## 1. Definisi Insiden
Setiap kejadian yang menurunkan *throughput* ekstraksi OCR atau memutus antrean webhook n8n selama lebih dari 15 menit.

## 2. Fase Respons (Triage)
1. **Deteksi:** Otomatisasi melalui `alert_escalation.py` via Telegram.
2. **Isolasi:** Mematikan sementara integrasi CRM target untuk mencegah polusi data.
3. **Mitigasi:** Mengalihkan *traffic* LLM ke `HighAvailabilityLLMRouter`.

## 3. Komunikasi Klien
Laporan Insiden (*Post-Mortem*) akan dikirim maksimal 24 jam setelah resolusi, mencakup akar penyebab (*Root Cause*) dan pencegahan di masa depan.
