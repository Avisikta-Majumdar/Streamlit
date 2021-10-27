import streamlit as st
from PIL import Image
image = Image.open('sunrise.png')
st.image(image, caption='Sunrise by the mountains')

# st.image()  --> Display an image or list of images.
# Source :- https://docs.streamlit.io/library/api-reference/media/st.image