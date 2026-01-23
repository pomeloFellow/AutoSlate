import numpy as np
import whisper as whisper
import math
import src.utils.utils as utils

# whisper
def transcribe(audio, end_time, start_time=0):
    """Uses whisper to transcribe audio numpy buffer from start to endtime

    Args:
        audio (numpy float32 buffer): Buffer holding audio information
        end_time: Time to transcribe till
        start_time: Time to start transcription

    Returns:
        string: transcription
    """
    start_sec = start_time
    end_sec = end_time
    start_sample = int(start_sec * 16000)
    end_sample = int(end_sec * 16000)
    audio_slice = audio[start_sample:end_sample].astype(np.float32)
    model = whisper.load_model("base")
    result = model.transcribe(audio_slice,
                              fp16=False,
                              language='en',
                              initial_prompt='Speaker is saying the scene, shot, and take of the video')
    lower_case_result = result["text"].lower()

    if "scene" not in lower_case_result or "shot" not in lower_case_result or "take" not in lower_case_result:
        utils.log("Whisper result: " + lower_case_result)
        raise ValueError("Unable to get all information (scene, shot, take)")
    
    return result

def total_weighted_audio_confidence(whisper_result):
    """Calculates the weighted avg log probability of all whisper_result segments that contains "scene" "shot" "take"

    Args:
        whisper_result (dict): dict result from whisper transcription

    Returns:
        float: "Confidence" from 0 to 1, 1 being 100% confidence
    """
    segments = whisper_result.get("segments", [])
    if not segments:
        return 0.0 
    
    keywords = {"shot", "scene", "take"}

    filtered_segments = [
        seg for seg in segments
        if any(word in seg.get("text", "").lower() for word in keywords)
    ]

    if not filtered_segments:
        return 0.0
    
    weighted_sum = 0.0
    total_duration = 0.0
    for seg in filtered_segments:
        duration = seg["end"] - seg["start"]
        total_duration += duration
        weighted_sum += seg["avg_logprob"] * duration

    avg_logprob = weighted_sum / total_duration

    confidence = math.exp(avg_logprob)
    return confidence

def get_text(whisper_result):
    """ Returns text from whisper result

    Args:
        whisper_result (dict): Result from whisper translation

    Returns:
        string: Text transcribed by whisper_result
    """
    text = whisper_result.get('text', None)
    if not text:
        raise KeyError("No text key in whisper result")
    return text
