import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#  remonte d'un niveau : pages/ → rag_project/
from extraction import process_pdf
import streamlit as st
import pdfplumber
import io
from sklearn.feature_extraction.text import TfidfVectorizer
from model import model
import joblib

st.set_page_config(page_title="Resume Analysis")
st.markdown("""
    <style>
    [data-testid="stSidebarNav"] {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

# Vérifier si le PDF existe dans session_state
if "pdf_bytes" in st.session_state:

    pdf_bytes = st.session_state["pdf_bytes"] #contenu du pdf 
    pdf_nom = st.session_state["pdf_nom"] # nom du pdf

    st.write(f"Fichier reçu : {pdf_nom}")

    # Convertir bytes → fichier lisible par pdfplumber
    pdf_file = io.BytesIO(pdf_bytes)

    text, tables = process_pdf(pdf_file)

    print("TEXT:\n", text)
    print("\nTABLES:\n", tables)

else:
    st.warning("Aucun PDF chargé !")


#data cleaning 
text=text.lower()
text=text.replace("\n","")
tokens=text.split()

#vectorisation
vectorizer = joblib.load("vectorizer.pkl")
model = joblib.load("model.pkl")

X = vectorizer.transform([text])

#prediction for a new resume
y=model.predict(X)


st.markdown(
     f"""
    <style>
    .stApp {{
        background-color:#EBF2FA;
       
    }}
    </style>
    """,unsafe_allow_html=True
)


st.markdown(
    f"<p style='color:#003C57;'>category: {y[0]}</p>",
    unsafe_allow_html=True
)

