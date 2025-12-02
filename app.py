import streamlit as st
import google.generative_ai as genai

st.set_page_config(page_title="Mój Asystent", page_icon="🤖")

st.title("Cześć Olek! 🤖")

api_key = st.text_input("Podaj klucz API:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        pytanie = st.chat_input("Napisz coś...")
        
        if pytanie:
            st.chat_message("user").write(pytanie)
            with st.spinner('Myślę...'):
                response = model.generate_content(pytanie)
                st.chat_message("ai").write(response.text)
    except Exception as e:
        st.error(f"Błąd: {e}")
