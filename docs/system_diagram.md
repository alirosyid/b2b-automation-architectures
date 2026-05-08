# Automation Architecture Flow

```mermaid
graph TD;
    A[Client CRM] -->|Webhook| B(n8n Orchestrator);
    B -->|HTTP Request| C[Python FastAPI];
    C -->|Prompt| D{LLM Gateway};
    D -->|Primary| E[Groq Llama-3];
    D -->|Fallback| F[Gemini 2.5 Flash];
    E --> C;
    F --> C;
    C -->|JSON Payload| B;
    B -->|Enriched Data| G[Target Database];
