import streamlit as st
from utils import get_llm

st.title("💬 Chatbot")

llm = get_llm()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history ABOVE the input
for role, message in st.session_state.messages:
    with st.chat_message("user" if role == "You" else "assistant"):
        st.write(message)

# Use chat_input for a better UX (sticks to bottom, clears on send)
user_input = st.chat_input("Ask something...")

if user_input:
    # Append and immediately render the user message
    st.session_state.messages.append(("You", user_input))
    with st.chat_message("user"):
        st.write(user_input)

    # Build message history for the LLM
    history = []
    for role, content in st.session_state.messages[:-1]:  # exclude latest
        history.append({
            "role": "user" if role == "You" else "assistant",
            "content": content
        })
    history.append({"role": "user", "content": user_input})

    # Stream or invoke with a spinner
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = llm.invoke(history)
            st.write(response.content)

    st.session_state.messages.append(("Bot", response.content))