import os
from dotenv import load_dotenv
import google.generativeai as genai
from groq import Groq

# Prompts.py'dan import (User'ın istediği isimlendirmeleri alias ile map ediyoruz)
try:
    from prompts import (
        SYSTEM_PROMPT,
        EXPENSE_EXTRACTION_PROMPT as ANALYZE_PROMPT,
        EXPENSE_CATEGORIZATION_PROMPT as CATEGORY_PROMPT,
        ANALYSIS_PROMPT as RISK_PROMPT,
        SAVINGS_SUGGESTION_PROMPT as SUGGESTION_PROMPT
    )
except ImportError:
    # Eğer backend klasöründen veya dışından çalıştırılırsa path sorunu olabilir diye
    from backend.prompts import (
        SYSTEM_PROMPT,
        EXPENSE_EXTRACTION_PROMPT as ANALYZE_PROMPT,
        EXPENSE_CATEGORIZATION_PROMPT as CATEGORY_PROMPT,
        ANALYSIS_PROMPT as RISK_PROMPT,
        SAVINGS_SUGGESTION_PROMPT as SUGGESTION_PROMPT
    )

load_dotenv()

# Client'ları hazırla
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def call_llm(prompt: str, provider: str = "gemini") -> str:
    """
    LLM'e istek atan birleşik fonksiyon.
    System prompt'u varsayılan olarak modele vermek daha iyi olabilir, 
    ancak buradaki tasarımda her adımda prompt'un içine gömeceğiz veya 
    her çağrıda system instruction olarak vereceğiz.
    Gemini flash system_instruction destekler.
    """
    try:
        if provider == "gemini":
            # System prompt ile model oluşturuyoruz
            model = genai.GenerativeModel(
                "gemini-2.5-flash",
                system_instruction=SYSTEM_PROMPT
            )
            response = model.generate_content(prompt)
            return response.text
        
        elif provider == "groq":
            completion = groq_client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt}
                ]
            )
            return completion.choices[0].message.content
        
        else:
            return "Hata: Geçersiz provider."
            
    except Exception as e:
        return f"Bir hata oluştu ({provider}): {str(e)}"

def run_financial_advisor_agent(user_input: str, provider: str = "gemini"):
    print(f"--- Agent Başlatılıyor ({provider}) ---")
    
    # Adım 1: Veri Çıkarma (Extraction)
    print("1. Harcamalar ayıklanıyor...")
    step1_prompt = ANALYZE_PROMPT.format(user_input=user_input)
    expense_list = call_llm(step1_prompt, provider)
    # print(f"Çıktı 1:\n{expense_list}\n")

    # Adım 2: Kategorilendirme
    print("2. Kategorize ediliyor...")
    step2_prompt = CATEGORY_PROMPT.format(expense_list=expense_list)
    categorized_data = call_llm(step2_prompt, provider)
    # print(f"Çıktı 2:\n{categorized_data}\n")

    # Adım 3: Risk Analizi
    print("3. Risk analizi yapılıyor...")
    step3_prompt = RISK_PROMPT.format(category_data=categorized_data)
    risk_analysis = call_llm(step3_prompt, provider)
    # print(f"Çıktı 3:\n{risk_analysis}\n")
    
    # Adım 4: Tasarruf Önerileri
    print("4. Tavsiyeler hazırlanıyor...")
    step4_prompt = SUGGESTION_PROMPT.format(analysis_result=risk_analysis)
    final_output = call_llm(step4_prompt, provider)
    
    return {
        "expenses": expense_list,
        "categories": categorized_data,
        "analysis": risk_analysis,
        "suggestion": final_output
    }

if __name__ == "__main__":
    # Test Senaryosu
    ornek_metin = """
    Geçen ay kiraya 15000 TL verdim. Markete 4000 TL gitti.
    Arkadaşlarla dışarı çıktık, yemek falan 2000 TL tuttu.
    Netflix ve Spotify toplam 300 TL.
    Bir de gereksiz yere yeni bir kulaklık aldım 5000 TL'ye.
    """
    
    sonuc = run_financial_advisor_agent(ornek_metin, provider="gemini")
    print("\n=== SONUÇ ===\n")
    print(sonuc)

# Alias for compatibility with app.py
def run_finance_agent(text: str):
    return run_financial_advisor_agent(text)

