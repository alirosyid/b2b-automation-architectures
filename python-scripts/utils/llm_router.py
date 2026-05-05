import logging

  logger = logging.getLogger(__name__)

  class HighAvailabilityLLMRouter:
      """
      Ensures 100% pipeline uptime by automatically failing over to backup AI models 
      if the primary API provider experiences an outage.
      """
      def __init__(self, primary_client, backup_client):
          self.primary = primary_client # e.g., Groq (Llama-3)
          self.backup = backup_client   # e.g., Google GenAI (Gemini)

      def generate_response(self, prompt: str) -> str:
          try:
              logger.info("Attempting generation with primary LLM...")
              return self.primary.generate(prompt)
          except Exception as e:
              logger.critical(f"Primary LLM failed: {e}. Initiating failover to backup LLM.")
              return self.backup.generate(prompt)
