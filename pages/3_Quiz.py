import streamlit as st
import pandas as pd
import io
from datetime import datetime
from utils.data_manager import DataManager
from utils.login_manager import LoginManager
import random

LoginManager().go_to_login('Start.py') 

data_manager = DataManager(fs_protocol= "webdav", fs_root_folder="Quiz_LN_Informatik")

data_manager.load_app_data(
    session_state_key= "Fragen_Parasitologie_df",
    file_name = "parasitologie_fragen.csv")

st.title("10 zufällige Fragen")

def start_quiz(df):
    """
    Funktion zum Starten oder Zurücksetzen des Quiz.
    Generiert 10 zufällige Fragen und initialisiert die Benutzerantworten.
    """
    # Lösche vorherige Fragen aus dem Session State
    if "random_questions" in st.session_state:
        del st.session_state["random_questions"]
    if "user_answers" in st.session_state:
        del st.session_state["user_answers"]
    if "current_question_index" in st.session_state:
        del st.session_state["current_question_index"]


    # Lade den DataFrame neu und mische die Reihenfolge
    df = df.sample(frac=1).reset_index(drop=True)

    # Generiere neue 10 zufällige Fragen
    question_list = df.drop_duplicates(subset="question").sample(
        n=min(10, len(df)), random_state=None
    ).to_dict(orient="records")

    # Speichere die neuen Fragen und initialisiere die Benutzerantworten
    st.session_state["random_questions"] = question_list
    st.session_state["user_answers"] = {}  # Initialisiere die Benutzerantworten
    st.session_state["current_question_index"] = 0

# Überprüfen, ob der DataFrame existiert
if "Fragen_Parasitologie_df" in st.session_state:
    # DataFrame aus dem Session State abrufen
    df = st.session_state["Fragen_Parasitologie_df"]

    # Quiz Button:
    if st.button("Quiz starten"):
        start_quiz(df)

    # Fragen und Antwortmöglichkeiten anzeigen
    if "random_questions" in st.session_state:
        questions = st.session_state["random_questions"]
        total_questions = len(questions)
        current_index = st.session_state.get("current_question_index", 0)
        question = questions[current_index]

        st.subheader(f"Frage {current_index + 1} von {total_questions}")
        st.markdown(f"<h2 style='font-size:24px;'>{question['question']}</h2>", unsafe_allow_html=True)


        

         # Überprüfe, ob ein Bild vorhanden ist, und zeige es an
        if pd.notna(question.get('images')):  # Prüfe, ob die Spalte 'image' nicht leer ist
            st.image(question["images"], caption="Bild zur Frage", use_container_width=True)

        user_answer = st.radio(
            "Wähle eine Antwort:",
            options=[question['answer_a'], question['answer_b'], question["answer_c"], question['answer_d']],
            key=f"question_{current_index}"
        )

        # Speichere die Benutzerantwort
        if user_answer != "Bitte wählen":
            st.session_state["user_answers"][current_index] = {
                "question": question['question'],
                "correct_answer": question['correct_answer'],
                "user_answer": user_answer
            }
        # Navigationsbuttons
        cols = st.columns(3)
        with cols[0]:
            if current_index > 0:
                if st.button("← Zurück"):
                    st.session_state["current_question_index"] -= 1

        with cols[2]:
            if current_index < total_questions - 1:
                if st.button("Weiter →"):
                    st.session_state["current_question_index"] += 1
            else:
                # Initialisiere die Variablen
                correct_count = 0
                incorrect_count = 0
                incorrect_questions = []

                #Auswertung anzeigen
                if st.button("Auswertung anzeigen"):
                    if "user_answers" in st.session_state:
                        correct_count = 0
                        incorrect_count = 0 
                        incorrect_questions = []

                        for i in range(total_questions):
                            answer_data = st.session_state["user_answers"][i]
                            if answer_data["user_answer"] == answer_data["correct_answer"]:
                                correct_count += 1
                            else:
                                incorrect_count += 1
                                incorrect_questions.append({
                                    "question": answer_data["question"],
                                    "correct_answer": answer_data["correct_answer"],
                                    "user_answer": answer_data["user_answer"]
                                })

                        # Zentriere die Auswertung mit einem Container
                        with st.container():
                            st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
                            st.success(f"Richtige Antworten: {correct_count}")
                            st.error(f"Falsche Antworten: {incorrect_count}")
                            st.markdown("</div>", unsafe_allow_html=True)

                        if incorrect_questions:
                            st.write("Falsch beantwortete Fragen:")
                            for q in incorrect_questions:
                                st.markdown(f"""
                                - **Frage:** {q['question']}
                                    - **Deine Antwort:** <span style='color:red'>{q['user_answer']}</span>  
                                    - **Richtige Antwort:** <span style='color:green'>{q['correct_answer']}</span>
                                """, unsafe_allow_html=True)

                        # --- Antworten speichern ---
                        from datetime import datetime
                        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        user = st.session_state.get("name", "Unbekannt")
                        for i in range(total_questions):
                            answer_data = st.session_state["user_answers"][i]
                            record = {
                                "timestamp": timestamp,
                                "user": user,
                                "question": answer_data["question"],
                                "user_answer": answer_data["user_answer"],
                                "correct_answer": answer_data["correct_answer"]
                            }
                            try:
                                DataManager().append_record(
                                    session_state_key="data_df",
                                    record_dict=record
                                )
                            except Exception as e:
                                st.error(f"Fehler beim Speichern der Antwort: {e}")
                        st.success("Alle Antworten wurden gespeichert.")
                                    

                                

                


