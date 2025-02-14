import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_URL = "https://newsapi.org/v2/everything"

def get_latest_articles(keyword, page_size=10):
    params = {
        "q": keyword,
        "sortBy": "publishedAt",
        "pageSize": page_size,
        "apiKey": NEWS_API_KEY
    }
    response = requests.get(NEWS_API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get("articles", [])
    else:
        print(f"Error fetching articles: {response.status_code}")
        return []
    
if __name__ == "__main__":
    test_keyword = input("Enter a keyword (e.g., sports, politics): ")
    articles = get_latest_articles(test_keyword)
    if articles:
        for i, article in enumerate(articles, 1):
            print(f"Article {i}: {article.get('title')}\nURL: {article.get('url')}\n")
    else:
        print("No articles found.")

