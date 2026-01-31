import streamlit as st
import requests

# SAYFA BAŞLIĞI VE AÇIKLAMA
st.set_page_config(page_title="AI Finance Agent", layout="centered")

st.title("💰 AI Destekli Kişisel Finans Asistanı")
st.write(
    "Harcama metninizi girin, yapay zeka harcamalarınızı analiz edip "
    "tasarruf önerileri sunsun."
)

#  KULLANICIDAN HARCAMA METNİ ALMA
user_input = st.text_area(
    "Harcama bilgilerinizi girin:",
    height=150,
    placeholder="Örnek: Kira 12.000, yemek 6.000, eğlence 4.000..."
)

#  API ADRESİ
API_URL = "http://127.0.0.1:8000/analyze"

# API’YE İSTEK GÖNDERME
if st.button("Analiz Et"):
    if user_input.strip() == "":
        st.warning("Lütfen harcama bilgisi girin.")
    else:
        with st.spinner("Analiz yapılıyor..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"text": user_input}
                )
                if response.status_code == 200:
                    result = response.json()
                    
                    #  SONUÇLARI GÖSTERME
                    if "expenses" in result:
                        st.subheader("📌 Ayıklanan Harcamalar")
                        st.write(result["expenses"])

                        st.subheader("📊 Kategoriler")
                        st.write(result["categories"])

                        st.subheader("⚠️ Analiz & Riskler")
                        st.write(result["analysis"])
                        
                        st.subheader("💡 Tasarruf Önerileri")
                        st.write(result.get("suggestion", "")) # User forgot this in snippet but it's crucial
                    elif "result" in result:
                        # Fallback for old backend
                        st.write(result["result"])
                    elif "error" in result:
                        st.error(f"Hata: {result['error']}")
                else:
                    st.error(f"Sunucu hatası: {response.status_code}")
            except Exception as e:
                st.error(f"Bağlantı hatası: {str(e)}")
