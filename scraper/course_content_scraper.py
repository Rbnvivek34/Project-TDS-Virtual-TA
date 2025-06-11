import json

def scrape_course_content():
    # Example: Load from downloaded notes
    contents = [
        {"title": "Tokenization", "content": "Tokenization is converting text into tokens..."},
        {"title": "Web APIs", "content": "Web APIs are interfaces for communication..."}
    ]
    with open("data/course_content.json", "w") as f:
        json.dump(contents, f)
    print("Course content scraped and saved to data/course_content.json")