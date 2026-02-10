from src.core.core import relabel_videos
from src.utils.utils import log
from tkinter import filedialog

def browse_folder(state):
    folder = filedialog.askdirectory()
    if folder:
        state.folder_path.set(folder)
        update_folder_button_text(state)

def update_folder_button_text(state):
    path = state.folder_path.get()
    if path:
        state.folder_button_text.set(path)
    else:
        state.folder_button_text.set("File / Folder")

def relabel_videos(state):
    folder_path_str = state.folder_path.get()
    start_time = state.start_time.get()
    min_time = state.min_time.get()
    min_confidence = state.min_confidence.get()

    log("folder: " + str(folder_path_str))
    log("start_time: " + str( start_time))
    log("min_time: " + str(min_time))
    log("min_confidence: " + str(min_confidence))

    # relabel_videos(folder_path_str, start_time, min_time, min_confidence)


