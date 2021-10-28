import streamlit as st
import pandas as pd
from io import StringIO

st.title("Insert a file uploader that accepts a single file at a time ")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)


st.title("Insert a file uploader that accepts multiple files at a time:")
uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

# st.file_uploader(label , type: , accept_multiple_files: False ) :- Display a file uploader widget.
#  Source :- https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader
