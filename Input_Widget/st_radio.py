import streamlit as st
genre = st.radio("What's your favorite movie genre",
                  ('Comedy', 'Drama', 'Documentary'))
if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")



# st.radio( label , options ):- Display a radio button widget.(Can select only 1 option)
# label :- What's your favorite movie genre
# options :- Comedy, Drama , Documentary
# Source :- https://docs.streamlit.io/library/api-reference/widgets/st.radio