import streamlit as st
import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

 
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "Add your Langchain API Key" #For LangSmith tracking



## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","I am chatbot. I am hear to assist you. Please type your queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title(' | 🤖 Smart AI Chatbot 🤖 | OLLAMA')
input_text=st.text_input("I am chatbot. How may I help you")

#Ollama (Mistral Model)
llm=Ollama(model="mistral:latest")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))