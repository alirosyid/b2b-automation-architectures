from fastapi import FastAPI, BackgroundTasks
import time
import logging

app = FastAPI()
logger = logging.getLogger(__name__)

def heavy_ai_processing(payload: dict):
    """Simulates a long-running LLM generation task."""
    logger.info(f"Starting background processing for {payload.get('id')}")
    time.sleep(10) # Simulate API latency
    logger.info(f"Completed processing for {payload.get('id')}")

@app.post("/webhook/enrich-lead")
async def handle_webhook(payload: dict, background_tasks: BackgroundTasks):
    background_tasks.add_task(heavy_ai_processing, payload)
    return {"status": "accepted", "message": "Processing started in background"}
