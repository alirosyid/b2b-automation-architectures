import random
import logging

logger = logging.getLogger(__name__)

class QASampler:
    """
    Mengalihkan persentase kecil (misal 5%) dari hasil ekstraksi AI ke antrean manual.
    Memastikan Quality Assurance (QA) enterprise tetap terjaga.
    """
    def __init__(self, sample_rate_percent: float = 5.0):
        self.threshold = sample_rate_percent / 100.0

    def requires_human_review(self, lead_data: dict) -> bool:
        if random.random() <= self.threshold:
            logger.info(f"Lead {lead_data.get('email')} routed to Human QA queue.")
            return True
        return False
