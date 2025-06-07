import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://discourse.onlinedegree.iitm.ac.in"

def scrape_discourse(start_date, end_date):
    # Dummy logic — you'll need to paginate through topic pages
    topics = []
    for i in range(1, 5):  # Adjust for real pagination
        res = requests.get(f"{BASE_URL}/latest?page={i}")
        soup = BeautifulSoup(res.text, "html.parser")
        for link in soup.find_all("a", href=True):
            if "/t/" in link['href']:
                topics.append(BASE_URL + link['href'])

    print(f"Found {len(topics)} topics.")
    with open("scraped_links.json", "w") as f:
        json.dump(topics, f)

if __name__ == "__main__":
    scrape_discourse("2025-01-01", "2025-04-14")
