import streamlit as st
from utils.parser import extract_text_from_pdf
from utils.analyzer import analyze_resume

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume", type="pdf")

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)

    st.subheader("Analysis Result")
    result = analyze_resume(text)

    st.write(result)