import requests
import re
from bs4 import BeautifulSoup

def scrape_full_article(url):
    """
    Scrapes the website to extract general content, emails, and phone numbers.

    :param url: The website URL to scrape.
    :return: A dictionary with content, emails, and phone numbers.
    """
    try:
        # Fetch website content
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all text content
        paragraphs = soup.find_all(['p', 'span', 'div', 'a'])  # Include multiple tags
        content = " ".join(para.get_text(strip=True) for para in paragraphs)

        return {
            "content": content
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    test_url = input("Enter the article URL to scrape: ")
    text = scrape_full_article(test_url)
    print("Scraped Article Text:")
    print(text)