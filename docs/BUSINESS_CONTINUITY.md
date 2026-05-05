# Business Continuity & Disaster Recovery Plan (BCP)

  ## 1. Objective
  To ensure the automated lead generation and enrichment pipelines remain operational during vendor outages.

  ## 2. Infrastructure Redundancy
  - **Orchestration:** n8n instances are stateless; workflows can be restored from GitHub in < 5 minutes.
  - **AI Processing:** Automatic failover implemented between Llama-3 (Groq) and Gemini Flash 2.5.
  
  ## 3. Data Integrity
  - All incoming webhooks are temporarily queued. If the processing microservice is down, webhooks are held and processed upon recovery, ensuring **zero data loss**.
