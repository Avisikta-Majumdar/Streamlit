import streamlit as st


start_loc, end_loc = st.select_slider(
        'Select your Initial Journey to Destination',
        options=[' Howrah' , 'Kharagpur' , 'Yashvantpur' , 'Hassan'],
        value=('Kharagpur', 'Yashvantpur'))
st.write('You selected journey between', start_loc, 'and', end_loc)

# st.select_slider(label  options , value(optional) ) -->Display a slider widget to select items from a list.
#  Source :- https://docs.streamlit.io/library/api-reference/widgets/st.select_slider