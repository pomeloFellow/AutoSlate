# core logic
from src.utils.utils import log
from src.filesys.files import is_dir, video_paths_in_folder, rename_video

def relabel_videos(input_folder):
    # check if input_folder is directory
    is_dir(input_folder)

    # make array of video posixpaths
    video_paths = video_paths_in_folder(input_folder)
    log(video_paths)

    # for every video path
    for video_path in video_paths:
        # get audio info (label, confidence)
        # get video info (label, confidence)

        # relabel video
        new_label = "newlabel2.mp4"
        rename_video(video_path, new_label)