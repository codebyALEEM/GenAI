import streamlit as st
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

# Background Image 
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(to bottom, rgba(0,0,0,0.5), rgba(0,0,0,0.3)), 
                    url("https://wallpapers.com/images/hd/robot-background-s0kq5o0tyixpq6c1.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)


#  API Keys 
os.environ["GOOGLE_API_KEY"] = "Add your Gemini API Key"   
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "Add your Langchain API Key" #For LangSmith tracking

# Streamlit UI 
st.set_page_config(page_title="Gemini AI Chatbot", page_icon="🤖")

st.title("     | 🤖 Smart AI Chatbot 🤖 | ")
st.write("Type your question below and the chatbot will respond using the Gemini model.")


#Prompt Template 
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI chatbot created by Aleem. Provide clear and accurate answers."),
        ("user", "Question: {question}")
    ]
)


# Gemini LLM 
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",  
    temperature=0.7,
    max_output_tokens=512
)

output_parser = StrOutputParser()

# Build pipeline
chain = prompt | llm | output_parser


# User Input 
input_text = st.text_input("Ask me anything:")


#Run Chat
if input_text:
    with st.spinner("Thinking..."):
        response = chain.invoke({"question": input_text})
    st.success(response)


