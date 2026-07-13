import os
import tempfile

import streamlit as st

from rag import build_vectorstore
from rag import get_answer

st.set_page_config(page_title="ChatGroq RAG")
st.title("ChatGroq RAG Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "retriever" not in st.session_state:
    st.session_state.retriever = None

uploaded_file = st.file_uploader("Upload PDF",type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp:
        tmp.write(uploaded_file.read())
        pdf_path = tmp.name

    if st.button("Process Document"):
        with st.spinner("Creating Vector Database..."):
            st.session_state.retriever = build_vectorstore(pdf_path)
        st.success("Document processed successfully!")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input("Ask a question")

if question:
    st.session_state.messages.append({"role":"user","content":question})
    with st.chat_message("user"):
        st.write(question)

    if st.session_state.retriever:
        answer = get_answer(question,st.session_state.retriever)
    else:
        answer = "Please upload a PDF first."

    st.session_state.messages.append({"role":"assistant","content":answer})

    with st.chat_message("assistant"):
        st.write(answer)


#use this command to run the app
#python -m streamlit run app.py