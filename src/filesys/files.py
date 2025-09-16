# file maniputlation
from pathlib import Path
from src.utils.utils import log
import src.errorhandling.fserrors as fserror
import re
import word2number as w2n


def is_dir(folder_path):
    """Returns if folder_path is a directory

    Args:
        folder_path (string): name of folder holding videos to relabel

    Returns:
        bool: if folder_path is a directory
    """
    p = Path(folder_path)
    if not p.is_dir():
        raise fserror.DirNotFoundError(p)
    
    log(f"{folder_path} found")
    return True



def video_paths_in_folder(folder_path):
    """Returns array of posix paths of .mp4 videos in folder_path dir

    Args:
        folder_path (string): name of folder holding videos to relabel

    Returns:
        array: array of posix paths of .mp4 videos
    """
    p = Path(folder_path)
    video_paths = list(p.glob('**/*.mp4'))
    if not video_paths:
        raise fserror.NoVideosInDirError(p)
    else:
        return video_paths

def convert_part(s):
    s = s.strip()
    # Handle "point X"
    if "point" in s:
        parts = s.split("point")
        whole = parts[0].strip()
        frac = parts[1].strip()
        try:
            whole_num = int(whole) if whole.isdigit() else w2n.word_to_num(whole)
        except:
            whole_num = whole
        try:
            frac_num = int(frac) if frac.isdigit() else w2n.word_to_num(frac)
        except:
            frac_num = frac
        return f"{whole_num}.{frac_num}"
    else:
        try:
            return str(w2n.word_to_num(s)) if not s[0].isdigit() else s
        except:
            return s

def text_to_file_name(text):
    clean_text = re.sub(r"[.,]", "", text.lower())

    pattern = r"scene\s+(.+?)\s+shot\s+(.+?)\s+take\s+(.+)"
    match = re.search(pattern, clean_text)
    if not match:
        return None
    
    scene_str, shot_str, take_str = match.groups()

    scene = convert_part(scene_str)
    shot = convert_part(shot_str)
    take = convert_part(take_str)
    
    scene = scene.zfill(3) if scene.replace('.', '').isdigit() else scene
    shot = shot.zfill(3) if shot.replace('.', '').isdigit() else shot
    take = take.zfill(3) if take.replace('.', '').isdigit() else take
    
    return f"S{scene}_SH{shot}_TK{take}"



def rename_video(old_video_path, new_video_name):
    """Renames video

    Args:
        old_video_path (PosixPath): PosixPath of video to rename
        new_video_name (string): new name of video (needs .mp4 suffix)

    Returns:
        bool: success or failure
    """
    if not old_video_path.exists():
        raise fserror.FileNotFoundError(old_video_path)
    
    new_file_path = old_video_path.parent / new_video_name
    if new_file_path.exists():
        raise fserror.FileAlreadyExistsError(new_file_path)
    if not new_video_name.endswith(".mp4"):
        raise fserror.NotMP4Error(new_file_path)
    
    old_video_path.rename(new_file_path)
    return True