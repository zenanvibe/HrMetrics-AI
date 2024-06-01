import streamlit as st
import requests,json
from audio_recorder_streamlit import audio_recorder as st_audio_recorder

ai_server = "http://127.0.0.1:8001/"

# Title
st.title("Leave Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def process_promt(prompt):
    # Display user message in chat message container
    with st.chat_message("user"):
        prompt = 'Context: '+prompt
        st.markdown(prompt)
    with st.chat_message("system"):   
        try:
            mes = json.loads(requests.post(f"{ai_server}leave/common?querry={prompt}").text)['response'].replace('\n', '  \n')
        except:
            mes = "Unable to get message from server!"
        st.markdown(mes)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages.append({"role": "system", "content": mes})

if "audio_message" not in st.session_state:
    st.session_state.audio_message = ""

with st.sidebar:
    col1, col2,col3 = st.columns([1,2, 1])
    with col2:
        recorded_audio = st_audio_recorder(key="audio_recorder",text='Speak',neutral_color="#ffffff")
        if st.session_state.audio_recorder:
            with open("out.mp3","wb") as f:
                f.write(recorded_audio)
            files = {"file": ("out.mp3", open("out.mp3","rb"), "audio/mpeg")}
            response = requests.post(ai_server+"audio", files=files)
            if response.status_code == 200:
                mess = json.loads(response.text)['text']
                st.session_state.audio_message = mess
            else:
                print("Error")

# Audio Message
if st.session_state.audio_message :
    process_promt(st.session_state.audio_message)
    del st.session_state.audio_message 

# Chat Input Box
if prompt:= st.chat_input("Your message...",key='input_text'):
    process_promt(prompt)