import os
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path


import os
from openai import OpenAI
from dotenv import load_dotenv


def get_openai_client():
    """
    Load environment variables safely
    """

    # Load .env from project root
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY not found!")

    return OpenAI(api_key=api_key)

def analyze_resume(resume_text):

    client = get_openai_client()

    prompt = f"""
    Analyze this resume and provide:

    1. Strengths
    2. Missing Skills
    3. ATS Score out of 100
    4. Improvement Suggestions

    Resume:
    {resume_text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content