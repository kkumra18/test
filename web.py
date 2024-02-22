import streamlit as st

st.title("This is my todo app")
st.text("This is a pragraph")
st.info("Info tag")
st.checkbox(label="Test chekboxes")
st.checkbox(label="Item 2")

x = ["item 1", "item 2", "item 3", "item 4"]

[st.checkbox(label=i) for i in x]

