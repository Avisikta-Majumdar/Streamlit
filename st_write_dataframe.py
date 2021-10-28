import streamlit as st
import pandas as pd
data_frame = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40],
 })
st.write('**Making DataFrame (Pandas)**')

st.write('Below is a DataFrame:', data_frame, 'Above is a dataframe.')