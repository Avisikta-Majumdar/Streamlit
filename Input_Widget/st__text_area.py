import streamlit as st
txt = st.text_area('Text to analyze', '''
                        It was the best of times, it was the worst of times, it was
                        the age of wisdom, it was the age of foolishness, it was
                        the epoch of belief, it was the epoch of incredulity, it
                        was the season of Light, it was the season of Darkness, it
                        was the spring of hope, it was the winter of despair, (...)
     ''')
st.write('Sentiment:', txt)
# st.text_area(label , value , height , max_chars  , key) :- Display a multi-line text input widget.
#  Source :- https://docs.streamlit.io/library/api-reference/widgets/st.text_area