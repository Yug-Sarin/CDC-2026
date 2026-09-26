import streamlit as st
import ollama 

st.title("SoundSafe")
st.caption("Please note that the data used is self-reported. This is NOT a diagnosis. Additionally, AI responses can contain mistakes.")

if "music_recommender" not in st.session_state:
    st.session_state["music_recommender"] = "music_recommender"


if "messages" not in st.session_state:
    st.session_state.messages = []

#if "is_processing" not in st.session_state:
#    st.session_state.is_processing = False

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#if not st.session_state.is_processing:
if prompt := st.chat_input("What is up?"):
  st.session_state.messages.append({"role": "user", "content": prompt})
  
  with st.chat_message("user"):
    st.markdown(prompt)
    #st.session_state.is_processing = True

    with st.spinner("AI is thinking..."):
      response = ollama.chat(model="music_recommender", messages=st.session_state.messages, stream=True)
      
    with st.chat_message("assistant"):
      full_response = st.write_stream((chunk['message']['content'] for chunk in response))
      st.session_state.messages.append({"role": "assistant", "content": full_response})
      #st.session_state.is_processing = False



    
