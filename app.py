import audio_to_txt
import streamlit as st

from pydub import AudioSegment
import pandas as pd
from io import StringIO, BytesIO
from st_audiorec import st_audiorec


st.header(":wave: Welcome to VoiceNotes!", divider = "rainbow")

container = st.container(border=True)
container.write("Tired of reading large documents trying to retain all that information? :confounded: ")
container.write("VoiceNotes is a tool to help you summarize those long text blobs for you.")
container.write("Upload an audio file or record audio and let us do the hardwork :wink: ")

# define session state for button clicks
if 'button' not in st.session_state:
    st.session_state.button = None

col1, col2 = st.columns(2, gap="small")
with col1:
    if st.button("Upload a file"):
        st.session_state.button = "upload"
with col2:
    if st.button("Record audio"):
        st.session_state.button = "record"

if st.session_state.button == "upload":
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        st.write("File Uploaded Succesfully")
        audio = AudioSegment.from_file(BytesIO(bytes_data), format = "wav")
        response = audio_to_txt.convert_audio(audio)
        st.write(response)

elif st.session_state.button == "record":
    wav_audio_data = st_audiorec()
    if wav_audio_data is not None:
        st.audio(wav_audio_data, format='audio/wav')
        audio = AudioSegment.from_file(BytesIO(wav_audio_data), format = "wav")
        response = audio_to_txt.convert_audio(audio)
        st.write(response)




