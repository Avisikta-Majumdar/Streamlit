import streamlit as st
st.write('Hello World')

Input_name = st.text_input("Enter your name:- ")
st.title("Your name is ",Input_name)