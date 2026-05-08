from typing import Dict, Any

class BaseAutomationAgent:
    """
    Core class for autonomous AI workers. Enforces a strict 6-component 
    prompting architecture to eliminate hallucinations in B2B environments.
    """
    def __init__(self, role: str, task: str, constraints: list, capabilities: list):
        self.role = role
        self.task = task
        self.constraints = constraints
        self.capabilities = capabilities

    def build_system_prompt(self, input_data: Dict[str, Any], expected_output_format: str) -> str:
        """Constructs the deterministic instruction set."""
        return f"""
        Role: {self.role}
        Task: {self.task}
        Input: {input_data}
        Output Format: {expected_output_format}
        Constraints: {', '.join(self.constraints)}
        Capabilities: {', '.join(self.capabilities)}
        """
