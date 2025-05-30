import streamlit as st
import pandas as pd
from datetime import datetime
from utils.data_manager import DataManager
from utils.login_manager import LoginManager
import random

# ---Initialisiere den DataManager---
data_manager = DataManager(fs_protocol="webdav", fs_root_folder="Quiz_LN_Informatik")

# ---Verweise den Benutzer zur Login-Seite, falls nicht eingeloggt---
LoginManager().go_to_login('Start.py')

# ---Lade die Quizfragen--- 
data_manager.load_app_data(
    session_state_key="Fragen_Parasitologie_df",
    file_name="parasitologie_fragen.csv"
)

# ---Quiz-Modus wird ausgelesen---
quiz_mode = st.session_state.get("quiz_mode", "Unbekannt")

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

# ---Titel und Logo---
cols = st.columns([3, 1])
with cols[0]:
    st.title("PathoLogic-Quiz")
with cols[1]:
    st.image("https://drive.switch.ch/index.php/s/NQzo46BcGfLbd3Z/download", width=150)

# ---Hinweis für den Nutzer---
st.markdown('Bestätige deine Antwort mit einem Doppelklick auf "Weiter".')

# ---Quiz-start Funktion (je nach Modus 10 oder 20 Fragen)---
def start_quiz(df):
    for key in ["random_questions", "user_answers", "current_question_index", "results_saved"]:
        st.session_state.pop(key, None)
    quiz_mode = st.session_state.get("quiz_mode", "Low Brain Power")
    if quiz_mode == "A Little More Brain Power":
        num_questions = 20
        st.title("A Little More Brain Power")
    else:
        num_questions = 10
        st.title("Low Brain Power")
    df = df.sample(frac=1).reset_index(drop=True)
    question_list = df.sample(
        n=min(num_questions, len(df)), random_state=None
    ).to_dict(orient="records")
    st.session_state["random_questions"] = question_list
    st.session_state["user_answers"] = {}
    st.session_state["current_question_index"] = 0
    st.session_state["results_saved"] = False  

# ---prüfen ob Fragen bereits im Session State gespeichert wurden---
if "Fragen_Parasitologie_df" in st.session_state:
    df = st.session_state["Fragen_Parasitologie_df"]

    # ---Button zum Starten des Quiz je nach Modus---
    if st.button("Quiz starten"):
        start_quiz(df)
    
    # ---zeigt die Fragen und Antwortmöglichkeiten & speichert die Antworten des Nutzers---
    if "random_questions" in st.session_state:
        questions = st.session_state["random_questions"]
        total_questions = len(questions)
        current_index = st.session_state.get("current_question_index", 0)
        question = questions[current_index]

        st.subheader(f"Frage {current_index + 1} von {total_questions}")
        st.markdown(f"<h2 style='font-size:24px;'>{question['question']}</h2>", unsafe_allow_html=True)

        if pd.notna(question.get("images")) and question["images"].strip():
            st.image(question["images"], caption="Bild zur Frage", use_container_width=True)

        answer_key = f"answer_{current_index}"
        user_answer = st.radio(
            "Wähle eine Antwort:",
            options=[question['answer_a'], question['answer_b'], question['answer_c'], question['answer_d']],
            key=answer_key
        )
        st.session_state["user_answers"][current_index] = {
            "question": question["question"],
            "correct_answer": question["correct_answer"],
            "user_answer": user_answer if user_answer else ""
        }

        # ---Buttons zur Navigation zwischen Fragen---
        cols = st.columns(3)
        with cols[0]:
            if current_index > 0:
                if st.button("← Zurück", key=f"back_{current_index}"):
                    st.session_state["current_question_index"] -= 1

        with cols[2]:
            if current_index < total_questions - 1:
                if st.button("Weiter →", key=f"next_{current_index}"):
                    st.session_state["current_question_index"] += 1
            else:
                if not st.session_state.get("results_saved", False):
                    if st.button("Auswertung anzeigen"):
                        st.session_state["show_results"] = True

                # ---Auswertung ---
                if st.session_state.get("show_results", False):
                    correct_count = 0
                    incorrect_count = 0
                    incorrect_questions = []
                    
                    # ---Sammle alle Antworten---
                    all_answers = []
                    for i in range(total_questions):
                        answer_data = st.session_state["user_answers"].get(i)
                        if not answer_data:
                            continue
                        if answer_data["user_answer"] == answer_data["correct_answer"]:
                            correct_count += 1
                        else:
                            incorrect_count += 1
                            incorrect_questions.append(answer_data)
                        all_answers.append(
                            f"Frage: {answer_data['question']} | Deine Antwort: {answer_data['user_answer']} | Richtig: {answer_data['correct_answer']}"
                        )
                
                    # ---Ergebnisse anzeigen---
                    with st.container():
                        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
                        st.success(f"Richtige Antworten: {correct_count}")
                        st.error(f"Falsche Antworten: {incorrect_count}")
                        st.markdown("</div>", unsafe_allow_html=True)

                    # ---Falsch beantwortete Fragen anzeigen---
                    if incorrect_questions:
                        st.write("Falsch beantwortete Fragen:")
                        for q in incorrect_questions:
                            st.markdown(f"""
                            - **Frage:** {q['question']}
                                - **Deine Antwort:** <span style='color:red'>{q['user_answer']}</span>  
                                - **Richtige Antwort:** <span style='color:green'>{q['correct_answer']}</span>
                            """, unsafe_allow_html=True)
                
                    # --- Antworten speichern ---
                    if not st.session_state.get("results_saved", False):
                        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        user = st.session_state.get("name", "Unbekannt")
                        record = {
                            "timestamp": timestamp,
                            "user": user,
                            "quiz_mode": st.session_state.get("quiz_mode", "Low Brain Power"),
                            "correct_count": correct_count,
                            "incorrect_count": incorrect_count,
                            "answers": " || ".join(all_answers)
                        }
                        try:
                            DataManager().append_record(
                                session_state_key="data_df",
                                record_dict=record
                            )
                            st.success("Quiz-Daten wurden gespeichert.")
                            st.session_state["results_saved"] = True
                        except Exception as e:
                            st.error(f"Fehler beim Speichern der Antwort: {e}")
                    st.success("Alle Antworten wurden gespeichert.")


                    # ---Navigation nach dem Quiz---
                    button_cols = st.columns(2)
                    with button_cols[0]:
                        if st.button("zur Antwort Übersicht"):
                            st.switch_page("pages/3_Antwort Übersicht.py")

                    with button_cols[1]:
                        if st.button("zur Statistik"):
                            st.switch_page("pages/4_Statistik.py") 