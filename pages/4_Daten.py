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
    # Zeige die Quiz-Datensätze an
    st.dataframe(
        data_df[["timestamp", "user", "quiz_mode", "correct_count", "incorrect_count", "answers"]],
        use_container_width=True
    )