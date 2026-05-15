import logging
from typing import List

logger = logging.getLogger(__name__)

class BrandSafetyFirewall:
    """
    Inspects outbound AI-generated communications. Blocks the transmission of 
    messages that mention direct competitors or internal Intellectual Property (IP) keywords.
    """
    def __init__(self, competitor_list: List[str], ip_keywords: List[str]):
        self.competitors = [c.lower() for c in competitor_list]
        self.ip_keywords = [ip.lower() for ip in ip_keywords]

    def scan_outbound_message(self, ai_generated_text: str) -> bool:
        text_lower = ai_generated_text.lower()

        for competitor in self.competitors:
            if competitor in text_lower:
                logger.error(f"Firewall Blocked: Competitor '{competitor}' mentioned in outbound copy.")
                return False

        for keyword in self.ip_keywords:
            if keyword in text_lower:
                logger.error("Firewall Blocked: Potential Intellectual Property leak detected.")
                return False

        return True
