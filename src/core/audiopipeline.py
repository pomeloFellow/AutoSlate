import src.audio.preprocessor as preprocessor
import src.audio.transcriber as transcriber
import src.gui.logic.ProgressReport as pr

import braw_extension as braw

def get_text_from_audio(video_path, ismp4, progress_report, start_time = 0, min_time = -1):
    """Gets text based on audio from video from path

    Args:
        video_path (PosixPath): video path to grab text with
        ismp4 (bool): if audio file is mp4 or braw
        start_time: time to start transcription
        min_time: minimum time to transcribe

    Returns:
        string: String from whisper
        float: confidence from 0 to 1, 1 being 100%
    """
    if (ismp4):
        raw_audio = preprocessor.MP4_extract_raw_audio(video_path)
    else:
        raw_audio = braw.BRAW_extract_raw_audio(str(video_path))
    
    curr_stage = pr.ProgressReport.Stage.FIN_EXTRACT
    progress_report.update_progress(curr_stage)
    progress_report.on_progress(progress_report.percent, curr_stage)

    audio = preprocessor.preprocess_audio(raw_audio)
    end_time = preprocessor.find_end_time(audio, min_time)

    if end_time <= start_time: # end earlier than start - not allowed ADD ERROR HANDLING
        return None
    
    curr_stage = pr.ProgressReport.Stage.FIN_PREPROCESS
    progress_report.update_progress(curr_stage)
    progress_report.on_progress(progress_report.percent, curr_stage)

    whisper_result = transcriber.transcribe(audio, end_time, start_time)

    confidence = transcriber.total_weighted_audio_confidence(whisper_result)
    audio_text = transcriber.get_text(whisper_result)

    curr_stage = pr.ProgressReport.Stage.FIN_TRANSCRIBE
    progress_report.update_progress(curr_stage)
    progress_report.on_progress(progress_report.percent, curr_stage)

    return audio_text, confidence