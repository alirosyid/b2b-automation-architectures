# ⚡ Enterprise B2B AI Automation Gateway & Architectures

Welcome to my portfolio of production-ready automation pipelines and AI agents. 
By separating the orchestration layer (n8n) from the cognitive layer (FastAPI + LLMs), this repository contains high-impact workflows designed to eliminate manual bottlenecks, bypass platform execution limits, and scale B2B operations.

---

## 🧠 Core Architecture: The AI Gateway (Frame Control)
Instead of running multiple heavy scripts, this architecture utilizes a single unified FastAPI Gateway (`main.py`) to handle diverse AI cognitive loads as microservices.

```mermaid
graph TD
    %% Styling
    classDef client fill:#f9f9f9,stroke:#333,stroke-width:2px;
    classDef orchestrator fill:#ff9900,stroke:#fff,stroke-width:2px,color:#fff;
    classDef gateway fill:#2b5e82,stroke:#fff,stroke-width:2px,color:#fff;
    classDef ai fill:#10a37f,stroke:#fff,stroke-width:2px,color:#fff;
    classDef output fill:#0088cc,stroke:#fff,stroke-width:2px,color:#fff;

    A[Incoming Trigger <br/> 📧 Email / 📊 Sheets / 📄 PDF]:::client -->|Raw Data| B{n8n Orchestrator}:::orchestrator
    
    B -->|HTTP POST JSON| C[FastAPI Gateway <br/> Port: 8000]:::gateway
    
    subgraph Cognitive Layer [Python Microservices: main.py]
        C -->|/enrich| D(Lead Enrichment Engine):::gateway
        C -->|/generate_reply| E(RAG Contextual Bot):::gateway
        C -->|/ocr_invoice| H(Gemini Vision Engine):::gateway
    end
    
    D -->|Strict JSON Prompt| F((Groq LLaMA-3.3)):::ai
    E -->|Read knowledge_base.txt| F
    H -->|Vision Parsing| I((Gemini 2.5 Flash)):::ai
    
    F -->|Validated JSON Response| C
    I -->|Validated JSON Response| C
    
    C -->|Return Payload| B
    
    B -->|Async Dispatch| G[Target Output <br/> 📱 Telegram / 📧 Resend / 🗄️ CRM]:::output

📑 Portfolio Use Cases
🏗️ 1. Automating B2B Lead Enrichment (The Sniper)
The Problem: Sales teams waste 60% of their day manually researching prospect bottlenecks before cold emailing.
The AI Solution: Feed a basic list of company domains, and the n8n pipeline automatically scrapes the websites. The main.py Gateway (/enrich endpoint) forces LLaMA-3 to identify exactly 3 critical business bottlenecks, outputting pure JSON for highly personalized outreach at scale.

🏗️ 2. Enterprise RAG Customer Support (The Defender)
The Problem: Support agents answer repetitive technical queries, while traditional AI chatbots hallucinate facts and frustrate enterprise clients.
The AI Solution: A context-aware RAG agent that intercepts incoming client emails. The Gateway (/generate_reply endpoint) queries the local knowledge_base.txt and drafts a highly authoritative, Senior Architect-level reply for the CTO within seconds, sending the draft directly to Telegram for review.

🏗️ 3. AI-Powered OCR & Invoice Data Extraction
The Problem: Finance teams waste hundreds of hours manually typing physical invoices into spreadsheets, leading to human error.
The AI Solution: A visual extraction pipeline receiving physical invoice PDFs. It routes through the Gateway to Google's Gemini 2.5 Flash vision model, extracting perfect JSON data (Vendor, Line Items, Totals) in under 3 seconds with 99% accuracy.

🎥 Workflow Demonstrations
B2B Automated Outreach Pipeline: View Technical Demonstration (Loom) - End-to-end execution of data extraction and dynamic personalization via Groq, orchestrated in n8n.

🛠️ How to Deploy (For Developers)
1. Run the Unified Cognitive Gateway (FastAPI)

Navigate to the project directory containing main.py.

Install dependencies: pip install fastapi uvicorn google-generativeai groq python-dotenv pydantic requests

Create a .env file and add your credentials (GROQ_API_KEY, GEMINI_API_KEY).

Launch the Monolithic Server:

Bash
uvicorn main:app --port 8000
2. n8n Orchestration

Import the workflows from the /n8n-workflows directory.

Ensure HTTP Request nodes are pointing to http://localhost:8000/[endpoint].

Activate the workflows.

Architected by Ali Rosyid.
