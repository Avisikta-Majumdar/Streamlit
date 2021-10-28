import streamlit as st

st.title("st.selectbox")
option = st.selectbox( 'How would you like to be contacted?',('Email', 'Home phone', 'Mobile phone') )
st.write('You selected:', option)


# st.selectbox(label, options) :-  Display a select widget.
# Source:-https://docs.streamlit.io/library/api-reference/widgets/st.selectbox