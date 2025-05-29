import streamlit as st
import requests

st.title("RAG Chatbot...")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", key="input")

if st.button("Send") and user_input:
    response = requests.post("http://localhost:8000/api/chat/", json={"message": user_input})
    bot_response = response.json().get("response", "Something went wrong.")

    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", bot_response))

for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")
