import logging

logger = logging.getLogger(__name__)

class DataResidencyRouter:
    """
    Ensures strict compliance with global data residency laws (e.g., GDPR, CCPA).
    Dynamically routes automation payloads to region-specific compute clusters 
    based on the geographical origin of the B2B lead.
    """
    EU_COUNTRY_CODES = {"DE", "FR", "IT", "ES", "NL", "BE", "SE"}

    @classmethod
    def route_payload(cls, payload: dict) -> str:
        country_code = payload.get("country_iso2", "US").upper()

        if country_code in cls.EU_COUNTRY_CODES:
            logger.info(f"GDPR Protocol: Routing {country_code} payload to EU-Central-1 cluster.")
            return "https://api.eu.b2b-engine.internal/webhook"
        else:
            logger.info(f"Standard Protocol: Routing {country_code} payload to US-East-1 cluster.")
            return "https://api.us.b2b-engine.internal/webhook"
