from tkinter import ttk
import src.gui.logic as logic

class StartPage(ttk.Frame):
    def __init__(self, parent, state):
        super().__init__(parent)

        self.state = state

        self.grid_columnconfigure(0, weight=1)

        fd_button = ttk.Button(
            self,
            textvariable=state.folder_button_text,
            command=lambda: logic.browse_folder(state)
        )

        relabel_button = ttk.Button(
            self,
            text="Relabel Videos",
            command=lambda: logic.relabel_videos(state)
        )

        adv_button = ttk.Button(
            self,
            text="Advanced Settings"
        )

        fd_button.grid(row=0, column=0, sticky="ew", pady=(0, 10))
        relabel_button.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        adv_button.grid(row=2, column=0, sticky="ew")
