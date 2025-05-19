import streamlit as st
import pandas as pd
from datetime import datetime
from utils.data_manager import DataManager
from utils.login_manager import LoginManager
import random

LoginManager().go_to_login('Start.py')

quiz_mode = st.session_state.get("quiz_mode", "Unbekannt")

data_manager = DataManager(fs_protocol="webdav", fs_root_folder="Quiz_LN_Informatik")
data_manager.load_app_data(
    session_state_key="Fragen_Parasitologie_df",
    file_name="parasitologie_fragen.csv"
)

st.title("10 zufällige Fragen")

def start_quiz(df):
    for key in ["random_questions", "user_answers", "current_question_index"]:
        st.session_state.pop(key, None)
    quiz_mode = st.session_state.get("quiz_mode", "Low Brain Power")
    if quiz_mode == "A Little More Brain Power":
        num_questions = 20
        st.title("20 zufällige Fragen")
    else:
        num_questions = 10
        st.title("10 zufällige Fragen")
    df = df.sample(frac=1).reset_index(drop=True)
    question_list = df.sample(
        n=min(num_questions, len(df)), random_state=None
    ).to_dict(orient="records")
    st.session_state["random_questions"] = question_list
    st.session_state["user_answers"] = {}
    st.session_state["current_question_index"] = 0

if "Fragen_Parasitologie_df" in st.session_state:
    df = st.session_state["Fragen_Parasitologie_df"]

    if st.button("Quiz starten"):
        start_quiz(df)

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

        # Speichere die Antwort immer, auch wenn sie leer ist
        st.session_state["user_answers"][current_index] = {
            "question": question["question"],
            "correct_answer": question["correct_answer"],
            "user_answer": user_answer if user_answer else ""
        }

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
                if st.button("Auswertung anzeigen"):
                    # Speichere die aktuelle Antwort auf die letzte Frage (nochmal redundant, aber sicher)
                    st.session_state["user_answers"][current_index] = {
                        "question": question["question"],
                        "correct_answer": question["correct_answer"],
                        "user_answer": user_answer if user_answer else ""
                    }

                    correct_count = 0
                    incorrect_count = 0
                    incorrect_questions = []

                    for i in range(total_questions):
                        answer_data = st.session_state["user_answers"].get(i)
                        if not answer_data:
                            continue
                        if answer_data["user_answer"] == answer_data["correct_answer"]:
                            correct_count += 1
                        else:
                            incorrect_count += 1
                            incorrect_questions.append(answer_data)

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
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    user = st.session_state.get("name", "Unbekannt")
                    quiz_mode = st.session_state.get("quiz_mode", "Low Brain Power")

                    for idx, answer_data in st.session_state["user_answers"].items():
                        # Falls answer_data None ist, verwende leere Werte
                        if not answer_data:
                            answer_data = {
                                "question": f"Frage {idx}",
                                "user_answer": "",
                                "correct_answer": ""
                            }

                        record = {
                            "timestamp": timestamp,  # Gleicher Timestamp für alle Antworten
                            "user": user,
                            "question": answer_data.get("question", ""),
                            "user_answer": answer_data.get("user_answer", ""),
                            "correct_answer": answer_data.get("correct_answer", ""),
                            "quiz_mode": quiz_mode
                        }

                        try:
                            DataManager().append_record(
                                session_state_key="data_df",
                                record_dict=record
                            )
                        except Exception as e:
                            st.error(f"Fehler beim Speichern der Antwort: {e}")

                    st.success("Alle Antworten wurden gespeichert.")