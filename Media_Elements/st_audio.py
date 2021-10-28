import streamlit as st
audio_file = open('Iphone.mp3', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/mp3')

# st.audio(data, format='audio/wav', start_time=0)  -->  Display an audio player
# Source :- https://docs.streamlit.io/library/api-reference/media/st.audio