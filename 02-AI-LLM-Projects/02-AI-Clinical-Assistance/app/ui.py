import streamlit as st
import requests
import json

st.set_page_config(page_title="AI Clinical Assistant")

st.title("🩺 AI Clinical Assistant")
st.subheader("Patient Report Analysis System")

uploaded_file = st.file_uploader("Upload Medical Report (PDF)", type=["pdf"])

age = st.number_input("Patient Age", min_value=0, max_value=120, value=30)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
symptoms = st.text_area("Patient Symptoms")

if st.button("Generate Clinical Summary"):

    if uploaded_file is None:
        st.error("Please upload a PDF first.")
    else:
        with st.spinner("Analyzing report..."):

            files = {
                "file": (uploaded_file.name, uploaded_file, "application/pdf")
            }

            data = {
                "age": age,
                "gender": gender,
                "symptoms": symptoms
            }

            try:
                response = requests.post(
                    "http://127.0.0.1:8000/analyze",
                    files=files,
                    data=data
                )

                if response.status_code == 200:
                    result = response.json()
                    report_json = json.dumps(result, indent=4)

                    st.download_button(
                    label="Download Clinical Report (JSON)",
                    data=report_json,
                    file_name="clinical_report.json",
                    mime="application/json"
)

                    st.success("Analysis Complete")

                    st.subheader("Summary")
                    st.write(result["summary"])

                    st.subheader("Risk Analysis")

                    for marker, details in result["risks"].items():
                        status = details["status"]

                    if status == "NORMAL":
                        st.success(f"{marker}: {status}")
                    elif status == "HIGH":
                        st.error(f"{marker}: {status}")
                    elif status == "LOW":
                        st.warning(f"{marker}: {status}")

                        st.write(f"Value: {details['value']}")
                        st.write(f"Range: {details['range']}")
                        st.caption(details["explanation"])
                        st.divider()

                else:
                    st.error("Backend error")

            except Exception as e:
                st.error(f"Connection failed: {e}")