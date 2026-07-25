def calculate_conversion_probability(lead_state_sequence):
    print("[Analytics] Modeling B2B lead intent using Markov Chain transition probabilities...")
    
    # Mocking transition matrix probabilities
    state_transitions = {
        "EMAIL_OPEN": 0.1,
        "PRICING_PAGE": 0.4,
        "WHITEPAPER_DL": 0.85
    }
    
    cumulative_probability = 0.0
    for state in lead_state_sequence:
        print(f"    -> Analyzing state transition: {state}")
        cumulative_probability = state_transitions.get(state, 0.0) # Simplified for demonstration
        
    print(f"    -> Markov Probability of Closing: {cumulative_probability * 100}%")
    
    if cumulative_probability >= 0.80:
        print("[🔥] HYPER-QUALIFIED LEAD. Autonomously routing to Account Executive dashboard.")
        return True
        
    return False

if __name__ == "__main__":
    sequence = ["EMAIL_OPEN", "PRICING_PAGE", "WHITEPAPER_DL"]
    calculate_conversion_probability(sequence)
