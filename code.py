import streamlit as st

st.title("FACE DETECTION APP")
activities = ["Detection","About"]
choice = st.sidebar.selectbox("Select Activity", activities)
