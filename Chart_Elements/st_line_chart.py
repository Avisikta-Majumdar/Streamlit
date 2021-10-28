import streamlit as st
import pandas as pd

x=[10,15,20,25,30,35,40,45,50]
seriesx=pd.Series(x)
st.write(seriesx)
st.line_chart(seriesx,width=1000 , height = 500)

y=[i-10 for i in x]
seriesy=pd.Series(y)
st.write(seriesy)
st.line_chart(seriesy,width=1000 , height = 500)

# st.line_chart(data=None, width=0, height=0, use_container_width=True)  --> Display a line chart .
# Source --> https://docs.streamlit.io/library/api-reference/charts/st.line_chart
