import streamlit as st
import pandas as pd
import numpy as np

st.title("Bar chart")

chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)

# st.bar_chart(data=None, width=0, height=0, use_container_width=True) --> Display a Bar chart
# Source --> https://docs.streamlit.io/library/api-reference/charts/st.bar_chart