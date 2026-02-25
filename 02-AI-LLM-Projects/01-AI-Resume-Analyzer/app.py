import streamlit as st

from utils.parser import extract_text_from_pdf
from utils.analyzer import analyze_resume_with_job

import pandas as pd


st.title("AI Resume Analyzer & Job Matcher")

uploaded_files = st.file_uploader(
    "Upload Resumes",
    type="pdf",
    accept_multiple_files=True
)

job_description = st.text_area(
    "Paste Job Description",
    height=200
)

analyze_button = st.button("Analyze Match")

# ✅ Run analysis
results = []

if analyze_button and uploaded_files and job_description:

    for file in uploaded_files:

        resume_text = extract_text_from_pdf(file)

        result = analyze_resume_with_job(
            resume_text,
            job_description
        )

        result["candidate_name"] = file.name
        results.append(result)
    # ✅ Display ONLY after result exists
    st.subheader("Match Score")
    st.metric("Score", f"{result['match_score']}%")

    st.subheader("Matching Skills")
    st.write(result["matching_skills"])

    st.subheader("Missing Skills")
    st.write(result["missing_skills"])

    st.subheader("Hiring Recommendation")
    st.success(result["recommendation"])
    
    
    


df = pd.DataFrame(results)
st.dataframe(df)
df.to_csv("candidate_analysis.csv", index=False)
