import streamlit as st
from dotenv import load_dotenv



load_dotenv()



# app config
st.set_page_config(page_title="Chat with websites", page_icon="🤖")
st.title("Chat with websites")

# sidebar
with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Website URL")

st.chat_input("Enter votre text ...")
