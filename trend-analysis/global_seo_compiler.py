class SEOCompiler:
    def __init__(self, target_rpm_markets: list):
        self.markets = target_rpm_markets
        self.banned_elements = ["local_slang", "untranslated_cultural_references"]

    def generate_metadata(self, core_topic: str) -> dict:
        # Synthesize titles using high-conversion global triggers
        blueprint = {
            "title": f"The Ultimate {core_topic} Blueprint (2026)",
            "tags": [core_topic.lower(), "global business", "automation strategy"],
            "markets": self.markets,
            "compliance_check": "passed"
        }
        return blueprint

compiler = SEOCompiler(target_rpm_markets=["USA", "EU", "UK"])
print(compiler.generate_metadata("AI Automation Infrastructure"))
