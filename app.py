import audio_to_txt
import streamlit as st

from pydub import AudioSegment
import pandas as pd
from io import StringIO, BytesIO

st.button("Upload a file")
uploaded_file = st.file_uploader("Choose a file")
    
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    st.write("File Uploaded Succesfully")
    audio = AudioSegment.from_file(BytesIO(bytes_data), format = "wav")
    response = audio_to_txt.convert_audio(audio)
    st.write(response)
# st.button("Upload a file", type="primary")
