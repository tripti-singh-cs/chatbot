from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
import os

load_dotenv()

def get_llm():

    llm = ChatMistralAI(
        model="mistral-large-latest",
        temperature=0.7,
        mistral_api_key=os.getenv("MISTRAL_API_KEY")
    )

    return llm