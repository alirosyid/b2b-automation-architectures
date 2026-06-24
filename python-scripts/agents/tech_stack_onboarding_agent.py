class OnboardingAgent:
    def __init__(self, client_name, tech_stack):
        self.client_name = client_name
        self.tech_stack = tech_stack

    def generate_custom_roadmap(self):
        print(f"[Agent] Analyzing software ecosystem for {self.client_name}: {self.tech_stack}")
        
        roadmap = f"""
        # Phase 1: Authentication
        - Generate API keys for {self.tech_stack[0]} and establish OAuth2 with {self.tech_stack[1]}.
        
        # Phase 2: Data Bridging
        - Deploy n8n edge nodes to map {self.tech_stack[2]} inventory webhooks into {self.tech_stack[0]} boards.
        
        # Phase 3: Automation Logic
        - Activate LLM intent classification on incoming {self.tech_stack[1]} emails.
        """
        
        print("[Agent] Custom integration roadmap generated. Dispatching to Ops team.")
        return roadmap

if __name__ == "__main__":
    agent = OnboardingAgent("RetailCorp", ["Monday.com", "Outlook", "Shopify"])
    print(agent.generate_custom_roadmap())
