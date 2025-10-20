# app.py

import os
from dotenv import load_dotenv
import streamlit as st
from datasets import load_dataset
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain

# --------------------------
# 1️⃣ .env Dosyasını Yükle
# --------------------------
load_dotenv()  # .env dosyasındaki değişkenleri alır

HF_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

if not HF_TOKEN:
    st.error("Huggingface token bulunamadı! Lütfen .env dosyasına ekleyin.")
    st.stop()
if not GEMINI_KEY:
    st.error("Gemini API key bulunamadı! Lütfen .env dosyasına ekleyin.")
    st.stop()

os.environ["OPENAI_API_KEY"] = GEMINI_KEY  # Gemini API key olarak geçer

# --------------------------
# 2️⃣ Streamlit Başlığı
# --------------------------
st.set_page_config(page_title="Kitap Asistanı Chatbot", page_icon="📚")
st.title("📚 Kitap Asistanı Chatbot (.env Destekli)")

# --------------------------
# 3️⃣ Veri Seti Yükleme
# --------------------------
@st.cache_data
def load_data():
    dataset = load_dataset("alibayram/kitapyurdu_yorumlar", use_auth_token=HF_TOKEN)
    df = dataset['train'].to_pandas().head(500)  # hızlı prototip
    return df

df = load_data()
st.write("Veri setinden örnek yorumlar:", df.head(3))

# --------------------------
# 4️⃣ Embedding ve Vektör Database
# --------------------------
@st.cache_resource
def create_vectorstore(df):
    embeddings = OpenAIEmbeddings()
    vectordb = Chroma.from_texts(df['yorum'].tolist(), embedding=embeddings)
    return vectordb

vectordb = create_vectorstore(df)

# --------------------------
# 5️⃣ RAG Pipeline
# --------------------------
@st.cache_resource
def create_rag_chain(vectordb):
    llm = ChatOpenAI(temperature=0)  # Gemini API key kullanıyor
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectordb.as_retriever()
    )
    return chain

rag_chain = create_rag_chain(vectordb)

# --------------------------
# 6️⃣ Chat Arayüzü
# --------------------------
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

user_input = st.text_input("Sorunuzu buraya yazın:")

if user_input:
    with st.spinner("Cevap oluşturuluyor..."):
        result = rag_chain({"question": user_input, "chat_history": st.session_state['chat_history']})
        answer = result['answer']
        st.session_state['chat_history'].append((user_input, answer))
        st.write("**Cevap:**", answer)

# --------------------------
# 7️⃣ Sohbet Geçmişi
# --------------------------
if st.session_state['chat_history']:
    st.write("### Sohbet Geçmişi")
    for i, (q, a) in enumerate(st.session_state['chat_history']):
        st.markdown(f"**Soru {i+1}:** {q}")
        st.markdown(f"**Cevap {i+1}:** {a}")
        st.write("---")

# --------------------------
# 8️⃣ Çalıştırma Talimatı
# --------------------------
st.write("💡 Kodun çalışması için terminalde şu komut kullanılabilir:")
st.code("streamlit run app.py")
