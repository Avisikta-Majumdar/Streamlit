import streamlit as st
import datetime

t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)

# st.time_input(label , value , key , help , on_change ) :- Display a time input widget.
#  Source :- https://docs.streamlit.io/library/api-reference/widgets/st.time_input