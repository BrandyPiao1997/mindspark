from news_fetcher import get_latest_articles
from azure_openai_helper import generate_quiz_questions
from scraper import scrape_full_article

def generate_quiz_for_articles(keyword, num_articles=1):
    # Retrieve articles from the news API
    articles = get_latest_articles(keyword, page_size=num_articles)
    quiz_results = []
    
    # Iterate through each article and scrape its full text
    for article in articles:
        url = article.get('url')
        title = article.get('title', 'No Title')
        if url:
            print(f"Scraping article: {title}\nURL: {url}")
            article_text = scrape_full_article(url)
            
            # Check if scraping was successful
            if article_text and "could not be extracted" not in article_text and "Error fetching article" not in article_text:
                # Generate quiz questions using the scraped text
                print("Generating quiz questions...")
                quiz = generate_quiz_questions(article_text)
            else:
                quiz = "Article text could not be extracted."
        else:
            quiz = "No URL found for this article."
        
        quiz_results.append({
            "title": title,
            "url": url,
            "quiz": quiz
        })
    
    return quiz_results

# Test block to run the complete logic
if __name__ == "__main__":
    keyword = input("Enter a keyword (e.g., sports, politics): ")
    results = generate_quiz_for_articles(keyword)
    
    for idx, result in enumerate(results, 1):
        print(f"\nArticle {idx}: {result['title']}")
        print(f"URL: {result['url']}")
        print("Quiz Questions:\n", result['quiz'])
        print("-" * 50)
