# AI Resume Decision Engine

### Multi-Candidate Resume Analysis using Large Language Models (LLMs)

---

## 📌 Project Overview

The **AI Resume Decision Engine** is an intelligent resume analysis system designed to automate candidate evaluation using Large Language Models (LLMs).

The system analyzes resumes, extracts relevant professional information, evaluates candidate suitability, and generates structured hiring insights to assist recruiters in faster and more consistent decision-making.

This project demonstrates practical application of **LLM-powered document intelligence** for real-world recruitment workflows.

---

## 🎯 Problem Statement

Manual resume screening is:

* Time-consuming
* Subjective
* Difficult to scale for large applicant pools

Recruiters often review hundreds of resumes for a single role, leading to inconsistent evaluations and delayed hiring decisions.

This project aims to automate early-stage candidate screening using AI-driven analysis.

---

## ⚙️ Solution Approach

The system performs the following steps:

1. Resume text extraction
2. Skill and experience understanding using LLMs
3. Candidate qualification analysis
4. Multi-candidate comparison
5. Decision-oriented evaluation output

The AI generates structured hiring insights instead of raw text summaries.

---

## 🧠 Key Features

* Automated resume parsing and analysis
* AI-based candidate suitability evaluation
* Multi-candidate comparison support
* Structured decision output for recruiters
* Dataset-driven evaluation workflow
* Modular and extensible architecture

---

## 🏗️ Project Architecture

```
Resume Input
     ↓
Text Extraction
     ↓
LLM Analysis
     ↓
Candidate Evaluation Engine
     ↓
Structured Hiring Insights
```

---

## 📂 Project Structure

```
01-AI-Resume-Analyzer/
│
├── app.py
├── utils/
│   ├── resume_parser.py
│   ├── analyzer.py
│   └── scoring.py
│
├── candidate_analysis.csv
├── README.md
└── .gitignore
```

---

## 🛠️ Tech Stack

* Python
* Large Language Models (OpenAI API)
* NLP Processing
* Pandas
* Prompt Engineering
* Data Analysis

---

## 🚀 How to Run Locally

### 1. Clone Repository

```
git clone https://github.com/<your-username>/Priya-AI-BI-Portfolio.git
```

### 2. Navigate to Project

```
cd 02-AI-LLM-Projects/01-AI-Resume-Analyzer
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Add Environment Variables

Create `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

### 5. Run Application

```
python app.py
```

---

## 📊 Example Output

The system generates structured insights such as:

* Candidate strengths
* Skill alignment
* Experience relevance
* Hiring recommendation
* Comparative evaluation across candidates

---

## 💡 Use Cases

* Recruitment automation
* HR analytics workflows
* Candidate pre-screening
* Talent intelligence systems
* AI-assisted hiring platforms

---

## 🔮 Future Enhancements

* Streamlit-based interactive recruiter dashboard
* Cloud deployment for live resume evaluation
* Resume ranking visualization
* API-based candidate scoring service
* Integration with ATS (Applicant Tracking Systems)

---

## 👩‍💻 Author

**Priya Mishra**
AI + Business Intelligence Engineer

Focused on building real-world AI systems combining **LLMs, analytics, and decision automation**.

---

## ⚠️ Disclaimer

This system provides AI-assisted evaluation for informational purposes only and should support—not replace—human hiring decisions.

---
