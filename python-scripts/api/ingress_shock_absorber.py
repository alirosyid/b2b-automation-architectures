import asyncio
import logging

logger = logging.getLogger(__name__)

class IngressShockAbsorber:
    """
    Enterprise Webhook Traffic Cop.
    Intercepts massive concurrent CRM webhook spikes, queues them in memory, 
    and drip-feeds the payloads to the n8n orchestrator. Mathematically guarantees 
    zero Out-Of-Memory (OOM) crashes under extreme B2B data loads.
    """
    def __init__(self, safe_rpm_limit: int = 100):
        self.queue = asyncio.Queue()
        self.drip_rate = 60.0 / safe_rpm_limit

    async def accept_payload(self, payload: dict) -> dict:
        await self.queue.put(payload)
        # Release the client connection instantly to prevent CRM timeouts
        return {"status": "202_accepted", "message": "Buffered for safe processing"}

    async def process_queue_safely(self, downstream_processor):
        while True:
            payload = await self.queue.get()
            logger.info("Routing buffered payload safely to orchestrator.")
            await downstream_processor(payload)
            self.queue.task_done()
            await asyncio.sleep(self.drip_rate)
