class PromptRegistry:
    """
    Enterprise PromptOps: Decouples system prompts from application logic.
    Allows for safe versioning, A/B testing, and instant rollbacks of AI instructions.
    """
    PROMPTS = {
        "b2b_extractor": {
            "v1.0": "Extract the company name and decision maker from this text.",
            "v1.1": "Strictly extract the Company Name (str) and CEO (str) in valid JSON format. Ignore marketing fluff."
        }
    }

    @classmethod
    def get_prompt(cls, agent_name: str, version: str = "v1.1") -> str:
        try:
            return cls.PROMPTS[agent_name][version]
        except KeyError:
            raise ValueError(f"Prompt version {version} for agent {agent_name} not found in registry.")
