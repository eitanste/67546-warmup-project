from pathlib import Path
import streamlit as st

import numpy as np
import matplotlib.pyplot as plt

import librosa
import librosa.display

import os
import soundfile as sf

# LOAD AUDIO

def load_audio(path):
    y, sr = librosa.load(path)

    st.audio(y, format='audio/wav', sample_rate=sr)

# SPECTROGRAM

def spec(y):
    D = librosa.stft(y,n_fft=2048, hop_length=256)  # STFT of y
    S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
    fig, ax = plt.subplots(sharex=True, figsize=(9,4))
    librosa.display.specshow(S_db, ax=ax)

    st.pyplot(fig)


# ALL SAMPLES CHART
def plot_all_samples(meta_dir_path):
    """
        ADD CODE HERE
        Total aggregation function - operates on all the samples in the directory, and provides insight about the dataset as a whole.
    """
    pass


# ALL UPLOADED SAMPLES CHART
def plot_all_uploaded_samples(meta_file_paths):
    """
        ADD CODE HERE
        Aggregation function - operates on all the uploaded samples, and provides insight about the selected samples.
    """
    pass

# SAMPLE CHART
def plot_sample(meta_file_path):
    """
        ADD CODE HERE
        Operator function - operates on an individual sample and displays an interesting property of the sample.
    """
    pass
    

meta_info_dir_path = 'META_INFO_DIR_PATH' # CHANGE TO DIR PATH

plot_all_samples(meta_info_dir_path)

# FILE UPLOADER
uploaded_files = st.sidebar.file_uploader("Choose a wav file", type='wav', accept_multiple_files=True)
if uploaded_files:

    meta_files_paths = [os.path.join(meta_info_dir_path, Path(uploaded_file.name).stem + '.txt')
                            for uploaded_file in uploaded_files]
    plot_all_uploaded_samples(meta_files_paths)

    for uploaded_file in uploaded_files:
        st.title(uploaded_file.name)
        st.audio(uploaded_file, format='audio/wav')
        
        arr, samplerate = sf.read(uploaded_file)
        spec(arr)

        file_stem = Path(uploaded_file.name).stem
        meta_info_file_path = os.path.join(meta_info_dir_path,file_stem + '.txt')
        plot_sample(meta_info_file_path)
