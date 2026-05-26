# ⚡ Enterprise B2B AI Automation Gateway & Architectures

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-00a393.svg)](https://fastapi.tiangolo.com/)
[![n8n](https://img.shields.io/badge/n8n-Workflow_Automation-FF6D5A.svg)](https://n8n.io/)
[![Groq](https://img.shields.io/badge/Groq-Llama_3-f55036.svg)](https://groq.com/)

Welcome to my portfolio of production-ready automation pipelines and AI agents. By decoupling the orchestration layer (n8n) from the cognitive execution layer (FastAPI + LLMs), this repository demonstrates high-impact architectures designed to eliminate manual bottlenecks, bypass platform execution limits, mitigate hallucination risks, and scale B2B operations safely.

---

## 🧠 Core Architecture: The Decoupled Gateway

A common anti-pattern in automation is tightly coupling LLM API calls directly inside orchestration nodes, leading to rate-limit failures and broken JSON schemas. This architecture utilizes a **Single Unified FastAPI Gateway (`main.py`)** to handle diverse AI cognitive loads as containerized microservices.

### Native Stateful Routing
The n8n orchestrator is strictly reserved for data routing, HTTP requests, and state management. It employs a JavaScript-based memory system to track previously processed URLs and Payload IDs, ensuring a fully stateful architecture that prevents duplicate executions across multiple cron triggers.

```mermaid
graph TD
    A[Incoming Trigger <br> Webhook / Cron / APIs] --> B(Raw Data Aggregation)
    B --> C{n8n Orchestrator <br> Stateful Memory Router}
    
    C -- HTTP POST JSON --> D[FastAPI Gateway <br> Port: 8000]
    
    subgraph Python Microservices (main.py)
        D --> E[/enrich <br> Groq Llama-3/]
        D --> F[/generate_reply <br> Contextual RAG/]
        D --> G[/ocr <br> Gemini 2.5 Flash/]
    end
    
    E -- Validated JSON --> C
    F -- Validated JSON --> C
    G -- Validated JSON --> C
    
    C -- Native JS Injection --> H((Target Output <br> Resend / Telegram / CRM))
```

---

## 📐 Engineering Philosophy: The 6-Component Prompt Framework

To guarantee deterministic, production-safe outputs from probabilistic models, every microservice within this gateway utilizes a rigorous 6-component prompt architecture. This prevents "bot-like" text and ensures 100% JSON compliance:

1. **Role:** Defining the precise expert persona (e.g., *World-class B2B IT Automation Architect*).
2. **Task:** The exact operational goal.
3. **Input:** Dynamic payload injection.
4. **Output:** Strict structural requirements (e.g., *Pure JSON ONLY*).
5. **Constraints:** Immutable rules (e.g., *Preserve exact capitalization for IT acronyms like AWS/LLM*).
6. **Capabilities:** Specific analytical boundaries to prevent hallucination.

---

## 💼 Portfolio Use Cases

| Module | The Operational Bottleneck | The Decoupled AI Solution |
| :--- | :--- | :--- |
| **🎯 The Sniper (B2B Lead Enrichment)** | Sales teams waste 60% of their day manually researching prospect bottlenecks before cold emailing. | The n8n pipeline scrapes platforms automatically. The FastAPI `/enrich` endpoint forces Llama-3 to identify exactly 3 critical business bottlenecks, outputting pure JSON. Native JS in n8n then seamlessly injects this data into plain-text HTML for highly personalized outreach at scale. |
| **🛡️ The Defender (Enterprise RAG)** | Support agents answer repetitive technical queries, while traditional AI chatbots hallucinate facts and frustrate clients. | A context-aware agent intercepts client emails. The `/generate_reply` endpoint queries a local knowledge base and drafts a highly authoritative, Senior Architect-level reply in seconds for human review. |
| **📄 The Extractor (AI-Powered OCR)** | Finance teams waste hundreds of hours manually typing physical invoices into spreadsheets, leading to human error. | A visual extraction pipeline routes physical invoice PDFs through the Gateway to Google's Gemini 2.5 Flash vision model, extracting perfect, structured JSON data in under 3 seconds with near-perfect accuracy. |

---

## 🚀 How to Deploy (For Developers)

### 1. Launch the Unified Cognitive Gateway (FastAPI)

Navigate to the project directory containing `main.py` and install the required dependencies:

```bash
pip install fastapi uvicorn google-generativeai groq python-dotenv pydantic requests bs4
```

Create a `.env` file in the root directory and add your API credentials:

```bash
GROQ_API_KEY=your_groq_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

Launch the monolithic server locally:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 2. Orchestration Setup (n8n)
* Import the desired JSON workflows from the `/n8n-workflows` directory into your n8n instance.
* Ensure all internal `HTTP Request` nodes in n8n are pointing to the local gateway: `http://localhost:8000/{endpoint}`.
* Activate the workflow triggers.

---
*Architected by Ali Rosyid.*
