import ffmpeg
import numpy as np
import src.utils.utils as utils
import noisereduce as nr
from scipy.signal import butter, sosfilt

def test_preprocessor(video_path):
    audio = extract_audio_raw(video_path)
    utils.plot_waveform_with_peaks(audio)
    denoised_audio = remove_audio_noise(audio)
    bandpassed_audio = bandpass_audio(denoised_audio)
    final_audio = normalize_raw_audio(bandpassed_audio)
    utils.plot_waveform_with_peaks(final_audio)
    find_clipping_sec(final_audio)


def extract_audio_raw(path):
    ffmpeg_output, _ =  (
        ffmpeg.input(path)
        .output("pipe:", format="s16le", acodec="pcm_s16le", ac=1, ar="16000")
        .run(capture_stdout=True, capture_stderr=True)
    )
    audio = np.frombuffer(ffmpeg_output, np.int16).astype(np.float32)
    return audio


def normalize_raw_audio(raw_audio): 
    min_val = np.min(raw_audio)
    max_val = np.max(raw_audio)

    normalized_audio = 2 * (raw_audio - min_val) / (max_val - min_val) - 1
    return normalized_audio

def remove_audio_noise(raw_audio):
    return nr.reduce_noise(y=raw_audio, sr=16000)


def bandpass_audio(audio, sr=16000, low=80, high=7600):
    sos = butter(4, [low, high], btype='band', fs=sr, output='sos')
    filtered_audio = sosfilt(sos, audio)
    return filtered_audio


# find clipping timestamp, return sec
def find_clipping_sec(audio, threshold = 0.99):
    peaks_idx = np.where(np.abs(audio) >= threshold)[0]
    return peaks_idx / 16000
