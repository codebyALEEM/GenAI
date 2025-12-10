import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chat_models import init_chat_model

if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"]="enter_api_key"
    
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.3,
    max_output_tokens=100
    )

    
def chat_with_ai():
    print("Gemini Conversational Assistant (LangChain)")
    print("Type 'exit' to stop.\n")
    
    while(True):
        user_input=input("You:")
        
        if user_input.lower() in ["exit","quit"]:
            print("Chatbot: GoodBye!")
            break
        
        responce=model.invoke(user_input)
        print("Chatbot:",responce.content)
        print()
        
if __name__ == "__main__":
    chat_with_ai()