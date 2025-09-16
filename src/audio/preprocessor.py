import ffmpeg
import numpy as np
import src.utils.utils as utils
import noisereduce as nr
from scipy.signal import butter, sosfilt
import src.errorhandling.audioerrors as audioerror

def test_preprocessor(video_path):
    audio = extract_audio_raw(video_path)
    # utils.plot_waveform_with_peaks(audio)
    denoised_audio = denoise_raw_audio(audio)
    bandpassed_audio = bandpass_audio(denoised_audio)
    final_audio = normalize_raw_audio(bandpassed_audio)
    # utils.plot_waveform_with_peaks(final_audio)
    
    return final_audio, find_clipping_sec(final_audio)[0]


def extract_audio_raw(path):
    ffmpeg_output, _ =  (
        ffmpeg.input(path)
        .output("pipe:", format="s16le", acodec="pcm_s16le", ac=1, ar="16000")
        .run(capture_stdout=True, capture_stderr=True)
    )
    audio = np.frombuffer(ffmpeg_output, np.int16).astype(np.float32)
    if audio.size == 0:
        raise audioerror.empty_audio_buffer()
    return audio


def normalize_raw_audio(raw_audio): 
    if raw_audio.size == 0:
        raise audioerror.empty_audio_buffer()
    min_val = np.min(raw_audio)
    max_val = np.max(raw_audio)

    normalized_audio = 2 * (raw_audio - min_val) / (max_val - min_val) - 1
    return normalized_audio

def denoise_raw_audio(raw_audio):
    if raw_audio.size == 0:
        raise audioerror.empty_audio_buffer()
    if not np.all(np.isfinite(raw_audio)):
        raise audioerror.buffer_as_inf_values()
    if len(raw_audio) < 2048:
        raise audioerror.audio_buffer_too_small()
    return nr.reduce_noise(y=raw_audio, sr=16000)


def bandpass_audio(audio, sr=16000, low=80, high=7600):
    if audio.size == 0:
        raise audioerror.empty_audio_buffer()
    sos = butter(4, [low, high], btype='band', fs=sr, output='sos')
    filtered_audio = sosfilt(sos, audio)
    return filtered_audio


# find clipping timestamp, return sec
def find_clipping_sec(audio, threshold = 0.99):
    if audio.size == 0:
        raise audioerror.empty_audio_buffer()
    peaks_idx = np.where(np.abs(audio) >= threshold)[0]
    return peaks_idx / 16000
