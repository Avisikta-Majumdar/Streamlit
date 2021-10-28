import streamlit as st

st.write("**The formulae is **")
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
   \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

# st.latex(str)  -->  Display mathematical expressions formatted as LaTeX.
# Source :- https://docs.streamlit.io/library/api-reference/text/st.latex