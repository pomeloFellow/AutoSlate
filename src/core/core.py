# core util.logic
import src.utils.utils as util
import src.filesys.files as fs
import src.audio.preprocessor as preprocessor
import src.audio.transcriber as transcriber
import src.core.audiopipeline as ap

def relabel_videos(input_folder):
    # check if input_folder is directory
    util.log(input_folder)
    fs.is_dir(input_folder)

    # make array of video posixpaths
    video_paths = fs.video_paths_in_folder(input_folder)
    util.log(video_paths)

    # for every video path
    # assumes video_paths_in_folder() "checks" files are videos
    for video_path in video_paths:
        isMP4 = True if video_path.suffix == ".mp4" else False
        # get audio info (label, confidence)
        audio_text, confidence = ap.get_text_from_audio(video_path, isMP4)

        # get video info (label, confidence)

        # relabel video
        new_label = fs.text_to_file_name(audio_text)
        fs.rename_video(video_path, new_label + video_path.suffix)