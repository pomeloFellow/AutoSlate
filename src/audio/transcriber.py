import src.audio.preprocessor as preprocessor
import numpy as np
import whisper as whisper
import math

# whisper
def transcribe(audio, clipping_time):
    start_sec = 0.0
    end_sec = clipping_time
    start_sample = int(start_sec * 16000)
    end_sample = int(end_sec * 16000)
    audio_slice = audio[start_sample:end_sample].astype(np.float32)
    model = whisper.load_model("base")
    result = model.transcribe(audio_slice,
                              fp16=False,
                              language='en',
                              initial_prompt='Speaker is saying the scene, shot, and take of the video')
    return result

def total_audio_confidence(whisper_result):
    segments = whisper_result.get("segments", [])
    if not segments:
        return 0.0 

    weighted_sum = 0.0
    total_duration = 0.0
    for seg in segments:
        duration = seg["end"] - seg["start"]
        total_duration += duration
        weighted_sum += seg["avg_logprob"] * duration

    avg_logprob = weighted_sum / total_duration

    confidence = math.exp(avg_logprob)
    return confidence

def get_text(whisper_result):
    return whisper_result.get('text', None)
