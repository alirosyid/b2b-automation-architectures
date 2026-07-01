import requests

def analyze_competitor_stack(org_name, github_token):
    headers = {"Authorization": f"token {github_token}"}
    url = f"https://api.github.com/orgs/{org_name}/repos?sort=created&direction=desc"
    
    response = requests.get(url, headers=headers).json()
    if response:
        latest_repo = response[0]['name']
        print(f"New repository detected: {latest_repo}")
        # Fetch package.json and send to LLM logic goes here
        return latest_repo
    return None

if __name__ == "__main__":
    analyze_competitor_stack("competitor-org", "ghp_xxxxxxxxxxxx")
