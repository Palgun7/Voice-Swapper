import sounddevice as sd
import soundfile as sf
import streamlit as st
import time

st.set_option('deprecation.showPyplotGlobalUse',False)
st.header("1. Record your own voice")

filename = st.text_input("Choose a filename: ")

def record_audio(duration):
    # Set audio parameters
    channels = 1
    sample_rate = 44100
    
    # Start recording
    st.write(f"Recording audio for {duration} seconds...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)
    sd.wait() # Wait for the recording to finish
    
    # Save audio file
    with st.spinner("Saving audio file..."):
        file_name = f"{filename}.wav"
        sf.write(file_name, audio_data, sample_rate)
        st.success(f"Audio saved to {file_name}")

# Streamlit app
def app():
    st.title("Audio Recorder")
    duration = st.slider("Recording duration (seconds)", 1, 10, 5)
    if st.button("Record"):
        record_audio(duration)

if __name__ == "__main__":
    app()