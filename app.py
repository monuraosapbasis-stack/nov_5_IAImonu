import streamlit as st

st.title("Hello, Streamlit!")
st.write("Welcome to your first Streamlit app.")
st.write("You clicked the button!" if st.button("Click me!") else "Button not clicked yet.")
st.write("This is a simple app to demonstrate Streamlit functionality.")
