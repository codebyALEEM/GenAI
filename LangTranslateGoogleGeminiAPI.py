import os
import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

# ------------------ Background Image ------------------
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(to bottom right, #1E90FF, #4682B4);
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Ensure API key is set (better to set in environment before running)
if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = "use_your_api_key"

# Initialize Gemini model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0)

# Streamlit UI
st.title("🌐 Language Translator (Gemini)")

# User input text
user_text = st.text_area(
    "Enter English text to translate:",
    "how are you team working on langchain with google gemini model?"
)

# Language selection
languages = [
    "Marathi", "Hindi", "Telugu", "Tamil", "French",
    "Spanish", "German", "Arabic", "Japanese", "Chinese"
]
target_lang = st.selectbox("Select target language:", languages)

# Translate button
if st.button("Translate"):
    messages = [
        SystemMessage(content=f"Translate the following from English into {target_lang} language"),
        HumanMessage(content=user_text)
    ]
    
    # Invoke Gemini
    response = model.invoke(messages).content
    
    # Display result
    st.subheader(f"Translation in {target_lang}:")
    st.write(response) 