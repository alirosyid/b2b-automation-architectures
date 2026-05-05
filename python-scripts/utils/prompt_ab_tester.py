import random

  class PromptABTester:
      """
      Routes traffic between different prompt variations to determine which 
      yields higher data extraction accuracy or lower token costs.
      """
      def __init__(self, prompt_a: str, prompt_b: str):
          self.prompt_a = prompt_a
          self.prompt_b = prompt_b
          self.stats = {"A": {"uses": 0, "success": 0}, "B": {"uses": 0, "success": 0}}

      def get_prompt(self) -> tuple:
          variation = "A" if random.random() < 0.5 else "B"
          self.stats[variation]["uses"] += 1
          return variation, self.prompt_a if variation == "A" else self.prompt_b
