import urllib.request
import re

def check_pricing(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read().decode('utf-8')
        
        # Look for dollar amounts in the HTML
        prices = re.findall(r'\$[0-9,]+', html)
        return list(set(prices))
    except Exception as e:
        return f"Failed to fetch data: {e}"

if __name__ == "__main__":
    # Example placeholder URL
    print("Detected Price Tiers:", check_pricing("https://example-agency.com/pricing"))
