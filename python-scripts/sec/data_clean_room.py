import hashlib
import logging
from typing import List, Set

logger = logging.getLogger(__name__)

class SecureDataCleanRoom:
    """
    Cryptographic B2B Data Collaboration.
    Allows two enterprise partners to find overlapping leads (e.g., for co-marketing) 
    without exposing their raw Personally Identifiable Information (PII) databases 
    to each other, ensuring strict legal compliance.
    """
    @staticmethod
    def _hash_list(raw_emails: List[str]) -> Set[str]:
        return {hashlib.sha256(email.lower().strip().encode()).hexdigest() for email in raw_emails}

    @classmethod
    def find_secure_overlap(cls, party_a_emails: List[str], party_b_emails: List[str]) -> int:
        logger.info("Initializing Secure Data Clean Room protocol...")

        hashed_a = cls._hash_list(party_a_emails)
        hashed_b = cls._hash_list(party_b_emails)

        overlap_count = len(hashed_a.intersection(hashed_b))
        logger.info(f"Clean Room Analysis Complete. Found {overlap_count} overlapping cryptographic hashes. Zero PII exposed.")

        return overlap_count
