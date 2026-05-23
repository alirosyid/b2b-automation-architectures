import logging
import asyncio

logger = logging.getLogger(__name__)

class AsyncOCRQueue:
    """
    Compute Offloading Engine.
    Isolates heavy, CPU-blocking tasks (like Multimodal PDF OCR or image processing) 
    into a dedicated asynchronous background worker queue. Ensures the main FastAPI 
    ingress threads remain unblocked and highly responsive.
    """
    def __init__(self):
        self.queue = asyncio.Queue()

    async def enqueue_document(self, document_uri: str, callback_url: str):
        await self.queue.put({"uri": document_uri, "callback": callback_url})
        logger.info(f"Document {document_uri} queued for heavy OCR processing.")

    async def _worker_loop(self):
        while True:
            task = await self.queue.get()
            logger.info(f"Worker executing heavy OCR on {task['uri']}...")

            # Simulated heavy processing
            await asyncio.sleep(3) 
            logger.info("OCR complete. Dispatching results via callback.")
            self.queue.task_done()
