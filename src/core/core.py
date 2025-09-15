# core util.logic
import src.utils.utils as util
from src.filesys.files import is_dir, video_paths_in_folder, rename_video
import src.audio.audioprocessor as audioprocessor

def relabel_videos(input_folder):
    # check if input_folder is directory
    is_dir(input_folder)

    # make array of video posixpaths
    video_paths = video_paths_in_folder(input_folder)
    util.log(video_paths)

    # for every video path
    # assumes video_paths_in_folder() "checks" files are videos
    for video_path in video_paths:
        # get audio info (label, confidence)
        audioprocessor.test_audioprocessor(video_path)

        # get video info (label, confidence)

        # relabel video
        new_label = "newlabel2.mp4"
        rename_video(video_path, new_label)