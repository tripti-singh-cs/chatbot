# from langchain_mistralai import ChatMistralAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

def get_llm():

    llm = ChatGroq(
        # model="open-mistral-nemo",
        model="openai/gpt-oss-20b",
        temperature=0.7,
        groq_api_key=os.getenv("GROQ_API_KEY")
    )

    return llm