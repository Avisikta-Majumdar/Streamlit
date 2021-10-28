import streamlit as st

number = st.number_input('Insert a number' , value = 19)
st.write('The current number is ', number)


# st.number_input(label , min_value , max_value , value , step):- Display a numeric input widget.
# Source :- https://docs.streamlit.io/library/api-reference/widgets/st.number_input