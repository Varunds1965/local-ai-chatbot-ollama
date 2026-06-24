import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Chatbot")
st.markdown(
    "Ask me anything and get AI-powered responses."
)

user_input = st.text_input("Enter your question")
ask = st.button("Ask")

if ask and user_input:
    try:
        st.write("Sending question to Groq...")

        llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            groq_api_key=os.getenv("GROQ_API_KEY"),
            temperature=0
        )

        response = llm.invoke(user_input)

        st.write("Received response from Groq.")
        st.markdown("### Response")
        st.markdown(response.content)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")