from fastapi import FastAPI, UploadFile, File, Form
import tempfile

from app.extractor import extract_text_from_pdf
from app.parser import extract_with_llm
from app.analyzer import analyze_health


app = FastAPI(title="AI Clinical Assistant API")


@app.get("/")
def home():
    return {"message": "AI Clinical Assistant Running"}


@app.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    age: int = Form(...),
    gender: str = Form(...),
    symptoms: str = Form("")
):

    # Save uploaded PDF
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        content = await file.read()
        tmp.write(content)
        pdf_path = tmp.name

    # Extract text
    text = extract_text_from_pdf(pdf_path)

    # Extract lab values
    values = extract_with_llm(text)

    # Analyze health
    analysis = analyze_health(values)
    
    # Build intelligent summary
    abnormal_markers =[
    name for name, data in analysis.items()
    if data["status"] in ["HIGH", "LOW"]
    ]
    
    if abnormal_markers:
        findings = ", ".join(abnormal_markers)
        summary_text = (
        f"{age}-year-old {gender} patient. "
        f"Abnormal findings detected in: {findings}."
        )
    else:
        summary_text = (
        f"{age}-year-old {gender} patient. "
        f"All tested parameters are within normal range."
    )
    
    return{
    "summary": summary_text,
    "risks": analysis,
    "tests": ["Blood Sugar Test", "Vitamin D Test"],
    "medications": "Consult physician if abnormalities persist",
    "notes": "AI generated clinical insight"
}
    
    