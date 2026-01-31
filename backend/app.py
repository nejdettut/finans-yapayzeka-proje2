from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import os

# Agent fonksiyonunu import et
from agent import run_financial_advisor_agent

app = FastAPI(
    title="AI Finance Agent API",
    description="Kişisel finans ve harcama analiz servisi",
    version="1.0"
)

class FinanceRequest(BaseModel):
    text: str
    provider: str = "gemini"

@app.get("/")
def home():
    return {"message": "AI Finance Agent API Çalışıyor!"}

@app.post("/analyze")
def analyze_finances(request: FinanceRequest):
    try:
        # Agent'i çalıştır - Sonuç artık bir sözlük (dict) dönüyor
        result_dict = run_financial_advisor_agent(request.text, request.provider)
        return result_dict
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
