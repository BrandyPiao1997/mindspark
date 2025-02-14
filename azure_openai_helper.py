import os
import json
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.getenv('OPENAI_API_ENDPOINT'),
    api_key=os.getenv('OPENAI_API_KEY'),
    api_version=os.getenv('AZURE_OPENAI_API_VERSION')
)

def generate_quiz_questions(article_text):
    prompt = (
        "Based on the following article text, generate 3 quiz questions that test comprehension. They can be multiple choice or true false questions."
        "For each question, provide three multiple choice options, indicate the correct answer, and provide the rationale behind it.\n\n"
        f"Article Text:\n{article_text}\n\nQuiz Questions:"
    )
    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        messages=[
            {"role": "system", "content": "You are an assistant that generates quiz questions based on provided article content."},
            {"role": "user", "content": prompt}
        ]
    )
    output = response.choices[0].message.content

    #TODO: Return json formatted output
    return output

# Test block
if __name__ == "__main__":
    sample_text = (
        "NASA's Perseverance rover has successfully collected samples of Martian rock, "
        "which may provide crucial insights into the planet's past climate and the potential for past life."
    )
    print("\nQuiz Questions Test:")
    print(generate_quiz_questions(sample_text))
