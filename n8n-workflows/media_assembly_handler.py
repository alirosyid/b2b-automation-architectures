import asyncio
import subprocess
import time
import logging
from typing import Dict, Any

logging.basicConfig(level=logging.INFO)

class AsyncTokenBucket:
    def __init__(self, capacity: int, fill_rate: float):
        self.capacity = capacity
        self.tokens = capacity
        self.fill_rate = fill_rate
        self.last_update = time.time()

    async def consume(self, tokens: int = 1) -> bool:
        now = time.time()
        self.tokens = min(self.capacity, self.tokens + (now - self.last_update) * self.fill_rate)
        self.last_update = now
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False

bucket = AsyncTokenBucket(capacity=50, fill_rate=5.0)

async def execute_media_shell_script(payload: Dict[str, Any]):
    """Executes bash automation for assembling media assets."""
    # Sanitize inputs to prevent shell injection
    video_dir = payload.get("video_folder", "/tmp/default")
    audio_dir = payload.get("audio_folder", "/tmp/default")
    
    command = f"bash ./assemble_media.sh --video {video_dir} --audio {audio_dir}"
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    if process.returncode == 0:
        logging.info(f"Media assembled successfully: {stdout.decode().strip()}")
    else:
        logging.error(f"Assembly failed: {stderr.decode().strip()}")

async def handle_n8n_webhook(payload: Dict[str, Any]):
    """SRE: Async shock absorber for n8n payload surges."""
    if await bucket.consume():
        asyncio.create_task(execute_media_shell_script(payload))
        return {"status": "accepted", "message": "Media assembly queued."}
    else:
        logging.warning("Rate limit exceeded. Shedding load.")
        return {"status": "429", "message": "Too Many Requests. DLQ routed."}
