def calculate_ai_coding_roi(lines_accepted, dev_hourly_rate=65):
    # Assuming 1 accepted line saves ~2 minutes of typing, debugging, and testing
    hours_saved = (lines_accepted * 2) / 60
    cost_savings = hours_saved * dev_hourly_rate
    
    print(f"[Analytics] GitHub Copilot Tracker:")
    print(f"- Lines Auto-Completed: {lines_accepted}")
    print(f"- Developer Hours Saved: {hours_saved:.1f} hrs")
    print(f"- Total ROI Generated: ${cost_savings:.2f}")
    
    return cost_savings

if __name__ == "__main__":
    calculate_ai_coding_roi(lines_accepted=4500)
