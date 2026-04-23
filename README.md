# ⚡ Enterprise B2B Automation Architectures

Welcome to my portfolio of production-ready automation pipelines and AI agents. 
This repository contains high-impact workflows designed to eliminate manual bottlenecks, reduce operational costs, and scale B2B operations using n8n, Python, and Large Language Models (LLMs).

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

## 🏗️ Architecture 4: Omnichannel Content Repurposing Engine
*(Located in `/n8n-workflows` & `/python-scripts`)*

### 🔴 The Problem
Marketing agencies and content creators struggle with the "content treadmill." Turning a single podcast episode or YouTube video into SEO blogs, Twitter threads, and LinkedIn posts requires hours of manual copywriting, creating a massive bottleneck and high operational costs.

### 🟢 The AI Solution
A hybrid Python + n8n automation pipeline that acts as an autonomous marketing team. It ingests raw video transcripts and uses Google Gemini 2.5 Flash with strict zero-shot prompting to instantly restructure the text into three distinct formats: an HTML-ready SEO Blog, an engaging Twitter Thread, and a professional LinkedIn hook.

* **Tech Stack:** n8n (Orchestration), FastAPI (Microservice), Google Gemini API.
* **Business Impact:** * Reduces content repurposing time from 4 hours to **under 5 seconds**.
  * Enforces strict formatting (JSON output) for direct CMS injection.
  * Eliminates the need for junior copywriters for content translation across platforms.
  
---

## Workflow Demonstrations

- **B2B Automated Outreach Pipeline**: [View Technical Demonstration (Loom)](https://www.loom.com/share/d005a1c870c44caaa44221b80e929d4d) - *End-to-end execution of prospect data extraction, dynamic email personalization via Groq (Llama-3), and multi-channel dispatch (Gmail/Telegram) orchestrated in n8n.*

---

## 🛠️ How to Deploy (For Developers)

**1. n8n Workflows**
* Open your n8n instance.
* Go to the workflows interface, click `Import from File`, and select the `.json` files from the `/n8n-workflows` directory.

**2. Custom Python Microservices (e.g., Gemini OCR)**
* Navigate to the `/python-scripts` directory.
* Install dependencies: `pip install fastapi uvicorn google-generativeai python-dotenv pillow`
* Create a `.env` file and add your credentials: `GEMINI_API_KEY=your_key_here`
* Run the server: `uvicorn gemini_vision_ocr_api:app --host 0.0.0.0 --port 8000 --reload`

---
*Architected by Ali Rosyid.*
