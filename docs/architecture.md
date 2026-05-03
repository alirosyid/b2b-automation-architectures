# 🏛️ System Architecture Overview

This system utilizes a distributed topology:

1. **Orchestrator:** n8n handles triggers, webhooks, and state management.
2. **AI Workers:** Python (FastAPI) microservices invoked by n8n for heavy-compute tasks (OCR via Gemini Vision, dynamic extraction via Llama-3).
3. **Storage:** Target destination nodes (Google Sheets, internal databases) accessed via secure credentials.

*Detailed node logic diagrams pending.*
