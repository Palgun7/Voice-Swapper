import gradio as gr
import sounddevice as sd
import soundfile as sf
import os
import subprocess

PATH__ = "./recordings/"
#IMAGE_PATH = r"C:\Users\Praveen\Desktop\Project Expo\peter.jpg"

def record_audio(filename):
    duration = 3  # Duration of recording in seconds
    sample_rate = 44100  # Sampling rate of audio
    channels = 1  # Number of audio channels (mono)

    # Start recording audio
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)

    # Wait for recording to finish
    sd.wait()

    new_path = os.path.join(PATH__,filename+".wav")
    # Save recording to file
    sf.write(new_path, recording, sample_rate)
    #calling the preprocess
    preprocess_path = "Project Expo\tm1_peter_preprocessed"
    pathb = new_path
    weight_path = "Project Expo\epoch14_weights"
    output_path = "Project Expo\outputs"
    subprocess.Popen(f'python ./test.py --mceps_dir {preprocess_path} --test_dir {pathb} --weight_dir {weight_path} --output_dir {output_path}', shell=True)
    return f"Recording saved as {new_path}"

audio_recorder = gr.Interface(
    fn=record_audio,
    inputs=gr.inputs.Textbox(label="Enter a filename to save the recorded audio as .wav file"),
    outputs="text",
    title="Voice Swapper",
    description="Enter a filename and then click submit to start the recording.",
    theme="light",
    
)

audio_recorder.launch()
