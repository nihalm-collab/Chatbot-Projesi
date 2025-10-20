# 📚 Kitap Asistanı Chatbot

Bu proje, Akbank GenAI Bootcamp kapsamında geliştirilmiş bir **RAG (Retrieval Augmented Generation)** temelli chatbot uygulamasıdır. Kullanıcılar, Kitapyurdu yorumlarını kullanarak kitaplarla ilgili sorularına cevap alabilirler.

---

## 🎯 Proje Amacı

- Kullanıcı sorularını yorumlar üzerinden yanıtlamak  
- RAG mimarisi ile retrieval ve generation kombinasyonu kullanmak  
- Web arayüzü üzerinden kolay kullanım sağlamak

---

## 🗂 Veri Seti

- **Kaynak:** [Huggingface – Kitapyurdu Yorumlar](https://huggingface.co/datasets/alibayram/kitapyurdu_yorumlar)  
- **İçerik:** Kitapyurdu’ndan alınmış kullanıcı yorumları  
- **Kullanım:** İlk 500 yorum prototip amaçlı çekildi ve Chroma vektör DB ile retrieval yapılmaktadır

---

## 🛠 Kullanılan Teknolojiler

- **LLM / Generation Model:** Gemini API (LangChain üzerinden ChatOpenAI sınıfı ile)  
- **Embedding Model:** OpenAIEmbeddings (Gemini embedding ile değiştirilebilir)  
- **Vektör Database:** Chroma  
- **RAG Pipeline:** LangChain – ConversationalRetrievalChain  
- **Web Arayüzü:** Streamlit  
- **Diğer:** Huggingface datasets, pandas, python-dotenv

---

## ⚙️ Kurulum ve Çalıştırma

1. **Repo’yu klonlayın**
```bash
git clone https://github.com/nihalm-collab/Chatbot-Projesi.git
cd Chatbot-Projesi
```
2. **Sanal ortamı oluşturun**
```bash
python -m venv venv
```
3. **Sanal ortamı aktive edin**
```bash
venv\Scripts\Activate.ps1 #Windows (Powershell) 
source venv/bin/activate #Mac/Linux
```
4. **Gerekli paketleri yükleyin**
```bash
pip install -r requirements.txt
```
5. **.env dosyasını oluşturun ve token/key ekleyin**
```bash
HUGGINGFACE_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxx
GEMINI_API_KEY= AIzxxxxxxxxxxxxxxxxxxxxx
```
6. **Chatbot’u başlatın**
```bash
streamlit run app.py
```
---

## 📂 Proje Dosya Yapısı

```bash
Chatbot-Projesi/
│
├─ app.py                # Chatbot kodu
├─ requirements.txt      # Gerekli paketler
├─ .gitignore            # Gizli ve gereksiz dosyalar
├─ LICENSE            
└─ README.md             # Proje açıklamaları ve kurulum
```
