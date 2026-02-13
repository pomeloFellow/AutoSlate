import src.core.core as core
from src.utils.utils import log
from tkinter import filedialog
import src.gui.logic.ProgressReport as pr
import threading

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

def progress_page_shown(state):
    # set up progress
    progressreport = pr.ProgressReport()
    state.progress_report = progressreport

    def on_progress(percent, stage):
        state.root.after(0, lambda: update_ui(state, percent, stage))

    progressreport.on_progress = on_progress

    # start work
    worker_thread = threading.Thread(
        target=relabel_videos,
        args=(state,),
        daemon=True
    )
    worker_thread.start()


def update_ui(state, percent, stage):
    state.progress_bar_value.set(percent)
    log("Progress Value: " + str(percent))

    match stage:
        case pr.ProgressReport.Stage.FIN_EXTRACT:
            state.progress_text.set("Finished extracting audio.")

        case pr.ProgressReport.Stage.FIN_PREPROCESS:
            state.progress_text.set("Finished cleaning audio.")

        case pr.ProgressReport.Stage.FIN_TRANSCRIBE:
            state.progress_text.set("Finished transcribing audio.")

        case pr.ProgressReport.Stage.FIN_RENAME:
            state.progress_text.set("Finished renaming file.")

    
def relabel_videos(state):
    log("UI Relabel Process Started")
    folder_path_str = state.folder_path.get()
    start_time = state.start_time.get()
    min_time = state.min_time.get()
    min_confidence = state.min_confidence.get()
    progress_report = state.progress_report

    log("folder: " + str(folder_path_str))
    log("start_time: " + str( start_time))
    log("min_time: " + str(min_time))
    log("min_confidence: " + str(min_confidence))

    # need to pass progress report to use callback

    core.relabel_videos(folder_path_str, progress_report, start_time, min_time, min_confidence)


