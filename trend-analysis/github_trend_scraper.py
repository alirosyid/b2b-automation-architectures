import requests

def fetch_trending_repos():
    # Public API endpoint for GitHub trends
    url = "https://api.githunt.io/programmingapi/repos?sort=stars&order=desc"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            repos = response.json()[:5] # Get top 5
            for repo in repos:
                print(f"Trend Alert: {repo['name']} - {repo['description']}")
    except Exception as e:
        print(f"Error fetching trends: {e}")

if __name__ == "__main__":
    fetch_trending_repos()
