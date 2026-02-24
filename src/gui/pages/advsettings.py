from tkinter import ttk
import tkinter as tk
import src.gui.logic.logic as logic
from src.gui.components.starttimesetting import StartTimeSetting
from src.gui.components.endtimesetting import EndTimeSetting
from src.gui.components.confidencesetting import ConfidenceSetting

class AdvSettingsPage(ttk.Frame):
    def __init__(self, parent, state, to_progress_bar):
        super().__init__(parent)
        self.state = state

        self.grid(row=0, column=0, sticky="nsew")

        for i in range(3):
            weight = 10 if i == 1 else 1
            self.grid_rowconfigure(i, weight=weight)
            self.grid_columnconfigure(i, weight=weight)

        inner_frame = ttk.Frame(self)
        inner_frame.grid(row=1, column=1, sticky="nsew")
        inner_frame.columnconfigure(0, weight=1)

        # Folder Button
        folder_button = ttk.Button(
            inner_frame,
            textvariable=state.folder_button_text,
            command=lambda: logic.browse_folder(state)
        )
        folder_button.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        # settings frame
        settings_frame = ttk.Frame(inner_frame)
        settings_frame.grid(row=1, column=0, sticky="ew")
        settings_frame.columnconfigure(0, weight=1)

        # settings
        StartTimeSetting(settings_frame, state)
        EndTimeSetting(settings_frame, state)
        ConfidenceSetting(settings_frame, state)
        
        # process button
        ttk.Button(
            inner_frame,
            text="Relabel Videos",
            command=to_progress_bar
        ).grid(row=2, column=0, sticky="ew", pady=(0, 10))