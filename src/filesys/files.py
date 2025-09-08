# file maniputlation
from pathlib import Path
from src.utils.utils import log


def is_dir(folder_path):
    """Returns if folder_path is a directory

    Args:
        folder_path (string): name of folder holding videos to relabel

    Returns:
        bool: if folder_path is a directory
    """
    p = Path(folder_path)
    isDir = p.is_dir()
    if isDir:
        log(folder_path + " found")
        return True
    else:
        log(folder_path + " not found")
        return False


def video_paths_in_folder(folder_path):
    """Returns array of posix paths of .mp4 videos in folder_path dir

    Args:
        folder_path (string): name of folder holding videos to relabel

    Returns:
        array: array of posix paths of .mp4 videos
    """
    p = Path(folder_path)
    video_paths = list(p.glob('**/*.mp4'))
    return video_paths


def rename_video(old_video_path, new_video_name):
    """Renames video

    Args:
        old_video_path (PosixPath): PosixPath of video to rename
        new_video_name (string): new name of video (needs .mp4 suffix)

    Returns:
        bool: success or failure
    """
    new_file_path = old_video_path.parent / new_video_name
    old_video_path.rename(new_file_path)
    return True