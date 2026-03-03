AI Clinical Report Analyzer

A hybrid AI clinical decision support system that extracts lab values from medical reports using an LLM and performs rule-based risk evaluation based on predefined medical ranges.

Overview

This project analyzes uploaded blood test reports and generates structured clinical insights.

It combines:

LLM-based information extraction

Rule-based medical range validation

Dynamic abnormality detection

Automated risk classification

Structured clinical summary generation

The system demonstrates applied LLM engineering integrated with deterministic validation logic.

Key Features

Upload medical PDF reports

Extract lab values using OpenAI LLM

Validate values against clinical ranges

Detect HIGH / LOW abnormalities

Generate patient-specific summary

Risk classification (LOW / MODERATE / HIGH)

FastAPI backend with interactive API documentation

System Architecture

Hybrid approach:

PDF → Text Extraction

LLM → Structured JSON output

Rule Engine → Clinical range validation

Logic Layer → Risk classification

API Response → Structured clinical insight

This combination ensures both flexibility (LLM) and reliability (rule-based validation).

Tech Stack

Python

FastAPI

OpenAI API

JSON-based rule engine

Uvicorn

Python-dotenv

Example Output
{
  "summary": "30-year-old Male patient presenting with fatigue. Abnormal findings detected in: Glucose, Vitamin D.",
  "overall_risk": "HIGH",
  "risks": {
    "Vitamin D": {
      "value": 8.98,
      "status": "LOW",
      "range": "20-50"
    }
  }
}
Installation

Clone the repository:

git clone https://github.com/mishrapriya2525/Priya-AI-BI-Portfolio/tree/main/02-AI-LLM-Projects/02-AI-Clinical-Assistance
cd Priya-AI-BI-Portfolio/02-AI-LLM-Projects/02-AI-Clinical-Assistance

Install dependencies:

pip install -r requirements.txt

Create a .env file:

OPENAI_API_KEY=your_api_key_here

Run the server:

python -m uvicorn app.main:app --reload

Open:

http://127.0.0.1:8000/docs
Use Case

This system can be extended into:

Clinical intelligence dashboard

Lab automation workflow

AI-assisted medical reporting

Decision support tools for clinics

Disclaimer

This project is for educational and demonstration purposes only.
It is not intended to replace professional medical advice.