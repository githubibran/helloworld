import streamlit as st

user_input = st.text_input("Enter Prompt:")
st.write('User Entered : ', user_input)