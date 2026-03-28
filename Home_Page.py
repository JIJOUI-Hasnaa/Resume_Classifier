import streamlit as st


st.set_page_config(page_title="Home page")


st.markdown(
     f"""
    <style>
    .stApp {{
        #background-color:#B6D8F2;
        background-image: url("https://f.hellowork.com/seo/cv/screenshot/metier/moderateur.jpeg");
        background-size: 50%;
        background-repeat: no-repeat;
        background-position: top right;
    }}
    </style>
    """,unsafe_allow_html=True
)

st.sidebar.markdown(
    "<h2 style='color:#7D4FFE;'>Resume Classifier</h2>",
    unsafe_allow_html=True
)

st.sidebar.markdown(
    "<p style='color:#5B374D;'>Drop your cv right here</p>",
    unsafe_allow_html=True
)

fichier = st.sidebar.file_uploader("upload a pdf", type=["pdf"])

if fichier is not None:
    # Stocker dans session_state
    st.session_state["pdf_bytes"] = fichier.read()
    st.session_state["pdf_nom"] = fichier.name
    st.success(f"{fichier.name} chargé !")

    # Bouton pour aller à la page de traitement
    if st.button("Traiter le document →"):
        st.switch_page("pages/Resume_Analysis.py")







st.markdown(
    """
    <style>
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #D2D2EB;
    }
    </style>
    """,
    unsafe_allow_html=True
)
