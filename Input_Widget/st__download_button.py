import streamlit as st
import pandas as pd

st.title("Example 1:- Download a large DataFrame as a CSV:")
@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')
my_large_df = pd.read_csv('iris.csv')


csv = convert_df(my_large_df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='iris.csv',
    mime='text/csv' )

st.title("Example 2:- Download a string as a file:")
text_contents = '''I am learning Streamlit'''
st.download_button('Download this txt file', text_contents)


st.title("Example 3:- Download an image:")
with open("sunrise.png", "rb") as file:
    btn = st.download_button(
    label="Download image",
    data=file,
    file_name="flower.png",
    mime="image/png")

# st.download_button(label, data, file_name)--> Display a download button widget.
#  Source :- https://docs.streamlit.io/library/api-reference/widgets/st.download_button