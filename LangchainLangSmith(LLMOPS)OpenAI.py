import streamlit as st
import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI  


#API Keys
os.environ["OPENAI_API_KEY"] = "Add your OpenAI key"          # <-- 
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "Add your LangChain API key"   # <-- Replace with your real key

#Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "I am a chatbot. I am here to assist you. Please type your queries."),
        ("user", "Question: {question}")
    ]
)

#Streamlit UI
st.title("| 🤖 Smart AI Chatbot 🤖 | ")
input_text = st.text_input("How may I help you?")

#OpenAI LLM
llm = ChatOpenAI(
    model="gpt-4.1",   # or "gpt-4o-mini" for faster response
    temperature=0.2
)

output_parser = StrOutputParser()

# Pipeline
chain = prompt | llm | output_parser

#Run Chat
if input_text:
    st.write(chain.invoke({"question": input_text}))
