import ffmpeg
import numpy as np
import src.utils.utils as utils
import noisereduce as nr
from scipy.signal import butter, sosfilt
import src.errorhandling.audioerrors as audioerror

def preprocess_audio(raw_audio):
    denoised_audio = denoise_raw_audio(raw_audio)
    bandpassed_audio = bandpass_audio(denoised_audio)
    final_audio = normalize_raw_audio(bandpassed_audio)
    # utils.plot_waveform_with_peaks(final_audio)
    return final_audio


def MP4_extract_raw_audio(path):
    ffmpeg_output, _ =  (
        ffmpeg.input(path)
        .output("pipe:", format="s16le", acodec="pcm_s16le", ac=1, ar="16000")
        .run(capture_stdout=True, capture_stderr=True)
    )
    audio = np.frombuffer(ffmpeg_output, np.int16).astype(np.float32)
    if audio.size == 0:
        raise audioerror.EmptyAudioBuffer()
    return audio


def normalize_raw_audio(raw_audio): 
    if raw_audio.size == 0:
        raise audioerror.EmptyAudioBuffer()
    min_val = np.min(raw_audio)
    max_val = np.max(raw_audio)

    normalized_audio = 2 * (raw_audio - min_val) / (max_val - min_val) - 1
    return normalized_audio

def denoise_raw_audio(raw_audio):
    if raw_audio.size == 0:
        raise audioerror.EmptyAudioBuffer()
    if not np.all(np.isfinite(raw_audio)):
        raise audioerror.BufferHasInfValues()
    if len(raw_audio) < 2048:
        raise audioerror.AudioBufferTooSmall()
    return nr.reduce_noise(y=raw_audio, sr=16000)


def bandpass_audio(audio, sr=16000, low=80, high=7600):
    if audio.size == 0:
        raise audioerror.EmptyAudioBuffer()
    sos = butter(4, [low, high], btype='band', fs=sr, output='sos')
    filtered_audio = sosfilt(sos, audio)
    return filtered_audio


# find clipping timestamp, return sec
def find_clipping_sec(audio, threshold = 0.99):
    if audio.size == 0:
        raise audioerror.EmptyAudioBuffer()
    peaks_idx = np.where(np.abs(audio) >= threshold)[0]
    return peaks_idx / 16000

def find_length_sec(audio, sample_rate=16000):
    return len(audio) / sample_rate

def find_end_time(audio, min_time):
    utils.log("Enters find_end_time")
    end_time = None
    if min_time == -1: # use clip_time
        end_time = find_clipping_sec(audio)[0]
        utils.log(f"Checks clip_time @ {end_time}")
    elif min_time == -2: # use full length
        utils.log("Checks full length")
        end_time = find_length_sec(audio)
    else: # use min_time
        clip_time = find_clipping_sec(audio)[0]
        if min_time >= clip_time: # min later than clip time
            audio_length = find_length_sec(audio)
            if audio_length < min_time: 
                end_time = audio_length
            else:
                end_time = min_time
        else:
            end_time = clip_time

        utils.log(f"Uses min_time @ {min_time}")
    return end_time