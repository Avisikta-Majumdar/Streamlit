import streamlit as st

video_file = open('star.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)

# st.video(data, format='video/mp4', start_time=0) --> Display a video player.
# Source :- https://docs.streamlit.io/library/api-reference/media/st.video