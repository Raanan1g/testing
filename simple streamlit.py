# simple_app.py
import streamlit as st

# 1. Title and text
st.title("My First Super Simple App")
st.write("Hello, world! This app does very little.")

# 2. A text input box
name = st.text_input("What's your name?", "friend")

# 3. Greet the user
st.write(f"Hello, {name}!")

# 4. Add a slider
st.header("Now for a slider...")
x = st.slider("Select a number to square", 0, 10, 3) # min, max, default
st.write(f"The number {x} squared is {x * x}")