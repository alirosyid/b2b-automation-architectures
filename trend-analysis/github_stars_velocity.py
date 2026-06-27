def calculate_star_velocity(repo_name, stars_yesterday, stars_today):
    velocity = stars_today - stars_yesterday
    growth_rate = (velocity / stars_yesterday) * 100 if stars_yesterday > 0 else 0
    
    print(f"[Trends] Repository: {repo_name}")
    print(f"- 24h Velocity: +{velocity} stars")
    print(f"- Growth Rate: {growth_rate:.1f}%")
    
    if growth_rate > 15.0:
        print(f"[!] VIRAL TRAJECTORY DETECTED. Flagging {repo_name} for immediate R&D evaluation.")
        return True
        
    return False

if __name__ == "__main__":
    calculate_star_velocity("n8n-io/n8n", stars_yesterday=35000, stars_today=35600)
