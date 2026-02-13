import tkinter as tk

class AppState:
    def __init__(self, root):
        super().__init__()
        self.root = root

        # folder/file
        self.folder_path = tk.StringVar()
        self.folder_button_text = tk.StringVar(value="File / Folder")

        # relabeling args
        self.start_time = tk.DoubleVar(value=0.0) # default: start at 0.00
        self.min_time = tk.DoubleVar(value=-1.0) # default: end @ first audio peak
        self.min_confidence = tk.DoubleVar(value=-1.0) # default: no min

        # progress
        self.progress_bar_value = tk.IntVar()
        self.progress_text = tk.StringVar()
        self.progress_report = None

