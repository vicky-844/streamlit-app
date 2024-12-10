import streamlit as st
from calculate_numbers import calculate_life_path_number
from calculate_numbers import calculate_destiny_number
from calculate_numbers import calculate_personality_number
from hugging_chat_connection import generate_response

st.set_page_config(page_title="My Numerology App",
                   page_icon="✨")


st.title("My Numerology App")

if 'lifepath_count' not in st.session_state:
    st.session_state.lifepath_count = 0

if 'destiny_count' not in st.session_state:
    st.session_state.destiny_count = 0

if 'personality_count' not in st.session_state:
    st.session_state.personality_count = 0

def activate_lifepath():
    st.session_state.lifepath_count = 1
    st.session_state.destiny_count = 0
    st.session_state.personality_count = 0

def activate_destiny():
    st.session_state.destiny_count = 1
    st.session_state.lifepath_count = 0
    st.session_state.personality_count = 0

def activate_personality():
    st.session_state.personality_count = 1
    st.session_state.lifepath_count = 0
    st.session_state.destiny_count = 0

with st.chat_message("user"):
    st.write("Hello Human! What would you like me to calculate?")
    c1, c2, c3 = st.columns(3)
    with c1:
        life_path = st.button("Life Path Number", on_click=activate_lifepath)
    with c2:
        destiny = st.button("Destiny Number", on_click=activate_destiny)
    with c3:
        personality = st.button("Personality Number", on_click=activate_personality)


if st.session_state.lifepath_count == 1:
    with st.chat_message("user"):
        dob = st.date_input("When is Your Birthday?", value=None)
        if dob:
            life_path_number = calculate_life_path_number(dob)
            st.write(f"Your life path number is {life_path_number}")
            prompt = st.chat_input("What would you like to know about your life path number?")
            if prompt:
                with st.spinner("Thinking"):
                    result = generate_response(prompt)
                    st.write(result)

if st.session_state.destiny_count == 1:
    with st.chat_message("user"):
        full_name = st.text_input("What is Your full name?")
        if full_name:
            destiny_number = calculate_destiny_number(full_name)
            st.write(f"Your destiny number is {destiny_number}")
            prompt2 = st.chat_input("Enter prompt here")
            if prompt2:
                with st.spinner("Thinking"):
                    result = generate_response(prompt2)
                    st.write(result)


if st.session_state.personality_count == 1:
    with st.chat_message("user"):
        pers = st.text_input("What is your full name?")
        if pers:
            personality_number = calculate_personality_number(pers)
            st.write(f"Your personality number is {personality_number}")
            prompt3 = st.chat_input("Enter prompt here")
            if prompt3:
                with st.spinner("Thinking"):
                    result = generate_response(prompt3)
                    st.write(result)
