import os
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

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
def analyze_resume_with_job(resume_text, job_description):

    client = get_openai_client()

    prompt = f"""
    Compare the Resume and Job Description.

    Provide:

    1. Match Score (%)
    2. Matching Skills
    3. Missing Skills
    4. Improvement Suggestions
    5. Hiring Recommendation (Yes/No)

    Resume:
    {resume_text}

    Job Description:
    {job_description}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content