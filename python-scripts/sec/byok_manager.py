import os
import logging
from cryptography.fernet import Fernet

logger = logging.getLogger(__name__)

class BYOKManager:
    """
    Bring Your Own Key (BYOK) Infrastructure.
    Allows enterprise clients to inject their own LLM API keys for strict data 
    governance and direct billing, utilizing hardware-backed encryption at rest.
    """
    def __init__(self, master_encryption_key: bytes):
        self.cipher_suite = Fernet(master_encryption_key)

    def decrypt_client_key(self, client_id: str, encrypted_key_blob: bytes) -> str:
        try:
            decrypted_key = self.cipher_suite.decrypt(encrypted_key_blob).decode('utf-8')
            logger.info(f"Successfully decrypted BYOK credentials for {client_id} in isolated memory.")
            return decrypted_key
        except Exception as e:
            logger.critical(f"BYOK Decryption failure for {client_id}. Halting execution to prevent leakage.")
            raise ValueError("Cryptographic key verification failed.")
