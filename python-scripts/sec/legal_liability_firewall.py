import logging
import re

logger = logging.getLogger(__name__)

class LegalLiabilityFirewall:
    """
    Deterministic safeguard against autonomous legal commitments.
    Scans all AI-generated outbound emails/messages to ensure the LLM 
    does not hallucinate unauthorized discounts, SLAs, or contractual promises.
    """
    # Regex to detect currency offers, percentages, or warranty claims
    RESTRICTED_PATTERNS = [
        r"\$\d+",              # Dollar amounts
        r"\d+%\s*(discount|off)", # Percentage discounts
        r"(guarantee|warranty|promise|liable)" # Legal terms
    ]

    @classmethod
    def vet_outbound_communication(cls, ai_generated_copy: str) -> bool:
        text_lower = ai_generated_copy.lower()

        for pattern in cls.RESTRICTED_PATTERNS:
            if re.search(pattern, text_lower):
                logger.critical(f"LEGAL FIREWALL TRIPPED: Unauthorized commitment detected -> '{pattern}'")
                # Quarantine the message; do not send to client
                return False

        logger.info("Outbound copy passed legal liability firewall. Cleared for sending.")
        return True
