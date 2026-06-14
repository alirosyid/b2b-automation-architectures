import random

def generate_stealth_message(target_name, niche):
    hooks = [
        f"Hey {target_name}, noticed your recent work in {niche}. Really impressive stuff. Curious how you're handling backend scaling right now?",
        f"Hi {target_name}, your approach to {niche} is unique. I've been experimenting with some backend workflows that might complement this. Open to a quick chat?",
        f"{target_name} - saw your latest update. Brilliant execution. Are you currently leveraging any custom automation for your {niche} processes?"
    ]
    # No hard selling, just building curiosity
    return random.choice(hooks)

if __name__ == "__main__":
    print("Generated Outreach:", generate_stealth_message("Client", "E-commerce AI"))
