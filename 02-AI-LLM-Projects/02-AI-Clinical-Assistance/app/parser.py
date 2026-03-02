import json
import os
import re
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def extract_with_llm(text):

    prompt = f"""
Extract the following lab values from this medical report.

Return ONLY JSON.

Format:
{{
"Hemoglobin": number,
"Glucose": number,
"Creatinine": number,
"Vitamin D": number
}}

Medical Report:
{text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    output_text = response.choices[0].message.content.strip()

    # ---- CLEAN RESPONSE ----
    output_text = output_text.replace("```json", "")
    output_text = output_text.replace("```", "")

    # Extract JSON safely using regex
    match = re.search(r"\{.*\}", output_text, re.DOTALL)

    if not match:
        raise ValueError("No JSON found in LLM response")

    json_text = match.group()

    try:
        data = json.loads(json_text)
        return data
    except Exception:
        print("Invalid JSON returned by LLM:")
        print(json_text)

        # fallback safe output
        return {
            "Hemoglobin": None,
            "Glucose": None,
            "Creatinine": None,
            "Vitamin D": None
        }