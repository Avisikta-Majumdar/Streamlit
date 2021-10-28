import streamlit as st

st.title("st.slider(label , min_value , max_value , value , step , format)")


st.write("Example 1:-")
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

st.write("Example 2:-")
values = st.slider(
        'Select a range of values',
        0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

st.write("Example 3:- This is a range time slider: ")
from datetime import time , datetime
appointment = st.slider(
        "Schedule your appointment:",
        value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

st.write("Example 4:- Finally, a datetime slider:")
start_time = st.slider(
        "When do you start?",
        value=datetime(2020, 1, 1, 9, 30),
        format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)


# st.slider(label: str, min_value=None, max_value=None, value=None, step=None, format=None) :- Display a slider widget.
# Source:- https://docs.streamlit.io/library/api-reference/widgets/st.slider