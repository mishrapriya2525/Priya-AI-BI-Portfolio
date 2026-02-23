import streamlit as st
from utils.parser import extract_text_from_pdf
from utils.analyzer import analyze_resume_with_job

st.title("AI Resume Analyzer & Job Matcher")

# Upload Resume
uploaded_file = st.file_uploader(
    "Upload Resume",
    type="pdf"
)

# Job Description Input
job_description = st.text_area(
    "Paste Job Description",
    height=200
)

# ✅ Execution Control Button
analyze_button = st.button("Analyze Match")

# Run ONLY when button clicked
if analyze_button and uploaded_file and job_description:

    resume_text = extract_text_from_pdf(uploaded_file)

    st.subheader("Analyzing Resume vs Job...")

    result = analyze_resume_with_job(
        resume_text,
        job_description
    )

    st.write(result)