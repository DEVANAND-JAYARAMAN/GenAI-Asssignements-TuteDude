import streamlit as st
st.title("Welcome to Streamlit!")
name = st.text_input("Enter Your Name here to greet: ")
if st.button("Greet Me"):
    st.write("Hello,", name + "!, Welcome to our page")