import asyncio
import logging
from typing import List

logger = logging.getLogger(__name__)

class WebhookBatchingGateway:
    """
    Enterprise Ingress Shock Absorber.
    Intercepts massive concurrent webhook spikes from client CRMs,
    acknowledges the HTTP requests instantly, and micro-batches the payloads 
    to prevent Out-Of-Memory (OOM) crashes in downstream AI/n8n workers.
    """
    def __init__(self, batch_size: int = 50, flush_interval_sec: float = 2.0):
        self.batch_size = batch_size
        self.flush_interval = flush_interval_sec
        self.current_batch = []

    async def ingest_payload(self, payload: dict) -> dict:
        self.current_batch.append(payload)

        # Instantly return 202 Accepted to the client CRM to prevent timeouts
        # while the payload is held safely in the internal queue
        return {"status": "202_accepted", "message": "Queued for batch processing"}

    async def flush_to_workers(self, downstream_ai_processor):
        """Background task to drip-feed payloads to the AI engine."""
        while True:
            await asyncio.sleep(self.flush_interval)
            if self.current_batch:
                # Isolate the current chunk and clear it from the queue
                chunk_to_process = self.current_batch[:self.batch_size]
                self.current_batch = self.current_batch[self.batch_size:]

                logger.info(f"Gateway Flush: Routing batch of {len(chunk_to_process)} leads to AI processors.")

                # Pass the controlled batch to the heavy-compute LLM workers
                await downstream_ai_processor.execute_parallel_batch(chunk_to_process)
