import openai
import streamlit as st


with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/htrangn/ItsTrangNguyen/blob/main/pages/Chatbot.py)"
activities = ["Chat", "About"]
choice = st.sidebar.selectbox("Select Activity", activities)

if choice == "Chat":
    st.title("💬 Chatbot")
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
    
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])
    
    if prompt := st.chat_input():
        if not openai_api_key:
            st.info("Please add your OpenAI API key to continue.")
            st.stop()
    
        openai.api_key = openai_api_key
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
        msg = response.choices[0].message
        st.session_state.messages.append(msg)
        st.chat_message("assistant").write(msg.content)
elif choice == "About":
     st.subheader("About this app")
     st.write("This app was made by Nguyen H.Trang")
     st.write("This app requires an OpenAI API key to activate")
     st.write("This chatbot is designed to deliver a seamless conversational experience with its natural language processing capabilities")
