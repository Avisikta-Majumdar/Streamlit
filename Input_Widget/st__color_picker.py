import streamlit as st
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

# st.color_picker(label: str, value: Optional[str] = None, key ) :- Display a color picker widget.
# Source :- https://docs.streamlit.io/library/api-reference/widgets/st.color_picker