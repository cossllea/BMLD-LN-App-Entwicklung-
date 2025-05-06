import streamlit as st
import pandas as pd
import io
from utils.data_manager import DataManager



data_manager = DataManager(fs_protocol= "webdav", fs_root_folder="Quiz_LN_Informatik")

data_manager.load_app_data(
    session_state_key= "Fragen_Parasitologie_df",
    file_name = "parasitologie_fragen.csv")

st.title("10 zufällige Fragen")


# Überprüfen, ob der DataFrame existiert
if "Fragen_Parasitologie_df" in st.session_state:
    # Generiere die zufälligen Fragen nur einmal und speichere sie im Session State
    if "random_questions" not in st.session_state:
        # Wähle 10 zufällige Fragen ohne Wiederholungen
        st.session_state["random_questions"] = st.session_state["Fragen_Parasitologie_df"].sample(n=10, replace=False)

    # Fragen und Antwortmöglichkeiten anzeigen
    random_questions = st.session_state["random_questions"]
    for i, row in enumerate(random_questions.iterrows(), start=1):
        st.subheader(f"Frage {i}: {row[1]['Frage']}")
        st.radio(
            "Wähle eine Antwort:",
            options=[row[1]['A'], row[1]['B'], row[1]["C"], row[1]['D']],
            key=f"question_{i}"
        )
else:
    st.error("Der DataFrame konnte nicht geladen werden. Bitte überprüfe die Datenquelle.")

