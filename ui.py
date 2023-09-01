import streamlit as st
from ui_utils import check_password
from text_to_quizz import txt_to_quizz
import json

import asyncio

st.title("Generate questions from text!")

def build_question(count, json_question):

    if json_question.get(f"question") is not None:
        st.write("Question: ", json_question.get(f"question", ""))
        choices = ['A', 'B', 'C', 'D']
        selected_answer = st.selectbox(f"Choose your answer:", choices, key=f"select_{count}")
        for choice in choices:
            choice_str = json_question.get(f"{choice}", "None")
            st.write(f"{choice} {choice_str}")
                    
        color = ""
        if st.button("Submit", key=f"button_{count}"):
            rep = json_question.get(f"reponse")
            if selected_answer == rep:
                color = ":green"
                st.write(f":green[Good answer: {rep}]")
                st.ballons()
                
            else:
                color = ":red"
                st.write(f":red[Wrong answer. The correct answer is {rep}].")                

        st.write(f"{color}[Your answer: {selected_answer}]")  

        count += 1

    return count

# Upload PDF file
# uploaded_file = st.file_uploader(":female-student:", type=["pdf"])
txt = st.text_area('Type the text from which you want to generate the quiz')

if st.button("Generate Quiz", key=f"button_generer"):
    if txt is not None:
        with st.spinner("Quiz generation..."):
            st.session_state['questions'] = asyncio.run(txt_to_quizz(txt))
            st.write("Quiz generated successfully!")

if ('questions' in st.session_state):
    # Display question
    count = 0
    for json_question in st.session_state['questions']:

        count = build_question(count, json_question)
        
   
