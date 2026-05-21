import asyncio
import httpx
import logging
from fastapi import BackgroundTasks

logger = logging.getLogger(__name__)

class AsyncCallbackEngine:
    """
    Decouples long-running LLM inferences from n8n webhook timeouts.
    Returns a 202 Accepted instantly, processes the data via FastAPI background tasks, 
    and pushes the enriched payload back to a dedicated n8n callback URL.
    """
    @staticmethod
    async def process_and_callback(payload: dict, callback_url: str):
        logger.info("Background processing initiated. Executing heavy LLM extraction...")
        await asyncio.sleep(2) # Simulated heavy inference

        enriched_data = {**payload, "ai_extracted_value": "High Intent B2B Lead"}

        async with httpx.AsyncClient() as client:
            await client.post(callback_url, json=enriched_data)
            logger.info(f"Asynchronous processing complete. Payload pushed to {callback_url}")
