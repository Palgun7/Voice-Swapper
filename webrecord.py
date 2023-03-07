import streamlit as st
from audio_recorder_streamlit import audio_recorder
#import plotly.express as px

st.set_option('deprecation.showPyplotGlobalUse',False)

st.write("""
# Voice Swapper App
This website enables the user to record their own voice and be able to synthesise it into the target speakers voice.
""")

audio_bytes = audio_recorder(
  energy_threshold=(-1.0, 1.0),
  pause_threshold=3.0,
)
if audio_bytes:
    test_audio = st.audio(audio_bytes, format="audio/wav")
    
#st.write(audio_bytes)