# Mindspark

## Overview

Mindspark is a FastAPI-based application that fetches news articles and generates quiz questions based on the full article text. It leverages the NewsAPI for fetching articles and Azure OpenAI for generating quiz questions.

## Features

- Fetch news articles based on a keyword.
- Generate quiz questions from the full text of a news article.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv env
    source env/Scripts/activate  # On Windows
    source env/bin/activate      # On Unix or MacOS
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a [.env](http://_vscodecontentref_/0) file in the root directory and add your environment variables:
    ```env
    NEWS_API_KEY=<your-news-api-key>
    AZURE_OPENAI_ENDPOINT=<your-openai-api-endpoint>
    AZURE_OPENAI_API_KEY=<your-openai-api-key>
    AZURE_OPENAI_API_VERSION=<your-azure-openai-api-version>
    AZURE_OPENAI_DEPLOYMENT_NAME=<your-azure-openai-model-name>
    ```

## Usage

1. Run the FastAPI application:
    ```sh
    uvicorn app:app --reload
    ```

   Alternatively, you can run the application using `python`:
    ```sh
    python app.py
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation.

## Endpoints

### GET /

- **Description**: Welcome message for the API.
- **Response**:
    ```json
    {
        "message": "Welcome to the NewsAI Quiz API. Use /articles?keyword=<your keyword> to get article URLs."
    }
    ```

### GET /articles

- **Description**: Fetches a list of articles based on a keyword.
- **Parameters**:
    - [keyword](http://_vscodecontentref_/1) (str): Keyword to search for articles.
    - [page_size](http://_vscodecontentref_/2) (int): Number of articles to return (default: 10).
- **Response**:
    ```json
    {
        "articles": [
            {
                "title": "Article Title",
                "url": "https://article.url"
            },
            ...
        ]
    }
    ```

### GET /quiz

- **Description**: Generates quiz questions based on the full text of a news article.
- **Parameters**:
    - [article_url](http://_vscodecontentref_/3) (str): URL of the article to generate quiz questions for.
- **Response**:
    ```json
    {
        "quiz": "Generated quiz questions"
    }
    ```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
