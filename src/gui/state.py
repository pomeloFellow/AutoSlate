import tkinter as tk

class AppState:
    def __init__(self):
        self.folder_path = tk.StringVar()
        self.folder_button_text = tk.StringVar(value="File / Folder")
