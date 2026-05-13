import gzip
import logging
from fastapi import Request

logger = logging.getLogger(__name__)

class PayloadCompressionMiddleware:
    """
    Intercepts and decompresses large inbound B2B data payloads (e.g., bulk lead exports).
    Significantly reduces cloud ingress/egress bandwidth costs for high-volume pipelines.
    """
    @staticmethod
    async def decompress_if_needed(request: Request) -> bytes:
        body = await request.body()
        if request.headers.get("Content-Encoding") == "gzip":
            logger.info("Decompressing inbound gzip payload to save bandwidth costs.")
            return gzip.decompress(body)
        return body
