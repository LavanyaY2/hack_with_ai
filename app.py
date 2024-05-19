import audio_to_txt
import streamlit as st

from pydub import AudioSegment

audio = AudioSegment.from_wav('test_audio.wav')
response = audio_to_txt.convert_audio(audio)
st.write(response)