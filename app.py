from fastapi import FastAPI, HTTPException, Query
from news_fetcher import get_latest_articles
from azure_openai_helper import generate_quiz_questions
from scraper import scrape_full_article

app = FastAPI(
    title="MindSpark",
    description="Fetches news articles and generates quiz questions based on the full article text",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the MindSpark. Use /articles?keyword=<your keyword> to get article URLs."}

@app.get("/articles")
def get_articles(keyword: str = Query(..., description="Keyword to search for articles"),
                 page_size: int = Query(10, description="Number of articles to return")):
    """
    Given a keyword, this endpoint returns a list of articles with their title and URL.
    """
    articles = get_latest_articles(keyword, page_size=page_size)
    if not articles:
        raise HTTPException(status_code=404, detail="No articles found for the provided keyword.")
    
    # Return a simplified list with title and URL.
    results = [{"title": article.get("title"), "url": article.get("url")} for article in articles if article.get("url")]
    return {"articles": results}

@app.get("/quiz")
def get_quiz(article_url: str = Query(..., description="URL of the article to generate quiz questions for")):
    """
    Given an article URL, this endpoint scrapes the full article text and generates quiz questions.
    """
    article_text = scrape_full_article(article_url)
    
    if not article_text or "could not be extracted" in article_text or "Error fetching article" in article_text:
        raise HTTPException(status_code=404, detail="Failed to retrieve full article text from the URL.")
    
    quiz = generate_quiz_questions(article_text)
    return {"quiz": quiz}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
