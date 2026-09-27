import streamlit as st
import ollama 

st.set_page_config(page_title="SoundSafe")

st.sidebar.header("SoundSafe")

st.title("SoundSafe")
st.caption("Please note that the data used is self-reported. This is NOT a diagnosis. Additionally, AI responses can contain mistakes.")


if "music_recommender" not in st.session_state:
    st.session_state["music_recommender"] = "music_recommender"


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

    with st.spinner("AI is thinking..."):
      response = ollama.chat(model="music_recommender", messages=st.session_state.messages, stream=True)

    with st.chat_message("assistant"):
      full_response = st.write_stream((chunk['message']['content'] for chunk in response))

      st.session_state.messages.append({"role": "assistant", "content": full_response})