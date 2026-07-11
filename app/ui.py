import streamlit as st
from core.llm_logic import ask_bot

st.set_page_config(page_title="RAG Bot", page_icon="🤖")
st.title("🤖 DataScience RAG Bot")
st.caption("Ask me anything about [Hands-On Machine Learning] by Aurélien Géron.")

query = st.text_input("Enter your question:")

if st.button("Submit"):
    if query:
        with st.spinner("Bot is thinking..."):
            try:
                answer = ask_bot(query)
                st.success("Response:") 
                st.markdown(answer)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please type a question first.")