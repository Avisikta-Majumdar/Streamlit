import streamlit as st
import datetime

d = st.date_input(
    "When's your birthday",
    datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)

# st.date_input(label , value , min_value , max_value ) :- Display a date input widget.
#  Source :- https://docs.streamlit.io/library/api-reference/widgets/st.date_input