import streamlit as st

st.write("**Python code example**")
Pcode = '''def hello():
     print("Hello, Streamlit!")'''

st.code(Pcode, language='python')



st.write("**C code example**")
Ccode = '''#include <stdio.h>
int main() {
    printf("Hello world");
    return 0;
}
'''
st.code(Ccode , language='c')




# st.code(code , language )  --> Display a code block with optional syntax highlighting.
# code -->  The string to display as code.
# language  -->  The language that the code is written in, for syntax highlighting. If omitted, the code will be unstyled.
