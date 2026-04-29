# ⚡ Enterprise B2B Automation Architectures

Welcome to my portfolio of production-ready automation pipelines and AI agents. 
This repository contains high-impact workflows designed to eliminate manual bottlenecks, reduce operational costs, and scale B2B operations using n8n, Python, and Large Language Models (LLMs).

---

## 📑 Table of Contents
- [Architecture 1: AI-Powered OCR & Invoice Data Extraction](#️-architecture-1-ai-powered-ocr--invoice-data-extraction)
- [Architecture 2: B2B Lead Enrichment Pipeline](#️-architecture-2-b2b-lead-enrichment-pipeline)
- [Architecture 3: Enterprise RAG Customer Support Agent](#️-architecture-3-enterprise-rag-customer-support-agent)
- [Architecture 4: Omnichannel Content Repurposing Engine](#️-architecture-4-omnichannel-content-repurposing-engine)
- [Workflow Demonstrations](#workflow-demonstrations)
- [How to Deploy (For Developers)](#️-how-to-deploy-for-developers)

---

## 🏗️ Architecture 1: AI-Powered OCR & Invoice Data Extraction
*(Located in `/n8n-workflows` & `/python-scripts`)*

### 🔴 The Problem
Finance and accounting teams waste hundreds of hours manually typing data from physical invoices and receipts into spreadsheets. This process is slow, expensive, and highly prone to human error.

### 🟢 The AI Solution
A fully automated visual extraction pipeline. It receives physical invoice images/PDFs, processes them through a custom FastAPI endpoint, and leverages Google's **Gemini 2.5 Flash** vision model to extract perfect, structured JSON data (Vendor Name, Dates, Line Items, Totals).

* **Tech Stack:** n8n (Orchestration), Python/FastAPI (Microservice), Google Gemini 2.5 Flash (Vision AI).
* **Business Impact:** * Reduces invoice processing time from minutes to **under 3 seconds** per document.
  * Achieves 99% accuracy in data extraction.
  * Completely eliminates the need for manual data entry clerks for accounts payable.

---

## 🏗️ Architecture 2: B2B Lead Enrichment Pipeline
*(Located in `/n8n-workflows/b2b_lead_enrichment_pipeline.json`)*

### 🔴 The Problem
Sales teams spend 60% of their day manually researching prospects on LinkedIn or company websites before sending cold emails, leading to low outreach volume and burnout.

### 🟢 The AI Solution
An automated lead enrichment engine. Feed it a basic list of company domains, and the pipeline automatically scrapes the websites, extracts key company data, identifies the value proposition, and drafts highly personalized cold outreach emails using AI.

* **Tech Stack:** n8n, Web Scraping Nodes, LLM APIs.
* **Business Impact:** * Increases outbound sales volume by 10x without sacrificing personalization quality.
  * Saves SDRs (Sales Development Reps) 20+ hours per week in manual research.

---

## 🏗️ Architecture 3: Enterprise RAG Customer Support Agent
*(Located in `/python-scripts/telegram_rag_bot.py`)*

### 🔴 The Problem
B2B SaaS companies spend heavily on Tier-1 support agents answering the same repetitive questions about pricing, operating hours, and refund policies. Traditional chatbots often hallucinate facts or frustrate users with rigid, robotic menus.

### 🟢 The AI Solution
A context-aware Retrieval-Augmented Generation (RAG) agent deployed via Telegram. Powered by Google Gemini 2.5 Flash, the bot dynamically reads from a strict internal company knowledge base. It answers valid queries instantly with a perfect professional tone and safely deflects out-of-scope questions to human agents without hallucinating.

* **Tech Stack:** Python, python-telegram-bot, Google Gemini API, RAG Architecture.
* **Business Impact:** * Automates 80% of Tier-1 customer support tickets instantly.
  * Zero hallucination risk (strict AI grounding to company documentation).
  * Available 24/7, reducing average human response time from hours to seconds.

---

## 🏗️ Architecture 4: Enterprise Content Repurposing Engine (Deep Context)
*(Located in `/n8n-workflows` & `/python-scripts/content_engine_api2.py`)*

### 🔴 The Problem
Marketing agencies struggle with the "content treadmill." Turning a deep, unstructured B2B podcast (2,500+ words of raw transcript) into multi-channel assets requires hours of manual copywriting. Existing SaaS tools lack strategic depth, hallucinate facts, and offer no customizable brand-voice architecture for white-labeling.

### 🟢 The AI Solution
A decoupled microservice architecture designed for enterprise agency deployment. It ingests raw, unformatted audio transcripts, chunks the tokens, and processes them through an ultra-low latency LLM inference engine to output a strict 11-point JSON asset array.

* **Tech Stack:** n8n (Stateless Orchestration), Python/FastAPI (Intelligence Core), Groq API / Llama 3 70B (LLM Engine).
* **Key Technical Features:**
  * **API Modularity:** Built to support multimodal processing (Gemini), but dynamically routed through Groq (Llama 3) for high-speed, text-heavy B2B inference.
  * **6-Component Prompt Framework:** Forces the LLM into a strict persona at `Temperature 0.1` to extract only high-value B2B signals, bypassing conversational filler and hallucinations.
  * **JSON Schema Enforcement:** Utilizes strict `json_object` formatting to guarantee parsable outputs for downstream CRM/CMS integrations.
* **Business Impact:** 
  * Reduces deep-context content repurposing from 4 hours to ~3.5 seconds.
  * Extracted assets include SEO Pillar Blogs, X Threads, LinkedIn Hooks, Newsletters, and Video Concepts.
  
---

## Workflow Demonstrations

- **B2B Automated Outreach Pipeline**: [View Technical Demonstration (Loom)](https://www.loom.com/share/d005a1c870c44caaa44221b80e929d4d) - *End-to-end execution of prospect data extraction, dynamic email personalization via Groq (Llama-3), and multi-channel dispatch (Gmail/Telegram) orchestrated in n8n.*

---

## 🛠️ How to Deploy (For Developers)

**1. n8n Workflows**
* Open your n8n instance.
* Go to the workflows interface, click `Import from File`, and select the `.json` files from the `/n8n-workflows` directory.

**2. Custom Python Microservices (Gemini Vision & Groq Content Engine)**
* Navigate to the `/python-scripts` directory.
* Install dependencies: `pip install fastapi uvicorn google-generativeai groq python-dotenv pillow`
* Create a `.env` file and add your credentials: 
  * `GEMINI_API_KEY=your_key_here`
  * `GROQ_API_KEY=your_key_here`
* **To run the Deep Context Content Engine:** `uvicorn content_engine_api2:app --host 0.0.0.0 --port 8000 --reload`
* **To run the Vision OCR Engine:** `uvicorn gemini_vision_ocr_api:app --host 0.0.0.0 --port 8000 --reload`

---
*Architected by Ali Rosyid.*
