import streamlit as st

st.title("Example 2")
st.write("""
# Header1
## Header2
### Header3
#### Header4
##### Header5
###### Header6""")



#1. st.title('') --> This is used to set the title
# 2. st.write("Write anything") --> To write something we have to use .write method
#          In this write function we can use heading as well like we have 5 lines to write and
#          1st line will have header1(Single hash ( # ) )
#          2nd line will have header2(Double hash ( ## ) )
#        3rd line will have header3(Triple hash ( ### ) )
#         4th line will have header4( #### )
#         5th line will have header1( ##### )
#         6th line will have header1( ###### )
