from pathlib import Path
import streamlit as st

import os


# ALL SAMPLES CHART
def plot_all_samples(meta_dir_path):
    pass


# ALL UPLOADED SAMPLES CHART
def plot_all_uploaded_samples(meta_file_paths):
    pass

# SAMPLE CHART
def plot_sample(meta_file_path):
    pass
    

meta_info_dir_path = 'META_INFO_DIR_PATH' # CHANGE TO DIR PATH

plot_all_samples(meta_info_dir_path)

# FILE UPLOADER
uploaded_files = st.sidebar.file_uploader("Choose a wav file", type=['png','jpg'], accept_multiple_files=True)
if uploaded_files:

    meta_files_paths = [os.path.join(meta_info_dir_path, Path(uploaded_file.name).stem + '.txt')
                            for uploaded_file in uploaded_files]
    plot_all_uploaded_samples(meta_files_paths)

    for uploaded_file in uploaded_files:

        st.title(uploaded_file.name)
        file_stem = Path(uploaded_file.name).stem
        st.image(uploaded_file)

        file_stem = Path(uploaded_file.name).stem
        meta_info_file_path = os.path.join(meta_info_dir_path,file_stem + '.txt')
        plot_sample(meta_info_file_path)
