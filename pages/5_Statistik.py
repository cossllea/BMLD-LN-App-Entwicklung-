import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.data_manager import DataManager

st.title("Statistik")

# Lade data_df, falls noch nicht vorhanden
if "data_df" not in st.session_state:
    DataManager().load_user_data(
        session_state_key='data_df',
        file_name='data.csv'
    )

if "data_df" not in st.session_state or st.session_state["data_df"].empty:
    st.info('Keine Daten vorhanden. Bitte löse das Quiz.')
else:
    data_df = st.session_state["data_df"]
    # Filtere ungültige Zeilen raus
    data_df = data_df.dropna(subset=["timestamp", "question", "user_answer", "correct_answer"], how="any")
    # Korrektur-Spalte berechnen
    data_df["Korrektur"] = data_df["user_answer"] == data_df["correct_answer"]
    data_df["Korrektur"] = data_df["Korrektur"].map({True: "Richtig", False: "Falsch"})

    # Prüfe, ob die Spalte für den Modus existiert
    if "quiz_mode" not in data_df.columns:
        st.warning("Es gibt keine Spalte 'quiz_mode' in den Daten. Bitte ergänze diese beim Speichern der Antworten!")
    else:
        for mode in ["Low Brain Power", "A Little More Brain Power"]:
            st.subheader(f"Ergebnisse für: {mode}")
            df_mode = data_df[data_df["quiz_mode"] == mode]
            if df_mode.empty:
                st.info(f"Keine Daten für {mode}.")
            else:
                counts = df_mode["Korrektur"].value_counts()
                fig, ax = plt.subplots()
                counts.plot.pie(
                    labels=counts.index,
                    autopct='%1.1f%%',
                    colors=['green', 'red'],
                    ax=ax
                )
                ax.set_ylabel("")
                ax.set_title(f"Richtig/Falsch ({mode})")
                st.pyplot(fig)