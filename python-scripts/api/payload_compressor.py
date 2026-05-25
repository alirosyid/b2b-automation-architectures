import zlib
import json
import logging

logger = logging.getLogger(__name__)

class DynamicPayloadCompressor:
    """
    FinOps Network Optimizer.
    Intersects massive intra-service JSON transfers (e.g., bulk scraped B2B lead arrays) 
    and applies dynamic zlib compression, drastically reducing cloud egress bandwidth costs.
    """
    @staticmethod
    def compress_outbound_data(payload: dict) -> bytes:
        payload_bytes = json.dumps(payload).encode('utf-8')
        original_size = len(payload_bytes)

        compressed_data = zlib.compress(payload_bytes, level=6)
        compressed_size = len(compressed_data)

        savings = 100 - ((compressed_size / original_size) * 100) if original_size > 0 else 0
        logger.debug(f"Payload compressed: {original_size}B -> {compressed_size}B ({savings:.1f}% bandwidth saved).")

        return compressed_data
