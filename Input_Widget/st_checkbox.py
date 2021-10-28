import streamlit as st

st.title("HS passing year")
P2018 = st.checkbox("You are 2018 HS Passout")
P2019 = st.checkbox("You are 2019 HS Passout")
other = st.checkbox("Currently studing in class 12")
result = st.button('Submit')
if result and P2018:
    st.write("So you're 2018 passout")
elif result and P2019:
    st.write("So you're 2019 passout")
elif result & other:
    st.write("All the best for ur HS exam")


# st.checkbox(label) :- Display a checkbox widget.(We can select multiple checkbox also).
# Source :- https://docs.streamlit.io/library/api-reference/widgets/st.checkbox