from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  

import streamlit as st
from utils.data_manager import DataManager

st.title('Antwort Übersicht')

# Lade data_df, falls noch nicht vorhanden
if "data_df" not in st.session_state:
    DataManager().load_user_data(
        session_state_key='data_df',
        file_name='data.csv'
    )

if "data_df" not in st.session_state or st.session_state["data_df"].empty:
    st.info('Keine Daten vorhanden. Bitte lösen Sie das Quiz.')
else:
    data_df = st.session_state["data_df"]
    # Nur Zeilen behalten, die echte Antworten sind
    data_df = data_df.dropna(subset=["timestamp", "question", "user_answer", "correct_answer"], how="any")
    if data_df.empty:
        st.info('Noch keine Antworten im neuen Format vorhanden.')
    else:
        # Index einmalig zurücksetzen (nur für die Anzeige)
        data_df = data_df.reset_index(drop=True)
        data_df["Korrektur"] = data_df["user_answer"] == data_df["correct_answer"]
        data_df["Korrektur"] = data_df["Korrektur"].map({True: "Richtig", False: "Falsch"})
        st.dataframe(
            data_df[["timestamp", "question", "user_answer", "correct_answer", "Korrektur"]],
            use_container_width=True
        )