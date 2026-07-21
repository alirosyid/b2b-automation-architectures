def score_visual_damage_severity(vision_ai_analysis):
    print("[Analytics] Calculating structural damage severity from Vision AI output...")
    
    # Mocking severity calculation based on vision tags
    severity_score = 0
    if "water damage" in vision_ai_analysis.lower() or "burst" in vision_ai_analysis.lower():
        severity_score += 60
    if "rust" in vision_ai_analysis.lower():
        severity_score += 30
        
    print(f"    -> Visual Severity Score: {severity_score}/100")
    
    if severity_score >= 85:
        print("[!] 🚨 EMERGENCY DETECTED. Triggering 1.5x surge pricing and immediate dispatch.")
        return {"status": "EMERGENCY", "surge_multiplier": 1.5}
        
    return {"status": "STANDARD", "surge_multiplier": 1.0}

if __name__ == "__main__":
    score_visual_damage_severity("Massive water damage from burst pipe. Heavy rust on compressor.")
