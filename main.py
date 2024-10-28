import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage

load_dotenv()


def reponse (user):
    return("im stupid")



# app config
st.set_page_config(page_title="Chatbot-WebMaster", page_icon="🤖")
st.title("Chatbot-WebMaster :wolf:")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
    AIMessage(content="hello stupid , how can I help you !!")
]

# sidebar
with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Website URL")

user = st.chat_input("Enter votre text ...")

if user is not None and user !="" :
    reply = reponse(user)
    st.session_state.chat_history.append(HumanMessage(content=user))
    st.session_state.chat_history.append(AIMessage(content=reply))


