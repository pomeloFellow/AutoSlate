from tkinter import filedialog

def browse_folder(state):
    folder = filedialog.askdirectory()
    if folder:
        state.folder_path.set(folder)
        update_folder_button_text(state)

def relabel_videos(state):
    folderpath_str = state.folder_path.get()
    print("Folderpath:", folderpath_str)

def update_folder_button_text(state):
    path = state.folder_path.get()
    if path:
        state.folder_button_text.set(path)
    else:
        state.folder_button_text.set("File / Folder")
