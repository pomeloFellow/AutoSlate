import src.utils.utils as util
import src.audio.preprocessor as preprocessor
import src.audio.transcriber as transcriber

def get_text_from_audio(video_path, ismp4):
    """Gets text based on audio from video from path

    Args:
        video_path (PosixPath): video path to grab text with
        ismp4 (bool): _description_

    Returns:
        string: String from whisper
        float: confidence from 0 to 1, 1 being 100%
    """
    audio = None
    clip_time = 0
    if (ismp4):
        audio, clip_time = preprocessor.test_preprocessor(video_path)
    whisper_result = transcriber.transcribe(audio, clip_time)
    confidence = transcriber.total_weighted_audio_confidence(whisper_result)
    audio_text = transcriber.get_text(whisper_result)
    return audio_text, confidence