from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.data_manager import DataManager

cols = st.columns([3, 1])
with cols[0]:
    st.title("Statistik")
with cols[1]:
    st.image("https://drive.switch.ch/index.php/s/NQzo46BcGfLbd3Z/download", width=150)


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

    if "quiz_mode" not in data_df.columns:
        st.warning("Es gibt keine Spalte 'quiz_mode' in den Daten. Bitte ergänze diese beim Speichern der Antworten!")
    else:
        for mode in ["Low Brain Power", "A Little More Brain Power"]:
            st.subheader(f"Ergebnisse für: {mode}")
            df_mode = data_df[data_df["quiz_mode"] == mode]
            if df_mode.empty:
                st.info(f"Keine Daten für {mode}.")
            else:
                total = len(df_mode)
                correct = df_mode["correct_count"].astype(int).sum()
                incorrect = df_mode["incorrect_count"].astype(int).sum()
                fig, ax = plt.subplots()
                ax.pie(
                    [correct, incorrect],
                    labels=["Richtig", "Falsch"],
                    autopct='%1.1f%%',
                    colors=['green', 'red']
                )
                ax.set_title(f"Richtig/Falsch ({mode})")
                st.pyplot(fig)
                st.write(f"Durchschnitt richtige Antworten: {df_mode['correct_count'].mean():.2f}")
                st.write(f"Durchschnitt falsche Antworten: {df_mode['incorrect_count'].mean():.2f}")