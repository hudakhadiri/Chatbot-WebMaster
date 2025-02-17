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



if website_url is None or website_url == "":
    st.info("Please enter a website URL")

else:
    # session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            AIMessage(content="Hello, I am a bot. How can I help you?"),
        ]

    # user input
    user_query = st.chat_input("Type your message here...")
    if user_query is not None and user_query != "":
        response = reponse(user_query)
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        st.session_state.chat_history.append(AIMessage(content=response))
        

    # conversation
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.write(message.content)
