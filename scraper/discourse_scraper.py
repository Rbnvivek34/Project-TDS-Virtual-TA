import requests
import json
from datetime import datetime

def fetch_post(topic_id):
    url = f"https://discourse.onlinedegree.iitm.ac.in/t/{topic_id}.json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except Exception:
        return None

def scrape_discourse(start_date="2025-01-01", end_date="2025-04-14", save_path="data/discourse_posts.json"):
    start = datetime.fromisoformat(start_date)
    end = datetime.fromisoformat(end_date)
    results = []

    for topic_id in range(155900, 156000):  # Adjust this range as needed
        data = fetch_post(topic_id)
        if not data:
            continue

        posts = data.get("post_stream", {}).get("posts", [])
        for post in posts:
            try:
                created = datetime.fromisoformat(post["created_at"].replace("Z", "+00:00"))
                if start <= created <= end:
                    results.append({
                        "topic_id": topic_id,
                        "raw": post["raw"],
                        "created_at": post["created_at"],
                        "url": f"https://discourse.onlinedegree.iitm.ac.in/t/{topic_id}"
                    })
            except Exception:
                continue

    with open(save_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Saved {len(results)} posts.")

if __name__ == "__main__":
    scrape_discourse()
