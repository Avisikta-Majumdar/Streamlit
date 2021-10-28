import streamlit as st

add_contact = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email-Id", "Home phone", "Mobile phone")
)
add_dept = st.sidebar.selectbox(
    "Please enter ur dept ",
    ("CSE", "ECE", "ME" , "CE")
)

st.write("# ****Your details ****\n")
st.write(f"#### We will connect with U using your {add_contact}")
st.write(f"#### Your deprartment is :- {add_dept}")


# sidebar is Not only can you add interactivity to your report with widgets,
#you can organize them into a sidebar with **st.sidebar.[element_name].**
#Each element that's passed to st.sidebar is pinned to the left, allowing users to focus on the content in your app

