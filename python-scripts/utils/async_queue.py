import asyncio

class AsyncWebhookQueue:
    """
    In-memory async queue untuk mencegah webhook overload.
    Dalam produksi B2B sejati, ini akan digantikan oleh Redis atau RabbitMQ.
    """
    def __init__(self):
        self.queue = asyncio.Queue()

    async def add_to_queue(self, payload: dict):
        await self.queue.put(payload)

    async def process_queue(self, worker_function):
        while True:
            payload = await self.queue.get()
            try:
                await worker_function(payload)
            finally:
                self.queue.task_done()
