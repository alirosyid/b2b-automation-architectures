import os
import sys
import logging

logger = logging.getLogger(__name__)

REQUIRED_SECRETS = [
    "GROQ_API_KEY",
    "STRIPE_SECRET_KEY",
    "N8N_WEBHOOK_URL",
    "DATABASE_URL"
]

def validate_environment():
    """
    Ensures all critical environment variables are present on startup.
    Fails fast if misconfigured.
    """
    missing = [secret for secret in REQUIRED_SECRETS if not os.getenv(secret)]
    
    if missing:
        logger.critical(f"Startup Failed. Missing required environment variables: {', '.join(missing)}")
        sys.exit(1)
        
    logger.info("Environment validation passed. All required secrets loaded.")

if __name__ == "__main__":
    validate_environment()
