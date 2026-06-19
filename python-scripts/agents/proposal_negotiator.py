class NegotiationAgent:
    def __init__(self, baseline_price, minimum_margin_price):
        self.baseline = baseline_price
        self.floor = minimum_margin_price

    def evaluate_counter_offer(self, client_offer):
        if client_offer < self.floor:
            print("[Agent] Offer is below minimum margin threshold.")
            return self._generate_pushback_response()
        elif client_offer < self.baseline:
            print("[Agent] Offer is acceptable but requires scope reduction.")
            return self._generate_compromise_response(client_offer)
        else:
            return "[Agent] Offer accepted. Generating final contract."

    def _generate_pushback_response(self):
        return "While we respect your budget constraints, our custom infrastructure costs prevent us from dropping to that tier without compromising system reliability."

    def _generate_compromise_response(self, offer):
        return f"We can accept the {offer} structure, provided we remove the 24/7 SLA requirement and shift to a 48-hour response window."

if __name__ == "__main__":
    agent = NegotiationAgent(baseline_price=10000, minimum_margin_price=7500)
    print(agent.evaluate_counter_offer(6000))
