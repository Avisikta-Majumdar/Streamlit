import streamlit as st
st.title("st.multiselect")
options = st.multiselect('What are your favorite colors',
                         ['Green', 'Yellow', 'Red', 'Blue'],
                       )

st.write('You selected:', options)

#st.multiselect(label , options) --> Display a multiselect widget.
#  Source :-https://docs.streamlit.io/library/api-reference/widgets/st.multiselect