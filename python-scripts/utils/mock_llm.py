class MockLLMAPI:
      """
      Zero-cost dummy API for CI/CD pipelines and local development.
      Prevents wasting paid API tokens (Groq/Gemini) when testing n8n webhooks or internal logic.
      """
      def __init__(self, simulate_latency_seconds: float = 1.0):
          self.latency = simulate_latency_seconds

      def generate(self, prompt: str) -> str:
          import time
          time.sleep(self.latency)
          return '{"status": "mock_success", "extracted_data": {"name": "Test CEO", "company": "Test Inc"}}'
