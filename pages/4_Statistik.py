from utils.login_manager import LoginManager
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.data_manager import DataManager

# ---verweise den Benutzer zur Login-Seite, falls nicht eingeloggt---
LoginManager().go_to_login('Start.py')

# ---Titel und Logo---
cols = st.columns([3, 1])
with cols[0]:
    st.title("Statistik")
with cols[1]:
    st.image("https://drive.switch.ch/index.php/s/NQzo46BcGfLbd3Z/download", width=150)


# ---prüft, ob data_df im Session-State vorhanden ist, wenn nicht, ladet es---
if "data_df" not in st.session_state:
    DataManager().load_user_data(
        session_state_key='data_df',
        file_name='data.csv'
    )

# ---Hintergrundbild mit Overlay---
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

# ---Überprüfe, ob data_df leer ist---
if "data_df" not in st.session_state or st.session_state["data_df"].empty:
    st.info('Keine Daten vorhanden. Bitte lösen Sie das Quiz.')
else:
    data_df = st.session_state["data_df"]

    # ---Anzahl Richtige und Falsche in % pro Modus + Durschschnttswerte---
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

# ---Daten für die Grafik vorbereiten---
st.subheader("Richtige Antworten pro Quiz-Durchlauf")
data_df = data_df.copy()
data_df["timestamp"] = pd.to_datetime(data_df["timestamp"], errors="coerce")
data_df = data_df.sort_values("timestamp")
data_df = data_df.reset_index(drop=True)
data_df["Durchlauf"] = data_df.index + 1  

fig, ax = plt.subplots()

# --- Grafik verlauf Anzahl Richtige Antworten pro Quiz-Durchlauf für jeden Modus---
df_low = data_df[data_df["quiz_mode"] == "Low Brain Power"]
line1 = ax.plot(df_low["Durchlauf"], df_low["correct_count"], color="blue", marker="o", label="Low Brain Power")
if not df_low.empty:
    mean_low = df_low["correct_count"].mean()
    line2 = ax.axhline(mean_low, color="blue", linestyle="--", linewidth=2, label="Low Brain Power Durchschnitt")

df_more = data_df[data_df["quiz_mode"] == "A Little More Brain Power"]
line3 = ax.plot(df_more["Durchlauf"], df_more["correct_count"], color="hotpink", marker="o", label="A Little More Brain Power")
if not df_more.empty:
    mean_more = df_more["correct_count"].mean()
    line4 = ax.axhline(mean_more, color="hotpink", linestyle="--", linewidth=2, label="A Little More Brain Power Durchschnitt")

ax.set_xlabel("Quiz-Durchlauf")
ax.set_ylabel("Richtige Antworten")
ax.grid(True)
ax.legend(loc="center left", bbox_to_anchor=(1, 0.5))  
st.pyplot(fig)

# ---Button für die Navigation zur Antwort Übersicht---
if st.button("zur Antwort Übersicht"):
    st.switch_page("pages/3_Antwort Übersicht.py")
