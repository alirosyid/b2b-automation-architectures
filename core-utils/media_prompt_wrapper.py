def build_cinematic_prompt(subject: str, aesthetic: str = "Dark Noir") -> str:
    # Enforcing strict prompt boundaries for AI media generation
    base_lighting = "High-contrast lighting, 8k resolution, hyper-detailed"
    negative_prompts = "--no zoom, --no camera movement, --no blurry, --no text"
    
    final_prompt = f"{subject}, {aesthetic} atmosphere, {base_lighting}. {negative_prompts}"
    return final_prompt

# Example: Generating prompts for the Chronos & Kairos project
scene = build_cinematic_prompt("A glowing neon server rack in an abandoned warehouse")
print(f"Generated Payload: {scene}")
