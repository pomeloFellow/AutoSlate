# core util.logic
import src.utils.utils as util
import src.filesys.files as fs
import src.core.audiopipeline as ap
from pathlib import Path

def relabel_videos(input, start_time=0, min_time=-1, min_confidence=-1):
    """Relabels input videos

    Args:
        input (string): video or directory path
        start_time (int, optional): Time to start transcription. Defaults to 0.
        min_time (int, optional): Minimum time to end transcription. Defaults to -1.
        min_confidence (int, optional): Minimum confidene allowed. Defaults to -1.
    """
    # check if input_folder is directory
    util.log(input)

    input_path = Path(input).expanduser().resolve(strict=False)

    if input_path.is_file():
        util.log("Goes to is file")
        process_video(input_path, start_time, min_time, min_confidence)
    elif input_path.is_dir():
        util.log("Goes to is dir")
        video_files = list(input_path.rglob("*"))
        util.log(video_files)
        for file_path in video_files:
            if file_path.suffix.lower() in {".mp4", ".braw"}:
                util.log("Is mp4 or braw")
                process_video(file_path, start_time, min_time, min_confidence)

def process_video(video_path, start_time, min_time, min_confidence):
    """Processes a single video

    Args:
        video_path (string): video path
        start_time (int, optional): Time to start transcription. Defaults to 0.
        min_time (int, optional): Minimum time to end transcription. Defaults to -1.
        min_confidence (int, optional): Minimum confidene allowed. Defaults to -1.

    Returns:
        bool: success
    """
    util.log("In processes_video")
    isMP4 = True if video_path.suffix == ".mp4" else False
    # get audio info (label, confidence)
    
    audio_text, confidence = ap.get_text_from_audio(video_path, isMP4, start_time, min_time)
    if min_confidence != -1 and confidence < min_confidence:
        util.log("Did not reach min confidence.")
        util.log(f"Avg confidence: {confidence}")
        return False

    # get video info (label, confidence)

    # relabel video
    new_label = fs.text_to_file_name(audio_text)
    fs.rename_video(video_path, new_label + video_path.suffix)
    return True