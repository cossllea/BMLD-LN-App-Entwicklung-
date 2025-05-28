from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  
import pandas as pd
import streamlit as st
from utils.data_manager import DataManager

cols = st.columns([3, 1])
with cols[0]:
    st.title("Antwort Übersicht")
with cols[1]:
    st.image("https://drive.switch.ch/index.php/s/NQzo46BcGfLbd3Z/download", width=150)

# Lade data_df, falls noch nicht vorhanden
if "data_df" not in st.session_state:
    DataManager().load_user_data(
        session_state_key='data_df',
        file_name='data.csv'
    )

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://drive.switch.ch/index.php/s/ZbkH4TCqVX6LLOZ/download");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    /* Overlay für bessere Lesbarkeit */
    .block-container {
        background: rgba(255, 255, 255, 0.85);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 4px 32px rgba(0,0,0,0.07);
        margin-top: 2rem;
        margin-bottom: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if "data_df" not in st.session_state or st.session_state["data_df"].empty:
    st.info('Keine Daten vorhanden. Bitte lösen Sie das Quiz.')
else:
    data_df = st.session_state["data_df"]
    for idx, row in data_df.iterrows():
        with st.expander(f"{row['timestamp']} | {row['user']} | {row['quiz_mode']} | Richtig: {row['correct_count']} | Falsch: {row['incorrect_count']}"):
            # Antworten in DataFrame umwandeln
            qa_list = [x.strip() for x in row["answers"].split("||")]
            qa_df = pd.DataFrame([q.split(" | ") for q in qa_list], columns=["Frage", "Deine Antwort", "Richtig"])
            # Präfixe entfernen
            qa_df["Frage"] = qa_df["Frage"].str.replace("Frage: ", "", regex=False)
            qa_df["Deine Antwort"] = qa_df["Deine Antwort"].str.replace("Deine Antwort: ", "", regex=False)
            qa_df["Richtig"] = qa_df["Richtig"].str.replace("Richtig: ", "", regex=False)
            # Spalte umbenennen
            qa_df = qa_df.rename(columns={"Richtig": "Richtige Antwort"})
            # Index entfernen
            qa_df = qa_df.reset_index(drop=True)
            st.dataframe(qa_df, use_container_width=True, hide_index=True)
        

if st.button("Zur Statistik"):
    st.switch_page("pages/4_Statistik.py")