# 💰 AI Destekli Kişisel Finans Asistanı

Bu proje, yapay zeka (LLM) kullanarak kişisel harcama metinlerinizi analiz eden, kategorilere ayıran ve tasarruf önerileri sunan tam kapsamlı bir uygulamadır.

## 🏗 Mimari

Proje iki ana bileşenden oluşur:
1.  **Backend (FastAPI):** `backend/` klasöründe bulunur. LLM servisine bağlanır ve harcama analiz mantığını yönetir.
2.  **Frontend (Streamlit):** `frontend/` klasöründe bulunur. Kullanıcıdan veri alır ve sonuçları görselleştirir.

## 🚀 Kurulum

1.  **Gereksinimleri Yükleyin**
    ```bash
    pip install -r requirements.txt
    ```

2.  **API Anahtarlarını Ayarlayın**
    Ana dizinde `.env` adlı bir dosya oluşturun ve içine Google (Gemini) veya Groq API anahtarlarınızı ekleyin:
    ```ini
    GEMINI_API_KEY=AIzaSxxxx
    GROQ_API_KEY=gsk_xxxx
    ```

## 🏃‍♂️ Çalıştırma

Projenin çalışması için **iki ayrı terminal** kullanmanız gerekir.

### 1. Backend'i Başlatma
Proje ana dizininde:
```bash
uvicorn backend.app:app --reload
```
API adresi: `http://127.0.0.1:8000`

### 2. Frontend'i Başlatma
Yeni bir terminalde, proje ana dizininde:
```bash
streamlit run frontend/app.py
```
Uygulama tarayıcıda otomatik açılacaktır (Genellikle `http://localhost:8501`).

## 📁 Proje Yapısı

```
.
├── backend/
│   ├── app.py       # FastAPI servisi
│   ├── agent.py     # AI Agent mantığı
│   └── prompts.py   # AI sistem istemleri (Prompts)
├── frontend/
│   └── app.py       # Streamlit arayüzü
├── .env             # API anahtarları (Gizli)
├── requirements.txt # Kütüphaneler
└── README.md        # Dokümantasyon
```

## 🛠 Kullanılan Teknolojiler
*   FastAPI
*   Streamlit
*   Google Gemini Pro / Flash
*   Groq API (Llama 3)
