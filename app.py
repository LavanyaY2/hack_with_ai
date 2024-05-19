import audio_to_txt
import txt_to_notes
import streamlit as st

from pydub import AudioSegment
import pandas as pd
from io import StringIO, BytesIO
from st_audiorec import st_audiorec
import json

file_path = "input_audio.txt"
summary_str = ""

st.header("👋 Welcome to VoiceNotes!", divider = "rainbow")

container = st.container(border=True)
container.write("Tired of reading large documents trying to retain all that information? 😖 ")
container.write("VoiceNotes is a tool to help you summarize those long text blobs for you.")
container.write("Upload an audio file or record audio and let us do the hardwork 😉 ")

# define session state for button clicks
if 'button' not in st.session_state:
    st.session_state.button = None

result_str = ""
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
        transcript = response.results[0].alternatives[0].transcript
        result_str = f'Transcript: {transcript}'
        col3, col4 = st.columns(2, gap="small")
        with col3:
            if st.button("Give me a short summary"):
                st.session_state.button = "short_summary"
        with col4:
            if st.button("Summarize based on sub-sections"):
                st.session_state.button = "sub_sections"

        if st.session_state.button == "sub_sections":
            with open(file_path, 'r') as f:
                toread = f.read()
                f.close()
                summary = txt_to_notes.notarize(toread)
                st.write(summary)
                summary_str = f'Summary: {summary}'
                st.download_button('Download Text File', summary_str)

elif st.session_state.button == "record":
    wav_audio_data = st_audiorec()
    if wav_audio_data is not None:
        st.audio(wav_audio_data, format='audio/wav')
        audio = AudioSegment.from_file(BytesIO(wav_audio_data), format = "wav")
        response = audio_to_txt.convert_audio(audio)
        transcript = response.results[0].alternatives[0].transcript
        result_str = f'Transcript: {transcript}'

        col3, col4 = st.columns(2, gap="small")
        with col3:
            if st.button("Give me a short summary"):
                st.session_state.button = "short_summary"
        with col4:
            if st.button("Summarize based on sub-sections"):
                st.session_state.button = "sub_sections"

        if st.session_state.button == "sub_sections":
            with open(file_path, 'r') as f:
                toread = f.read()
                f.close()
                summary = txt_to_notes.notarize(toread)
                st.write(summary)
                summary_str = f'Summary: {summary}'
                st.download_button('Download Text File', summary_str)

with open(file_path, "w") as f:
    f.write(result_str)
