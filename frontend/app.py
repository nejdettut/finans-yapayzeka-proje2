import streamlit as st
import sys
import os

# Backend modülüne erişim sağla (Streamlit Cloud için)
# Bu dosya frontend/ klasöründe olduğu için bir üst dizini (root) path'e ekliyoruz.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.agent import run_finance_agent

# SAYFA BAŞLIĞI VE AÇIKLAMA
st.set_page_config(page_title="AI Finance Agent", layout="centered")

st.title("💰 AI Destekli Kişisel Finans Asistanı")
st.write(
    "Harcama metninizi girin, yapay zeka harcamalarınızı analiz edip "
    "tasarruf önerileri sunsun."
)

# KULLANICIDAN HARCAMA METNİ ALMA
user_input = st.text_area(
    "Harcama bilgilerinizi girin:",
    height=150,
    placeholder="Örnek: Kira 12.000, yemek 6.000, eğlence 4.000..."
)

# BUTON VE İŞLEM
if st.button("Analiz Et"):
    if user_input.strip() == "":
        st.warning("Lütfen harcama bilgisi girin.")
    else:
        with st.spinner("Analiz yapılıyor..."):
            try:
                # API yerine doğrudan fonksiyonu çağırıyoruz
                # result zaten dict olarak dönüyor (backend/agent.py güncellemiştik)
                result = run_finance_agent(user_input)
                
                # SONUÇLARI GÖSTERME
                if "expenses" in result:
                    st.subheader("📌 Ayıklanan Harcamalar")
                    st.write(result["expenses"])

                    st.subheader("📊 Kategoriler")
                    st.write(result["categories"])

                    st.subheader("⚠️ Analiz & Riskler")
                    st.write(result["analysis"])
                    
                    st.subheader("💡 Tasarruf Önerileri")
                    st.write(result.get("suggestion", ""))
                elif "error" in result: # Agent'tan bir hata sözlüğü dönerse
                     st.error(f"Hata: {result['error']}")
                else: # Fallback
                     st.write(result)
            
            except Exception as e:
                st.error(f"Bir hata oluştu: {str(e)}")
