import streamlit as st


if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

# st.button(label: str, key, ...)  --> Display a Button widget
# Source :- https://docs.streamlit.io/library/api-reference/widgets/st.button