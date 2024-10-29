import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage

load_dotenv()


def reponse (user):
    return("im not trained yet")



# app config
st.set_page_config(page_title="Chatbot-WebMaster", page_icon="wolf")
st.title("Chatbot-WebMaster :wolf:")

# chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
    AIMessage(content="hello, how can I help you !!")
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


# aconversation
for msg in st.session_state.chat_history:
    if isinstance(msg,AIMessage):
        with st.chat_message("AI"):
            st.write(msg.content)

    elif isinstance(msg,HumanMessage):
        with st.chat_message("Human"):
            st.write(msg.content)
