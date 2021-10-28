import streamlit as st

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)
# st.text_input(label , value) :- Display a single-line text input widget.
# Source :- https://docs.streamlit.io/library/api-reference/widgets/st.text_input